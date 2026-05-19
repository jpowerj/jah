# ...JupyterHub doesn't seem to allow viewing dot files/folders in the UI.
# So, this renames "github" to ".github" before pushing
cp github .github
git add -A .
git commit -m "Auto-push"
git push
