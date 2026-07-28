---
collection: ansible
version: "8"
title: "community.general.nosh module – Manage services with nosh"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/nosh_module.html
fetched_at: 2026-07-28T01:48:11+00:00
---
# community.general.nosh module – Manage services with nosh

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](nosh_module.md#ansible-collections-community-general-nosh-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.nosh`.

- [Synopsis](nosh_module.md#synopsis)
- [Requirements](nosh_module.md#requirements)
- [Parameters](nosh_module.md#parameters)
- [Attributes](nosh_module.md#attributes)
- [Notes](nosh_module.md#notes)
- [Examples](nosh_module.md#examples)
- [Return Values](nosh_module.md#return-values)

## [Synopsis](nosh_module.md#id1)

- Control running and enabled state for system-wide or user services.
- BSD and Linux systems are supported.

Aliases: system.nosh

## [Requirements](nosh_module.md#id2)

The below requirements are needed on the host that executes this module.

- A system with an active nosh service manager, see Notes for further information.

## [Parameters](nosh_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **enabled**  boolean | Enable or disable the service, independently of `*.preset` file preference or running state. Mutually exclusive with `preset`. Will take effect prior to `state=reset`.  **Choices:**   - `false` - `true` |
| **name**  string / required | Name of the service to manage. |
| **preset**  boolean | Enable or disable the service according to local preferences in `*.preset` files. Mutually exclusive with `enabled`. Only has an effect if set to true. Will take effect prior to `state=reset`.  **Choices:**   - `false` - `true` |
| **state**  string | `started`/`stopped` are idempotent actions that will not run commands unless necessary. `restarted` will always bounce the service. `reloaded` will send a SIGHUP or start the service. `reset` will start or stop the service according to whether it is enabled or not.  **Choices:**   - `"started"` - `"stopped"` - `"reset"` - `"restarted"` - `"reloaded"` |
| **user**  boolean | Run system-control talking to the calling user’s service manager, rather than the system-wide service manager.  **Choices:**   - `false` ← (default) - `true` |

## [Attributes](nosh_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](nosh_module.md#id5)

> **Note:**
>
> - Information on the nosh utilities suite may be found at <https://jdebp.eu/Softwares/nosh/>.

## [Examples](nosh_module.md#id6)

```yaml+jinja
- name: Start dnscache if not running
  community.general.nosh:
    name: dnscache
    state: started

- name: Stop mpd, if running
  community.general.nosh:
    name: mpd
    state: stopped

- name: Restart unbound or start it if not already running
  community.general.nosh:
    name: unbound
    state: restarted

- name: Reload fail2ban or start it if not already running
  community.general.nosh:
    name: fail2ban
    state: reloaded

- name: Disable nsd
  community.general.nosh:
    name: nsd
    enabled: false

- name: For package installers, set nginx running state according to local enable settings, preset and reset
  community.general.nosh:
    name: nginx
    preset: true
    state: reset

- name: Reboot the host if nosh is the system manager, would need a "wait_for*" task at least, not recommended as-is
  community.general.nosh:
    name: reboot
    state: started

- name: Using conditionals with the module facts
  tasks:
    - name: Obtain information on tinydns service
      community.general.nosh:
        name: tinydns
      register: result

    - name: Fail if service not loaded
      ansible.builtin.fail:
        msg: "The {{ result.name }} service is not loaded"
      when: not result.status

    - name: Fail if service is running
      ansible.builtin.fail:
        msg: "The {{ result.name }} service is running"
      when: result.status and result.status['DaemontoolsEncoreState'] == "running"
```

## [Return Values](nosh_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **enabled**  boolean | whether the service is enabled at system bootstrap  **Returned:** success  **Sample:** `true` |
| **name**  string | name used to find the service  **Returned:** success  **Sample:** `"sshd"` |
| **preset**  boolean | whether the enabled status reflects the one set in the relevant `*.preset` file  **Returned:** success  **Sample:** `false` |
| **service_path**  string | resolved path for the service  **Returned:** success  **Sample:** `"/var/sv/sshd"` |
| **state**  string | service process run state, `none` if the service is not loaded and will not be started  **Returned:** if state option is used  **Sample:** `"reloaded"` |
| **status**  complex | A dictionary with the key=value pairs returned by `system-control show-json` or `none` if the service is not loaded  **Returned:** success |
| **After**  list / elements=string | **Returned:** success  **Sample:** `["/etc/service-bundles/targets/basic", "../sshdgenkeys", "log"]` |
| **Before**  list / elements=string | **Returned:** success  **Sample:** `["/etc/service-bundles/targets/shutdown"]` |
| **Conflicts**  list / elements=string | **Returned:** success  **Sample:** `[]` |
| **DaemontoolsEncoreState**  string | **Returned:** success  **Sample:** `"running"` |
| **DaemontoolsState**  string | **Returned:** success  **Sample:** `"up"` |
| **Enabled**  boolean | **Returned:** success  **Sample:** `true` |
| **LogService**  string | **Returned:** success  **Sample:** `"../cyclog@sshd"` |
| **MainPID**  integer | **Returned:** success  **Sample:** `661` |
| **Paused**  boolean | **Returned:** success  **Sample:** `false` |
| **ReadyAfterRun**  boolean | **Returned:** success  **Sample:** `false` |
| **RemainAfterExit**  boolean | **Returned:** success  **Sample:** `false` |
| **Required-By**  list / elements=string | **Returned:** success  **Sample:** `[]` |
| **RestartExitStatusCode**  integer | **Returned:** success  **Sample:** `0` |
| **RestartExitStatusNumber**  integer | **Returned:** success  **Sample:** `0` |
| **RestartTimestamp**  integer | **Returned:** success  **Sample:** `4611686019935648081` |
| **RestartUTCTimestamp**  integer | **Returned:** success  **Sample:** `1508260140` |
| **RunExitStatusCode**  integer | **Returned:** success  **Sample:** `0` |
| **RunExitStatusNumber**  integer | **Returned:** success  **Sample:** `0` |
| **RunTimestamp**  integer | **Returned:** success  **Sample:** `4611686019935648081` |
| **RunUTCTimestamp**  integer | **Returned:** success  **Sample:** `1508260140` |
| **StartExitStatusCode**  integer | **Returned:** success  **Sample:** `1` |
| **StartExitStatusNumber**  integer | **Returned:** success  **Sample:** `0` |
| **StartTimestamp**  integer | **Returned:** success  **Sample:** `4611686019935648081` |
| **StartUTCTimestamp**  integer | **Returned:** success  **Sample:** `1508260140` |
| **StopExitStatusCode**  integer | **Returned:** success  **Sample:** `0` |
| **StopExitStatusNumber**  integer | **Returned:** success  **Sample:** `0` |
| **Stopped-By**  list / elements=string | **Returned:** success  **Sample:** `["/etc/service-bundles/targets/shutdown"]` |
| **StopTimestamp**  integer | **Returned:** success  **Sample:** `4611686019935648081` |
| **StopUTCTimestamp**  integer | **Returned:** success  **Sample:** `1508260140` |
| **Timestamp**  integer | **Returned:** success  **Sample:** `4611686019935648081` |
| **UTCTimestamp**  integer | **Returned:** success  **Sample:** `1508260140` |
| **Want**  string | **Returned:** success  **Sample:** `"nothing"` |
| **Wanted-By**  list / elements=string | **Returned:** success  **Sample:** `["/etc/service-bundles/targets/server", "/etc/service-bundles/targets/sockets"]` |
| **Wants**  list / elements=string | **Returned:** success  **Sample:** `["/etc/service-bundles/targets/basic", "../sshdgenkeys"]` |
| **user**  boolean | whether the user-level service manager is called  **Returned:** success  **Sample:** `false` |

### Authors

- Thomas Caravia (@tacatac)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
