---
collection: ansible
version: "8"
title: "f5networks.f5_modules.bigip_iapp_service module – Manages TCL iApp services on a BIG-IP"
source_url: https://docs.ansible.com/projects/ansible/8/collections/f5networks/f5_modules/bigip_iapp_service_module.html
fetched_at: 2026-07-28T02:06:26+00:00
---
# f5networks.f5_modules.bigip_iapp_service module – Manages TCL iApp services on a BIG-IP

> **Note:**
>
> This module is part of the [f5networks.f5_modules collection](https://galaxy.ansible.com/ui/repo/published/f5networks/f5_modules/) (version 1.27.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install f5networks.f5_modules`.
>
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_iapp_service`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_iapp_service_module.md#synopsis)
- [Parameters](bigip_iapp_service_module.md#parameters)
- [Notes](bigip_iapp_service_module.md#notes)
- [Examples](bigip_iapp_service_module.md#examples)

## [Synopsis](bigip_iapp_service_module.md#id1)

- Manages TCL iApp services on a BIG-IP.
- The API the system uses to communicate with on the BIG-IP is `/mgmt/tm/sys/application/service/`.

## [Parameters](bigip_iapp_service_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **description**  string | Description of the iApp service.  If this option is specified in the Ansible task, it takes precedence over any similar setting in the iApp Service payload that you provide in the `parameters` field. |
| **device_group**  string | The device group for the iApp service.  If this option is specified in the Ansible task, it takes precedence over any similar setting in the iApp Service payload that you provide in the `parameters` field. |
| **force**  boolean | Forces the updating of an iApp service, even if the parameters to the service have not changed. This option is of particular importance if the iApp template that underlies the service has been updated in-place. This option is equivalent to re-configuring the iApp if that template has changed.  **Choices:**   - `false` ← (default) - `true` |
| **metadata**  list / elements=any | Metadata associated with the iApp service.  If this option is specified in the Ansible task, it takes precedence over any similar setting in the iApp Service payload that you provide in the `parameters` field. |
| **name**  string / required | The name of the iApp service you want to deploy. |
| **parameters**  dictionary | A hash of all the required template variables for the iApp template. If your parameters are stored in a file (the more common scenario) we recommend you use either the `file` or `template` lookups to supply the expected parameters.  These parameters typically consist of the `lists`, `tables`, and `variables` fields. |
| **partition**  string | Device partition to manage resources on.  **Default:** `"Common"` |
| **provider**  dictionary  *added in f5networks.f5_modules 1.0.0* | A dict object containing connection details. |
| **auth_provider**  string | Configures the auth provider for to obtain authentication tokens from the remote device.  This option is really used when working with BIG-IQ devices. |
| **no_f5_teem**  boolean | If `yes`, TEEM telemetry data is not sent to F5.  You may omit this option by setting the environment variable `F5_TELEMETRY_OFF`.  Previously used variable `F5_TEEM` is deprecated as its name was confusing.  **Choices:**   - `false` ← (default) - `true` |
| **password**  aliases: pass, pwd  string / required | The password for the user account used to connect to the BIG-IP or the BIG-IQ.  You may omit this option by setting the environment variable `F5_PASSWORD`. |
| **server**  string / required | The BIG-IP host or the BIG-IQ host.  You may omit this option by setting the environment variable `F5_SERVER`. |
| **server_port**  integer | The BIG-IP server port.  You may omit this option by setting the environment variable `F5_SERVER_PORT`.  **Default:** `443` |
| **timeout**  integer | Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands. If the timeout is exceeded before the operation is completed, the module will error. |
| **transport**  string | Configures the transport connection to use when connecting to the remote device.  **Choices:**   - `"rest"` ← (default) |
| **user**  string / required | The username to connect to the BIG-IP or the BIG-IQ. This user must have administrative privileges on the device.  You may omit this option by setting the environment variable `F5_USER`. |
| **validate_certs**  boolean | If `no`, SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.  You may omit this option by setting the environment variable `F5_VALIDATE_CERTS`.  **Choices:**   - `false` - `true` ← (default) |
| **state**  string | When `present`, ensures the iApp service is created and running. When `absent`, ensures the iApp service has been removed.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **strict_updates**  boolean | Indicates whether the application service is tied to the template, so when the template is updated, the application service changes to reflect the updates.  When `true`, disallows any updates to the resources that the iApp service has created, if they are not updated directly through the iApp.  When `false`, allows updates outside of the iApp.  If this option is specified in the Ansible task, it takes precedence over any similar setting in the iApp Service payload that you provide in the `parameters` field.  **Choices:**   - `false` - `true` |
| **template**  string | The iApp template from which to instantiate a new service. This template must exist on your BIG-IP before you can successfully create a service.  When creating a new service, this parameter is required. |
| **traffic_group**  string | The traffic group for the iApp service. When creating a new service, if this value is not specified, the default of `/Common/traffic-group-1` is used.  If this option is specified in the Ansible task, it takes precedence over any similar setting in the iApp Service payload that you provide in the `parameters` field. |

## [Notes](bigip_iapp_service_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_iapp_service_module.md#id4)

```yaml+jinja
- name: Create HTTP iApp service from iApp template
  bigip_iapp_service:
    name: foo-service
    template: f5.http
    parameters: "{{ lookup('file', 'f5.http.parameters.json') }}"
    state: present
    provider:
      user: admin
      password: secret
      server: lb.mydomain.com
  delegate_to: localhost

- name: Upgrade foo-service to v1.2.0rc4 of the f5.http template
  bigip_iapp_service:
    name: foo-service
    template: f5.http.v1.2.0rc4
    state: present
    provider:
      user: admin
      password: secret
      server: lb.mydomain.com
  delegate_to: localhost

- name: Configure a service using parameters in YAML
  bigip_iapp_service:
    name: tests
    template: web_frontends
    state: present
    parameters:
      variables:
        - name: var__vs_address
          value: 1.1.1.1
        - name: pm__apache_servers_for_http
          value: 2.2.2.1:80
        - name: pm__apache_servers_for_https
          value: 2.2.2.2:80
    provider:
      user: admin
      password: secret
      server: lb.mydomain.com
  delegate_to: localhost

- name: Re-configure a service whose underlying iApp was updated in place
  bigip_iapp_service:
    name: tests
    template: web_frontends
    force: true
    state: present
    parameters:
      variables:
        - name: var__vs_address
          value: 1.1.1.1
        - name: pm__apache_servers_for_http
          value: 2.2.2.1:80
        - name: pm__apache_servers_for_https
          value: 2.2.2.2:80
    provider:
      user: admin
      password: secret
      server: lb.mydomain.com
  delegate_to: localhost

- name: Try to remove the iApp template before the associated Service is removed
  bigip_iapp_template:
    name: web_frontends
    state: absent
    provider:
      user: admin
      password: secret
      server: lb.mydomain.com
  register: result
  failed_when:
    - result is not success
    - "'referenced by one or more applications' not in result.msg"

- name: Configure a service using more complicated parameters
  bigip_iapp_service:
    name: tests
    template: web_frontends
    state: present
    provider:
      user: admin
      password: secret
      server: lb.mydomain.com
    parameters:
      variables:
        - name: var__vs_address
          value: 1.1.1.1
        - name: pm__apache_servers_for_http
          value: 2.2.2.1:80
        - name: pm__apache_servers_for_https
          value: 2.2.2.2:80
      lists:
        - name: irules__irules
          value:
            - foo
            - bar
      tables:
        - name: basic__snatpool_members
        - name: net__snatpool_members
        - name: optimizations__hosts
        - name: pool__hosts
          columnNames:
            - name
          rows:
            - row:
                - internal.company.bar
        - name: pool__members
          columnNames:
            - addr
            - port
            - connection_limit
          rows:
            - row:
                - "none"
                - 80
                - 0
        - name: server_pools__servers
  delegate_to: localhost

- name: Override metadata that may or may not exist in parameters
  bigip_iapp_service:
    name: foo-service
    template: f5.http
    parameters: "{{ lookup('file', 'f5.http.parameters.json') }}"
    metadata:
      - persist: true
        name: data 1
      - persist: true
        name: data 2
    state: present
    provider:
      user: admin
      password: secret
      server: lb.mydomain.com
  delegate_to: localhost
```

### Authors

- Tim Rupp (@caphrim007)
- Wojciech Wypior (@wojtek0806)

### Collection links

- [Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
- [Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
- [Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
