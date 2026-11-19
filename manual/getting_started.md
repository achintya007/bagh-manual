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

The output file contains, in order:

1. the BAGH logo, version, development team and external contributors;
2. a copy of the input file;
3. a job summary (method, reference, Hamiltonian, basis, integrals, frozen core,
   memory, threads);
4. the molecule (coordinates in Angstrom, number of basis functions and
   electrons, nuclear repulsion energy);
5. the SCF iterations (energy, energy change, gradient norm, density change)
   and the converged energy;
6. all orbital energies (spinor energies for DHF) in Eh and eV with
   occupations, the frozen-core orbitals marked, and the HOMO–LUMO gap;
7. the correlated method: frozen core, active orbitals, incore level, and the
   energies (for MP2 with RHF: opposite-spin, same-spin, correlation and total
   energy);
8. the total run time.

`printlevel 3` adds timings, memory use and batch sizes; `printlevel 1` prints
only the final energies.

All numbers are also written to `water_mp2.results.json`
(see [Results file](results_file.md)), which is the file to read from scripts.
