# JAH (Jeff's AutoHinter)

For data science and public policy courses at Georgetown. This repo combines two formerly-separate repos: one for the **Python package** that gets imported in each student's notebook, and another for the **documentation** of the package.

## (1) Publishing to PyPI

There are a few steps where, if one is skipped, the project won't update on PyPI!

1. Increment the version number (can use semantic versioning etc.) in `pyproject.toml`
2. Run `python3 -m build`, which will create new `tar.gz` files in the `dist` directory corresponding to the new version number
3. Run `add-dots.sh`, which just handles the annoying-ness of JupyterHub's interface not allowing me to see dotfiles
4. Push to github like usual

### Testing the PyPI Version

1. Create a new virtual environment with e.g. `python3 -m venv .venv`
2. Activate that environment with `source .venv/bin/activate`
3. Install `jah` into the virtual environment with `python3 -m pip install jah`
4. Start a Python REPL shell with `python`
5. Try importing and using `jah`
6. Use `quit()` to exit the Python REPL shell
7. Uninstall with `python3 -m pip uninstall jah`
8. Deactivate the virtual environment by just typing `deactivate`

## (2) Package Documentation

The documentation of the package uses [Zensical](https://zensical.org/). The goal of Zensical, in theory, is to streamline the conversion of codebases into documentation (for example, by automatically converting in-code comment strings into pieces of the documentation). Here we don't use thse fancy features, so it essentially just becomes a... static site publishing system like Jekyll.

All of the Zensical operations here should be run within the custom virtual environment for the docs, by first running:

```bash
source .venv/bin/activate
```

You should then see a `(jag)` prefix in the Terminal shell, indicating that you're working within this virtual environment.

### Previewing Documentation

The documentation pages are drawn from the `docs` subfolder. To preview what it looks like, run

```
zensical serve
```


