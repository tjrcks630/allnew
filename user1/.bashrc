# .bashrc

# User specific aliases and functions

alias rm='rm -i'
alias cp='cp -i'
alias mv='mv -i'

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi
alias c='clear'
alias h='history'
alias df='df -Th'
alias grep='grep --color=auto'
alias egrep='egrep --color=auto'
alias fgrep='fgrep --color=auto'
alias ls='ls -aCF --color=auto'
alias ll='ls -alF --color=auto'

export PS1='[\[\e[1;31m\]\u\[\e[m\]@\[\e[1;32m\]\h\[\e[m\] \[\e[1;36m\]\w\[\e[m\]]\$ '

