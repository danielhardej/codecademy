#### Why use the command below?

    git checkout HEAD filename

- [ ] To unstage the file from the staging area
- [ ] To move HEAD to a previous commit
- [x] To restore a file in the working directory to look as it did in your last commit
- [ ] To remove a file from a previous commit

#### Why use Git backtracking commands?

- [ ] To unstage a file from the staging area
- [x] All of these
- [ ] To discard changes in the working directory
- [ ] To go back to a previous commit

#### What Git command gives the output below?

    Unstaged changes after reset:              
    M       file.txt

- [ ] git status
- [x] git reset HEAD file.txt
- [ ] git delete filename
- [ ] git add file.txt

#### Which Git command lets you view the SHAs of all previous commits?

- [x] git log
- [ ] git checkout HEAD filename
- [ ] git reset SHA
- [ ] git status

#### You accidentally deleted lines from a file. Which command can undo your mistake?

- [ ] git reset HEAD filename
- [ ] git add filename
- [x] git checkout HEAD filename
- [ ] git commit -m “message”

#### Which statement is true about the command below?

    git reset 844d1f7

- [ ] It should be typed as “git 844d1f7 reset”
- [ ] The command will not work unless the SHA is in quotes
- [ ] The command will not work without the “-m” option
- [x] HEAD will be reset to the commit whose SHA starts with 844d1f7

#### Which command removes file changes from the staging area?

- [ ] git reset SHA
- [x] git reset HEAD filename
- [ ] git checkout HEAD filename
- [ ] git add filename_1 filename_2

#### In Git, the HEAD commit is

- [ ] Code that runs before you checkout a commit
- [ ] The default commit made during the “git init” command
- [x] The commit you are currently on
- [ ] The first commit deleted from a repository
