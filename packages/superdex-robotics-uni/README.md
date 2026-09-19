# superdex-robotics-uni

Temporary unilabsim build of the SuperDex robotics facade
(`superdex.robotics`), rebuilt unchanged from the vendored upstream source so
that its dependency edge points at `superdex-physics-uni` instead of pulling
upstream `superdex-physics` into the environment. Published from
[unilabsim/superdex-uni](https://github.com/unilabsim/superdex-uni); will be
retired once the upstream PR merges.

Source commit for the 1.2.0 candidate:
`8379ee08d059d0899746fdce3fc663f664356f97`
([project_superdex#13](https://github.com/unilabsim/project_superdex/pull/13)).
Do not publish this candidate until the wheels workflow for that exact submodule
provenance has succeeded.
It requires `superdex-physics-uni==1.2.0`.
This package does not claim UniSim adapter support; that integration remains
blocked until the source change and rebuilt wheels are published and installed.

Do not co-install with `superdex-robotics`: both packages own `superdex/robotics/`.

Apache-2.0, copyright Meta Platforms, Inc. and affiliates; see LICENSE and
thirdparty_licenses/.
