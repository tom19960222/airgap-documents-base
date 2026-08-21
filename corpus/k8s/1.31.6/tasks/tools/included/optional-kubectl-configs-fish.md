---
collection: k8s
version: "1.31.6"
title: "fish auto-completion"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/tasks/tools/included/optional-kubectl-configs-fish.md
fetched_at: 2026-01-16T10:18:07+05:30
---
> **Note:**
>
> Autocomplete for Fish requires kubectl 1.23 or later.

The kubectl completion script for Fish can be generated with the command `kubectl completion fish`. Sourcing the completion script in your shell enables kubectl autocompletion.

To do so in all your shell sessions, add the following line to your `~/.config/fish/config.fish` file:

```shell
kubectl completion fish | source
```

After reloading your shell, kubectl autocompletion should be working.
