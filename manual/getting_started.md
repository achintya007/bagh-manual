# Getting started

## A first calculation

Save this as `water_mp2.inp`:

```{literalinclude} examples/water_mp2.inp
:language: text
```

and run

```bash
bagh water_mp2.inp
```

(or `python -m bagh water_mp2.inp`). The input format is explained in
[Input format](input/format.md).

## Output

The output lists the SCF energy, the incore level chosen for the memory
available, and the MP2 energies:

```text
  e_corr_os         opposite-spin correlation energy
  e_corr_ss         same-spin correlation energy
  e_corr            total correlation energy
  e_total           SCF + correlation energy
```

All numbers are also written to `water_mp2.results.json`
(see [Results file](results_file.md)), which is the file to read from scripts.
