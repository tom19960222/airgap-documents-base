---
collection: ansible
version: "6"
title: "netapp.ontap.na_ontap_restit module – NetApp ONTAP Run any REST API on ONTAP"
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp/ontap/na_ontap_restit_module.html
fetched_at: 2026-07-28T00:13:03+00:00
---
# netapp.ontap.na_ontap_restit module – NetApp ONTAP Run any REST API on ONTAP

> **Note:**
>
> This module is part of the [netapp.ontap collection](https://galaxy.ansible.com/netapp/ontap) (version 21.24.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netapp.ontap`.
> You need further requirements to be able to use this module,
> see [Requirements](na_ontap_restit_module.md#ansible-collections-netapp-ontap-na-ontap-restit-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.ontap.na_ontap_restit`.

New in netapp.ontap 20.4.0

- [Synopsis](na_ontap_restit_module.md#synopsis)
- [Requirements](na_ontap_restit_module.md#requirements)
- [Parameters](na_ontap_restit_module.md#parameters)
- [Notes](na_ontap_restit_module.md#notes)
- [Examples](na_ontap_restit_module.md#examples)
- [Return Values](na_ontap_restit_module.md#return-values)

## [Synopsis](na_ontap_restit_module.md#id1)

- Call a REST API on ONTAP.
- Cluster REST API are run using a cluster admin account.
- Vserver REST API can be run using a vsadmin account or using vserver tunneling (cluster admin with *vserver_* options).
- In case of success, a json dictionary is returned as `response`.
- In case of a REST API error, `status_code`, `error_code`, `error_message` are set to help with diagnosing the issue,
- and the call is reported as an error (‘failed’).
- Other errors (eg connection issues) are reported as Ansible error.

## [Requirements](na_ontap_restit_module.md#id2)

The below requirements are needed on the host that executes this module.

- Ansible 2.9 or later - 2.12 or later is recommended.
- Python3 - 3.9 or later is recommended.
- When using ZAPI, netapp-lib 2018.11.13 or later (install using ‘pip install netapp-lib’), netapp-lib 2020.3.12 is strongly recommended as it provides better error reporting for connection issues
- a physical or virtual clustered Data ONTAP system, the modules support Data ONTAP 9.1 and onward, REST support requires ONTAP 9.6 or later

## [Parameters](na_ontap_restit_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **accept_header**  string  added in netapp.ontap 21.24.0 | Value for the Accept request HTTP header.  This is very infrequently needed, but required to read a file (see examples).  For most cases, omit this field. Set it to “multipart/form-data” when expecting such a format.  By default the module is using “application/json” or “application/hal+json” when hal_linking is true. |
| **api**  string / required | The REST API to call (eg *cluster/software*, *svms/svm*). |
| **body**  aliases: info  dictionary | A dictionary for the info parameter |
| **cert_filepath**  string  added in netapp.ontap 20.6.0 | path to SSL client cert file (.pem).  not supported with python 2.6. |
| **feature_flags**  dictionary  added in netapp.ontap 20.5.0 | Enable or disable a new feature.  This can be used to enable an experimental feature or disable a new feature that breaks backward compatibility.  Supported keys and values are subject to change without notice. Unknown keys are ignored. |
| **files**  dictionary  added in netapp.ontap 21.24.0 | A dictionary for the parameters when using multipart/form-data.  This is very infrequently needed, but required to write a file (see examples)  When present, requests will automatically set the Content-Type header to multipart/form-data. |
| **force_ontap_version**  string  added in netapp.ontap 21.23.0 | Override the cluster ONTAP version when using REST.  The behavior is undefined if the version does not match the target cluster.  This is provided as a work-around when the cluster version cannot be read because of permission issues. See <https://github.com/ansible-collections/netapp.ontap/wiki/Known-issues>.  This should be in the form 9.10 or 9.10.1 with each element being an integer number.  When `use_rest` is set to auto, this may force a switch to ZAPI based on the version and platform capabilities.  Ignored with ZAPI. |
| **hal_linking**  boolean | if true, HAL-encoded links are returned in the response.  Choices:   - `false` ← (default) - `true` |
| **hostname**  string / required | The hostname or IP address of the ONTAP instance. |
| **http_port**  integer | Override the default port (80 or 443) with this port |
| **https**  boolean | Enable and disable https.  Ignored when using REST as only https is supported.  Ignored when using SSL certificate authentication as it requires SSL.  Choices:   - `false` ← (default) - `true` |
| **key_filepath**  string  added in netapp.ontap 20.6.0 | path to SSL client key file. |
| **method**  string | The REST method to use.  Default: `"GET"` |
| **ontapi**  integer | The ontap api version to use |
| **password**  aliases: pass  string | Password for the specified user. |
| **query**  dictionary | A list of dictionaries for the query parameters |
| **use_rest**  string | Whether to use REST or ZAPI.  always – will always use the REST API if the module supports REST. A warning is issued if the module does not support REST. An error is issued if a module option is not supported in REST.  never – will always use ZAPI if the module supports ZAPI. An error may be issued if a REST option is not supported in ZAPI.  auto – will try to use the REST API if the module supports REST and modules options are supported. Reverts to ZAPI otherwise.  Default: `"auto"` |
| **username**  aliases: user  string | This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required.  For more information, please read the documentation <https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/>.  Two authentication methods are supported   1. basic authentication, using username and password, 2. SSL certificate authentication, using a ssl client cert file, and optionally a private key file.   To use a certificate, the certificate must have been installed in the ONTAP cluster, and cert authentication must have been enabled. |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `False` used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |
| **vserver_name**  string | if provided, forces vserver tunneling. username identifies a cluster admin account. |
| **vserver_uuid**  string | if provided, forces vserver tunneling. username identifies a cluster admin account. |
| **wait_for_completion**  boolean  added in netapp.ontap 21.14.0 | when true, POST/PATCH/DELETE can be handled synchronously and asynchronously.  if the response indicates that a job is in progress, the job status is checked periodically until is completes.  when false, the call returns immediately.  Choices:   - `false` ← (default) - `true` |

## [Notes](na_ontap_restit_module.md#id4)

> **Note:**
>
> - The modules prefixed with na_ontap are built to support the ONTAP storage platform.
> - https is enabled by default and recommended. To enable http on the cluster you must run the following commands ‘set -privilege advanced;’ ‘system services web modify -http-enabled true;’

## [Examples](na_ontap_restit_module.md#id5)

```yaml+jinja
-
  name: Ontap REST API
  hosts: localhost
  gather_facts: False
  collections:
    - netapp.ontap
  vars:
    login: &login
      hostname: "{{ admin_ip }}"
      username: "{{ admin_username }}"
      password: "{{ admin_password }}"
      https: true
      validate_certs: false
    svm_login: &svm_login
      hostname: "{{ svm_admin_ip }}"
      username: "{{ svm_admin_username }}"
      password: "{{ svm_admin_password }}"
      https: true
      validate_certs: false

  tasks:
    - name: run ontap REST API command as cluster admin
      na_ontap_restit:
        <<: *login
        api: cluster/software
      register: result
    - debug: var=result
    - assert: { that: result.status_code==200, quiet: True }

    - name: run ontap REST API command as cluster admin
      na_ontap_restit:
        <<: *login
        api: cluster/software
        query:
          fields: version
      register: result
    - debug: var=result
    - assert: { that: result.status_code==200, quiet: True }

    - name: run ontap REST API command as cluster admin
      na_ontap_restit:
        <<: *login
        api: svm/svms
      register: result
    - debug: var=result
    - assert: { that: result.status_code==200, quiet: True }

    - name: run ontap REST API command as cluster admin
      na_ontap_restit:
        <<: *login
        api: svm/svms
        query:
          fields: aggregates,cifs,nfs,uuid
          query_fields: name
          query: trident_svm
        hal_linking: true
      register: result
    - debug: var=result

    - name: run ontap REST API command as vsadmin
      na_ontap_restit:
        <<: *svm_login
        api: svm/svms
      register: result
    - debug: var=result
    - assert: { that: result.status_code==200, quiet: True }

    - name: run ontap REST API command as vserver tunneling
      na_ontap_restit:
        <<: *login
        api: storage/volumes
        vserver_name: ansibleSVM
      register: result
    - debug: var=result
    - assert: { that: result.status_code==200, quiet: True }
    - set_fact:
        uuid: "{{ result.response.records | json_query(get_uuid) }}"
      vars:
        get_uuid: "[? name=='deleteme_ln1'].uuid"
    - debug: var=uuid

    - name: run ontap REST API command as DELETE method with vserver tunneling
      na_ontap_restit:
        <<: *login
        api: "storage/volumes/{{ uuid[0] }}"
        method: DELETE
        vserver_name: ansibleSVM
        query:
          return_timeout: 60
      register: result
      when: uuid|length == 1
    - debug: var=result
    - assert: { that: result.skipped|default(false) or result.status_code|default(404) == 200, quiet: True }

    - name: run ontap REST API command as POST method with vserver tunneling
      na_ontap_restit:
        <<: *login
        api: storage/volumes
        method: POST
        vserver_name: ansibleSVM
        query:
          return_records: "true"
          return_timeout: 60
        body:
          name: deleteme_ln1
          aggregates:
            - name: aggr1
      register: result
    - debug: var=result
    - assert: { that: result.status_code==201, quiet: True }

    - name: run ontap REST API command as DELETE method with vserver tunneling
      # delete test volume if present
      na_ontap_restit:
        <<: *login
        api: "storage/volumes/{{ result.response.records[0].uuid }}"
        method: DELETE
        vserver_name: ansibleSVM
        query:
          return_timeout: 60
      register: result
    - debug: var=result
    - assert: { that: result.status_code==200, quiet: True }

    - name: create a file
      # assuming credentials are set using module_defaults
      na_ontap_restit:
        api: storage/volumes/f3c003cb-2974-11ed-b2f8-005056b38dae/files/laurent123.txt
        method: post
        files: {'data': 'some data'}

    - name: read a file
      # assuming credentials are set using module_defaults
      na_ontap_restit:
        api: storage/volumes/f3c003cb-2974-11ed-b2f8-005056b38dae/files/laurent123.txt
        method: get
        accept_header: "multipart/form-data"
        query:
          length: 100

# error cases
    - name: run ontap REST API command
      na_ontap_restit:
        <<: *login
        api: unknown/endpoint
      register: result
      ignore_errors: True
    - debug: var=result
    - assert: { that: result.status_code==404, quiet: True }
```

## [Return Values](na_ontap_restit_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **error_code**  string | If the REST API was executed but failed, the error code set by the REST API.  Not present if successful, or if the REST API call cannot be performed.  Returned: On error |
| **error_message**  string | If the REST API was executed but failed, the error message set by the REST API.  Not present if successful, or if the REST API call cannot be performed.  Returned: On error |
| **response**  dictionary | If successful, a json dictionary returned by the REST API.  If the REST API was executed but failed, an empty dictionary.  Not present if the REST API call cannot be performed.  Returned: On success |
| **status_code**  string | The http status code.  When wait_for_completion is True, this is forced to 0.  Returned: Always |

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/netapp.ontap/issues)
[Homepage](https://netapp.io/configuration-management-and-automation/)
[Repository (Sources)](https://github.com/ansible-collections/netapp.ontap)
