# JAH (Jeff's AutoHinter)

For data science and public policy courses at Georgetown.

## Publishing to PyPI

There are a few steps where, if one is skipped, the project won't update on PyPI!

1. Increment the version number (can use semantic versioning etc.) in `pyproject.toml`
2. Run `python3 -m build`, which will create new `tar.gz` files in the `dist` directory corresponding to the new version number
3. Run `add-dots.sh`, which just handles the annoying-ness of JupyterHub's interface not allowing me to see dotfiles
4. Push to github like usual

## Testing the PyPI Version

1. Create a new virtual environment with e.g. `python3 -m venv .venv`
2. Activate that environment with `source .venv/bin/activate`
3. Install `jah` into the virtual environment with `python3 -m pip install jah`
4. Start a Python REPL shell with `python`
5. Try importing and using `jah`
6. Use `quit()` to exit the Python REPL shell
7. Uninstall with `python3 -m pip uninstall jah`
8. Deactivate the virtual environment by just typing `deactivate`

