# Reference wavefunctions and Hamiltonians

## RHF

Closed-shell restricted Hartree–Fock. Used by every method in the
[methods overview](methods/index.md) whose "References" column lists RHF.
The SCF is converged to `scf_conv` (default $10^{-10}$ $E_h$) within `scf_maxiter`
iterations; with `DF` it is density fitted with the `jkbasis` auxiliary basis.

## DHF (four-component)

Closed-shell Dirac–Hartree–Fock with the Dirac–Coulomb Hamiltonian, including
the (SS|SS) integrals. Request it with `! DHF` (or `! SPINOR`, the BAGH 0.x
spelling) or `%reference dhf`.

- Correlated methods use the **positive-energy (electronic) spinors** only
  (no-pair approximation); all MO quantities are complex.
- Each spinor holds one electron, so a molecule with $N$ electrons has $N$
  occupied spinors. `fc true` freezes twice as many spinors as there are core
  orbitals (e.g. 2 for the O 1s shell); `fc_no` counts spinors.
- `light_speed` changes the speed of light (default 137.036 a.u.). A very large
  value gives the non-relativistic limit, which is useful for checking results.
- RI (`DF`) and Cholesky (`CD`) are available; see
  [Integral approximations](integrals.md).

Reference: K. G. Dyall and K. Fægri, *Introduction to Relativistic Quantum
Chemistry* (Oxford, 2007), ch. 14.

## X2CAMF (two-component)

Closed-shell two-component spinor Hartree–Fock with the X2CAMF Hamiltonian:
exact two-component theory with spin–orbit coupling from atomic mean fields
(computed with socutils, as in BAGH 0.x). Request it with `! X2CAMF`
(or `! SOC-X2CAMF ... spinor`, the BAGH 0.x spelling) or `%reference x2camf`.

- Orbitals are complex two-component spinors; there are no negative-energy
  states. Correlated methods use the ordinary Coulomb integrals over these
  spinors.
- `fc true` freezes twice as many spinors as there are core orbitals; `fc_no`
  counts spinors.
- The **X2C level** is a separate keyword, `x2c_type` (as in BAGH 0.x), default
  `x2camf`; the levels are listed below. `gaunt true` adds the Gaunt interaction
  and `breit true` the full Breit interaction (Gaunt + gauge term) to the atomic
  mean field (they have no effect for the purely one-electron levels `1e`, `sf1e`).
  Example:

  ```text
  ! X2CAMF MP2 cc-pvtz
  %x2c_type x2cmp
  %gaunt true
  ```
- Exact, RI (`DF`) and Cholesky (`CD`) integrals are available. RI and Cholesky
  use the same real 3-centre factors as RHF, applied to the α and β parts of each
  spinor.

References: L. Cheng and J. Gauss, *J. Chem. Phys.* **135**, 084114 (2011);
J. Liu and L. Cheng, *J. Chem. Phys.* **148**, 144108 (2018);
K. Zhang and L. Cheng, *J. Phys. Chem. A* **126**, 4537 (2022).

### X2C levels (`x2c_type`)

<!-- GENERATED:x2c-levels -->
| x2c_type | Meaning |
|---|---|
| `x2camf` (default) | X2C with atomic mean-field (AMF) spin-orbit integrals (default, as BAGH 0.x) |
| `x2camf_sd` | variant of x2camf (socutils `x2camf_sd`) |
| `x2camf_axr` | variant of x2camf (socutils `x2camf_axr`) |
| `x2camf_au` | variant of x2camf (socutils `x2camf_au`) |
| `x2cmp` | X2C with an atomic model potential (scalar and spin-orbit two-electron picture-change corrections) |
| `sfmp` | spin-free version of x2cmp |
| `x2cmp_x1e` | variant of x2cmp (socutils `x2cmp_x1e`) |
| `dirac_amf` | atomic mean field from four-component atomic Dirac-HF (socutils `dirac_amf`) |
| `cq_amf` | atomic mean-field variant (socutils `cq_amf`) |
| `1e_amf` | atomic mean-field variant (socutils `1e_amf`) |
| `atm_fock` | atomic Fock-matrix variant (socutils `atm_fock`) |
| `atm_x2e` | atomic two-electron X2C variant (socutils `atm_x2e`) |
| `1e` | one-electron X2C including spin-orbit coupling (X2C1e) |
| `sf1e` | spin-free one-electron X2C (same physics as RHF with sfx2c1e, in spinors) |
<!-- END GENERATED -->

The levels are those of socutils' `X2CMP`; see socutils for their exact
definitions. (`amfx2c_a1e` exists in socutils but currently fails there and is
not offered.)

## Hamiltonians

| `hamiltonian` | Meaning | How to request |
|---|---|---|
| `nonrel` | non-relativistic (default for RHF) | — |
| `sfx2c1e` | spin-free exact two-component Hamiltonian in its one-electron variant (SFX2C1e): scalar-relativistic effects (RHF) | `%hamiltonian sfx2c1e`, `! SFX2C1E`, or `x2c true` (BAGH 0.x keyword) |
| `dirac-coulomb` | four-component Dirac–Coulomb (DHF; the only choice for DHF, used automatically) | `! DHF` |
| X2C levels | two-component X2C Hamiltonians for the X2CAMF reference (table above) | `! X2CAMF` and `%x2c_type ...` |

SFX2C1e replaces only the one-electron part of the Hamiltonian; the two-electron
integrals are not changed. It therefore works with **every method that uses an
RHF reference**, with exact, RI and Cholesky integrals, and with frozen core.
Scalar-relativistic effects matter for heavier elements; use basis sets
contracted for relativistic calculations (e.g. `cc-pvdz-dk`) or uncontracted
basis sets for quantitative work.

References: K. G. Dyall, *J. Chem. Phys.* **106**, 9618 (1997);
W. Kutzelnigg and W. Liu, *J. Chem. Phys.* **123**, 241102 (2005);
L. Cheng and J. Gauss, *J. Chem. Phys.* **135**, 084114 (2011).

Spin–orbit Hamiltonians (X2CAMF) and spinor references will be added as those
methods are ported.
