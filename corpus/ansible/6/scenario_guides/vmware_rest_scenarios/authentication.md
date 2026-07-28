---
collection: ansible
version: "6"
title: "How to configure the vmware_rest collection"
source_url: https://docs.ansible.com/projects/ansible/6/scenario_guides/vmware_rest_scenarios/authentication.html
fetched_at: 2026-07-27T16:43:17+00:00
---
# How to configure the vmware_rest collection

- [Introduction](authentication.md#introduction)
- [Environment variables](authentication.md#environment-variables)
- [Module parameters](authentication.md#module-parameters)
- [Ignore SSL certificate error](authentication.md#ignore-ssl-certificate-error)

## [Introduction](authentication.md#id1)

The vcenter_rest modules need to be authenticated. There are two different

## [Environment variables](authentication.md#id2)

> **Note:**
>
> This solution requires that you call the modules from the local machine.

You need to export some environment variables in your shell before you call the modules.

```shell
$ export VMWARE_HOST=vcenter.test
$ export VMWARE_USER=myvcenter-user
$ export VMWARE_password=mypassword
$ ansible-playbook my-playbook.yaml
```

## [Module parameters](authentication.md#id3)

All the vcenter_rest modules accept the following arguments:

- `vcenter_host`
- `vcenter_username`
- `vcenter_password`

## [Ignore SSL certificate error](authentication.md#id4)

It’s common to run a test environment without a proper SSL certificate configuration.

To ignore the SSL error, you can use the `vcenter_validate_certs: no` argument or
`export VMWARE_VALIDATE_CERTS=no` to set the environment variable.
