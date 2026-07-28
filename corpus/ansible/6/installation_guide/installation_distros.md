---
collection: ansible
version: "6"
title: "Installing Ansible on specific operating systems"
source_url: https://docs.ansible.com/projects/ansible/6/installation_guide/installation_distros.html
fetched_at: 2026-07-27T16:39:39+00:00
---
# Installing Ansible on specific operating systems

The `ansible` package can always be [installed from PyPI using pip](intro_installation.md#intro-installation-guide) on most systems but it is also packaged and maintained by the community for a variety of Linux distributions.

The following instructions will guide you through installing the `ansible` package with your preferred distribution’s package manager.

- [Installing Ansible on Fedora or CentOS](installation_distros.md#installing-ansible-on-fedora-or-centos)
- [Installing Ansible on Ubuntu](installation_distros.md#installing-ansible-on-ubuntu)
- [Installing Ansible on Debian](installation_distros.md#installing-ansible-on-debian)
- [Installing Ansible on Windows](installation_distros.md#installing-ansible-on-windows)

## [Installing Ansible on Fedora or CentOS](installation_distros.md#id1)

On Fedora:

```bash
$ sudo dnf install ansible
```

On CentOS:

```bash
$ sudo yum install epel-release
$ sudo yum install ansible
```

RPMs for currently supported versions of CentOS are also available from [EPEL](https://fedoraproject.org/wiki/EPEL).

## [Installing Ansible on Ubuntu](installation_distros.md#id2)

Ubuntu builds are available [in a PPA here](https://launchpad.net/~ansible/+archive/ubuntu/ansible).

To configure the PPA on your system and install Ansible run these commands:

```bash
$ sudo apt update
$ sudo apt install software-properties-common
$ sudo add-apt-repository --yes --update ppa:ansible/ansible
$ sudo apt install ansible
```

> **Note:**
>
> On older Ubuntu distributions, “software-properties-common” is called “python-software-properties”. You may want to use `apt-get` rather than `apt` in older versions. Also, be aware that only newer distributions (that is, 18.04, 18.10, and later) have a `-u` or `--update` flag. Adjust your script as needed.

## [Installing Ansible on Debian](installation_distros.md#id3)

Debian users can use the same source as the Ubuntu PPA (using the following table).

| Debian |  | Ubuntu |
| --- | --- | --- |
| Debian 11 (Bullseye) | -> | Ubuntu 20.04 (Focal) |
| Debian 10 (Buster) | -> | Ubuntu 18.04 (Bionic) |

> **Note:**
>
> Ansible releases are only built for Ubuntu 18.04 (Bionic) or later releases.

Add the following line to `/etc/apt/sources.list` or `/etc/apt/sources.list.d/ansible.list`:

```bash
deb http://ppa.launchpad.net/ansible/ansible/ubuntu MATCHING_UBUNTU_CODENAME_HERE main
```

Example for Debian 11 (Bullseye)

```bash
deb http://ppa.launchpad.net/ansible/ansible/ubuntu focal main
```

Then run these commands:

```bash
$ sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 93C4A3FD7BB9C367
$ sudo apt update
$ sudo apt install ansible
```

## [Installing Ansible on Windows](installation_distros.md#id4)

You cannot use a Windows system for the Ansible control node. See [Can Ansible run on Windows?](../user_guide/windows_faq.md#windows-faq-ansible)

> **See also:**
>
> [Installing Ansible on ARch Linux](https://wiki.archlinux.org/title/Ansible#Installation)
> :   Distro-specific installation on Arch Linux
>
> [Installing Ansible on Clear Linux](https://clearlinux.org/software/bundle/ansible)
> :   Distro-specific installation on Clear Linux
