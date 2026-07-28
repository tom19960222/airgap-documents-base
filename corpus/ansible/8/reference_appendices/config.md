---
collection: ansible
version: "8"
title: "Ansible Configuration Settings"
source_url: https://docs.ansible.com/projects/ansible/8/reference_appendices/config.html
fetched_at: 2026-07-28T00:57:58+00:00
---
# Ansible Configuration Settings

Ansible supports several sources for configuring its behavior, including an ini file named `ansible.cfg`, environment variables, command-line options, playbook keywords, and variables. See [Controlling how Ansible behaves: precedence rules](general_precedence.md#general-precedence-rules) for details on the relative precedence of each source.

The `ansible-config` utility allows users to see all the configuration settings available, their defaults, how to set them and
where their current value comes from. See [ansible-config](../cli/ansible-config.md#ansible-config) for more information.

## The configuration file

Changes can be made and used in a configuration file which will be searched for in the following order:

> - `ANSIBLE_CONFIG` (environment variable if set)
> - `ansible.cfg` (in the current directory)
> - `~/.ansible.cfg` (in the home directory)
> - `/etc/ansible/ansible.cfg`

Ansible will process the above list and use the first file found, all others are ignored.

> **Note:**
>
> The configuration file is one variant of an INI format.
> Both the hash sign (`#`) and semicolon (`;`) are allowed as
> comment markers when the comment starts the line.
> However, if the comment is inline with regular values,
> only the semicolon is allowed to introduce the comment.
> For instance:
>
> ```YAML+Jinja
> # some basic default values...
> inventory = /etc/ansible/hosts  ; This points to the file that lists your hosts
> ```

### Generating a sample `ansible.cfg` file

You can generate a fully commented-out example `ansible.cfg` file, for example:

```YAML+Jinja
$ ansible-config init --disabled > ansible.cfg
```

You can also have a more complete file that includes existing plugins:

```YAML+Jinja
$ ansible-config init --disabled -t all > ansible.cfg
```

You can use these as starting points to create your own `ansible.cfg` file.

### Avoiding security risks with `ansible.cfg` in the current directory

If Ansible were to load `ansible.cfg` from a world-writable current working
directory, it would create a serious security risk. Another user could place
their own config file there, designed to make Ansible run malicious code both
locally and remotely, possibly with elevated privileges. For this reason,
Ansible will not automatically load a config file from the current working
directory if the directory is world-writable.

If you depend on using Ansible with a config file in the current working
directory, the best way to avoid this problem is to restrict access to your
Ansible directories to particular user(s) and/or group(s). If your Ansible
directories live on a filesystem which has to emulate Unix permissions, like
Vagrant or Windows Subsystem for Linux (WSL), you may, at first, not know how
you can fix this as `chmod`, `chown`, and `chgrp` might not work there.
In most of those cases, the correct fix is to modify the mount options of the
filesystem so the files and directories are readable and writable by the users
and groups running Ansible but closed to others. For more details on the
correct settings, see:

- for Vagrant, the [Vagrant documentation](https://www.vagrantup.com/docs/synced-folders/) covers synced folder permissions.
- for WSL, the [WSL docs](https://docs.microsoft.com/en-us/windows/wsl/wsl-config#set-wsl-launch-settings)
  and this [Microsoft blog post](https://blogs.msdn.microsoft.com/commandline/2018/01/12/chmod-chown-wsl-improvements/) cover mount options.

If you absolutely depend on storing your Ansible config in a world-writable current
working directory, you can explicitly specify the config file via the
[`ANSIBLE_CONFIG`](config.md#envvar-ANSIBLE_CONFIG) environment variable. Please take
appropriate steps to mitigate the security concerns above before doing so.

### Relative paths for configuration

You can specify a relative path for many configuration options. In most of
those cases the path used will be relative to the `ansible.cfg` file used
for the current execution. If you need a path relative to your current working
directory (CWD) you can use the `{{CWD}}` macro to specify
it. We do not recommend this approach, as using your CWD as the root of
relative paths can be a security risk. For example:
`cd /tmp; secureinfo=./newrootpassword ansible-playbook ~/safestuff/change_root_pwd.yml`.

## Common Options

This is a copy of the options available from our release, your local install might have extra options due to additional plugins,
you can use the command line utility mentioned above (ansible-config) to browse through those.

### ACTION_WARNINGS

Description:
:   By default Ansible will issue a warning when received from a task action (module or action plugin) These warnings can be silenced by adjusting this setting to False.

Type:
:   boolean

Default:
:   `True`

Version Added:
:   2.5

Ini:
:   Section:
    :   [defaults]

    Key:
    :   action_warnings

Environment:
:   Variable:
    :   [`ANSIBLE_ACTION_WARNINGS`](config.md#envvar-ANSIBLE_ACTION_WARNINGS)

### AGNOSTIC_BECOME_PROMPT

Description:
:   Display an agnostic become prompt instead of displaying a prompt containing the command line supplied become method

Type:
:   boolean

Default:
:   `True`

Version Added:
:   2.5

Ini:
:   Section:
    :   [privilege_escalation]

    Key:
    :   agnostic_become_prompt

Environment:
:   Variable:
    :   [`ANSIBLE_AGNOSTIC_BECOME_PROMPT`](config.md#envvar-ANSIBLE_AGNOSTIC_BECOME_PROMPT)

### ANSIBLE_CONNECTION_PATH

Description:
:   Specify where to look for the ansible-connection script. This location will be checked before searching $PATH. If null, ansible will start with the same directory as the ansible script.

Type:
:   path

Default:
:   `None`

Version Added:
:   2.8

Ini:
:   Section:
    :   [persistent_connection]

    Key:
    :   ansible_connection_path

Environment:
:   Variable:
    :   [`ANSIBLE_CONNECTION_PATH`](config.md#envvar-ANSIBLE_CONNECTION_PATH)

### ANSIBLE_COW_ACCEPTLIST

Description:
:   Accept list of cowsay templates that are ‘safe’ to use, set to empty list if you want to enable all installed templates.

Type:
:   list

Default:
:   `['bud-frogs', 'bunny', 'cheese', 'daemon', 'default', 'dragon', 'elephant-in-snake', 'elephant', 'eyes', 'hellokitty', 'kitty', 'luke-koala', 'meow', 'milk', 'moofasa', 'moose', 'ren', 'sheep', 'small', 'stegosaurus', 'stimpy', 'supermilker', 'three-eyes', 'turkey', 'turtle', 'tux', 'udder', 'vader-koala', 'vader', 'www']`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   cowsay_enabled_stencils
        :Version Added: 2.11

Environment:
:   Variable:
    :   [`ANSIBLE_COW_ACCEPTLIST`](config.md#envvar-ANSIBLE_COW_ACCEPTLIST)
        :Version Added: 2.11

### ANSIBLE_COW_PATH

Description:
:   Specify a custom cowsay path or swap in your cowsay implementation of choice

Type:
:   string

Default:
:   `None`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   cowpath

Environment:
:   Variable:
    :   [`ANSIBLE_COW_PATH`](config.md#envvar-ANSIBLE_COW_PATH)

### ANSIBLE_COW_SELECTION

Description:
:   This allows you to chose a specific cowsay stencil for the banners or use ‘random’ to cycle through them.

Default:
:   `default`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   cow_selection

Environment:
:   Variable:
    :   [`ANSIBLE_COW_SELECTION`](config.md#envvar-ANSIBLE_COW_SELECTION)

### ANSIBLE_FORCE_COLOR

Description:
:   This option forces color mode even when running without a TTY or the “nocolor” setting is True.

Type:
:   boolean

Default:
:   `False`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   force_color

Environment:
:   Variable:
    :   [`ANSIBLE_FORCE_COLOR`](config.md#envvar-ANSIBLE_FORCE_COLOR)

### ANSIBLE_HOME

Description:
:   The default root path for Ansible config files on the controller.

Type:
:   path

Default:
:   `~/.ansible`

Version Added:
:   2.14

Ini:
:   Section:
    :   [defaults]

    Key:
    :   home

Environment:
:   Variable:
    :   [`ANSIBLE_HOME`](config.md#envvar-ANSIBLE_HOME)

### ANSIBLE_NOCOLOR

Description:
:   This setting allows suppressing colorizing output, which is used to give a better indication of failure and status information.

Type:
:   boolean

Default:
:   `False`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   nocolor

Environment:
:   - Variable:
      :   [`ANSIBLE_NOCOLOR`](config.md#envvar-ANSIBLE_NOCOLOR)
    - Variable:
      :   [`NO_COLOR`](config.md#envvar-NO_COLOR)

      Version Added:
      :   2.11

### ANSIBLE_NOCOWS

Description:
:   If you have cowsay installed but want to avoid the ‘cows’ (why????), use this.

Type:
:   boolean

Default:
:   `False`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   nocows

Environment:
:   Variable:
    :   [`ANSIBLE_NOCOWS`](config.md#envvar-ANSIBLE_NOCOWS)

### ANSIBLE_PIPELINING

Description:
:   This is a global option, each connection plugin can override either by having more specific options or not supporting pipelining at all. Pipelining, if supported by the connection plugin, reduces the number of network operations required to execute a module on the remote server, by executing many Ansible modules without actual file transfer. It can result in a very significant performance improvement when enabled. However this conflicts with privilege escalation (become). For example, when using ‘sudo:’ operations you must first disable ‘requiretty’ in /etc/sudoers on all managed hosts, which is why it is disabled by default. This setting will be disabled if `ANSIBLE_KEEP_REMOTE_FILES` is enabled.

Type:
:   boolean

Default:
:   `False`

Ini:
:   - Section:
      :   [connection]

      Key:
      :   pipelining
    - Section:
      :   [defaults]

      Key:
      :   pipelining

Environment:
:   Variable:
    :   [`ANSIBLE_PIPELINING`](config.md#envvar-ANSIBLE_PIPELINING)

### ANY_ERRORS_FATAL

Description:
:   Sets the default value for the any_errors_fatal keyword, if True, Task failures will be considered fatal errors.

Type:
:   boolean

Default:
:   `False`

Version Added:
:   2.4

Ini:
:   Section:
    :   [defaults]

    Key:
    :   any_errors_fatal

Environment:
:   Variable:
    :   [`ANSIBLE_ANY_ERRORS_FATAL`](config.md#envvar-ANSIBLE_ANY_ERRORS_FATAL)

### BECOME_ALLOW_SAME_USER

Description:
:   This setting controls if become is skipped when remote user and become user are the same. I.E root sudo to root. If executable, it will be run and the resulting stdout will be used as the password.

Type:
:   boolean

Default:
:   `False`

Ini:
:   Section:
    :   [privilege_escalation]

    Key:
    :   become_allow_same_user

Environment:
:   Variable:
    :   [`ANSIBLE_BECOME_ALLOW_SAME_USER`](config.md#envvar-ANSIBLE_BECOME_ALLOW_SAME_USER)

### BECOME_PASSWORD_FILE

Description:
:   The password file to use for the become plugin. –become-password-file. If executable, it will be run and the resulting stdout will be used as the password.

Type:
:   path

Default:
:   `None`

Version Added:
:   2.12

Ini:
:   Section:
    :   [defaults]

    Key:
    :   become_password_file

Environment:
:   Variable:
    :   [`ANSIBLE_BECOME_PASSWORD_FILE`](config.md#envvar-ANSIBLE_BECOME_PASSWORD_FILE)

### BECOME_PLUGIN_PATH

Description:
:   Colon separated paths in which Ansible will search for Become Plugins.

Type:
:   pathspec

Default:
:   `{{ ANSIBLE_HOME ~ "/plugins/become:/usr/share/ansible/plugins/become" }}`

Version Added:
:   2.8

Ini:
:   Section:
    :   [defaults]

    Key:
    :   become_plugins

Environment:
:   Variable:
    :   [`ANSIBLE_BECOME_PLUGINS`](config.md#envvar-ANSIBLE_BECOME_PLUGINS)

### CACHE_PLUGIN

Description:
:   Chooses which cache plugin to use, the default ‘memory’ is ephemeral.

Default:
:   `memory`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   fact_caching

Environment:
:   Variable:
    :   [`ANSIBLE_CACHE_PLUGIN`](config.md#envvar-ANSIBLE_CACHE_PLUGIN)

### CACHE_PLUGIN_CONNECTION

Description:
:   Defines connection or path information for the cache plugin

Default:
:   `None`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   fact_caching_connection

Environment:
:   Variable:
    :   [`ANSIBLE_CACHE_PLUGIN_CONNECTION`](config.md#envvar-ANSIBLE_CACHE_PLUGIN_CONNECTION)

### CACHE_PLUGIN_PREFIX

Description:
:   Prefix to use for cache plugin files/tables

Default:
:   `ansible_facts`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   fact_caching_prefix

Environment:
:   Variable:
    :   [`ANSIBLE_CACHE_PLUGIN_PREFIX`](config.md#envvar-ANSIBLE_CACHE_PLUGIN_PREFIX)

### CACHE_PLUGIN_TIMEOUT

Description:
:   Expiration timeout for the cache plugin data

Type:
:   integer

Default:
:   `86400`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   fact_caching_timeout

Environment:
:   Variable:
    :   [`ANSIBLE_CACHE_PLUGIN_TIMEOUT`](config.md#envvar-ANSIBLE_CACHE_PLUGIN_TIMEOUT)

### CALLBACKS_ENABLED

Description:
:   List of enabled callbacks, not all callbacks need enabling, but many of those shipped with Ansible do as we don’t want them activated by default.

Type:
:   list

Default:
:   `[]`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   callbacks_enabled
        :Version Added: 2.11

Environment:
:   Variable:
    :   [`ANSIBLE_CALLBACKS_ENABLED`](config.md#envvar-ANSIBLE_CALLBACKS_ENABLED)
        :Version Added: 2.11

### COLLECTIONS_ON_ANSIBLE_VERSION_MISMATCH

Description:
:   When a collection is loaded that does not support the running Ansible version (with the collection metadata key requires_ansible).

Default:
:   `warning`

Choices:
:   - error:
      :   issue a ‘fatal’ error and stop the play
    - warning:
      :   issue a warning but continue
    - ignore:
      :   just continue silently

Ini:
:   Section:
    :   [defaults]

    Key:
    :   collections_on_ansible_version_mismatch

Environment:
:   Variable:
    :   [`ANSIBLE_COLLECTIONS_ON_ANSIBLE_VERSION_MISMATCH`](config.md#envvar-ANSIBLE_COLLECTIONS_ON_ANSIBLE_VERSION_MISMATCH)

### COLLECTIONS_PATHS

Description:
:   Colon separated paths in which Ansible will search for collections content. Collections must be in nested *subdirectories*, not directly in these directories. For example, if `COLLECTIONS_PATHS` includes `'{{ ANSIBLE_HOME ~ "/collections" }}'`, and you want to add `my.collection` to that directory, it must be saved as `'{{ ANSIBLE_HOME} ~ "/collections/ansible_collections/my/collection" }}'`.

Type:
:   pathspec

Default:
:   `{{ ANSIBLE_HOME ~ "/collections:/usr/share/ansible/collections" }}`

Ini:
:   - Section:
      :   [defaults]

      Key:
      :   collections_paths
    - Section:
      :   [defaults]

      Key:
      :   collections_path

      Version Added:
      :   2.10

Environment:
:   - Variable:
      :   [`ANSIBLE_COLLECTIONS_PATH`](config.md#envvar-ANSIBLE_COLLECTIONS_PATH)

      Version Added:
      :   2.10
    - Variable:
      :   [`ANSIBLE_COLLECTIONS_PATHS`](config.md#envvar-ANSIBLE_COLLECTIONS_PATHS)

### COLLECTIONS_SCAN_SYS_PATH

Description:
:   A boolean to enable or disable scanning the sys.path for installed collections

Type:
:   boolean

Default:
:   `True`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   collections_scan_sys_path

Environment:
:   Variable:
    :   [`ANSIBLE_COLLECTIONS_SCAN_SYS_PATH`](config.md#envvar-ANSIBLE_COLLECTIONS_SCAN_SYS_PATH)

### COLOR_CHANGED

Description:
:   Defines the color to use on ‘Changed’ task status

Default:
:   `yellow`

Choices:
:   - black
    - bright gray
    - blue
    - white
    - green
    - bright blue
    - cyan
    - bright green
    - red
    - bright cyan
    - purple
    - bright red
    - yellow
    - bright purple
    - dark gray
    - bright yellow
    - magenta
    - bright magenta
    - normal

Ini:
:   Section:
    :   [colors]

    Key:
    :   changed

Environment:
:   Variable:
    :   [`ANSIBLE_COLOR_CHANGED`](config.md#envvar-ANSIBLE_COLOR_CHANGED)

### COLOR_CONSOLE_PROMPT

Description:
:   Defines the default color to use for ansible-console

Default:
:   `white`

Choices:
:   - black
    - bright gray
    - blue
    - white
    - green
    - bright blue
    - cyan
    - bright green
    - red
    - bright cyan
    - purple
    - bright red
    - yellow
    - bright purple
    - dark gray
    - bright yellow
    - magenta
    - bright magenta
    - normal

Version Added:
:   2.7

Ini:
:   Section:
    :   [colors]

    Key:
    :   console_prompt

Environment:
:   Variable:
    :   [`ANSIBLE_COLOR_CONSOLE_PROMPT`](config.md#envvar-ANSIBLE_COLOR_CONSOLE_PROMPT)

### COLOR_DEBUG

Description:
:   Defines the color to use when emitting debug messages

Default:
:   `dark gray`

Choices:
:   - black
    - bright gray
    - blue
    - white
    - green
    - bright blue
    - cyan
    - bright green
    - red
    - bright cyan
    - purple
    - bright red
    - yellow
    - bright purple
    - dark gray
    - bright yellow
    - magenta
    - bright magenta
    - normal

Ini:
:   Section:
    :   [colors]

    Key:
    :   debug

Environment:
:   Variable:
    :   [`ANSIBLE_COLOR_DEBUG`](config.md#envvar-ANSIBLE_COLOR_DEBUG)

### COLOR_DEPRECATE

Description:
:   Defines the color to use when emitting deprecation messages

Default:
:   `purple`

Choices:
:   - black
    - bright gray
    - blue
    - white
    - green
    - bright blue
    - cyan
    - bright green
    - red
    - bright cyan
    - purple
    - bright red
    - yellow
    - bright purple
    - dark gray
    - bright yellow
    - magenta
    - bright magenta
    - normal

Ini:
:   Section:
    :   [colors]

    Key:
    :   deprecate

Environment:
:   Variable:
    :   [`ANSIBLE_COLOR_DEPRECATE`](config.md#envvar-ANSIBLE_COLOR_DEPRECATE)

### COLOR_DIFF_ADD

Description:
:   Defines the color to use when showing added lines in diffs

Default:
:   `green`

Choices:
:   - black
    - bright gray
    - blue
    - white
    - green
    - bright blue
    - cyan
    - bright green
    - red
    - bright cyan
    - purple
    - bright red
    - yellow
    - bright purple
    - dark gray
    - bright yellow
    - magenta
    - bright magenta
    - normal

Ini:
:   Section:
    :   [colors]

    Key:
    :   diff_add

Environment:
:   Variable:
    :   [`ANSIBLE_COLOR_DIFF_ADD`](config.md#envvar-ANSIBLE_COLOR_DIFF_ADD)

### COLOR_DIFF_LINES

Description:
:   Defines the color to use when showing diffs

Default:
:   `cyan`

Choices:
:   - black
    - bright gray
    - blue
    - white
    - green
    - bright blue
    - cyan
    - bright green
    - red
    - bright cyan
    - purple
    - bright red
    - yellow
    - bright purple
    - dark gray
    - bright yellow
    - magenta
    - bright magenta
    - normal

Ini:
:   Section:
    :   [colors]

    Key:
    :   diff_lines

Environment:
:   Variable:
    :   [`ANSIBLE_COLOR_DIFF_LINES`](config.md#envvar-ANSIBLE_COLOR_DIFF_LINES)

### COLOR_DIFF_REMOVE

Description:
:   Defines the color to use when showing removed lines in diffs

Default:
:   `red`

Choices:
:   - black
    - bright gray
    - blue
    - white
    - green
    - bright blue
    - cyan
    - bright green
    - red
    - bright cyan
    - purple
    - bright red
    - yellow
    - bright purple
    - dark gray
    - bright yellow
    - magenta
    - bright magenta
    - normal

Ini:
:   Section:
    :   [colors]

    Key:
    :   diff_remove

Environment:
:   Variable:
    :   [`ANSIBLE_COLOR_DIFF_REMOVE`](config.md#envvar-ANSIBLE_COLOR_DIFF_REMOVE)

### COLOR_ERROR

Description:
:   Defines the color to use when emitting error messages

Default:
:   `red`

Choices:
:   - black
    - bright gray
    - blue
    - white
    - green
    - bright blue
    - cyan
    - bright green
    - red
    - bright cyan
    - purple
    - bright red
    - yellow
    - bright purple
    - dark gray
    - bright yellow
    - magenta
    - bright magenta
    - normal

Ini:
:   Section:
    :   [colors]

    Key:
    :   error

Environment:
:   Variable:
    :   [`ANSIBLE_COLOR_ERROR`](config.md#envvar-ANSIBLE_COLOR_ERROR)

### COLOR_HIGHLIGHT

Description:
:   Defines the color to use for highlighting

Default:
:   `white`

Choices:
:   - black
    - bright gray
    - blue
    - white
    - green
    - bright blue
    - cyan
    - bright green
    - red
    - bright cyan
    - purple
    - bright red
    - yellow
    - bright purple
    - dark gray
    - bright yellow
    - magenta
    - bright magenta
    - normal

Ini:
:   Section:
    :   [colors]

    Key:
    :   highlight

Environment:
:   Variable:
    :   [`ANSIBLE_COLOR_HIGHLIGHT`](config.md#envvar-ANSIBLE_COLOR_HIGHLIGHT)

### COLOR_OK

Description:
:   Defines the color to use when showing ‘OK’ task status

Default:
:   `green`

Choices:
:   - black
    - bright gray
    - blue
    - white
    - green
    - bright blue
    - cyan
    - bright green
    - red
    - bright cyan
    - purple
    - bright red
    - yellow
    - bright purple
    - dark gray
    - bright yellow
    - magenta
    - bright magenta
    - normal

Ini:
:   Section:
    :   [colors]

    Key:
    :   ok

Environment:
:   Variable:
    :   [`ANSIBLE_COLOR_OK`](config.md#envvar-ANSIBLE_COLOR_OK)

### COLOR_SKIP

Description:
:   Defines the color to use when showing ‘Skipped’ task status

Default:
:   `cyan`

Choices:
:   - black
    - bright gray
    - blue
    - white
    - green
    - bright blue
    - cyan
    - bright green
    - red
    - bright cyan
    - purple
    - bright red
    - yellow
    - bright purple
    - dark gray
    - bright yellow
    - magenta
    - bright magenta
    - normal

Ini:
:   Section:
    :   [colors]

    Key:
    :   skip

Environment:
:   Variable:
    :   [`ANSIBLE_COLOR_SKIP`](config.md#envvar-ANSIBLE_COLOR_SKIP)

### COLOR_UNREACHABLE

Description:
:   Defines the color to use on ‘Unreachable’ status

Default:
:   `bright red`

Choices:
:   - black
    - bright gray
    - blue
    - white
    - green
    - bright blue
    - cyan
    - bright green
    - red
    - bright cyan
    - purple
    - bright red
    - yellow
    - bright purple
    - dark gray
    - bright yellow
    - magenta
    - bright magenta
    - normal

Ini:
:   Section:
    :   [colors]

    Key:
    :   unreachable

Environment:
:   Variable:
    :   [`ANSIBLE_COLOR_UNREACHABLE`](config.md#envvar-ANSIBLE_COLOR_UNREACHABLE)

### COLOR_VERBOSE

Description:
:   Defines the color to use when emitting verbose messages. i.e those that show with ‘-v’s.

Default:
:   `blue`

Choices:
:   - black
    - bright gray
    - blue
    - white
    - green
    - bright blue
    - cyan
    - bright green
    - red
    - bright cyan
    - purple
    - bright red
    - yellow
    - bright purple
    - dark gray
    - bright yellow
    - magenta
    - bright magenta
    - normal

Ini:
:   Section:
    :   [colors]

    Key:
    :   verbose

Environment:
:   Variable:
    :   [`ANSIBLE_COLOR_VERBOSE`](config.md#envvar-ANSIBLE_COLOR_VERBOSE)

### COLOR_WARN

Description:
:   Defines the color to use when emitting warning messages

Default:
:   `bright purple`

Choices:
:   - black
    - bright gray
    - blue
    - white
    - green
    - bright blue
    - cyan
    - bright green
    - red
    - bright cyan
    - purple
    - bright red
    - yellow
    - bright purple
    - dark gray
    - bright yellow
    - magenta
    - bright magenta
    - normal

Ini:
:   Section:
    :   [colors]

    Key:
    :   warn

Environment:
:   Variable:
    :   [`ANSIBLE_COLOR_WARN`](config.md#envvar-ANSIBLE_COLOR_WARN)

### CONNECTION_FACTS_MODULES

Description:
:   Which modules to run during a play’s fact gathering stage based on connection

Type:
:   dict

Default:
:   `{'asa': 'ansible.legacy.asa_facts', 'cisco.asa.asa': 'cisco.asa.asa_facts', 'eos': 'ansible.legacy.eos_facts', 'arista.eos.eos': 'arista.eos.eos_facts', 'frr': 'ansible.legacy.frr_facts', 'frr.frr.frr': 'frr.frr.frr_facts', 'ios': 'ansible.legacy.ios_facts', 'cisco.ios.ios': 'cisco.ios.ios_facts', 'iosxr': 'ansible.legacy.iosxr_facts', 'cisco.iosxr.iosxr': 'cisco.iosxr.iosxr_facts', 'junos': 'ansible.legacy.junos_facts', 'junipernetworks.junos.junos': 'junipernetworks.junos.junos_facts', 'nxos': 'ansible.legacy.nxos_facts', 'cisco.nxos.nxos': 'cisco.nxos.nxos_facts', 'vyos': 'ansible.legacy.vyos_facts', 'vyos.vyos.vyos': 'vyos.vyos.vyos_facts', 'exos': 'ansible.legacy.exos_facts', 'extreme.exos.exos': 'extreme.exos.exos_facts', 'slxos': 'ansible.legacy.slxos_facts', 'extreme.slxos.slxos': 'extreme.slxos.slxos_facts', 'voss': 'ansible.legacy.voss_facts', 'extreme.voss.voss': 'extreme.voss.voss_facts', 'ironware': 'ansible.legacy.ironware_facts', 'community.network.ironware': 'community.network.ironware_facts'}`

### CONNECTION_PASSWORD_FILE

Description:
:   The password file to use for the connection plugin. –connection-password-file.

Type:
:   path

Default:
:   `None`

Version Added:
:   2.12

Ini:
:   Section:
    :   [defaults]

    Key:
    :   connection_password_file

Environment:
:   Variable:
    :   [`ANSIBLE_CONNECTION_PASSWORD_FILE`](config.md#envvar-ANSIBLE_CONNECTION_PASSWORD_FILE)

### COVERAGE_REMOTE_OUTPUT

Description:
:   Sets the output directory on the remote host to generate coverage reports to. Currently only used for remote coverage on PowerShell modules. This is for internal use only.

Type:
:   str

Version Added:
:   2.9

Environment:
:   Variable:
    :   [`_ANSIBLE_COVERAGE_REMOTE_OUTPUT`](config.md#envvar-_ANSIBLE_COVERAGE_REMOTE_OUTPUT)

Variables:
:   name:
    :   _ansible_coverage_remote_output

### COVERAGE_REMOTE_PATHS

Description:
:   A list of paths for files on the Ansible controller to run coverage for when executing on the remote host. Only files that match the path glob will have its coverage collected. Multiple path globs can be specified and are separated by `:`. Currently only used for remote coverage on PowerShell modules. This is for internal use only.

Type:
:   str

Default:
:   `*`

Version Added:
:   2.9

Environment:
:   Variable:
    :   [`_ANSIBLE_COVERAGE_REMOTE_PATH_FILTER`](config.md#envvar-_ANSIBLE_COVERAGE_REMOTE_PATH_FILTER)

### DEFAULT_ACTION_PLUGIN_PATH

Description:
:   Colon separated paths in which Ansible will search for Action Plugins.

Type:
:   pathspec

Default:
:   `{{ ANSIBLE_HOME ~ "/plugins/action:/usr/share/ansible/plugins/action" }}`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   action_plugins

Environment:
:   Variable:
    :   [`ANSIBLE_ACTION_PLUGINS`](config.md#envvar-ANSIBLE_ACTION_PLUGINS)

### DEFAULT_ALLOW_UNSAFE_LOOKUPS

Description:
:   When enabled, this option allows lookup plugins (whether used in variables as `{{lookup('foo')}}` or as a loop as with_foo) to return data that is not marked ‘unsafe’. By default, such data is marked as unsafe to prevent the templating engine from evaluating any jinja2 templating language, as this could represent a security risk. This option is provided to allow for backward compatibility, however users should first consider adding allow_unsafe=True to any lookups which may be expected to contain data which may be run through the templating engine late

Type:
:   boolean

Default:
:   `False`

Version Added:
:   2.2.3

Ini:
:   Section:
    :   [defaults]

    Key:
    :   allow_unsafe_lookups

### DEFAULT_ASK_PASS

Description:
:   This controls whether an Ansible playbook should prompt for a login password. If using SSH keys for authentication, you probably do not need to change this setting.

Type:
:   boolean

Default:
:   `False`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   ask_pass

Environment:
:   Variable:
    :   [`ANSIBLE_ASK_PASS`](config.md#envvar-ANSIBLE_ASK_PASS)

### DEFAULT_ASK_VAULT_PASS

Description:
:   This controls whether an Ansible playbook should prompt for a vault password.

Type:
:   boolean

Default:
:   `False`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   ask_vault_pass

Environment:
:   Variable:
    :   [`ANSIBLE_ASK_VAULT_PASS`](config.md#envvar-ANSIBLE_ASK_VAULT_PASS)

### DEFAULT_BECOME

Description:
:   Toggles the use of privilege escalation, allowing you to ‘become’ another user after login.

Type:
:   boolean

Default:
:   `False`

Ini:
:   Section:
    :   [privilege_escalation]

    Key:
    :   become

Environment:
:   Variable:
    :   [`ANSIBLE_BECOME`](config.md#envvar-ANSIBLE_BECOME)

### DEFAULT_BECOME_ASK_PASS

Description:
:   Toggle to prompt for privilege escalation password.

Type:
:   boolean

Default:
:   `False`

Ini:
:   Section:
    :   [privilege_escalation]

    Key:
    :   become_ask_pass

Environment:
:   Variable:
    :   [`ANSIBLE_BECOME_ASK_PASS`](config.md#envvar-ANSIBLE_BECOME_ASK_PASS)

### DEFAULT_BECOME_EXE

Description:
:   executable to use for privilege escalation, otherwise Ansible will depend on PATH

Default:
:   `None`

Ini:
:   Section:
    :   [privilege_escalation]

    Key:
    :   become_exe

Environment:
:   Variable:
    :   [`ANSIBLE_BECOME_EXE`](config.md#envvar-ANSIBLE_BECOME_EXE)

### DEFAULT_BECOME_FLAGS

Description:
:   Flags to pass to the privilege escalation executable.

Default:

Ini:
:   Section:
    :   [privilege_escalation]

    Key:
    :   become_flags

Environment:
:   Variable:
    :   [`ANSIBLE_BECOME_FLAGS`](config.md#envvar-ANSIBLE_BECOME_FLAGS)

### DEFAULT_BECOME_METHOD

Description:
:   Privilege escalation method to use when become is enabled.

Default:
:   `sudo`

Ini:
:   Section:
    :   [privilege_escalation]

    Key:
    :   become_method

Environment:
:   Variable:
    :   [`ANSIBLE_BECOME_METHOD`](config.md#envvar-ANSIBLE_BECOME_METHOD)

### DEFAULT_BECOME_USER

Description:
:   The user your login/remote user ‘becomes’ when using privilege escalation, most systems will use ‘root’ when no user is specified.

Default:
:   `root`

Ini:
:   Section:
    :   [privilege_escalation]

    Key:
    :   become_user

Environment:
:   Variable:
    :   [`ANSIBLE_BECOME_USER`](config.md#envvar-ANSIBLE_BECOME_USER)

### DEFAULT_CACHE_PLUGIN_PATH

Description:
:   Colon separated paths in which Ansible will search for Cache Plugins.

Type:
:   pathspec

Default:
:   `{{ ANSIBLE_HOME ~ "/plugins/cache:/usr/share/ansible/plugins/cache" }}`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   cache_plugins

Environment:
:   Variable:
    :   [`ANSIBLE_CACHE_PLUGINS`](config.md#envvar-ANSIBLE_CACHE_PLUGINS)

### DEFAULT_CALLBACK_PLUGIN_PATH

Description:
:   Colon separated paths in which Ansible will search for Callback Plugins.

Type:
:   pathspec

Default:
:   `{{ ANSIBLE_HOME ~ "/plugins/callback:/usr/share/ansible/plugins/callback" }}`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   callback_plugins

Environment:
:   Variable:
    :   [`ANSIBLE_CALLBACK_PLUGINS`](config.md#envvar-ANSIBLE_CALLBACK_PLUGINS)

### DEFAULT_CLICONF_PLUGIN_PATH

Description:
:   Colon separated paths in which Ansible will search for Cliconf Plugins.

Type:
:   pathspec

Default:
:   `{{ ANSIBLE_HOME ~ "/plugins/cliconf:/usr/share/ansible/plugins/cliconf" }}`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   cliconf_plugins

Environment:
:   Variable:
    :   [`ANSIBLE_CLICONF_PLUGINS`](config.md#envvar-ANSIBLE_CLICONF_PLUGINS)

### DEFAULT_CONNECTION_PLUGIN_PATH

Description:
:   Colon separated paths in which Ansible will search for Connection Plugins.

Type:
:   pathspec

Default:
:   `{{ ANSIBLE_HOME ~ "/plugins/connection:/usr/share/ansible/plugins/connection" }}`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   connection_plugins

Environment:
:   Variable:
    :   [`ANSIBLE_CONNECTION_PLUGINS`](config.md#envvar-ANSIBLE_CONNECTION_PLUGINS)

### DEFAULT_DEBUG

Description:
:   Toggles debug output in Ansible. This is *very* verbose and can hinder multiprocessing. Debug output can also include secret information despite no_log settings being enabled, which means debug mode should not be used in production.

Type:
:   boolean

Default:
:   `False`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   debug

Environment:
:   Variable:
    :   [`ANSIBLE_DEBUG`](config.md#envvar-ANSIBLE_DEBUG)

### DEFAULT_EXECUTABLE

Description:
:   This indicates the command to use to spawn a shell under for Ansible’s execution needs on a target. Users may need to change this in rare instances when shell usage is constrained, but in most cases it may be left as is.

Default:
:   `/bin/sh`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   executable

Environment:
:   Variable:
    :   [`ANSIBLE_EXECUTABLE`](config.md#envvar-ANSIBLE_EXECUTABLE)

### DEFAULT_FACT_PATH

Description:
:   This option allows you to globally configure a custom path for ‘local_facts’ for the implied [ansible_collections.ansible.builtin.setup_module](https://docs.ansible.com/ansible/7/collections/ansible/builtin/setup_module.html#ansible-collections-ansible-builtin-setup-module "(in Ansible v7)") task when using fact gathering. If not set, it will fallback to the default from the `ansible.builtin.setup` module: `/etc/ansible/facts.d`. This does **not** affect user defined tasks that use the `ansible.builtin.setup` module. The real action being created by the implicit task is currently `ansible.legacy.gather_facts` module, which then calls the configured fact modules, by default this will be `ansible.builtin.setup` for POSIX systems but other platforms might have different defaults.

Type:
:   string

Ini:
:   Section:
    :   [defaults]

    Key:
    :   fact_path

Environment:
:   Variable:
    :   [`ANSIBLE_FACT_PATH`](config.md#envvar-ANSIBLE_FACT_PATH)

Deprecated in:
:   2.18

Deprecated detail:
:   the module_defaults keyword is a more generic version and can apply to all calls to the M(ansible.builtin.gather_facts) or M(ansible.builtin.setup) actions

Deprecated alternatives:
:   module_defaults

### DEFAULT_FILTER_PLUGIN_PATH

Description:
:   Colon separated paths in which Ansible will search for Jinja2 Filter Plugins.

Type:
:   pathspec

Default:
:   `{{ ANSIBLE_HOME ~ "/plugins/filter:/usr/share/ansible/plugins/filter" }}`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   filter_plugins

Environment:
:   Variable:
    :   [`ANSIBLE_FILTER_PLUGINS`](config.md#envvar-ANSIBLE_FILTER_PLUGINS)

### DEFAULT_FORCE_HANDLERS

Description:
:   This option controls if notified handlers run on a host even if a failure occurs on that host. When false, the handlers will not run if a failure has occurred on a host. This can also be set per play or on the command line. See Handlers and Failure for more details.

Type:
:   boolean

Default:
:   `False`

Version Added:
:   1.9.1

Ini:
:   Section:
    :   [defaults]

    Key:
    :   force_handlers

Environment:
:   Variable:
    :   [`ANSIBLE_FORCE_HANDLERS`](config.md#envvar-ANSIBLE_FORCE_HANDLERS)

### DEFAULT_FORKS

Description:
:   Maximum number of forks Ansible will use to execute tasks on target hosts.

Type:
:   integer

Default:
:   `5`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   forks

Environment:
:   Variable:
    :   [`ANSIBLE_FORKS`](config.md#envvar-ANSIBLE_FORKS)

### DEFAULT_GATHER_SUBSET

Description:
:   Set the gather_subset option for the [ansible_collections.ansible.builtin.setup_module](https://docs.ansible.com/ansible/7/collections/ansible/builtin/setup_module.html#ansible-collections-ansible-builtin-setup-module "(in Ansible v7)") task in the implicit fact gathering. See the module documentation for specifics. It does **not** apply to user defined `ansible.builtin.setup` tasks.

Type:
:   list

Version Added:
:   2.1

Ini:
:   Section:
    :   [defaults]

    Key:
    :   gather_subset

Environment:
:   Variable:
    :   [`ANSIBLE_GATHER_SUBSET`](config.md#envvar-ANSIBLE_GATHER_SUBSET)

Deprecated in:
:   2.18

Deprecated detail:
:   the module_defaults keyword is a more generic version and can apply to all calls to the M(ansible.builtin.gather_facts) or M(ansible.builtin.setup) actions

Deprecated alternatives:
:   module_defaults

### DEFAULT_GATHER_TIMEOUT

Description:
:   Set the timeout in seconds for the implicit fact gathering, see the module documentation for specifics. It does **not** apply to user defined [ansible_collections.ansible.builtin.setup_module](https://docs.ansible.com/ansible/7/collections/ansible/builtin/setup_module.html#ansible-collections-ansible-builtin-setup-module "(in Ansible v7)") tasks.

Type:
:   integer

Ini:
:   Section:
    :   [defaults]

    Key:
    :   gather_timeout

Environment:
:   Variable:
    :   [`ANSIBLE_GATHER_TIMEOUT`](config.md#envvar-ANSIBLE_GATHER_TIMEOUT)

Deprecated in:
:   2.18

Deprecated detail:
:   the module_defaults keyword is a more generic version and can apply to all calls to the M(ansible.builtin.gather_facts) or M(ansible.builtin.setup) actions

Deprecated alternatives:
:   module_defaults

### DEFAULT_GATHERING

Description:
:   This setting controls the default policy of fact gathering (facts discovered about remote systems). This option can be useful for those wishing to save fact gathering time. Both ‘smart’ and ‘explicit’ will use the cache plugin.

Default:
:   `implicit`

Choices:
:   - implicit:
      :   the cache plugin will be ignored and facts will be gathered per play unless ‘gather_facts: False’ is set.
    - explicit:
      :   facts will not be gathered unless directly requested in the play.
    - smart:
      :   each new host that has no facts discovered will be scanned, but if the same host is addressed in multiple plays it will not be contacted again in the run.

Version Added:
:   1.6

Ini:
:   Section:
    :   [defaults]

    Key:
    :   gathering

Environment:
:   Variable:
    :   [`ANSIBLE_GATHERING`](config.md#envvar-ANSIBLE_GATHERING)

### DEFAULT_HASH_BEHAVIOUR

Description:
:   This setting controls how duplicate definitions of dictionary variables (aka hash, map, associative array) are handled in Ansible. This does not affect variables whose values are scalars (integers, strings) or arrays. **WARNING**, changing this setting is not recommended as this is fragile and makes your content (plays, roles, collections) non portable, leading to continual confusion and misuse. Don’t change this setting unless you think you have an absolute need for it. We recommend avoiding reusing variable names and relying on the `combine` filter and `vars` and `varnames` lookups to create merged versions of the individual variables. In our experience this is rarely really needed and a sign that too much complexity has been introduced into the data structures and plays. For some uses you can also look into custom vars_plugins to merge on input, even substituting the default `host_group_vars` that is in charge of parsing the `host_vars/` and `group_vars/` directories. Most users of this setting are only interested in inventory scope, but the setting itself affects all sources and makes debugging even harder. All playbooks and roles in the official examples repos assume the default for this setting. Changing the setting to `merge` applies across variable sources, but many sources will internally still overwrite the variables. For example `include_vars` will dedupe variables internally before updating Ansible, with ‘last defined’ overwriting previous definitions in same file. The Ansible project recommends you **avoid ``merge`` for new projects.** It is the intention of the Ansible developers to eventually deprecate and remove this setting, but it is being kept as some users do heavily rely on it. New projects should **avoid ‘merge’**.

Type:
:   string

Default:
:   `replace`

Choices:
:   - replace:
      :   Any variable that is defined more than once is overwritten using the order from variable precedence rules (highest wins).
    - merge:
      :   Any dictionary variable will be recursively merged with new definitions across the different variable definition sources.

Ini:
:   Section:
    :   [defaults]

    Key:
    :   hash_behaviour

Environment:
:   Variable:
    :   [`ANSIBLE_HASH_BEHAVIOUR`](config.md#envvar-ANSIBLE_HASH_BEHAVIOUR)

### DEFAULT_HOST_LIST

Description:
:   Comma separated list of Ansible inventory sources

Type:
:   pathlist

Default:
:   `/etc/ansible/hosts`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   inventory

Environment:
:   Variable:
    :   [`ANSIBLE_INVENTORY`](config.md#envvar-ANSIBLE_INVENTORY)

### DEFAULT_HTTPAPI_PLUGIN_PATH

Description:
:   Colon separated paths in which Ansible will search for HttpApi Plugins.

Type:
:   pathspec

Default:
:   `{{ ANSIBLE_HOME ~ "/plugins/httpapi:/usr/share/ansible/plugins/httpapi" }}`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   httpapi_plugins

Environment:
:   Variable:
    :   [`ANSIBLE_HTTPAPI_PLUGINS`](config.md#envvar-ANSIBLE_HTTPAPI_PLUGINS)

### DEFAULT_INTERNAL_POLL_INTERVAL

Description:
:   This sets the interval (in seconds) of Ansible internal processes polling each other. Lower values improve performance with large playbooks at the expense of extra CPU load. Higher values are more suitable for Ansible usage in automation scenarios, when UI responsiveness is not required but CPU usage might be a concern. The default corresponds to the value hardcoded in Ansible <= 2.1

Type:
:   float

Default:
:   `0.001`

Version Added:
:   2.2

Ini:
:   Section:
    :   [defaults]

    Key:
    :   internal_poll_interval

### DEFAULT_INVENTORY_PLUGIN_PATH

Description:
:   Colon separated paths in which Ansible will search for Inventory Plugins.

Type:
:   pathspec

Default:
:   `{{ ANSIBLE_HOME ~ "/plugins/inventory:/usr/share/ansible/plugins/inventory" }}`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   inventory_plugins

Environment:
:   Variable:
    :   [`ANSIBLE_INVENTORY_PLUGINS`](config.md#envvar-ANSIBLE_INVENTORY_PLUGINS)

### DEFAULT_JINJA2_EXTENSIONS

Description:
:   This is a developer-specific feature that allows enabling additional Jinja2 extensions. See the Jinja2 documentation for details. If you do not know what these do, you probably don’t need to change this setting :)

Default:
:   `[]`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   jinja2_extensions

Environment:
:   Variable:
    :   [`ANSIBLE_JINJA2_EXTENSIONS`](config.md#envvar-ANSIBLE_JINJA2_EXTENSIONS)

### DEFAULT_JINJA2_NATIVE

Description:
:   This option preserves variable types during template operations.

Type:
:   boolean

Default:
:   `False`

Version Added:
:   2.7

Ini:
:   Section:
    :   [defaults]

    Key:
    :   jinja2_native

Environment:
:   Variable:
    :   [`ANSIBLE_JINJA2_NATIVE`](config.md#envvar-ANSIBLE_JINJA2_NATIVE)

### DEFAULT_KEEP_REMOTE_FILES

Description:
:   Enables/disables the cleaning up of the temporary files Ansible used to execute the tasks on the remote. If this option is enabled it will disable `ANSIBLE_PIPELINING`.

Type:
:   boolean

Default:
:   `False`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   keep_remote_files

Environment:
:   Variable:
    :   [`ANSIBLE_KEEP_REMOTE_FILES`](config.md#envvar-ANSIBLE_KEEP_REMOTE_FILES)

### DEFAULT_LIBVIRT_LXC_NOSECLABEL

Description:
:   This setting causes libvirt to connect to lxc containers by passing –noseclabel to virsh. This is necessary when running on systems which do not have SELinux.

Type:
:   boolean

Default:
:   `False`

Version Added:
:   2.1

Ini:
:   Section:
    :   [selinux]

    Key:
    :   libvirt_lxc_noseclabel

Environment:
:   Variable:
    :   [`ANSIBLE_LIBVIRT_LXC_NOSECLABEL`](config.md#envvar-ANSIBLE_LIBVIRT_LXC_NOSECLABEL)

### DEFAULT_LOAD_CALLBACK_PLUGINS

Description:
:   Controls whether callback plugins are loaded when running /usr/bin/ansible. This may be used to log activity from the command line, send notifications, and so on. Callback plugins are always loaded for `ansible-playbook`.

Type:
:   boolean

Default:
:   `False`

Version Added:
:   1.8

Ini:
:   Section:
    :   [defaults]

    Key:
    :   bin_ansible_callbacks

Environment:
:   Variable:
    :   [`ANSIBLE_LOAD_CALLBACK_PLUGINS`](config.md#envvar-ANSIBLE_LOAD_CALLBACK_PLUGINS)

### DEFAULT_LOCAL_TMP

Description:
:   Temporary directory for Ansible to use on the controller.

Type:
:   tmppath

Default:
:   `{{ ANSIBLE_HOME ~ "/tmp" }}`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   local_tmp

Environment:
:   Variable:
    :   [`ANSIBLE_LOCAL_TEMP`](config.md#envvar-ANSIBLE_LOCAL_TEMP)

### DEFAULT_LOG_FILTER

Description:
:   List of logger names to filter out of the log file

Type:
:   list

Default:
:   `[]`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   log_filter

Environment:
:   Variable:
    :   [`ANSIBLE_LOG_FILTER`](config.md#envvar-ANSIBLE_LOG_FILTER)

### DEFAULT_LOG_PATH

Description:
:   File to which Ansible will log on the controller. When empty logging is disabled.

Type:
:   path

Default:
:   `None`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   log_path

Environment:
:   Variable:
    :   [`ANSIBLE_LOG_PATH`](config.md#envvar-ANSIBLE_LOG_PATH)

### DEFAULT_LOOKUP_PLUGIN_PATH

Description:
:   Colon separated paths in which Ansible will search for Lookup Plugins.

Type:
:   pathspec

Default:
:   `{{ ANSIBLE_HOME ~ "/plugins/lookup:/usr/share/ansible/plugins/lookup" }}`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   lookup_plugins

Environment:
:   Variable:
    :   [`ANSIBLE_LOOKUP_PLUGINS`](config.md#envvar-ANSIBLE_LOOKUP_PLUGINS)

### DEFAULT_MANAGED_STR

Description:
:   Sets the macro for the ‘ansible_managed’ variable available for [ansible_collections.ansible.builtin.template_module](https://docs.ansible.com/ansible/7/collections/ansible/builtin/template_module.html#ansible-collections-ansible-builtin-template-module "(in Ansible v7)") and [ansible_collections.ansible.windows.win_template_module](https://docs.ansible.com/ansible/7/collections/ansible/windows/win_template_module.html#ansible-collections-ansible-windows-win-template-module "(in Ansible v7)"). This is only relevant for those two modules.

Default:
:   `Ansible managed`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   ansible_managed

### DEFAULT_MODULE_ARGS

Description:
:   This sets the default arguments to pass to the `ansible` adhoc binary if no `-a` is specified.

Default:
:   `None`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   module_args

Environment:
:   Variable:
    :   [`ANSIBLE_MODULE_ARGS`](config.md#envvar-ANSIBLE_MODULE_ARGS)

### DEFAULT_MODULE_COMPRESSION

Description:
:   Compression scheme to use when transferring Python modules to the target.

Default:
:   `ZIP_DEFLATED`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   module_compression

### DEFAULT_MODULE_NAME

Description:
:   Module to use with the `ansible` AdHoc command, if none is specified via `-m`.

Default:
:   `command`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   module_name

### DEFAULT_MODULE_PATH

Description:
:   Colon separated paths in which Ansible will search for Modules.

Type:
:   pathspec

Default:
:   `{{ ANSIBLE_HOME ~ "/plugins/modules:/usr/share/ansible/plugins/modules" }}`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   library

Environment:
:   Variable:
    :   [`ANSIBLE_LIBRARY`](config.md#envvar-ANSIBLE_LIBRARY)

### DEFAULT_MODULE_UTILS_PATH

Description:
:   Colon separated paths in which Ansible will search for Module utils files, which are shared by modules.

Type:
:   pathspec

Default:
:   `{{ ANSIBLE_HOME ~ "/plugins/module_utils:/usr/share/ansible/plugins/module_utils" }}`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   module_utils

Environment:
:   Variable:
    :   [`ANSIBLE_MODULE_UTILS`](config.md#envvar-ANSIBLE_MODULE_UTILS)

### DEFAULT_NETCONF_PLUGIN_PATH

Description:
:   Colon separated paths in which Ansible will search for Netconf Plugins.

Type:
:   pathspec

Default:
:   `{{ ANSIBLE_HOME ~ "/plugins/netconf:/usr/share/ansible/plugins/netconf" }}`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   netconf_plugins

Environment:
:   Variable:
    :   [`ANSIBLE_NETCONF_PLUGINS`](config.md#envvar-ANSIBLE_NETCONF_PLUGINS)

### DEFAULT_NO_LOG

Description:
:   Toggle Ansible’s display and logging of task details, mainly used to avoid security disclosures.

Type:
:   boolean

Default:
:   `False`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   no_log

Environment:
:   Variable:
    :   [`ANSIBLE_NO_LOG`](config.md#envvar-ANSIBLE_NO_LOG)

### DEFAULT_NO_TARGET_SYSLOG

Description:
:   Toggle Ansible logging to syslog on the target when it executes tasks. On Windows hosts this will disable a newer style PowerShell modules from writing to the event log.

Type:
:   boolean

Default:
:   `False`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   no_target_syslog

Environment:
:   Variable:
    :   [`ANSIBLE_NO_TARGET_SYSLOG`](config.md#envvar-ANSIBLE_NO_TARGET_SYSLOG)

Variables:
:   name:
    :   ansible_no_target_syslog
        :Version Added: 2.10

### DEFAULT_NULL_REPRESENTATION

Description:
:   What templating should return as a ‘null’ value. When not set it will let Jinja2 decide.

Type:
:   raw

Default:
:   `None`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   null_representation

Environment:
:   Variable:
    :   [`ANSIBLE_NULL_REPRESENTATION`](config.md#envvar-ANSIBLE_NULL_REPRESENTATION)

### DEFAULT_POLL_INTERVAL

Description:
:   For asynchronous tasks in Ansible (covered in Asynchronous Actions and Polling), this is how often to check back on the status of those tasks when an explicit poll interval is not supplied. The default is a reasonably moderate 15 seconds which is a tradeoff between checking in frequently and providing a quick turnaround when something may have completed.

Type:
:   integer

Default:
:   `15`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   poll_interval

Environment:
:   Variable:
    :   [`ANSIBLE_POLL_INTERVAL`](config.md#envvar-ANSIBLE_POLL_INTERVAL)

### DEFAULT_PRIVATE_KEY_FILE

Description:
:   Option for connections using a certificate or key file to authenticate, rather than an agent or passwords, you can set the default value here to avoid re-specifying –private-key with every invocation.

Type:
:   path

Default:
:   `None`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   private_key_file

Environment:
:   Variable:
    :   [`ANSIBLE_PRIVATE_KEY_FILE`](config.md#envvar-ANSIBLE_PRIVATE_KEY_FILE)

### DEFAULT_PRIVATE_ROLE_VARS

Description:
:   Makes role variables inaccessible from other roles. This was introduced as a way to reset role variables to default values if a role is used more than once in a playbook.

Type:
:   boolean

Default:
:   `False`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   private_role_vars

Environment:
:   Variable:
    :   [`ANSIBLE_PRIVATE_ROLE_VARS`](config.md#envvar-ANSIBLE_PRIVATE_ROLE_VARS)

### DEFAULT_REMOTE_PORT

Description:
:   Port to use in remote connections, when blank it will use the connection plugin default.

Type:
:   integer

Default:
:   `None`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   remote_port

Environment:
:   Variable:
    :   [`ANSIBLE_REMOTE_PORT`](config.md#envvar-ANSIBLE_REMOTE_PORT)

### DEFAULT_REMOTE_USER

Description:
:   Sets the login user for the target machines When blank it uses the connection plugin’s default, normally the user currently executing Ansible.

Ini:
:   Section:
    :   [defaults]

    Key:
    :   remote_user

Environment:
:   Variable:
    :   [`ANSIBLE_REMOTE_USER`](config.md#envvar-ANSIBLE_REMOTE_USER)

### DEFAULT_ROLES_PATH

Description:
:   Colon separated paths in which Ansible will search for Roles.

Type:
:   pathspec

Default:
:   `{{ ANSIBLE_HOME ~ "/roles:/usr/share/ansible/roles:/etc/ansible/roles" }}`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   roles_path

Environment:
:   Variable:
    :   [`ANSIBLE_ROLES_PATH`](config.md#envvar-ANSIBLE_ROLES_PATH)

### DEFAULT_SELINUX_SPECIAL_FS

Description:
:   Some filesystems do not support safe operations and/or return inconsistent errors, this setting makes Ansible ‘tolerate’ those in the list w/o causing fatal errors. Data corruption may occur and writes are not always verified when a filesystem is in the list.

Type:
:   list

Default:
:   `fuse, nfs, vboxsf, ramfs, 9p, vfat`

Ini:
:   Section:
    :   [selinux]

    Key:
    :   special_context_filesystems

Environment:
:   Variable:
    :   [`ANSIBLE_SELINUX_SPECIAL_FS`](config.md#envvar-ANSIBLE_SELINUX_SPECIAL_FS)
        :Version Added: 2.9

### DEFAULT_STDOUT_CALLBACK

Description:
:   Set the main callback used to display Ansible output. You can only have one at a time. You can have many other callbacks, but just one can be in charge of stdout. See [Callback plugins](../plugins/callback.md#callback-plugins) for a list of available options.

Default:
:   `default`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   stdout_callback

Environment:
:   Variable:
    :   [`ANSIBLE_STDOUT_CALLBACK`](config.md#envvar-ANSIBLE_STDOUT_CALLBACK)

### DEFAULT_STRATEGY

Description:
:   Set the default strategy used for plays.

Default:
:   `linear`

Version Added:
:   2.3

Ini:
:   Section:
    :   [defaults]

    Key:
    :   strategy

Environment:
:   Variable:
    :   [`ANSIBLE_STRATEGY`](config.md#envvar-ANSIBLE_STRATEGY)

### DEFAULT_STRATEGY_PLUGIN_PATH

Description:
:   Colon separated paths in which Ansible will search for Strategy Plugins.

Type:
:   pathspec

Default:
:   `{{ ANSIBLE_HOME ~ "/plugins/strategy:/usr/share/ansible/plugins/strategy" }}`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   strategy_plugins

Environment:
:   Variable:
    :   [`ANSIBLE_STRATEGY_PLUGINS`](config.md#envvar-ANSIBLE_STRATEGY_PLUGINS)

### DEFAULT_SU

Description:
:   Toggle the use of “su” for tasks.

Type:
:   boolean

Default:
:   `False`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   su

Environment:
:   Variable:
    :   [`ANSIBLE_SU`](config.md#envvar-ANSIBLE_SU)

### DEFAULT_SYSLOG_FACILITY

Description:
:   Syslog facility to use when Ansible logs to the remote target

Default:
:   `LOG_USER`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   syslog_facility

Environment:
:   Variable:
    :   [`ANSIBLE_SYSLOG_FACILITY`](config.md#envvar-ANSIBLE_SYSLOG_FACILITY)

### DEFAULT_TERMINAL_PLUGIN_PATH

Description:
:   Colon separated paths in which Ansible will search for Terminal Plugins.

Type:
:   pathspec

Default:
:   `{{ ANSIBLE_HOME ~ "/plugins/terminal:/usr/share/ansible/plugins/terminal" }}`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   terminal_plugins

Environment:
:   Variable:
    :   [`ANSIBLE_TERMINAL_PLUGINS`](config.md#envvar-ANSIBLE_TERMINAL_PLUGINS)

### DEFAULT_TEST_PLUGIN_PATH

Description:
:   Colon separated paths in which Ansible will search for Jinja2 Test Plugins.

Type:
:   pathspec

Default:
:   `{{ ANSIBLE_HOME ~ "/plugins/test:/usr/share/ansible/plugins/test" }}`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   test_plugins

Environment:
:   Variable:
    :   [`ANSIBLE_TEST_PLUGINS`](config.md#envvar-ANSIBLE_TEST_PLUGINS)

### DEFAULT_TIMEOUT

Description:
:   This is the default timeout for connection plugins to use.

Type:
:   integer

Default:
:   `10`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   timeout

Environment:
:   Variable:
    :   [`ANSIBLE_TIMEOUT`](config.md#envvar-ANSIBLE_TIMEOUT)

### DEFAULT_TRANSPORT

Description:
:   Default connection plugin to use, the ‘smart’ option will toggle between ‘ssh’ and ‘paramiko’ depending on controller OS and ssh versions

Default:
:   `smart`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   transport

Environment:
:   Variable:
    :   [`ANSIBLE_TRANSPORT`](config.md#envvar-ANSIBLE_TRANSPORT)

### DEFAULT_UNDEFINED_VAR_BEHAVIOR

Description:
:   When True, this causes ansible templating to fail steps that reference variable names that are likely typoed. Otherwise, any ‘{{ template_expression }}’ that contains undefined variables will be rendered in a template or ansible action line exactly as written.

Type:
:   boolean

Default:
:   `True`

Version Added:
:   1.3

Ini:
:   Section:
    :   [defaults]

    Key:
    :   error_on_undefined_vars

Environment:
:   Variable:
    :   [`ANSIBLE_ERROR_ON_UNDEFINED_VARS`](config.md#envvar-ANSIBLE_ERROR_ON_UNDEFINED_VARS)

### DEFAULT_VARS_PLUGIN_PATH

Description:
:   Colon separated paths in which Ansible will search for Vars Plugins.

Type:
:   pathspec

Default:
:   `{{ ANSIBLE_HOME ~ "/plugins/vars:/usr/share/ansible/plugins/vars" }}`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   vars_plugins

Environment:
:   Variable:
    :   [`ANSIBLE_VARS_PLUGINS`](config.md#envvar-ANSIBLE_VARS_PLUGINS)

### DEFAULT_VAULT_ENCRYPT_IDENTITY

Description:
:   The vault_id to use for encrypting by default. If multiple vault_ids are provided, this specifies which to use for encryption. The –encrypt-vault-id cli option overrides the configured value.

Ini:
:   Section:
    :   [defaults]

    Key:
    :   vault_encrypt_identity

Environment:
:   Variable:
    :   [`ANSIBLE_VAULT_ENCRYPT_IDENTITY`](config.md#envvar-ANSIBLE_VAULT_ENCRYPT_IDENTITY)

### DEFAULT_VAULT_ID_MATCH

Description:
:   If true, decrypting vaults with a vault id will only try the password from the matching vault-id

Default:
:   `False`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   vault_id_match

Environment:
:   Variable:
    :   [`ANSIBLE_VAULT_ID_MATCH`](config.md#envvar-ANSIBLE_VAULT_ID_MATCH)

### DEFAULT_VAULT_IDENTITY

Description:
:   The label to use for the default vault id label in cases where a vault id label is not provided

Default:
:   `default`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   vault_identity

Environment:
:   Variable:
    :   [`ANSIBLE_VAULT_IDENTITY`](config.md#envvar-ANSIBLE_VAULT_IDENTITY)

### DEFAULT_VAULT_IDENTITY_LIST

Description:
:   A list of vault-ids to use by default. Equivalent to multiple –vault-id args. Vault-ids are tried in order.

Type:
:   list

Default:
:   `[]`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   vault_identity_list

Environment:
:   Variable:
    :   [`ANSIBLE_VAULT_IDENTITY_LIST`](config.md#envvar-ANSIBLE_VAULT_IDENTITY_LIST)

### DEFAULT_VAULT_PASSWORD_FILE

Description:
:   The vault password file to use. Equivalent to –vault-password-file or –vault-id If executable, it will be run and the resulting stdout will be used as the password.

Type:
:   path

Default:
:   `None`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   vault_password_file

Environment:
:   Variable:
    :   [`ANSIBLE_VAULT_PASSWORD_FILE`](config.md#envvar-ANSIBLE_VAULT_PASSWORD_FILE)

### DEFAULT_VERBOSITY

Description:
:   Sets the default verbosity, equivalent to the number of `-v` passed in the command line.

Type:
:   integer

Default:
:   `0`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   verbosity

Environment:
:   Variable:
    :   [`ANSIBLE_VERBOSITY`](config.md#envvar-ANSIBLE_VERBOSITY)

### DEPRECATION_WARNINGS

Description:
:   Toggle to control the showing of deprecation warnings

Type:
:   boolean

Default:
:   `True`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   deprecation_warnings

Environment:
:   Variable:
    :   [`ANSIBLE_DEPRECATION_WARNINGS`](config.md#envvar-ANSIBLE_DEPRECATION_WARNINGS)

### DEVEL_WARNING

Description:
:   Toggle to control showing warnings related to running devel

Type:
:   boolean

Default:
:   `True`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   devel_warning

Environment:
:   Variable:
    :   [`ANSIBLE_DEVEL_WARNING`](config.md#envvar-ANSIBLE_DEVEL_WARNING)

### DIFF_ALWAYS

Description:
:   Configuration toggle to tell modules to show differences when in ‘changed’ status, equivalent to `--diff`.

Type:
:   bool

Default:
:   `False`

Ini:
:   Section:
    :   [diff]

    Key:
    :   always

Environment:
:   Variable:
    :   [`ANSIBLE_DIFF_ALWAYS`](config.md#envvar-ANSIBLE_DIFF_ALWAYS)

### DIFF_CONTEXT

Description:
:   How many lines of context to show when displaying the differences between files.

Type:
:   integer

Default:
:   `3`

Ini:
:   Section:
    :   [diff]

    Key:
    :   context

Environment:
:   Variable:
    :   [`ANSIBLE_DIFF_CONTEXT`](config.md#envvar-ANSIBLE_DIFF_CONTEXT)

### DISPLAY_ARGS_TO_STDOUT

Description:
:   Normally `ansible-playbook` will print a header for each task that is run. These headers will contain the name: field from the task if you specified one. If you didn’t then `ansible-playbook` uses the task’s action to help you tell which task is presently running. Sometimes you run many of the same action and so you want more information about the task to differentiate it from others of the same action. If you set this variable to True in the config then `ansible-playbook` will also include the task’s arguments in the header. This setting defaults to False because there is a chance that you have sensitive values in your parameters and you do not want those to be printed. If you set this to True you should be sure that you have secured your environment’s stdout (no one can shoulder surf your screen and you aren’t saving stdout to an insecure file) or made sure that all of your playbooks explicitly added the `no_log: True` parameter to tasks which have sensitive values See How do I keep secret data in my playbook? for more information.

Type:
:   boolean

Default:
:   `False`

Version Added:
:   2.1

Ini:
:   Section:
    :   [defaults]

    Key:
    :   display_args_to_stdout

Environment:
:   Variable:
    :   [`ANSIBLE_DISPLAY_ARGS_TO_STDOUT`](config.md#envvar-ANSIBLE_DISPLAY_ARGS_TO_STDOUT)

### DISPLAY_SKIPPED_HOSTS

Description:
:   Toggle to control displaying skipped task/host entries in a task in the default callback

Type:
:   boolean

Default:
:   `True`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   display_skipped_hosts

Environment:
:   Variable:
    :   [`ANSIBLE_DISPLAY_SKIPPED_HOSTS`](config.md#envvar-ANSIBLE_DISPLAY_SKIPPED_HOSTS)

### DOC_FRAGMENT_PLUGIN_PATH

Description:
:   Colon separated paths in which Ansible will search for Documentation Fragments Plugins.

Type:
:   pathspec

Default:
:   `{{ ANSIBLE_HOME ~ "/plugins/doc_fragments:/usr/share/ansible/plugins/doc_fragments" }}`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   doc_fragment_plugins

Environment:
:   Variable:
    :   [`ANSIBLE_DOC_FRAGMENT_PLUGINS`](config.md#envvar-ANSIBLE_DOC_FRAGMENT_PLUGINS)

### DOCSITE_ROOT_URL

Description:
:   Root docsite URL used to generate docs URLs in warning/error text; must be an absolute URL with valid scheme and trailing slash.

Default:
:   `https://docs.ansible.com/ansible-core/`

Version Added:
:   2.8

Ini:
:   Section:
    :   [defaults]

    Key:
    :   docsite_root_url

### DUPLICATE_YAML_DICT_KEY

Description:
:   By default Ansible will issue a warning when a duplicate dict key is encountered in YAML. These warnings can be silenced by adjusting this setting to False.

Type:
:   string

Default:
:   `warn`

Choices:
:   - error:
      :   issue a ‘fatal’ error and stop the play
    - warn:
      :   issue a warning but continue
    - ignore:
      :   just continue silently

Version Added:
:   2.9

Ini:
:   Section:
    :   [defaults]

    Key:
    :   duplicate_dict_key

Environment:
:   Variable:
    :   [`ANSIBLE_DUPLICATE_YAML_DICT_KEY`](config.md#envvar-ANSIBLE_DUPLICATE_YAML_DICT_KEY)

### EDITOR

Default:
:   `vi`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   editor
        :Version Added: 2.15

Environment:
:   - Variable:
      :   [`ANSIBLE_EDITOR`](config.md#envvar-ANSIBLE_EDITOR)

      Version Added:
      :   2.15
    - Variable:
      :   [`EDITOR`](config.md#envvar-EDITOR)

### ENABLE_TASK_DEBUGGER

Description:
:   Whether or not to enable the task debugger, this previously was done as a strategy plugin. Now all strategy plugins can inherit this behavior. The debugger defaults to activating when a task is failed on unreachable. Use the debugger keyword for more flexibility.

Type:
:   boolean

Default:
:   `False`

Version Added:
:   2.5

Ini:
:   Section:
    :   [defaults]

    Key:
    :   enable_task_debugger

Environment:
:   Variable:
    :   [`ANSIBLE_ENABLE_TASK_DEBUGGER`](config.md#envvar-ANSIBLE_ENABLE_TASK_DEBUGGER)

### ERROR_ON_MISSING_HANDLER

Description:
:   Toggle to allow missing handlers to become a warning instead of an error when notifying.

Type:
:   boolean

Default:
:   `True`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   error_on_missing_handler

Environment:
:   Variable:
    :   [`ANSIBLE_ERROR_ON_MISSING_HANDLER`](config.md#envvar-ANSIBLE_ERROR_ON_MISSING_HANDLER)

### FACTS_MODULES

Description:
:   Which modules to run during a play’s fact gathering stage, using the default of ‘smart’ will try to figure it out based on connection type. If adding your own modules but you still want to use the default Ansible facts, you will want to include ‘setup’ or corresponding network module to the list (if you add ‘smart’, Ansible will also figure it out). This does not affect explicit calls to the ‘setup’ module, but does always affect the ‘gather_facts’ action (implicit or explicit).

Type:
:   list

Default:
:   `['smart']`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   facts_modules

Environment:
:   Variable:
    :   [`ANSIBLE_FACTS_MODULES`](config.md#envvar-ANSIBLE_FACTS_MODULES)

Variables:
:   name:
    :   ansible_facts_modules

### GALAXY_CACHE_DIR

Description:
:   The directory that stores cached responses from a Galaxy server. This is only used by the `ansible-galaxy collection install` and `download` commands. Cache files inside this dir will be ignored if they are world writable.

Type:
:   path

Default:
:   `{{ ANSIBLE_HOME ~ "/galaxy_cache" }}`

Version Added:
:   2.11

Ini:
:   Section:
    :   [galaxy]

    Key:
    :   cache_dir

Environment:
:   Variable:
    :   [`ANSIBLE_GALAXY_CACHE_DIR`](config.md#envvar-ANSIBLE_GALAXY_CACHE_DIR)

### GALAXY_COLLECTION_SKELETON

Description:
:   Collection skeleton directory to use as a template for the `init` action in `ansible-galaxy collection`, same as `--collection-skeleton`.

Type:
:   path

Ini:
:   Section:
    :   [galaxy]

    Key:
    :   collection_skeleton

Environment:
:   Variable:
    :   [`ANSIBLE_GALAXY_COLLECTION_SKELETON`](config.md#envvar-ANSIBLE_GALAXY_COLLECTION_SKELETON)

### GALAXY_COLLECTION_SKELETON_IGNORE

Description:
:   patterns of files to ignore inside a Galaxy collection skeleton directory

Type:
:   list

Default:
:   `['^.git$', '^.*/.git_keep$']`

Ini:
:   Section:
    :   [galaxy]

    Key:
    :   collection_skeleton_ignore

Environment:
:   Variable:
    :   [`ANSIBLE_GALAXY_COLLECTION_SKELETON_IGNORE`](config.md#envvar-ANSIBLE_GALAXY_COLLECTION_SKELETON_IGNORE)

### GALAXY_DISABLE_GPG_VERIFY

Description:
:   Disable GPG signature verification during collection installation.

Type:
:   bool

Default:
:   `False`

Version Added:
:   2.13

Ini:
:   Section:
    :   [galaxy]

    Key:
    :   disable_gpg_verify

Environment:
:   Variable:
    :   [`ANSIBLE_GALAXY_DISABLE_GPG_VERIFY`](config.md#envvar-ANSIBLE_GALAXY_DISABLE_GPG_VERIFY)

### GALAXY_DISPLAY_PROGRESS

Description:
:   Some steps in `ansible-galaxy` display a progress wheel which can cause issues on certain displays or when outputting the stdout to a file. This config option controls whether the display wheel is shown or not. The default is to show the display wheel if stdout has a tty.

Type:
:   bool

Default:
:   `None`

Version Added:
:   2.10

Ini:
:   Section:
    :   [galaxy]

    Key:
    :   display_progress

Environment:
:   Variable:
    :   [`ANSIBLE_GALAXY_DISPLAY_PROGRESS`](config.md#envvar-ANSIBLE_GALAXY_DISPLAY_PROGRESS)

### GALAXY_GPG_KEYRING

Description:
:   Configure the keyring used for GPG signature verification during collection installation and verification.

Type:
:   path

Version Added:
:   2.13

Ini:
:   Section:
    :   [galaxy]

    Key:
    :   gpg_keyring

Environment:
:   Variable:
    :   [`ANSIBLE_GALAXY_GPG_KEYRING`](config.md#envvar-ANSIBLE_GALAXY_GPG_KEYRING)

### GALAXY_IGNORE_CERTS

Description:
:   If set to yes, ansible-galaxy will not validate TLS certificates. This can be useful for testing against a server with a self-signed certificate.

Type:
:   boolean

Ini:
:   Section:
    :   [galaxy]

    Key:
    :   ignore_certs

Environment:
:   Variable:
    :   [`ANSIBLE_GALAXY_IGNORE`](config.md#envvar-ANSIBLE_GALAXY_IGNORE)

### GALAXY_IGNORE_INVALID_SIGNATURE_STATUS_CODES

Description:
:   A list of GPG status codes to ignore during GPG signature verification. See L(<https://github.com/gpg/gnupg/blob/master/doc/DETAILS#general-status-codes>) for status code descriptions. If fewer signatures successfully verify the collection than GALAXY_REQUIRED_VALID_SIGNATURE_COUNT, signature verification will fail even if all error codes are ignored.

Type:
:   list

Choices:
:   - EXPSIG
    - EXPKEYSIG
    - REVKEYSIG
    - BADSIG
    - ERRSIG
    - NO_PUBKEY
    - MISSING_PASSPHRASE
    - BAD_PASSPHRASE
    - NODATA
    - UNEXPECTED
    - ERROR
    - FAILURE
    - BADARMOR
    - KEYEXPIRED
    - KEYREVOKED
    - NO_SECKEY

Ini:
:   Section:
    :   [galaxy]

    Key:
    :   ignore_signature_status_codes

Environment:
:   Variable:
    :   [`ANSIBLE_GALAXY_IGNORE_SIGNATURE_STATUS_CODES`](config.md#envvar-ANSIBLE_GALAXY_IGNORE_SIGNATURE_STATUS_CODES)

### GALAXY_REQUIRED_VALID_SIGNATURE_COUNT

Description:
:   The number of signatures that must be successful during GPG signature verification while installing or verifying collections. This should be a positive integer or all to indicate all signatures must successfully validate the collection. Prepend + to the value to fail if no valid signatures are found for the collection.

Type:
:   str

Default:
:   `1`

Ini:
:   Section:
    :   [galaxy]

    Key:
    :   required_valid_signature_count

Environment:
:   Variable:
    :   [`ANSIBLE_GALAXY_REQUIRED_VALID_SIGNATURE_COUNT`](config.md#envvar-ANSIBLE_GALAXY_REQUIRED_VALID_SIGNATURE_COUNT)

### GALAXY_ROLE_SKELETON

Description:
:   Role skeleton directory to use as a template for the `init` action in `ansible-galaxy`/`ansible-galaxy role`, same as `--role-skeleton`.

Type:
:   path

Ini:
:   Section:
    :   [galaxy]

    Key:
    :   role_skeleton

Environment:
:   Variable:
    :   [`ANSIBLE_GALAXY_ROLE_SKELETON`](config.md#envvar-ANSIBLE_GALAXY_ROLE_SKELETON)

### GALAXY_ROLE_SKELETON_IGNORE

Description:
:   patterns of files to ignore inside a Galaxy role or collection skeleton directory

Type:
:   list

Default:
:   `['^.git$', '^.*/.git_keep$']`

Ini:
:   Section:
    :   [galaxy]

    Key:
    :   role_skeleton_ignore

Environment:
:   Variable:
    :   [`ANSIBLE_GALAXY_ROLE_SKELETON_IGNORE`](config.md#envvar-ANSIBLE_GALAXY_ROLE_SKELETON_IGNORE)

### GALAXY_SERVER

Description:
:   URL to prepend when roles don’t specify the full URI, assume they are referencing this server as the source.

Default:
:   `https://galaxy.ansible.com`

Ini:
:   Section:
    :   [galaxy]

    Key:
    :   server

Environment:
:   Variable:
    :   [`ANSIBLE_GALAXY_SERVER`](config.md#envvar-ANSIBLE_GALAXY_SERVER)

### GALAXY_SERVER_LIST

Description:
:   A list of Galaxy servers to use when installing a collection. The value corresponds to the config ini header `[galaxy_server.{{item}}]` which defines the server details. See [Configuring the ansible-galaxy client](../collections_guide/collections_installing.md#galaxy-server-config) for more details on how to define a Galaxy server. The order of servers in this list is used to as the order in which a collection is resolved. Setting this config option will ignore the [GALAXY_SERVER](config.md#galaxy-server) config option.

Type:
:   list

Version Added:
:   2.9

Ini:
:   Section:
    :   [galaxy]

    Key:
    :   server_list

Environment:
:   Variable:
    :   [`ANSIBLE_GALAXY_SERVER_LIST`](config.md#envvar-ANSIBLE_GALAXY_SERVER_LIST)

### GALAXY_TOKEN_PATH

Description:
:   Local path to galaxy access token file

Type:
:   path

Default:
:   `{{ ANSIBLE_HOME ~ "/galaxy_token" }}`

Version Added:
:   2.9

Ini:
:   Section:
    :   [galaxy]

    Key:
    :   token_path

Environment:
:   Variable:
    :   [`ANSIBLE_GALAXY_TOKEN_PATH`](config.md#envvar-ANSIBLE_GALAXY_TOKEN_PATH)

### HOST_KEY_CHECKING

Description:
:   Set this to “False” if you want to avoid host key checking by the underlying tools Ansible uses to connect to the host

Type:
:   boolean

Default:
:   `True`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   host_key_checking

Environment:
:   Variable:
    :   [`ANSIBLE_HOST_KEY_CHECKING`](config.md#envvar-ANSIBLE_HOST_KEY_CHECKING)

### HOST_PATTERN_MISMATCH

Description:
:   This setting changes the behaviour of mismatched host patterns, it allows you to force a fatal error, a warning or just ignore it

Default:
:   `warning`

Choices:
:   - error:
      :   issue a ‘fatal’ error and stop the play
    - warning:
      :   issue a warning but continue
    - ignore:
      :   just continue silently

Version Added:
:   2.8

Ini:
:   Section:
    :   [inventory]

    Key:
    :   host_pattern_mismatch

Environment:
:   Variable:
    :   [`ANSIBLE_HOST_PATTERN_MISMATCH`](config.md#envvar-ANSIBLE_HOST_PATTERN_MISMATCH)

### INJECT_FACTS_AS_VARS

Description:
:   Facts are available inside the ansible_facts variable, this setting also pushes them as their own vars in the main namespace. Unlike inside the ansible_facts dictionary, these will have an ansible_ prefix.

Type:
:   boolean

Default:
:   `True`

Version Added:
:   2.5

Ini:
:   Section:
    :   [defaults]

    Key:
    :   inject_facts_as_vars

Environment:
:   Variable:
    :   [`ANSIBLE_INJECT_FACT_VARS`](config.md#envvar-ANSIBLE_INJECT_FACT_VARS)

### INTERPRETER_PYTHON

Description:
:   Path to the Python interpreter to be used for module execution on remote targets, or an automatic discovery mode. Supported discovery modes are `auto` (the default), `auto_silent`, `auto_legacy`, and `auto_legacy_silent`. All discovery modes employ a lookup table to use the included system Python (on distributions known to include one), falling back to a fixed ordered list of well-known Python interpreter locations if a platform-specific default is not available. The fallback behavior will issue a warning that the interpreter should be set explicitly (since interpreters installed later may change which one is used). This warning behavior can be disabled by setting `auto_silent` or `auto_legacy_silent`. The value of `auto_legacy` provides all the same behavior, but for backwards-compatibility with older Ansible releases that always defaulted to `/usr/bin/python`, will use that interpreter if present.

Default:
:   `auto`

Version Added:
:   2.8

Ini:
:   Section:
    :   [defaults]

    Key:
    :   interpreter_python

Environment:
:   Variable:
    :   [`ANSIBLE_PYTHON_INTERPRETER`](config.md#envvar-ANSIBLE_PYTHON_INTERPRETER)

Variables:
:   name:
    :   ansible_python_interpreter

### INTERPRETER_PYTHON_FALLBACK

Type:
:   list

Default:
:   `['python3.11', 'python3.10', 'python3.9', 'python3.8', 'python3.7', 'python3.6', 'python3.5', '/usr/bin/python3', '/usr/libexec/platform-python', 'python2.7', '/usr/bin/python', 'python']`

Version Added:
:   2.8

Variables:
:   name:
    :   ansible_interpreter_python_fallback

### INVALID_TASK_ATTRIBUTE_FAILED

Description:
:   If ‘false’, invalid attributes for a task will result in warnings instead of errors

Type:
:   boolean

Default:
:   `True`

Version Added:
:   2.7

Ini:
:   Section:
    :   [defaults]

    Key:
    :   invalid_task_attribute_failed

Environment:
:   Variable:
    :   [`ANSIBLE_INVALID_TASK_ATTRIBUTE_FAILED`](config.md#envvar-ANSIBLE_INVALID_TASK_ATTRIBUTE_FAILED)

### INVENTORY_ANY_UNPARSED_IS_FAILED

Description:
:   If ‘true’, it is a fatal error when any given inventory source cannot be successfully parsed by any available inventory plugin; otherwise, this situation only attracts a warning.

Type:
:   boolean

Default:
:   `False`

Version Added:
:   2.7

Ini:
:   Section:
    :   [inventory]

    Key:
    :   any_unparsed_is_failed

Environment:
:   Variable:
    :   [`ANSIBLE_INVENTORY_ANY_UNPARSED_IS_FAILED`](config.md#envvar-ANSIBLE_INVENTORY_ANY_UNPARSED_IS_FAILED)

### INVENTORY_CACHE_ENABLED

Description:
:   Toggle to turn on inventory caching. This setting has been moved to the individual inventory plugins as a plugin option [Inventory plugins](../plugins/inventory.md#inventory-plugins). The existing configuration settings are still accepted with the inventory plugin adding additional options from inventory configuration. This message will be removed in 2.16.

Type:
:   bool

Default:
:   `False`

Ini:
:   Section:
    :   [inventory]

    Key:
    :   cache

Environment:
:   Variable:
    :   [`ANSIBLE_INVENTORY_CACHE`](config.md#envvar-ANSIBLE_INVENTORY_CACHE)

### INVENTORY_CACHE_PLUGIN

Description:
:   The plugin for caching inventory. This setting has been moved to the individual inventory plugins as a plugin option [Inventory plugins](../plugins/inventory.md#inventory-plugins). The existing configuration settings are still accepted with the inventory plugin adding additional options from inventory and fact cache configuration. This message will be removed in 2.16.

Ini:
:   Section:
    :   [inventory]

    Key:
    :   cache_plugin

Environment:
:   Variable:
    :   [`ANSIBLE_INVENTORY_CACHE_PLUGIN`](config.md#envvar-ANSIBLE_INVENTORY_CACHE_PLUGIN)

### INVENTORY_CACHE_PLUGIN_CONNECTION

Description:
:   The inventory cache connection. This setting has been moved to the individual inventory plugins as a plugin option [Inventory plugins](../plugins/inventory.md#inventory-plugins). The existing configuration settings are still accepted with the inventory plugin adding additional options from inventory and fact cache configuration. This message will be removed in 2.16.

Ini:
:   Section:
    :   [inventory]

    Key:
    :   cache_connection

Environment:
:   Variable:
    :   [`ANSIBLE_INVENTORY_CACHE_CONNECTION`](config.md#envvar-ANSIBLE_INVENTORY_CACHE_CONNECTION)

### INVENTORY_CACHE_PLUGIN_PREFIX

Description:
:   The table prefix for the cache plugin. This setting has been moved to the individual inventory plugins as a plugin option [Inventory plugins](../plugins/inventory.md#inventory-plugins). The existing configuration settings are still accepted with the inventory plugin adding additional options from inventory and fact cache configuration. This message will be removed in 2.16.

Default:
:   `ansible_inventory_`

Ini:
:   Section:
    :   [inventory]

    Key:
    :   cache_prefix

Environment:
:   Variable:
    :   [`ANSIBLE_INVENTORY_CACHE_PLUGIN_PREFIX`](config.md#envvar-ANSIBLE_INVENTORY_CACHE_PLUGIN_PREFIX)

### INVENTORY_CACHE_TIMEOUT

Description:
:   Expiration timeout for the inventory cache plugin data. This setting has been moved to the individual inventory plugins as a plugin option [Inventory plugins](../plugins/inventory.md#inventory-plugins). The existing configuration settings are still accepted with the inventory plugin adding additional options from inventory and fact cache configuration. This message will be removed in 2.16.

Default:
:   `3600`

Ini:
:   Section:
    :   [inventory]

    Key:
    :   cache_timeout

Environment:
:   Variable:
    :   [`ANSIBLE_INVENTORY_CACHE_TIMEOUT`](config.md#envvar-ANSIBLE_INVENTORY_CACHE_TIMEOUT)

### INVENTORY_ENABLED

Description:
:   List of enabled inventory plugins, it also determines the order in which they are used.

Type:
:   list

Default:
:   `['host_list', 'script', 'auto', 'yaml', 'ini', 'toml']`

Ini:
:   Section:
    :   [inventory]

    Key:
    :   enable_plugins

Environment:
:   Variable:
    :   [`ANSIBLE_INVENTORY_ENABLED`](config.md#envvar-ANSIBLE_INVENTORY_ENABLED)

### INVENTORY_EXPORT

Description:
:   Controls if ansible-inventory will accurately reflect Ansible’s view into inventory or its optimized for exporting.

Type:
:   bool

Default:
:   `False`

Ini:
:   Section:
    :   [inventory]

    Key:
    :   export

Environment:
:   Variable:
    :   [`ANSIBLE_INVENTORY_EXPORT`](config.md#envvar-ANSIBLE_INVENTORY_EXPORT)

### INVENTORY_IGNORE_EXTS

Description:
:   List of extensions to ignore when using a directory as an inventory source

Type:
:   list

Default:
:   `{{(REJECT_EXTS + ('.orig', '.ini', '.cfg', '.retry'))}}`

Ini:
:   - Section:
      :   [defaults]

      Key:
      :   inventory_ignore_extensions
    - Section:
      :   [inventory]

      Key:
      :   ignore_extensions

Environment:
:   Variable:
    :   [`ANSIBLE_INVENTORY_IGNORE`](config.md#envvar-ANSIBLE_INVENTORY_IGNORE)

### INVENTORY_IGNORE_PATTERNS

Description:
:   List of patterns to ignore when using a directory as an inventory source

Type:
:   list

Default:
:   `[]`

Ini:
:   - Section:
      :   [defaults]

      Key:
      :   inventory_ignore_patterns
    - Section:
      :   [inventory]

      Key:
      :   ignore_patterns

Environment:
:   Variable:
    :   [`ANSIBLE_INVENTORY_IGNORE_REGEX`](config.md#envvar-ANSIBLE_INVENTORY_IGNORE_REGEX)

### INVENTORY_UNPARSED_IS_FAILED

Description:
:   If ‘true’ it is a fatal error if every single potential inventory source fails to parse, otherwise this situation will only attract a warning.

Type:
:   bool

Default:
:   `False`

Ini:
:   Section:
    :   [inventory]

    Key:
    :   unparsed_is_failed

Environment:
:   Variable:
    :   [`ANSIBLE_INVENTORY_UNPARSED_FAILED`](config.md#envvar-ANSIBLE_INVENTORY_UNPARSED_FAILED)

### INVENTORY_UNPARSED_WARNING

Description:
:   By default Ansible will issue a warning when no inventory was loaded and notes that it will use an implicit localhost-only inventory. These warnings can be silenced by adjusting this setting to False.

Type:
:   boolean

Default:
:   `True`

Version Added:
:   2.14

Ini:
:   Section:
    :   [inventory]

    Key:
    :   inventory_unparsed_warning

Environment:
:   Variable:
    :   [`ANSIBLE_INVENTORY_UNPARSED_WARNING`](config.md#envvar-ANSIBLE_INVENTORY_UNPARSED_WARNING)

### JINJA2_NATIVE_WARNING

Description:
:   Toggle to control showing warnings related to running a Jinja version older than required for jinja2_native

Type:
:   boolean

Default:
:   `True`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   jinja2_native_warning

Environment:
:   Variable:
    :   [`ANSIBLE_JINJA2_NATIVE_WARNING`](config.md#envvar-ANSIBLE_JINJA2_NATIVE_WARNING)
        :Deprecated in: 2.17
        :Deprecated detail: This option is no longer used in the Ansible Core code base.

### LOCALHOST_WARNING

Description:
:   By default Ansible will issue a warning when there are no hosts in the inventory. These warnings can be silenced by adjusting this setting to False.

Type:
:   boolean

Default:
:   `True`

Version Added:
:   2.6

Ini:
:   Section:
    :   [defaults]

    Key:
    :   localhost_warning

Environment:
:   Variable:
    :   [`ANSIBLE_LOCALHOST_WARNING`](config.md#envvar-ANSIBLE_LOCALHOST_WARNING)

### MAX_FILE_SIZE_FOR_DIFF

Description:
:   Maximum size of files to be considered for diff display

Type:
:   int

Default:
:   `104448`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   max_diff_size

Environment:
:   Variable:
    :   [`ANSIBLE_MAX_DIFF_SIZE`](config.md#envvar-ANSIBLE_MAX_DIFF_SIZE)

### MODULE_IGNORE_EXTS

Description:
:   List of extensions to ignore when looking for modules to load This is for rejecting script and binary module fallback extensions

Type:
:   list

Default:
:   `{{(REJECT_EXTS + ('.yaml', '.yml', '.ini'))}}`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   module_ignore_exts

Environment:
:   Variable:
    :   [`ANSIBLE_MODULE_IGNORE_EXTS`](config.md#envvar-ANSIBLE_MODULE_IGNORE_EXTS)

### MODULE_STRICT_UTF8_RESPONSE

Description:
:   Enables whether module responses are evaluated for containing non UTF-8 data Disabling this may result in unexpected behavior Only ansible-core should evaluate this configuration

Type:
:   bool

Default:
:   `True`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   module_strict_utf8_response

Environment:
:   Variable:
    :   [`ANSIBLE_MODULE_STRICT_UTF8_RESPONSE`](config.md#envvar-ANSIBLE_MODULE_STRICT_UTF8_RESPONSE)

### NETCONF_SSH_CONFIG

Description:
:   This variable is used to enable bastion/jump host with netconf connection. If set to True the bastion/jump host ssh settings should be present in ~/.ssh/config file, alternatively it can be set to custom ssh configuration file path to read the bastion/jump host settings.

Default:
:   `None`

Ini:
:   Section:
    :   [netconf_connection]

    Key:
    :   ssh_config

Environment:
:   Variable:
    :   [`ANSIBLE_NETCONF_SSH_CONFIG`](config.md#envvar-ANSIBLE_NETCONF_SSH_CONFIG)

### NETWORK_GROUP_MODULES

Type:
:   list

Default:
:   `['eos', 'nxos', 'ios', 'iosxr', 'junos', 'enos', 'ce', 'vyos', 'sros', 'dellos9', 'dellos10', 'dellos6', 'asa', 'aruba', 'aireos', 'bigip', 'ironware', 'onyx', 'netconf', 'exos', 'voss', 'slxos']`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   network_group_modules

Environment:
:   Variable:
    :   [`ANSIBLE_NETWORK_GROUP_MODULES`](config.md#envvar-ANSIBLE_NETWORK_GROUP_MODULES)

### OLD_PLUGIN_CACHE_CLEARING

Description:
:   Previously Ansible would only clear some of the plugin loading caches when loading new roles, this led to some behaviours in which a plugin loaded in previous plays would be unexpectedly ‘sticky’. This setting allows to return to that behaviour.

Type:
:   boolean

Default:
:   `False`

Version Added:
:   2.8

Ini:
:   Section:
    :   [defaults]

    Key:
    :   old_plugin_cache_clear

Environment:
:   Variable:
    :   [`ANSIBLE_OLD_PLUGIN_CACHE_CLEAR`](config.md#envvar-ANSIBLE_OLD_PLUGIN_CACHE_CLEAR)

### PAGER

Default:
:   `less`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   pager
        :Version Added: 2.15

Environment:
:   - Variable:
      :   [`ANSIBLE_PAGER`](config.md#envvar-ANSIBLE_PAGER)

      Version Added:
      :   2.15
    - Variable:
      :   [`PAGER`](config.md#envvar-PAGER)

### PARAMIKO_HOST_KEY_AUTO_ADD

Type:
:   boolean

Default:
:   `False`

Ini:
:   Section:
    :   [paramiko_connection]

    Key:
    :   host_key_auto_add

Environment:
:   Variable:
    :   [`ANSIBLE_PARAMIKO_HOST_KEY_AUTO_ADD`](config.md#envvar-ANSIBLE_PARAMIKO_HOST_KEY_AUTO_ADD)

### PARAMIKO_LOOK_FOR_KEYS

Type:
:   boolean

Default:
:   `True`

Ini:
:   Section:
    :   [paramiko_connection]

    Key:
    :   look_for_keys

Environment:
:   Variable:
    :   [`ANSIBLE_PARAMIKO_LOOK_FOR_KEYS`](config.md#envvar-ANSIBLE_PARAMIKO_LOOK_FOR_KEYS)

### PERSISTENT_COMMAND_TIMEOUT

Description:
:   This controls the amount of time to wait for response from remote device before timing out persistent connection.

Type:
:   int

Default:
:   `30`

Ini:
:   Section:
    :   [persistent_connection]

    Key:
    :   command_timeout

Environment:
:   Variable:
    :   [`ANSIBLE_PERSISTENT_COMMAND_TIMEOUT`](config.md#envvar-ANSIBLE_PERSISTENT_COMMAND_TIMEOUT)

### PERSISTENT_CONNECT_RETRY_TIMEOUT

Description:
:   This controls the retry timeout for persistent connection to connect to the local domain socket.

Type:
:   integer

Default:
:   `15`

Ini:
:   Section:
    :   [persistent_connection]

    Key:
    :   connect_retry_timeout

Environment:
:   Variable:
    :   [`ANSIBLE_PERSISTENT_CONNECT_RETRY_TIMEOUT`](config.md#envvar-ANSIBLE_PERSISTENT_CONNECT_RETRY_TIMEOUT)

### PERSISTENT_CONNECT_TIMEOUT

Description:
:   This controls how long the persistent connection will remain idle before it is destroyed.

Type:
:   integer

Default:
:   `30`

Ini:
:   Section:
    :   [persistent_connection]

    Key:
    :   connect_timeout

Environment:
:   Variable:
    :   [`ANSIBLE_PERSISTENT_CONNECT_TIMEOUT`](config.md#envvar-ANSIBLE_PERSISTENT_CONNECT_TIMEOUT)

### PERSISTENT_CONTROL_PATH_DIR

Description:
:   Path to socket to be used by the connection persistence system.

Type:
:   path

Default:
:   `{{ ANSIBLE_HOME ~ "/pc" }}`

Ini:
:   Section:
    :   [persistent_connection]

    Key:
    :   control_path_dir

Environment:
:   Variable:
    :   [`ANSIBLE_PERSISTENT_CONTROL_PATH_DIR`](config.md#envvar-ANSIBLE_PERSISTENT_CONTROL_PATH_DIR)

### PLAYBOOK_DIR

Description:
:   A number of non-playbook CLIs have a `--playbook-dir` argument; this sets the default value for it.

Type:
:   path

Version Added:
:   2.9

Ini:
:   Section:
    :   [defaults]

    Key:
    :   playbook_dir

Environment:
:   Variable:
    :   [`ANSIBLE_PLAYBOOK_DIR`](config.md#envvar-ANSIBLE_PLAYBOOK_DIR)

### PLAYBOOK_VARS_ROOT

Description:
:   This sets which playbook dirs will be used as a root to process vars plugins, which includes finding host_vars/group_vars

Default:
:   `top`

Choices:
:   - top:
      :   follows the traditional behavior of using the top playbook in the chain to find the root directory.
    - bottom:
      :   follows the 2.4.0 behavior of using the current playbook to find the root directory.
    - all:
      :   examines from the first parent to the current playbook.

Version Added:
:   2.4.1

Ini:
:   Section:
    :   [defaults]

    Key:
    :   playbook_vars_root

Environment:
:   Variable:
    :   [`ANSIBLE_PLAYBOOK_VARS_ROOT`](config.md#envvar-ANSIBLE_PLAYBOOK_VARS_ROOT)

### PLUGIN_FILTERS_CFG

Description:
:   A path to configuration for filtering which plugins installed on the system are allowed to be used. See [Rejecting modules](../module_plugin_guide/plugin_filtering_config.md#plugin-filtering-config) for details of the filter file’s format. The default is /etc/ansible/plugin_filters.yml

Type:
:   path

Default:
:   `None`

Version Added:
:   2.5.0

Ini:
:   Section:
    :   [defaults]

    Key:
    :   plugin_filters_cfg

### PYTHON_MODULE_RLIMIT_NOFILE

Description:
:   Attempts to set RLIMIT_NOFILE soft limit to the specified value when executing Python modules (can speed up subprocess usage on Python 2.x. See <https://bugs.python.org/issue11284>). The value will be limited by the existing hard limit. Default value of 0 does not attempt to adjust existing system-defined limits.

Default:
:   `0`

Version Added:
:   2.8

Ini:
:   Section:
    :   [defaults]

    Key:
    :   python_module_rlimit_nofile

Environment:
:   Variable:
    :   [`ANSIBLE_PYTHON_MODULE_RLIMIT_NOFILE`](config.md#envvar-ANSIBLE_PYTHON_MODULE_RLIMIT_NOFILE)

Variables:
:   name:
    :   ansible_python_module_rlimit_nofile

### RETRY_FILES_ENABLED

Description:
:   This controls whether a failed Ansible playbook should create a .retry file.

Type:
:   bool

Default:
:   `False`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   retry_files_enabled

Environment:
:   Variable:
    :   [`ANSIBLE_RETRY_FILES_ENABLED`](config.md#envvar-ANSIBLE_RETRY_FILES_ENABLED)

### RETRY_FILES_SAVE_PATH

Description:
:   This sets the path in which Ansible will save .retry files when a playbook fails and retry files are enabled. This file will be overwritten after each run with the list of failed hosts from all plays.

Type:
:   path

Default:
:   `None`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   retry_files_save_path

Environment:
:   Variable:
    :   [`ANSIBLE_RETRY_FILES_SAVE_PATH`](config.md#envvar-ANSIBLE_RETRY_FILES_SAVE_PATH)

### RUN_VARS_PLUGINS

Description:
:   This setting can be used to optimize vars_plugin usage depending on user’s inventory size and play selection.

Type:
:   str

Default:
:   `demand`

Choices:
:   - demand:
      :   will run vars_plugins relative to inventory sources anytime vars are ‘demanded’ by tasks.
    - start:
      :   will run vars_plugins relative to inventory sources after importing that inventory source.

Version Added:
:   2.10

Ini:
:   Section:
    :   [defaults]

    Key:
    :   run_vars_plugins

Environment:
:   Variable:
    :   [`ANSIBLE_RUN_VARS_PLUGINS`](config.md#envvar-ANSIBLE_RUN_VARS_PLUGINS)

### SHOW_CUSTOM_STATS

Description:
:   This adds the custom stats set via the set_stats plugin to the default output

Type:
:   bool

Default:
:   `False`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   show_custom_stats

Environment:
:   Variable:
    :   [`ANSIBLE_SHOW_CUSTOM_STATS`](config.md#envvar-ANSIBLE_SHOW_CUSTOM_STATS)

### STRING_CONVERSION_ACTION

Description:
:   Action to take when a module parameter value is converted to a string (this does not affect variables). For string parameters, values such as ‘1.00’, “[‘a’, ‘b’,]”, and ‘yes’, ‘y’, etc. will be converted by the YAML parser unless fully quoted. Valid options are ‘error’, ‘warn’, and ‘ignore’. Since 2.8, this option defaults to ‘warn’ but will change to ‘error’ in 2.12.

Type:
:   string

Default:
:   `warn`

Version Added:
:   2.8

Ini:
:   Section:
    :   [defaults]

    Key:
    :   string_conversion_action

Environment:
:   Variable:
    :   [`ANSIBLE_STRING_CONVERSION_ACTION`](config.md#envvar-ANSIBLE_STRING_CONVERSION_ACTION)

### STRING_TYPE_FILTERS

Description:
:   This list of filters avoids ‘type conversion’ when templating variables Useful when you want to avoid conversion into lists or dictionaries for JSON strings, for example.

Type:
:   list

Default:
:   `['string', 'to_json', 'to_nice_json', 'to_yaml', 'to_nice_yaml', 'ppretty', 'json']`

Ini:
:   Section:
    :   [jinja2]

    Key:
    :   dont_type_filters

Environment:
:   Variable:
    :   [`ANSIBLE_STRING_TYPE_FILTERS`](config.md#envvar-ANSIBLE_STRING_TYPE_FILTERS)

### SYSTEM_WARNINGS

Description:
:   Allows disabling of warnings related to potential issues on the system running ansible itself (not on the managed hosts) These may include warnings about 3rd party packages or other conditions that should be resolved if possible.

Type:
:   boolean

Default:
:   `True`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   system_warnings

Environment:
:   Variable:
    :   [`ANSIBLE_SYSTEM_WARNINGS`](config.md#envvar-ANSIBLE_SYSTEM_WARNINGS)

### TAGS_RUN

Description:
:   default list of tags to run in your plays, Skip Tags has precedence.

Type:
:   list

Default:
:   `[]`

Version Added:
:   2.5

Ini:
:   Section:
    :   [tags]

    Key:
    :   run

Environment:
:   Variable:
    :   [`ANSIBLE_RUN_TAGS`](config.md#envvar-ANSIBLE_RUN_TAGS)

### TAGS_SKIP

Description:
:   default list of tags to skip in your plays, has precedence over Run Tags

Type:
:   list

Default:
:   `[]`

Version Added:
:   2.5

Ini:
:   Section:
    :   [tags]

    Key:
    :   skip

Environment:
:   Variable:
    :   [`ANSIBLE_SKIP_TAGS`](config.md#envvar-ANSIBLE_SKIP_TAGS)

### TASK_DEBUGGER_IGNORE_ERRORS

Description:
:   This option defines whether the task debugger will be invoked on a failed task when ignore_errors=True is specified. True specifies that the debugger will honor ignore_errors, False will not honor ignore_errors.

Type:
:   boolean

Default:
:   `True`

Version Added:
:   2.7

Ini:
:   Section:
    :   [defaults]

    Key:
    :   task_debugger_ignore_errors

Environment:
:   Variable:
    :   [`ANSIBLE_TASK_DEBUGGER_IGNORE_ERRORS`](config.md#envvar-ANSIBLE_TASK_DEBUGGER_IGNORE_ERRORS)

### TASK_TIMEOUT

Description:
:   Set the maximum time (in seconds) that a task can run for. If set to 0 (the default) there is no timeout.

Type:
:   integer

Default:
:   `0`

Version Added:
:   2.10

Ini:
:   Section:
    :   [defaults]

    Key:
    :   task_timeout

Environment:
:   Variable:
    :   [`ANSIBLE_TASK_TIMEOUT`](config.md#envvar-ANSIBLE_TASK_TIMEOUT)

### TRANSFORM_INVALID_GROUP_CHARS

Description:
:   Make ansible transform invalid characters in group names supplied by inventory sources.

Type:
:   string

Default:
:   `never`

Choices:
:   - always:
      :   it will replace any invalid characters with ‘_’ (underscore) and warn the user
    - never:
      :   it will allow for the group name but warn about the issue
    - ignore:
      :   it does the same as ‘never’, without issuing a warning
    - silently:
      :   it does the same as ‘always’, without issuing a warning

Version Added:
:   2.8

Ini:
:   Section:
    :   [defaults]

    Key:
    :   force_valid_group_names

Environment:
:   Variable:
    :   [`ANSIBLE_TRANSFORM_INVALID_GROUP_CHARS`](config.md#envvar-ANSIBLE_TRANSFORM_INVALID_GROUP_CHARS)

### USE_PERSISTENT_CONNECTIONS

Description:
:   Toggles the use of persistence for connections.

Type:
:   boolean

Default:
:   `False`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   use_persistent_connections

Environment:
:   Variable:
    :   [`ANSIBLE_USE_PERSISTENT_CONNECTIONS`](config.md#envvar-ANSIBLE_USE_PERSISTENT_CONNECTIONS)

### VALIDATE_ACTION_GROUP_METADATA

Description:
:   A toggle to disable validating a collection’s ‘metadata’ entry for a module_defaults action group. Metadata containing unexpected fields or value types will produce a warning when this is True.

Type:
:   bool

Default:
:   `True`

Version Added:
:   2.12

Ini:
:   Section:
    :   [defaults]

    Key:
    :   validate_action_group_metadata

Environment:
:   Variable:
    :   [`ANSIBLE_VALIDATE_ACTION_GROUP_METADATA`](config.md#envvar-ANSIBLE_VALIDATE_ACTION_GROUP_METADATA)

### VARIABLE_PLUGINS_ENABLED

Description:
:   Accept list for variable plugins that require it.

Type:
:   list

Default:
:   `['host_group_vars']`

Version Added:
:   2.10

Ini:
:   Section:
    :   [defaults]

    Key:
    :   vars_plugins_enabled

Environment:
:   Variable:
    :   [`ANSIBLE_VARS_ENABLED`](config.md#envvar-ANSIBLE_VARS_ENABLED)

### VARIABLE_PRECEDENCE

Description:
:   Allows to change the group variable precedence merge order.

Type:
:   list

Default:
:   `['all_inventory', 'groups_inventory', 'all_plugins_inventory', 'all_plugins_play', 'groups_plugins_inventory', 'groups_plugins_play']`

Version Added:
:   2.4

Ini:
:   Section:
    :   [defaults]

    Key:
    :   precedence

Environment:
:   Variable:
    :   [`ANSIBLE_PRECEDENCE`](config.md#envvar-ANSIBLE_PRECEDENCE)

### VAULT_ENCRYPT_SALT

Description:
:   The salt to use for the vault encryption. If it is not provided, a random salt will be used.

Default:
:   `None`

Version Added:
:   2.15

Ini:
:   Section:
    :   [defaults]

    Key:
    :   vault_encrypt_salt

Environment:
:   Variable:
    :   [`ANSIBLE_VAULT_ENCRYPT_SALT`](config.md#envvar-ANSIBLE_VAULT_ENCRYPT_SALT)

### VERBOSE_TO_STDERR

Description:
:   Force ‘verbose’ option to use stderr instead of stdout

Type:
:   bool

Default:
:   `False`

Version Added:
:   2.8

Ini:
:   Section:
    :   [defaults]

    Key:
    :   verbose_to_stderr

Environment:
:   Variable:
    :   [`ANSIBLE_VERBOSE_TO_STDERR`](config.md#envvar-ANSIBLE_VERBOSE_TO_STDERR)

### WIN_ASYNC_STARTUP_TIMEOUT

Description:
:   For asynchronous tasks in Ansible (covered in Asynchronous Actions and Polling), this is how long, in seconds, to wait for the task spawned by Ansible to connect back to the named pipe used on Windows systems. The default is 5 seconds. This can be too low on slower systems, or systems under heavy load. This is not the total time an async command can run for, but is a separate timeout to wait for an async command to start. The task will only start to be timed against its async_timeout once it has connected to the pipe, so the overall maximum duration the task can take will be extended by the amount specified here.

Type:
:   integer

Default:
:   `5`

Version Added:
:   2.10

Ini:
:   Section:
    :   [defaults]

    Key:
    :   win_async_startup_timeout

Environment:
:   Variable:
    :   [`ANSIBLE_WIN_ASYNC_STARTUP_TIMEOUT`](config.md#envvar-ANSIBLE_WIN_ASYNC_STARTUP_TIMEOUT)

Variables:
:   name:
    :   ansible_win_async_startup_timeout

### WORKER_SHUTDOWN_POLL_COUNT

Description:
:   The maximum number of times to check Task Queue Manager worker processes to verify they have exited cleanly. After this limit is reached any worker processes still running will be terminated. This is for internal use only.

Type:
:   integer

Default:
:   `0`

Version Added:
:   2.10

Environment:
:   Variable:
    :   [`ANSIBLE_WORKER_SHUTDOWN_POLL_COUNT`](config.md#envvar-ANSIBLE_WORKER_SHUTDOWN_POLL_COUNT)

### WORKER_SHUTDOWN_POLL_DELAY

Description:
:   The number of seconds to sleep between polling loops when checking Task Queue Manager worker processes to verify they have exited cleanly. This is for internal use only.

Type:
:   float

Default:
:   `0.1`

Version Added:
:   2.10

Environment:
:   Variable:
    :   [`ANSIBLE_WORKER_SHUTDOWN_POLL_DELAY`](config.md#envvar-ANSIBLE_WORKER_SHUTDOWN_POLL_DELAY)

### YAML_FILENAME_EXTENSIONS

Description:
:   Check all of these extensions when looking for ‘variable’ files which should be YAML or JSON or vaulted versions of these. This affects vars_files, include_vars, inventory and vars plugins among others.

Type:
:   list

Default:
:   `['.yml', '.yaml', '.json']`

Ini:
:   Section:
    :   [defaults]

    Key:
    :   yaml_valid_extensions

Environment:
:   Variable:
    :   [`ANSIBLE_YAML_FILENAME_EXT`](config.md#envvar-ANSIBLE_YAML_FILENAME_EXT)

## Environment Variables

Other environment variables to configure plugins in collections can be found in [Index of all Collection Environment Variables](../collections/environment_variables.md#list-of-collection-env-vars).

ANSIBLE_CONFIG
:   Override the default ansible config file

ANSIBLE_HOME
:   The default root path for Ansible config files on the controller.

    See also [ANSIBLE_HOME](config.md#ansible-home)

ANSIBLE_CONNECTION_PATH
:   Specify where to look for the ansible-connection script. This location will be checked before searching $PATH.If null, ansible will start with the same directory as the ansible script.

    See also [ANSIBLE_CONNECTION_PATH](config.md#ansible-connection-path)

ANSIBLE_COW_SELECTION
:   This allows you to chose a specific cowsay stencil for the banners or use ‘random’ to cycle through them.

    See also [ANSIBLE_COW_SELECTION](config.md#ansible-cow-selection)

ANSIBLE_COW_ACCEPTLIST
:   Accept list of cowsay templates that are ‘safe’ to use, set to empty list if you want to enable all installed templates.

    See also [ANSIBLE_COW_ACCEPTLIST](config.md#ansible-cow-acceptlist)

    Version Added:
    :   2.11

ANSIBLE_FORCE_COLOR
:   This option forces color mode even when running without a TTY or the “nocolor” setting is True.

    See also [ANSIBLE_FORCE_COLOR](config.md#ansible-force-color)

ANSIBLE_NOCOLOR
:   This setting allows suppressing colorizing output, which is used to give a better indication of failure and status information.

    See also [ANSIBLE_NOCOLOR](config.md#ansible-nocolor)

NO_COLOR
:   This setting allows suppressing colorizing output, which is used to give a better indication of failure and status information.

    See also [ANSIBLE_NOCOLOR](config.md#ansible-nocolor)

    Version Added:
    :   2.11

ANSIBLE_NOCOWS
:   If you have cowsay installed but want to avoid the ‘cows’ (why????), use this.

    See also [ANSIBLE_NOCOWS](config.md#ansible-nocows)

ANSIBLE_COW_PATH
:   Specify a custom cowsay path or swap in your cowsay implementation of choice

    See also [ANSIBLE_COW_PATH](config.md#ansible-cow-path)

ANSIBLE_PIPELINING
:   This is a global option, each connection plugin can override either by having more specific options or not supporting pipelining at all.Pipelining, if supported by the connection plugin, reduces the number of network operations required to execute a module on the remote server, by executing many Ansible modules without actual file transfer.It can result in a very significant performance improvement when enabled.However this conflicts with privilege escalation (become). For example, when using ‘sudo:’ operations you must first disable ‘requiretty’ in /etc/sudoers on all managed hosts, which is why it is disabled by default.This setting will be disabled if `ANSIBLE_KEEP_REMOTE_FILES` is enabled.

    See also [ANSIBLE_PIPELINING](config.md#ansible-pipelining)

ANSIBLE_ANY_ERRORS_FATAL
:   Sets the default value for the any_errors_fatal keyword, if True, Task failures will be considered fatal errors.

    See also [ANY_ERRORS_FATAL](config.md#any-errors-fatal)

ANSIBLE_BECOME_ALLOW_SAME_USER
:   This setting controls if become is skipped when remote user and become user are the same. I.E root sudo to root.If executable, it will be run and the resulting stdout will be used as the password.

    See also [BECOME_ALLOW_SAME_USER](config.md#become-allow-same-user)

ANSIBLE_BECOME_PASSWORD_FILE
:   The password file to use for the become plugin. –become-password-file.If executable, it will be run and the resulting stdout will be used as the password.

    See also [BECOME_PASSWORD_FILE](config.md#become-password-file)

ANSIBLE_AGNOSTIC_BECOME_PROMPT
:   Display an agnostic become prompt instead of displaying a prompt containing the command line supplied become method

    See also [AGNOSTIC_BECOME_PROMPT](config.md#agnostic-become-prompt)

ANSIBLE_CACHE_PLUGIN
:   Chooses which cache plugin to use, the default ‘memory’ is ephemeral.

    See also [CACHE_PLUGIN](config.md#cache-plugin)

ANSIBLE_CACHE_PLUGIN_CONNECTION
:   Defines connection or path information for the cache plugin

    See also [CACHE_PLUGIN_CONNECTION](config.md#cache-plugin-connection)

ANSIBLE_CACHE_PLUGIN_PREFIX
:   Prefix to use for cache plugin files/tables

    See also [CACHE_PLUGIN_PREFIX](config.md#cache-plugin-prefix)

ANSIBLE_CACHE_PLUGIN_TIMEOUT
:   Expiration timeout for the cache plugin data

    See also [CACHE_PLUGIN_TIMEOUT](config.md#cache-plugin-timeout)

ANSIBLE_COLLECTIONS_SCAN_SYS_PATH
:   A boolean to enable or disable scanning the sys.path for installed collections

    See also [COLLECTIONS_SCAN_SYS_PATH](config.md#collections-scan-sys-path)

ANSIBLE_COLLECTIONS_PATHS
:   Colon separated paths in which Ansible will search for collections content. Collections must be in nested *subdirectories*, not directly in these directories. For example, if `COLLECTIONS_PATHS` includes `'{{ ANSIBLE_HOME ~ "/collections" }}'`, and you want to add `my.collection` to that directory, it must be saved as `'{{ ANSIBLE_HOME} ~ "/collections/ansible_collections/my/collection" }}'`.

    See also [COLLECTIONS_PATHS](config.md#collections-paths)

ANSIBLE_COLLECTIONS_PATH
:   Colon separated paths in which Ansible will search for collections content. Collections must be in nested *subdirectories*, not directly in these directories. For example, if `COLLECTIONS_PATHS` includes `'{{ ANSIBLE_HOME ~ "/collections" }}'`, and you want to add `my.collection` to that directory, it must be saved as `'{{ ANSIBLE_HOME} ~ "/collections/ansible_collections/my/collection" }}'`.

    See also [COLLECTIONS_PATHS](config.md#collections-paths)

    Version Added:
    :   2.10

ANSIBLE_COLLECTIONS_ON_ANSIBLE_VERSION_MISMATCH
:   When a collection is loaded that does not support the running Ansible version (with the collection metadata key requires_ansible).

    See also [COLLECTIONS_ON_ANSIBLE_VERSION_MISMATCH](config.md#collections-on-ansible-version-mismatch)

ANSIBLE_COLOR_CHANGED
:   Defines the color to use on ‘Changed’ task status

    See also [COLOR_CHANGED](config.md#color-changed)

ANSIBLE_COLOR_CONSOLE_PROMPT
:   Defines the default color to use for ansible-console

    See also [COLOR_CONSOLE_PROMPT](config.md#color-console-prompt)

ANSIBLE_COLOR_DEBUG
:   Defines the color to use when emitting debug messages

    See also [COLOR_DEBUG](config.md#color-debug)

ANSIBLE_COLOR_DEPRECATE
:   Defines the color to use when emitting deprecation messages

    See also [COLOR_DEPRECATE](config.md#color-deprecate)

ANSIBLE_COLOR_DIFF_ADD
:   Defines the color to use when showing added lines in diffs

    See also [COLOR_DIFF_ADD](config.md#color-diff-add)

ANSIBLE_COLOR_DIFF_LINES
:   Defines the color to use when showing diffs

    See also [COLOR_DIFF_LINES](config.md#color-diff-lines)

ANSIBLE_COLOR_DIFF_REMOVE
:   Defines the color to use when showing removed lines in diffs

    See also [COLOR_DIFF_REMOVE](config.md#color-diff-remove)

ANSIBLE_COLOR_ERROR
:   Defines the color to use when emitting error messages

    See also [COLOR_ERROR](config.md#color-error)

ANSIBLE_COLOR_HIGHLIGHT
:   Defines the color to use for highlighting

    See also [COLOR_HIGHLIGHT](config.md#color-highlight)

ANSIBLE_COLOR_OK
:   Defines the color to use when showing ‘OK’ task status

    See also [COLOR_OK](config.md#color-ok)

ANSIBLE_COLOR_SKIP
:   Defines the color to use when showing ‘Skipped’ task status

    See also [COLOR_SKIP](config.md#color-skip)

ANSIBLE_COLOR_UNREACHABLE
:   Defines the color to use on ‘Unreachable’ status

    See also [COLOR_UNREACHABLE](config.md#color-unreachable)

ANSIBLE_COLOR_VERBOSE
:   Defines the color to use when emitting verbose messages. i.e those that show with ‘-v’s.

    See also [COLOR_VERBOSE](config.md#color-verbose)

ANSIBLE_COLOR_WARN
:   Defines the color to use when emitting warning messages

    See also [COLOR_WARN](config.md#color-warn)

ANSIBLE_CONNECTION_PASSWORD_FILE
:   The password file to use for the connection plugin. –connection-password-file.

    See also [CONNECTION_PASSWORD_FILE](config.md#connection-password-file)

_ANSIBLE_COVERAGE_REMOTE_OUTPUT
:   Sets the output directory on the remote host to generate coverage reports to.Currently only used for remote coverage on PowerShell modules.This is for internal use only.

    See also [COVERAGE_REMOTE_OUTPUT](config.md#coverage-remote-output)

_ANSIBLE_COVERAGE_REMOTE_PATH_FILTER
:   A list of paths for files on the Ansible controller to run coverage for when executing on the remote host.Only files that match the path glob will have its coverage collected.Multiple path globs can be specified and are separated by `:`.Currently only used for remote coverage on PowerShell modules.This is for internal use only.

    See also [COVERAGE_REMOTE_PATHS](config.md#coverage-remote-paths)

ANSIBLE_ACTION_WARNINGS
:   By default Ansible will issue a warning when received from a task action (module or action plugin)These warnings can be silenced by adjusting this setting to False.

    See also [ACTION_WARNINGS](config.md#action-warnings)

ANSIBLE_LOCALHOST_WARNING
:   By default Ansible will issue a warning when there are no hosts in the inventory.These warnings can be silenced by adjusting this setting to False.

    See also [LOCALHOST_WARNING](config.md#localhost-warning)

ANSIBLE_INVENTORY_UNPARSED_WARNING
:   By default Ansible will issue a warning when no inventory was loaded and notes that it will use an implicit localhost-only inventory.These warnings can be silenced by adjusting this setting to False.

    See also [INVENTORY_UNPARSED_WARNING](config.md#inventory-unparsed-warning)

ANSIBLE_DOC_FRAGMENT_PLUGINS
:   Colon separated paths in which Ansible will search for Documentation Fragments Plugins.

    See also [DOC_FRAGMENT_PLUGIN_PATH](config.md#doc-fragment-plugin-path)

ANSIBLE_ACTION_PLUGINS
:   Colon separated paths in which Ansible will search for Action Plugins.

    See also [DEFAULT_ACTION_PLUGIN_PATH](config.md#default-action-plugin-path)

ANSIBLE_ASK_PASS
:   This controls whether an Ansible playbook should prompt for a login password. If using SSH keys for authentication, you probably do not need to change this setting.

    See also [DEFAULT_ASK_PASS](config.md#default-ask-pass)

ANSIBLE_ASK_VAULT_PASS
:   This controls whether an Ansible playbook should prompt for a vault password.

    See also [DEFAULT_ASK_VAULT_PASS](config.md#default-ask-vault-pass)

ANSIBLE_BECOME
:   Toggles the use of privilege escalation, allowing you to ‘become’ another user after login.

    See also [DEFAULT_BECOME](config.md#default-become)

ANSIBLE_BECOME_ASK_PASS
:   Toggle to prompt for privilege escalation password.

    See also [DEFAULT_BECOME_ASK_PASS](config.md#default-become-ask-pass)

ANSIBLE_BECOME_METHOD
:   Privilege escalation method to use when become is enabled.

    See also [DEFAULT_BECOME_METHOD](config.md#default-become-method)

ANSIBLE_BECOME_EXE
:   executable to use for privilege escalation, otherwise Ansible will depend on PATH

    See also [DEFAULT_BECOME_EXE](config.md#default-become-exe)

ANSIBLE_BECOME_FLAGS
:   Flags to pass to the privilege escalation executable.

    See also [DEFAULT_BECOME_FLAGS](config.md#default-become-flags)

ANSIBLE_BECOME_PLUGINS
:   Colon separated paths in which Ansible will search for Become Plugins.

    See also [BECOME_PLUGIN_PATH](config.md#become-plugin-path)

ANSIBLE_BECOME_USER
:   The user your login/remote user ‘becomes’ when using privilege escalation, most systems will use ‘root’ when no user is specified.

    See also [DEFAULT_BECOME_USER](config.md#default-become-user)

ANSIBLE_CACHE_PLUGINS
:   Colon separated paths in which Ansible will search for Cache Plugins.

    See also [DEFAULT_CACHE_PLUGIN_PATH](config.md#default-cache-plugin-path)

ANSIBLE_CALLBACK_PLUGINS
:   Colon separated paths in which Ansible will search for Callback Plugins.

    See also [DEFAULT_CALLBACK_PLUGIN_PATH](config.md#default-callback-plugin-path)

ANSIBLE_CALLBACKS_ENABLED
:   List of enabled callbacks, not all callbacks need enabling, but many of those shipped with Ansible do as we don’t want them activated by default.

    See also [CALLBACKS_ENABLED](config.md#callbacks-enabled)

    Version Added:
    :   2.11

ANSIBLE_CLICONF_PLUGINS
:   Colon separated paths in which Ansible will search for Cliconf Plugins.

    See also [DEFAULT_CLICONF_PLUGIN_PATH](config.md#default-cliconf-plugin-path)

ANSIBLE_CONNECTION_PLUGINS
:   Colon separated paths in which Ansible will search for Connection Plugins.

    See also [DEFAULT_CONNECTION_PLUGIN_PATH](config.md#default-connection-plugin-path)

ANSIBLE_DEBUG
:   Toggles debug output in Ansible. This is *very* verbose and can hinder multiprocessing. Debug output can also include secret information despite no_log settings being enabled, which means debug mode should not be used in production.

    See also [DEFAULT_DEBUG](config.md#default-debug)

ANSIBLE_EXECUTABLE
:   This indicates the command to use to spawn a shell under for Ansible’s execution needs on a target. Users may need to change this in rare instances when shell usage is constrained, but in most cases it may be left as is.

    See also [DEFAULT_EXECUTABLE](config.md#default-executable)

ANSIBLE_FACT_PATH
:   This option allows you to globally configure a custom path for ‘local_facts’ for the implied [ansible_collections.ansible.builtin.setup_module](https://docs.ansible.com/ansible/7/collections/ansible/builtin/setup_module.html#ansible-collections-ansible-builtin-setup-module "(in Ansible v7)") task when using fact gathering.If not set, it will fallback to the default from the `ansible.builtin.setup` module: `/etc/ansible/facts.d`.This does **not** affect user defined tasks that use the `ansible.builtin.setup` module.The real action being created by the implicit task is currently `ansible.legacy.gather_facts` module, which then calls the configured fact modules, by default this will be `ansible.builtin.setup` for POSIX systems but other platforms might have different defaults.

    See also [DEFAULT_FACT_PATH](config.md#default-fact-path)

ANSIBLE_FILTER_PLUGINS
:   Colon separated paths in which Ansible will search for Jinja2 Filter Plugins.

    See also [DEFAULT_FILTER_PLUGIN_PATH](config.md#default-filter-plugin-path)

ANSIBLE_FORCE_HANDLERS
:   This option controls if notified handlers run on a host even if a failure occurs on that host.When false, the handlers will not run if a failure has occurred on a host.This can also be set per play or on the command line. See Handlers and Failure for more details.

    See also [DEFAULT_FORCE_HANDLERS](config.md#default-force-handlers)

ANSIBLE_FORKS
:   Maximum number of forks Ansible will use to execute tasks on target hosts.

    See also [DEFAULT_FORKS](config.md#default-forks)

ANSIBLE_GATHERING
:   This setting controls the default policy of fact gathering (facts discovered about remote systems).This option can be useful for those wishing to save fact gathering time. Both ‘smart’ and ‘explicit’ will use the cache plugin.

    See also [DEFAULT_GATHERING](config.md#default-gathering)

ANSIBLE_GATHER_SUBSET
:   Set the gather_subset option for the [ansible_collections.ansible.builtin.setup_module](https://docs.ansible.com/ansible/7/collections/ansible/builtin/setup_module.html#ansible-collections-ansible-builtin-setup-module "(in Ansible v7)") task in the implicit fact gathering. See the module documentation for specifics.It does **not** apply to user defined `ansible.builtin.setup` tasks.

    See also [DEFAULT_GATHER_SUBSET](config.md#default-gather-subset)

ANSIBLE_GATHER_TIMEOUT
:   Set the timeout in seconds for the implicit fact gathering, see the module documentation for specifics.It does **not** apply to user defined [ansible_collections.ansible.builtin.setup_module](https://docs.ansible.com/ansible/7/collections/ansible/builtin/setup_module.html#ansible-collections-ansible-builtin-setup-module "(in Ansible v7)") tasks.

    See also [DEFAULT_GATHER_TIMEOUT](config.md#default-gather-timeout)

ANSIBLE_HASH_BEHAVIOUR
:   This setting controls how duplicate definitions of dictionary variables (aka hash, map, associative array) are handled in Ansible.This does not affect variables whose values are scalars (integers, strings) or arrays.\*\*WARNING\*\*, changing this setting is not recommended as this is fragile and makes your content (plays, roles, collections) non portable, leading to continual confusion and misuse. Don’t change this setting unless you think you have an absolute need for it.We recommend avoiding reusing variable names and relying on the `combine` filter and `vars` and `varnames` lookups to create merged versions of the individual variables. In our experience this is rarely really needed and a sign that too much complexity has been introduced into the data structures and plays.For some uses you can also look into custom vars_plugins to merge on input, even substituting the default `host_group_vars` that is in charge of parsing the `host_vars/` and `group_vars/` directories. Most users of this setting are only interested in inventory scope, but the setting itself affects all sources and makes debugging even harder.All playbooks and roles in the official examples repos assume the default for this setting.Changing the setting to `merge` applies across variable sources, but many sources will internally still overwrite the variables. For example `include_vars` will dedupe variables internally before updating Ansible, with ‘last defined’ overwriting previous definitions in same file.The Ansible project recommends you **avoid ``merge`` for new projects.\*\*It is the intention of the Ansible developers to eventually deprecate and remove this setting, but it is being kept as some users do heavily rely on it. New projects should \*\*avoid ‘merge’**.

    See also [DEFAULT_HASH_BEHAVIOUR](config.md#default-hash-behaviour)

ANSIBLE_INVENTORY
:   Comma separated list of Ansible inventory sources

    See also [DEFAULT_HOST_LIST](config.md#default-host-list)

ANSIBLE_HTTPAPI_PLUGINS
:   Colon separated paths in which Ansible will search for HttpApi Plugins.

    See also [DEFAULT_HTTPAPI_PLUGIN_PATH](config.md#default-httpapi-plugin-path)

ANSIBLE_INVENTORY_PLUGINS
:   Colon separated paths in which Ansible will search for Inventory Plugins.

    See also [DEFAULT_INVENTORY_PLUGIN_PATH](config.md#default-inventory-plugin-path)

ANSIBLE_JINJA2_EXTENSIONS
:   This is a developer-specific feature that allows enabling additional Jinja2 extensions.See the Jinja2 documentation for details. If you do not know what these do, you probably don’t need to change this setting :)

    See also [DEFAULT_JINJA2_EXTENSIONS](config.md#default-jinja2-extensions)

ANSIBLE_JINJA2_NATIVE
:   This option preserves variable types during template operations.

    See also [DEFAULT_JINJA2_NATIVE](config.md#default-jinja2-native)

ANSIBLE_KEEP_REMOTE_FILES
:   Enables/disables the cleaning up of the temporary files Ansible used to execute the tasks on the remote.If this option is enabled it will disable `ANSIBLE_PIPELINING`.

    See also [DEFAULT_KEEP_REMOTE_FILES](config.md#default-keep-remote-files)

ANSIBLE_LIBVIRT_LXC_NOSECLABEL
:   This setting causes libvirt to connect to lxc containers by passing –noseclabel to virsh. This is necessary when running on systems which do not have SELinux.

    See also [DEFAULT_LIBVIRT_LXC_NOSECLABEL](config.md#default-libvirt-lxc-noseclabel)

ANSIBLE_LOAD_CALLBACK_PLUGINS
:   Controls whether callback plugins are loaded when running /usr/bin/ansible. This may be used to log activity from the command line, send notifications, and so on. Callback plugins are always loaded for `ansible-playbook`.

    See also [DEFAULT_LOAD_CALLBACK_PLUGINS](config.md#default-load-callback-plugins)

ANSIBLE_LOCAL_TEMP
:   Temporary directory for Ansible to use on the controller.

    See also [DEFAULT_LOCAL_TMP](config.md#default-local-tmp)

ANSIBLE_LOG_PATH
:   File to which Ansible will log on the controller. When empty logging is disabled.

    See also [DEFAULT_LOG_PATH](config.md#default-log-path)

ANSIBLE_LOG_FILTER
:   List of logger names to filter out of the log file

    See also [DEFAULT_LOG_FILTER](config.md#default-log-filter)

ANSIBLE_LOOKUP_PLUGINS
:   Colon separated paths in which Ansible will search for Lookup Plugins.

    See also [DEFAULT_LOOKUP_PLUGIN_PATH](config.md#default-lookup-plugin-path)

ANSIBLE_MODULE_ARGS
:   This sets the default arguments to pass to the `ansible` adhoc binary if no `-a` is specified.

    See also [DEFAULT_MODULE_ARGS](config.md#default-module-args)

ANSIBLE_LIBRARY
:   Colon separated paths in which Ansible will search for Modules.

    See also [DEFAULT_MODULE_PATH](config.md#default-module-path)

ANSIBLE_MODULE_UTILS
:   Colon separated paths in which Ansible will search for Module utils files, which are shared by modules.

    See also [DEFAULT_MODULE_UTILS_PATH](config.md#default-module-utils-path)

ANSIBLE_NETCONF_PLUGINS
:   Colon separated paths in which Ansible will search for Netconf Plugins.

    See also [DEFAULT_NETCONF_PLUGIN_PATH](config.md#default-netconf-plugin-path)

ANSIBLE_NO_LOG
:   Toggle Ansible’s display and logging of task details, mainly used to avoid security disclosures.

    See also [DEFAULT_NO_LOG](config.md#default-no-log)

ANSIBLE_NO_TARGET_SYSLOG
:   Toggle Ansible logging to syslog on the target when it executes tasks. On Windows hosts this will disable a newer style PowerShell modules from writing to the event log.

    See also [DEFAULT_NO_TARGET_SYSLOG](config.md#default-no-target-syslog)

ANSIBLE_NULL_REPRESENTATION
:   What templating should return as a ‘null’ value. When not set it will let Jinja2 decide.

    See also [DEFAULT_NULL_REPRESENTATION](config.md#default-null-representation)

ANSIBLE_POLL_INTERVAL
:   For asynchronous tasks in Ansible (covered in Asynchronous Actions and Polling), this is how often to check back on the status of those tasks when an explicit poll interval is not supplied. The default is a reasonably moderate 15 seconds which is a tradeoff between checking in frequently and providing a quick turnaround when something may have completed.

    See also [DEFAULT_POLL_INTERVAL](config.md#default-poll-interval)

ANSIBLE_PRIVATE_KEY_FILE
:   Option for connections using a certificate or key file to authenticate, rather than an agent or passwords, you can set the default value here to avoid re-specifying –private-key with every invocation.

    See also [DEFAULT_PRIVATE_KEY_FILE](config.md#default-private-key-file)

ANSIBLE_PRIVATE_ROLE_VARS
:   Makes role variables inaccessible from other roles.This was introduced as a way to reset role variables to default values if a role is used more than once in a playbook.

    See also [DEFAULT_PRIVATE_ROLE_VARS](config.md#default-private-role-vars)

ANSIBLE_REMOTE_PORT
:   Port to use in remote connections, when blank it will use the connection plugin default.

    See also [DEFAULT_REMOTE_PORT](config.md#default-remote-port)

ANSIBLE_REMOTE_USER
:   Sets the login user for the target machinesWhen blank it uses the connection plugin’s default, normally the user currently executing Ansible.

    See also [DEFAULT_REMOTE_USER](config.md#default-remote-user)

ANSIBLE_ROLES_PATH
:   Colon separated paths in which Ansible will search for Roles.

    See also [DEFAULT_ROLES_PATH](config.md#default-roles-path)

ANSIBLE_SELINUX_SPECIAL_FS
:   Some filesystems do not support safe operations and/or return inconsistent errors, this setting makes Ansible ‘tolerate’ those in the list w/o causing fatal errors.Data corruption may occur and writes are not always verified when a filesystem is in the list.

    See also [DEFAULT_SELINUX_SPECIAL_FS](config.md#default-selinux-special-fs)

    Version Added:
    :   2.9

ANSIBLE_STDOUT_CALLBACK
:   Set the main callback used to display Ansible output. You can only have one at a time.You can have many other callbacks, but just one can be in charge of stdout.See [Callback plugins](../plugins/callback.md#callback-plugins) for a list of available options.

    See also [DEFAULT_STDOUT_CALLBACK](config.md#default-stdout-callback)

ANSIBLE_EDITOR
:   See also [EDITOR](config.md#editor)

    Version Added:
    :   2.15

EDITOR
:   See also [EDITOR](config.md#editor)

ANSIBLE_ENABLE_TASK_DEBUGGER
:   Whether or not to enable the task debugger, this previously was done as a strategy plugin.Now all strategy plugins can inherit this behavior. The debugger defaults to activating whena task is failed on unreachable. Use the debugger keyword for more flexibility.

    See also [ENABLE_TASK_DEBUGGER](config.md#enable-task-debugger)

ANSIBLE_TASK_DEBUGGER_IGNORE_ERRORS
:   This option defines whether the task debugger will be invoked on a failed task when ignore_errors=True is specified.True specifies that the debugger will honor ignore_errors, False will not honor ignore_errors.

    See also [TASK_DEBUGGER_IGNORE_ERRORS](config.md#task-debugger-ignore-errors)

ANSIBLE_STRATEGY
:   Set the default strategy used for plays.

    See also [DEFAULT_STRATEGY](config.md#default-strategy)

ANSIBLE_STRATEGY_PLUGINS
:   Colon separated paths in which Ansible will search for Strategy Plugins.

    See also [DEFAULT_STRATEGY_PLUGIN_PATH](config.md#default-strategy-plugin-path)

ANSIBLE_SU
:   Toggle the use of “su” for tasks.

    See also [DEFAULT_SU](config.md#default-su)

ANSIBLE_SYSLOG_FACILITY
:   Syslog facility to use when Ansible logs to the remote target

    See also [DEFAULT_SYSLOG_FACILITY](config.md#default-syslog-facility)

ANSIBLE_TERMINAL_PLUGINS
:   Colon separated paths in which Ansible will search for Terminal Plugins.

    See also [DEFAULT_TERMINAL_PLUGIN_PATH](config.md#default-terminal-plugin-path)

ANSIBLE_TEST_PLUGINS
:   Colon separated paths in which Ansible will search for Jinja2 Test Plugins.

    See also [DEFAULT_TEST_PLUGIN_PATH](config.md#default-test-plugin-path)

ANSIBLE_TIMEOUT
:   This is the default timeout for connection plugins to use.

    See also [DEFAULT_TIMEOUT](config.md#default-timeout)

ANSIBLE_TRANSPORT
:   Default connection plugin to use, the ‘smart’ option will toggle between ‘ssh’ and ‘paramiko’ depending on controller OS and ssh versions

    See also [DEFAULT_TRANSPORT](config.md#default-transport)

ANSIBLE_ERROR_ON_UNDEFINED_VARS
:   When True, this causes ansible templating to fail steps that reference variable names that are likely typoed.Otherwise, any ‘{{ template_expression }}’ that contains undefined variables will be rendered in a template or ansible action line exactly as written.

    See also [DEFAULT_UNDEFINED_VAR_BEHAVIOR](config.md#default-undefined-var-behavior)

ANSIBLE_VARS_PLUGINS
:   Colon separated paths in which Ansible will search for Vars Plugins.

    See also [DEFAULT_VARS_PLUGIN_PATH](config.md#default-vars-plugin-path)

ANSIBLE_VAULT_ID_MATCH
:   If true, decrypting vaults with a vault id will only try the password from the matching vault-id

    See also [DEFAULT_VAULT_ID_MATCH](config.md#default-vault-id-match)

ANSIBLE_VAULT_IDENTITY
:   The label to use for the default vault id label in cases where a vault id label is not provided

    See also [DEFAULT_VAULT_IDENTITY](config.md#default-vault-identity)

ANSIBLE_VAULT_ENCRYPT_SALT
:   The salt to use for the vault encryption. If it is not provided, a random salt will be used.

    See also [VAULT_ENCRYPT_SALT](config.md#vault-encrypt-salt)

ANSIBLE_VAULT_ENCRYPT_IDENTITY
:   The vault_id to use for encrypting by default. If multiple vault_ids are provided, this specifies which to use for encryption. The –encrypt-vault-id cli option overrides the configured value.

    See also [DEFAULT_VAULT_ENCRYPT_IDENTITY](config.md#default-vault-encrypt-identity)

ANSIBLE_VAULT_IDENTITY_LIST
:   A list of vault-ids to use by default. Equivalent to multiple –vault-id args. Vault-ids are tried in order.

    See also [DEFAULT_VAULT_IDENTITY_LIST](config.md#default-vault-identity-list)

ANSIBLE_VAULT_PASSWORD_FILE
:   The vault password file to use. Equivalent to –vault-password-file or –vault-idIf executable, it will be run and the resulting stdout will be used as the password.

    See also [DEFAULT_VAULT_PASSWORD_FILE](config.md#default-vault-password-file)

ANSIBLE_VERBOSITY
:   Sets the default verbosity, equivalent to the number of `-v` passed in the command line.

    See also [DEFAULT_VERBOSITY](config.md#default-verbosity)

ANSIBLE_DEPRECATION_WARNINGS
:   Toggle to control the showing of deprecation warnings

    See also [DEPRECATION_WARNINGS](config.md#deprecation-warnings)

ANSIBLE_DEVEL_WARNING
:   Toggle to control showing warnings related to running devel

    See also [DEVEL_WARNING](config.md#devel-warning)

ANSIBLE_DIFF_ALWAYS
:   Configuration toggle to tell modules to show differences when in ‘changed’ status, equivalent to `--diff`.

    See also [DIFF_ALWAYS](config.md#diff-always)

ANSIBLE_DIFF_CONTEXT
:   How many lines of context to show when displaying the differences between files.

    See also [DIFF_CONTEXT](config.md#diff-context)

ANSIBLE_DISPLAY_ARGS_TO_STDOUT
:   Normally `ansible-playbook` will print a header for each task that is run. These headers will contain the name: field from the task if you specified one. If you didn’t then `ansible-playbook` uses the task’s action to help you tell which task is presently running. Sometimes you run many of the same action and so you want more information about the task to differentiate it from others of the same action. If you set this variable to True in the config then `ansible-playbook` will also include the task’s arguments in the header.This setting defaults to False because there is a chance that you have sensitive values in your parameters and you do not want those to be printed.If you set this to True you should be sure that you have secured your environment’s stdout (no one can shoulder surf your screen and you aren’t saving stdout to an insecure file) or made sure that all of your playbooks explicitly added the `no_log: True` parameter to tasks which have sensitive values See How do I keep secret data in my playbook? for more information.

    See also [DISPLAY_ARGS_TO_STDOUT](config.md#display-args-to-stdout)

ANSIBLE_DISPLAY_SKIPPED_HOSTS
:   Toggle to control displaying skipped task/host entries in a task in the default callback

    See also [DISPLAY_SKIPPED_HOSTS](config.md#display-skipped-hosts)

ANSIBLE_DUPLICATE_YAML_DICT_KEY
:   By default Ansible will issue a warning when a duplicate dict key is encountered in YAML.These warnings can be silenced by adjusting this setting to False.

    See also [DUPLICATE_YAML_DICT_KEY](config.md#duplicate-yaml-dict-key)

ANSIBLE_ERROR_ON_MISSING_HANDLER
:   Toggle to allow missing handlers to become a warning instead of an error when notifying.

    See also [ERROR_ON_MISSING_HANDLER](config.md#error-on-missing-handler)

ANSIBLE_FACTS_MODULES
:   Which modules to run during a play’s fact gathering stage, using the default of ‘smart’ will try to figure it out based on connection type.If adding your own modules but you still want to use the default Ansible facts, you will want to include ‘setup’ or corresponding network module to the list (if you add ‘smart’, Ansible will also figure it out).This does not affect explicit calls to the ‘setup’ module, but does always affect the ‘gather_facts’ action (implicit or explicit).

    See also [FACTS_MODULES](config.md#facts-modules)

ANSIBLE_GALAXY_IGNORE
:   If set to yes, ansible-galaxy will not validate TLS certificates. This can be useful for testing against a server with a self-signed certificate.

    See also [GALAXY_IGNORE_CERTS](config.md#galaxy-ignore-certs)

ANSIBLE_GALAXY_ROLE_SKELETON
:   Role skeleton directory to use as a template for the `init` action in `ansible-galaxy`/`ansible-galaxy role`, same as `--role-skeleton`.

    See also [GALAXY_ROLE_SKELETON](config.md#galaxy-role-skeleton)

ANSIBLE_GALAXY_ROLE_SKELETON_IGNORE
:   patterns of files to ignore inside a Galaxy role or collection skeleton directory

    See also [GALAXY_ROLE_SKELETON_IGNORE](config.md#galaxy-role-skeleton-ignore)

ANSIBLE_GALAXY_COLLECTION_SKELETON
:   Collection skeleton directory to use as a template for the `init` action in `ansible-galaxy collection`, same as `--collection-skeleton`.

    See also [GALAXY_COLLECTION_SKELETON](config.md#galaxy-collection-skeleton)

ANSIBLE_GALAXY_COLLECTION_SKELETON_IGNORE
:   patterns of files to ignore inside a Galaxy collection skeleton directory

    See also [GALAXY_COLLECTION_SKELETON_IGNORE](config.md#galaxy-collection-skeleton-ignore)

ANSIBLE_GALAXY_SERVER
:   URL to prepend when roles don’t specify the full URI, assume they are referencing this server as the source.

    See also [GALAXY_SERVER](config.md#galaxy-server)

ANSIBLE_GALAXY_SERVER_LIST
:   A list of Galaxy servers to use when installing a collection.The value corresponds to the config ini header `[galaxy_server.{{item}}]` which defines the server details.See [Configuring the ansible-galaxy client](../collections_guide/collections_installing.md#galaxy-server-config) for more details on how to define a Galaxy server.The order of servers in this list is used to as the order in which a collection is resolved.Setting this config option will ignore the [GALAXY_SERVER](config.md#galaxy-server) config option.

    See also [GALAXY_SERVER_LIST](config.md#galaxy-server-list)

ANSIBLE_GALAXY_TOKEN_PATH
:   Local path to galaxy access token file

    See also [GALAXY_TOKEN_PATH](config.md#galaxy-token-path)

ANSIBLE_GALAXY_DISPLAY_PROGRESS
:   Some steps in `ansible-galaxy` display a progress wheel which can cause issues on certain displays or when outputting the stdout to a file.This config option controls whether the display wheel is shown or not.The default is to show the display wheel if stdout has a tty.

    See also [GALAXY_DISPLAY_PROGRESS](config.md#galaxy-display-progress)

ANSIBLE_GALAXY_CACHE_DIR
:   The directory that stores cached responses from a Galaxy server.This is only used by the `ansible-galaxy collection install` and `download` commands.Cache files inside this dir will be ignored if they are world writable.

    See also [GALAXY_CACHE_DIR](config.md#galaxy-cache-dir)

ANSIBLE_GALAXY_DISABLE_GPG_VERIFY
:   Disable GPG signature verification during collection installation.

    See also [GALAXY_DISABLE_GPG_VERIFY](config.md#galaxy-disable-gpg-verify)

ANSIBLE_GALAXY_GPG_KEYRING
:   Configure the keyring used for GPG signature verification during collection installation and verification.

    See also [GALAXY_GPG_KEYRING](config.md#galaxy-gpg-keyring)

ANSIBLE_GALAXY_IGNORE_SIGNATURE_STATUS_CODES
:   A list of GPG status codes to ignore during GPG signature verification. See L(<https://github.com/gpg/gnupg/blob/master/doc/DETAILS#general-status-codes>) for status code descriptions.If fewer signatures successfully verify the collection than GALAXY_REQUIRED_VALID_SIGNATURE_COUNT, signature verification will fail even if all error codes are ignored.

    See also [GALAXY_IGNORE_INVALID_SIGNATURE_STATUS_CODES](config.md#galaxy-ignore-invalid-signature-status-codes)

ANSIBLE_GALAXY_REQUIRED_VALID_SIGNATURE_COUNT
:   The number of signatures that must be successful during GPG signature verification while installing or verifying collections.This should be a positive integer or all to indicate all signatures must successfully validate the collection.Prepend + to the value to fail if no valid signatures are found for the collection.

    See also [GALAXY_REQUIRED_VALID_SIGNATURE_COUNT](config.md#galaxy-required-valid-signature-count)

ANSIBLE_HOST_KEY_CHECKING
:   Set this to “False” if you want to avoid host key checking by the underlying tools Ansible uses to connect to the host

    See also [HOST_KEY_CHECKING](config.md#host-key-checking)

ANSIBLE_HOST_PATTERN_MISMATCH
:   This setting changes the behaviour of mismatched host patterns, it allows you to force a fatal error, a warning or just ignore it

    See also [HOST_PATTERN_MISMATCH](config.md#host-pattern-mismatch)

ANSIBLE_PYTHON_INTERPRETER
:   Path to the Python interpreter to be used for module execution on remote targets, or an automatic discovery mode. Supported discovery modes are `auto` (the default), `auto_silent`, `auto_legacy`, and `auto_legacy_silent`. All discovery modes employ a lookup table to use the included system Python (on distributions known to include one), falling back to a fixed ordered list of well-known Python interpreter locations if a platform-specific default is not available. The fallback behavior will issue a warning that the interpreter should be set explicitly (since interpreters installed later may change which one is used). This warning behavior can be disabled by setting `auto_silent` or `auto_legacy_silent`. The value of `auto_legacy` provides all the same behavior, but for backwards-compatibility with older Ansible releases that always defaulted to `/usr/bin/python`, will use that interpreter if present.

    See also [INTERPRETER_PYTHON](config.md#interpreter-python)

ANSIBLE_TRANSFORM_INVALID_GROUP_CHARS
:   Make ansible transform invalid characters in group names supplied by inventory sources.

    See also [TRANSFORM_INVALID_GROUP_CHARS](config.md#transform-invalid-group-chars)

ANSIBLE_INVALID_TASK_ATTRIBUTE_FAILED
:   If ‘false’, invalid attributes for a task will result in warnings instead of errors

    See also [INVALID_TASK_ATTRIBUTE_FAILED](config.md#invalid-task-attribute-failed)

ANSIBLE_INVENTORY_ANY_UNPARSED_IS_FAILED
:   If ‘true’, it is a fatal error when any given inventory source cannot be successfully parsed by any available inventory plugin; otherwise, this situation only attracts a warning.

    See also [INVENTORY_ANY_UNPARSED_IS_FAILED](config.md#inventory-any-unparsed-is-failed)

ANSIBLE_INVENTORY_CACHE
:   Toggle to turn on inventory caching.This setting has been moved to the individual inventory plugins as a plugin option [Inventory plugins](../plugins/inventory.md#inventory-plugins).The existing configuration settings are still accepted with the inventory plugin adding additional options from inventory configuration.This message will be removed in 2.16.

    See also [INVENTORY_CACHE_ENABLED](config.md#inventory-cache-enabled)

ANSIBLE_INVENTORY_CACHE_PLUGIN
:   The plugin for caching inventory.This setting has been moved to the individual inventory plugins as a plugin option [Inventory plugins](../plugins/inventory.md#inventory-plugins).The existing configuration settings are still accepted with the inventory plugin adding additional options from inventory and fact cache configuration.This message will be removed in 2.16.

    See also [INVENTORY_CACHE_PLUGIN](config.md#inventory-cache-plugin)

ANSIBLE_INVENTORY_CACHE_CONNECTION
:   The inventory cache connection.This setting has been moved to the individual inventory plugins as a plugin option [Inventory plugins](../plugins/inventory.md#inventory-plugins).The existing configuration settings are still accepted with the inventory plugin adding additional options from inventory and fact cache configuration.This message will be removed in 2.16.

    See also [INVENTORY_CACHE_PLUGIN_CONNECTION](config.md#inventory-cache-plugin-connection)

ANSIBLE_INVENTORY_CACHE_PLUGIN_PREFIX
:   The table prefix for the cache plugin.This setting has been moved to the individual inventory plugins as a plugin option [Inventory plugins](../plugins/inventory.md#inventory-plugins).The existing configuration settings are still accepted with the inventory plugin adding additional options from inventory and fact cache configuration.This message will be removed in 2.16.

    See also [INVENTORY_CACHE_PLUGIN_PREFIX](config.md#inventory-cache-plugin-prefix)

ANSIBLE_INVENTORY_CACHE_TIMEOUT
:   Expiration timeout for the inventory cache plugin data.This setting has been moved to the individual inventory plugins as a plugin option [Inventory plugins](../plugins/inventory.md#inventory-plugins).The existing configuration settings are still accepted with the inventory plugin adding additional options from inventory and fact cache configuration.This message will be removed in 2.16.

    See also [INVENTORY_CACHE_TIMEOUT](config.md#inventory-cache-timeout)

ANSIBLE_INVENTORY_ENABLED
:   List of enabled inventory plugins, it also determines the order in which they are used.

    See also [INVENTORY_ENABLED](config.md#inventory-enabled)

ANSIBLE_INVENTORY_EXPORT
:   Controls if ansible-inventory will accurately reflect Ansible’s view into inventory or its optimized for exporting.

    See also [INVENTORY_EXPORT](config.md#inventory-export)

ANSIBLE_INVENTORY_IGNORE
:   List of extensions to ignore when using a directory as an inventory source

    See also [INVENTORY_IGNORE_EXTS](config.md#inventory-ignore-exts)

ANSIBLE_INVENTORY_IGNORE_REGEX
:   List of patterns to ignore when using a directory as an inventory source

    See also [INVENTORY_IGNORE_PATTERNS](config.md#inventory-ignore-patterns)

ANSIBLE_INVENTORY_UNPARSED_FAILED
:   If ‘true’ it is a fatal error if every single potential inventory source fails to parse, otherwise this situation will only attract a warning.

    See also [INVENTORY_UNPARSED_IS_FAILED](config.md#inventory-unparsed-is-failed)

ANSIBLE_JINJA2_NATIVE_WARNING
:   Toggle to control showing warnings related to running a Jinja version older than required for jinja2_native

    See also [JINJA2_NATIVE_WARNING](config.md#jinja2-native-warning)

    Deprecated in:
    :   2.17

    Deprecated detail:
    :   This option is no longer used in the Ansible Core code base.

ANSIBLE_MAX_DIFF_SIZE
:   Maximum size of files to be considered for diff display

    See also [MAX_FILE_SIZE_FOR_DIFF](config.md#max-file-size-for-diff)

ANSIBLE_NETWORK_GROUP_MODULES
:   See also [NETWORK_GROUP_MODULES](config.md#network-group-modules)

ANSIBLE_INJECT_FACT_VARS
:   Facts are available inside the ansible_facts variable, this setting also pushes them as their own vars in the main namespace.Unlike inside the ansible_facts dictionary, these will have an ansible_ prefix.

    See also [INJECT_FACTS_AS_VARS](config.md#inject-facts-as-vars)

ANSIBLE_MODULE_IGNORE_EXTS
:   List of extensions to ignore when looking for modules to loadThis is for rejecting script and binary module fallback extensions

    See also [MODULE_IGNORE_EXTS](config.md#module-ignore-exts)

ANSIBLE_MODULE_STRICT_UTF8_RESPONSE
:   Enables whether module responses are evaluated for containing non UTF-8 dataDisabling this may result in unexpected behaviorOnly ansible-core should evaluate this configuration

    See also [MODULE_STRICT_UTF8_RESPONSE](config.md#module-strict-utf8-response)

ANSIBLE_OLD_PLUGIN_CACHE_CLEAR
:   Previously Ansible would only clear some of the plugin loading caches when loading new roles, this led to some behaviours in which a plugin loaded in previous plays would be unexpectedly ‘sticky’. This setting allows to return to that behaviour.

    See also [OLD_PLUGIN_CACHE_CLEARING](config.md#old-plugin-cache-clearing)

ANSIBLE_PAGER
:   See also [PAGER](config.md#pager)

    Version Added:
    :   2.15

PAGER
:   See also [PAGER](config.md#pager)

ANSIBLE_PARAMIKO_HOST_KEY_AUTO_ADD
:   See also [PARAMIKO_HOST_KEY_AUTO_ADD](config.md#paramiko-host-key-auto-add)

ANSIBLE_PARAMIKO_LOOK_FOR_KEYS
:   See also [PARAMIKO_LOOK_FOR_KEYS](config.md#paramiko-look-for-keys)

ANSIBLE_PERSISTENT_CONTROL_PATH_DIR
:   Path to socket to be used by the connection persistence system.

    See also [PERSISTENT_CONTROL_PATH_DIR](config.md#persistent-control-path-dir)

ANSIBLE_PERSISTENT_CONNECT_TIMEOUT
:   This controls how long the persistent connection will remain idle before it is destroyed.

    See also [PERSISTENT_CONNECT_TIMEOUT](config.md#persistent-connect-timeout)

ANSIBLE_PERSISTENT_CONNECT_RETRY_TIMEOUT
:   This controls the retry timeout for persistent connection to connect to the local domain socket.

    See also [PERSISTENT_CONNECT_RETRY_TIMEOUT](config.md#persistent-connect-retry-timeout)

ANSIBLE_PERSISTENT_COMMAND_TIMEOUT
:   This controls the amount of time to wait for response from remote device before timing out persistent connection.

    See also [PERSISTENT_COMMAND_TIMEOUT](config.md#persistent-command-timeout)

ANSIBLE_PLAYBOOK_DIR
:   A number of non-playbook CLIs have a `--playbook-dir` argument; this sets the default value for it.

    See also [PLAYBOOK_DIR](config.md#playbook-dir)

ANSIBLE_PLAYBOOK_VARS_ROOT
:   This sets which playbook dirs will be used as a root to process vars plugins, which includes finding host_vars/group_vars

    See also [PLAYBOOK_VARS_ROOT](config.md#playbook-vars-root)

ANSIBLE_PYTHON_MODULE_RLIMIT_NOFILE
:   Attempts to set RLIMIT_NOFILE soft limit to the specified value when executing Python modules (can speed up subprocess usage on Python 2.x. See <https://bugs.python.org/issue11284>). The value will be limited by the existing hard limit. Default value of 0 does not attempt to adjust existing system-defined limits.

    See also [PYTHON_MODULE_RLIMIT_NOFILE](config.md#python-module-rlimit-nofile)

ANSIBLE_RETRY_FILES_ENABLED
:   This controls whether a failed Ansible playbook should create a .retry file.

    See also [RETRY_FILES_ENABLED](config.md#retry-files-enabled)

ANSIBLE_RETRY_FILES_SAVE_PATH
:   This sets the path in which Ansible will save .retry files when a playbook fails and retry files are enabled.This file will be overwritten after each run with the list of failed hosts from all plays.

    See also [RETRY_FILES_SAVE_PATH](config.md#retry-files-save-path)

ANSIBLE_RUN_VARS_PLUGINS
:   This setting can be used to optimize vars_plugin usage depending on user’s inventory size and play selection.

    See also [RUN_VARS_PLUGINS](config.md#run-vars-plugins)

ANSIBLE_SHOW_CUSTOM_STATS
:   This adds the custom stats set via the set_stats plugin to the default output

    See also [SHOW_CUSTOM_STATS](config.md#show-custom-stats)

ANSIBLE_STRING_TYPE_FILTERS
:   This list of filters avoids ‘type conversion’ when templating variablesUseful when you want to avoid conversion into lists or dictionaries for JSON strings, for example.

    See also [STRING_TYPE_FILTERS](config.md#string-type-filters)

ANSIBLE_SYSTEM_WARNINGS
:   Allows disabling of warnings related to potential issues on the system running ansible itself (not on the managed hosts)These may include warnings about 3rd party packages or other conditions that should be resolved if possible.

    See also [SYSTEM_WARNINGS](config.md#system-warnings)

ANSIBLE_RUN_TAGS
:   default list of tags to run in your plays, Skip Tags has precedence.

    See also [TAGS_RUN](config.md#tags-run)

ANSIBLE_SKIP_TAGS
:   default list of tags to skip in your plays, has precedence over Run Tags

    See also [TAGS_SKIP](config.md#tags-skip)

ANSIBLE_TASK_TIMEOUT
:   Set the maximum time (in seconds) that a task can run for.If set to 0 (the default) there is no timeout.

    See also [TASK_TIMEOUT](config.md#task-timeout)

ANSIBLE_WORKER_SHUTDOWN_POLL_COUNT
:   The maximum number of times to check Task Queue Manager worker processes to verify they have exited cleanly.After this limit is reached any worker processes still running will be terminated.This is for internal use only.

    See also [WORKER_SHUTDOWN_POLL_COUNT](config.md#worker-shutdown-poll-count)

ANSIBLE_WORKER_SHUTDOWN_POLL_DELAY
:   The number of seconds to sleep between polling loops when checking Task Queue Manager worker processes to verify they have exited cleanly.This is for internal use only.

    See also [WORKER_SHUTDOWN_POLL_DELAY](config.md#worker-shutdown-poll-delay)

ANSIBLE_USE_PERSISTENT_CONNECTIONS
:   Toggles the use of persistence for connections.

    See also [USE_PERSISTENT_CONNECTIONS](config.md#use-persistent-connections)

ANSIBLE_VARS_ENABLED
:   Accept list for variable plugins that require it.

    See also [VARIABLE_PLUGINS_ENABLED](config.md#variable-plugins-enabled)

ANSIBLE_PRECEDENCE
:   Allows to change the group variable precedence merge order.

    See also [VARIABLE_PRECEDENCE](config.md#variable-precedence)

ANSIBLE_WIN_ASYNC_STARTUP_TIMEOUT
:   For asynchronous tasks in Ansible (covered in Asynchronous Actions and Polling), this is how long, in seconds, to wait for the task spawned by Ansible to connect back to the named pipe used on Windows systems. The default is 5 seconds. This can be too low on slower systems, or systems under heavy load.This is not the total time an async command can run for, but is a separate timeout to wait for an async command to start. The task will only start to be timed against its async_timeout once it has connected to the pipe, so the overall maximum duration the task can take will be extended by the amount specified here.

    See also [WIN_ASYNC_STARTUP_TIMEOUT](config.md#win-async-startup-timeout)

ANSIBLE_YAML_FILENAME_EXT
:   Check all of these extensions when looking for ‘variable’ files which should be YAML or JSON or vaulted versions of these.This affects vars_files, include_vars, inventory and vars plugins among others.

    See also [YAML_FILENAME_EXTENSIONS](config.md#yaml-filename-extensions)

ANSIBLE_NETCONF_SSH_CONFIG
:   This variable is used to enable bastion/jump host with netconf connection. If set to True the bastion/jump host ssh settings should be present in ~/.ssh/config file, alternatively it can be set to custom ssh configuration file path to read the bastion/jump host settings.

    See also [NETCONF_SSH_CONFIG](config.md#netconf-ssh-config)

ANSIBLE_STRING_CONVERSION_ACTION
:   Action to take when a module parameter value is converted to a string (this does not affect variables). For string parameters, values such as ‘1.00’, “[‘a’, ‘b’,]”, and ‘yes’, ‘y’, etc. will be converted by the YAML parser unless fully quoted.Valid options are ‘error’, ‘warn’, and ‘ignore’.Since 2.8, this option defaults to ‘warn’ but will change to ‘error’ in 2.12.

    See also [STRING_CONVERSION_ACTION](config.md#string-conversion-action)

ANSIBLE_VALIDATE_ACTION_GROUP_METADATA
:   A toggle to disable validating a collection’s ‘metadata’ entry for a module_defaults action group. Metadata containing unexpected fields or value types will produce a warning when this is True.

    See also [VALIDATE_ACTION_GROUP_METADATA](config.md#validate-action-group-metadata)

ANSIBLE_VERBOSE_TO_STDERR
:   Force ‘verbose’ option to use stderr instead of stdout

    See also [VERBOSE_TO_STDERR](config.md#verbose-to-stderr)
