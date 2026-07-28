---
collection: ansible
version: "6"
title: "Ansible.Builtin"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/builtin/
fetched_at: 2026-07-27T16:43:14+00:00
---
# Ansible.Builtin

Collection version 2.13.10.post0

- [Description](index.md#description)
- [Communication](index.md#communication)
- [Plugin Index](index.md#plugin-index)

## [Description](index.md#id1)

These are all modules and plugins contained in ansible-core.

**Author:**

- Ansible, Inc.

[Issue Tracker](https://github.com/ansible/ansible/issues)
[Repository (Sources)](https://github.com/ansible/ansible)

## [Communication](index.md#id2)

- Matrix room `#users:ansible.im`: [General usage and support questions](https://matrix.to/#/#users:ansible.im).
- IRC channel `#ansible` (Libera network):
  [General usage and support questions](https://web.libera.chat/?channel=#ansible).
- Mailing list: [Ansible Project List](https://groups.google.com/g/ansible-project).
  ([Subscribe](mailto:ansible-project+subscribe%40googlegroups.com?subject=subscribe))

## [Plugin Index](index.md#id3)

These are the plugins in the ansible.builtin collection:

### Modules

- [add_host module](add_host_module.md#ansible-collections-ansible-builtin-add-host-module) – Add a host (and alternatively a group) to the ansible-playbook in-memory inventory
- [apt module](apt_module.md#ansible-collections-ansible-builtin-apt-module) – Manages apt-packages
- [apt_key module](apt_key_module.md#ansible-collections-ansible-builtin-apt-key-module) – Add or remove an apt key
- [apt_repository module](apt_repository_module.md#ansible-collections-ansible-builtin-apt-repository-module) – Add and remove APT repositories
- [assemble module](assemble_module.md#ansible-collections-ansible-builtin-assemble-module) – Assemble configuration files from fragments
- [assert module](assert_module.md#ansible-collections-ansible-builtin-assert-module) – Asserts given expressions are true
- [async_status module](async_status_module.md#ansible-collections-ansible-builtin-async-status-module) – Obtain status of asynchronous task
- [blockinfile module](blockinfile_module.md#ansible-collections-ansible-builtin-blockinfile-module) – Insert/update/remove a text block surrounded by marker lines
- [command module](command_module.md#ansible-collections-ansible-builtin-command-module) – Execute commands on targets
- [copy module](copy_module.md#ansible-collections-ansible-builtin-copy-module) – Copy files to remote locations
- [cron module](cron_module.md#ansible-collections-ansible-builtin-cron-module) – Manage cron.d and crontab entries
- [debconf module](debconf_module.md#ansible-collections-ansible-builtin-debconf-module) – Configure a .deb package
- [debug module](debug_module.md#ansible-collections-ansible-builtin-debug-module) – Print statements during execution
- [dnf module](dnf_module.md#ansible-collections-ansible-builtin-dnf-module) – Manages packages with the *dnf* package manager
- [dpkg_selections module](dpkg_selections_module.md#ansible-collections-ansible-builtin-dpkg-selections-module) – Dpkg package selection selections
- [expect module](expect_module.md#ansible-collections-ansible-builtin-expect-module) – Executes a command and responds to prompts
- [fail module](fail_module.md#ansible-collections-ansible-builtin-fail-module) – Fail with custom message
- [fetch module](fetch_module.md#ansible-collections-ansible-builtin-fetch-module) – Fetch files from remote nodes
- [file module](file_module.md#ansible-collections-ansible-builtin-file-module) – Manage files and file properties
- [find module](find_module.md#ansible-collections-ansible-builtin-find-module) – Return a list of files based on specific criteria
- [gather_facts module](gather_facts_module.md#ansible-collections-ansible-builtin-gather-facts-module) – Gathers facts about remote hosts
- [get_url module](get_url_module.md#ansible-collections-ansible-builtin-get-url-module) – Downloads files from HTTP, HTTPS, or FTP to node
- [getent module](getent_module.md#ansible-collections-ansible-builtin-getent-module) – A wrapper to the unix getent utility
- [git module](git_module.md#ansible-collections-ansible-builtin-git-module) – Deploy software (or files) from git checkouts
- [group module](group_module.md#ansible-collections-ansible-builtin-group-module) – Add or remove groups
- [group_by module](group_by_module.md#ansible-collections-ansible-builtin-group-by-module) – Create Ansible groups based on facts
- [hostname module](hostname_module.md#ansible-collections-ansible-builtin-hostname-module) – Manage hostname
- [import_playbook module](import_playbook_module.md#ansible-collections-ansible-builtin-import-playbook-module) – Import a playbook
- [import_role module](import_role_module.md#ansible-collections-ansible-builtin-import-role-module) – Import a role into a play
- [import_tasks module](import_tasks_module.md#ansible-collections-ansible-builtin-import-tasks-module) – Import a task list
- [include module](include_module.md#ansible-collections-ansible-builtin-include-module) – Include a task list
- [include_role module](include_role_module.md#ansible-collections-ansible-builtin-include-role-module) – Load and execute a role
- [include_tasks module](include_tasks_module.md#ansible-collections-ansible-builtin-include-tasks-module) – Dynamically include a task list
- [include_vars module](include_vars_module.md#ansible-collections-ansible-builtin-include-vars-module) – Load variables from files, dynamically within a task
- [iptables module](iptables_module.md#ansible-collections-ansible-builtin-iptables-module) – Modify iptables rules
- [known_hosts module](known_hosts_module.md#ansible-collections-ansible-builtin-known-hosts-module) – Add or remove a host from the `known_hosts` file
- [lineinfile module](lineinfile_module.md#ansible-collections-ansible-builtin-lineinfile-module) – Manage lines in text files
- [meta module](meta_module.md#ansible-collections-ansible-builtin-meta-module) – Execute Ansible ‘actions’
- [package module](package_module.md#ansible-collections-ansible-builtin-package-module) – Generic OS package manager
- [package_facts module](package_facts_module.md#ansible-collections-ansible-builtin-package-facts-module) – Package information as facts
- [pause module](pause_module.md#ansible-collections-ansible-builtin-pause-module) – Pause playbook execution
- [ping module](ping_module.md#ansible-collections-ansible-builtin-ping-module) – Try to connect to host, verify a usable python and return `pong` on success
- [pip module](pip_module.md#ansible-collections-ansible-builtin-pip-module) – Manages Python library dependencies
- [raw module](raw_module.md#ansible-collections-ansible-builtin-raw-module) – Executes a low-down and dirty command
- [reboot module](reboot_module.md#ansible-collections-ansible-builtin-reboot-module) – Reboot a machine
- [replace module](replace_module.md#ansible-collections-ansible-builtin-replace-module) – Replace all instances of a particular string in a file using a back-referenced regular expression
- [rpm_key module](rpm_key_module.md#ansible-collections-ansible-builtin-rpm-key-module) – Adds or removes a gpg key from the rpm db
- [script module](script_module.md#ansible-collections-ansible-builtin-script-module) – Runs a local script on a remote node after transferring it
- [service module](service_module.md#ansible-collections-ansible-builtin-service-module) – Manage services
- [service_facts module](service_facts_module.md#ansible-collections-ansible-builtin-service-facts-module) – Return service state information as fact data
- [set_fact module](set_fact_module.md#ansible-collections-ansible-builtin-set-fact-module) – Set host variable(s) and fact(s).
- [set_stats module](set_stats_module.md#ansible-collections-ansible-builtin-set-stats-module) – Define and display stats for the current ansible run
- [setup module](setup_module.md#ansible-collections-ansible-builtin-setup-module) – Gathers facts about remote hosts
- [shell module](shell_module.md#ansible-collections-ansible-builtin-shell-module) – Execute shell commands on targets
- [slurp module](slurp_module.md#ansible-collections-ansible-builtin-slurp-module) – Slurps a file from remote nodes
- [stat module](stat_module.md#ansible-collections-ansible-builtin-stat-module) – Retrieve file or file system status
- [subversion module](subversion_module.md#ansible-collections-ansible-builtin-subversion-module) – Deploys a subversion repository
- [systemd module](systemd_module.md#ansible-collections-ansible-builtin-systemd-module) – Manage systemd units
- [sysvinit module](sysvinit_module.md#ansible-collections-ansible-builtin-sysvinit-module) – Manage SysV services.
- [tempfile module](tempfile_module.md#ansible-collections-ansible-builtin-tempfile-module) – Creates temporary files and directories
- [template module](template_module.md#ansible-collections-ansible-builtin-template-module) – Template a file out to a target host
- [unarchive module](unarchive_module.md#ansible-collections-ansible-builtin-unarchive-module) – Unpacks an archive after (optionally) copying it from the local machine
- [uri module](uri_module.md#ansible-collections-ansible-builtin-uri-module) – Interacts with webservices
- [user module](user_module.md#ansible-collections-ansible-builtin-user-module) – Manage user accounts
- [validate_argument_spec module](validate_argument_spec_module.md#ansible-collections-ansible-builtin-validate-argument-spec-module) – Validate role argument specs.
- [wait_for module](wait_for_module.md#ansible-collections-ansible-builtin-wait-for-module) – Waits for a condition before continuing
- [wait_for_connection module](wait_for_connection_module.md#ansible-collections-ansible-builtin-wait-for-connection-module) – Waits until remote system is reachable/usable
- [yum module](yum_module.md#ansible-collections-ansible-builtin-yum-module) – Manages packages with the *yum* package manager
- [yum_repository module](yum_repository_module.md#ansible-collections-ansible-builtin-yum-repository-module) – Add or remove YUM repositories

### Become Plugins

- [runas become](runas_become.md#ansible-collections-ansible-builtin-runas-become) – Run As user
- [su become](su_become.md#ansible-collections-ansible-builtin-su-become) – Substitute User
- [sudo become](sudo_become.md#ansible-collections-ansible-builtin-sudo-become) – Substitute User DO

### Cache Plugins

- [jsonfile cache](jsonfile_cache.md#ansible-collections-ansible-builtin-jsonfile-cache) – JSON formatted files.
- [memory cache](memory_cache.md#ansible-collections-ansible-builtin-memory-cache) – RAM backed, non persistent

### Callback Plugins

- [default callback](default_callback.md#ansible-collections-ansible-builtin-default-callback) – default Ansible screen output
- [junit callback](junit_callback.md#ansible-collections-ansible-builtin-junit-callback) – write playbook output to a JUnit file.
- [minimal callback](minimal_callback.md#ansible-collections-ansible-builtin-minimal-callback) – minimal Ansible screen output
- [oneline callback](oneline_callback.md#ansible-collections-ansible-builtin-oneline-callback) – oneline Ansible screen output
- [tree callback](tree_callback.md#ansible-collections-ansible-builtin-tree-callback) – Save host events to files

### Connection Plugins

- [local connection](local_connection.md#ansible-collections-ansible-builtin-local-connection) – execute on controller
- [paramiko_ssh connection](paramiko_ssh_connection.md#ansible-collections-ansible-builtin-paramiko-ssh-connection) – Run tasks via python ssh (paramiko)
- [psrp connection](psrp_connection.md#ansible-collections-ansible-builtin-psrp-connection) – Run tasks over Microsoft PowerShell Remoting Protocol
- [ssh connection](ssh_connection.md#ansible-collections-ansible-builtin-ssh-connection) – connect via SSH client binary
- [winrm connection](winrm_connection.md#ansible-collections-ansible-builtin-winrm-connection) – Run tasks over Microsoft’s WinRM

### Inventory Plugins

- [advanced_host_list inventory](advanced_host_list_inventory.md#ansible-collections-ansible-builtin-advanced-host-list-inventory) – Parses a ‘host list’ with ranges
- [auto inventory](auto_inventory.md#ansible-collections-ansible-builtin-auto-inventory) – Loads and executes an inventory plugin specified in a YAML config
- [constructed inventory](constructed_inventory.md#ansible-collections-ansible-builtin-constructed-inventory) – Uses Jinja2 to construct vars and groups based on existing inventory.
- [generator inventory](generator_inventory.md#ansible-collections-ansible-builtin-generator-inventory) – Uses Jinja2 to construct hosts and groups from patterns
- [host_list inventory](host_list_inventory.md#ansible-collections-ansible-builtin-host-list-inventory) – Parses a ‘host list’ string
- [ini inventory](ini_inventory.md#ansible-collections-ansible-builtin-ini-inventory) – Uses an Ansible INI file as inventory source.
- [script inventory](script_inventory.md#ansible-collections-ansible-builtin-script-inventory) – Executes an inventory script that returns JSON
- [toml inventory](toml_inventory.md#ansible-collections-ansible-builtin-toml-inventory) – Uses a specific TOML file as an inventory source.
- [yaml inventory](yaml_inventory.md#ansible-collections-ansible-builtin-yaml-inventory) – Uses a specific YAML file as an inventory source.

### Lookup Plugins

- [config lookup](config_lookup.md#ansible-collections-ansible-builtin-config-lookup) – Lookup current Ansible configuration values
- [csvfile lookup](csvfile_lookup.md#ansible-collections-ansible-builtin-csvfile-lookup) – read data from a TSV or CSV file
- [dict lookup](dict_lookup.md#ansible-collections-ansible-builtin-dict-lookup) – returns key/value pair items from dictionaries
- [env lookup](env_lookup.md#ansible-collections-ansible-builtin-env-lookup) – Read the value of environment variables
- [file lookup](file_lookup.md#ansible-collections-ansible-builtin-file-lookup) – read file contents
- [fileglob lookup](fileglob_lookup.md#ansible-collections-ansible-builtin-fileglob-lookup) – list files matching a pattern
- [first_found lookup](first_found_lookup.md#ansible-collections-ansible-builtin-first-found-lookup) – return first file found from list
- [indexed_items lookup](indexed_items_lookup.md#ansible-collections-ansible-builtin-indexed-items-lookup) – rewrites lists to return ‘indexed items’
- [ini lookup](ini_lookup.md#ansible-collections-ansible-builtin-ini-lookup) – read data from an ini file
- [inventory_hostnames lookup](inventory_hostnames_lookup.md#ansible-collections-ansible-builtin-inventory-hostnames-lookup) – list of inventory hosts matching a host pattern
- [items lookup](items_lookup.md#ansible-collections-ansible-builtin-items-lookup) – list of items
- [lines lookup](lines_lookup.md#ansible-collections-ansible-builtin-lines-lookup) – read lines from command
- [list lookup](list_lookup.md#ansible-collections-ansible-builtin-list-lookup) – simply returns what it is given.
- [nested lookup](nested_lookup.md#ansible-collections-ansible-builtin-nested-lookup) – composes a list with nested elements of other lists
- [password lookup](password_lookup.md#ansible-collections-ansible-builtin-password-lookup) – retrieve or generate a random password, stored in a file
- [pipe lookup](pipe_lookup.md#ansible-collections-ansible-builtin-pipe-lookup) – read output from a command
- [random_choice lookup](random_choice_lookup.md#ansible-collections-ansible-builtin-random-choice-lookup) – return random element from list
- [sequence lookup](sequence_lookup.md#ansible-collections-ansible-builtin-sequence-lookup) – generate a list based on a number sequence
- [subelements lookup](subelements_lookup.md#ansible-collections-ansible-builtin-subelements-lookup) – traverse nested key from a list of dictionaries
- [template lookup](template_lookup.md#ansible-collections-ansible-builtin-template-lookup) – retrieve contents of file after templating with Jinja2
- [together lookup](together_lookup.md#ansible-collections-ansible-builtin-together-lookup) – merges lists into synchronized list
- [unvault lookup](unvault_lookup.md#ansible-collections-ansible-builtin-unvault-lookup) – read vaulted file(s) contents
- [url lookup](url_lookup.md#ansible-collections-ansible-builtin-url-lookup) – return contents from URL
- [varnames lookup](varnames_lookup.md#ansible-collections-ansible-builtin-varnames-lookup) – Lookup matching variable names
- [vars lookup](vars_lookup.md#ansible-collections-ansible-builtin-vars-lookup) – Lookup templated value of variables

### Shell Plugins

- [cmd shell](cmd_shell.md#ansible-collections-ansible-builtin-cmd-shell) – Windows Command Prompt
- [powershell shell](powershell_shell.md#ansible-collections-ansible-builtin-powershell-shell) – Windows PowerShell
- [sh shell](sh_shell.md#ansible-collections-ansible-builtin-sh-shell) – POSIX shell (/bin/sh)

### Strategy Plugins

- [debug strategy](debug_strategy.md#ansible-collections-ansible-builtin-debug-strategy) – Executes tasks in interactive debug session.
- [free strategy](free_strategy.md#ansible-collections-ansible-builtin-free-strategy) – Executes tasks without waiting for all hosts
- [host_pinned strategy](host_pinned_strategy.md#ansible-collections-ansible-builtin-host-pinned-strategy) – Executes tasks on each host without interruption
- [linear strategy](linear_strategy.md#ansible-collections-ansible-builtin-linear-strategy) – Executes tasks in a linear fashion

### Vars Plugins

- [host_group_vars vars](host_group_vars_vars.md#ansible-collections-ansible-builtin-host-group-vars-vars) – In charge of loading group_vars and host_vars

> **See also:**
>
> List of [collections](../../index.md#list-of-collections) with docs hosted here.
