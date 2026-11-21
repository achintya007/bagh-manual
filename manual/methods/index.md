# Methods overview

Which reference wavefunctions, integral approximations, incore levels and
properties each method supports:

<!-- GENERATED:methods -->
| Method | Description | References | Hamiltonians | Integrals | Incore levels | Properties |
|---|---|---|---|---|---|---|
| HF | SCF only (no correlated method). | RHF, DHF, X2CAMF | RHF: nonrel, sfx2c1e<br>DHF: dirac-coulomb<br>X2CAMF: x2camf, x2camf_sd, x2camf_axr, x2camf_au, x2cmp, sfmp, x2cmp_x1e, dirac_amf, cq_amf, 1e_amf, atm_fock, atm_x2e, 1e, sf1e | RHF: exact, ri<br>DHF: exact, ri<br>X2CAMF: exact, ri | - | - |
| [MP2](mp2.md) | Second-order Moller-Plesset perturbation theory. | RHF, DHF, X2CAMF | RHF: nonrel, sfx2c1e<br>DHF: dirac-coulomb<br>X2CAMF: x2camf, x2camf_sd, x2camf_axr, x2camf_au, x2cmp, sfmp, x2cmp_x1e, dirac_amf, cq_amf, 1e_amf, atm_fock, atm_x2e, 1e, sf1e | RHF: exact, ri, cd<br>DHF: exact, ri, cd<br>X2CAMF: exact, ri, cd | 2, 3, 4, 5 | - |
| [CCSD](ccsd.md) | Coupled cluster with single and double excitations. | RHF | RHF: nonrel, sfx2c1e | RHF: exact | 3, 4, 5 | - |
<!-- END GENERATED -->

```{toctree}
:maxdepth: 1
:hidden:

mp2
ccsd
```
