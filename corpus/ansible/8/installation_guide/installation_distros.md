---
collection: ansible
version: "8"
title: "Installing Ansible on specific operating systems"
source_url: https://docs.ansible.com/projects/ansible/8/installation_guide/installation_distros.html
fetched_at: 2026-07-28T00:58:14+00:00
---
# Installing Ansible on specific operating systems

> **Note:**
>
> These instructions are provided by their respective communities. Any bugs/issues should be filed with that community to update these instructions. Ansible maintains only the `pip install` instructions.

The `ansible` package can always be [installed from PyPI using pip](intro_installation.md#intro-installation-guide) on most systems but it is also packaged and maintained by the community for a variety of Linux distributions.

The following instructions will guide you through installing the `ansible` package with your preferred distribution’s package manager.

> **Note:**
>
> For maintainers who wish to add distributions to this guide, installation instructions are included here only for distributions with a reasonably up-to-date version of `ansible`. The distribution MUST ensure that `ansible-core` and `ansible` versions are kept in sync to the extent that the distribution build system allows. Maintainers MUST include a way to contact them with their instructions here and are encouraged to join the [Ansible Packaging](https://matrix.to/#/#packaging:ansible.com) Matrix room.

- [Installing Ansible on Fedora Linux](installation_distros.md#installing-ansible-on-fedora-linux)
- [Installing Ansible from EPEL](installation_distros.md#installing-ansible-from-epel)
- [Installing Ansible on OpenSUSE Tumbleweed/Leap](installation_distros.md#installing-ansible-on-opensuse-tumbleweed-leap)
- [Installing Ansible on Ubuntu](installation_distros.md#installing-ansible-on-ubuntu)
- [Installing Ansible on Debian](installation_distros.md#installing-ansible-on-debian)
- [Installing Ansible on Arch Linux](installation_distros.md#installing-ansible-on-arch-linux)
- [Installing Ansible on Windows](installation_distros.md#installing-ansible-on-windows)

## [Installing Ansible on Fedora Linux](installation_distros.md#id3)

To install the batteries included `ansible` package on Fedora run

```bash
$ sudo dnf install ansible
```

If you prefer to install the minimal `ansible-core` package run

```bash
$ sudo dnf install ansible-core
```

Several Ansible collections are also available from the Fedora repositories as
standalone packages that users can install alongside `ansible-core`.
For example, to install the `community.general` collection run

```bash
$ sudo dnf install ansible-collection-community-general
```

See the [Fedora Packages index](https://packages.fedoraproject.org/search?query=ansible-collection)
for a full list of Ansible collections packaged in Fedora.

Please [file a bug](https://bugzilla.redhat.com/enter_bug.cgi) against the
`Fedora` product in Red Hat Bugzilla to reach the package maintainers.

## [Installing Ansible from EPEL](installation_distros.md#id4)

Users of CentOS Stream, Almalinux, Rocky Linux, and related distributions
can install `ansible` or Ansible collections from the community maintained
[EPEL](https://docs.fedoraproject.org/en-US/epel/)
(Extra Packages for Enterprise Linux) repository.

After [enabling the EPEL repository](https://docs.fedoraproject.org/en-US/epel/#_quickstart),
users can use the same `dnf` commands as for Fedora Linux.

Please [file a bug](https://bugzilla.redhat.com/enter_bug.cgi) against the
`Fedora EPEL` product in Red Hat Bugzilla to reach the package maintainers.

## [Installing Ansible on OpenSUSE Tumbleweed/Leap](installation_distros.md#id5)

```bash
$ sudo zypper install ansible
```

See [OpenSUSE Support Portal](https://en.opensuse.org/Portal:Support) for additional help with Ansible on OpenSUSE.

## [Installing Ansible on Ubuntu](installation_distros.md#id6)

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

## [Installing Ansible on Debian](installation_distros.md#id7)

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

## [Installing Ansible on Arch Linux](installation_distros.md#id8)

To install the full `ansible` package run:

```bash
$ sudo pacman -S ansible
```

To install the minimal `ansible-core` package run:

```bash
$ sudo pacman -S ansible-core
```

Several Ansible ecosystem packages are also available from the Arch Linux repositories as
standalone packages that users can install alongside `ansible-core`.
See the [Arch Linux Packages index](https://archlinux.org/packages/?sort=&q=ansible)
for a full list of Ansible packages in Arch Linux.

Please [file a bug](https://bugs.archlinux.org/) to reach the package maintainers.

## [Installing Ansible on Windows](installation_distros.md#id9)

You cannot use a Windows system for the Ansible control node. See [Can Ansible run on Windows?](../os_guide/windows_faq.md#windows-faq-ansible)

> **See also:**
>
> [Installing Ansible on Arch Linux](https://wiki.archlinux.org/title/Ansible#Installation)
> :   Distro-specific installation on Arch Linux
>
> [Installing Ansible on Clear Linux](https://clearlinux.org/software/bundle/ansible)
> :   Distro-specific installation on Clear Linux
