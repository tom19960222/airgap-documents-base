---
collection: ansible
version: "8"
title: "ansible.builtin.generator inventory – Uses Jinja2 to construct hosts and groups from patterns"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/generator_inventory.html
fetched_at: 2026-07-28T01:08:27+00:00
---
# ansible.builtin.generator inventory – Uses Jinja2 to construct hosts and groups from patterns

> **Note:**
>
> This inventory plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `generator`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.generator` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same inventory plugin name.

- [Synopsis](generator_inventory.md#synopsis)
- [Parameters](generator_inventory.md#parameters)
- [Examples](generator_inventory.md#examples)

## [Synopsis](generator_inventory.md#id1)

- Uses a YAML configuration file with a valid YAML or `.config` extension to define var expressions and group conditionals
- Create a template pattern that describes each host, and then use independent configuration layers
- Every element of every layer is combined to create a host for every layer combination
- Parent groups can be defined with reference to hosts and other groups using the same template variables

## [Parameters](generator_inventory.md#id2)

| Parameter | Comments |
| --- | --- |
| **hosts**  string | The `name` key is a template used to generate hostnames based on the `layers` option. Each variable in the name is expanded to create a cartesian product of all possible layer combinations.  The `parents` are a list of parent groups that the host belongs to. Each `parent` item contains a `name` key, again expanded from the template, and an optional `parents` key that lists its parents.  Parents can also contain `vars`, which is a dictionary of vars that is then always set for that variable. This can provide easy access to the group name. E.g set an `application` variable that is set to the value of the `application` layer name. |
| **layers**  string | A dictionary of layers, with the key being the layer name, used as a variable name in the `host` `name` and `parents` keys. Each layer value is a list of possible values for that layer. |
| **plugin**  string / required | token that ensures this is a source file for the ‘generator’ plugin.  **Choices:**   - `"ansible.builtin.generator"` - `"generator"` |

## [Examples](generator_inventory.md#id3)

```yaml+jinja
# inventory.config file in YAML format
# remember to enable this inventory plugin in the ansible.cfg before using
# View the output using `ansible-inventory -i inventory.config --list`
plugin: ansible.builtin.generator
hosts:
    name: "{{ operation }}_{{ application }}_{{ environment }}_runner"
    parents:
      - name: "{{ operation }}_{{ application }}_{{ environment }}"
        parents:
          - name: "{{ operation }}_{{ application }}"
            parents:
              - name: "{{ operation }}"
              - name: "{{ application }}"
          - name: "{{ application }}_{{ environment }}"
            parents:
              - name: "{{ application }}"
                vars:
                  application: "{{ application }}"
              - name: "{{ environment }}"
                vars:
                  environment: "{{ environment }}"
      - name: runner
layers:
    operation:
        - build
        - launch
    environment:
        - dev
        - test
        - prod
    application:
        - web
        - api
```

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
