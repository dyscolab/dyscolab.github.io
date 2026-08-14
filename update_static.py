#!/usr/bin/env python3

""" 
Script to create static html sites from documentation notebooks in dyscolab-tutorials. 
Configure output and notebbok directories from notebook_directories.toml.
"""
from pathlib import Path
import subprocess
import tomllib


CONFIG_FILE = Path("notebook_directories.toml")


def load_config(path: Path) -> tuple[list[Path], Path]:
    with path.open("rb") as f:
        config = tomllib.load(f)

    notebook_dirs = [Path(directory) for directory in config["notebook_dirs"]]
    output_dir = Path(config["output_dir"])

    return notebook_dirs, output_dir


def export_notebook(
    notebook_path: Path,
    notebook_dir: Path,
    output_dir: Path,
) -> bool:
    relative_path = notebook_path.relative_to(notebook_dir)
    output_path = output_dir / relative_path.with_suffix(".html")

    output_path.parent.mkdir(parents=True, exist_ok=True)

    print(f"Exporting {notebook_path} -> {output_path}")

    try:
        subprocess.run(
            [
                "marimo",
                "export",
                "html",
                str(notebook_path),
                "-o",
                str(output_path),
                "--force",
                "--no-sandbox",
            ],
            check=True,
        )
        return True

    except subprocess.CalledProcessError as error:
        print(
            f"ERROR: Failed to export {notebook_path} "
            f"(exit code {error.returncode})"
        )
        return False


def main() -> None:
    notebook_dirs, output_dir = load_config(CONFIG_FILE)

    notebooks = []

    for notebook_dir in notebook_dirs:
        notebooks.extend(
            (notebook_dir, path)
            for path in notebook_dir.rglob("*.py")
        )

    successful = 0
    failed = []

    for notebook_dir, notebook in sorted(notebooks):
        if export_notebook(notebook, notebook_dir, output_dir):
            successful += 1
        else:
            failed.append(notebook)

    print()
    print(f"Exported: {successful}")
    print(f"Failed:   {len(failed)}")

    if failed:
        print("\nFailed notebooks:")
        for notebook in failed:
            print(f"  - {notebook}")


if __name__ == "__main__":
    main()