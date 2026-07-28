---
collection: ansible
version: "8"
title: "theforeman.foreman.compute_resource module – Manage Compute Resources"
source_url: https://docs.ansible.com/projects/ansible/8/collections/theforeman/foreman/compute_resource_module.html
fetched_at: 2026-07-28T02:55:37+00:00
---
# theforeman.foreman.compute_resource module – Manage Compute Resources

> **Note:**
>
> This module is part of the [theforeman.foreman collection](https://galaxy.ansible.com/ui/repo/published/theforeman/foreman/) (version 3.15.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install theforeman.foreman`.
> You need further requirements to be able to use this module,
> see [Requirements](compute_resource_module.md#ansible-collections-theforeman-foreman-compute-resource-module-requirements) for details.
>
> To use it in a playbook, specify: `theforeman.foreman.compute_resource`.

New in theforeman.foreman 1.0.0

- [Synopsis](compute_resource_module.md#synopsis)
- [Requirements](compute_resource_module.md#requirements)
- [Parameters](compute_resource_module.md#parameters)
- [Attributes](compute_resource_module.md#attributes)
- [Examples](compute_resource_module.md#examples)
- [Return Values](compute_resource_module.md#return-values)

## [Synopsis](compute_resource_module.md#id1)

- Create, update, and delete Compute Resources

Aliases: foreman_compute_resource

## [Requirements](compute_resource_module.md#id2)

The below requirements are needed on the host that executes this module.

- requests

## [Parameters](compute_resource_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **description**  string | compute resource description |
| **locations**  list / elements=string | List of locations the entity should be assigned to |
| **name**  string / required | compute resource name |
| **organizations**  list / elements=string | List of organizations the entity should be assigned to |
| **password**  string / required | Password of the user accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_PASSWORD` will be used instead. |
| **provider**  string | Compute resource provider. Required if *state=present_with_defaults*.  **Choices:**   - `"vmware"` - `"libvirt"` - `"ovirt"` - `"proxmox"` - `"EC2"` - `"AzureRm"` - `"GCE"` - `"Openstack"` |
| **provider_params**  dictionary | Parameter specific to compute resource provider. Required if *state=present_with_defaults*. |
| **app_ident**  string | AzureRM client id |
| **caching_enabled**  boolean | enable caching for *provider=vmware*  **Choices:**   - `false` - `true` |
| **cloud**  string  *added in theforeman.foreman 2.1.0* | cloud for *provider=AzureRm*  **Choices:**   - `"azure"` - `"azureusgovernment"` - `"azurechina"` - `"azuregermancloud"` |
| **datacenter**  string | Datacenter the compute resource is in, not valid for *provider=libvirt* |
| **display_type**  string | Display type to use for the remote console, only valid for *provider=libvirt* |
| **domain**  string | Auth domain for users, only valid for *provider=Openstack* |
| **email**  string | Email for *provider=GCE* |
| **key_path**  string | Certificate path for *provider=GCE* |
| **keyboard_layout**  string  *added in theforeman.foreman 2.0.0* | Default VNC Keyboard for *provider=ovirt*  **Choices:**   - `"ar"` - `"da"` - `"de"` - `"de-ch"` - `"en-gb"` - `"en-us"` - `"es"` - `"et"` - `"fi"` - `"fo"` - `"fr"` - `"fr-be"` - `"fr-ca"` - `"fr-ch"` - `"hr"` - `"hu"` - `"is"` - `"it"` - `"ja"` - `"lt"` - `"lv"` - `"mk"` - `"nl"` - `"nl-be"` - `"no"` - `"pl"` - `"pt"` - `"pt-br"` - `"ru"` - `"sl"` - `"sv"` - `"th"` - `"tr"` |
| **ovirt_quota**  string | oVirt quota ID, only valid for *provider=ovirt* |
| **password**  string | Password for the compute resource connection, not valid for *provider=libvirt* |
| **project**  string | Project id for *provider=GCE* |
| **project_domain_id**  string | Project domain id, only valid for *provider=Openstack* |
| **project_domain_name**  string | Project domain name, only valid for *provider=Openstack* |
| **public_key**  string  *added in theforeman.foreman 2.0.0* | X509 Certification Authorities, only valid for *provider=ovirt* |
| **region**  string | AWS region, AZURE region |
| **set_console_password**  boolean  *added in theforeman.foreman 2.0.0* | Set a randomly generated password on the display connection for *provider=vmware* and *provider=libvirt*  **Choices:**   - `false` - `true` |
| **ssl_verify_peer**  boolean | verify ssl from provider *provider=proxmox*  **Choices:**   - `false` - `true` |
| **sub_id**  string  *added in theforeman.foreman 2.1.0* | Subscription ID for *provider=AzureRm* |
| **tenant**  string | AzureRM tenant, Openstack project name |
| **url**  string | URL of the compute resource |
| **use_v4**  boolean | Use oVirt API v4, only valid for *provider=ovirt*  **Choices:**   - `false` - `true` |
| **user**  string | Username for the compute resource connection, not valid for *provider=libvirt* |
| **zone**  string | zone for *provider=GCE* |
| **server_url**  string / required | URL of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_SERVER_URL` will be used instead. |
| **state**  string | State of the entity  `present_with_defaults` will ensure the entity exists, but won’t update existing ones  **Choices:**   - `"present"` ← (default) - `"present_with_defaults"` - `"absent"` |
| **updated_name**  string | new compute resource name |
| **username**  string / required | Username accessing the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_USERNAME` will be used instead. |
| **validate_certs**  boolean | Whether or not to verify the TLS certificates of the Foreman server.  If the value is not specified in the task, the value of environment variable `FOREMAN_VALIDATE_CERTS` will be used instead.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](compute_resource_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying the entity |
| **diff_mode** | **Support:** **full** | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |

## [Examples](compute_resource_module.md#id5)

```yaml+jinja
- name: Create libvirt compute resource
  theforeman.foreman.compute_resource:
    name: example_compute_resource
    locations:
      - Munich
    organizations:
      - ACME
    provider: libvirt
    provider_params:
      url: qemu+ssh://root@libvirt.example.com/system
      display_type: spice
    server_url: "https://foreman.example.com"
    username: "admin"
    password: "changeme"
    state: present

- name: Update libvirt compute resource
  theforeman.foreman.compute_resource:
    name: example_compute_resource
    description: updated compute resource
    locations:
      - Munich
    organizations:
      - ACME
    provider: libvirt
    provider_params:
      url: qemu+ssh://root@libvirt.example.com/system
      display_type: spice
    server_url: "https://foreman.example.com"
    username: "admin"
    password: "changeme"
    state: present

- name: Delete libvirt compute resource
  theforeman.foreman.compute_resource:
    name: example_compute_resource
    server_url: "https://foreman.example.com"
    username: "admin"
    password: "changeme"
    state: absent

- name: Create vmware compute resource
  theforeman.foreman.compute_resource:
    name: example_compute_resource
    locations:
      - Munich
    organizations:
      - ACME
    provider: vmware
    provider_params:
      caching_enabled: false
      url: vsphere.example.com
      user: admin
      password: secret
      datacenter: ax01
    server_url: "https://foreman.example.com"
    username: "admin"
    password: "changeme"
    state: present

- name: Create ovirt compute resource
  theforeman.foreman.compute_resource:
    name: ovirt_compute_resource
    locations:
      - France/Toulouse
    organizations:
      - Example Org
    provider: ovirt
    provider_params:
      url: ovirt.example.com
      user: ovirt-admin@example.com
      password: ovirtsecret
      datacenter: aa92fb54-0736-4066-8fa8-b8b9e3bd75ac
      ovirt_quota: 24868ab9-c2a1-47c3-87e7-706f17d215ac
      use_v4: true
    server_url: "https://foreman.example.com"
    username: "admin"
    password: "changeme"
    state: present

- name: Create proxmox compute resource
  theforeman.foreman.compute_resource:
    name: proxmox_compute_resource
    locations:
      - Munich
    organizations:
      - ACME
    provider: proxmox
    provider_params:
      url: https://proxmox.example.com:8006/api2/json
      user: root@pam
      password: secretpassword
      ssl_verify_peer: true
    server_url: "https://foreman.example.com"
    username: "admin"
    password: "changeme"
    state: present

- name: create EC2 compute resource
  theforeman.foreman.compute_resource:
    name: EC2_compute_resource
    description: EC2
    locations:
      - AWS
    organizations:
      - ACME
    provider: EC2
    provider_params:
      user: AWS_ACCESS_KEY
      password: AWS_SECRET_KEY
      region: eu-west-1
    server_url: "https://foreman.example.com"
    username: "admin"
    password: "changeme"
    state: present

- name: create Azure compute resource
  theforeman.foreman.compute_resource:
    name: AzureRm_compute_resource
    description: AzureRm
    locations:
      - Azure
    organizations:
      - ACME
    provider: AzureRm
    provider_params:
      sub_id: SUBSCRIPTION_ID
      tenant: TENANT_ID
      app_ident: CLIENT_ID
      password: CLIENT_SECRET
      region: westeurope
    server_url: "https://foreman.example.com"
    username: "admin"
    password: "changeme"
    state: present

- name: create GCE compute resource
  theforeman.foreman.compute_resource:
    name: GCE compute resource
    description: Google Cloud Engine
    locations:
      - GCE
    organizations:
      - ACME
    provider: GCE
    provider_params:
      project: orcharhino
      email: myname@atix.de
      key_path: "/usr/share/foreman/gce_orcharhino_key.json"
      zone: europe-west3-b
    server_url: "https://foreman.example.com"
    username: "admin"
    password: "changeme"
    state: present

- name: create Openstack compute resource
  theforeman.foreman.compute_resource:
    name: Openstack compute resource
    description: Openstack
    locations:
      - DC1
    organizations:
      - ACME
    provider: Openstack
    provider_params:
      url: "https://Openstack.example.com:5000/v3"
      user: admin
      password: secret
      tenant: "MyProject"
      domain: "example.com"
      project_domain_name: "example.com"
      project_domain_id: "0123456789a0123456789b0123456789"
    server_url: "https://foreman.example.com"
    username: "admin"
    password: "changeme"
    state: present
```

## [Return Values](compute_resource_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **entity**  dictionary | Final state of the affected entities grouped by their type.  **Returned:** success |
| **compute_resources**  list / elements=dictionary | List of compute resources.  **Returned:** success |

### Authors

- Philipp Joos (@philippj)
- Baptiste Agasse (@bagasse)
- Manisha Singhal (@Manisha15) ATIX AG
- Mark Hlawatschek (@hlawatschek) ATIX AG

### Collection links

- [Issue Tracker](https://github.com/theforeman/foreman-ansible-modules/issues)
- [Homepage](https://theforeman.org/)
- [Repository (Sources)](https://github.com/theforeman/foreman-ansible-modules)
