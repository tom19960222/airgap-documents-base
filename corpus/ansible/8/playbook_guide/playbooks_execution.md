---
collection: ansible
version: "8"
title: "Executing playbooks"
source_url: https://docs.ansible.com/projects/ansible/8/playbook_guide/playbooks_execution.html
fetched_at: 2026-07-28T00:58:33+00:00
---
# Executing playbooks

Ready to run your Ansible playbook?

Running complex playbooks requires some trial and error so learn about some of the abilities that Ansible gives you to ensure successful execution.
You can validate your tasks with “dry run” playbooks, use the start-at-task and step mode options to efficiently troubleshoot playbooks.
You can also use Ansible debugger to correct tasks during execution.
Ansible also offers flexibility with asynchronous playbook execution and tags that let you run specific parts of your playbook.

- [Validating tasks: check mode and diff mode](playbooks_checkmode.md)
  - [Using check mode](playbooks_checkmode.md#using-check-mode)
  - [Using diff mode](playbooks_checkmode.md#using-diff-mode)
- [Understanding privilege escalation: become](playbooks_privilege_escalation.md)
  - [Using become](playbooks_privilege_escalation.md#using-become)
  - [Risks and limitations of become](playbooks_privilege_escalation.md#risks-and-limitations-of-become)
  - [Become and network automation](playbooks_privilege_escalation.md#become-and-network-automation)
  - [Become and Windows](playbooks_privilege_escalation.md#become-and-windows)
- [Tags](playbooks_tags.md)
  - [Adding tags with the tags keyword](playbooks_tags.md#adding-tags-with-the-tags-keyword)
  - [Special tags: always and never](playbooks_tags.md#special-tags-always-and-never)
  - [Selecting or skipping tags when you run a playbook](playbooks_tags.md#selecting-or-skipping-tags-when-you-run-a-playbook)
- [Executing playbooks for troubleshooting](playbooks_startnstep.md)
  - [start-at-task](playbooks_startnstep.md#start-at-task)
  - [Step mode](playbooks_startnstep.md#step-mode)
- [Debugging tasks](playbooks_debugger.md)
  - [Enabling the debugger](playbooks_debugger.md#enabling-the-debugger)
  - [Resolving errors in the debugger](playbooks_debugger.md#resolving-errors-in-the-debugger)
  - [Available debug commands](playbooks_debugger.md#available-debug-commands)
  - [How the debugger interacts with the free strategy](playbooks_debugger.md#how-the-debugger-interacts-with-the-free-strategy)
- [Asynchronous actions and polling](playbooks_async.md)
  - [Asynchronous ad hoc tasks](playbooks_async.md#asynchronous-ad-hoc-tasks)
  - [Asynchronous playbook tasks](playbooks_async.md#asynchronous-playbook-tasks)
- [Controlling playbook execution: strategies and more](playbooks_strategies.md)
  - [Selecting a strategy](playbooks_strategies.md#selecting-a-strategy)
  - [Setting the number of forks](playbooks_strategies.md#setting-the-number-of-forks)
  - [Using keywords to control execution](playbooks_strategies.md#using-keywords-to-control-execution)
