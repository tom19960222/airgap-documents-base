---
collection: gitlab
version: "17.9.8"
title: "Install Git"
source_url: https://gitlab.com/gitlab-org/gitlab/-/blob/v17.9.8-ee/doc/topics/git/how_to_install_git/_index.md
fetched_at: 2025-05-07T10:05:15Z
---
To contribute to GitLab projects, you must download and install the Git client on your local machine.
This page explains how to install and configure Git on macOS and Ubuntu Linux.

For information on downloading and installing Git on other operating systems, see the
[official Git website](https://git-scm.com/downloads).

After you install and configure Git, [generate and add an SSH key pair](../../../user/ssh.md#generate-an-ssh-key-pair)
to your GitLab account. GitLab uses the SSH protocol to securely communicate with Git.
With SSH, you can authenticate to the GitLab remote server without entering your username and password each time.

## Install and update Git

**Tab: macOS**

Though a version of Git is supplied by macOS, you should install the latest version of Git. A common way to
install Git is with [Homebrew](https://brew.sh/index.html).

To install the latest version of Git on macOS with Homebrew:

1. If you've never installed Homebrew before, follow the
   [Homebrew installation instructions](https://brew.sh/index.html).
1. In a terminal, install Git by running `brew install git`.
1. Verify that Git works on your local machine:

   ```shell
   git --version
   ```

Keep Git up to date by periodically running the following command:

```shell
brew update && brew upgrade git
```

**Tab: Ubuntu Linux**

Though a version of Git is supplied by Ubuntu, you should install the latest version of Git. The latest version is
available using a Personal Package Archive (PPA).

To install the latest version of Git on Ubuntu Linux with a PPA:

1. In a terminal, configure the required PPA, update the list of Ubuntu packages, and install `git`:

   ```shell
   sudo apt-add-repository ppa:git-core/ppa
   sudo apt-get update
   sudo apt-get install git
   ```

1. Verify that Git works on your local machine:

   ```shell
   git --version
   ```

Keep Git up to date by periodically running the following command:

```shell
sudo apt-get update && sudo apt-get install git
```

## Configure Git

To start using Git from your local machine, you must enter your credentials
to identify yourself as the author of your work.

You can configure your Git identity locally or globally:

- Locally: Use for the current project only.
- Globally: Use for all current and future projects.

**Tab: Local setup**

Configure your Git identity locally to use it for the current project only.

The full name and email address should match the ones you use in GitLab.

1. In your terminal, add your full name. For example:

   ```shell
   git config --local user.name "Alex Smith"
   ```

1. Add your email address. For example:

   ```shell
   git config --local user.email "your_email_address@example.com"
   ```

1. To check the configuration, run:

   ```shell
   git config --local --list
   ```

**Tab: Global setup**

Configure your Git identity globally to use it for all current and future projects on your machine.

The full name and email address should match the ones you use in GitLab.

1. In your terminal, add your full name. For example:

   ```shell
   git config --global user.name "Sidney Jones"
   ```

1. Add your email address. For example:

   ```shell
   git config --global user.email "your_email_address@example.com"
   ```

1. To check the configuration, run:

   ```shell
   git config --global --list
   ```

### Check Git configuration settings

To check your configured Git settings, run:

```shell
git config user.name && git config user.email
```

## Related topics

- [Git configuration documentation](https://git-scm.com/book/en/v2/Customizing-Git-Git-Configuration)
- [Use SSH keys to communicate with GitLab](../../../user/ssh.md)
