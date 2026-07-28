---
collection: ansible
version: "8"
title: "Guidelines for VMware module development"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/vmware/docsite/dev_guide.html
fetched_at: 2026-07-28T01:00:40+00:00
---
# Guidelines for VMware module development

The Ansible VMware collection (on [Galaxy](https://galaxy.ansible.com/community/vmware), source code [repository](https://github.com/ansible-collections/community.vmware)) is maintained by the VMware Working Group. For more information see the [team community page](https://github.com/ansible/community/wiki/VMware).

- [Testing with your own infrastructure](dev_guide.md#testing-with-your-own-infrastructure)

  - [Requirements](dev_guide.md#requirements)

    - [NFS server configuration](dev_guide.md#nfs-server-configuration)
  - [Configure your installation](dev_guide.md#configure-your-installation)
  - [Using an HTTP proxy](dev_guide.md#using-an-http-proxy)
  - [Run the test-suite](dev_guide.md#run-the-test-suite)
- [Unit-test](dev_guide.md#unit-test)
- [Code style and best practice](dev_guide.md#code-style-and-best-practice)

  - [datacenter argument with ESXi](dev_guide.md#datacenter-argument-with-esxi)
  - [esxi_hostname should not be mandatory](dev_guide.md#esxi-hostname-should-not-be-mandatory)
  - [Example should use the fully qualified collection name (FQCN)](dev_guide.md#example-should-use-the-fully-qualified-collection-name-fqcn)
  - [Functional tests](dev_guide.md#functional-tests)

    - [Writing new tests](dev_guide.md#writing-new-tests)
    - [No need to create too much resources](dev_guide.md#no-need-to-create-too-much-resources)
    - [VM names should be predictable](dev_guide.md#vm-names-should-be-predictable)
    - [Avoid the common boiler plate code in your test playbook](dev_guide.md#avoid-the-common-boiler-plate-code-in-your-test-playbook)
- [Typographic convention](dev_guide.md#typographic-convention)

  - [Nomenclature](dev_guide.md#nomenclature)

## [Testing with your own infrastructure](dev_guide.md#id1)

You can target a regular VMware environment. This paragraph explains step by step how you can run the test-suite yourself.

### [Requirements](dev_guide.md#id2)

- 2 ESXi hosts (6.5 or 6.7)
  :   - with 2 NIC, the second ones should be available for the test
- a VCSA host
- a NFS server
- Python dependencies:
  :   - [pyvmomi](https://github.com/vmware/pyvmomi/tree/master/pyVmomi)
      - [requests](https://2.python-requests.org/en/master/)

If you want to deploy your test environment in a hypervisor, both [VMware or Libvirt](https://github.com/goneri/vmware-on-libvirt) work well.

#### [NFS server configuration](dev_guide.md#id3)

Your NFS server must expose the following directory structure:

```shell
$ tree /srv/share/
/srv/share/
├── isos
│   ├── base.iso
│   ├── centos.iso
│   └── fedora.iso
└── vms
2 directories, 3 files
```

On a Linux system, you can expose the directory over NFS with the following export file:

```shell
$ cat /etc/exports
/srv/share  192.168.122.0/255.255.255.0(rw,anonuid=1000,anongid=1000)
```

> **Note:**
>
> With this configuration all the new files will be owned by the user with the UID and GID 1000/1000.
> Adjust the configuration to match your user’s UID/GID.

The service can be enabled with:

```shell
$ sudo systemctl enable --now nfs-server
```

### [Configure your installation](dev_guide.md#id4)

Prepare a configuration file that describes your set-up. The file
should be called test/integration/cloud-config-vcenter.ini and based on
test/lib/ansible_test/config/cloud-config-vcenter.ini.template. For instance, if you have deployed your lab with
[vmware-on-libvirt](https://github.com/goneri/vmware-on-libvirt):

```ini
[DEFAULT]
vcenter_username: administrator@vsphere.local
vcenter_password: !234AaAa56
vcenter_hostname: vcenter.test
vmware_validate_certs: false
esxi1_hostname: esxi1.test
esxi1_username: root
esxi1_password: root
esxi2_hostname: test2.test
esxi2_username: root
esxi2_password: root
```

### [Using an HTTP proxy](dev_guide.md#id5)

Hosting test infrastructure behind an HTTP proxy is supported. You can specify the location of the proxy server with the two extra keys:

```ini
vmware_proxy_host: esxi1-gw.ws.testing.ansible.com
vmware_proxy_port: 11153
```

In addition, you may need to adjust the variables of the following [var files](https://github.com/ansible-collections/community.vmware/tree/main/tests/integration/targets/prepare_vmware_tests/vars) to match the configuration of your lab. If you use vmware-on-libvirt to prepare your lab, you do not have anything to change.

### [Run the test-suite](dev_guide.md#id6)

Once your configuration is ready, you can trigger a run with the following command:

```shell
source hacking/env-setup
VMWARE_TEST_PLATFORM=static ansible-test integration --python 3.7 vmware_host_firewall_manager
```

`vmware_host_firewall_manager` is the name of the module to test.

`vmware_guest` is much larger than any other test role and is rather slow. You can enable or disable some of its test playbooks in [main.yml](https://github.com/ansible-collections/community.vmware/tree/main/tests/integration/targets/vmware_guest/defaults/main.yml).

## [Unit-test](dev_guide.md#id7)

The VMware modules have limited unit-test coverage. You can run the test suite with the
following commands:

```shell
source hacking/env-setup
ansible-test units --venv --python 3.7 '.*vmware.*'
```

## [Code style and best practice](dev_guide.md#id8)

### [datacenter argument with ESXi](dev_guide.md#id9)

The `datacenter` parameter should not use `ha-datacenter` by default. This is because the user may
not realize that Ansible silently targets the wrong data center.

### [esxi_hostname should not be mandatory](dev_guide.md#id10)

Depending upon the functionality provided by ESXi or vCenter, some modules can seamlessly work with both. In this case,
`esxi_hostname` parameter should be optional.

```python
if self.is_vcenter():
    esxi_hostname = module.params.get('esxi_hostname')
    if not esxi_hostname:
        self.module.fail_json("esxi_hostname parameter is mandatory")
    self.host = self.get_all_host_objs(cluster_name=cluster_name, esxi_host_name=esxi_hostname)[0]
else:
    self.host = find_obj(self.content, [vim.HostSystem], None)
if self.host is None:
    self.module.fail_json(msg="Failed to find host system.")
```

### [Example should use the fully qualified collection name (FQCN)](dev_guide.md#id11)

Use FQCN for examples within module documentation. For instance, you should use `community.vmware.vmware_guest` instead of just
`vmware_guest`.

This way, the examples do not depend on the `collections` directive of the
playbook.

### [Functional tests](dev_guide.md#id12)

#### [Writing new tests](dev_guide.md#id13)

If you are writing a new collection of integration tests, there are a few VMware-specific things to note beyond
the standard Ansible [integration testing](../../../../dev_guide/testing_integration.md#testing-integration) process.

The test-suite uses a set of common, pre-defined vars located [in prepare_vmware_tests](https://github.com/ansible-collections/community.vmware/tree/main/tests/integration/targets/test/integration/targets/prepare_vmware_tests/) role.
The resources defined there are automatically created by importing that role at the start of your test:

```yaml
- import_role:
    name: prepare_vmware_tests
  vars:
    setup_datacenter: true
```

This will give you a ready to use cluster, datacenter, datastores, folder, switch, dvswitch, ESXi hosts, and VMs.

#### [No need to create too much resources](dev_guide.md#id14)

Most of the time, it’s not necessary to use `with_items` to create multiple resources. By avoiding it,
you speed up the test execution and you simplify the clean up afterwards.

#### [VM names should be predictable](dev_guide.md#id15)

If you need to create a new VM during your test, you can use `test_vm1`, `test_vm2` or `test_vm3`. This
way it will be automatically clean up for you.

#### [Avoid the common boiler plate code in your test playbook](dev_guide.md#id16)

From Ansible 2.10, the test suite uses modules_defaults. This module
allow us to preinitialize the following default keys of the VMware modules:

- hostname
- username
- password
- validate_certs

For example, the following block:

```yaml
- name: Add a VMware vSwitch
  community.vmware.vmware_vswitch:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    validate_certs: 'no'
    esxi_hostname: 'esxi1'
    switch_name: "boby"
    state: present
```

should be simplified to just:

```yaml
- name: Add a VMware vSwitch
  community.vmware.vmware_vswitch:
    esxi_hostname: 'esxi1'
    switch_name: "boby"
    state: present
```

## [Typographic convention](dev_guide.md#id17)

### [Nomenclature](dev_guide.md#id18)

We try to enforce the following rules in our documentation:

- VMware, not VMWare or vmware
- ESXi, not esxi or ESXI
- vCenter, not vcenter or VCenter
