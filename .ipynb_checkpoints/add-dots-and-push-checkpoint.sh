# ...JupyterHub doesn't seem to allow viewing dot files/folders in the UI.
# So, this renames "github" to ".github" before pushing
rm -rf .github
mkdir .github
cp -r github/* .github
# And copy gitignore to .gitignore
cp gitignore .gitignore
git add -A .
git commit -m "Auto-push"
git push
