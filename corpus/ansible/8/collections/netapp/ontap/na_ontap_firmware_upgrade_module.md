---
collection: ansible
version: "8"
title: "netapp.ontap.na_ontap_firmware_upgrade module – NetApp ONTAP firmware upgrade for SP, shelf, ACP, and disk."
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp/ontap/na_ontap_firmware_upgrade_module.html
fetched_at: 2026-07-28T02:42:10+00:00
---
# netapp.ontap.na_ontap_firmware_upgrade module – NetApp ONTAP firmware upgrade for SP, shelf, ACP, and disk.

> **Note:**
>
> This module is part of the [netapp.ontap collection](https://galaxy.ansible.com/ui/repo/published/netapp/ontap/) (version 22.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netapp.ontap`.
> You need further requirements to be able to use this module,
> see [Requirements](na_ontap_firmware_upgrade_module.md#ansible-collections-netapp-ontap-na-ontap-firmware-upgrade-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.ontap.na_ontap_firmware_upgrade`.

New in netapp.ontap 2.9.0

- [Synopsis](na_ontap_firmware_upgrade_module.md#synopsis)
- [Requirements](na_ontap_firmware_upgrade_module.md#requirements)
- [Parameters](na_ontap_firmware_upgrade_module.md#parameters)
- [Notes](na_ontap_firmware_upgrade_module.md#notes)
- [Examples](na_ontap_firmware_upgrade_module.md#examples)
- [Return Values](na_ontap_firmware_upgrade_module.md#return-values)

## [Synopsis](na_ontap_firmware_upgrade_module.md#id1)

- Update ONTAP service-prosessor firmware
- The recommend procedure is to 1. download the firmware package from the NetApp Support site 2. copy the package to a web server 3. download the package from the web server using this module
- Once a disk qualification, disk, shelf, or ACP firmware package is downloaded, ONTAP will automatically update the related resources in background.
- It may take some time to complete.
- For service processor, the update requires a node reboot to take effect.

## [Requirements](na_ontap_firmware_upgrade_module.md#id2)

The below requirements are needed on the host that executes this module.

- Ansible 2.9 or later - 2.12 or later is recommended.
- Python3 - 3.9 or later is recommended.
- When using ZAPI, netapp-lib 2018.11.13 or later (install using ‘pip install netapp-lib’), netapp-lib 2020.3.12 is strongly recommended as it provides better error reporting for connection issues
- a physical or virtual clustered Data ONTAP system, the modules support Data ONTAP 9.1 and onward, REST support requires ONTAP 9.6 or later

## [Parameters](na_ontap_firmware_upgrade_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **cert_filepath**  string  *added in netapp.ontap 20.6.0* | path to SSL client cert file (.pem).  not supported with python 2.6. |
| **clear_logs**  boolean | Clear logs on the device after update. Default value is true.  Not used if force_disruptive_update is False.  Not supported with REST when set to false.  **Choices:**   - `false` - `true` ← (default) |
| **disk_fw**  string | disk firmware to be updated to.  Not used if force_disruptive_update is False (ONTAP will automatically select the firmware)  Not supported with REST. |
| **fail_on_502_error**  boolean  *added in netapp.ontap 20.6.0* | The firmware download may take time if the web server is slow and if there are many nodes in the cluster.  ONTAP will break the ZAPI connection after 5 minutes with a 502 Bad Gateway error, even though the download is still happening.  By default, this module ignores this error and assumes the download is progressing as ONTAP does not provide a way to check the status.  When setting this option to true, the module will report 502 as an error.  Not supported with REST when set to true.  **Choices:**   - `false` ← (default) - `true` |
| **feature_flags**  dictionary  *added in netapp.ontap 20.5.0* | Enable or disable a new feature.  This can be used to enable an experimental feature or disable a new feature that breaks backward compatibility.  Supported keys and values are subject to change without notice. Unknown keys are ignored. |
| **firmware_type**  string | Type of firmware to be upgraded. Options include shelf, ACP, service-processor, and disk.  For shelf firmware upgrade the operation is asynchronous, and therefore returns no errors that might occur during the download process.  Shelf firmware upgrade is idempotent if shelf_module_fw is provided .  disk firmware upgrade is idempotent if disk_fw is provided .  With check mode, SP, ACP, disk, and shelf firmware upgrade is not idempotent.  This operation will only update firmware on shelves/disk that do not have the latest firmware-revision.  For normal operations, choose one of storage or service-processor.  Type storage includes acp, shelf and disk and ONTAP will automatically determine what to do.  With REST, the module does not validate that the package matches the firmware type. ONTAP determines the type automatically.  With REST, `storage` downloads any firmware, including service-processor firmware.  With REST, `service-processor` unlocks SP reboot options.  **Choices:**   - `"storage"` ← (default) - `"service-processor"` - `"shelf"` - `"acp"` - `"disk"` |
| **force_disruptive_update**  boolean  *added in netapp.ontap 20.5.0* | If set to `False`, and URL is given, the upgrade is non disruptive. If URL is not given, no operation is performed.  Do not set this to `True`, unless directed by NetApp Tech Support.  It will force an update even if the resource is not ready for it, and can be disruptive.  Not supported with REST when set to true.  **Choices:**   - `false` ← (default) - `true` |
| **force_ontap_version**  string  *added in netapp.ontap 21.23.0* | Override the cluster ONTAP version when using REST.  The behavior is undefined if the version does not match the target cluster.  This is provided as a work-around when the cluster version cannot be read because of permission issues. See <https://github.com/ansible-collections/netapp.ontap/wiki/Known-issues>.  This should be in the form 9.10 or 9.10.1 with each element being an integer number.  When `use_rest` is set to auto, this may force a switch to ZAPI based on the version and platform capabilities.  Ignored with ZAPI. |
| **hostname**  string / required | The hostname or IP address of the ONTAP instance. |
| **http_port**  integer | Override the default port (80 or 443) with this port |
| **https**  boolean | Enable and disable https.  Ignored when using REST as only https is supported.  Ignored when using SSL certificate authentication as it requires SSL.  **Choices:**   - `false` ← (default) - `true` |
| **install_baseline_image**  boolean | Install the version packaged with ONTAP if this parameter is set to true. Otherwise, package must be used to specify the package to install.  Not used if force_disruptive_update is False (ONTAP will automatically select the firmware)  Not supported with REST when set to true.  **Choices:**   - `false` ← (default) - `true` |
| **key_filepath**  string  *added in netapp.ontap 20.6.0* | path to SSL client key file. |
| **node**  string | Node on which the device is located.  Not required if package_url is present and force_disruptive_update is False.  If this option is not given, the firmware will be downloaded on all nodes in the cluster,  and the resources will be updated in background on all nodes, except for service processor.  For service processor, the upgrade will happen automatically when each node is rebooted. |
| **ontapi**  integer | The ontap api version to use |
| **package**  string | Name of the package file containing the firmware to be installed. Not required when -baseline is true.  Not used if force_disruptive_update is False.  Not supported with REST. |
| **package_url**  string  *added in netapp.ontap 20.5.0* | URL of the package file containing the firmware to be downloaded.  Once the package file is downloaded to a node, the firmware update will happen automatically in background.  For SP, the upgrade will happen automatically when a node is rebooted.  For SP, the upgrade will happen automatically if autoupdate is enabled (which is the recommended setting). |
| **password**  aliases: pass  string | Password for the specified user. |
| **reboot_sp**  boolean  *added in netapp.ontap 20.7.0* | Reboot service processor before downloading package.  Only available if ‘firmware_type’ is ‘service-processor’.  Defaults to True if not set when ‘firmware_type’ is ‘service-processor’.  Set this explictly to true to avoid a warning, and to false to not reboot the SP.  Rebooting the SP before download is strongly recommended.  **Choices:**   - `false` - `true` |
| **reboot_sp_after_download**  boolean  *added in netapp.ontap 21.15.0* | Reboot service processor after downloading package.  Only available if ‘firmware_type’ is ‘service-processor’.  **Choices:**   - `false` - `true` |
| **rename_package**  string  *added in netapp.ontap 20.7.0* | Rename the package.  Only available if ‘firmware_type’ is ‘service-processor’.  Not supported with REST. |
| **replace_package**  boolean  *added in netapp.ontap 20.7.0* | Replace the local package.  Only available if ‘firmware_type’ is ‘service-processor’.  Not supported with REST when set to false.  **Choices:**   - `false` - `true` |
| **server_password**  string  *added in netapp.ontap 21.15.0* | password to authenticate with the firmware package server.  Ignored with ZAPI. |
| **server_username**  string  *added in netapp.ontap 21.15.0* | username to authenticate with the firmware package server.  Ignored with ZAPI. |
| **shelf_module_fw**  string | Shelf module firmware to be updated to.  Not used if force_disruptive_update is False (ONTAP will automatically select the firmware)  Not supported with REST. |
| **state**  string | Whether the specified ONTAP firmware should be upgraded or not.  **Default:** `"present"` |
| **update_type**  string | Type of firmware update to be performed. Options include serial_full, serial_differential, network_full.  Not used if force_disruptive_update is False (ONTAP will automatically select the firmware)  Not supported with REST. |
| **use_rest**  string | Whether to use REST or ZAPI.  always – will always use the REST API if the module supports REST. A warning is issued if the module does not support REST. An error is issued if a module option is not supported in REST.  never – will always use ZAPI if the module supports ZAPI. An error may be issued if a REST option is not supported in ZAPI.  auto – will try to use the REST API if the module supports REST and modules options are supported. Reverts to ZAPI otherwise.  **Default:** `"auto"` |
| **username**  aliases: user  string | This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required.  For more information, please read the documentation <https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/>.  Two authentication methods are supported   1. basic authentication, using username and password, 2. SSL certificate authentication, using a ssl client cert file, and optionally a private key file.   To use a certificate, the certificate must have been installed in the ONTAP cluster, and cert authentication must have been enabled. |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `False` used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](na_ontap_firmware_upgrade_module.md#id4)

> **Note:**
>
> - The modules prefixed with na_ontap are built to support the ONTAP storage platform.
> - https is enabled by default and recommended. To enable http on the cluster you must run the following commands ‘set -privilege advanced;’ ‘system services web modify -http-enabled true;’

## [Examples](na_ontap_firmware_upgrade_module.md#id5)

```yaml+jinja
- name: firmware upgrade
  netapp.ontap.na_ontap_firmware_upgrade:
    state: present
    package_url: "{{ web_link }}"
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
- name: firmware upgrade, confirm successful download
  netapp.ontap.na_ontap_firmware_upgrade:
    state: present
    package_url: "{{ web_link }}"
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
    fail_on_502_error: true
- name: SP firmware upgrade
  netapp.ontap.na_ontap_firmware_upgrade:
    state: present
    node: vsim1
    package: "{{ file name }}"
    package_url: "{{ web_link }}"
    clear_logs: True
    install_baseline_image: False
    update_type: serial_full
    force_disruptive_update: False
    firmware_type: service-processor
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
- name: SP firmware download replace package
  tags:
  - sp_download
  netapp.ontap.na_ontap_firmware_upgrade:
    state: present
    node: vsim1
    package_url: "{{ web_link }}"
    firmware_type: service-processor
    replace_package: true
    reboot_sp: true
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
    https: true
    validate_certs: false
- name: SP firmware download rename package
  tags:
  - sp_download
  netapp.ontap.na_ontap_firmware_upgrade:
    state: present
    node: vsim1
    package_url: "{{ web_link }}"
    firmware_type: service-processor
    rename_package: SP_FW.zip
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
    https: true
    validate_certs: false
- name: ACP firmware download and upgrade
  netapp.ontap.na_ontap_firmware_upgrade:
    state: present
    node: vsim1
    firmware_type: acp
    package_url: "{{ web_link }}"
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
- name: shelf firmware upgrade
  netapp.ontap.na_ontap_firmware_upgrade:
    state: present
    firmware_type: shelf
    package_url: "{{ web_link }}"
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
- name: disk firmware upgrade
  netapp.ontap.na_ontap_firmware_upgrade:
    state: present
    firmware_type: disk
    package_url: "{{ web_link }}"
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
- name: any firmware upgrade (REST)
  netapp.ontap.na_ontap_firmware_upgrade:
    state: present
    package_url: "{{ web_link }}"
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
- name: SP firmware upgrade with reboots (REST)
  netapp.ontap.na_ontap_firmware_upgrade:
    state: present
    package_url: "{{ web_link }}"
    firmware_type: service-processor
    reboot_sp_: true
    reboot_sp_after_download: true
    hostname: "{{ netapp_hostname }}"
    username: "{{ netapp_username }}"
    password: "{{ netapp_password }}"
```

## [Return Values](na_ontap_firmware_upgrade_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | Returns additional information in case of success.  **Returned:** always |

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/netapp.ontap/issues)
- [Homepage](https://netapp.io/configuration-management-and-automation/)
- [Repository (Sources)](https://github.com/ansible-collections/netapp.ontap)
