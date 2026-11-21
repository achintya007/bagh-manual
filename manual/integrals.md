# Integral approximations

The two-electron integrals of the correlated method can be computed exactly or
approximated by a product of 3-centre factors,
$(pq|rs) \approx \sum_P L^P_{pq} L^P_{rs}$. BAGH offers two ways to make the factors:

| Option | How to request | SCF | Factors $L^P_{pq}$ | Accuracy set by |
|---|---|---|---|---|
| Exact | (default) | exact | none | — |
| RI (density fitting) | `! DF` or `! RI`, or `df true` | density fitted with `jkbasis` | auxiliary basis `auxbasis` | choice of auxiliary basis |
| Cholesky decomposition (CD) | `! CD`, or `cd true` | exact (or DF with `df true`) | pivoted Cholesky vectors of the AO integrals | `cd_threshold` (default $10^{-5}$) |

- **RI** uses pre-optimised auxiliary basis sets: `jkbasis` for the SCF and
  `auxbasis` for the correlated method. If they are not given, BAGH (through
  pyscf) chooses, per element, the fitting set made for the orbital basis
  (e.g. `cc-pvdz-jkfit` / `cc-pvdz-ri` for `cc-pvdz`); if there is none, a stand-in
  from another family (e.g. `def2-svp-ri` for `sto-3g`) or a generated
  even-tempered set (e.g. for Dyall bases). The output section **Auxiliary basis
  sets** lists the set used for every element, how it was chosen and the number
  of auxiliary functions, and prints a warning for stand-ins and generated sets;
  the same information is in the results file under `scf.auxiliary_basis`.
  Give both explicitly when results must be reproducible across program versions.
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

With a DHF reference the integrals are complex spinor integrals over the large
and small components ($(LL|LL)$, $(SS|SS)$, $(SS|LL)$, $(LL|SS)$, Dirac–Coulomb).
All three options are available:

- **Exact**: the four-index spinor integrals.
- **RI** (`DF true`): the SCF is density-fitted DHF (`jkbasis`), and the correlated
  method uses spinor 3-centre integrals for both components with one auxiliary
  basis (`auxbasis`) and one Coulomb metric, $(pq|rs) \approx \sum_P B^P_{pq} B^P_{rs}$.
  Density-fitted DHF keeps its 3-centre integrals in memory (no out-of-core
  version), so `maxcore` must be large enough for them.
- **Cholesky** (`CD true`): the SCF is exact DHF. Each complex spinor pair density
  is split into its real and imaginary parts, which have a real, positive
  Coulomb matrix; that matrix is Cholesky-decomposed with the same algorithm as
  for RHF, and small-component pairs are weighted by $(1/2c)^2$ so the threshold
  reflects their size in the energy. The error goes to zero as `cd_threshold`
  is tightened.

## Two-component (X2CAMF) references

The two-electron integrals over X2CAMF spinors are ordinary Coulomb integrals.
Exact integrals are transformed directly to complex spinor integrals. RI and
Cholesky use the same real 3-centre factors as for RHF (the Cholesky vectors are
identical to BAGH 0.x's); each spinor is split into its α and β parts in the
scalar basis, $B^P_{pq} = \sum_\sigma C^{\sigma *}_{\mu p} L^P_{\mu\nu} C^\sigma_{\nu q}$.
With `DF true` the SCF is density fitted too (`jkbasis`).
