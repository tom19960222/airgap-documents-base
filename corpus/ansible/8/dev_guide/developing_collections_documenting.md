---
collection: ansible
version: "8"
title: "Documenting collections"
source_url: https://docs.ansible.com/projects/ansible/8/dev_guide/developing_collections_documenting.html
fetched_at: 2026-07-28T01:00:44+00:00
---
# Documenting collections

## Documenting modules and plugins

Documenting modules is thoroughly documented in [Module format and documentation](developing_modules_documenting.md#module-documenting). Plugins can be documented the same way as modules, that is with `DOCUMENTATION`, `EXAMPLES`, and `RETURN` blocks.

## Documenting roles

To document a role, you have to add a role argument spec by creating a file `meta/argument_specs.yml` in your role. See [Role argument validation](../playbook_guide/playbooks_reuse_roles.md#role-argument-spec) for details. As an example, you can look at [the argument specs file](https://github.com/sensu/sensu-go-ansible/blob/master/roles/install/meta/argument_specs.yml) of the [sensu.sensu_go.install role](../collections/sensu/sensu_go/install_role.md#ansible-collections-sensu-sensu-go-install-role) on GitHub.

## Build a docsite with antsibull-docs

You can use [antsibull-docs](https://pypi.org/project/antsibull-docs) to build a Sphinx-based docsite for your collection:

1. Create your collection and make sure you can use it with ansible-core by adding it to your [COLLECTIONS_PATHS](../reference_appendices/config.md#collections-paths).
2. Create a directory `dest` and run `antsibull-docs sphinx-init --use-current --dest-dir dest namespace.name`, where `namespace.name` is the name of your collection.
3. Go into `dest` and run `pip install -r requirements.txt`. You might want to create a venv and activate it first to avoid installing this globally.
4. Then run `./build.sh`.
5. Open `build/html/index.html` in a browser of your choice.

If you want to add additional documentation to your collection next to the plugin, module, and role documentation, see [docs directory](developing_collections_structure.md#collections-doc-dir).
