# Integral approximations

| Option | Keyword | SCF | Correlated method |
|---|---|---|---|
| Exact | (default) | exact 4-index integrals | exact $(pq\|rs)$ |
| Density fitting | `DF` / `RI` on the `!` line, or `df true` | DF with `jkbasis` | RI with `auxbasis` |

If `auxbasis` / `jkbasis` are not given, a standard fitting basis for the
orbital basis is chosen automatically. Give them explicitly when results must be
reproducible across program versions.

Cholesky decomposition (CD) and tensor hypercontraction (THC) will be added as
methods that use them are ported.
