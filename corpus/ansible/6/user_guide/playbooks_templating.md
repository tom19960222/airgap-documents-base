---
collection: ansible
version: "6"
title: "Templating (Jinja2)"
source_url: https://docs.ansible.com/projects/ansible/6/user_guide/playbooks_templating.html
fetched_at: 2026-07-27T16:40:32+00:00
---
# Templating (Jinja2)

Ansible uses Jinja2 templating to enable dynamic expressions and access to [variables](playbooks_variables.md#playbooks-variables) and [facts](playbooks_vars_facts.md#vars-and-facts). You can use templating with the [template module](../collections/ansible/builtin/template_module.md#template-module). For example, you can create a template for a configuration file, then deploy that configuration file to multiple environments and supply the correct data (IP address, hostname, version) for each environment. You can also use templating in playbooks directly, by templating task names and more. You can use all the [standard filters and tests](https://jinja.palletsprojects.com/en/3.1.x/templates/#builtin-filters "(in Jinja v3.1.x)") included in Jinja2. Ansible includes additional specialized filters for selecting and transforming data, tests for evaluating template expressions, and [Lookup plugins](../plugins/lookup.md#lookup-plugins) for retrieving data from external sources such as files, APIs, and databases for use in templating.

All templating happens on the Ansible controller **before** the task is sent and executed on the target machine. This approach minimizes the package requirements on the target (jinja2 is only required on the controller). It also limits the amount of data Ansible passes to the target machine. Ansible parses templates on the controller and passes only the information needed for each task to the target machine, instead of passing all the data on the controller and parsing it on the target.

> **Note:**
>
> Files and data used by the [template module](../collections/ansible/builtin/template_module.md#template-module) must be utf-8 encoded.

- [Get the current time](playbooks_templating.md#get-the-current-time)

- [Using filters to manipulate data](playbooks_filters.md)
  - [Handling undefined variables](playbooks_filters.md#handling-undefined-variables)
  - [Defining different values for true/false/null (ternary)](playbooks_filters.md#defining-different-values-for-true-false-null-ternary)
  - [Managing data types](playbooks_filters.md#managing-data-types)
  - [Formatting data: YAML and JSON](playbooks_filters.md#formatting-data-yaml-and-json)
  - [Combining and selecting data](playbooks_filters.md#combining-and-selecting-data)
  - [Randomizing data](playbooks_filters.md#randomizing-data)
  - [Managing list variables](playbooks_filters.md#managing-list-variables)
  - [Selecting from sets or lists (set theory)](playbooks_filters.md#selecting-from-sets-or-lists-set-theory)
  - [Calculating numbers (math)](playbooks_filters.md#calculating-numbers-math)
  - [Managing network interactions](playbooks_filters.md#managing-network-interactions)
  - [Hashing and encrypting strings and passwords](playbooks_filters.md#hashing-and-encrypting-strings-and-passwords)
  - [Manipulating text](playbooks_filters.md#manipulating-text)
  - [Manipulating strings](playbooks_filters.md#manipulating-strings)
  - [Managing UUIDs](playbooks_filters.md#managing-uuids)
  - [Handling dates and times](playbooks_filters.md#handling-dates-and-times)
  - [Getting Kubernetes resource names](playbooks_filters.md#getting-kubernetes-resource-names)
- [Tests](playbooks_tests.md)
  - [Test syntax](playbooks_tests.md#test-syntax)
  - [Testing strings](playbooks_tests.md#testing-strings)
  - [Vault](playbooks_tests.md#vault)
  - [Testing truthiness](playbooks_tests.md#testing-truthiness)
  - [Comparing versions](playbooks_tests.md#comparing-versions)
  - [Set theory tests](playbooks_tests.md#set-theory-tests)
  - [Testing if a list contains a value](playbooks_tests.md#testing-if-a-list-contains-a-value)
  - [Testing if a list value is True](playbooks_tests.md#testing-if-a-list-value-is-true)
  - [Testing paths](playbooks_tests.md#testing-paths)
  - [Testing size formats](playbooks_tests.md#testing-size-formats)
  - [Testing task results](playbooks_tests.md#testing-task-results)
  - [Type Tests](playbooks_tests.md#type-tests)
- [Lookups](playbooks_lookups.md)
  - [Using lookups in variables](playbooks_lookups.md#using-lookups-in-variables)
- [Python3 in templates](playbooks_python_version.md)
  - [Dictionary views](playbooks_python_version.md#dictionary-views)
  - [dict.iteritems()](playbooks_python_version.md#dict-iteritems)

## [Get the current time](playbooks_templating.md#id1)

New in version 2.8.

The `now()` Jinja2 function retrieves a Python datetime object or a string representation for the current time.

The `now()` function supports 2 arguments:

utc
:   Specify `True` to get the current time in UTC. Defaults to `False`.

fmt
:   Accepts a [strftime](https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior) string that returns a formatted date time string.

> **See also:**
>
> [Intro to playbooks](playbooks_intro.md#playbooks-intro)
> :   An introduction to playbooks
>
> [Conditionals](playbooks_conditionals.md#playbooks-conditionals)
> :   Conditional statements in playbooks
>
> [Loops](playbooks_loops.md#playbooks-loops)
> :   Looping in playbooks
>
> [Roles](playbooks_reuse_roles.md#playbooks-reuse-roles)
> :   Playbook organization by roles
>
> [Tips and tricks](playbooks_best_practices.md#playbooks-best-practices)
> :   Tips and tricks for playbooks
>
> [Jinja2 Docs](https://jinja.palletsprojects.com/en/latest/templates/)
> :   Jinja2 documentation, includes the syntax and semantics of the templates
>
> [User Mailing List](https://groups.google.com/group/ansible-devel)
> :   Have a question? Stop by the google group!
>
> [Real-time chat](../community/communication.md#communication-irc)
> :   How to join Ansible chat channels
