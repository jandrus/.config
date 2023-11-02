set -U fish_greeting ""


# PATHS
export PATH="$HOME/.config/emacs/bin:$HOME/.local/bin:$HOME/.composer/vendor/bin:$PATH"

if status is-interactive
	alias ls='exa'
	alias l='exa'
	alias ll='exa -l --icons'
	alias la='exa --icons -ld .*'
	alias grep='rg'
	alias cp="cp -i"                          # confirm before overwriting something
	alias df='df -h'                          # human-readable sizes
	alias free='free -m'                      # show sizes in MB
	alias cat='bat'
	alias tree='exa -la --tree --icons'
	alias tre='exa -a --tree --icons'
	alias userlist="cut -d: -f1 /etc/passwd | sort"
	alias sizeof="du -sh"
	alias shuty='sudo shutdown now'
	alias v='nvim'
	alias :q='exit'
	alias :w='cowsay -d "A specter is haunting the modern world"'
end



neofetch
