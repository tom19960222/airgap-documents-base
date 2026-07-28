---
collection: ansible
version: "6"
title: "Developing modules"
source_url: https://docs.ansible.com/projects/ansible/6/dev_guide/developing_modules_general.html
fetched_at: 2026-07-27T16:39:52+00:00
---
# Developing modules

A module is a reusable, standalone script that Ansible runs on your behalf, either locally or remotely. Modules interact with your local machine, an API, or a remote system to perform specific tasks like changing a database password or spinning up a cloud instance. Each module can be used by the Ansible API, or by the **ansible** or **ansible-playbook** programs. A module provides a defined interface, accepts arguments, and returns information to Ansible by printing a JSON string to stdout before exiting.

If you need functionality that is not available in any of the thousands of Ansible modules found in collections, you can easily write your own custom module. When you write a module for local use, you can choose any programming language and follow your own rules. Use this topic to learn how to create an Ansible module in Python. After you create a module, you must add it locally to the appropriate directory so that Ansible can find and execute it. For details about adding a module locally, see [Adding modules and plugins locally](developing_locally.md#developing-locally).

If you are developing a module in a [collection](developing_collections.md#developing-collections), see those documents instead.

- [Preparing an environment for developing Ansible modules](developing_modules_general.md#preparing-an-environment-for-developing-ansible-modules)
- [Creating a module](developing_modules_general.md#creating-a-module)
- [Creating an info or a facts module](developing_modules_general.md#creating-an-info-or-a-facts-module)
- [Verifying your module code](developing_modules_general.md#verifying-your-module-code)

  - [Verifying your module code locally](developing_modules_general.md#verifying-your-module-code-locally)
  - [Verifying your module code in a playbook](developing_modules_general.md#verifying-your-module-code-in-a-playbook)
- [Testing your newly-created module](developing_modules_general.md#testing-your-newly-created-module)

  - [Performing sanity tests](developing_modules_general.md#performing-sanity-tests)
- [Contributing back to Ansible](developing_modules_general.md#contributing-back-to-ansible)
- [Communication and development support](developing_modules_general.md#communication-and-development-support)
- [Credit](developing_modules_general.md#credit)

## [Preparing an environment for developing Ansible modules](developing_modules_general.md#id1)

You just need `ansible-core` installed to test the module. Modules can be written in any language,
but most of the following guide is assuming you are using Python.
Modules for inclusion in Ansible itself must be Python or Powershell.

One advantage of using Python or Powershell for your custom modules is being able to use the `module_utils` common code that does a lot of the
heavy lifting for argument processing, logging and response writing, among other things.

## [Creating a module](developing_modules_general.md#id2)

It is highly recommended that you use a `venv` or `virtualenv` for Python development.

To create a module:

1. Create a `library` directory in your workspace, your test play should live in the same directory.
2. Create your new module file: `$ touch library/my_test.py`. Or just open/create it with your editor of choice.
3. Paste the content below into your new module file. It includes the [required Ansible format and documentation](developing_modules_documenting.md#developing-modules-documenting), a simple [argument spec for declaring the module options](developing_program_flow_modules.md#argument-spec), and some example code.
4. Modify and extend the code to do what you want your new module to do. See the [programming tips](developing_modules_best_practices.md#developing-modules-best-practices) and [Python 3 compatibility](developing_python_3.md#developing-python-3) pages for pointers on writing clean and concise module code.

```python
#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: my_test

short_description: This is my test module

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.0.0"

description: This is my longer description explaining my test module.

options:
    name:
        description: This is the message to send to the test module.
        required: true
        type: str
    new:
        description:
            - Control to demo if the result of this module is changed or not.
            - Parameter description can be a list as well.
        required: false
        type: bool
# Specify this value according to your collection
# in format of namespace.collection.doc_fragment_name
extends_documentation_fragment:
    - my_namespace.my_collection.my_doc_fragment_name

author:
    - Your Name (@yourGitHubHandle)
'''

EXAMPLES = r'''
# Pass in a message
- name: Test with a message
  my_namespace.my_collection.my_test:
    name: hello world

# pass in a message and have changed true
- name: Test with a message and changed output
  my_namespace.my_collection.my_test:
    name: hello world
    new: true

# fail the module
- name: Test failure of the module
  my_namespace.my_collection.my_test:
    name: fail me
'''

RETURN = r'''
# These are examples of possible return values, and in general should use other names for return values.
original_message:
    description: The original name param that was passed in.
    type: str
    returned: always
    sample: 'hello world'
message:
    description: The output message that the test module generates.
    type: str
    returned: always
    sample: 'goodbye'
'''

from ansible.module_utils.basic import AnsibleModule

def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        name=dict(type='str', required=True),
        new=dict(type='bool', required=False, default=False)
    )

    # seed the result dict in the object
    # we primarily care about changed and state
    # changed is if this module effectively modified the target
    # state will include any data that you want your module to pass back
    # for consumption, for example, in a subsequent task
    result = dict(
        changed=False,
        original_message='',
        message=''
    )

    # the AnsibleModule object will be our abstraction working with Ansible
    # this includes instantiation, a couple of common attr would be the
    # args/params passed to the execution, as well as if the module
    # supports check mode
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # if the user is working with this module in only check mode we do not
    # want to make any changes to the environment, just return the current
    # state with no modifications
    if module.check_mode:
        module.exit_json(**result)

    # manipulate or modify the state as needed (this is going to be the
    # part where your module will do what it needs to do)
    result['original_message'] = module.params['name']
    result['message'] = 'goodbye'

    # use whatever logic you need to determine whether or not this module
    # made any modifications to your target
    if module.params['new']:
        result['changed'] = True

    # during the execution of the module, if there is an exception or a
    # conditional state that effectively causes a failure, run
    # AnsibleModule.fail_json() to pass in the message and the result
    if module.params['name'] == 'fail me':
        module.fail_json(msg='You requested this to fail', **result)

    # in the event of a successful module execution, you will want to
    # simple AnsibleModule.exit_json(), passing the key/value results
    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()
```

## [Creating an info or a facts module](developing_modules_general.md#id3)

Ansible gathers information about the target machines using facts modules, and gathers information on other objects or files using info modules.
If you find yourself trying to add `state: info` or `state: list` to an existing module, that is often a sign that a new dedicated `_facts` or `_info` module is needed.

In Ansible 2.8 and onwards, we have two type of information modules, they are `*_info` and `*_facts`.

If a module is named `<something>_facts`, it should be because its main purpose is returning `ansible_facts`. Do not name modules that do not do this with `_facts`.
Only use `ansible_facts` for information that is specific to the host machine, for example network interfaces and their configuration, which operating system and which programs are installed.

Modules that query/return general information (and not `ansible_facts`) should be named `_info`.
General information is non-host specific information, for example information on online/cloud services (you can access different accounts for the same online service from the same host), or information on VMs and containers accessible from the machine, or information on individual files or programs.

Info and facts modules, are just like any other Ansible Module, with a few minor requirements:

1. They MUST be named `<something>_info` or `<something>_facts`, where <something> is singular.
2. Info `*_info` modules MUST return in the form of the [result dictionary](../reference_appendices/common_return_values.md#common-return-values) so other modules can access them.
3. Fact `*_facts` modules MUST return in the `ansible_facts` field of the [result dictionary](../reference_appendices/common_return_values.md#common-return-values) so other modules can access them.
4. They MUST support [check_mode](../user_guide/playbooks_checkmode.md#check-mode-dry).
5. They MUST NOT make any changes to the system.
6. They MUST document the [return fields](developing_modules_documenting.md#return-block) and [examples](developing_modules_documenting.md#examples-block).

The rest is just like creating a normal module.

## [Verifying your module code](developing_modules_general.md#id4)

After you modify the sample code above to do what you want, you can try out your module.
Our [debugging tips](debugging.md#debugging-modules) will help if you run into bugs as you verify your module code.

### [Verifying your module code locally](developing_modules_general.md#id5)

The simplest way is to use `ansible` adhoc command:

```shell
ANSIBLE_LIBRARY=./library ansible -m my_test -a 'name=hello new=true' remotehost
```

If your module does not need to target a remote host, you can quickly and easily exercise your code locally like this:

```shell
ANSIBLE_LIBRARY=./library ansible -m my_test -a 'name=hello new=true' localhost
```

- If for any reason (pdb, using print(), faster iteration, etc) you want to avoid going through Ansible,
  another way is to create an arguments file, a basic JSON config file that passes parameters to your module so that you can run it.
  Name the arguments file `/tmp/args.json` and add the following content:

```json
{
    "ANSIBLE_MODULE_ARGS": {
        "name": "hello",
        "new": true
    }
}
```

- Then the module can be tested locally and directly. This skips the packing steps and uses module_utils files directly:

```console
``$ python library/my_test.py /tmp/args.json``
```

It should return output like this:

```json
{"changed": true, "state": {"original_message": "hello", "new_message": "goodbye"}, "invocation": {"module_args": {"name": "hello", "new": true}}}
```

### [Verifying your module code in a playbook](developing_modules_general.md#id6)

You can easily run a full test by including it in a playbook, as long as the `library` directory is in the same directory as the play:

- Create a playbook in any directory: `$ touch testmod.yml`
- Add the following to the new playbook file:

```yaml
- name: test my new module
  hosts: localhost
  tasks:
  - name: run the new module
    my_test:
      name: 'hello'
      new: true
    register: testout
  - name: dump test output
    debug:
      msg: '{{ testout }}'
```

- Run the playbook and analyze the output: `$ ansible-playbook ./testmod.yml`

## [Testing your newly-created module](developing_modules_general.md#id7)

The following two examples will get you started with testing your module code. Please review our [testing](testing.md#developing-testing) section for more detailed
information, including instructions for [testing module documentation](testing_documentation.md#testing-module-documentation), adding [integration tests](testing_integration.md#testing-integration), and more.

> **Note:**
>
> If contributing to Ansible, every new module and plugin should have integration tests, even if the tests cannot be run on Ansible CI infrastructure.
> In this case, the tests should be marked with the `unsupported` alias in [aliases file](https://docs.ansible.com/ansible/latest/dev_guide/testing/sanity/integration-aliases.html).

### [Performing sanity tests](developing_modules_general.md#id8)

You can run through Ansible’s sanity checks in a container:

`$ ansible-test sanity -v --docker --python 3.10 MODULE_NAME`

> **Note:**
>
> Note that this example requires Docker to be installed and running. If you’d rather not use a container for this, you can choose to use `--venv` instead of `--docker`.

## [Contributing back to Ansible](developing_modules_general.md#id9)

If you would like to contribute to `ansible-core` by adding a new feature or fixing a bug, [create a fork](https://help.github.com/articles/fork-a-repo/) of the ansible/ansible repository and develop against a new feature branch using the `devel` branch as a starting point. When you have a good working code change, you can submit a pull request to the Ansible repository by selecting your feature branch as a source and the Ansible devel branch as a target.

If you want to contribute a module to an [Ansible collection](../community/contributing_maintained_collections.md#contributing-maintained-collections), review our [submission checklist](developing_modules_checklist.md#developing-modules-checklist), [programming tips](developing_modules_best_practices.md#developing-modules-best-practices), and [strategy for maintaining Python 2 and Python 3 compatibility](developing_python_3.md#developing-python-3), as well as information about [testing](testing.md#developing-testing) before you open a pull request.

The [Community Guide](../community/index.md#ansible-community-guide) covers how to open a pull request and what happens next.

## [Communication and development support](developing_modules_general.md#id10)

Join the `#ansible-devel` chat channel (using Matrix at ansible.im or using IRC at [irc.libera.chat](https://libera.chat/)) for discussions surrounding Ansible development.

For questions and discussions pertaining to using the Ansible product, join the `#ansible` channel.

To find other topic-specific chat channels, look at [Community Guide, Communicating](../community/communication.md#communication-irc).

## [Credit](developing_modules_general.md#id11)

Thank you to Thomas Stringer ([@trstringer](https://github.com/trstringer)) for contributing source
material for this topic.
