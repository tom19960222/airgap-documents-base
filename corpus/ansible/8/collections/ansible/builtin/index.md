---
collection: ansible
version: "8"
title: "Ansible.Builtin"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/index.html
fetched_at: 2026-07-28T01:01:48+00:00
---
# Ansible.Builtin

Collection version 2.15.8.post0

- [Description](index.md#description)
- [Communication](index.md#communication)
- [Plugin Index](index.md#plugin-index)

## [Description](index.md#id1)

These are all modules and plugins contained in ansible-core.

**Author:**

- Ansible, Inc.

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)

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
- [deb822_repository module](deb822_repository_module.md#ansible-collections-ansible-builtin-deb822-repository-module) – Add and remove deb822 formatted repositories
- [debconf module](debconf_module.md#ansible-collections-ansible-builtin-debconf-module) – Configure a .deb package
- [debug module](debug_module.md#ansible-collections-ansible-builtin-debug-module) – Print statements during execution
- [dnf module](dnf_module.md#ansible-collections-ansible-builtin-dnf-module) – Manages packages with the *dnf* package manager
- [dnf5 module](dnf5_module.md#ansible-collections-ansible-builtin-dnf5-module) – Manages packages with the *dnf5* package manager
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
- [systemd_service module](systemd_service_module.md#ansible-collections-ansible-builtin-systemd-service-module) – Manage systemd units
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

### Filter Plugins

- [b64decode filter](b64decode_filter.md#ansible-collections-ansible-builtin-b64decode-filter) – Decode a base64 string
- [b64encode filter](b64encode_filter.md#ansible-collections-ansible-builtin-b64encode-filter) – Encode a string as base64
- [basename filter](basename_filter.md#ansible-collections-ansible-builtin-basename-filter) – get a path’s base name
- [bool filter](bool_filter.md#ansible-collections-ansible-builtin-bool-filter) – cast into a boolean
- [checksum filter](checksum_filter.md#ansible-collections-ansible-builtin-checksum-filter) – checksum of input data
- [combinations filter](combinations_filter.md#ansible-collections-ansible-builtin-combinations-filter) – combinations from the elements of a list
- [combine filter](combine_filter.md#ansible-collections-ansible-builtin-combine-filter) – combine two dictionaries
- [comment filter](comment_filter.md#ansible-collections-ansible-builtin-comment-filter) – comment out a string
- [commonpath filter](commonpath_filter.md#ansible-collections-ansible-builtin-commonpath-filter) – gets the common path
- [dict2items filter](dict2items_filter.md#ansible-collections-ansible-builtin-dict2items-filter) – Convert a dictionary into an itemized list of dictionaries
- [difference filter](difference_filter.md#ansible-collections-ansible-builtin-difference-filter) – the difference of one list from another
- [dirname filter](dirname_filter.md#ansible-collections-ansible-builtin-dirname-filter) – get a path’s directory name
- [expanduser filter](expanduser_filter.md#ansible-collections-ansible-builtin-expanduser-filter) – Returns a path with `~` translation.
- [expandvars filter](expandvars_filter.md#ansible-collections-ansible-builtin-expandvars-filter) – expand environment variables
- [extract filter](extract_filter.md#ansible-collections-ansible-builtin-extract-filter) – extract a value based on an index or key
- [fileglob filter](fileglob_filter.md#ansible-collections-ansible-builtin-fileglob-filter) – explode a path glob to matching files
- [flatten filter](flatten_filter.md#ansible-collections-ansible-builtin-flatten-filter) – flatten lists within a list
- [from_json filter](from_json_filter.md#ansible-collections-ansible-builtin-from-json-filter) – Convert JSON string into variable structure
- [from_yaml filter](from_yaml_filter.md#ansible-collections-ansible-builtin-from-yaml-filter) – Convert YAML string into variable structure
- [from_yaml_all filter](from_yaml_all_filter.md#ansible-collections-ansible-builtin-from-yaml-all-filter) – Convert a series of YAML documents into a variable structure
- [hash filter](hash_filter.md#ansible-collections-ansible-builtin-hash-filter) – hash of input data
- [human_readable filter](human_readable_filter.md#ansible-collections-ansible-builtin-human-readable-filter) – Make bytes/bits human readable
- [human_to_bytes filter](human_to_bytes_filter.md#ansible-collections-ansible-builtin-human-to-bytes-filter) – Get bytes from string
- [intersect filter](intersect_filter.md#ansible-collections-ansible-builtin-intersect-filter) – intersection of lists
- [items2dict filter](items2dict_filter.md#ansible-collections-ansible-builtin-items2dict-filter) – Consolidate a list of itemized dictionaries into a dictionary
- [log filter](log_filter.md#ansible-collections-ansible-builtin-log-filter) – log of (math operation)
- [mandatory filter](mandatory_filter.md#ansible-collections-ansible-builtin-mandatory-filter) – make a variable’s existance mandatory
- [md5 filter](md5_filter.md#ansible-collections-ansible-builtin-md5-filter) – MD5 hash of input data
- [normpath filter](normpath_filter.md#ansible-collections-ansible-builtin-normpath-filter) – Normalize a pathname
- [password_hash filter](password_hash_filter.md#ansible-collections-ansible-builtin-password-hash-filter) – convert input password into password_hash
- [path_join filter](path_join_filter.md#ansible-collections-ansible-builtin-path-join-filter) – Join one or more path components
- [permutations filter](permutations_filter.md#ansible-collections-ansible-builtin-permutations-filter) – permutations from the elements of a list
- [pow filter](pow_filter.md#ansible-collections-ansible-builtin-pow-filter) – power of (math operation)
- [product filter](product_filter.md#ansible-collections-ansible-builtin-product-filter) – cartesian product of lists
- [quote filter](quote_filter.md#ansible-collections-ansible-builtin-quote-filter) – shell quoting
- [random filter](random_filter.md#ansible-collections-ansible-builtin-random-filter) – random number or list item
- [realpath filter](realpath_filter.md#ansible-collections-ansible-builtin-realpath-filter) – Turn path into real path
- [regex_escape filter](regex_escape_filter.md#ansible-collections-ansible-builtin-regex-escape-filter) – escape regex chars
- [regex_findall filter](regex_findall_filter.md#ansible-collections-ansible-builtin-regex-findall-filter) – extract all regex matches from string
- [regex_replace filter](regex_replace_filter.md#ansible-collections-ansible-builtin-regex-replace-filter) – replace a string via regex
- [regex_search filter](regex_search_filter.md#ansible-collections-ansible-builtin-regex-search-filter) – extract regex match from string
- [rekey_on_member filter](rekey_on_member_filter.md#ansible-collections-ansible-builtin-rekey-on-member-filter) – Rekey a list of dicts into a dict using a member
- [relpath filter](relpath_filter.md#ansible-collections-ansible-builtin-relpath-filter) – Make a path relative
- [root filter](root_filter.md#ansible-collections-ansible-builtin-root-filter) – root of (math operation)
- [sha1 filter](sha1_filter.md#ansible-collections-ansible-builtin-sha1-filter) – SHA-1 hash of input data
- [shuffle filter](shuffle_filter.md#ansible-collections-ansible-builtin-shuffle-filter) – randomize a list
- [split filter](split_filter.md#ansible-collections-ansible-builtin-split-filter) – split a string into a list
- [splitext filter](splitext_filter.md#ansible-collections-ansible-builtin-splitext-filter) – split a path into root and file extension
- [strftime filter](strftime_filter.md#ansible-collections-ansible-builtin-strftime-filter) – date formating
- [subelements filter](subelements_filter.md#ansible-collections-ansible-builtin-subelements-filter) – returns a product of a list and its elements
- [symmetric_difference filter](symmetric_difference_filter.md#ansible-collections-ansible-builtin-symmetric-difference-filter) – different items from two lists
- [ternary filter](ternary_filter.md#ansible-collections-ansible-builtin-ternary-filter) – Ternary operation filter
- [to_datetime filter](to_datetime_filter.md#ansible-collections-ansible-builtin-to-datetime-filter) – Get `datetime` from string
- [to_json filter](to_json_filter.md#ansible-collections-ansible-builtin-to-json-filter) – Convert variable to JSON string
- [to_nice_json filter](to_nice_json_filter.md#ansible-collections-ansible-builtin-to-nice-json-filter) – Convert variable to ‘nicely formatted’ JSON string
- [to_nice_yaml filter](to_nice_yaml_filter.md#ansible-collections-ansible-builtin-to-nice-yaml-filter) – Convert variable to YAML string
- [to_uuid filter](to_uuid_filter.md#ansible-collections-ansible-builtin-to-uuid-filter) – namespaced UUID generator
- [to_yaml filter](to_yaml_filter.md#ansible-collections-ansible-builtin-to-yaml-filter) – Convert variable to YAML string
- [type_debug filter](type_debug_filter.md#ansible-collections-ansible-builtin-type-debug-filter) – show input data type
- [union filter](union_filter.md#ansible-collections-ansible-builtin-union-filter) – union of lists
- [unique filter](unique_filter.md#ansible-collections-ansible-builtin-unique-filter) – set of unique items of a list
- [unvault filter](unvault_filter.md#ansible-collections-ansible-builtin-unvault-filter) – Open an Ansible Vault
- [urlsplit filter](urlsplit_filter.md#ansible-collections-ansible-builtin-urlsplit-filter) – get components from URL
- [vault filter](vault_filter.md#ansible-collections-ansible-builtin-vault-filter) – vault your secrets
- [win_basename filter](win_basename_filter.md#ansible-collections-ansible-builtin-win-basename-filter) – Get a Windows path’s base name
- [win_dirname filter](win_dirname_filter.md#ansible-collections-ansible-builtin-win-dirname-filter) – Get a Windows path’s directory
- [win_splitdrive filter](win_splitdrive_filter.md#ansible-collections-ansible-builtin-win-splitdrive-filter) – Split a Windows path by the drive letter
- [zip filter](zip_filter.md#ansible-collections-ansible-builtin-zip-filter) – combine list elements
- [zip_longest filter](zip_longest_filter.md#ansible-collections-ansible-builtin-zip-longest-filter) – combine list elements, with filler

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

### Test Plugins

- [abs test](abs_test.md#ansible-collections-ansible-builtin-abs-test) – is the path absolute
- [all test](all_test.md#ansible-collections-ansible-builtin-all-test) – are all conditions in a list true
- [any test](any_test.md#ansible-collections-ansible-builtin-any-test) – is any conditions in a list true
- [changed test](changed_test.md#ansible-collections-ansible-builtin-changed-test) – did the task require changes
- [contains test](contains_test.md#ansible-collections-ansible-builtin-contains-test) – does the list contain this element
- [directory test](directory_test.md#ansible-collections-ansible-builtin-directory-test) – does the path resolve to an existing directory
- [exists test](exists_test.md#ansible-collections-ansible-builtin-exists-test) – does the path exist, follow symlinks
- [failed test](failed_test.md#ansible-collections-ansible-builtin-failed-test) – did the task fail
- [falsy test](falsy_test.md#ansible-collections-ansible-builtin-falsy-test) – Pythonic false
- [file test](file_test.md#ansible-collections-ansible-builtin-file-test) – does the path resolve to an existing file
- [finished test](finished_test.md#ansible-collections-ansible-builtin-finished-test) – Did async task finish
- [link test](link_test.md#ansible-collections-ansible-builtin-link-test) – does the path reference existing symbolic link
- [link_exists test](link_exists_test.md#ansible-collections-ansible-builtin-link-exists-test) – does the path exist, no follow
- [match test](match_test.md#ansible-collections-ansible-builtin-match-test) – Does string match regular expression from the start
- [mount test](mount_test.md#ansible-collections-ansible-builtin-mount-test) – does the path resolve to mount point
- [nan test](nan_test.md#ansible-collections-ansible-builtin-nan-test) – is this not a number (NaN)
- [reachable test](reachable_test.md#ansible-collections-ansible-builtin-reachable-test) – Task did not end due to unreachable host
- [regex test](regex_test.md#ansible-collections-ansible-builtin-regex-test) – Does string match regular expression from the start
- [same_file test](same_file_test.md#ansible-collections-ansible-builtin-same-file-test) – compares two paths to see if they resolve to the same filesystem object
- [search test](search_test.md#ansible-collections-ansible-builtin-search-test) – Does string match a regular expression
- [skipped test](skipped_test.md#ansible-collections-ansible-builtin-skipped-test) – Was task skipped
- [started test](started_test.md#ansible-collections-ansible-builtin-started-test) – Was async task started
- [subset test](subset_test.md#ansible-collections-ansible-builtin-subset-test) – is the list a subset of this other list
- [success test](success_test.md#ansible-collections-ansible-builtin-success-test) – check task success
- [superset test](superset_test.md#ansible-collections-ansible-builtin-superset-test) – is the list a superset of this other list
- [truthy test](truthy_test.md#ansible-collections-ansible-builtin-truthy-test) – Pythonic true
- [unreachable test](unreachable_test.md#ansible-collections-ansible-builtin-unreachable-test) – Did task end due to the host was unreachable
- [uri test](uri_test.md#ansible-collections-ansible-builtin-uri-test) – is the string a valid URI
- [url test](url_test.md#ansible-collections-ansible-builtin-url-test) – is the string a valid URL
- [urn test](urn_test.md#ansible-collections-ansible-builtin-urn-test) – is the string a valid URN
- [vault_encrypted test](vault_encrypted_test.md#ansible-collections-ansible-builtin-vault-encrypted-test) – Is this an encrypted vault
- [version test](version_test.md#ansible-collections-ansible-builtin-version-test) – compare version strings

### Vars Plugins

- [host_group_vars vars](host_group_vars_vars.md#ansible-collections-ansible-builtin-host-group-vars-vars) – In charge of loading group_vars and host_vars

> **See also:**
>
> List of [collections](../../index.md#list-of-collections) with docs hosted here.
