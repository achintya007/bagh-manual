# BAGH 1.0

BAGH is a quantum chemistry program for correlated electronic-structure methods
(coupled cluster, EOM-CC, ADC, perturbation theory), from non-relativistic to
two- and four-component relativistic Hamiltonians.

## How to read this manual

- New users: [Installation](installation.md) → [Getting started](getting_started.md).
- Looking up a keyword: [Keywords](input/keywords.md) (complete, generated from the code).
- Choosing a method: [Methods overview](methods/index.md) shows which method works
  with which reference, integral approximation and property.
- Running large jobs: [Run settings](run_settings.md) (memory, disk, threads).

```{toctree}
:maxdepth: 2
:caption: User manual

installation
getting_started
input/format
input/keywords
run_settings
references
integrals
methods/index
properties
results_file
python_api
troubleshooting
developer
```

## Citing BAGH

<!-- TODO: citation -->

## Licence of this manual

This manual is licensed under
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). The licence covers the
manual only, not the BAGH program.
