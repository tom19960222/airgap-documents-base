---
collection: ansible
version: "6"
title: "community.general.filetree lookup – recursively match all files in a directory tree"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/filetree_lookup.html
fetched_at: 2026-07-27T17:15:03+00:00
---
# community.general.filetree lookup – recursively match all files in a directory tree

> **Note:**
>
> This lookup plugin is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.filetree`.

- [Synopsis](filetree_lookup.md#synopsis)
- [Terms](filetree_lookup.md#terms)
- [Examples](filetree_lookup.md#examples)
- [Return Value](filetree_lookup.md#return-value)

## [Synopsis](filetree_lookup.md#id1)

- This lookup enables you to template a complete tree of files on a target system while retaining permissions and ownership.
- Supports directories, files and symlinks, including SELinux and other file properties.
- If you provide more than one path, it will implement a first_found logic, and will not process entries it already processed in previous paths. This enables merging different trees in order of importance, or add role_vars to specific paths to influence different instances of the same role.

## [Terms](filetree_lookup.md#id2)

| Parameter | Comments |
| --- | --- |
| **Terms**  string / required | path(s) of files to read |

## [Examples](filetree_lookup.md#id3)

```yaml+jinja
- name: Create directories
  ansible.builtin.file:
    path: /web/{{ item.path }}
    state: directory
    mode: '{{ item.mode }}'
  with_community.general.filetree: web/
  when: item.state == 'directory'

- name: Template files (explicitly skip directories in order to use the 'src' attribute)
  ansible.builtin.template:
    src: '{{ item.src }}'
    # Your template files should be stored with a .j2 file extension,
    # but should not be deployed with it. splitext|first removes it.
    dest: /web/{{ item.path | splitext | first }}
    mode: '{{ item.mode }}'
  with_community.general.filetree: web/
  when: item.state == 'file'

- name: Recreate symlinks
  ansible.builtin.file:
    src: '{{ item.src }}'
    dest: /web/{{ item.path }}
    state: link
    follow: false  # avoid corrupting target files if the link already exists
    force: true
    mode: '{{ item.mode }}'
  with_community.general.filetree: web/
  when: item.state == 'link'

- name: list all files under web/
  ansible.builtin.debug:
    msg: "{{ lookup('community.general.filetree', 'web/') }}"
```

## [Return Value](filetree_lookup.md#id4)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=dictionary | List of dictionaries with file information.  Returned: success |
| **ctime**  float | Time of last metadata update or creation (depends on OS).  Returned: success |
| **gid**  integer | Group ID of the file/directory.  Returned: success |
| **group**  any | Name of the group that owns the file/directory.  Returned: success |
| **mode**  string | The permissions the resulting file or directory.  Returned: success |
| **mtime**  float | Time of last modification.  Returned: success |
| **owner**  any | Name of the user that owns the file/directory.  Returned: success |
| **path**  path | Contains the relative path to root.  Returned: success |
| **root**  path | Allows filtering by original location.  Returned: success |
| **selevel**  any | The level part of the SELinux file context.  Returned: success |
| **serole**  any | The role part of the SELinux file context.  Returned: success |
| **setype**  any | The type part of the SELinux file context.  Returned: success |
| **seuser**  any | The user part of the SELinux file context.  Returned: success |
| **size**  integer | Size of the target.  Returned: success |
| **src**  path | Full path to file.  Not returned when *item.state* is set to `directory`.  Returned: success |
| **state**  string | TODO  Returned: success |
| **uid**  integer | Owner ID of the file/directory.  Returned: success |

### Authors

- Dag Wieers (@dagwieers)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
