"""
Make the static notebook builds reproducible.

update_static.py puts this folder on PYTHONPATH when it exports the notebooks,
so Python imports this module at startup. It is not used anywhere else: the
notebooks and the pixi environments run as usual outside the build.

Two things change between builds otherwise, and neither reads a seed from the
environment:

- xarray's HTML repr gives its collapsible sections ids from uuid.uuid4().
- Stochastic simulations called without a seed use np.random.default_rng(None),
  which takes fresh entropy from the OS.

- marimo gives each UI element (tables, sliders, ...) a random-id from
  UIElement._random_seed, an unseeded random.Random.

All of them are replaced here with versions that start from a fixed seed.
Calls that pass their own seed are unaffected.
"""

import random
import uuid

SEED = 0

_uuid_rng = random.Random(SEED)


def _seeded_uuid4() -> uuid.UUID:
    return uuid.UUID(int=_uuid_rng.getrandbits(128), version=4)


uuid.uuid4 = _seeded_uuid4

try:
    import numpy as np
except ImportError:
    pass
else:
    _default_rng = np.random.default_rng
    _seed_sequence = np.random.SeedSequence(SEED)

    def _seeded_default_rng(seed=None):
        if seed is None:
            # Each unseeded call gets its own stream, as with OS entropy, but
            # the streams are the same in every build.
            seed = _seed_sequence.spawn(1)[0]
        return _default_rng(seed)

    np.random.default_rng = _seeded_default_rng
    np.random.seed(SEED)

try:
    from marimo._plugins.ui._core.ui_element import UIElement
except ImportError:
    pass
else:
    UIElement._random_seed = random.Random(SEED)
