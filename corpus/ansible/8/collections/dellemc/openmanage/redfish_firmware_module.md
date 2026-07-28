---
collection: ansible
version: "8"
title: "dellemc.openmanage.redfish_firmware module – To perform a component firmware update using the image file available on the local or remote system"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/openmanage/redfish_firmware_module.html
fetched_at: 2026-07-28T02:04:56+00:00
---
# dellemc.openmanage.redfish_firmware module – To perform a component firmware update using the image file available on the local or remote system

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
> see [Requirements](redfish_firmware_module.md#ansible-collections-dellemc-openmanage-redfish-firmware-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.openmanage.redfish_firmware`.

New in dellemc.openmanage 2.1.0

- [Synopsis](redfish_firmware_module.md#synopsis)
- [Requirements](redfish_firmware_module.md#requirements)
- [Parameters](redfish_firmware_module.md#parameters)
- [Notes](redfish_firmware_module.md#notes)
- [Examples](redfish_firmware_module.md#examples)
- [Return Values](redfish_firmware_module.md#return-values)

## [Synopsis](redfish_firmware_module.md#id1)

- This module allows the firmware update of only one component at a time. If the module is run for more than one component, an error message is returned.
- Depending on the component, the firmware update is applied after an automatic or manual reboot.

## [Requirements](redfish_firmware_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.8.6
- urllib3

## [Parameters](redfish_firmware_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **baseuri**  string / required | IP address of the target out-of-band controller. For example- <ipaddress>:<port>. |
| **ca_path**  path  *added in dellemc.openmanage 5.0.0* | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **image_uri**  string / required | Firmware Image location URI or local path.  For example- <http://%3Cweb_address%3E/components.exe> or /home/firmware_repo/component.exe. |
| **job_wait**  boolean | Provides the option to wait for job completion.  **Choices:**   - `false` - `true` ← (default) |
| **job_wait_timeout**  integer | The maximum wait time of *job_wait* in seconds. The job is tracked only for this duration.  This option is applicable when *job_wait* is `True`.  Note: If a firmware update needs a reboot, the job will get scheduled and waits for no of seconds specfied in *job_wait_time*. to reduce the wait time either give *job_wait_time* minimum or make *job_wait*as false and retrigger.  **Default:** `3600` |
| **password**  string / required | Password of the target out-of-band controller. |
| **timeout**  integer  *added in dellemc.openmanage 5.0.0* | The socket level timeout in seconds.  **Default:** `30` |
| **transfer_protocol**  string | Protocol used to transfer the firmware image file. Applicable for URI based update.  **Choices:**   - `"CIFS"` - `"FTP"` - `"HTTP"` ← (default) - `"HTTPS"` - `"NSF"` - `"OEM"` - `"SCP"` - `"SFTP"` - `"TFTP"` |
| **username**  string / required | Username of the target out-of-band controller. |
| **validate_certs**  boolean  *added in dellemc.openmanage 5.0.0* | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](redfish_firmware_module.md#id4)

> **Note:**
>
> - Run this module from a system that has direct access to Redfish APIs.
> - This module does not support `check_mode`.

## [Examples](redfish_firmware_module.md#id5)

```yaml+jinja
---
- name: Update the firmware from a single executable file available in a HTTP protocol
  dellemc.openmanage.redfish_firmware:
    baseuri: "192.168.0.1"
    username: "user_name"
    password: "user_password"
    ca_path: "/path/to/ca_cert.pem"
    image_uri: "http://192.168.0.2/firmware_repo/component.exe"
    transfer_protocol: "HTTP"

- name: Update the firmware from a single executable file available in a HTTP protocol with job_Wait
  dellemc.openmanage.redfish_firmware:
    baseuri: "192.168.0.1"
    username: "user_name"
    password: "user_password"
    ca_path: "/path/to/ca_cert.pem"
    image_uri: "http://192.168.0.2/firmware_repo/component.exe"
    transfer_protocol: "HTTP"
    job_wait: true
    job_wait_timeout: 600

- name: Update the firmware from a single executable file available in a local path
  dellemc.openmanage.redfish_firmware:
    baseuri: "192.168.0.1"
    username: "user_name"
    password: "user_password"
    ca_path: "/path/to/ca_cert.pem"
    image_uri: "/home/firmware_repo/component.exe"
```

## [Return Values](redfish_firmware_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **error_info**  dictionary | Details of http error.  **Returned:** on http error  **Sample:** `{"error": {"@Message.ExtendedInfo": [{"Message": "Unable to complete the operation because the JSON data format entered is invalid.", "Resolution": "Do the following and the retry the operation: 1) Enter the correct JSON data format and retry the operation. 2) Make sure that no syntax error is present in JSON data format. 3) Make sure that a duplicate key is not present in JSON data format.", "Severity": "Critical"}, {"Message": "The request body submitted was malformed JSON and could not be parsed by the receiving service.", "Resolution": "Ensure that the request body is valid JSON and resubmit the request.", "Severity": "Critical"}], "code": "Base.1.2.GeneralError", "message": "A general error has occurred. See ExtendedInfo for more information."}}` |
| **msg**  string | Overall status of the firmware update task.  **Returned:** always  **Sample:** `"Successfully updated the firmware."` |
| **task**  dictionary | Returns ID and URI of the created task.  **Returned:** success  **Sample:** `{"id": "JID_XXXXXXXXXXXX", "uri": "/redfish/v1/TaskService/Tasks/JID_XXXXXXXXXXXX"}` |

### Authors

- Felix Stephen (@felixs88)
- Husniya Hameed (@husniya_hameed)
- Shivam Sharma (@Shivam-Sharma)
- Kritika Bhateja (@Kritika_Bhateja)

### Collection links

- [Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
- [Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
- [Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
