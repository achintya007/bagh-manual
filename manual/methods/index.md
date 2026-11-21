# Methods overview

Which reference wavefunctions, integral approximations, incore levels and
properties each method supports:

<!-- GENERATED:methods -->
| Method | Description | References | Hamiltonians | Integrals | Incore levels | Properties |
|---|---|---|---|---|---|---|
| HF | SCF only (no correlated method). | RHF, DHF, X2CAMF | RHF: nonrel, sfx2c1e<br>DHF: dirac-coulomb<br>X2CAMF: x2camf, x2camf-gaunt, x2camf-breit | RHF: exact, ri<br>DHF: exact, ri<br>X2CAMF: exact, ri | - | - |
| [MP2](mp2.md) | Second-order Moller-Plesset perturbation theory. | RHF, DHF, X2CAMF | RHF: nonrel, sfx2c1e<br>DHF: dirac-coulomb<br>X2CAMF: x2camf, x2camf-gaunt, x2camf-breit | RHF: exact, ri, cd<br>DHF: exact, ri, cd<br>X2CAMF: exact, ri, cd | 2, 3, 4, 5 | - |
<!-- END GENERATED -->

```{toctree}
:maxdepth: 1
:hidden:

mp2
```
