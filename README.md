# git_assignment_HeroVired
Calculator Plus App -- Git assignment 1 from HeroVired batch 16A:

Steps:

a. Repository named git_assignment_HeroVired created in my Github account - tb-repo

b. This repository is created as private repo 

c. A new folder is created on my machine for this assignment

d. Open VSCode from the new assignment folder created

e. Open terminal and run 
    git init

f. Now clone the main repo from Git to local machine
    git clone git@github.com:tb-repo/git_assignment_HeroVired.git

g. Create a new branch called 'dev'
    git branch dev

h. Move to dev branch
    git checkout dev

i. Create a new file named app.py that will hold the main application code. Make sure that you set the right Python interpretor on the VSCode

j. Add the basic calculator operations (add,sub,mul,div) program code as provided on the assignment

k. Execute the code and check the output (fix any errors):
    (base) PS D:\HeroVired\Assignments\git_assignment_HeroVired\git_assignment_HeroVired> & C:/Users/thiagarajanb/anaconda3/python.exe d:/HeroVired/Assignments/git_assignment_HeroVired/git_assignment_HeroVired/app.py
    16 + 4 = 20
    16 - 4 = 12
    16 * 4 = 64
    16 / 4 = 4.0

h. Commit the version 1 of this app in dev branch and push to repo:
    (base) PS D:\HeroVired\Assignments\git_assignment_HeroVired\git_assignment_HeroVired> git add .
    (base) PS D:\HeroVired\Assignments\git_assignment_HeroVired\git_assignment_HeroVired> git commit -m "Version 1 of calculator plus app"
    [dev 5e902d7] Version 1 of calculator plus app
    3 files changed, 57 insertions(+), 1 deletion(-)
    create mode 100644 .vscode/settings.json
    create mode 100644 app.py
    (base) PS D:\HeroVired\Assignments\git_assignment_HeroVired\git_assignment_HeroVired> git status
    On branch dev
    nothing to commit, working tree clean
    (base) PS D:\HeroVired\Assignments\git_assignment_HeroVired\git_assignment_HeroVired> git push -u origin dev
    Enumerating objects: 11, done.
    Counting objects: 100% (11/11), done.
    Delta compression using up to 8 threads
    Compressing objects: 100% (8/8), done.
    Writing objects: 100% (9/9), 1.67 KiB | 341.00 KiB/s, done.
    Total 9 (delta 2), reused 0 (delta 0), pack-reused 0 (from 0)
    remote: Resolving deltas: 100% (2/2), done.
    remote: 
    remote: Create a pull request for 'dev' on GitHub by visiting:
    remote:      https://github.com/tb-repo/git_assignment_HeroVired/pull/new/dev
    remote:
    To github.com:tb-repo/git_assignment_HeroVired.git
    * [new branch]      dev -> dev
    branch 'dev' set up to track 'origin/dev'.

i. Merge the dev and main branch
    (base) PS D:\HeroVired\Assignments\git_assignment_HeroVired\git_assignment_HeroVired> git checkout main
    Switched to branch 'main'
    Your branch is up to date with 'origin/main'.
    (base) PS D:\HeroVired\Assignments\git_assignment_HeroVired\git_assignment_HeroVired> git merge dev
    Updating dec7aaf..752acfd
    Fast-forward
    .vscode/settings.json |  4 ++++
    README.md             | 65 ++++++++++++++++++++++++++++++++++++++++++++++++++-
    app.py                | 19 +++++++++++++++
    3 files changed, 87 insertions(+), 1 deletion(-)
    create mode 100644 .vscode/settings.json
    create mode 100644 app.py
    