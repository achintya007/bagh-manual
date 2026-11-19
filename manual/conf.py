"""Sphinx configuration for the BAGH 1.0 manual (built on Read the Docs)."""

project = "BAGH"
author = "BAGH developers"
copyright = "2026, BAGH developers. Manual licensed under CC BY 4.0"
release = "1.0.0.dev0"

extensions = [
    "myst_parser",       # write pages in Markdown
    "sphinx.ext.mathjax",
]
myst_enable_extensions = ["dollarmath", "amsmath", "colon_fence", "deflist"]
source_suffix = {".md": "markdown"}
exclude_patterns = ["_build", "methods/_template.md", "conf.py"]

html_theme = "sphinx_rtd_theme"
html_title = "BAGH 1.0 Manual"
