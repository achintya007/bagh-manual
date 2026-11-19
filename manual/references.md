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

## Hamiltonians

| `hamiltonian` | Meaning | How to request |
|---|---|---|
| `nonrel` | non-relativistic (default for RHF) | — |
| `sfx2c1e` | spin-free exact two-component Hamiltonian in its one-electron variant (SFX2C1e): scalar-relativistic effects (RHF) | `%hamiltonian sfx2c1e`, `! SFX2C1E`, or `x2c true` (BAGH 0.x keyword) |
| `dirac-coulomb` | four-component Dirac–Coulomb (DHF; the only choice for DHF, used automatically) | `! DHF` |

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
