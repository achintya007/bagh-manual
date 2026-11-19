# Visualising orbitals (Chemcraft, Avogadro, ...)

BAGH writes standard files that visualisation programs read directly.

## Molden file (RHF)

`<job>.molden` is written after every RHF SCF (keyword `molden`, on by default):
geometry, basis set, all SCF orbitals with energies and occupations. Open it in
**Chemcraft** (File → Open) or **Avogadro** (File → Open; then Extensions/Analyze →
Molecular Orbitals) to look at the structure and draw any orbital; Jmol, VMD,
Molden and IboView read it too. SFX2C1e orbitals are written the same way.

## Cube files

Give the orbitals to plot with `cube` — numbers as in the orbital table of the
output, and/or `homo`, `lumo`, `homo-N`, `lumo+N`:

```text
! MP2 cc-pvdz
%cube homo-1, homo, lumo
%cube_points 80        # grid points per direction (default 80)
```

RHF writes one cube per orbital: `<job>.mo5_homo.cube`, `<job>.mo6_lumo.cube`, ...
Open them in Chemcraft or Avogadro and draw isosurfaces (positive and negative
lobes).

## Four-component (DHF) spinors

A DHF spinor is complex and has four components (large α, large β, small α,
small β), so it cannot be stored in a Molden file, and a cube file holds only
real numbers. BAGH therefore writes:

| File | Content |
|---|---|
| `<job>.spinorN.density.cube` | spinor density $|\psi_N(\mathbf r)|^2$, summed over all four components; real, positive, independent of the spinor's arbitrary phase; the same for both spinors of a Kramers pair |
| `<job>.spinorN.re_La.cube`, `.im_La.cube`, `.re_Lb.cube`, `.im_Lb.cube` | with `cube_re_im true`: real and imaginary parts of the large-component α and β parts, which show nodes and lobes like an ordinary orbital |

A spinor is defined only up to a complex phase (and the two spinors of a Kramers
pair can be mixed), so BAGH fixes the phase by making the largest
large-component coefficient real and positive; the real/imaginary pictures are
then reproducible. The small component is about $1/(2c)$ of the large one and
matters only close to heavy nuclei; it is included in the density but not in the
real/imaginary files. No Molden file is written for DHF.

All files written are listed at the end of the SCF part of the output (section
*Files for visualisation*) and in the results file under `files`.
