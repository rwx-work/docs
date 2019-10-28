*********
Configure
*********

Configuration
=============

* etc/bash.bashrc

.. code:: bash

  file="/usr/share/bash-completion/bash_completion"
  if [ -f "${file}" ]; then
      source "${file}"
  fi

  PS1="\
  ┌ \e[0;31m\t\e[0m\
   – \e[0;32m\${?}\e[0m\
   – \e[0;33m\u\e[0m\
   @ \e[0;34m\h\e[0m\
  "
  if git --version &> /dev/null; then
      PS1="${PS1} –\e[0;35m\$(__git_ps1)\e[0m"
  fi
  PS1="${PS1}\n\
  │\e[0;36m\${PWD}\e[0m\n\
  └ "
  PS2="\
  └ "

  file="/etc/bash.alias"
  if [ -f "${file}" ]; then
      source "${file}"
  fi

Alias
=====

* etc/bash.alias

Described
---------

.. code:: bash

  # apt

  # update packages catalog
  alias aud='apt-get update'

  # show package information
  alias a='apt-cache show'

  # package versions policy
  alias ap='apt-cache policy'

  # upgrade forbidding package installation or removal
  alias aug='apt-get upgrade'

  # upgrade allowing package installation or removal
  alias adu='apt-get dist-upgrade'

  # install packages
  alias ai='apt-get install'

  # clean packages cache
  alias ac='apt-get autoclean;apt-get clean;apt-get autoremove'

  # bash

  # clear terminal
  alias c='clear'

  # exit terminal
  alias x='exit'

  # change current directory to its parent
  alias ..='cd ..'

  # make a directory
  alias md='mkdir'

  # make a directory after making its parents
  alias mdp='mkdir --parents'

  # change current directory to the previous one
  alias pd='cd -'

  # change mode as directory
  alias cmd='chmod 755'

  # change mode as file
  alias cmf='chmod 644'

  # change owner as root
  alias cor='chown 0:0'

  # change owner as user
  alias cou='chown 1000:1000'

  # look for a string in processes names
  alias pg='ps -A|grep'

  # kill a process by id
  alias k='kill -9'

  # kill all instances of a process by name
  alias ka='killall'

  # grep from current directory with regex
  alias g='grep -rn . -e'

  # list current directory entries
  alias l='ls --all --color -l -p --time-style="+%Y%m%d-%H%M%S%-:::z"'

  # git

  # add to index
  alias ga='git add'

  # add all to index
  alias gaa='git add --all'

  # add interactively
  alias gai='git add --interactive'

  # create a branch
  alias gb='git branch'

  # delete a branch
  alias gbd='git branch --delete'

  # force a branch deletion
  alias gbdf='git branch --delete --force'

  # list branches
  alias gbl='git branch --all --list --verbose --verbose'

  # set the link to a remote branch from a local branch
  alias gbu='git branch -u'

  # clone a remote repository
  alias gc='git clone'

  # clean untracked files
  alias gcf='git clean -d --force'

  # index all and commit
  alias gacm='git add --all;git commit -m'

  # commit the index
  alias gcm='git commit -m'

  # redo the last commit with a different message
  alias gcma='git commit --amend -m'

  # make a root commit
  alias gcmr='git commit --allow-empty --allow-empty-message -m ""'

  # switch to a branch or checkout file(s) from a commit
  alias gco='git checkout'

  # checkout an orphan branch
  alias gcoo='git checkout --orphan'

  # checkout development branch
  alias gcod='git checkout dev'

  # checkout feature branch
  alias gcof='git checkout f'

  # pick a commit
  alias gcp='git cherry-pick'

  # abort the commit pick
  alias gcpa='git cherry-pick --abort'

  # continue the commit pick
  alias gcpc='git cherry-pick --continue'

  # configure the user name
  alias gcun='git config user.name'

  # configure the user email
  alias gcue='git config user.email'

  # differences from last or between commits
  alias gd='git diff'

  # display what is indexed in cache
  alias gdc='git diff --cached'

  # differences via external tool
  alias gdt='git difftool --dir-diff'

  # differences via external tool
  alias gdw='git diff --word-diff-regex=.'

  # fetch from the remote repository
  alias gf='git fetch --tags --verbose'

  # fetch from remote repository and prune local orphan branches
  alias gfp='git fetch --prune --tags --verbose'

  # garbage collect all orphan commits
  alias ggc='git reflog expire --expire=now --all;git gc --prune=now'

  # initialize a new repository
  alias gi='git init'

  # initialize a new bare repository
  alias gib='git init --bare'

  # log commits history
  alias gl='git log --all --graph \
  --format="%C(auto)%h%d %C(red)%ai%n%C(auto)%B"'

  # log commits history with patches
  alias glp='git log --all --graph \
  --format="%C(auto)%h%d %C(red)%ai%n%C(auto)%B" --patch'

  # log medium information
  alias glm='git log --all --decorate --graph --pretty=medium'

  # fast-forward to remote branch
  alias gmf='git merge --ff-only'

  # do a merge commit
  alias gmc='git merge --no-ff -m'

  # abort the current merge commit
  alias gma='git merge --abort'

  # squash a branch and index its modifications
  alias gms='git merge --squash'

  # merge via external tool
  alias gmt='git mergetool'

  # push to the remote repository
  alias gp='git push --set-upstream --verbose'

  # delete from the remote repository
  alias gpd='git push --verbose --delete'

  # force the push to the remote repository
  alias gpf='git push --set-upstream --verbose --force'

  # rebase current branch onto another
  alias grb='git rebase'

  # abort current rebase
  alias grba='git rebase --abort'

  # continue current rebase
  alias grbc='git rebase --continue'

  # force rebase without fast-forward
  alias grbf='git rebase --no-ff'

  # rebase interactively
  alias grbi='git rebase --interactive'

  # list all remote repositories
  alias grm='git remote'

  # add a new remote repository
  alias grma='git remote add'

  # list remote repositories
  alias grml='git remote --verbose'

  # show a connection to a repository
  alias grms='git remote show'

  # set the location of the remote repository
  alias grmu='git remote set-url'

  # remove file(s) from index or move current branch pointer
  alias grs='git reset'

  # move current branch pointer to the development branch
  alias grsd='git reset dev'

  # wipe modifications or reset current branch to another commit
  alias grsh='git reset --hard'

  # reset current branch to the development branch
  alias grshd='git reset --hard dev'

  # current state of repository
  alias gs='git status --untracked-files=all'

  # show a commit
  alias gsh='git show'

  # tag a commit
  alias gt='git tag'

  # delete a tag
  alias gtd='git tag --delete'

  # rsync

  # synchronize
  alias rs='rsync --archive --no-whole-file --progress --verbose'

  # no synchronize
  alias rsn='rsync --archive --no-whole-file --progress --verbose -n'

  # synchronize and delete
  alias rsd='rsync --archive --no-whole-file --progress --verbose --delete'

  # synchronize and delete
  alias rsdn='rsync --archive --no-whole-file --progress --verbose --delete -n'

