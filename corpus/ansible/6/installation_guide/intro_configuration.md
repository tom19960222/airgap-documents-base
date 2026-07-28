---
collection: ansible
version: "6"
title: "Configuring Ansible"
source_url: https://docs.ansible.com/projects/ansible/6/installation_guide/intro_configuration.html
fetched_at: 2026-07-27T16:39:39+00:00
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

Certain settings in Ansible are adjustable via a configuration file (ansible.cfg).
The stock configuration should be sufficient for most users, but there may be reasons you would want to change them.
Paths where configuration file is searched are listed in [reference documentation](../reference_appendices/config.md#ansible-configuration-settings-locations).

### [Getting the latest configuration](intro_configuration.md#id5)

If installing Ansible from a package manager, the latest `ansible.cfg` file should be present in `/etc/ansible`, possibly
as a `.rpmnew` file (or other) as appropriate in the case of updates.

If you installed Ansible from pip or from source, you may want to create this file in order to override
default settings in Ansible.

An [example file is available on GitHub](https://github.com/ansible/ansible/blob/devel/examples/ansible.cfg).

For more details and a full listing of available configurations go to [configuration_settings](../reference_appendices/config.md#ansible-configuration-settings). Starting with Ansible version 2.4, you can use the [ansible-config](../cli/ansible-config.md#ansible-config) command line utility to list your available options and inspect the current values.

For in-depth details, see [Ansible Configuration Settings](../reference_appendices/config.md#ansible-configuration-settings).

## [Environmental configuration](intro_configuration.md#id6)

Ansible also allows configuration of settings using environment variables.
If these environment variables are set, they will override any setting loaded from the configuration file.

You can get a full listing of available environment variables from [Ansible Configuration Settings](../reference_appendices/config.md#ansible-configuration-settings).

## [Command line options](intro_configuration.md#id7)

Not all configuration options are present in the command line, just the ones deemed most useful or common.
Settings in the command line will override those passed through the configuration file and the environment.

The full list of options available is in [ansible-playbook](../cli/ansible-playbook.md#ansible-playbook) and [ansible](../cli/ansible.md#ansible).
