#!/usr/bin/env python3

"""
Pre-push hook: build the static notebooks with the pixi environment set for
the current branch in notebook_directories.toml ([pre_push_envs]).
Branches not listed there skip the build.
"""
from pathlib import Path
import subprocess
import sys
import tomllib


CONFIG_FILE = Path("notebook_directories.toml")


def main() -> None:
    with CONFIG_FILE.open("rb") as f:
        envs = tomllib.load(f).get("pre_push_envs", {})

    branch = subprocess.run(
        ["git", "branch", "--show-current"],
        capture_output=True, text=True, check=True,
    ).stdout.strip()

    env = envs.get(branch)
    if env is None:
        print(f"No build environment set for branch '{branch}', skipping.")
        return

    print(f"Branch '{branch}': building static notebooks with env '{env}'")
    result = subprocess.run(["pixi", "run", "-e", env, "python", "update_static.py"])
    sys.exit(result.returncode)


if __name__ == "__main__":
    main()
