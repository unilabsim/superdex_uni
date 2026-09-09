#!/usr/bin/env python3
"""Stage packaging inputs from the pinned vendor tree into packages/*.

Copies each facade package and the upstream license files into the package
directories (all gitignored), then applies the packaging-only renames listed
below. The vendored source itself is never modified.

Renames (error-message text only, no behavior change):
  - superdex/physics/_native_payload.py: distribution "superdex-physics" ->
    "superdex-physics-uni"; the fp64 sibling name is left untouched because this
    channel ships no fp64 package.

Also stages a full copy of the vendored engine source at stage/project_superdex
(gitignored) and relaxes the two hardcoded CMake Python version ranges
(3.12...3.12.99 -> 3.12...3.13.99) so cp313 wheels can be built. This is a
packaging-only patch: it widens the interpreter search window, nothing else.
"""

from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VENDOR = ROOT / "vendor" / "project_superdex"
STAGE_SOURCE = ROOT / "stage" / "project_superdex"

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


SOURCE_PATCHES = {
    "superdex_physics/libraries/mochi/CMakeLists.txt": [
        ("find_package(Python3 3.12...3.12.99", "find_package(Python3 3.12...3.13.99"),
    ],
    "superdex_physics/libraries/mochi/third_party/CMakeLists.txt": [
        ("find_package(Python3 3.12...3.12.99", "find_package(Python3 3.12...3.13.99"),
    ],
}


def stage_source_tree() -> None:
    if not STAGE_SOURCE.exists():
        shutil.copytree(VENDOR, STAGE_SOURCE, ignore=shutil.ignore_patterns(".git"))
    for relpath, replacements in SOURCE_PATCHES.items():
        target = STAGE_SOURCE / relpath
        text = target.read_text()
        for old, new in replacements:
            if old not in text and new not in text:
                raise RuntimeError(f"patch anchor missing in {relpath}: {old!r}")
            text = text.replace(old, new)
        target.write_text(text)
        print(f"patched {relpath}")


if __name__ == "__main__":
    stage()
    stage_source_tree()
