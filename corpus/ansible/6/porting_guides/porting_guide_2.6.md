---
collection: ansible
version: "6"
title: "Ansible 2.6 Porting Guide"
source_url: https://docs.ansible.com/projects/ansible/6/porting_guides/porting_guide_2.6.html
fetched_at: 2026-07-27T16:39:43+00:00
---
# [Ansible 2.6 Porting Guide](porting_guide_2.6.md#id2)

This section discusses the behavioral changes between Ansible 2.5 and Ansible 2.6.

It is intended to assist in updating your playbooks, plugins and other parts of your Ansible infrastructure so they will work with this version of Ansible.

We suggest you read this page along with [Ansible Changelog for 2.6](https://github.com/ansible/ansible/blob/stable-2.6/changelogs/CHANGELOG-v2.6.rst) to understand what updates you may need to make.

This document is part of a collection on porting. The complete list of porting guides can be found at [porting guides](porting_guides.md#porting-guides).

Topics

- [Ansible 2.6 Porting Guide](porting_guide_2.6.md#ansible-2-6-porting-guide)

  - [Playbook](porting_guide_2.6.md#playbook)
  - [Deprecated](porting_guide_2.6.md#deprecated)
  - [Modules](porting_guide_2.6.md#modules)

    - [Modules removed](porting_guide_2.6.md#modules-removed)
    - [Deprecation notices](porting_guide_2.6.md#deprecation-notices)
    - [Noteworthy module changes](porting_guide_2.6.md#noteworthy-module-changes)
  - [Plugins](porting_guide_2.6.md#plugins)

    - [Deprecation notices](porting_guide_2.6.md#id1)
    - [Noteworthy plugin changes](porting_guide_2.6.md#noteworthy-plugin-changes)
  - [Porting custom scripts](porting_guide_2.6.md#porting-custom-scripts)
  - [Networking](porting_guide_2.6.md#networking)
  - [Dynamic inventory scripts](porting_guide_2.6.md#dynamic-inventory-scripts)

## [Playbook](porting_guide_2.6.md#id3)

- The deprecated task option `always_run` has been removed, please use `check_mode: no` instead.

## [Deprecated](porting_guide_2.6.md#id4)

- In the [nxos_igmp_interface module](https://docs.ansible.com/ansible/2.9/modules/nxos_igmp_interface_module.html#nxos-igmp-interface-module "(in Ansible v2.9)"), `oif_prefix` and `oif_source` properties are deprecated. Use `ois_ps` parameter with a dictionary of prefix and source to values instead.

## [Modules](porting_guide_2.6.md#id5)

Major changes in popular modules are detailed here:

### [Modules removed](porting_guide_2.6.md#id6)

The following modules no longer exist:

### [Deprecation notices](porting_guide_2.6.md#id7)

The following modules will be removed in Ansible 2.10. Please update your playbooks accordingly.

- `k8s_raw` use [k8s](https://docs.ansible.com/ansible/2.9/modules/k8s_module.html#k8s-module "(in Ansible v2.9)") instead.
- `openshift_raw` use [k8s](https://docs.ansible.com/ansible/2.9/modules/k8s_module.html#k8s-module "(in Ansible v2.9)") instead.
- `openshift_scale` use [k8s_scale](https://docs.ansible.com/ansible/2.9/modules/k8s_scale_module.html#k8s-scale-module "(in Ansible v2.9)") instead.

### [Noteworthy module changes](porting_guide_2.6.md#id8)

- The `upgrade` module option for `win_chocolatey` has been removed; use `state: latest` instead.
- The `reboot` module option for `win_feature` has been removed; use the `win_reboot` action plugin instead.
- The `win_iis_webapppool` module no longer accepts a string for the `attributes` module option; use the free form dictionary value instead.
- The `name` module option for `win_package` has been removed; this is not used anywhere and should just be removed from your playbooks.
- The `win_regedit` module no longer automatically corrects the hive path `HCCC` to `HKCC`; use `HKCC` because this is the correct hive path.
- The [file_module](https://docs.ansible.com/ansible/6/collections/ansible/builtin/file_module.html#file-module "(in Ansible v6)") now emits a deprecation warning when `src` is specified with a state
  other than `hard` or `link` as it is only supposed to be useful with those. This could have
  an effect on people who were depending on a buggy interaction between src and other state’s to
  place files into a subdirectory. For instance:

  ```YAML+Jinja
  $ ansible localhost -m file -a 'path=/var/lib src=/tmp/ state=directory'
  ```

  Would create a directory named `/tmp/lib`. Instead of the above, simply spell out the entire
  destination path like this:

  ```YAML+Jinja
  $ ansible localhost -m file -a 'path=/tmp/lib state=directory'
  ```
- The `k8s_raw` and `openshift_raw` modules have been aliased to the new `k8s` module.
- The `k8s` module supports all Kubernetes resources including those from Custom Resource Definitions and aggregated API servers. This includes all OpenShift resources.
- The `k8s` module will not accept resources where subkeys have been snake_cased. This was a workaround that was suggested with the `k8s_raw` and `openshift_raw` modules.
- The `k8s` module may not accept resources where the `api_version` has been changed to match the shortened version in the Kubernetes Python client. You should now specify the proper full Kubernetes `api_version` for a resource.
- The `k8s` module can now process multi-document YAML files if they are passed with the `src` parameter. It will process each document as a separate resource. Resources provided inline with the `resource_definition` parameter must still be a single document.
- The `k8s` module will not automatically change `Project` creation requests into `ProjectRequest` creation requests as the `openshift_raw` module did. You must now specify the `ProjectRequest` kind explicitly.
- The `k8s` module will not automatically remove secrets from the Ansible return values (and by extension the log). In order to prevent secret values in a task from being logged, specify the `no_log` parameter on the task block.
- The `k8s_scale` module now supports scalable OpenShift objects, such as `DeploymentConfig`.
- The `lineinfile` module was changed to show a warning when using an empty string as a regexp.
  Since an empty regexp matches every line in a file, it will replace the last line in a file rather
  than inserting. If this is the desired behavior, use `'^'` which will match every line and
  will not trigger the warning.
- Openstack modules are no longer using `shade` library. Instead `openstacksdk` is used. Since `openstacksdk` should be already present as a dependency to `shade` no additional actions are required.

## [Plugins](porting_guide_2.6.md#id9)

### [Deprecation notices](porting_guide_2.6.md#id10)

The following modules will be removed in Ansible 2.10. Please update your playbooks accordingly.

- `openshift` use `k8s` instead.

### [Noteworthy plugin changes](porting_guide_2.6.md#id11)

- The `k8s` lookup plugin now supports all Kubernetes resources including those from Custom Resource Definitions and aggregated API servers. This includes all OpenShift resources.
- The `k8s` lookup plugin may not accept resources where the `api_version` has been changed to match the shortened version in the Kubernetes Python client. You should now specify the proper full Kubernetes `api_version` for a resource.
- The `k8s` lookup plugin will no longer remove secrets from the Ansible return values (and by extension the log). In order to prevent secret values in a task from being logged, specify the `no_log` parameter on the task block.

## [Porting custom scripts](porting_guide_2.6.md#id12)

No notable changes.

## [Networking](porting_guide_2.6.md#id13)

No notable changes.

## [Dynamic inventory scripts](porting_guide_2.6.md#id14)

- `contrib/inventory/openstack.py` has been renamed to `contrib/inventory/openstack_inventory.py`. If you have used `openstack.py` as a name for your OpenStack dynamic inventory file, change it to `openstack_inventory.py`. Otherwise the file name will conflict with imports from `openstacksdk`.
