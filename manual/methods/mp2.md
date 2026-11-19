# MP2

## What it computes

Second-order Møller–Plesset perturbation theory (MP2) correlation energy for a
closed-shell RHF reference, split into opposite-spin and same-spin parts.

## Theory and references

$$
E^{(2)} = \sum_{ijab} \frac{(ia|jb)\,\left[2(ia|jb) - (ib|ja)\right]}
{\varepsilon_i + \varepsilon_j - \varepsilon_a - \varepsilon_b}
= E_\mathrm{OS} + E_\mathrm{SS}
$$

with $E_\mathrm{OS} = \sum (ia|jb)^2 / D_{ijab}$ and
$E_\mathrm{SS} = \sum (ia|jb)\left[(ia|jb) - (ib|ja)\right] / D_{ijab}$.

- C. Møller and M. S. Plesset, *Phys. Rev.* **46**, 618 (1934).
- A. Szabo and N. S. Ostlund, *Modern Quantum Chemistry*, eq. (6.74).
- S. Grimme, *J. Chem. Phys.* **118**, 9095 (2003) (spin components).
- With `DF` (RI): M. Feyereisen, G. Fitzgerald and A. Komornicki, *Chem. Phys. Lett.*
  **208**, 359 (1993); F. Weigend and M. Häser, *Theor. Chem. Acc.* **97**, 331 (1997).
- With `CD`: H. Koch, A. Sánchez de Merás and T. B. Pedersen, *J. Chem. Phys.*
  **118**, 9481 (2003); F. Aquilante, T. B. Pedersen and R. Lindh, *J. Chem. Phys.*
  **126**, 194106 (2007).

## Supported cases

<!-- GENERATED:method:MP2 -->
|  |  |
|---|---|
| References | RHF |
| Hamiltonians | nonrel, sfx2c1e |
| Integrals | exact, ri, cd |
| Incore levels | 2, 3, 4, 5 |
| Properties | none yet |
<!-- END GENERATED -->

## Keywords used

`df`, `auxbasis`, `jkbasis` (RI), `cd`, `cd_threshold` (Cholesky),
`fc`, `fc_no` (frozen core), `hamiltonian` (e.g. SFX2C1e, see
[References and Hamiltonians](../references.md)), and the
[run settings](../run_settings.md) (`maxcore`, `incore`, `nthreads`). See the
[keyword list](../input/keywords.md).

With `DF`, both the SCF (basis `jkbasis`) and the MP2 integrals (basis `auxbasis`)
are density fitted, as in BAGH 0.x. With `CD`, the MP2 integrals use Cholesky
vectors and the SCF is exact. See [Integral approximations](../integrals.md).

## Example

```{literalinclude} ../examples/water_mp2.inp
:language: text
```

## Cost and practical advice

- Cost scales as $O(o^2 v^2 N)$ (integral transformation $O(N^5)$); memory for
  $(ia|jb)$ is $8\,o^2v^2$ bytes.
- At `incore 5`–`3`, $(ia|jb)$ is held in memory. At `incore 2` it is on disk
  (exact) or rebuilt in batches from $L_{ov}$ (RI, CD), and the batch size is
  chosen from `maxcore`.
- Use `DF` or `CD` for anything but small molecules. CD with the default
  threshold ($10^{-5}$) changes the MP2 energy by about $10^{-6}$ $E_h$.

## Limitations

- RHF reference only (UHF, GHF and relativistic references: not yet ported).
- No gradients or relaxed densities yet.
