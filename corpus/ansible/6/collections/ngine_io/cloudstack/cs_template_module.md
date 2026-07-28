---
collection: ansible
version: "6"
title: "ngine_io.cloudstack.cs_template module – Manages templates on Apache CloudStack based clouds."
source_url: https://docs.ansible.com/projects/ansible/6/collections/ngine_io/cloudstack/cs_template_module.html
fetched_at: 2026-07-28T00:15:50+00:00
---
# ngine_io.cloudstack.cs_template module – Manages templates on Apache CloudStack based clouds.

> **Note:**
>
> This module is part of the [ngine_io.cloudstack collection](https://galaxy.ansible.com/ngine_io/cloudstack) (version 2.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ngine_io.cloudstack`.
> You need further requirements to be able to use this module,
> see [Requirements](cs_template_module.md#ansible-collections-ngine-io-cloudstack-cs-template-module-requirements) for details.
>
> To use it in a playbook, specify: `ngine_io.cloudstack.cs_template`.

New in ngine_io.cloudstack 0.1.0

- [Synopsis](cs_template_module.md#synopsis)
- [Requirements](cs_template_module.md#requirements)
- [Parameters](cs_template_module.md#parameters)
- [Notes](cs_template_module.md#notes)
- [Examples](cs_template_module.md#examples)
- [Return Values](cs_template_module.md#return-values)

## [Synopsis](cs_template_module.md#id1)

- Register templates from an URL.
- Create templates from a ROOT volume of a stopped VM or its snapshot.
- Update, extract and delete templates.

## [Requirements](cs_template_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- cs >= 0.9.0

## [Parameters](cs_template_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **account**  string | Account the template, snapshot or VM is related to. |
| **api_http_method**  string | HTTP method used to query the API endpoint.  If not given, the `CLOUDSTACK_METHOD` env variable is considered.  Choices:   - `"get"` ← (default) - `"post"` |
| **api_key**  string / required | API key of the CloudStack API.  If not given, the `CLOUDSTACK_KEY` env variable is considered. |
| **api_secret**  string / required | Secret key of the CloudStack API.  If not set, the `CLOUDSTACK_SECRET` env variable is considered. |
| **api_timeout**  integer | HTTP timeout in seconds.  If not given, the `CLOUDSTACK_TIMEOUT` env variable is considered.  Default: `10` |
| **api_url**  string / required | URL of the CloudStack API e.g. <https://cloud.example.com/client/api>.  If not given, the `CLOUDSTACK_ENDPOINT` env variable is considered. |
| **api_verify_ssl_cert**  string | Verify CA authority cert file.  If not given, the `CLOUDSTACK_VERIFY` env variable is considered. |
| **bits**  integer | 32 or 64 bits support.  Choices:   - `32` - `64` ← (default) |
| **checksum**  string | The MD5 checksum value of this template.  If set, we search by checksum instead of name. |
| **cross_zones**  boolean | Whether the template should be synced or removed across zones.  Only used if *state* is `present` or `absent`.  Choices:   - `false` ← (default) - `true` |
| **details**  string | Template details in key/value pairs. |
| **display_text**  string | Display text of the template. |
| **domain**  string | Domain the template, snapshot or VM is related to. |
| **format**  string | The format for the template.  Only considered if *state=present*.  Choices:   - `"QCOW2"` - `"RAW"` - `"VHD"` - `"OVA"` |
| **hypervisor**  string | Name the hypervisor to be used for creating the new template.  Relevant when using *state=present*.  Possible values are `KVM`, `VMware`, `BareMetal`, `XenServer`, `LXC`, `HyperV`, `UCS`, `OVM`, `Simulator`. |
| **is_dynamically_scalable**  boolean | Register the template having XS/VMware tools installed in order to support dynamic scaling of VM CPU/memory.  Only used if *state* is `present`.  Choices:   - `false` - `true` |
| **is_extractable**  boolean | Allows the template or its derivatives to be extractable.  Choices:   - `false` - `true` |
| **is_featured**  boolean | Register the template to be featured.  Only used if *state* is `present`.  Choices:   - `false` - `true` |
| **is_public**  boolean | Register the template to be publicly available to all users.  Only used if *state* is `present`.  Choices:   - `false` - `true` |
| **is_routing**  boolean | Sets the template type to routing, i.e. if template is used to deploy routers.  Only considered if *url* is used.  Choices:   - `false` - `true` |
| **mode**  string | Mode for the template extraction.  Only used if *state=extracted*.  Choices:   - `"http_download"` ← (default) - `"ftp_upload"` |
| **name**  string / required | Name of the template. |
| **os_type**  string | OS type that best represents the OS of this template. |
| **password_enabled**  boolean | Enable template password reset support.  Choices:   - `false` - `true` |
| **poll_async**  boolean | Poll async jobs until job has finished.  Choices:   - `false` - `true` ← (default) |
| **project**  string | Name of the project the template to be registered in. |
| **requires_hvm**  boolean | Whether the template requires HVM or not.  Only considered while creating the template.  Choices:   - `false` - `true` |
| **snapshot**  string | Name of the snapshot, created from the VM ROOT volume, the template will be created from.  *vm* is required together with this argument. |
| **sshkey_enabled**  boolean | True if the template supports the sshkey upload feature.  Only considered if *url* is used (API limitation).  Choices:   - `false` - `true` |
| **state**  string | State of the template.  Choices:   - `"present"` ← (default) - `"absent"` - `"extracted"` |
| **tags**  aliases: tag  list / elements=dictionary | List of tags. Tags are a list of dictionaries having keys *key* and *value*.  To delete all tags, set a empty list e.g. *tags: []*. |
| **template_filter**  string | Name of the filter used to search for the template.  The filter `all` was added in 2.7.  Choices:   - `"all"` - `"featured"` - `"self"` ← (default) - `"selfexecutable"` - `"sharedexecutable"` - `"executable"` - `"community"` |
| **template_find_options**  aliases: template_find_option  list / elements=string | Options to find a template uniquely.  More than one allowed.  Choices:   - `"display_text"` - `"checksum"` - `"cross_zones"`   Default: `[]` |
| **template_tag**  string | The tag for this template. |
| **url**  string | URL of where the template is hosted on *state=present*.  URL to which the template would be extracted on *state=extracted*.  Mutually exclusive with *vm*. |
| **vm**  string | VM name the template will be created from its volume or alternatively from a snapshot.  VM must be in stopped state if created from its volume.  Mutually exclusive with *url*. |
| **zone**  string | Name of the zone you wish the template to be registered or deleted from.  Required when *cross_zones* is `no` |

## [Notes](cs_template_module.md#id4)

> **Note:**
>
> - A detailed guide about cloudstack modules can be found in the [CloudStack Cloud Guide](../scenario_guides/guide_cloudstack.md).
> - This module supports check mode.

## [Examples](cs_template_module.md#id5)

```yaml+jinja
- name: register a systemvm template
  ngine_io.cloudstack.cs_template:
    name: systemvm-vmware-4.5
    url: "http://packages.shapeblue.com/systemvmtemplate/4.5/systemvm64template-4.5-vmware.ova"
    hypervisor: VMware
    format: OVA
    cross_zones: yes
    os_type: Debian GNU/Linux 7(64-bit)

- name: Create a template from a stopped virtual machine's volume
  ngine_io.cloudstack.cs_template:
    name: Debian 9 (64-bit) 20GB ({{ ansible_date_time.date }})
    vm: debian-9-base-vm
    os_type: Debian GNU/Linux 9 (64-bit)
    zone: tokio-ix
    password_enabled: yes
    is_public: yes

# Note: Use template_find_option(s) when a template name is not unique
- name: Create a template from a stopped virtual machine's volume
  ngine_io.cloudstack.cs_template:
    name: Debian 9 (64-bit)
    display_text: Debian 9 (64-bit) 20GB ({{ ansible_date_time.date }})
    template_find_option: display_text
    vm: debian-9-base-vm
    os_type: Debian GNU/Linux 9 (64-bit)
    zone: tokio-ix
    password_enabled: yes
    is_public: yes

- name: create a template from a virtual machine's root volume snapshot
  ngine_io.cloudstack.cs_template:
    name: Debian 9 (64-bit) Snapshot ROOT-233_2015061509114
    snapshot: ROOT-233_2015061509114
    os_type: Debian GNU/Linux 9 (64-bit)
    zone: tokio-ix
    password_enabled: yes
    is_public: yes

- name: Remove a template
  ngine_io.cloudstack.cs_template:
    name: systemvm-4.2
    cross_zones: yes
    state: absent
```

## [Return Values](cs_template_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **account**  string | Account the template is related to.  Returned: success  Sample: `"example account"` |
| **checksum**  string | MD5 checksum of the template.  Returned: if available  Sample: `"0b31bccccb048d20b551f70830bb7ad0"` |
| **created**  string | Date of registering.  Returned: success  Sample: `"2015-03-29T14:57:06+0200"` |
| **cross_zones**  boolean | true if the template is managed across all zones, false otherwise.  Returned: if available  Sample: `false` |
| **display_text**  string | Display text of the template.  Returned: if available  Sample: `"Debian 7.7 64-bit minimal 2015-03-19"` |
| **domain**  string | Domain the template is related to.  Returned: success  Sample: `"example domain"` |
| **format**  string | Format of the template.  Returned: if available  Sample: `"OVA"` |
| **hypervisor**  string | Hypervisor related to this template.  Returned: if available  Sample: `"VMware"` |
| **id**  string | UUID of the template or extracted object.  Returned: success  Sample: `"a6f7a5fc-43f8-11e5-a151-feff819cdc9f"` |
| **is_extractable**  boolean | True if the template is extractable.  Returned: if available  Sample: `true` |
| **is_featured**  boolean | True if the template is featured.  Returned: if available  Sample: `true` |
| **is_public**  boolean | True if the template is public.  Returned: if available  Sample: `true` |
| **is_ready**  boolean | True if the template is ready to be deployed from.  Returned: if available  Sample: `true` |
| **mode**  string | Mode of extraction  Returned: on state=extracted  Sample: `"http_download"` |
| **name**  string | Name of the template or extracted object.  Returned: success  Sample: `"Debian 7 64-bit"` |
| **os_type**  string | Type of the OS.  Returned: if available  Sample: `"CentOS 6.5 (64-bit)"` |
| **password_enabled**  boolean | True if the reset password feature is enabled, false otherwise.  Returned: if available  Sample: `false` |
| **project**  string | Name of project the template is related to.  Returned: success  Sample: `"Production"` |
| **sshkey_enabled**  boolean | true if template is sshkey enabled, false otherwise.  Returned: if available  Sample: `false` |
| **state**  string | State of the extracted template  Returned: on state=extracted  Sample: `"DOWNLOAD_URL_CREATED"` |
| **status**  string | Status of the template or extracted object.  Returned: success  Sample: `"Download Complete"` |
| **tags**  list / elements=string | List of resource tags associated with the template.  Returned: if available  Sample: `["[ { \"key\": \"foo\"", " \"value\": \"bar\" } ]"]` |
| **template_tag**  string | Template tag related to this template.  Returned: if available  Sample: `"special"` |
| **template_type**  string | Type of the template.  Returned: if available  Sample: `"USER"` |
| **url**  string | Url to which the template is extracted to  Returned: on state=extracted  Sample: `"http://1.2.3.4/userdata/eb307f13-4aca-45e8-b157-a414a14e6b04.ova"` |
| **zone**  string | Name of zone the template is registered in.  Returned: success  Sample: `"zuerich"` |

### Authors

- René Moser (@resmo)

### Collection links

[Issue Tracker](https://github.com/ngine-io/ansible-collection-cloudstack/issues)
[Repository (Sources)](https://github.com/ngine-io/ansible-collection-cloudstack)
