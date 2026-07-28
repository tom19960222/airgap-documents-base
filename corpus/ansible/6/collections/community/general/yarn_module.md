---
collection: ansible
version: "6"
title: "community.general.yarn module – Manage node.js packages with Yarn"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/yarn_module.html
fetched_at: 2026-07-27T17:14:10+00:00
---
# community.general.yarn module – Manage node.js packages with Yarn

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](yarn_module.md#ansible-collections-community-general-yarn-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.yarn`.

- [Synopsis](yarn_module.md#synopsis)
- [Requirements](yarn_module.md#requirements)
- [Parameters](yarn_module.md#parameters)
- [Examples](yarn_module.md#examples)
- [Return Values](yarn_module.md#return-values)

## [Synopsis](yarn_module.md#id1)

- Manage node.js packages with the Yarn package manager (<https://yarnpkg.com/>)

## [Requirements](yarn_module.md#id2)

The below requirements are needed on the host that executes this module.

- Yarn installed in bin path (typically /usr/local/bin)

## [Parameters](yarn_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **executable**  path | The executable location for yarn. |
| **global**  boolean | Install the node.js library globally  Choices:   - `false` ← (default) - `true` |
| **ignore_scripts**  boolean | Use the –ignore-scripts flag when installing.  Choices:   - `false` ← (default) - `true` |
| **name**  string | The name of a node.js library to install  If omitted all packages in package.json are installed.  To globally install from local node.js library. Prepend “file:” to the path of the node.js library. |
| **path**  path | The base path where Node.js libraries will be installed.  This is where the node_modules folder lives. |
| **production**  boolean | Install dependencies in production mode.  Yarn will ignore any dependencies under devDependencies in package.json  Choices:   - `false` ← (default) - `true` |
| **registry**  string | The registry to install modules from. |
| **state**  string | Installation state of the named node.js library  If absent is selected, a name option must be provided  Choices:   - `"present"` ← (default) - `"absent"` - `"latest"` |
| **version**  string | The version of the library to be installed.  Must be in semver format. If “latest” is desired, use “state” arg instead |

## [Examples](yarn_module.md#id4)

```yaml+jinja
- name: Install "imagemin" node.js package.
  community.general.yarn:
    name: imagemin
    path: /app/location

- name: Install "imagemin" node.js package on version 5.3.1
  community.general.yarn:
    name: imagemin
    version: '5.3.1'
    path: /app/location

- name: Install "imagemin" node.js package globally.
  community.general.yarn:
    name: imagemin
    global: true

- name: Remove the globally-installed package "imagemin".
  community.general.yarn:
    name: imagemin
    global: true
    state: absent

- name: Install "imagemin" node.js package from custom registry.
  community.general.yarn:
    name: imagemin
    registry: 'http://registry.mysite.com'

- name: Install packages based on package.json.
  community.general.yarn:
    path: /app/location

- name: Update all packages in package.json to their latest version.
  community.general.yarn:
    path: /app/location
    state: latest
```

## [Return Values](yarn_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | Whether Yarn changed any package data  Returned: always  Sample: `true` |
| **invocation**  dictionary | Parameters and values used during execution  Returned: success  Sample: `{"module_args": {"executable": null, "globally": false, "ignore_scripts": false, "name": null, "path": "/some/path/folder", "production": false, "registry": null, "state": "present", "version": null}}` |
| **msg**  string | Provides an error message if Yarn syntax was incorrect  Returned: failure  Sample: `"Package must be explicitly named when uninstalling."` |
| **out**  string | Output generated from Yarn.  Returned: always  Sample: `"yarn add v0.16.1[1/4] Resolving packages...[2/4] Fetching packages...[3/4] Linking dependencies...[4/4] Building fresh packages...success Saved lockfile.success Saved 1 new dependency..left-pad@1.1.3 Done in 0.59s."` |

### Authors

- David Gunter (@verkaufer)
- Chris Hoffman (@chrishoffman), creator of NPM Ansible module)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
