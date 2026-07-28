---
collection: ansible
version: "8"
title: "Other Tools and Programs"
source_url: https://docs.ansible.com/projects/ansible/8/community/other_tools_and_programs.html
fetched_at: 2026-07-28T00:59:00+00:00
---
# Other Tools and Programs

- [Popular editors](other_tools_and_programs.md#popular-editors)

  - [Emacs](other_tools_and_programs.md#emacs)
  - [PyCharm](other_tools_and_programs.md#pycharm)
  - [Sublime](other_tools_and_programs.md#sublime)
  - [vim](other_tools_and_programs.md#vim)
  - [Visual studio code](other_tools_and_programs.md#visual-studio-code)
- [Development tools](other_tools_and_programs.md#development-tools)

  - [Finding related issues and PRs](other_tools_and_programs.md#finding-related-issues-and-prs)
- [Tools for validating playbooks](other_tools_and_programs.md#tools-for-validating-playbooks)
- [Other tools](other_tools_and_programs.md#other-tools)

The Ansible community uses a range of tools for working with the Ansible project. This is a list of some of the most popular of these tools.

If you know of any other tools that should be added, this list can be updated by clicking “Edit on GitHub” on the top right of this page.

## [Popular editors](other_tools_and_programs.md#id3)

### [Emacs](other_tools_and_programs.md#id4)

A free, open-source text editor and IDE that supports auto-indentation, syntax highlighting and built in terminal shell(among other things).

- [yaml-mode](https://github.com/yoshiki/yaml-mode) - YAML highlighting and syntax checking.
- [jinja2-mode](https://github.com/paradoxxxzero/jinja2-mode) - Jinja2 highlighting and syntax checking.
- [magit-mode](https://github.com/magit/magit) - Git porcelain within Emacs.
- [lsp-mode](https://emacs-lsp.github.io/lsp-mode/page/lsp-ansible/) - Ansible syntax highlighting, auto-completion and diagnostics.

### [PyCharm](other_tools_and_programs.md#id5)

A full IDE (integrated development environment) for Python software development. It ships with everything you need to write python scripts and complete software, including support for YAML syntax highlighting. It’s a little overkill for writing roles/playbooks, but it can be a very useful tool if you write modules and submit code for Ansible. Can be used to debug `ansible-core`. For more information, see [PyCharm](https://www.jetbrains.com/pycharm/)

### [Sublime](other_tools_and_programs.md#id6)

A closed-source, subscription GUI text editor. You can customize the GUI with themes and install packages for language highlighting and other refinements. You can install Sublime on Linux, macOS and Windows. Useful Sublime plugins include:

- [GitGutter](https://packagecontrol.io/packages/GitGutter) - shows information about files in a git repository.
- [SideBarEnhancements](https://packagecontrol.io/packages/SideBarEnhancements) - provides enhancements to the operations on Sidebar of Files and Folders.
- [Sublime Linter](https://packagecontrol.io/packages/SublimeLinter) - a code-linting framework for Sublime Text 3.
- [Pretty YAML](https://packagecontrol.io/packages/Pretty%20YAML) - prettifies YAML for Sublime Text 2 and 3.
- [Yamllint](https://packagecontrol.io/packages/SublimeLinter-contrib-yamllint) - a Sublime wrapper around yamllint.

### [vim](other_tools_and_programs.md#id7)

An open-source, free command-line text editor. Useful vim plugins include:

- [Ansible vim](https://github.com/pearofducks/ansible-vim) - vim syntax plugin for Ansible 2.x, it supports YAML playbooks, Jinja2 templates, and Ansible’s hosts files.
- [Ansible vim and neovim plugin](https://www.npmjs.com/package/@yaegassy/coc-ansible) - vim plugin (lsp client) for Ansible, it supports autocompletion, syntax highlighting, hover, diagnostics, and goto support.

### [Visual studio code](other_tools_and_programs.md#id8)

An open-source, free GUI text editor created and maintained by Microsoft. Useful Visual Studio Code plugins include:

- [Ansible extension by Red Hat](https://marketplace.visualstudio.com/items?itemName=redhat.ansible) - provides autocompletion, syntax highlighting, hover, diagnostics, goto support, and command to run ansible-playbook and ansible-navigator tool for both local and execution-environment setups.
- [YAML Support by Red Hat](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml) - provides YAML support through yaml-language-server with built-in Kubernetes and Kedge syntax support.

> **Note:**
>
> the Visual Studio Code Ansible extension is maintained by the Ansible community and Red Hat.

## [Development tools](other_tools_and_programs.md#id9)

### [Finding related issues and PRs](other_tools_and_programs.md#id10)

There are various ways to find existing issues and pull requests (PRs)

- [jctanner’s Ansible Tools](https://github.com/jctanner/ansible-tools) - miscellaneous collection of useful helper scripts for Ansible development.

## [Tools for validating playbooks](other_tools_and_programs.md#id11)

- [Ansible Lint](https://docs.ansible.com/ansible-lint/index.html) - a highly configurable linter for Ansible playbooks.
- [Ansible Review](https://github.com/willthames/ansible-review) - an extension of Ansible Lint designed for code review.
- [Molecule](https://ansible.readthedocs.io/projects/molecule/) - a testing framework for Ansible plays and roles.
- [yamllint](https://yamllint.readthedocs.io/en/stable/) - a command-line utility to check syntax validity including key repetition and indentation issues.

## [Other tools](other_tools_and_programs.md#id12)

- [Ansible Inventory Grapher](https://github.com/willthames/ansible-inventory-grapher) - visually displays inventory inheritance hierarchies and at what level a variable is defined in inventory.
- [Ansible Shell](https://github.com/dominis/ansible-shell) - an interactive shell for Ansible with built-in tab completion for all the modules.
- [Ansible Silo](https://github.com/groupon/ansible-silo) - a self-contained Ansible environment by Docker.
- [Ansigenome](https://github.com/nickjj/ansigenome) - a command line tool designed to help you manage your Ansible roles.
- [antsibull-changelog](https://github.com/ansible-community/antsibull-changelog) - a changelog generator for Ansible collections.
- [antsibull-docs](https://github.com/ansible-community/antsibull-docs) - generates docsites for collections and can validate collection documentation.
- [ARA](https://github.com/ansible-community/ara) - ARA Records Ansible playbooks and makes them easier to understand and troubleshoot with a reporting API, UI and CLI.
- [Awesome Ansible](https://github.com/ansible-community/awesome-ansible) - a collaboratively curated list of awesome Ansible resources.
- [nanvault](https://github.com/marcobellaccini/nanvault) - a standalone tool to encrypt and decrypt files in the Ansible Vault format, featuring UNIX-style composability.
- [OpsTools-ansible](https://github.com/centos-opstools/opstools-ansible) - uses Ansible to configure an environment that provides the support of [OpsTools](https://wiki.centos.org/SpecialInterestGroup/OpsTools), namely centralized logging and analysis, availability monitoring, and performance monitoring.
