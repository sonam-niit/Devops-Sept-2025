# Push Code to Remote Repo

- open the existing folder of last session in GitBash
- set up one repository on GitHub.com
- click repositories -> new -> give repo name like git demo
- keep it public only, don't add anything like gitignore or readme etc.. 
- just create

- Once repo created then run below commands to push

```bash
git branch -M main # make default branch as main from master
git branch # you can see you have only one branch main
git remote add origin url_of_git_repo # to set origin
git remote -v # to verify origin
git push -u origin main # push to the upstream main branch

# -u origin main is used to set upsteam branch 
# this req to run only once later on you can just say git push, it will push to main branch
```

## Reset the Origin If set some orign by mistake.
```bash
git remote set-url url_of_git_repo
```