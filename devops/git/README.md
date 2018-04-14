# git

# summary

history
- manually copy
- local vcs: e.g. rcs.
- centralized vcs: support collaborate. e.g. cvs, subversion. drawback: single point of failure.
- distributed vcs: fully checkout. e.g. git, mercurial.

git
- snapshots, not differences: efficient.
- mostly local operation: support offline control.
- integrity: impl by SHA-1 hash.
- only add data: support undo.

states
- https://git-scm.com/book/en/v2/Git-Tools-Reset-Demystified
- checkout <file>
- add, rm --cached, reset HEAD <file>
- commit, commit --amend,
- git log -p -2 

branch
- branch -v
- checkout -b
- merge
- rebase: support commits apply cleanly to remote, e.g. open-source contribution, composite commits into one before push. WARNING: do NOT rebase commits that exist outside your repository.

remote
- remote -v
- remote show <remote>
- fetch, pull, push

transfer protocol
- local
- http: dump, smart. e.g. github.
- ssh
- git: daemon on port 9418.

workflow
- centralized: typical project.
- intergation-manager: official project.
- dictator and lieutenants: huge project e.g. linux kernel.

other features
- stash
- tag: support importance mark. lightweight tag=tag, annotated tag=tag -a.
- hooks: trigger custom scripts by events.
- alias: e.g. git config --global alias.unstage 'reset HEAD --'.
- credential cache: git config --global credential.helper cache

# usecase

my config
~~~~
git config --global user.name "tang"
git config --global user.email maxtangli@qq.com
git config --global core.autocrlf input
~~~~

create pushable repository
~~~~
cd /vagrant/sonico/devops/jenkins/guided-tour/remote/
git init --bare

cd /vagrant/sonico/devops/jenkins/guided-tour/local/
git init
git commit
git remote add origin file:///vagrant/sonico/devops/jenkins/guided-tour/remote/
git push origin --all

git clone file:///vagrant/sonico/devops/jenkins/guided-tour/remote/ local-pulled

git ls-remote -h file:///vagrant/sonico/devops/jenkins/guided-tour/remote/ HEAD
~~~~

join commits to keep clean commit history
~~~~
git reset --soft <your-commit>
git commit --amend
~~~~

rebase feature branch to keep clean merge history
~~~~
git checkout my-branch
git rebase master

git checkout master
git merge my-branch
~~~~

undo add
~~~~
git rm --cached <file>
git reset
~~~~

undo commit or merge
~~~~
# commit -> untracked
git reset ~HEAD

# commit -> staging
git reset --soft
~~~~

undo push
~~~~
# make sure no other fetchs
git push -f origin last_known_good_commit:branch_name
~~~~

# eol

all files convert crlf -> lf
~~~~
rubymine: settings/editor/code style
rubymine: file/line separators
~~~~

all files ensure newline at end of file
~~~~
rubymine: settings/editor/general/Ensure line feed at file end on save
~~~~

git config
~~~~
# Sets the line ending type to use in the working directory for files that have the text property set when core.autocrlf is false.
git config --global core.eol lf
# Setting this variable to "true" is the same as setting the text attribute to "auto" on all files and core.eol to "crlf".
git config --global core.autocrlf input
~~~~

.gitattributes
~~~~
# Autodetect text files
* text=auto

# ...Unless the name matches the following
# overriding patterns

# Definitively text files 
*.txt text
*.c text
*.h text

# Ensure those won't be messed up with
*.jpg binary
*.data binary
~~~~

# internal

~~~~
$ ls -F1
config # project specified config
description # gitweb
HEAD # pointer to current branch
hooks/ # hook script
info/ # e.g. global ignored
objects/ # store contents in kvs by tree of blobs
refs/ # pointer to any branches
~~~~