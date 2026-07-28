---
collection: ansible
version: "8"
title: "sensu.sensu_go.install role – Enable Sensu Go repos and install selected packages"
source_url: https://docs.ansible.com/projects/ansible/8/collections/sensu/sensu_go/install_role.html
fetched_at: 2026-07-28T01:05:26+00:00
---
# sensu.sensu_go.install role – Enable Sensu Go repos and install selected packages

> **Note:**
>
> This role is part of the [sensu.sensu_go collection](https://galaxy.ansible.com/ui/repo/published/sensu/sensu_go/) (version 1.14.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it use: `ansible-galaxy collection install sensu.sensu_go`.
>
> To use it in a playbook, specify: `sensu.sensu_go.install`.

- [Entry point `main` – Enable Sensu Go repos and install selected packages](install_role.md#entry-point-main-enable-sensu-go-repos-and-install-selected-packages)

  - [Synopsis](install_role.md#synopsis)
  - [Parameters](install_role.md#parameters)
- [Entry point `packages` – Install selected Sensu Go packages](install_role.md#entry-point-packages-install-selected-sensu-go-packages)

  - [Synopsis](install_role.md#id1)
  - [Parameters](install_role.md#id2)
- [Entry point `repositories` – Enable Sensu Go repos](install_role.md#entry-point-repositories-enable-sensu-go-repos)

  - [Synopsis](install_role.md#id3)
  - [Parameters](install_role.md#id4)

## [Entry point `main` – Enable Sensu Go repos and install selected packages](install_role.md#id5)

### [Synopsis](install_role.md#id6)

- The main entry point just combines the repositories and packages entry points.

### [Parameters](install_role.md#id7)

| Parameter | Comments |
| --- | --- |
| **build**  string | Package build to install.  Can be any valid build string such as `8290` or a special value latest.  If the *version* variable is set to latest, this variable is ignored and the latest available build is installed.  **Default:** `"latest"` |
| **channel**  string | Repository channel that serves as a source of packages.  Visit the packagecloud site to find all available channels.  **Default:** `"stable"` |
| **components**  list / elements=string | List of components to install.  **Choices:**   - `"sensu-go-backend"` ← (default) - `"sensu-go-agent"` ← (default) - `"sensu-go-cli"` ← (default)   **Default:** `["sensu-go-backend", "sensu-go-agent", "sensu-go-cli"]` |
| **version**  string | Package version to install.  Can be any valid version string such as `6.2.5` or special value `latest`.  **Default:** `"latest"` |

## [Entry point `packages` – Install selected Sensu Go packages](install_role.md#id8)

### [Synopsis](install_role.md#id9)

- Make sure selected packages are installed.
- By default, the role will install latest available package version. This will change in the next major version of the collection where the *version* will become a required variable.

### [Parameters](install_role.md#id10)

| Parameter | Comments |
| --- | --- |
| **build**  string | Package build to install.  Can be any valid build string such as `8290` or a special value latest.  If the *version* variable is set to latest, this variable is ignored and the latest available build is installed.  **Default:** `"latest"` |
| **components**  list / elements=string | List of components to install.  **Choices:**   - `"sensu-go-backend"` ← (default) - `"sensu-go-agent"` ← (default) - `"sensu-go-cli"` ← (default)   **Default:** `["sensu-go-backend", "sensu-go-agent", "sensu-go-cli"]` |
| **version**  string | Package version to install.  Can be any valid version string such as `6.2.5` or special value `latest`.  **Default:** `"latest"` |

## [Entry point `repositories` – Enable Sensu Go repos](install_role.md#id11)

### [Synopsis](install_role.md#id12)

- Install required repository files on supported distributions.
- This entry point does not work on Windows because there is no concept of repository there.

### [Parameters](install_role.md#id13)

| Parameter | Comments |
| --- | --- |
| **channel**  string | Repository channel that serves as a source of packages.  Visit the packagecloud site to find all available channels.  **Default:** `"stable"` |

#### Collection links

- [Issue Tracker](https://github.com/sensu/sensu-go-ansible/issues)
- [Repository (Sources)](https://github.com/sensu/sensu-go-ansible)
