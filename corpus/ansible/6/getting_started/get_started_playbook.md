---
collection: ansible
version: "6"
title: "Creating a playbook"
source_url: https://docs.ansible.com/projects/ansible/6/getting_started/get_started_playbook.html
fetched_at: 2026-07-27T16:39:38+00:00
---
# Creating a playbook

Playbooks are automation blueprints, in `YAML` format, that Ansible uses to deploy and configure managed nodes.

Playbook
:   A list of plays that define the order in which Ansible performs operations, from top to bottom, to achieve an overall goal.

Play
:   An ordered list of tasks that maps to managed nodes in an inventory.

Task
:   A list of one or more modules that defines the operations that Ansible performs.

Module
:   A unit of code or binary that Ansible runs on managed nodes.
    Ansible modules are grouped in collections with a [Fully Qualified Collection Name (FQCN)](../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) for each module.

In the previous section, you used the `ansible` command to ping hosts in your inventory.
Now let’s create a playbook that pings your hosts and also prints a “Hello world” message.

Complete the following steps:

1. Open a terminal window on your control node.
2. Create a new playbook file named `playbook.yaml` in any directory and open it for editing.
3. Add the following content to `playbook.yaml`:

   ```yaml
   - name: My first play
     hosts: virtualmachines
     tasks:
      - name: Ping my hosts
        ansible.builtin.ping:
      - name: Print message
        ansible.builtin.debug:
          msg: Hello world
   ```
4. Run your playbook.

   ```bash
   ansible-playbook -i inventory.yaml playbook.yaml
   ```

Ansible returns the following output:

```
PLAY [My first play] **********************************************************************

TASK [Gathering Facts] ********************************************************************
ok: [vm01]
ok: [vm02]
ok: [vm03]

TASK [Ping my hosts] **********************************************************************
ok: [vm01]
ok: [vm02]
ok: [vm03]

TASK [Print message] **********************************************************************
ok: [vm01] => {
    "msg": "Hello world"
}
ok: [vm02] => {
    "msg": "Hello world"
}
ok: [vm03] => {
    "msg": "Hello world"
}

PLAY RECAP ********************************************************************************
vm01: ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
vm02: ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
vm03: ok=3    changed=0    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

In this output you can see:

- The names that you give the play and each task.
  You should always use descriptive names that make it easy to verify and troubleshoot playbooks.
- The `Gather Facts` task runs implicitly.
  By default Ansible gathers information about your inventory that it can use in the playbook.
- The status of each task.
  Each task has a status of `ok` which means it ran successfully.
- The play recap that summarizes results of all tasks in the playbook per host.
  In this example, there are three tasks so `ok=3` indicates that each task ran successfully.

Congratulations! You have just created your first Ansible playbook.

> **See also:**
>
> [Intro to playbooks](../user_guide/playbooks_intro.md#playbooks-intro)
> :   Start building playbooks for real world scenarios.
>
> [Working with playbooks](../user_guide/playbooks.md#working-with-playbooks)
> :   Go into more detail with Ansible playbooks.
>
> [Tips and tricks](../user_guide/playbooks_best_practices.md#playbooks-best-practices)
> :   Get tips and tricks for using playbooks.
>
> [Discovering variables: facts and magic variables](../user_guide/playbooks_vars_facts.md#vars-and-facts)
> :   Learn more about the `gather_facts` keyword in playbooks.
