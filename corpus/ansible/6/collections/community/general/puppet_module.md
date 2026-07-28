---
collection: ansible
version: "6"
title: "community.general.puppet module – Runs puppet"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/puppet_module.html
fetched_at: 2026-07-27T17:12:15+00:00
---
# community.general.puppet module – Runs puppet

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](puppet_module.md#ansible-collections-community-general-puppet-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.puppet`.

- [Synopsis](puppet_module.md#synopsis)
- [Requirements](puppet_module.md#requirements)
- [Parameters](puppet_module.md#parameters)
- [Examples](puppet_module.md#examples)

## [Synopsis](puppet_module.md#id2)

- Runs *puppet* agent or apply in a reliable manner.

## [Requirements](puppet_module.md#id3)

The below requirements are needed on the host that executes this module.

- puppet

## [Parameters](puppet_module.md#id4)

| Parameter | Comments |
| --- | --- |
| **certname**  string | The name to use when handling certificates. |
| **confdir**  string  added in community.general 5.1.0 | Path to the directory containing the puppet.conf file. |
| **debug**  boolean | Enable full debugging.  Choices:   - `false` ← (default) - `true` |
| **environment**  string | Puppet environment to be used. |
| **execute**  string | Execute a specific piece of Puppet code.  It has no effect with a puppetmaster. |
| **facter_basename**  string | Basename of the facter output file.  Default: `"ansible"` |
| **facts**  dictionary | A dict of values to pass in as persistent external facter facts. |
| **logdest**  string | Where the puppet logs should go, if puppet apply is being used.  `all` will go to both `console` and `syslog`.  `stdout` will be deprecated and replaced by `console`.  Choices:   - `"all"` - `"stdout"` ← (default) - `"syslog"` |
| **manifest**  string | Path to the manifest file to run puppet apply on. |
| **modulepath**  string | Path to an alternate location for puppet modules. |
| **noop**  boolean | Override puppet.conf noop mode.  When `true`, run Puppet agent with `--noop` switch set.  When `false`, run Puppet agent with `--no-noop` switch set.  When unset (default), use default or puppet.conf value if defined.  Choices:   - `false` - `true` |
| **puppetmaster**  string | The hostname of the puppetmaster to contact. |
| **show_diff**  aliases: show-diff  boolean | Whether to print file changes details  Alias `show-diff` has been deprecated and will be removed in community.general 7.0.0.  Choices:   - `false` ← (default) - `true` |
| **summarize**  boolean | Whether to print a transaction summary.  Choices:   - `false` ← (default) - `true` |
| **tags**  list / elements=string | A list of puppet tags to be used. |
| **timeout**  string | How long to wait for *puppet* to finish.  Default: `"30m"` |
| **use_srv_records**  boolean | Toggles use_srv_records flag  Choices:   - `false` - `true` |
| **verbose**  boolean | Print extra information.  Choices:   - `false` ← (default) - `true` |

## [Examples](puppet_module.md#id5)

```yaml+jinja
- name: Run puppet agent and fail if anything goes wrong
  community.general.puppet:

- name: Run puppet and timeout in 5 minutes
  community.general.puppet:
    timeout: 5m

- name: Run puppet using a different environment
  community.general.puppet:
    environment: testing

- name: Run puppet using a specific certname
  community.general.puppet:
    certname: agent01.example.com

- name: Run puppet using a specific piece of Puppet code. Has no effect with a puppetmaster
  community.general.puppet:
    execute: include ::mymodule

- name: Run puppet using a specific tags
  community.general.puppet:
    tags:
    - update
    - nginx

- name: Run puppet agent in noop mode
  community.general.puppet:
    noop: true

- name: Run a manifest with debug, log to both syslog and console, specify module path
  community.general.puppet:
    modulepath: /etc/puppet/modules:/opt/stack/puppet-modules:/usr/share/openstack-puppet/modules
    logdest: all
    manifest: /var/lib/example/puppet_step_config.pp
```

### Authors

- Monty Taylor (@emonty)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
