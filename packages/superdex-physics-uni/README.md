# superdex-physics-uni

Temporary unilabsim build of the SuperDex physics runtime
(`superdex.physics`), carrying the native `SceneBatchExecutorV2` ABI 2
(multi-actor flattened layout, selective state writes, actor-offset
`step_control`).
Published from [unilabsim/superdex-uni](https://github.com/unilabsim/superdex-uni);
will be retired once the upstream PR merges into
[facebookresearch/project_superdex](https://github.com/facebookresearch/project_superdex).

Source commit for the 1.1.0 candidate:
`34a825082e7541e0156997a6a3187624204ffa96`
([project_superdex#11](https://github.com/unilabsim/project_superdex/pull/11)).
Do not publish this candidate until the wheels workflow for that exact submodule
provenance has succeeded.
This package does not claim UniSim adapter support; that integration remains
blocked until the source change and rebuilt wheels are published and installed.

Do not co-install with `superdex-physics`: both packages own `superdex/physics/`.

Apache-2.0, copyright Meta Platforms, Inc. and affiliates; see LICENSE and
thirdparty_licenses/.
