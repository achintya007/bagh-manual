# Methods overview

Which reference wavefunctions, integral approximations, incore levels and
properties each method supports:

<!-- GENERATED:methods -->
| Method | Description | References | Hamiltonians | Integrals | Incore levels | Properties |
|---|---|---|---|---|---|---|
| HF | SCF only (no correlated method). | RHF, DHF | RHF: nonrel, sfx2c1e<br>DHF: dirac-coulomb | RHF: exact, ri<br>DHF: exact | - | - |
| [MP2](mp2.md) | Second-order Moller-Plesset perturbation theory. | RHF, DHF | RHF: nonrel, sfx2c1e<br>DHF: dirac-coulomb | RHF: exact, ri, cd<br>DHF: exact | 2, 3, 4, 5 | - |
<!-- END GENERATED -->

```{toctree}
:maxdepth: 1
:hidden:

mp2
```
