# /// script
# requires-python = ">=3.12"
# dependencies = ["build", "cibuildwheel==4.1.1", "scikit-build-core", "setuptools", "wheel"]
# ///

"""Build the two superdex-uni wheels into one wheelhouse.

    uv run tools/build_wheels.py --output wheelhouse           # publishable (cibuildwheel)
    uv run tools/build_wheels.py --output wheelhouse --fast    # local iteration (host tag)

Run from the repository root. Stages sources first, then builds
superdex-physics-uni and superdex-robotics-uni. Configuration lives in each
package's pyproject.toml; this script holds only the package list.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKAGES = ["superdex-physics-uni", "superdex-robotics-uni"]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--fast", action="store_true")
    args = parser.parse_args()

    sys.path.insert(0, str(ROOT / "tools"))
    import stage_sources

    stage_sources.stage()
    args.output.mkdir(parents=True, exist_ok=True)
    for package in PACKAGES:
        package_dir = ROOT / "packages" / package
        if args.fast:
            cmd = [
                sys.executable,
                "-m",
                "build",
                "--wheel",
                "--no-isolation",
                "--outdir",
                str(args.output),
                str(package_dir),
            ]
        else:
            cmd = [
                sys.executable,
                "-m",
                "cibuildwheel",
                "--output-dir",
                str(args.output),
                str(package_dir),
            ]
        print("+", " ".join(cmd), flush=True)
        subprocess.run(cmd, cwd=ROOT, check=True)


if __name__ == "__main__":
    main()
