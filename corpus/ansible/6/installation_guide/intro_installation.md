---
collection: ansible
version: "6"
title: "Installing Ansible"
source_url: https://docs.ansible.com/projects/ansible/6/installation_guide/intro_installation.html
fetched_at: 2026-07-27T16:39:38+00:00
---
# Installing Ansible

Ansible is an agentless automation tool that you install on a single host (referred to as the control node). From the control node, Ansible can manage an entire fleet of machines and other devices (referred to as managed nodes) remotely with SSH, Powershell remoting, and numerous other transports, all from a simple command-line interface with no databases or daemons required.

- [Control node requirements](intro_installation.md#control-node-requirements)
- [Selecting an Ansible package and version to install](intro_installation.md#selecting-an-ansible-package-and-version-to-install)
- [Installing and upgrading Ansible](intro_installation.md#installing-and-upgrading-ansible)

  - [Locating Python](intro_installation.md#locating-python)
  - [Ensuring `pip` is available](intro_installation.md#ensuring-pip-is-available)
  - [Installing Ansible](intro_installation.md#pip-install)
  - [Upgrading Ansible](intro_installation.md#upgrading-ansible)
  - [Confirming your installation](intro_installation.md#confirming-your-installation)
- [Installing for development](intro_installation.md#installing-for-development)

  - [Installing `devel` from GitHub with `pip`](intro_installation.md#installing-devel-from-github-with-pip)
  - [Running the `devel` branch from a clone](intro_installation.md#running-the-devel-branch-from-a-clone)
- [Adding Ansible command shell completion](intro_installation.md#adding-ansible-command-shell-completion)

  - [Installing `argcomplete`](intro_installation.md#installing-argcomplete)
  - [Configuring `argcomplete`](intro_installation.md#configuring-argcomplete)

    - [Global configuration](intro_installation.md#global-configuration)
    - [Per command configuration](intro_installation.md#per-command-configuration)
    - [Using `argcomplete` with zsh or tcsh](intro_installation.md#using-argcomplete-with-zsh-or-tcsh)

## [Control node requirements](intro_installation.md#id4)

For your control node (the machine that runs Ansible), you can use nearly any UNIX-like machine with Python 3.8 or newer installed. This includes Red Hat, Debian, Ubuntu, macOS, BSDs, and Windows under a [Windows Subsystem for Linux (WSL) distribution](https://docs.microsoft.com/en-us/windows/wsl/about). Windows without WSL is not natively supported as a control node; see [Matt Davis’ blog post](http://blog.rolpdog.com/2020/03/why-no-ansible-controller-for-windows.html) for more information.

## [Selecting an Ansible package and version to install](intro_installation.md#id5)

Ansible’s community packages are distributed in two ways: a minimalist language and runtime package called `ansible-core`, and a much larger “batteries included” package called `ansible`, which adds a community-curated selection of [Ansible Collections](../user_guide/collections_using.md#collections) for automating a wide variety of devices. Choose the package that fits your needs; The following instructions use `ansible`, but you can substitute `ansible-core` if you prefer to start with a more minimal package and separately install only the Ansible Collections you require. The `ansible` or `ansible-core` packages may be available in your operating systems package manager, and you are free to install these packages with your preferred method. These installation instructions only cover the officially supported means of installing the python package with `pip`.

## [Installing and upgrading Ansible](intro_installation.md#id6)

### [Locating Python](intro_installation.md#id7)

Locate and remember the path to the Python interpreter you wish to use to run Ansible. The following instructions refer to this Python as `python3`. For example, if you’ve determined that you want the Python at `/usr/bin/python3.9` to be the one that you’ll install Ansible under, specify that instead of `python3`.

### [Ensuring `pip` is available](intro_installation.md#id8)

To verify whether `pip` is already installed for your preferred Python:

```console
$ python3 -m pip -V
```

If all is well, you should see something like the following:

```console
$ python3 -m pip -V
pip 21.0.1 from /usr/lib/python3.9/site-packages/pip (python 3.9)
```

If so, `pip` is available, and you can move on to the [next step](intro_installation.md#pip-install).

If you see an error like `No module named pip`, you’ll need to install `pip` under your chosen Python interpreter before proceeding. This may mean installing an additional OS package (for example, `python3-pip`), or installing the latest `pip` directly from the Python Packaging Authority by running the following:

```console
$ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
$ python3 get-pip.py --user
```

You may need to perform some additional configuration before you are able to run Ansible. See the Python documentation on [installing to the user site](https://packaging.python.org/tutorials/installing-packages/#installing-to-the-user-site) for more information.

### [Installing Ansible](intro_installation.md#id9)

Use `pip` in your selected Python environment to install the Ansible package of your choice for the current user:

```console
$ python3 -m pip install --user ansible
```

Alternately, you can install a specific version of `ansible-core` in this Python environment:

```console
$ python3 -m pip install --user ansible-core==2.12.3
```

### [Upgrading Ansible](intro_installation.md#id10)

To upgrade an existing Ansible installation in this Python environment to the latest released version, simply add `--upgrade` to the command above:

```console
$ python3 -m pip install --upgrade --user ansible
```

### [Confirming your installation](intro_installation.md#id11)

You can test that Ansible is installed correctly by checking the version:

```console
$ ansible --version
```

The version displayed by this command is for the associated `ansible-core` package that has been installed.

To check the version of the `ansible` package that has been installed:

```console
$ python3 -m pip show ansible
```

## [Installing for development](intro_installation.md#id12)

If you are testing new features, fixing bugs, or otherwise working with the development team on changes to the core code, you can install and run the source from GitHub.

> **Note:**
>
> You should only install and run the `devel` branch if you are modifying `ansible-core` or trying out features under development. This is a rapidly changing source of code and can become unstable at any point.

For more information on getting involved in the Ansible project, see the [Ansible Community Guide](../community/index.md#ansible-community-guide). For more information on creating Ansible modules and Collections, see the [Developer Guide](../dev_guide/index.md#developer-guide).

### [Installing `devel` from GitHub with `pip`](intro_installation.md#id13)

You can install the `devel` branch of `ansible-core` directly from GitHub with `pip`:

```console
$ python3 -m pip install --user https://github.com/ansible/ansible/archive/devel.tar.gz
```

You can replace `devel` in the URL mentioned above, with any other branch or tag on GitHub to install older versions of Ansible, tagged alpha or beta versions, and release candidates.

### [Running the `devel` branch from a clone](intro_installation.md#id14)

`ansible-core` is easy to run from source. You do not need `root` permissions to use it and there is no software to actually install. No daemons or database setup are required.

1. Clone the `ansible-core` repository

   ```console
   $ git clone https://github.com/ansible/ansible.git
   $ cd ./ansible
   ```
2. Setup the Ansible environment

   - Using Bash

     ```console
     $ source ./hacking/env-setup
     ```
   - Using Fish

     ```console
     $ source ./hacking/env-setup.fish
     ```
   - To suppress spurious warnings/errors, use `-q`

     ```console
     $ source ./hacking/env-setup -q
     ```
3. Install Python dependencies

   ```console
   $ python3 -m pip install --user -r ./requirements.txt
   ```
4. Update the `devel` branch of `ansible-core` on your local machine

   Use pull-with-rebase so any local changes are replayed.

   ```console
   $ git pull --rebase
   ```

## [Adding Ansible command shell completion](intro_installation.md#id15)

You can add shell completion of the Ansible command line utilities by installing an optional dependency called `argcomplete`. `argcomplete` supports bash, and has limited support for zsh and tcsh.

For more information about installation and configuration, see the [argcomplete documentation](https://kislyuk.github.io/argcomplete/).

### [Installing `argcomplete`](intro_installation.md#id16)

```console
$ python3 -m pip install --user argcomplete
```

### [Configuring `argcomplete`](intro_installation.md#id17)

There are 2 ways to configure `argcomplete` to allow shell completion of the Ansible command line utilities: globally or per command.

#### [Global configuration](intro_installation.md#id18)

Global completion requires bash 4.2.

```console
$ activate-global-python-argcomplete
```

This will write a bash completion file to a global location. Use `--dest` to change the location.

#### [Per command configuration](intro_installation.md#id19)

If you do not have bash 4.2, you must register each script independently.

```console
$ eval $(register-python-argcomplete ansible)
$ eval $(register-python-argcomplete ansible-config)
$ eval $(register-python-argcomplete ansible-console)
$ eval $(register-python-argcomplete ansible-doc)
$ eval $(register-python-argcomplete ansible-galaxy)
$ eval $(register-python-argcomplete ansible-inventory)
$ eval $(register-python-argcomplete ansible-playbook)
$ eval $(register-python-argcomplete ansible-pull)
$ eval $(register-python-argcomplete ansible-vault)
```

You should place the above commands into your shells profile file such as `~/.profile` or `~/.bash_profile`.

#### [Using `argcomplete` with zsh or tcsh](intro_installation.md#id20)

See the [argcomplete documentation](https://kislyuk.github.io/argcomplete/).

> **See also:**
>
> [Introduction to ad hoc commands](../user_guide/intro_adhoc.md#intro-adhoc)
> :   Examples of basic commands
>
> [Working with playbooks](../user_guide/playbooks.md#working-with-playbooks)
> :   Learning ansible’s configuration management language
>
> [How do I handle the package dependencies required by Ansible package dependencies during Ansible installation ?](../reference_appendices/faq.md#installation-faqs)
> :   Ansible Installation related to FAQs
>
> [Mailing List](https://groups.google.com/group/ansible-project)
> :   Questions? Help? Ideas? Stop by the list on Google Groups
>
> [Real-time chat](../community/communication.md#communication-irc)
> :   How to join Ansible chat channels
