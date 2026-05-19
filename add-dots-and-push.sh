# ...JupyterHub doesn't seem to allow viewing dot files/folders in the UI.
# So, this renames "github" to ".github" before pushing
cp -r github .github
git add -A .
git commit -m "Auto-push"
git push
