# Results file

Every run writes `<job>.results.json` next to the input. Read this file from
scripts instead of parsing the text output, whose layout may change.

```text
{
  "schema_version": 1,
  "program": "bagh",
  "input":   {"method": "MP2", "basis": "cc-pvdz", "df": false},
  "scf":     {"reference": "RHF", "energy": -75.98979, "natm": 3, "nao": 24, ...},
  "results": [
    {"method": "MP2", "backend": "cpp",
     "energies": {"e_corr_os": ..., "e_corr_ss": ..., "e_corr": ..., "e_total": ...},
     "metadata": {"incore_level": 5, "batch_size": 5, "n_batches": 1,
                  "peak_memory_mb": 0.07, "wall_time_s": 0.02}}
  ]
}
```

Energies are in hartree. `schema_version` changes only when existing fields
change meaning or are removed.
