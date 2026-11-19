# Run settings: memory, disk, threads, output

These settings control *how* a calculation runs, not *what* it computes. They
never change the results beyond about $10^{-10}$ $E_h$ (this is tested).

<!-- GENERATED:run-settings-keywords -->
| Keyword | Type / values | Default | Meaning |
|---|---|---|---|
| `maxcore` | float | `4000` | Memory limit in MB per process. Never exceeded. |
| `incore` | int | `-1` | Incore level (2-5, see Run settings). -1: chosen automatically from `maxcore`. |
| `nthreads` | int | `0` | Number of threads. 0: all cores of the machine. |
| `scratch` | str |  | Scratch directory. Empty: `$BAGH_SCRATCH`, else `./bagh_scratch`. |
| `keep_scratch` | bool | `False` | Keep scratch files after a successful run. |
| `printlevel` | int | `2` | Amount of output, 0 (errors only) to 5 (debug dumps). |
| `backend` | `cpp`, `py`, `both` | `cpp` | Implementation to run: `cpp`, `py` (Python reference, development only) or `both` (run both and compare). |
| `job_name` | str | `bagh` | Job name; set from the input file name. |
<!-- END GENERATED -->

## Memory (`maxcore`)

The memory, in MB per process, that BAGH may use. BAGH never uses more. If a step
cannot fit, BAGH stops with a message giving the memory needed and the memory
available; then raise `maxcore` or lower `incore`.

## What is kept in memory (`incore`)

Large quantities are kept in memory or on disk depending on the **incore level**.
Higher levels are faster and need more memory:

<!-- GENERATED:incore-levels -->
| incore | What is kept on disk (everything else is in memory) |
|---|---|
| `5` | Everything in memory. |
| `4` | On disk: vvvv integrals, and amplitudes of rank higher than doubles (triples and beyond). |
| `3` | On disk: vvvv and ovvv integrals, and amplitudes of rank higher than doubles. |
| `2` | On disk: vvvv, ovvv, ovov and ovvo integrals, the vv block of the 3-centre factors (L_vv), and all amplitudes. |
<!-- END GENERATED -->

By default BAGH estimates the memory each level needs and **chooses the highest
level that fits in `maxcore`**. Set `incore` to force a level. The chosen level is
printed in the output. Not every method supports every level; see the method's
page.

## Scratch files (`scratch`, `keep_scratch`)

Temporary files go to a job directory inside `scratch` (default: the
`BAGH_SCRATCH` environment variable, else `./bagh_scratch`). Put it on a fast
local disk. It is deleted after a successful run and kept after a failure (the
path is printed). Set `keep_scratch true` to always keep it.

## Threads (`nthreads`)

Number of CPU threads (default: all cores). BAGH divides threads between its own
parallel loops and the linear-algebra library itself; do not set
`OMP_NUM_THREADS` or `MKL_NUM_THREADS` by hand. Results do not depend on the
number of threads.

## Output detail (`printlevel`)

| Level | Output |
|---|---|
| 0 | errors only |
| 1 | final results only |
| 2 | normal output (default) |
| 3 | + iterations, timings, memory use, batch sizes |
| 4 | + debugging information |
| 5 | + intermediate dumps to scratch (developers) |
