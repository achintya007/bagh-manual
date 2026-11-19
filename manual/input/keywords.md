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
| `fc` | bool | `False` | Freeze core orbitals (standard chemical core). |
| `fc_no` | int | `-1` | Number of frozen core orbitals; overrides `fc`. -1: not set. |

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
<!-- END GENERATED -->
