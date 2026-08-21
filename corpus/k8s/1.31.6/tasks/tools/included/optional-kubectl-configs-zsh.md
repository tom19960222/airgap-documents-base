---
collection: k8s
version: "1.31.6"
title: "zsh auto-completion"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/tasks/tools/included/optional-kubectl-configs-zsh.md
fetched_at: 2026-01-16T10:18:07+05:30
---
The kubectl completion script for Zsh can be generated with the command `kubectl completion zsh`. Sourcing the completion script in your shell enables kubectl autocompletion.

To do so in all your shell sessions, add the following to your `~/.zshrc` file:

```zsh
source <(kubectl completion zsh)
```

If you have an alias for kubectl, kubectl autocompletion will automatically work with it.

After reloading your shell, kubectl autocompletion should be working.

If you get an error like `2: command not found: compdef`, then add the following to the beginning of your `~/.zshrc` file:

```zsh
autoload -Uz compinit
compinit
```
