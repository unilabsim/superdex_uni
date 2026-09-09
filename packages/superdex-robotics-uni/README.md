# superdex-robotics-uni

Temporary unilabsim build of the SuperDex robotics facade
(`superdex.robotics`), rebuilt unchanged from the vendored upstream source so
that its dependency edge points at `superdex-physics-uni` instead of pulling
upstream `superdex-physics` into the environment. Published from
[unilabsim/superdex-uni](https://github.com/unilabsim/superdex-uni); will be
retired once the upstream PR merges.

Do not co-install with `superdex-robotics`: both packages own `superdex/robotics/`.

Apache-2.0, copyright Meta Platforms, Inc. and affiliates; see LICENSE and
thirdparty_licenses/.