Old
---

.. code:: bash

  alias c="clear"
  alias cmd="chmod 755"
  alias cmf="chmod 644"
  alias cor="chown 0:0"
  alias cou="chown 1000:1000"
  alias k="kill -9"
  alias ka="killall -9"
  alias l="ls --all --color=always -l \
  --indicator-style=slash --time-style=\"+%Y%m%d-%H%M%S%-:::z\""
  alias pg="ps -A|grep"
  alias x="exit"

  alias a="apt-cache show"
  alias ac="apt-get autoclean;apt-get clean;apt-get autoremove"
  alias acl="apt-get changelog"
  alias adl="apt-get download"
  alias adu="apt-get dist-upgrade"
  alias adus="apt-get dist-upgrade --simulate"
  alias adub="apt-get dist-upgrade --target-release stretch-backports"
  alias adubs="apt-get dist-upgrade --target-release stretch-backports --simulate"
  alias af="apt-get --fix-broken install"
  alias afs="apt-get --fix-broken install --simulate"
  alias ai="apt-get install"
  alias ais="apt-get install --simulate"
  alias aib="apt-get install --target-release stretch-backports"
  alias aibs="apt-get install --target-release stretch-backports --simulate"
  alias ait="apt-get install --target-release testing"
  alias aits="apt-get install --target-release testing --simulate"
  alias aiu="apt-get install --target-release unstable"
  alias aius="apt-get install --target-release unstable --simulate"
  alias ap="apt-cache policy"
  alias as="apt-cache search"
  alias asrc="apt-get source"
  alias aud="apt-get update"
  alias aug="apt-get upgrade"
  alias augs="apt-get upgrade --simulate"
  alias augb="apt-get upgrade --target-release stretch-backports"
  alias augbs="apt-get upgrade --target-release stretch-backports --simulate"

  alias ga="git add"
  alias gaa="git add --all"
  alias gb="git branch"
  alias gbd="git branch --delete"
  alias gbdf="git branch --delete --force"
  alias gbl="git branch --all --list --verbose --verbose"
  alias gbu="git branch -u"
  alias gc="git clone"
  alias gcf="git clean -d --force"
  alias gcm="git commit -m"
  alias gcma="git commit --amend -m"
  alias gcme="git commit --allow-empty --allow-empty-message -m"
  alias gco="git checkout"
  alias gcob="git checkout -b"
  alias gcoo="git checkout --orphan"
  alias gcp="git cherry-pick"
  alias gcpa="git cherry-pick --abort"
  alias gcpc="git cherry-pick --continue"
  alias gcue="git config user.email"
  alias gcun="git config user.name"
  alias gd="git diff"
  alias gdc="git diff --word-diff-regex=."
  alias gdt="git difftool --dir-diff"
  alias gf="git fetch --tags --verbose"
  alias gfsnr="git fsck --no-progress --no-reflogs"
  alias ggc="git reflog expire --expire=now --all; git gc --prune=now"
  alias gi="git init"
  alias gib="git init --bare"
  alias gl="git log --abbrev-commit --all --decorate --graph --format=oneline"
  alias gla="git log --all --decorate --graph \
  --format=\"%C(auto)%h %C(red)%an%C(auto)%d %C(reset)%s\""
  alias glm="git log --all --decorate --graph --format=medium"
  alias gma="git merge --abort"
  alias gmc="git merge --no-ff -m"
  alias gmf="git merge --ff-only"
  alias gms="git merge --squash"
  alias gmt="git mergetool"
  alias gp="git push --set-upstream --tags --verbose"
  alias gpd="git push --delete origin"
  alias grb="git rebase"
  alias grba="git rebase --abort"
  alias grbc="git rebase --continue"
  alias grbi="git rebase --interactive"
  alias grma="git remote add origin"
  alias grmc="git rm --cached"
  alias grms="git remote show origin"
  alias grmu="git remote set-url origin"
  alias grs="git reset"
  alias grsh="git reset --hard"
  alias grshd="git reset --hard dev"
  alias grshm="git reset --hard master"
  alias gs="git status --untracked-files"
  alias gsc="git show"
  alias gt="git tag"
  alias gtd="git tag --delete"

  alias rs="rsync --archive --progress --verbose"
  alias rsn="rsync --archive --progress --verbose -n"
  alias rsd="rsync --archive --progress --verbose --delete"
  alias rsdn="rsync --archive --progress --verbose --delete -n"

  alias tc="tar --numeric-owner --verbose --create --auto-compress --file"
  alias tx="tar --numeric-owner --verbose --extract --file"
