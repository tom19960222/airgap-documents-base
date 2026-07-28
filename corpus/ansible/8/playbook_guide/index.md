---
collection: ansible
version: "8"
title: "Using Ansible playbooks"
source_url: https://docs.ansible.com/projects/ansible/8/playbook_guide/index.html
fetched_at: 2026-07-28T00:57:42+00:00
---
# Using Ansible playbooks

> **Note:**
>
> **Making Open Source More Inclusive**
>
> Red Hat is committed to replacing problematic language in our code, documentation, and web properties. We are beginning with these four terms: master, slave, blacklist, and whitelist. We ask that you open an issue or pull request if you come upon a term that we have missed. For more details, see [our CTO Chris Wright’s message](https://www.redhat.com/en/blog/making-open-source-more-inclusive-eradicating-problematic-language).

Welcome to the Ansible playbooks guide.
Playbooks are automation blueprints, in `YAML` format, that Ansible uses to deploy and configure nodes in an inventory.
This guide introduces you to playbooks and then covers different use cases for tasks and plays, such as:

- Executing tasks with elevated privileges or as a different user.
- Using loops to repeat tasks for items in a list.
- Delegating playbooks to execute tasks on different machines.
- Running conditional tasks and evaluating conditions with playbook tests.
- Using blocks to group sets of tasks.

You can also learn how to use Ansible playbooks more effectively by using collections, creating reusable files and roles, including and importing playbooks, and running selected parts of a playbook with tags.

- [Ansible playbooks](playbooks_intro.md)
  - [Playbook syntax](playbooks_intro.md#playbook-syntax)
  - [Playbook execution](playbooks_intro.md#playbook-execution)
  - [Ansible-Pull](playbooks_intro.md#ansible-pull)
  - [Verifying playbooks](playbooks_intro.md#verifying-playbooks)
- [Working with playbooks](playbooks.md)
  - [Templating (Jinja2)](playbooks_templating.md)
  - [Using filters to manipulate data](playbooks_filters.md)
  - [Tests](playbooks_tests.md)
  - [Lookups](playbooks_lookups.md)
  - [Python3 in templates](playbooks_python_version.md)
  - [The now function: get the current time](playbooks_templating_now.md)
  - [Loops](playbooks_loops.md)
  - [Controlling where tasks run: delegation and local actions](playbooks_delegation.md)
  - [Conditionals](playbooks_conditionals.md)
  - [Blocks](playbooks_blocks.md)
  - [Handlers: running operations on change](playbooks_handlers.md)
  - [Error handling in playbooks](playbooks_error_handling.md)
  - [Setting the remote environment](playbooks_environment.md)
  - [Working with language-specific version managers](playbooks_environment.md#working-with-language-specific-version-managers)
  - [Re-using Ansible artifacts](playbooks_reuse.md)
  - [Roles](playbooks_reuse_roles.md)
  - [Module defaults](playbooks_module_defaults.md)
  - [Interactive input: prompts](playbooks_prompts.md)
  - [Using Variables](playbooks_variables.md)
  - [Discovering variables: facts and magic variables](playbooks_vars_facts.md)
  - [Playbook Example: Continuous Delivery and Rolling Upgrades](guide_rolling_upgrade.md)
- [Executing playbooks](playbooks_execution.md)
  - [Validating tasks: check mode and diff mode](playbooks_checkmode.md)
  - [Understanding privilege escalation: become](playbooks_privilege_escalation.md)
  - [Tags](playbooks_tags.md)
  - [Executing playbooks for troubleshooting](playbooks_startnstep.md)
  - [Debugging tasks](playbooks_debugger.md)
  - [Asynchronous actions and polling](playbooks_async.md)
  - [Controlling playbook execution: strategies and more](playbooks_strategies.md)
- [Advanced playbook syntax](playbooks_advanced_syntax.md)
  - [Unsafe or raw strings](playbooks_advanced_syntax.md#unsafe-or-raw-strings)
  - [YAML anchors and aliases: sharing variable values](playbooks_advanced_syntax.md#yaml-anchors-and-aliases-sharing-variable-values)
- [Manipulating data](complex_data_manipulation.md)
  - [Loops and list comprehensions](complex_data_manipulation.md#loops-and-list-comprehensions)
  - [Complex Type transformations](complex_data_manipulation.md#complex-type-transformations)
