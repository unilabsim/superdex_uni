# superdex-robotics-uni

Temporary unilabsim build of the SuperDex robotics facade
(`superdex.robotics`), rebuilt unchanged from the vendored upstream source so
that its dependency edge points at `superdex-physics-uni` instead of pulling
upstream `superdex-physics` into the environment. Published from
[unilabsim/superdex-uni](https://github.com/unilabsim/superdex-uni); will be
retired once the upstream PR merges.

Source commit for the 1.1.0 candidate:
`973aaba5481b0279cdc764e8b73fc6a702c03fe7`
([project_superdex#11](https://github.com/unilabsim/project_superdex/pull/11)).
Do not publish this candidate until that source PR is merged and the packaging
submodule points to the resulting merged source head.
It requires `superdex-physics-uni==1.1.0`.
This package does not claim UniSim adapter support; that integration remains
blocked until the source change and rebuilt wheels are published and installed.

Do not co-install with `superdex-robotics`: both packages own `superdex/robotics/`.

Apache-2.0, copyright Meta Platforms, Inc. and affiliates; see LICENSE and
thirdparty_licenses/.
