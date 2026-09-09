#!/usr/bin/env python3
"""Stage packaging inputs from the pinned vendor tree into packages/*.

Copies each facade package and the upstream license files into the package
directories (all gitignored), then applies the packaging-only renames listed
below. The vendored source itself is never modified.

Renames (error-message text only, no behavior change):
  - superdex/physics/_native_payload.py: distribution "superdex-physics" ->
    "superdex-physics-uni"; the fp64 sibling name is left untouched because this
    channel ships no fp64 package.
"""

from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VENDOR = ROOT / "vendor" / "project_superdex"

# package dir -> (facade source dir, upstream wheel dir holding LICENSE etc.)
PACKAGES = {
    "superdex-physics-uni": (
        VENDOR / "superdex_physics/wheels/superdex-physics/superdex",
        VENDOR / "superdex_physics/wheels/superdex-physics",
    ),
    "superdex-robotics-uni": (
        VENDOR / "superdex_robotics/superdex",
        VENDOR / "superdex_robotics/wheels/superdex-robotics",
    ),
}

RENAMES = {
    "superdex/physics/_native_payload.py": [
        ('distribution="superdex-physics"', 'distribution="superdex-physics-uni"'),
    ],
}


def stage() -> None:
    for package, (facade_src, wheel_src) in PACKAGES.items():
        package_dir = ROOT / "packages" / package
        facade_dst = package_dir / "superdex"
        if facade_dst.exists():
            shutil.rmtree(facade_dst)
        shutil.copytree(facade_src, facade_dst)
        for name in ("LICENSE", "NOTICE", "thirdparty_licenses"):
            src = wheel_src / name
            dst = package_dir / name
            if not src.exists():
                continue
            if dst.exists():
                shutil.rmtree(dst) if dst.is_dir() else dst.unlink()
            shutil.copytree(src, dst) if src.is_dir() else shutil.copy2(src, dst)
        for relpath, replacements in RENAMES.items():
            target = facade_dst.parent / relpath
            if not target.is_file():
                continue
            text = target.read_text()
            for old, new in replacements:
                if old in text:
                    text = text.replace(old, new)
            target.write_text(text)
        print(f"staged {package}: {facade_dst}")


if __name__ == "__main__":
    stage()
