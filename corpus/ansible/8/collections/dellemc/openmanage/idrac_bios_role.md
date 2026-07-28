---
collection: ansible
version: "8"
title: "dellemc.openmanage.idrac_bios role – Modify and clear BIOS attributes, and reset BIOS settings"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/openmanage/idrac_bios_role.html
fetched_at: 2026-07-28T02:04:59+00:00
---
# dellemc.openmanage.idrac_bios role – Modify and clear BIOS attributes, and reset BIOS settings

> **Note:**
>
> This role is part of the [dellemc.openmanage collection](https://galaxy.ansible.com/ui/repo/published/dellemc/openmanage/) (version 7.6.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it use: `ansible-galaxy collection install dellemc.openmanage`.
>
> To use it in a playbook, specify: `dellemc.openmanage.idrac_bios`.

- [Entry point `main` – Modify and clear BIOS attributes, and reset BIOS settings](idrac_bios_role.md#entry-point-main-modify-and-clear-bios-attributes-and-reset-bios-settings)

  - [Synopsis](idrac_bios_role.md#synopsis)
  - [Parameters](idrac_bios_role.md#parameters)

## [Entry point `main` – Modify and clear BIOS attributes, and reset BIOS settings](idrac_bios_role.md#id1)

New in dellemc.openmanage 7.6.0

### [Synopsis](idrac_bios_role.md#id2)

- This role allows to modify BIOS attributes, clear pending BIOS attributes, and reset the BIOS to default settings.

### [Parameters](idrac_bios_role.md#id3)

| Parameter | Comments |
| --- | --- |
| **apply_time**  string | Apply time of the *attributes*.  This is applicable only to *attributes*.  `Immediate` Allows the user to immediately reboot the host and apply the changes. *job_wait* is applicable.  `OnReset` Allows the user to apply the changes on the next reboot of the host server.  `AtMaintenanceWindowStart` Allows the user to apply the changes at the start of a maintenance window as specified in *maintenance_window*. A reboot job will be scheduled.  `InMaintenanceWindowOnReset` Allows to apply the changes after a manual reset but within the maintenance window as specified in *maintenance_window*.  **Choices:**   - `"Immediate"` ← (default) - `"OnReset"` - `"AtMaintenanceWindowStart"` - `"InMaintenanceWindowOnReset"` |
| **attributes**  dictionary | Dictionary of BIOS attributes and value pair. Attributes should be part of the Redfish Dell BIOS Attribute Registry. Use idrac_gather_facts role to fetch the BIOS attributes.  This is mutually exclusive with *reset_bios*. |
| **ca_path**  path | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **clear_pending**  boolean | Allows the user to clear all pending BIOS attributes changes.  `true` discards any pending changes to BIOS attributes or removes the job if in scheduled state.  This operation will not create any job.  `false` does not perform any operation.  This is mutually exclusive with *boot_sources*, *attributes*, and *reset_bios*.  `Note` Any BIOS job scheduled will not be cleared because of boot sources configuration.  **Choices:**   - `false` - `true` |
| **hostname**  string / required | iDRAC IP Address. |
| **https_port**  integer | iDRAC port.  **Default:** `443` |
| **https_timeout**  integer | The socket level timeout in seconds.  **Default:** `30` |
| **job_wait**  boolean | Provides the option to wait for job completion.  This is applicable for *attributes* when *apply_time* is `Immediate`.  **Choices:**   - `false` - `true` ← (default) |
| **job_wait_timeout**  integer | The maximum wait time of *job_wait* in seconds. The job is tracked only for this duration.  This option is applicable when *job_wait* is `true`.  **Default:** `1200` |
| **maintenance_window**  dictionary | Option to schedule the maintenance window.  This is required when *apply_time* is `AtMaintenanceWindowStart` or `InMaintenanceWindowOnReset`. |
| **duration**  integer / required | The duration in seconds for the maintenance window. |
| **start_time**  string / required | The start time for the maintenance window to be scheduled.  The format is YYYY-MM-DDThh:mm:ss<offset>  <offset> is the time offset from UTC that the current time zone set in iDRAC in the format: +05:30 for IST. |
| **password**  string / required | iDRAC user password. |
| **reset_bios**  boolean | Resets the BIOS to default settings and triggers a reboot of host system.  This is applied to the host after the restart.  This operation will not create any job.  `false` does not perform any operation.  This is mutually exclusive with *boot_sources*, *attributes*, and *clear_pending*.  When `true`, this action will always report as changes found to be applicable.  **Choices:**   - `false` - `true` |
| **reset_type**  string | `force_restart` Forcefully reboot the host system.  `graceful_restart` Gracefully reboot the host system.  This is applicable for *reset_bios*, and *attributes* when *apply_time* is `Immediate`.  **Choices:**   - `"graceful_restart"` ← (default) - `"force_restart"` |
| **username**  string / required | iDRAC username. |
| **validate_certs**  boolean | If `false`, the SSL certificates will not be validated.  Configure `false` only on personally controlled sites where self-signed certificates are used.  **Choices:**   - `false` - `true` ← (default) |

#### Collection links

- [Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
- [Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
- [Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
