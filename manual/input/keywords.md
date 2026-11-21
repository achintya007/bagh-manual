# Keywords

Every keyword can be given as a one-line `%keyword value` or inside any
`%block ... end` (see [Input format](format.md)). Names are case-insensitive.

<!-- GENERATED:keywords -->

## Calculation

| Keyword | Type / values | Default | Meaning |
|---|---|---|---|
| `method` | str | `HF` | Method, given on the `!` line (e.g. `MP2`). |
| `basis` | str | `sto-3g` | Orbital basis set, given on the `!` line. |
| `df` | bool | `False` | Density fitting with an auxiliary basis (RI): DF-SCF (with `jkbasis`) and RI for the correlated method (with `auxbasis`). Also `! DF` or `! RI`. |
| `auxbasis` | str |  | Auxiliary basis for density fitting. Empty: chosen automatically for the orbital basis. |
| `jkbasis` | str |  | Auxiliary basis for DF-SCF. Empty: chosen automatically. Also on the `!` line (`...jkfit`). |
| `cd` | bool | `False` | Cholesky decomposition of the two-electron integrals for the correlated method (no auxiliary basis; SCF follows `df`). Also `! CD`. |
| `cd_threshold` | float | `1e-05` | Cholesky decomposition threshold: largest remaining diagonal (Eh). |
| `fc` | bool | `True` | Freeze core orbitals (standard chemical core; twice as many spinors for DHF). On by default (BAGH 0.x: off); `fc false` or `! NOFC` for all-electron. |
| `fc_no` | int | `-1` | Number of frozen core orbitals (spinors for DHF); overrides `fc`. -1: not set. |
| `reference` | `rhf`, `dhf`, `x2camf` | `rhf` | Reference wavefunction: `rhf`, `dhf` (four-component Dirac-Hartree-Fock; also `! DHF`, or `! SPINOR` as in BAGH 0.x) or `x2camf` (two-component spinor HF with the X2CAMF Hamiltonian; also `! X2CAMF`, or `! SOC-X2CAMF` as in BAGH 0.x). |
| `hamiltonian` | `auto`, `nonrel`, `sfx2c1e`, `dirac-coulomb`, `x2camf`, `x2camf-gaunt`, `x2camf-breit` | `auto` | Hamiltonian. RHF: `nonrel` or `sfx2c1e` (spin-free exact two-component, one-electron; also `! SFX2C1E` or `x2c true`). DHF: `dirac-coulomb`. X2CAMF: `x2camf` (Dirac-Coulomb atomic mean field), `x2camf-gaunt`, `x2camf-breit` (Gaunt / Breit terms in the atomic mean field). `auto`: the first one listed for the reference. |
| `light_speed` | float | `0.0` | Speed of light (a.u.) for DHF and X2CAMF. 0: the standard value (137.036). |

## Molecule

| Keyword | Type / values | Default | Meaning |
|---|---|---|---|
| `units` | `angstrom`, `bohr` | `angstrom` | Units of the coordinates. Also `! Bohr`. |
| `charge` | int | `0` | Molecular charge, from the `*xyz` line. |
| `multiplicity` | int | `1` | Spin multiplicity, from the `*xyz` line. |
| `geometry` | str |  | Atoms and coordinates, from the `*xyz` block. |

## SCF

| Keyword | Type / values | Default | Meaning |
|---|---|---|---|
| `scf_conv` | float | `1e-10` | SCF energy convergence threshold (Eh). |
| `scf_maxiter` | int | `100` | Maximum number of SCF iterations. |

## Resources (memory, disk, threads)

| Keyword | Type / values | Default | Meaning |
|---|---|---|---|
| `maxcore` | float | `4000` | Memory limit in MB per process. Never exceeded. |
| `incore` | int | `-1` | Incore level (2-5, see Run settings). -1: chosen automatically from `maxcore`. |
| `nthreads` | int | `0` | Number of threads. 0: all cores of the machine. |
| `scratch` | str |  | Scratch directory. Empty: `$BAGH_SCRATCH`, else `./bagh_scratch`. |
| `keep_scratch` | bool | `False` | Keep scratch files after a successful run. |

## Output

| Keyword | Type / values | Default | Meaning |
|---|---|---|---|
| `printlevel` | int | `2` | Amount of output, 0 (errors only) to 5 (debug dumps). |
| `backend` | `cpp`, `py`, `both` | `cpp` | Implementation to run: `cpp`, `py` (Python reference, development only) or `both` (run both and compare). |
| `job_name` | str | `bagh` | Job name; set from the input file name. |
| `molden` | bool | `True` | Write `<job>.molden` (geometry, basis, SCF orbitals, energies, occupations) for Chemcraft, Avogadro, Jmol, ... RHF only: Molden files cannot hold four-component spinors (use `cube` for DHF). |
| `cube` | str |  | Orbitals to write as cube files: comma-separated numbers as in the orbital table and/or `homo`, `lumo`, `homo-N`, `lumo+N`. RHF: the orbital; DHF: the spinor density |psi|^2 (and see `cube_re_im`). Empty: none. |
| `cube_points` | int | `80` | Grid points per direction in cube files. |
| `cube_re_im` | bool | `False` | DHF: also write real and imaginary parts of the large-component alpha and beta parts of each `cube` spinor, phase fixed so the largest coefficient is real and positive. |
<!-- END GENERATED -->
