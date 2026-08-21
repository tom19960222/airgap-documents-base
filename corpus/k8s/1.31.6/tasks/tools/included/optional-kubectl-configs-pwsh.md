---
collection: k8s
version: "1.31.6"
title: "PowerShell auto-completion"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/tasks/tools/included/optional-kubectl-configs-pwsh.md
fetched_at: 2026-01-16T10:18:07+05:30
---
The kubectl completion script for PowerShell can be generated with the command `kubectl completion powershell`.

To do so in all your shell sessions, add the following line to your `$PROFILE` file:

```powershell
kubectl completion powershell | Out-String | Invoke-Expression
```

This command will regenerate the auto-completion script on every PowerShell start up. You can also add the generated script directly to your `$PROFILE` file.

To add the generated script to your `$PROFILE` file, run the following line in your powershell prompt:

```powershell
kubectl completion powershell >> $PROFILE
```

After reloading your shell, kubectl autocompletion should be working.
