# CCSD

## What it computes

Coupled-cluster singles and doubles (CCSD) correlation energy for a closed-shell
RHF reference, with the spin-adapted closed-shell equations. The iterations
start from MP2 amplitudes, whose energy is printed as well.

## Theory and references

$$
E_\mathrm{CCSD} = \sum_{ijab} \tau_{ij}^{ab}\left[2(ia|jb) - (ib|ja)\right],
\qquad \tau_{ij}^{ab} = t_{ij}^{ab} + t_i^a t_j^b ,
$$

with the amplitude equations in the spin-adapted form of BAGH 0.x / pyscf.

- G. D. Purvis III and R. J. Bartlett, *J. Chem. Phys.* **76**, 1910 (1982).
- S. Hirata, P.-D. Fan, A. A. Auer, M. Nooijen and P. Piecuch, *J. Chem. Phys.*
  **121**, 12197 (2004); spin-adapted equations as in S. Hirata *et al.*,
  *J. Chem. Phys.* **120**, 2581 (2004).
- DIIS: P. Pulay, *Chem. Phys. Lett.* **73**, 393 (1980).

## Supported cases

<!-- GENERATED:method:CCSD -->
|  |  |
|---|---|
| References | RHF |
| Hamiltonians | RHF: nonrel, sfx2c1e |
| Integrals | RHF: exact, ri, cd |
| Incore levels | 2, 3, 4, 5 |
| Properties | none yet |
<!-- END GENERATED -->

## Keywords used

`cc_convergence` (energy, default $10^{-10}$ $E_h$), `cc_convergence_r` (rms
amplitude change, default $10^{-8}$), `cc_max_cycle`, `diis`, `diis_space`, and
`fc`, `fc_no`, `hamiltonian` (e.g. SFX2C1e), [run settings](../run_settings.md).

## Example

```{literalinclude} ../examples/water_ccsd.inp
:language: text
```

The output shows one line per iteration (correlation energy, change, rms
amplitude change, number of DIIS vectors) and the converged energies.

## Cost and practical advice

- Cost scales as $O(o^2 v^4)$ per iteration.
- RI (`DF true` or `! RI`, auxiliary basis `auxbasis`) and Cholesky (`CD true`,
  threshold `cd_threshold`) use 3-centre factors $L^P_{pq}$ in place of the
  four-index integrals, as BAGH 0.x does: $(ia|bc)$ and $(ab|cd)$ are never formed
  or stored, and every term that needs them is evaluated from $L_{ov}$ and $L_{vv}$.
  Disk and memory then grow only as $N_\mathrm{aux} v^2$ instead of $v^4$. Cholesky
  CCSD tends to the exact-integral result as `cd_threshold` is lowered (water,
  cc-pVDZ: $3\times10^{-7}$ $E_h$ at $10^{-4}$, $2\times10^{-9}$ $E_h$ at $10^{-7}$).
- Memory follows the [incore level](../run_settings.md), chosen automatically from
  `maxcore` or set with `incore`:
  - `incore 5`: all integrals in memory (memory grows as $v^4$);
  - `incore 4`: $(ab|cd)$ on disk, read in batches each iteration (memory grows as
    $o v^3$);
  - `incore 3`: $(ab|cd)$ and $(ia|bc)$ on disk (memory grows as $o^2 v^2$, the
    size of the amplitudes);
  - `incore 2`: also $(ia|jb)$, $(ia|bj)$ and the stored amplitudes (the DIIS
    history) on disk; the current and new amplitudes and the work arrays of one
    iteration stay in memory. About half the memory of `incore 3`, with more disk
    traffic.
  All levels give the same result. Put `scratch` on a fast local disk.
  With RI or Cholesky, levels 5, 4 and 3 are the same (no $(ia|bc)$ or $(ab|cd)$ to
  move); at `incore 2` the factor $L_{vv}$ is on disk, read in batches of the
  auxiliary index, together with $(ia|jb)$ and the DIIS history.
- Core orbitals are frozen by default.

## Limitations

- RHF reference only for now (spinor references: to come).
- At `incore 2` the work arrays of one iteration (about a dozen arrays of the
  size of the amplitudes) are still in memory.
