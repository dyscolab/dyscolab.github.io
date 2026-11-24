---
hide:
  - navigation
---
# SimBio
<div class="grid cards" markdown>

- ![Example](images/simbio_example.svg){ align=left , width="400" } 
```py
from simbio import *
from simbio.reactions import *
import numpy as np

class Water(System):
    H2: Variable = initial(default=1)
    O2: Variable = initial(default=1)
    H2O: Variable = initial(default=0)

    creation = Synthesis(A=2 * H2, B=O2, AB=2 * H2O, rate=1)
    electrolysis = Dissociation(AB=2 * H2O, A=2 * H2, B=O2, rate=0.5)

sim = Simulator(Water)
sim.solve(save_at=np.linspace(0, 30, 1000)).to_dataframe().plot()
```
</div>
<div style="text-align:center;"><i>Water synthesis and <a href="https://en.wikipedia.org/wiki/Electrolysis">electrolysis</a> implemeneted in SimBio. </i></div>
SimBio is a Python-based package for simulation of Chemical Reaction Networks (CRNs). It extends [Poincare](https://github.com/dyscolab/poincare), a package for modelling dynamical systems. It's designed around:

- __Modularity__: SimBio is intended to create a layer to separate the actual declaration and simulation of models, allowing to easily switch between methods and compile to different backends (including [NumPy](https://numpy.org/) [Numba](https://numba.pydata.org/) and [JAX](https://docs.jax.dev/en/latest/)). The same model can be compiled for either ODE or stochastic simulation by changing a single line of code.
- __Composability__: models are composable, allowing for the combination of smaller systems to create larger ones; complex models can be broken up into more manageable parts.
- __Reproducibility__: it intends to be a centralized place for all information concerning models, making it easy to extract data about information and parameters and encouraging consistency between analytical formulations and numerical implementations. Models can also be imported directly from the [SBML](https://sbml.org/) format.

---
## Installation

Using [pixi](https://pixi.sh/latest/),
install from PyPI with:

```sh
pixi add --pypi simbio
```

or install the latest development version from GitHub with:

```sh
pixi add --pypi simbio@https://github.com/dyscolab/simbio.git
```

Otherwise,
use `pip` or your `pip`-compatible package manager:

```sh
pip install simbio  # from PyPI
pip install git+https://github.com/dyscolab/simbio.git  # from GitHub
```

### Agent skill

SimBio ships with the `dyscolab-modeling` agent skill, which teaches coding agents how to use Poincare, SimBio and Jablonski. It is downloaded with the library, but has to be added to your agent's skills folder separately.

In pixi projects, link it with [pixi skills](https://pixi.prefix.dev/dev/integration/extensions/pixi_skills/), so it updates together with the library:

```sh
pixi global install pixi-skills                   # once
pixi skills manage --backend claude --scope local  # or another agent's backend
```

In any other environment, copy it with the environment's Python, and run the command again after upgrading the library:

```sh
python -m poincare.skill install --dest .agents/skills   # or .claude/skills, ~/.codex/skills, ...
```

See [Agent skills](skills.md) for more details.

---
## Documentation
Documentation is structured as a series of interactive [marimo](https://marimo.io/) notebooks which cover basic and advanced topics. They can be ran in the browser either in a static or interactive version or by cloning the [dyscolab-tutorials](https://github.com/dyscolab/dyscolab-tutorials) repository to open them locally. For more information, see [Poincare's documentation](poincare.md#documentation).
### Basics
- **Getting started with SimBio**: the essentials necessary to simulate CNRs. [Interactive](https://marimo.app/github.com/dyscolab/dyscolab-tutorials/blob/main/simbio/getting_started_with_simbio.py) / [Static](static_notebooks/getting_started_with_simbio.html)
- **Implementing the repressilator in SimBio**: an example showing an implementation of the [repressilator](https://en.wikipedia.org/wiki/Repressilator) model in SimBio, including model definition by composition of smaller parts, simulation and parameter sweeps looking at how the period changes. [Interactive](https://marimo.app/https://github.com/dyscolab/dyscolab-tutorials/blob/main/simbio/repressilator.py) / [Static](static_notebooks/repressilator.html)
### Topic guides
- **Using volume in SimBio**: explains how to make models with volume using `Compartment` and represent variables which react to volume as `Species`, using either concentrations or absolute amounts. [Interactive](https://marimo.app/github.com/dyscolab/dyscolab-tutorials/blob/main/simbio/using_volume.py) / [Static](static_notebooks/using_volume.html)
- **Stochastic simulations**: how to simulate the same systems stochastically using the  [Gillespie algorithm](https://en.wikipedia.org/wiki/Gillespie_algorithm). [Static](static_notebooks/stochastic.html) *(stochastich simulations cannot be run online, to see the interactive version clone the [dyscolab-tutorials](https://github.com/dyscolab/dyscolab-tutorials) repository)*
- **Importing SBML models**: load models from [SBML](https://sbml.org/) files or the [BioModels](https://www.ebi.ac.uk/biomodels/) repository as SimBio systems, which can then be simulated and analysed like any other model. [Interactive](https://marimo.app/github.com/dyscolab/dyscolab-tutorials/blob/main/simbio/sbml.py) / [Static](static_notebooks/sbml.html)

---
## GitHub
SimBio is developed in it's [github repo](https://github.com/dyscolab/simbio).
