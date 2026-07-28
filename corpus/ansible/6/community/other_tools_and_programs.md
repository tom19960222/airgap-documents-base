---
collection: ansible
version: "6"
title: "Other Tools and Programs"
source_url: https://docs.ansible.com/projects/ansible/6/community/other_tools_and_programs.html
fetched_at: 2026-07-27T16:39:49+00:00
---
# Other Tools and Programs

The Ansible community uses a range of tools for working with the Ansible project. This is a list of some of the most popular of these tools.

If you know of any other tools that should be added, this list can be updated by clicking “Edit on GitHub” on the top right of this page.

# Popular editors

## Atom

An open-source, free GUI text editor created and maintained by GitHub. You can keep track of git project
changes, commit from the GUI, and see what branch you are on. You can customize the themes for different colors and install syntax highlighting packages for different languages. You can install Atom on Linux, macOS and Windows. Useful Atom plugins include:

- [language-yaml](https://atom.io/packages/language-yaml) - YAML highlighting for Atom (built-in).
- [linter-js-yaml](https://atom.io/packages/linter-js-yaml) - parses your YAML files in Atom through js-yaml.

## Emacs

A free, open-source text editor and IDE that supports auto-indentation, syntax highlighting and built in terminal shell(among other things).

- [yaml-mode](https://github.com/yoshiki/yaml-mode) - YAML highlighting and syntax checking.
- [jinja2-mode](https://github.com/paradoxxxzero/jinja2-mode) - Jinja2 highlighting and syntax checking.
- [magit-mode](https://github.com/magit/magit) - Git porcelain within Emacs.
- [lsp-mode](https://emacs-lsp.github.io/lsp-mode/page/lsp-ansible/) - Ansible syntax highlighting, auto-completion and diagnostics.

## PyCharm

A full IDE (integrated development environment) for Python software development. It ships with everything you need to write python scripts and complete software, including support for YAML syntax highlighting. It’s a little overkill for writing roles/playbooks, but it can be a very useful tool if you write modules and submit code for Ansible. Can be used to debug the Ansible engine.

## Sublime

A closed-source, subscription GUI text editor. You can customize the GUI with themes and install packages for language highlighting and other refinements. You can install Sublime on Linux, macOS and Windows. Useful Sublime plugins include:

- [GitGutter](https://packagecontrol.io/packages/GitGutter) - shows information about files in a git repository.
- [SideBarEnhancements](https://packagecontrol.io/packages/SideBarEnhancements) - provides enhancements to the operations on Sidebar of Files and Folders.
- [Sublime Linter](https://packagecontrol.io/packages/SublimeLinter) - a code-linting framework for Sublime Text 3.
- [Pretty YAML](https://packagecontrol.io/packages/Pretty%20YAML) - prettifies YAML for Sublime Text 2 and 3.
- [Yamllint](https://packagecontrol.io/packages/SublimeLinter-contrib-yamllint) - a Sublime wrapper around yamllint.

## Visual studio code

An open-source, free GUI text editor created and maintained by Microsoft. Useful Visual Studio Code plugins include:

- [Ansible extension by Red Hat](https://marketplace.visualstudio.com/items?itemName=redhat.ansible) - provides autocompletion, syntax highlighting, hover, diagnostics, goto support, and command to run ansible-playbook and ansible-navigator tool for both local and execution-environment setups.
- [YAML Support by Red Hat](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml) - provides YAML support through yaml-language-server with built-in Kubernetes and Kedge syntax support.

## vim

An open-source, free command-line text editor. Useful vim plugins include:

- [Ansible vim](https://github.com/pearofducks/ansible-vim) - vim syntax plugin for Ansible 2.x, it supports YAML playbooks, Jinja2 templates, and Ansible’s hosts files.
- [Ansible vim and neovim plugin](https://www.npmjs.com/package/@yaegassy/coc-ansible) - vim plugin (lsp client) for Ansible, it supports autocompletion, syntax highlighting, hover, diagnostics, and goto support.

## JetBrains

An open-source Community edition and closed-source Enterprise edition, integrated development environments based on IntelliJ’s framework including IDEA, AppCode, CLion, GoLand, PhpStorm, PyCharm and others. Useful JetBrains platform plugins include:

- [Ansible](https://plugins.jetbrains.com/plugin/14893-ansible) - general Ansible plugin provides auto-completion, role name suggestion and other handy features for working with playbooks and roles.
- [Ansible Vault Editor](https://plugins.jetbrains.com/plugin/14278-ansible-vault-editor) - Ansible Vault Editor with auto encryption/decryption.

# Development tools

## Finding related issues and PRs

There are various ways to find existing issues and pull requests (PRs)

- [PR by File](https://ansible.sivel.net/pr/byfile.html) - shows a current list of all open pull requests by individual file. An essential tool for Ansible module maintainers.
- [jctanner’s Ansible Tools](https://github.com/jctanner/ansible-tools) - miscellaneous collection of useful helper scripts for Ansible development.

# Tools for validating playbooks

- [Ansible Lint](https://docs.ansible.com/ansible-lint/index.html) - a highly configurable linter for Ansible playbooks.
- [Ansible Review](https://github.com/willthames/ansible-review) - an extension of Ansible Lint designed for code review.
- [Molecule](https://molecule.readthedocs.io/en/latest/) - a testing framework for Ansible plays and roles.
- [yamllint](https://yamllint.readthedocs.io/en/stable/) - a command-line utility to check syntax validity including key repetition and indentation issues.

# Other tools

- [Ansible cmdb](https://github.com/fboender/ansible-cmdb) - takes the output of Ansible’s fact gathering and converts it into a static HTML overview page containing system configuration information.
- [Ansible Inventory Grapher](https://github.com/willthames/ansible-inventory-grapher) - visually displays inventory inheritance hierarchies and at what level a variable is defined in inventory.
- [Ansible Language Server](https://www.npmjs.com/package/@ansible/ansible-language-server) - a server that implements [language server protocol](https://microsoft.github.io/language-server-protocol/) for Ansible.
- [Ansible Playbook Grapher](https://github.com/haidaraM/ansible-playbook-grapher) - a command line tool to create a graph representing your Ansible playbook tasks and roles.
- [Ansible Shell](https://github.com/dominis/ansible-shell) - an interactive shell for Ansible with built-in tab completion for all the modules.
- [Ansible Silo](https://github.com/groupon/ansible-silo) - a self-contained Ansible environment by Docker.
- [Ansigenome](https://github.com/nickjj/ansigenome) - a command line tool designed to help you manage your Ansible roles.
- [ARA](https://github.com/ansible-community/ara) - ARA Records Ansible playbooks and makes them easier to understand and troubleshoot with a reporting API, UI and CLI.
- [Awesome Ansible](https://github.com/jdauphant/awesome-ansible) - a collaboratively curated list of awesome Ansible resources.
- [AWX](https://github.com/ansible/awx) - provides a web-based user interface, REST API, and task engine built on top of Ansible. Red Hat Ansible Automation Platform includes code from AWX.
- [Mitogen for Ansible](https://mitogen.networkgenomics.com/ansible_detailed.html) - uses the [Mitogen](https://github.com/dw/mitogen/) library to execute Ansible playbooks in a more efficient way (decreases the execution time).
- [nanvault](https://github.com/marcobellaccini/nanvault) - a standalone tool to encrypt and decrypt files in the Ansible Vault format, featuring UNIX-style composability.
- [OpsTools-ansible](https://github.com/centos-opstools/opstools-ansible) - uses Ansible to configure an environment that provides the support of [OpsTools](https://wiki.centos.org/SpecialInterestGroup/OpsTools), namely centralized logging and analysis, availability monitoring, and performance monitoring.
- [TD4A](https://github.com/cidrblock/td4a) - a template designer for automation. TD4A is a visual design aid for building and testing jinja2 templates. It will combine data in yaml format with a jinja2 template and render the output.
- [PHP-Ansible](https://github.com/maschmann/php-ansible) - an object oriented Ansible wrapper for PHP.
