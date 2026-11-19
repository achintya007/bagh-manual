# Input format

BAGH 1.0 reads the same input format as BAGH 0.x:

```text
! MP2 cc-pvdz DF Bohr        # method, basis set and flags
%maxcore 2000                # one keyword on one line ...
%cc                          # ... or several in a block (block name is free)
  fc     true
  incore 3
end
*xyz 0 1                     # charge and spin multiplicity
O  0.000  -0.143  0.000
H  1.638   1.137  0.000
H -1.638   1.137  0.000
*
```

- Everything after `#` is a comment.
- **`!` line:** the method name, the orbital basis set and any of these flags:
  `Bohr`, `Angstrom` (default), `DF` or `RI` (density fitting), `CD` (Cholesky),
  `DHF` (four-component reference), `SFX2C1E`, `FC` / `NOFC` (frozen core on / off;
  **on by default**, unlike BAGH 0.x).
  A word ending in `-ri` (e.g. `cc-pvdz-ri`) sets the RI auxiliary basis
  (`auxbasis`); a word ending in `jkfit` (e.g. `ccpvdzjkfit`) sets the DF-SCF basis
  (`jkbasis`).
- **`%` lines and blocks:** any keyword from the [keyword list](keywords.md).
  Unknown keywords are an error, so typing mistakes are caught.
- **`*xyz charge multiplicity`** starts the geometry; a line with only `*` ends it.
