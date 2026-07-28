---
collection: ansible
version: "8"
title: "Python API"
source_url: https://docs.ansible.com/projects/ansible/8/dev_guide/developing_api.html
fetched_at: 2026-07-28T00:59:16+00:00
---
# [Python API](developing_api.md#id2)

Topics

- [Python API](developing_api.md#python-api)

  - [Python API example](developing_api.md#python-api-example)
> **Note:**
>
> This API is intended for internal Ansible use. Ansible may make changes to this API at any time that could break backward compatibility with older versions of the API. Because of this, external use is not supported by Ansible. If you want to use Python API only for executing playbooks or modules, consider [ansible-runner](https://ansible-runner.readthedocs.io/en/latest/) first.

There are several ways to use Ansible from an API perspective. You can use
the Ansible Python API to control nodes, you can extend Ansible to respond to various Python events, you can
write plugins, and you can plug in inventory data from external data sources. This document
gives a basic overview and examples of the Ansible execution and playbook API.

If you would like to use Ansible programmatically from a language other than Python, trigger events asynchronously,
or have access control and logging demands, please see the [AWX project](https://github.com/ansible/awx/).

> **Note:**
>
> Because Ansible relies on forking processes, this API is not thread safe.

## [Python API example](developing_api.md#id3)

This example is a simple demonstration that shows how to minimally run a couple of tasks:

```python
#!/usr/bin/env python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import json
import shutil

import ansible.constants as C
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.module_utils.common.collections import ImmutableDict
from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader
from ansible.playbook.play import Play
from ansible.plugins.callback import CallbackBase
from ansible.vars.manager import VariableManager
from ansible import context

# Create a callback plugin so we can capture the output
class ResultsCollectorJSONCallback(CallbackBase):
    """A sample callback plugin used for performing an action as results come in.

    If you want to collect all results into a single object for processing at
    the end of the execution, look into utilizing the ``json`` callback plugin
    or writing your own custom callback plugin.
    """

    def __init__(self, *args, **kwargs):
        super(ResultsCollectorJSONCallback, self).__init__(*args, **kwargs)
        self.host_ok = {}
        self.host_unreachable = {}
        self.host_failed = {}

    def v2_runner_on_unreachable(self, result):
        host = result._host
        self.host_unreachable[host.get_name()] = result

    def v2_runner_on_ok(self, result, *args, **kwargs):
        """Print a json representation of the result.

        Also, store the result in an instance attribute for retrieval later
        """
        host = result._host
        self.host_ok[host.get_name()] = result
        print(json.dumps({host.name: result._result}, indent=4))

    def v2_runner_on_failed(self, result, *args, **kwargs):
        host = result._host
        self.host_failed[host.get_name()] = result

def main():
    host_list = ['localhost', 'www.example.com', 'www.google.com']
    # since the API is constructed for CLI it expects certain options to always be set in the context object
    context.CLIARGS = ImmutableDict(connection='smart', module_path=['/to/mymodules', '/usr/share/ansible'], forks=10, become=None,
                                    become_method=None, become_user=None, check=False, diff=False, verbosity=0)
    # required for
    # https://github.com/ansible/ansible/blob/devel/lib/ansible/inventory/manager.py#L204
    sources = ','.join(host_list)
    if len(host_list) == 1:
        sources += ','

    # initialize needed objects
    loader = DataLoader()  # Takes care of finding and reading yaml, json and ini files
    passwords = dict(vault_pass='secret')

    # Instantiate our ResultsCollectorJSONCallback for handling results as they come in. Ansible expects this to be one of its main display outlets
    results_callback = ResultsCollectorJSONCallback()

    # create inventory, use path to host config file as source or hosts in a comma separated string
    inventory = InventoryManager(loader=loader, sources=sources)

    # variable manager takes care of merging all the different sources to give you a unified view of variables available in each context
    variable_manager = VariableManager(loader=loader, inventory=inventory)

    # instantiate task queue manager, which takes care of forking and setting up all objects to iterate over host list and tasks
    # IMPORTANT: This also adds library dirs paths to the module loader
    # IMPORTANT: and so it must be initialized before calling `Play.load()`.
    tqm = TaskQueueManager(
        inventory=inventory,
        variable_manager=variable_manager,
        loader=loader,
        passwords=passwords,
        stdout_callback=results_callback,  # Use our custom callback instead of the ``default`` callback plugin, which prints to stdout
    )

    # create data structure that represents our play, including tasks, this is basically what our YAML loader does internally.
    play_source = dict(
        name="Ansible Play",
        hosts=host_list,
        gather_facts='no',
        tasks=[
            dict(action=dict(module='shell', args='ls'), register='shell_out'),
            dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}'))),
            dict(action=dict(module='command', args=dict(cmd='/usr/bin/uptime'))),
        ]
    )

    # Create play object, playbook objects use .load instead of init or new methods,
    # this will also automatically create the task objects from the info provided in play_source
    play = Play().load(play_source, variable_manager=variable_manager, loader=loader)

    # Actually run it
    try:
        result = tqm.run(play)  # most interesting data for a play is actually sent to the callback's methods
    finally:
        # we always need to cleanup child procs and the structures we use to communicate with them
        tqm.cleanup()
        if loader:
            loader.cleanup_all_tmp_files()

    # Remove ansible tmpdir
    shutil.rmtree(C.DEFAULT_LOCAL_TMP, True)

    print("UP ***********")
    for host, result in results_callback.host_ok.items():
        print('{0} >>> {1}'.format(host, result._result['stdout']))

    print("FAILED *******")
    for host, result in results_callback.host_failed.items():
        print('{0} >>> {1}'.format(host, result._result['msg']))

    print("DOWN *********")
    for host, result in results_callback.host_unreachable.items():
        print('{0} >>> {1}'.format(host, result._result['msg']))

if __name__ == '__main__':
    main()
```

> **Note:**
>
> Ansible emits warnings and errors through the display object, which prints directly to stdout, stderr and the Ansible log.

The source code for the `ansible`
command line tools (`lib/ansible/cli/`) is [available on GitHub](https://github.com/ansible/ansible/tree/devel/lib/ansible/cli).

> **See also:**
>
> [Developing dynamic inventory](developing_inventory.md#developing-inventory)
> :   Developing dynamic inventory integrations
>
> [Developing modules](developing_modules_general.md#developing-modules-general)
> :   Getting started on developing a module
>
> [Developing plugins](developing_plugins.md#developing-plugins)
> :   How to develop plugins
>
> [Development Mailing List](https://groups.google.com/group/ansible-devel)
> :   Mailing list for development topics
>
> [Real-time chat](../community/communication.md#communication-irc)
> :   How to join Ansible chat channels
