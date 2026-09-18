# superdex-physics-uni

Temporary unilabsim build of the SuperDex physics runtime
(`superdex.physics`), carrying the native `SceneBatchExecutorV2` ABI 2
(multi-actor flattened layout, selective state writes, actor-offset
`step_control`).
Published from [unilabsim/superdex-uni](https://github.com/unilabsim/superdex-uni);
will be retired once the upstream PR merges into
[facebookresearch/project_superdex](https://github.com/facebookresearch/project_superdex).

Source commit for the 1.1.0 candidate:
`973aaba5481b0279cdc764e8b73fc6a702c03fe7`
([project_superdex#11](https://github.com/unilabsim/project_superdex/pull/11)).
Do not publish this candidate until that source PR is merged and the packaging
submodule points to the resulting merged source head.
This package does not claim UniSim adapter support; that integration remains
blocked until the source change and rebuilt wheels are published and installed.

Do not co-install with `superdex-physics`: both packages own `superdex/physics/`.

Apache-2.0, copyright Meta Platforms, Inc. and affiliates; see LICENSE and
thirdparty_licenses/.
