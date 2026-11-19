# Integral approximations

The two-electron integrals of the correlated method can be computed exactly or
approximated by a product of 3-centre factors,
$(pq|rs) \approx \sum_P L^P_{pq} L^P_{rs}$. BAGH offers two ways to make the factors:

| Option | How to request | SCF | Factors $L^P_{pq}$ | Accuracy set by |
|---|---|---|---|---|
| Exact | (default) | exact | none | — |
| RI (density fitting) | `! DF` or `! RI`, or `df true` | density fitted with `jkbasis` | auxiliary basis `auxbasis` | choice of auxiliary basis |
| Cholesky decomposition (CD) | `! CD`, or `cd true` | exact (or DF with `df true`) | pivoted Cholesky vectors of the AO integrals | `cd_threshold` (default $10^{-5}$) |

- **RI** uses a pre-optimised auxiliary basis. If `auxbasis` / `jkbasis` are not
  given, standard fitting bases for the orbital basis are chosen. Give them
  explicitly when results must be reproducible across program versions.
- **CD** needs no auxiliary basis: vectors are added until the largest remaining
  diagonal integral is below `cd_threshold`, so the error is controlled by one
  number and goes to zero as the threshold is tightened. At most $10\,n_\mathrm{AO}$
  vectors are made (as in BAGH 0.x); for very tight thresholds BAGH stops and asks
  for a larger `cd_threshold`. The Cholesky vectors are identical to those of
  BAGH 0.x.

## Where the 3-centre factors are kept

Both kinds of factors are always built and stored according to the
[incore level](run_settings.md):

<!-- GENERATED:factor-storage -->
| Factor | incore 5 | incore 4 | incore 3 | incore 2 |
|---|---|---|---|---|
| AO factors (RI integrals or Cholesky vectors) | memory | memory | memory | disk |
| $L_{oo}$ | memory | memory | memory | memory |
| $L_{ov}$ | memory | memory | memory | memory |
| $L_{vv}$ | memory | memory | memory | disk |
<!-- END GENERATED -->

On disk the factors are built and read in chunks whose size is set by `maxcore`.

## Four-component (DHF) references

With a DHF reference the correlated method uses exact Dirac–Coulomb integrals
over the large and small components, $(LL|LL)$, $(SS|SS)$, $(SS|LL)$ and
$(LL|SS)$, transformed to complex spinor integrals. RI and Cholesky
decomposition are not available for DHF yet.
