---
collection: ansible
version: "8"
title: "Run Your First Command and Playbook"
source_url: https://docs.ansible.com/projects/ansible/8/network/getting_started/first_playbook.html
fetched_at: 2026-07-28T00:59:22+00:00
---
# Run Your First Command and Playbook

Put the concepts you learned to work with this quick tutorial. Install Ansible, execute a network configuration command manually, execute the same command with Ansible, then create a playbook so you can execute the command any time on multiple network devices.

- [Prerequisites](first_playbook.md#prerequisites)
- [Install Ansible](first_playbook.md#install-ansible)
- [Establish a manual connection to a managed node](first_playbook.md#establish-a-manual-connection-to-a-managed-node)
- [Run your first network Ansible command](first_playbook.md#run-your-first-network-ansible-command)
- [Create and run your first network Ansible Playbook](first_playbook.md#create-and-run-your-first-network-ansible-playbook)
- [Gathering facts from network devices](first_playbook.md#gathering-facts-from-network-devices)

## [Prerequisites](first_playbook.md#id1)

Before you work through this tutorial you need:

- Ansible 2.10 (or higher) installed
- One or more network devices that are compatible with Ansible
- Basic Linux command line knowledge
- Basic knowledge of network switch & router configuration

## [Install Ansible](first_playbook.md#id2)

Install Ansible using your preferred method. See [Installing Ansible](../../installation_guide/intro_installation.md#installation-guide). Then return to this tutorial.

Confirm the version of Ansible (must be >= 2.10):

```bash
ansible --version
```

## [Establish a manual connection to a managed node](first_playbook.md#id3)

To confirm your credentials, connect to a network device manually and retrieve its configuration. Replace the sample user and device name with your real credentials. For example, for a VyOS router:

```bash
ssh my_vyos_user@vyos.example.net
show config
exit
```

This manual connection also establishes the authenticity of the network device, adding its RSA key fingerprint to your list of known hosts. (If you have connected to the device before, you have already established its authenticity.)

## [Run your first network Ansible command](first_playbook.md#id4)

Instead of manually connecting and running a command on the network device, you can retrieve its configuration with a single, stripped-down Ansible command:

```bash
ansible all -i vyos.example.net, -c ansible.netcommon.network_cli -u my_vyos_user -k -m vyos.vyos.vyos_facts -e ansible_network_os=vyos.vyos.vyos
```

The flags in this command set seven values:
:   - the host group(s) to which the command should apply (in this case, all)
    - the inventory (-i, the device or devices to target - without the trailing comma -i points to an inventory file)
    - the connection method (-c, the method for connecting and executing ansible)
    - the user (-u, the username for the SSH connection)
    - the SSH connection method (-k, please prompt for the password)
    - the module (-m, the Ansible module to run, using the fully qualified collection name (FQCN))
    - an extra variable ( -e, in this case, setting the network OS value)

NOTE: If you use `ssh-agent` with ssh keys, Ansible loads them automatically. You can omit `-k` flag.

> **Note:**
>
> If you are running Ansible in a virtual environment, you will also need to add the variable `ansible_python_interpreter=/path/to/venv/bin/python`

## [Create and run your first network Ansible Playbook](first_playbook.md#id5)

If you want to run this command every day, you can save it in a playbook and run it with `ansible-playbook` instead of `ansible`. The playbook can store a lot of the parameters you provided with flags at the command line, leaving less to type at the command line. You need two files for this - a playbook and an inventory file.

1. Download [`first_playbook.yml`](../../_downloads/588d4b6e9316c8eb903fbe2485b14d64/first_playbook.yml.md), which looks like this:

```YAML
---

- name: Network Getting Started First Playbook
  connection: ansible.netcommon.network_cli
  gather_facts: false
  hosts: all
  tasks:

    - name: Get config for VyOS devices
      vyos.vyos.vyos_facts:
        gather_subset: all

    - name: Display the config
      debug:
        msg: "The hostname is {{ ansible_net_hostname }} and the OS is {{ ansible_net_version }}"
```

The playbook sets three of the seven values from the command line above: the group (`hosts: all`), the connection method (`connection: ansible.netcommon.network_cli`) and the module (in each task). With those values set in the playbook, you can omit them on the command line. The playbook also adds a second task to show the config output. When a module runs in a playbook, the output is held in memory for use by future tasks instead of written to the console. The debug task here lets you see the results in your shell.

2. Run the playbook with the command:

```bash
ansible-playbook -i vyos.example.net, -u ansible -k -e ansible_network_os=vyos.vyos.vyos first_playbook.yml
```

The playbook contains one play with two tasks, and should generate output like this:

```shell
$ ansible-playbook -i vyos.example.net, -u ansible -k -e ansible_network_os=vyos.vyos.vyos first_playbook.yml

PLAY [Network Getting Started First Playbook]
***************************************************************************************************************************

TASK [Get config for VyOS devices]
***************************************************************************************************************************
ok: [vyos.example.net]

TASK [Display the config]
***************************************************************************************************************************
ok: [vyos.example.net] => {
    "msg": "The hostname is vyos and the OS is VyOS 1.1.8"
}
```

3. Now that you can retrieve the device config, try updating it with Ansible. Download [`first_playbook_ext.yml`](../../_downloads/47cc11a5d29fe635cb56cb6e1cd74e0f/first_playbook_ext.yml.md), which is an extended version of the first playbook:

```YAML
---

- name: Network Getting Started First Playbook Extended
  connection: ansible.netcommon.network_cli
  gather_facts: false
  hosts: all
  tasks:

    - name: Get config for VyOS devices
      vyos.vyos.vyos_facts:
        gather_subset: all

    - name: Display the config
      debug:
        msg: "The hostname is {{ ansible_net_hostname }} and the OS is {{ ansible_net_version }}"

    - name: Update the hostname
      vyos.vyos.vyos_config:
        backup: yes
        lines:
          - set system host-name vyos-changed

    - name: Get changed config for VyOS devices
      vyos.vyos.vyos_facts:
        gather_subset: all

    - name: Display the changed config
      debug:
        msg: "The new hostname is {{ ansible_net_hostname }} and the OS is {{ ansible_net_version }}"
```

The extended first playbook has five tasks in a single play. Run it with the same command you used above. The output shows you the change Ansible made to the config:

```shell
$ ansible-playbook -i vyos.example.net, -u ansible -k -e ansible_network_os=vyos.vyos.vyos first_playbook_ext.yml

PLAY [Network Getting Started First Playbook Extended]
************************************************************************************************************************************

TASK [Get config for VyOS devices]
**********************************************************************************************************************************
ok: [vyos.example.net]

TASK [Display the config]
*************************************************************************************************************************************
ok: [vyos.example.net] => {
    "msg": "The hostname is vyos and the OS is VyOS 1.1.8"
}

TASK [Update the hostname]
*************************************************************************************************************************************
changed: [vyos.example.net]

TASK [Get changed config for VyOS devices]
*************************************************************************************************************************************
ok: [vyos.example.net]

TASK [Display the changed config]
*************************************************************************************************************************************
ok: [vyos.example.net] => {
    "msg": "The new hostname is vyos-changed and the OS is VyOS 1.1.8"
}

PLAY RECAP
************************************************************************************************************************************
vyos.example.net           : ok=5    changed=1    unreachable=0    failed=0
```

## [Gathering facts from network devices](first_playbook.md#id6)

The `gather_facts` keyword now supports gathering network device facts in standardized key/value pairs. You can feed these network facts into further tasks to manage the network device.

You can also use the new `gather_network_resources` parameter with the network `*_facts` modules (such as [arista.eos.eos_facts](../../collections/arista/eos/eos_facts_module.md#ansible-collections-arista-eos-eos-facts-module)) to return just a subset of the device configuration, as shown below.

```yaml
- hosts: arista
  gather_facts: True
  gather_subset: interfaces
  module_defaults:
    arista.eos.eos_facts:
      gather_network_resources: interfaces
```

The playbook returns the following interface facts:

```yaml
"network_resources": {
      "interfaces": [
          {
              "description": "test-interface",
              "enabled": true,
              "mtu": "512",
              "name": "Ethernet1"
          },
          {
              "enabled": true,
              "mtu": "3000",
              "name": "Ethernet2"
          },
          {
              "enabled": true,
              "name": "Ethernet3"
          },
          {
              "enabled": true,
              "name": "Ethernet4"
          },
          {
              "enabled": true,
              "name": "Ethernet5"
          },
          {
              "enabled": true,
              "name": "Ethernet6"
          },
      ]
  }
```

Note that this returns a subset of what is returned by just setting `gather_subset: interfaces`.

You can store these facts and use them directly in another task, such as with the [eos_interfaces](../../collections/arista/eos/eos_interfaces_module.md#ansible-collections-arista-eos-eos-interfaces-module) resource module.
