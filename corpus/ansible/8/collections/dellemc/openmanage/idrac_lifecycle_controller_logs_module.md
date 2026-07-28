---
collection: ansible
version: "8"
title: "dellemc.openmanage.idrac_lifecycle_controller_logs module – Export Lifecycle Controller logs to a network share or local path."
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/openmanage/idrac_lifecycle_controller_logs_module.html
fetched_at: 2026-07-28T02:04:07+00:00
---
# dellemc.openmanage.idrac_lifecycle_controller_logs module – Export Lifecycle Controller logs to a network share or local path.

> **Note:**
>
> This module is part of the [dellemc.openmanage collection](https://galaxy.ansible.com/ui/repo/published/dellemc/openmanage/) (version 7.6.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install dellemc.openmanage`.
> You need further requirements to be able to use this module,
> see [Requirements](idrac_lifecycle_controller_logs_module.md#ansible-collections-dellemc-openmanage-idrac-lifecycle-controller-logs-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.openmanage.idrac_lifecycle_controller_logs`.

New in dellemc.openmanage 2.1.0

- [Synopsis](idrac_lifecycle_controller_logs_module.md#synopsis)
- [Requirements](idrac_lifecycle_controller_logs_module.md#requirements)
- [Parameters](idrac_lifecycle_controller_logs_module.md#parameters)
- [Notes](idrac_lifecycle_controller_logs_module.md#notes)
- [Examples](idrac_lifecycle_controller_logs_module.md#examples)
- [Return Values](idrac_lifecycle_controller_logs_module.md#return-values)

## [Synopsis](idrac_lifecycle_controller_logs_module.md#id1)

- Export Lifecycle Controller logs to a given network share or local path.

## [Requirements](idrac_lifecycle_controller_logs_module.md#id2)

The below requirements are needed on the host that executes this module.

- omsdk >= 1.2.488
- python >= 3.9.6

## [Parameters](idrac_lifecycle_controller_logs_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_path**  path  *added in dellemc.openmanage 5.0.0* | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **idrac_ip**  string / required | iDRAC IP Address. |
| **idrac_password**  aliases: idrac_pwd  string / required | iDRAC user password. |
| **idrac_port**  integer | iDRAC port.  **Default:** `443` |
| **idrac_user**  string / required | iDRAC username. |
| **job_wait**  boolean | Whether to wait for the running job completion or not.  **Choices:**   - `false` - `true` ← (default) |
| **share_name**  string / required | Network share or local path.  CIFS, NFS network share types are supported. |
| **share_password**  aliases: share_pwd  string | Network share user password. This option is mandatory for CIFS Network Share. |
| **share_user**  string | Network share user in the format [‘user@domain](mailto:'user%40domain)’ or ‘domain\user’ if user is part of a domain else ‘user’. This option is mandatory for CIFS Network Share. |
| **timeout**  integer  *added in dellemc.openmanage 5.0.0* | The socket level timeout in seconds.  **Default:** `30` |
| **validate_certs**  boolean  *added in dellemc.openmanage 5.0.0* | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](idrac_lifecycle_controller_logs_module.md#id4)

> **Note:**
>
> - This module requires ‘Administrator’ privilege for *idrac_user*.
> - Exporting data to a local share is supported only on iDRAC9-based PowerEdge Servers and later.
> - Run this module from a system that has direct access to Dell iDRAC.
> - This module supports both IPv4 and IPv6 address for *idrac_ip*.
> - This module does not support `check_mode`.

## [Examples](idrac_lifecycle_controller_logs_module.md#id5)

```yaml+jinja
---
- name: Export lifecycle controller logs to NFS share.
  dellemc.openmanage.idrac_lifecycle_controller_logs:
    idrac_ip: "190.168.0.1"
    idrac_user: "user_name"
    idrac_password: "user_password"
    ca_path: "/path/to/ca_cert.pem"
    share_name: "192.168.0.0:/nfsfileshare"

- name: Export lifecycle controller logs to CIFS share.
  dellemc.openmanage.idrac_lifecycle_controller_logs:
    idrac_ip: "190.168.0.1"
    idrac_user: "user_name"
    idrac_password: "user_password"
    ca_path: "/path/to/ca_cert.pem"
    share_name: "\\\\192.168.0.2\\share"
    share_user: "share_user_name"
    share_password: "share_user_pwd"

- name: Export lifecycle controller logs to LOCAL path.
  dellemc.openmanage.idrac_lifecycle_controller_logs:
    idrac_ip: "190.168.0.1"
    idrac_user: "user_name"
    idrac_password: "user_password"
    ca_path: "/path/to/ca_cert.pem"
    share_name: "/example/export_lc"
```

## [Return Values](idrac_lifecycle_controller_logs_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **error_info**  dictionary | Details of the HTTP Error.  **Returned:** on HTTP error  **Sample:** `{"error": {"@Message.ExtendedInfo": [{"Message": "Unable to process the request because an error occurred.", "MessageArgs": [], "MessageId": "GEN1234", "RelatedProperties": [], "Resolution": "Retry the operation. If the issue persists, contact your system administrator.", "Severity": "Critical"}], "code": "Base.1.0.GeneralError", "message": "A general error has occurred. See ExtendedInfo for more information."}}` |
| **lc_logs_status**  dictionary | Status of the export operation along with job details and file path.  **Returned:** success  **Sample:** `{"ElapsedTimeSinceCompletion": "0", "InstanceID": "JID_274774785395", "JobStartTime": "NA", "JobStatus": "Completed", "JobUntilTime": "NA", "Message": "LCL Export was successful", "MessageArguments": "NA", "MessageID": "LC022", "Name": "LC Export", "PercentComplete": "100", "Status": "Success", "file": "192.168.0.0:/nfsfileshare/190.168.0.1_20210728_133437_LC_Log.log", "retval": true}` |
| **msg**  string | Status of the export lifecycle controller logs job.  **Returned:** always  **Sample:** `"Successfully exported the lifecycle controller logs."` |

### Authors

- Rajeev Arakkal (@rajeevarakkal)
- Anooja Vardhineni (@anooja-vardhineni)

### Collection links

- [Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
- [Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
- [Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
