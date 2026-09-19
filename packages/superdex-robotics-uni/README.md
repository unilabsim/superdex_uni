# superdex-robotics-uni

Temporary unilabsim build of the SuperDex robotics facade
(`superdex.robotics`), rebuilt unchanged from the vendored upstream source so
that its dependency edge points at `superdex-physics-uni` instead of pulling
upstream `superdex-physics` into the environment. Published from
[unilabsim/superdex-uni](https://github.com/unilabsim/superdex-uni); will be
retired once the upstream PR merges.

Source commit for the 1.1.0 candidate:
`34a825082e7541e0156997a6a3187624204ffa96`
([project_superdex#11](https://github.com/unilabsim/project_superdex/pull/11)).
Do not publish this candidate until the wheels workflow for that exact submodule
provenance has succeeded.
It requires `superdex-physics-uni==1.1.0`.
This package does not claim UniSim adapter support; that integration remains
blocked until the source change and rebuilt wheels are published and installed.

Do not co-install with `superdex-robotics`: both packages own `superdex/robotics/`.

Apache-2.0, copyright Meta Platforms, Inc. and affiliates; see LICENSE and
thirdparty_licenses/.
