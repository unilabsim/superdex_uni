# superdex-uni

Temporary packaging and publishing channel for SuperDex wheels that carry the
unilabsim native batch executor work
([`unilabsim/project_superdex`, pinned in `vendor/`](vendor/project_superdex)).

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
| `superdex-physics-uni` | `superdex-physics` | `superdex.physics` facade + `_native/` payload with `SceneBatchExecutorV3` ABI 3 (multi-actor flattened layout, selective state/boundary-condition writes, actor-offset `step_control`); ABI 2 remains available |
| `superdex-robotics-uni` | `superdex-robotics` | `superdex.robotics` facade + `_native/` payload, rebuilt from the same vendored source; depends on `superdex-physics-uni==1.3.0` |

**Mutual exclusion:** `superdex-physics-uni` and upstream `superdex-physics` install
into the same `superdex/physics/` path and must never be co-installed. The same holds
for the robotics pair. Downstream environments must resolve exactly one pair.

## Install

```bash
pip install superdex-robotics-uni==1.3.0  # pulls superdex-physics-uni==1.3.0
```

Requires CPython 3.12 or 3.13 on Linux x86_64 (the only validated platform; macOS/Windows
wheels are intentionally not published).

## Build

All build configuration lives in each distribution's `packages/*/pyproject.toml`,
mirroring the upstream layout. The driver stages facade/license files out of the
vendored source, applies the packaging-only distribution rename, and invokes
cibuildwheel:

```bash
git clone --recurse-submodules https://github.com/unilabsim/superdex-uni.git
cd superdex-uni
uv run tools/build_wheels.py --output wheelhouse           # publishable (manylinux)
uv run tools/build_wheels.py --output wheelhouse --fast    # local iteration only
```

## Release process

Modeled on the upstream `wheels.yml` / `publish.yml` pair:

1. Ensure the source change is merged, pin `vendor/project_superdex` to that
   merged source commit, and merge the `superdex-uni` release change.
2. Tag the merged release commit as `v1.3.0`.
3. Dispatch `wheels` from that tag; it uploads a flat `wheelhouse` artifact
   (exactly 4 wheels: `superdex_physics_uni` + `superdex_robotics_uni` for
   cp312 and cp313 manylinux x86_64). Record the successful run ID.
4. Dispatch `publish` from the same `v1.3.0` tag and wheelhouse run ID. Run
   `target=validate` first, then `target=pypi`. Publication goes directly to
   PyPI with Trusted Publishing (configure the publisher on the PyPI project
   page for `superdex-physics-uni` / `superdex-robotics-uni`). There is no
   TestPyPI stage, and a published version must not be partially overwritten.

## Relationship to upstream

- Engine source: `vendor/project_superdex` (submodule, pinned SHA).
- Current 1.3.0 source:
  `0ed957041092a30bb60d804e31591871741cf7e4`
  ([project_superdex#14](https://github.com/unilabsim/project_superdex/pull/14)).
  Do not publish this release until the wheels workflow for that exact
  submodule provenance has succeeded.
- Packaging these wheels does not claim UniSim adapter support; that work
  remains blocked until the rebuilt exact wheels are published and installed.
- Packaging logic only; no task, reward, or downstream-adapter changes live here.
- License: Apache-2.0, preserving `LICENSE` and `thirdparty_licenses/` from upstream
  in every wheel.
