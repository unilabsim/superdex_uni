# superdex-uni

Temporary packaging and publishing channel for SuperDex wheels that carry the
unilabsim native batch executor work
([`unilabsim/project_superdex` PR head, pinned in `vendor/`](vendor/project_superdex)).

**This repository is a sunset artifact.** It exists only until
[facebookresearch/project_superdex](https://github.com/facebookresearch/project_superdex)
merges the upstream PR. It performs no semantic fork: the physics and robotics
facades are copied verbatim from the vendored source at package time, and the only
source change relative to upstream is the batch-executor PR itself. Once upstream
merges and publishes equivalent wheels, downstream (unisim) switches its dependency
back to `superdex-physics`/`superdex-robotics` and this repository is archived.

## Packages

| package | mirrors | contents |
| --- | --- | --- |
| `superdex-physics-uni` | `superdex-physics` | `superdex.physics` facade + `_native/` payload with `SceneBatchExecutor` (indexed dispatch, selective readback, `step_control`) |
| `superdex-robotics-uni` | `superdex-robotics` | `superdex.robotics` facade + `_native/` payload, rebuilt from the same vendored source; depends on `superdex-physics-uni==1.0.0` |

**Mutual exclusion:** `superdex-physics-uni` and upstream `superdex-physics` install
into the same `superdex/physics/` path and must never be co-installed. The same holds
for the robotics pair. Downstream environments must resolve exactly one pair.

## Install

```bash
pip install superdex-robotics-uni==1.0.0  # pulls superdex-physics-uni==1.0.0
```

Requires CPython 3.12 on Linux x86_64 (the only validated platform; macOS/Windows
wheels are intentionally not published).

## Build

All build configuration lives in each distribution's `packages/*/pyproject.toml`,
mirroring the upstream layout. The driver stages facade/license files out of the
vendored source, applies the packaging-only patches under `patches/`, and invokes
cibuildwheel:

```bash
git clone --recurse-submodules https://github.com/unilabsim/superdex-uni.git
cd superdex-uni
uv run tools/build_wheels.py --output wheelhouse           # publishable (manylinux)
uv run tools/build_wheels.py --output wheelhouse --fast    # local iteration only
```

## Release process

Modeled on the upstream `wheels.yml` / `publish.yml` pair:

1. Pin `vendor/project_superdex` to the intended commit (PR head).
2. Run the `wheels` workflow manually; it uploads a flat `wheelhouse` artifact
   (exactly 2 wheels: `superdex_physics_uni` + `superdex_robotics_uni`, cp312
   manylinux x86_64).
3. Publish from the wheelhouse, TestPyPI first, then PyPI. PyPI publication uses
   Trusted Publishing (configure the publisher on the PyPI project page for
   `superdex-physics-uni` / `superdex-robotics-uni`); `publish.yml` refuses to run
   from any ref other than a `v*` tag.

## Relationship to upstream

- Engine source: `vendor/project_superdex` (submodule, pinned SHA).
- Packaging logic only; no task, reward, or downstream-adapter changes live here.
- License: Apache-2.0, preserving `LICENSE` and `thirdparty_licenses/` from upstream
  in every wheel.
