---
collection: ansible
version: "6"
title: "sensu.sensu_go.agent role – Install, configure, and start Sensu Go agent"
source_url: https://docs.ansible.com/projects/ansible/6/collections/sensu/sensu_go/agent_role.html
fetched_at: 2026-07-28T00:19:53+00:00
---
# sensu.sensu_go.agent role – Install, configure, and start Sensu Go agent

> **Note:**
>
> This role is part of the [sensu.sensu_go collection](https://galaxy.ansible.com/sensu/sensu_go) (version 1.13.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it use: `ansible-galaxy collection install sensu.sensu_go`.
>
> To use it in a playbook, specify: `sensu.sensu_go.agent`.

- [Entry point `configure` – Configure Sensu Go agent](agent_role.md#entry-point-configure-configure-sensu-go-agent)

  - [Synopsis](agent_role.md#synopsis)
  - [Parameters](agent_role.md#parameters)
- [Entry point `main` – Install, configure, and start Sensu Go agent](agent_role.md#entry-point-main-install-configure-and-start-sensu-go-agent)

  - [Synopsis](agent_role.md#id1)
  - [Parameters](agent_role.md#id2)
- [Entry point `start` – Start Sensu Go agent](agent_role.md#entry-point-start-start-sensu-go-agent)

  - [Synopsis](agent_role.md#id3)

## [Entry point `configure` – Configure Sensu Go agent](agent_role.md#id4)

### [Synopsis](agent_role.md#id5)

- Write the Sensu Go agent configuration file.

### [Parameters](agent_role.md#id6)

| Parameter | Comments |
| --- | --- |
| **agent_config**  dictionary | Any option that is valid for the Sensu Go agent version we are installing.  All valid options are listed at <https://docs.sensu.io/sensu-go/latest/reference/agent/#configuration>.  Role copies the key-value pairs from the *agent_config* variable verbatim to the configuration file. This means that we must copy the key names **exactly** as they appear in the configuration reference. In a way, the *agent_config* variable should contain a properly indented copy of the `/etc/sensu/agent.yml` file. |

## [Entry point `main` – Install, configure, and start Sensu Go agent](agent_role.md#id7)

### [Synopsis](agent_role.md#id8)

- Install, configure, and start the Sensu Go agent service.

### [Parameters](agent_role.md#id9)

| Parameter | Comments |
| --- | --- |
| **agent_config**  dictionary | Any option that is valid for the Sensu Go agent version we are installing.  All valid options are listed at <https://docs.sensu.io/sensu-go/latest/reference/agent/#configuration>.  Role copies the key-value pairs from the *agent_config* variable verbatim to the configuration file. This means that we must copy the key names **exactly** as they appear in the configuration reference. In a way, the *agent_config* variable should contain a properly indented copy of the `/etc/sensu/agent.yml` file. |
| **build**  string | Package build to install.  Can be any valid build string such as `8290` or a special value latest.  If the *version* variable is set to latest, this variable is ignored and the latest available build is installed.  Default: `"latest"` |
| **channel**  string | Repository channel that serves as a source of packages.  Visit the packagecloud site to find all available channels.  Default: `"stable"` |
| **version**  string | Package version to install.  Can be any valid version string such as `6.2.5` or special value `latest`.  Default: `"latest"` |

## [Entry point `start` – Start Sensu Go agent](agent_role.md#id10)

### [Synopsis](agent_role.md#id11)

- Start the Sensu Go agent service.

#### Collection links

[Issue Tracker](https://github.com/sensu/sensu-go-ansible/issues)
[Repository (Sources)](https://github.com/sensu/sensu-go-ansible)
