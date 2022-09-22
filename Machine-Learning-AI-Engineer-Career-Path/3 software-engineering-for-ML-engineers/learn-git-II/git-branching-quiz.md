#### You try to merge two branches which contain commits that alter a file in conflicting ways. This is called

- [ ] A reset
- [x] A merge conflict
- [ ] A fast-forward merge
- [ ] None of these

#### Merging a branch into “master”

- [ ] Will always result in a merge conflict
- [ ] Integrates changes made to “master” into the new branch
- [x] Integrates changes made on the new branch into “master”
- [ ] Cannot result in a merge conflict

#### Which command will list all branches for a Git project?

- [ ] git checkout branchname
- [x] git branch
- [ ] git list
- [ ] git show branches

#### A Git project has a branch “bug-fix”. How do you switch to it?

- [ ] git branch bug-fix
- [x] git checkout bug-fix
- [ ] git switch bug-switch
- [ ] git switch master bug-fix

#### Why is the branch name “my branch” invalid?

- [ ] The word “my” cannot be used
- [x] Branch names cannot contain whitespace
- [ ] Valid branch names must contain a dash
- [ ] Branch names must be capitalized

#### Which is a common reason Git users make a new branch?

- [ ] To duplicate “master” as a backup
- [ ] To see if the branch has the same commit history as “master”
- [ ] In case a merge conflict can’t be resolved
- [x] To develop a new project feature

#### The command below

    git branch new_branch

- [ ] Changes the name of a branch
- [x] Creates a new branch
- [ ] Lists the commit history of the new branch
- [ ] Switches you over to a new branch

#### What does the command below accomplish?

    git branch -d my-branch

- [ ] It will merge “my-branch” into “master”
- [ ] It will create and switch the user to “my-branch”
- [x] It will delete “my-branch”
- [ ] This is invalid Git syntax

#### When you are on “master” and create a new branch

- [ ] None of these
- [x] The new branch and “master” share the exact same commit history
- [ ] Every change you make to the new branch will also be made to “master”
- [ ] The “git branch” command will not list the new branch

#### What does the code below indicate?

    <<<<<<< HEAD -
     Intuitive and easy to use, providing crucial functionality
    =======
    - Intuitive and fun for use, offering the best in software
    >>>>>>> feature


- [ ] A successful merge
- [x] A merge conflict
- [ ] The output of “git status”
- [ ] Git’s code syntax checker

#### You’ve merged a branch called “new-feature” into “master”. Which is true?


- [x] “master” is the receiver branch
- [ ] “new-feature” is the receiver branch
- [ ] “master” is the giver branch
- [ ] “master” is the giver branch and “new-feature” is the receiver branch
