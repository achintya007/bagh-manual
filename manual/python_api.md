# Using BAGH from Python

```python
from bagh.frontend.input_parser import parse_text
from bagh.frontend.driver import run

opts = parse_text(open("water_mp2.inp").read(), job_name="water_mp2")
scf, results = run(opts)
print(scf["energy"], results[0].energies["e_corr"])
```

`results` is a list of `Result` objects with `energies`, `metadata` and (for
developers) `intermediates`. A loop over molecules, basis sets or settings is
ordinary Python.
