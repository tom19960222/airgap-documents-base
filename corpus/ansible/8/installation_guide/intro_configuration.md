---
collection: ansible
version: "8"
title: "Configuring Ansible"
source_url: https://docs.ansible.com/projects/ansible/8/installation_guide/intro_configuration.html
fetched_at: 2026-07-28T00:58:15+00:00
---
# [Configuring Ansible](intro_configuration.md#id3)

Topics

- [Configuring Ansible](intro_configuration.md#configuring-ansible)

  - [Configuration file](intro_configuration.md#configuration-file)

    - [Getting the latest configuration](intro_configuration.md#getting-the-latest-configuration)
  - [Environmental configuration](intro_configuration.md#environmental-configuration)
  - [Command line options](intro_configuration.md#command-line-options)

This topic describes how to control Ansible settings.

## [Configuration file](intro_configuration.md#id4)

Certain settings in Ansible are adjustable with a configuration file (`ansible.cfg`).
The stock configuration should be sufficient for most users, but there may be reasons you would want to change them.

Paths where the configuration file is searched are listed in [reference documentation](../reference_appendices/config.md#ansible-configuration-settings-locations).

### [Getting the latest configuration](intro_configuration.md#id5)

If installing Ansible from a package manager, the latest `ansible.cfg` file should be present in `/etc/ansible`, possibly
as a `.rpmnew` file (or other) as appropriate in the case of updates.

If you installed Ansible from `pip` or from the source, you may want to create this file in order to override
default settings in Ansible.

You can generate an Ansible configuration file, `ansible.cfg`, that lists all default settings as follows:

```console
$ ansible-config init --disabled > ansible.cfg
```

Include available plugins to create a more complete Ansible configuration as follows:

```console
$ ansible-config init --disabled -t all > ansible.cfg
```

For more details and a full listing of available configurations go to [configuration_settings](../reference_appendices/config.md#ansible-configuration-settings).

You can use the [ansible-config](../cli/ansible-config.md#ansible-config) command-line utility to list your available options and inspect the current values.

For in-depth details, see [Ansible Configuration Settings](../reference_appendices/config.md#ansible-configuration-settings).

## [Environmental configuration](intro_configuration.md#id6)

Ansible also allows configuring settings using environment variables.
If these environment variables are set, they will override any associated settings loaded from the configuration file.
You can get a full listing of available environment variables from:

- [Ansible Configuration Settings](../reference_appendices/config.md#ansible-configuration-settings): for configuring core functionality
- [Index of all Collection Environment Variables](../collections/environment_variables.md#list-of-collection-env-vars): for configuring plugins in collections

## [Command line options](intro_configuration.md#id7)

Not all configuration options are present in the command line, just the ones deemed most useful or common.
Settings in the command line will override those passed through the configuration file and the environment.

The full list of options available is in [ansible-playbook](../cli/ansible-playbook.md#ansible-playbook) and [ansible](../cli/ansible.md#ansible).
