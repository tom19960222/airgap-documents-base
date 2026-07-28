---
collection: ansible
version: "8"
title: "Galaxy Developer Guide"
source_url: https://docs.ansible.com/projects/ansible/8/galaxy/dev_guide.html
fetched_at: 2026-07-28T00:57:55+00:00
---
# Galaxy Developer Guide

You can host collections and roles on Galaxy to share with the Ansible community. Galaxy content is formatted in pre-packaged units of work such as [roles](../playbook_guide/playbooks_reuse_roles.md#playbooks-reuse-roles), and [collections](../collections_guide/index.md#collections).
You can create roles for provisioning infrastructure, deploying applications, and all of the tasks you do everyday. Taking this a step further, you can create collections which provide a comprehensive package of automation that may include multiple playbooks, roles, modules, and plugins.

- [Creating collections for Galaxy](dev_guide.md#creating-collections-for-galaxy)
- [Creating roles for Galaxy](dev_guide.md#creating-roles-for-galaxy)

  - [Force](dev_guide.md#force)
  - [Container enabled](dev_guide.md#container-enabled)
  - [Using a custom role skeleton](dev_guide.md#using-a-custom-role-skeleton)
  - [Authenticate with Galaxy](dev_guide.md#authenticate-with-galaxy)
  - [Import a role](dev_guide.md#import-a-role)
  - [Delete a role](dev_guide.md#delete-a-role)
  - [Travis integrations](dev_guide.md#travis-integrations)

## [Creating collections for Galaxy](dev_guide.md#id1)

Collections are a distribution format for Ansible content. You can use collections to package and distribute playbooks, roles, modules, and plugins.
You can publish and use collections through [Ansible Galaxy](https://galaxy.ansible.com).

See [Developing collections](../dev_guide/developing_collections.md#developing-collections) for details on how to create collections.

## [Creating roles for Galaxy](dev_guide.md#id2)

Use the `init` command to initialize the base structure of a new role, saving time on creating the various directories and main.yml files a role requires

```bash
$ ansible-galaxy role init role_name
```

The above will create the following directory structure in the current working directory:

```
role_name/
    README.md
    defaults/
        main.yml
    files/
    handlers/
        main.yml
    meta/
        main.yml
    tasks/
        main.yml
    templates/
    tests/
        inventory
        test.yml
    vars/
        main.yml
```

If you want to create a repository for the role, the repository root should be role_name.

### [Force](dev_guide.md#id3)

If a directory matching the name of the role already exists in the current working directory, the init command will result in an error. To ignore the error
use the `--force` option. Force will create the above subdirectories and files, replacing anything that matches.

### [Container enabled](dev_guide.md#id4)

If you are creating a Container Enabled role, pass `--type container` to `ansible-galaxy init`. This will create the same directory structure as above, but populate it
with default files appropriate for a Container Enabled role. For example, the README.md has a slightly different structure, the *.travis.yml* file tests
the role using [Ansible Container](https://github.com/ansible/ansible-container), and the meta directory includes a *container.yml* file.

### [Using a custom role skeleton](dev_guide.md#id5)

A custom role skeleton directory can be supplied as follows:

```bash
$ ansible-galaxy init --role-skeleton=/path/to/skeleton role_name
```

When a skeleton is provided, init will:

- copy all files and directories from the skeleton to the new role
- any .j2 files found outside of a templates folder will be rendered as templates. The only useful variable at the moment is role_name
- The .git folder and any .git_keep files will not be copied

Alternatively, the role_skeleton and ignoring of files can be configured with ansible.cfg

```
[galaxy]
role_skeleton = /path/to/skeleton
role_skeleton_ignore = ^.git$,^.*/.git_keep$
```

### [Authenticate with Galaxy](dev_guide.md#id6)

Using the `import`, `delete` and `setup` commands to manage your roles on the Galaxy website requires authentication in the form of an API key, you must create an account on the Galaxy website.

To create an authentication token:

1. Click Collections > API Token.
2. Click Load Token and then copy it.
3. Save your token in the path set in the [GALAXY_TOKEN_PATH](../reference_appendices/config.md#galaxy-token-path).

### [Import a role](dev_guide.md#id7)

The ``` import``command requires that you authenticate with the API token. You can include it in your ``ansible.cfg ``` file or use the `--token` command option. You are only allowed to remove roles where you have access to the repository in GitHub.

To import a new role:

```bash
$ ansible-galaxy role import github_user github_repo
```

By default the command will wait for Galaxy to complete the import process, displaying the results as the import progresses:

```
Successfully submitted import request 41
Starting import 41: role_name=myrole repo=githubuser/ansible-role-repo ref=
Retrieving GitHub repo githubuser/ansible-role-repo
Accessing branch: devel
Parsing and validating meta/main.yml
Parsing galaxy_tags
Parsing platforms
Adding dependencies
Parsing and validating README.md
Adding repo tags as role versions
Import completed
Status SUCCESS : warnings=0 errors=0
```

See [ansible-galaxy](../cli/ansible-galaxy.md#ansible-galaxy) for other command options.

### [Delete a role](dev_guide.md#id8)

The `delete` command requires that you authenticate with the API token. You can include it in your `ansible.cfg` file or use the `--token` command option. You are only allowed to remove roles where you have access to the repository in GitHub.

Use the following to delete a role:

```bash
$ ansible-galaxy role delete github_user github_repo
```

This only removes the role from Galaxy. It does not remove or alter the actual GitHub repository.

### [Travis integrations](dev_guide.md#id9)

You can create an integration or connection between a role in Galaxy and [Travis](https://travis-ci.org). Once the connection is established, a build in Travis will
automatically trigger an import in Galaxy, updating the search index with the latest information about the role.

You create the integration using the `setup` command with your API token. You will
also need an account in Travis, and your Travis token. Once you’re ready, use the following command to create the integration:

```bash
$ ansible-galaxy role setup travis github_user github_repo xxx-travis-token-xxx
```

The setup command requires your Travis token, however the token is not stored in Galaxy. It is used along with the GitHub username and repo to create a hash as described
in [the Travis documentation](https://docs.travis-ci.com/user/notifications/). The hash is stored in Galaxy and used to verify notifications received from Travis.

The setup command enables Galaxy to respond to notifications. To configure Travis to run a build on your repository and send a notification, follow the
[Travis getting started guide](https://docs.travis-ci.com/user/getting-started/).

To instruct Travis to notify Galaxy when a build completes, add the following to your .travis.yml file:

```
notifications:
    webhooks: https://galaxy.ansible.com/api/v1/notifications/
```

#### List Travis integrations

Use the `--list` option to display your Travis integrations:

```bash
$ ansible-galaxy setup --list travis github_user github_repo xxx-travis-token-xxx

ID         Source     Repo
---------- ---------- ----------
2          travis     github_user/github_repo
1          travis     github_user/github_repo
```

#### Remove Travis integrations

Use the `--remove` option to disable and remove a Travis integration:

> ```bash
> $ ansible-galaxy role setup --remove ID
> ```

Provide the ID of the integration to be disabled. You can find the ID by using the `--list` option.

> **See also:**
>
> [Using Ansible collections](../collections_guide/index.md#collections)
> :   Shareable collections of modules, playbooks and roles
>
> [Roles](../playbook_guide/playbooks_reuse_roles.md#playbooks-reuse-roles)
> :   All about ansible roles
>
> [Mailing List](https://groups.google.com/group/ansible-project)
> :   Questions? Help? Ideas? Stop by the list on Google Groups
>
> [Real-time chat](../community/communication.md#communication-irc)
> :   How to join Ansible chat channels
