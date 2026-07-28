---
collection: ansible
version: "8"
title: "Using Variables"
source_url: https://docs.ansible.com/projects/ansible/8/playbook_guide/playbooks_variables.html
fetched_at: 2026-07-28T01:00:03+00:00
---
# Using Variables

Ansible uses variables to manage differences between systems. With Ansible, you can execute tasks and playbooks on multiple different systems with a single command. To represent the variations among those different systems, you can create variables with standard YAML syntax, including lists and dictionaries. You can define these variables in your playbooks, in your [inventory](../inventory_guide/intro_inventory.md#intro-inventory), in reusable [files](playbooks_reuse.md#playbooks-reuse) or [roles](playbooks_reuse_roles.md#playbooks-reuse-roles), or at the command line. You can also create variables during a playbook run by registering the return value or values of a task as a new variable.

After you create variables, either by defining them in a file, passing them at the command line, or registering the return value or values of a task as a new variable, you can use those variables in module arguments, in [conditional “when” statements](playbooks_conditionals.md#playbooks-conditionals), in [templates](playbooks_templating.md#playbooks-templating), and in [loops](playbooks_loops.md#playbooks-loops). The [ansible-examples GitHub repository](https://github.com/ansible/ansible-examples) contains many examples of using variables in Ansible.

Once you understand the concepts and examples on this page, read about [Ansible facts](playbooks_vars_facts.md#vars-and-facts), which are variables you retrieve from remote systems.

- [Creating valid variable names](playbooks_variables.md#creating-valid-variable-names)
- [Simple variables](playbooks_variables.md#simple-variables)

  - [Defining simple variables](playbooks_variables.md#defining-simple-variables)
  - [Referencing simple variables](playbooks_variables.md#referencing-simple-variables)
- [When to quote variables (a YAML gotcha)](playbooks_variables.md#when-to-quote-variables-a-yaml-gotcha)
- [Boolean variables](playbooks_variables.md#boolean-variables)
- [List variables](playbooks_variables.md#list-variables)

  - [Defining variables as lists](playbooks_variables.md#defining-variables-as-lists)
  - [Referencing list variables](playbooks_variables.md#referencing-list-variables)
- [Dictionary variables](playbooks_variables.md#dictionary-variables)

  - [Defining variables as key:value dictionaries](playbooks_variables.md#defining-variables-as-key-value-dictionaries)
  - [Referencing key:value dictionary variables](playbooks_variables.md#referencing-key-value-dictionary-variables)
- [Registering variables](playbooks_variables.md#registering-variables)
- [Referencing nested variables](playbooks_variables.md#referencing-nested-variables)
- [Transforming variables with Jinja2 filters](playbooks_variables.md#transforming-variables-with-jinja2-filters)
- [Where to set variables](playbooks_variables.md#where-to-set-variables)

  - [Defining variables in inventory](playbooks_variables.md#defining-variables-in-inventory)
  - [Defining variables in a play](playbooks_variables.md#defining-variables-in-a-play)
  - [Defining variables in included files and roles](playbooks_variables.md#defining-variables-in-included-files-and-roles)
  - [Defining variables at runtime](playbooks_variables.md#defining-variables-at-runtime)

    - [key=value format](playbooks_variables.md#key-value-format)
    - [JSON string format](playbooks_variables.md#json-string-format)
    - [vars from a JSON or YAML file](playbooks_variables.md#vars-from-a-json-or-yaml-file)
- [Variable precedence: Where should I put a variable?](playbooks_variables.md#variable-precedence-where-should-i-put-a-variable)

  - [Understanding variable precedence](playbooks_variables.md#understanding-variable-precedence)
  - [Scoping variables](playbooks_variables.md#scoping-variables)
  - [Tips on where to set variables](playbooks_variables.md#tips-on-where-to-set-variables)
- [Using advanced variable syntax](playbooks_variables.md#using-advanced-variable-syntax)

## [Creating valid variable names](playbooks_variables.md#id18)

Not all strings are valid Ansible variable names. A variable name can only include letters, numbers, and underscores. [Python keywords](https://docs.python.org/3/reference/lexical_analysis.html#keywords) or [playbook keywords](../reference_appendices/playbooks_keywords.md#playbook-keywords) are not valid variable names. A variable name cannot begin with a number.

Variable names can begin with an underscore. In many programming languages, variables that begin with an underscore are private. This is not true in Ansible. Variables that begin with an underscore are treated exactly the same as any other variable. Do not rely on this convention for privacy or security.

This table gives examples of valid and invalid variable names:

| Valid variable names | Not valid |
| --- | --- |
| `foo` | `*foo`, [Python keywords](https://docs.python.org/3/reference/lexical_analysis.html#keywords) such as `async` and `lambda` |
| `foo_env` | [playbook keywords](../reference_appendices/playbooks_keywords.md#playbook-keywords) such as `environment` |
| `foo_port` | `foo-port`, `foo port`, `foo.port` |
| `foo5`, `_foo` | `5foo`, `12` |

## [Simple variables](playbooks_variables.md#id19)

Simple variables combine a variable name with a single value. You can use this syntax (and the syntax for lists and dictionaries shown below) in a variety of places. For details about setting variables in inventory, in playbooks, in reusable files, in roles, or at the command line, see [Where to set variables](playbooks_variables.md#setting-variables).

### [Defining simple variables](playbooks_variables.md#id20)

You can define a simple variable using standard YAML syntax. For example:

```
remote_install_path: /opt/my_app_config
```

### [Referencing simple variables](playbooks_variables.md#id21)

After you define a variable, use Jinja2 syntax to reference it. Jinja2 variables use double curly braces. For example, the expression `My amp goes to {{ max_amp_value }}` demonstrates the most basic form of variable substitution. You can use Jinja2 syntax in playbooks. For example:

```yaml+jinja
ansible.builtin.template:
  src: foo.cfg.j2
  dest: '{{ remote_install_path }}/foo.cfg'
```

In this example, the variable defines the location of a file, which can vary from one system to another.

> **Note:**
>
> Ansible allows Jinja2 loops and conditionals in [templates](playbooks_templating.md#playbooks-templating) but not in playbooks. You cannot create a loop of tasks. Ansible playbooks are pure machine-parseable YAML.

## [When to quote variables (a YAML gotcha)](playbooks_variables.md#id22)

If you start a value with `{{ foo }}`, you must quote the whole expression to create valid YAML syntax. If you do not quote the whole expression, the YAML parser cannot interpret the syntax - it might be a variable or it might be the start of a YAML dictionary. For guidance on writing YAML, see the [YAML Syntax](../reference_appendices/YAMLSyntax.md#yaml-syntax) documentation.

If you use a variable without quotes like this:

```yaml+jinja
- hosts: app_servers
  vars:
      app_path: {{ base_path }}/22
```

You will see: `ERROR! Syntax Error while loading YAML.` If you add quotes, Ansible works correctly:

```yaml+jinja
- hosts: app_servers
  vars:
       app_path: "{{ base_path }}/22"
```

## [Boolean variables](playbooks_variables.md#id23)

Ansible accepts a broad range of values for boolean variables: `true/false`, `1/0`, `yes/no`, `True/False` and so on. The matching of valid strings is case insensitive.
While documentation examples focus on `true/false` to be compatible with `ansible-lint` default settings, you can use any of the following:

| Valid values | Description |
| --- | --- |
| `True` , `'true'` , `'t'` , `'yes'` , `'y'` , `'on'` , `'1'` , `1` , `1.0` | Truthy values |
| `False` , `'false'` , `'f'` , `'no'` , `'n'` , `'off'` , `'0'` , `0` , `0.0` | Falsy values |

## [List variables](playbooks_variables.md#id24)

A list variable combines a variable name with multiple values. The multiple values can be stored as an itemized list or in square brackets `[]`, separated with commas.

### [Defining variables as lists](playbooks_variables.md#id25)

You can define variables with multiple values using YAML lists. For example:

```yaml
region:
  - northeast
  - southeast
  - midwest
```

### [Referencing list variables](playbooks_variables.md#id26)

When you use variables defined as a list (also called an array), you can use individual, specific fields from that list. The first item in a list is item 0, the second item is item 1. For example:

```yaml+jinja
region: "{{ region[0] }}"
```

The value of this expression would be “northeast”.

## [Dictionary variables](playbooks_variables.md#id27)

A dictionary stores the data in key-value pairs. Usually, dictionaries are used to store related data, such as the information contained in an ID or a user profile.

### [Defining variables as key:value dictionaries](playbooks_variables.md#id28)

You can define more complex variables using YAML dictionaries. A YAML dictionary maps keys to values. For example:

```yaml
foo:
  field1: one
  field2: two
```

### [Referencing key:value dictionary variables](playbooks_variables.md#id29)

When you use variables defined as a key:value dictionary (also called a hash), you can use individual, specific fields from that dictionary using either bracket notation or dot notation:

```yaml
foo['field1']
foo.field1
```

Both of these examples reference the same value (“one”). Bracket notation always works. Dot notation can cause problems because some keys collide with attributes and methods of python dictionaries. Use bracket notation if you use keys which start and end with two underscores (which are reserved for special meanings in python) or are any of the known public attributes:

`add`, `append`, `as_integer_ratio`, `bit_length`, `capitalize`, `center`, `clear`, `conjugate`, `copy`, `count`, `decode`, `denominator`, `difference`, `difference_update`, `discard`, `encode`, `endswith`, `expandtabs`, `extend`, `find`, `format`, `fromhex`, `fromkeys`, `get`, `has_key`, `hex`, `imag`, `index`, `insert`, `intersection`, `intersection_update`, `isalnum`, `isalpha`, `isdecimal`, `isdigit`, `isdisjoint`, `is_integer`, `islower`, `isnumeric`, `isspace`, `issubset`, `issuperset`, `istitle`, `isupper`, `items`, `iteritems`, `iterkeys`, `itervalues`, `join`, `keys`, `ljust`, `lower`, `lstrip`, `numerator`, `partition`, `pop`, `popitem`, `real`, `remove`, `replace`, `reverse`, `rfind`, `rindex`, `rjust`, `rpartition`, `rsplit`, `rstrip`, `setdefault`, `sort`, `split`, `splitlines`, `startswith`, `strip`, `swapcase`, `symmetric_difference`, `symmetric_difference_update`, `title`, `translate`, `union`, `update`, `upper`, `values`, `viewitems`, `viewkeys`, `viewvalues`, `zfill`.

## [Registering variables](playbooks_variables.md#id30)

You can create variables from the output of an Ansible task with the task keyword `register`. You can use registered variables in any later tasks in your play. For example:

```yaml
- hosts: web_servers

  tasks:

     - name: Run a shell command and register its output as a variable
       ansible.builtin.shell: /usr/bin/foo
       register: foo_result
       ignore_errors: true

     - name: Run a shell command using output of the previous task
       ansible.builtin.shell: /usr/bin/bar
       when: foo_result.rc == 5
```

For more examples of using registered variables in conditions on later tasks, see [Conditionals](playbooks_conditionals.md#playbooks-conditionals). Registered variables may be simple variables, list variables, dictionary variables, or complex nested data structures. The documentation for each module includes a `RETURN` section describing the return values for that module. To see the values for a particular task, run your playbook with `-v`.

Registered variables are stored in memory. You cannot cache registered variables for use in future playbook runs. Registered variables are only valid on the host for the rest of the current playbook run, including subsequent plays within the same playbook run.

Registered variables are host-level variables. When you register a variable in a task with a loop, the registered variable contains a value for each item in the loop. The data structure placed in the variable during the loop will contain a `results` attribute, that is a list of all responses from the module. For a more in-depth example of how this works, see the [Loops](playbooks_loops.md#playbooks-loops) section on using register with a loop.

> **Note:**
>
> If a task fails or is skipped, Ansible still registers a variable with a failure or skipped status, unless the task is skipped based on tags. See [Tags](playbooks_tags.md#tags) for information on adding and using tags.

## [Referencing nested variables](playbooks_variables.md#id31)

Many registered variables (and [facts](playbooks_vars_facts.md#vars-and-facts)) are nested YAML or JSON data structures. You cannot access values from these nested data structures with the simple `{{ foo }}` syntax. You must use either bracket notation or dot notation. For example, to reference an IP address from your facts using the bracket notation:

```yaml+jinja
{{ ansible_facts["eth0"]["ipv4"]["address"] }}
```

To reference an IP address from your facts using the dot notation:

```yaml+jinja
{{ ansible_facts.eth0.ipv4.address }}
```

## [Transforming variables with Jinja2 filters](playbooks_variables.md#id32)

Jinja2 filters let you transform the value of a variable within a template expression. For example, the `capitalize` filter capitalizes any value passed to it; the `to_yaml` and `to_json` filters change the format of your variable values. Jinja2 includes many [built-in filters](https://jinja.palletsprojects.com/templates/#builtin-filters) and Ansible supplies many more filters. To find more examples of filters, see [Using filters to manipulate data](playbooks_filters.md#playbooks-filters).

## [Where to set variables](playbooks_variables.md#id33)

You can define variables in a variety of places, such as in inventory, in playbooks, in reusable files, in roles, and at the command line. Ansible loads every possible variable it finds, then chooses the variable to apply based on [variable precedence rules](playbooks_variables.md#ansible-variable-precedence).

### [Defining variables in inventory](playbooks_variables.md#id34)

You can define different variables for each host individually, or set shared variables for a group of hosts in your inventory. For example, if all machines in the `[Boston]` group use ‘boston.ntp.example.com’ as an NTP server, you can set a group variable. The [How to build your inventory](../inventory_guide/intro_inventory.md#intro-inventory) page has details on setting [host variables](../inventory_guide/intro_inventory.md#host-variables) and [group variables](../inventory_guide/intro_inventory.md#group-variables) in inventory.

### [Defining variables in a play](playbooks_variables.md#id35)

You can define variables directly in a playbook play:

```yaml
- hosts: webservers
  vars:
    http_port: 80
```

When you define variables in a play, they are only visible to tasks executed in that play.

### [Defining variables in included files and roles](playbooks_variables.md#id36)

You can define variables in reusable variables files and/or in reusable roles. When you define variables in reusable variable files, the sensitive variables are separated from playbooks. This separation enables you to store your playbooks in a source control software and even share the playbooks, without the risk of exposing passwords or other sensitive and personal data. For information about creating reusable files and roles, see [Re-using Ansible artifacts](playbooks_reuse.md#playbooks-reuse).

This example shows how you can include variables defined in an external file:

```yaml
---

- hosts: all
  remote_user: root
  vars:
    favcolor: blue
  vars_files:
    - /vars/external_vars.yml

  tasks:

  - name: This is just a placeholder
    ansible.builtin.command: /bin/echo foo
```

The contents of each variables file is a simple YAML dictionary. For example:

```yaml
---
# in the above example, this would be vars/external_vars.yml
somevar: somevalue
password: magic
```

> **Note:**
>
> You can keep per-host and per-group variables in similar files. To learn about organizing your variables, see [Organizing host and group variables](../inventory_guide/intro_inventory.md#splitting-out-vars).

### [Defining variables at runtime](playbooks_variables.md#id37)

You can define variables when you run your playbook by passing variables at the command line using the `--extra-vars` (or `-e`) argument. You can also request user input with a `vars_prompt` (see [Interactive input: prompts](playbooks_prompts.md#playbooks-prompts)). When you pass variables at the command line, use a single quoted string, that contains one or more variables, in one of the formats below.

#### [key=value format](playbooks_variables.md#id38)

Values passed in using the `key=value` syntax are interpreted as strings. Use the JSON format if you need to pass non-string values such as Booleans, integers, floats, lists, and so on.

```
ansible-playbook release.yml --extra-vars "version=1.23.45 other_variable=foo"
```

#### [JSON string format](playbooks_variables.md#id39)

```shell
ansible-playbook release.yml --extra-vars '{"version":"1.23.45","other_variable":"foo"}'
ansible-playbook arcade.yml --extra-vars '{"pacman":"mrs","ghosts":["inky","pinky","clyde","sue"]}'
```

When passing variables with `--extra-vars`, you must escape quotes and other special characters appropriately for both your markup (for example, JSON) and for your shell:

```shell
ansible-playbook arcade.yml --extra-vars "{\"name\":\"Conan O\'Brien\"}"
ansible-playbook arcade.yml --extra-vars '{"name":"Conan O'\\\''Brien"}'
ansible-playbook script.yml --extra-vars "{\"dialog\":\"He said \\\"I just can\'t get enough of those single and double-quotes"\!"\\\"\"}"
```

#### [vars from a JSON or YAML file](playbooks_variables.md#id40)

If you have a lot of special characters, use a JSON or YAML file containing the variable definitions. Prepend both JSON and YAML filenames with @.

```
ansible-playbook release.yml --extra-vars "@some_file.json"
ansible-playbook release.yml --extra-vars "@some_file.yaml"
```

## [Variable precedence: Where should I put a variable?](playbooks_variables.md#id41)

You can set multiple variables with the same name in many different places. When you do this, Ansible loads every possible variable it finds, and then chooses the variable to apply based on variable precedence. In other words, the different variables will override each other in a certain order.

Teams and projects that agree on guidelines for defining variables (where to define certain types of variables) usually avoid variable precedence concerns. We suggest that you define each variable in one place: figure out where to define a variable, and keep it simple. For examples, see [Tips on where to set variables](playbooks_variables.md#variable-examples).

Some behavioral parameters that you can set in variables you can also set in Ansible configuration, as command-line options, and using playbook keywords. For example, you can define the user Ansible uses to connect to remote devices as a variable with `ansible_user`, in a configuration file with `DEFAULT_REMOTE_USER`, as a command-line option with `-u`, and with the playbook keyword `remote_user`. If you define the same parameter in a variable and by another method, the variable overrides the other setting. This approach allows host-specific settings to override more general settings. For examples and more details on the precedence of these various settings, see [Controlling how Ansible behaves: precedence rules](../reference_appendices/general_precedence.md#general-precedence-rules).

### [Understanding variable precedence](playbooks_variables.md#id42)

Ansible does apply variable precedence, and you might have a use for it. Here is the order of precedence from least to greatest (the last listed variables override all other variables):

> 1. command line values (for example, `-u my_user`, these are not variables)
> 2. role defaults (defined in role/defaults/main.yml) [[1]](playbooks_variables.md#id14)
> 3. inventory file or script group vars [[2]](playbooks_variables.md#id15)
> 4. inventory group_vars/all [[3]](playbooks_variables.md#id16)
> 5. playbook group_vars/all [[3]](playbooks_variables.md#id16)
> 6. inventory group_vars/\* [[3]](playbooks_variables.md#id16)
> 7. playbook group_vars/\* [[3]](playbooks_variables.md#id16)
> 8. inventory file or script host vars [[2]](playbooks_variables.md#id15)
> 9. inventory host_vars/\* [[3]](playbooks_variables.md#id16)
> 10. playbook host_vars/\* [[3]](playbooks_variables.md#id16)
> 11. host facts / cached set_facts [[4]](playbooks_variables.md#id17)
> 12. play vars
> 13. play vars_prompt
> 14. play vars_files
> 15. role vars (defined in role/vars/main.yml)
> 16. block vars (only for tasks in block)
> 17. task vars (only for the task)
> 18. include_vars
> 19. set_facts / registered vars
> 20. role (and include_role) params
> 21. include params
> 22. extra vars (for example, `-e "user=my_user"`)(always win precedence)

In general, Ansible gives precedence to variables that were defined more recently, more actively, and with more explicit scope. Variables in the defaults folder inside a role are easily overridden. Anything in the vars directory of the role overrides previous versions of that variable in the namespace. Host and/or inventory variables override role defaults, but explicit includes such as the vars directory or an `include_vars` task override inventory variables.

Ansible merges different variables set in inventory so that more specific settings override more generic settings. For example, `ansible_ssh_user` specified as a group_var is overridden by `ansible_user` specified as a host_var. For details about the precedence of variables set in inventory, see [How variables are merged](../inventory_guide/intro_inventory.md#how-we-merge).

Footnotes

[[1](playbooks_variables.md#id4)]

Tasks in each role see their own role’s defaults. Tasks defined outside of a role see the last role’s defaults.

[2]
([1](playbooks_variables.md#id5),[2](playbooks_variables.md#id10))

Variables defined in inventory file or provided by dynamic inventory.

[3]
([1](playbooks_variables.md#id6),[2](playbooks_variables.md#id7),[3](playbooks_variables.md#id8),[4](playbooks_variables.md#id9),[5](playbooks_variables.md#id11),[6](playbooks_variables.md#id12))

Includes vars added by ‘vars plugins’ as well as host_vars and group_vars which are added by the default vars plugin shipped with Ansible.

[[4](playbooks_variables.md#id13)]

When created with set_facts’s cacheable option, variables have the high precedence in the play,
but are the same as a host facts precedence when they come from the cache.

> **Note:**
>
> Within any section, redefining a var overrides the previous instance.
> If multiple groups have the same variable, the last one loaded wins.
> If you define a variable twice in a play’s `vars:` section, the second one wins.

> **Note:**
>
> The previous describes the default config `hash_behaviour=replace`, switch to `merge` to only partially overwrite.

### [Scoping variables](playbooks_variables.md#id43)

You can decide where to set a variable based on the scope you want that value to have. Ansible has three main scopes:

> - Global: this is set by config, environment variables and the command line
> - Play: each play and contained structures, vars entries (vars; vars_files; vars_prompt), role defaults and vars.
> - Host: variables directly associated to a host, like inventory, include_vars, facts or registered task outputs

Inside a template, you automatically have access to all variables that are in scope for a host, plus any registered variables, facts, and magic variables.

### [Tips on where to set variables](playbooks_variables.md#id44)

You should choose where to define a variable based on the kind of control you might want over values.

Set variables in inventory that deal with geography or behavior. Since groups are frequently the entity that maps roles onto hosts, you can often set variables on the group instead of defining them on a role. Remember: child groups override parent groups, and host variables override group variables. See [Defining variables in inventory](playbooks_variables.md#define-variables-in-inventory) for details on setting host and group variables.

Set common defaults in a `group_vars/all` file. See [Organizing host and group variables](../inventory_guide/intro_inventory.md#splitting-out-vars) for details on how to organize host and group variables in your inventory. Group variables are generally placed alongside your inventory file, but they can also be returned by dynamic inventory (see [Working with dynamic inventory](../inventory_guide/intro_dynamic_inventory.md#intro-dynamic-inventory)) or defined in AWX or on [Red Hat Ansible Automation Platform](../reference_appendices/tower.md#ansible-platform) from the UI or API:

```yaml
---
# file: /etc/ansible/group_vars/all
# this is the site wide default
ntp_server: default-time.example.com
```

Set location-specific variables in `group_vars/my_location` files. All groups are children of the `all` group, so variables set here override those set in `group_vars/all`:

```yaml
---
# file: /etc/ansible/group_vars/boston
ntp_server: boston-time.example.com
```

If one host used a different NTP server, you could set that in a host_vars file, which would override the group variable:

```yaml
---
# file: /etc/ansible/host_vars/xyz.boston.example.com
ntp_server: override.example.com
```

Set defaults in roles to avoid undefined-variable errors. If you share your roles, other users can rely on the reasonable defaults you added in the `roles/x/defaults/main.yml` file, or they can easily override those values in inventory or at the command line. See [Roles](playbooks_reuse_roles.md#playbooks-reuse-roles) for more info. For example:

```yaml
---
# file: roles/x/defaults/main.yml
# if no other value is supplied in inventory or as a parameter, this value will be used
http_port: 80
```

Set variables in roles to ensure a value is used in that role, and is not overridden by inventory variables. If you are not sharing your role with others, you can define app-specific behaviors like ports this way, in `roles/x/vars/main.yml`. If you are sharing roles with others, putting variables here makes them harder to override, although they still can by passing a parameter to the role or setting a variable with `-e`:

```yaml
---
# file: roles/x/vars/main.yml
# this will absolutely be used in this role
http_port: 80
```

Pass variables as parameters when you call roles for maximum clarity, flexibility, and visibility. This approach overrides any defaults that exist for a role. For example:

```yaml
roles:
   - role: apache
     vars:
        http_port: 8080
```

When you read this playbook it is clear that you have chosen to set a variable or override a default. You can also pass multiple values, which allows you to run the same role multiple times. See [Running a role multiple times in one play](playbooks_reuse_roles.md#run-role-twice) for more details. For example:

```yaml
roles:
   - role: app_user
     vars:
        myname: Ian
   - role: app_user
     vars:
       myname: Terry
   - role: app_user
     vars:
       myname: Graham
   - role: app_user
     vars:
       myname: John
```

Variables set in one role are available to later roles. You can set variables in a `roles/common_settings/vars/main.yml` file and use them in other roles and elsewhere in your playbook:

```yaml
roles:
   - role: common_settings
   - role: something
     vars:
       foo: 12
   - role: something_else
```

> **Note:**
>
> There are some protections in place to avoid the need to namespace variables.
> In this example, variables defined in ‘common_settings’ are available to ‘something’ and ‘something_else’ tasks, but tasks in ‘something’ have foo set at 12, even if ‘common_settings’ sets foo to 20.

Instead of worrying about variable precedence, we encourage you to think about how easily or how often you want to override a variable when deciding where to set it. If you are not sure what other variables are defined, and you need a particular value, use `--extra-vars` (`-e`) to override all other variables.

## [Using advanced variable syntax](playbooks_variables.md#id45)

For information about advanced YAML syntax used to declare variables and have more control over the data placed in YAML files used by Ansible, see [Advanced playbook syntax](playbooks_advanced_syntax.md#playbooks-advanced-syntax).

> **See also:**
>
> [Ansible playbooks](playbooks_intro.md#about-playbooks)
> :   An introduction to playbooks
>
> [Conditionals](playbooks_conditionals.md#playbooks-conditionals)
> :   Conditional statements in playbooks
>
> [Using filters to manipulate data](playbooks_filters.md#playbooks-filters)
> :   Jinja2 filters and their uses
>
> [Loops](playbooks_loops.md#playbooks-loops)
> :   Looping in playbooks
>
> [Roles](playbooks_reuse_roles.md#playbooks-reuse-roles)
> :   Playbook organization by roles
>
> [General tips](../tips_tricks/ansible_tips_tricks.md#tips-and-tricks)
> :   Tips and tricks for playbooks
>
> [Special Variables](../reference_appendices/special_variables.md#special-variables)
> :   List of special variables
>
> [User Mailing List](https://groups.google.com/group/ansible-devel)
> :   Have a question? Stop by the Google group!
>
> [Real-time chat](../community/communication.md#communication-irc)
> :   How to join Ansible chat channels
