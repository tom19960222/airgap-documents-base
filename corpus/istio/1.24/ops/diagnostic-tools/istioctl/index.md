---
collection: istio
version: "1.24"
title: "Using the Istioctl Command-line Tool"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/ops/diagnostic-tools/istioctl/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "Istio includes a supplemental tool that provides debugging and diagnosis for Istio service mesh deployments."
---
You can gain insights into what individual components are doing by inspecting their
[logs](../component-logging/index.md) or peering inside via
[introspection](../controlz/index.md). If that's insufficient,
the steps below explain how to get under the hood.

The [`istioctl`](https://istio.io/v1.24/docs/reference/commands/istioctl) <!-- unresolved-site-link: route=/docs/reference/commands/istioctl --> tool is a configuration command line utility
that allows service operators to debug and diagnose their Istio service mesh deployments.
The Istio project also includes two helpful scripts for `istioctl` that enable auto-completion
for Bash and Zsh. Both of these scripts provide support for the currently available `istioctl` commands.

> **Tip:**
>
> `istioctl` only has auto-completion enabled for non-deprecated commands.

## Before you begin

We recommend you use an `istioctl` version that is the same version as your Istio control plane.
Using matching versions helps avoid unforeseen issues.

> **Tip:**
>
> If you have already [downloaded the Istio release](../../../setup/additional-setup/download-istio-release/index.md), you should
> already have `istioctl` and do not need to install it again.

## Install [istioctl]

Install the `istioctl` binary with `curl`:

1. Download the latest release with the command:

```bash
$ curl -sL https://istio.io/downloadIstioctl | sh -
```

1. Add the `istioctl` client to your path, on a macOS or Linux system:

```bash
$ export PATH=$HOME/.istioctl/bin:$PATH
```

1. You can optionally enable the [auto-completion option](#enabling-auto-completion) when working with a bash or Zsh console.

## Get an overview of your mesh

You can get an overview of your mesh using the `proxy-status` or `ps` command:

```bash
$ istioctl proxy-status
```

If a proxy is missing from the output list it means that it is not currently connected to an istiod instance and so it
will not receive any configuration. Additionally, if it is marked stale, it likely means there are networking issues or
istiod needs to be scaled.

## Get proxy configuration

[`istioctl`](https://istio.io/v1.24/docs/reference/commands/istioctl) <!-- unresolved-site-link: route=/docs/reference/commands/istioctl --> allows you to retrieve information
about proxy configuration using the `proxy-config` or `pc` command.

For example, to retrieve information about cluster configuration for the Envoy instance in a specific pod:

```bash
$ istioctl proxy-config cluster <pod-name> [flags]
```

To retrieve information about bootstrap configuration for the Envoy instance in a specific pod:

```bash
$ istioctl proxy-config bootstrap <pod-name> [flags]
```

To retrieve information about listener configuration for the Envoy instance in a specific pod:

```bash
$ istioctl proxy-config listener <pod-name> [flags]
```

To retrieve information about route configuration for the Envoy instance in a specific pod:

```bash
$ istioctl proxy-config route <pod-name> [flags]
```

To retrieve information about endpoint configuration for the Envoy instance in a specific pod:

```bash
$ istioctl proxy-config endpoints <pod-name> [flags]
```

See [Debugging Envoy and Istiod](../proxy-cmd/index.md) for more advice on interpreting this information.

## `istioctl` auto-completion

**Tabset (prereqs):**

**Tab: macOS**

If you are using the macOS operating system with the Zsh terminal shell, make sure that
the `zsh-completions` package is installed. With the [brew](https://brew.sh) package manager
for macOS, you can check to see if the `zsh-completions` package is installed with the following command:

```bash
$ brew list zsh-completions
/usr/local/Cellar/zsh-completions/0.34.0/share/zsh-completions/ (147 files)
```

If you receive `Error: No such keg: /usr/local/Cellar/zsh-completion`,
proceed with installing the `zsh-completions` package with the following command:

```bash
$ brew install zsh-completions
```

Once the `zsh-completions package` has been installed on your macOS system, add the following to your `~/.zshrc` file:

```plain
if type brew &>/dev/null; then
  FPATH=$(brew --prefix)/share/zsh-completions:$FPATH

  autoload -Uz compinit
  compinit
fi
```

You may also need to force rebuild `zcompdump`:

```bash
$ rm -f ~/.zcompdump; compinit
```

Additionally, if you receive `Zsh compinit: insecure directories` warnings
when attempting to load these completions, you may need to run this:

```bash
$ chmod -R go-w "$(brew --prefix)/share"
```

**Tab: Linux**

If you are using a Linux-based operating system, you can install the Bash completion package
with the `apt-get install bash-completion` command for Debian-based Linux distributions or
`yum install bash-completion` for RPM-based Linux distributions, the two most common occurrences.

Once the `bash-completion` package has been installed on your Linux system,
add the following line to your `~/.bash_profile` file:

```plain
[[ -r "/usr/local/etc/profile.d/bash_completion.sh" ]] && . "/usr/local/etc/profile.d/bash_completion.sh"
```

### Enabling auto-completion

To enable `istioctl` completion on your system, follow the steps for your preferred shell:

> **Warning:**
>
> You will need to download the full Istio release containing the auto-completion files (in the `/tools` directory).
> If you haven't already done so, [download the full release](../../../setup/additional-setup/download-istio-release/index.md) now.

**Tabset (profile):**

**Tab: Bash**

Installing the bash auto-completion file

If you are using bash, the `istioctl` auto-completion file is located in the `tools` directory.
To use it, copy the `istioctl.bash` file to your home directory, then add the following line to
source the `istioctl` tab completion file from your `.bashrc` file:

```bash
$ source ~/istioctl.bash
```

**Tab: Zsh**

Installing the Zsh auto-completion file

For Zsh users, the `istioctl` auto-completion file is located in the `tools` directory.
Copy the `_istioctl` file to your home directory, or any directory of your choosing
(update directory in script snippet below), and source the `istioctl` auto-completion file
in your `.zshrc` file as follows:

```zsh
source ~/_istioctl
```

You may also add the `_istioctl` file to a directory listed in the `fpath` variable.
To achieve this, place the `_istioctl` file in an existing directory in the `fpath`,
or create a new directory and add it to the `fpath` variable in your `~/.zshrc` file.

> **Tip:**
>
> If you get an error like `complete:13: command not found: compdef`,
> then add the following to the beginning of your `~/.zshrc` file:
>
>
>
> ```bash
> $ autoload -Uz compinit
> $ compinit
> ```
>
>
>
> If your auto-completion is not working, try again after restarting your terminal.
> If auto-completion still does not work, try resetting the completion cache using
> the above commands in your terminal.

### Using auto-completion

If the `istioctl` completion file has been installed correctly, press the Tab key
while writing an `istioctl` command, and it should return a set of command suggestions
for you to choose from:

```bash
$ istioctl proxy-<TAB>
proxy-config proxy-status
```
