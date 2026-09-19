# superdex-physics-uni

Temporary unilabsim build of the SuperDex physics runtime
(`superdex.physics`), carrying the native `SceneBatchExecutorV3` ABI 3
(multi-actor flattened layout, selective state writes, selective
boundary-condition writes, actor-offset `step_control`). The ABI 2 executor
remains available and reports ABI 2.
Published from [unilabsim/superdex-uni](https://github.com/unilabsim/superdex-uni);
will be retired once the upstream PR merges into
[facebookresearch/project_superdex](https://github.com/facebookresearch/project_superdex).

Source commit for the 1.3.0 release:
`0ed957041092a30bb60d804e31591871741cf7e4`
([project_superdex#14](https://github.com/unilabsim/project_superdex/pull/14)).
Do not publish this release until the wheels workflow for that exact submodule
provenance has succeeded.
This package does not claim UniSim adapter support; that integration remains
blocked until the source change and rebuilt wheels are published and installed.

Do not co-install with `superdex-physics`: both packages own `superdex/physics/`.

Apache-2.0, copyright Meta Platforms, Inc. and affiliates; see LICENSE and
thirdparty_licenses/.
