# Git & GitHub Cheatsheet

## The Git Workflow

#### The workflow for Git collaborations typically follows this order:

1. Fetch and merge changes from the remote
2. Create a branch to work on a new project feature
3. Develop the feature on your branch and commit your work
4. Fetch and merge from the remote again (in case new commits were made while you were working)
5. Push your branch up to the remote for review

#### What is the Git remote?
A remote is a Git repository that lives outside your Git project folder. Remotes can live on the web, on a shared network or even in a separate folder on your local computer.

The Git Collaborative Workflow are steps that enable smooth project development when multiple collaborators are working on the same Git project.
We also learned the following commands


## Git Commands

### Inizialize a Repository

    git init

Creates a new Git repository from the current working directory.

### Status

    git status

Inspects the contents of the working directory and staging area.

### Git Add

    git add

Adds files from the working directory to the staging area

### Git Diff

    git diff
shows the difference between the working directory and the staging area

    git commit
permanently stores file changes from the staging area in the repository

    git log
shows a list of all previous commits

    git checkout HEAD filename
Discards changes in the working directory.

    git reset HEAD <filename>
Unstages file changes in the staging area.

    git reset <commit_SHA>
Resets to a previous commit in your commit history.

What is the difference between **checkout** and **reset** in Git?
https://discuss.codecademy.com/t/what-is-the-difference-between-checkout-and-reset/405720

### Git Branch

    git branch

Lists all a Git project’s branches.

    git branch <branch_name>

Creates a new branch.

    git branch -d <branch_name>

Deletes the branch specified.

### Git Checkout

    git checkout <branch_name>

Switches from one branch to another.

### Git Merge

    git merge <branch_name>

Used to join file changes from one branch to another.

    git merge origin/master

Merges origin/master into your local branch.

### Git Push

    git push origin <your_branch_name>

This command will push your branch up to the remote, origin. From there, collaborators can review your branch and merge your work into the master branch, making it part of the definitive project version.

### Git Clone

    git clone <remote_location> <clone_name>

Creates a local copy of a remote.

### Git Remote

    git remote -v

Lists the remote repositories of a Git project.

### Git Fetch

    git fetch

Fetches work from the remote into the local copy.
