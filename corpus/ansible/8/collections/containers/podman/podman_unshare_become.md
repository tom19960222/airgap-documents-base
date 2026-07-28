---
collection: ansible
version: "8"
title: "containers.podman.podman_unshare become – Run tasks using podman unshare"
source_url: https://docs.ansible.com/projects/ansible/8/collections/containers/podman/podman_unshare_become.html
fetched_at: 2026-07-28T02:03:20+00:00
---
# containers.podman.podman_unshare become – Run tasks using podman unshare

> **Note:**
>
> This become plugin is part of the [containers.podman collection](https://galaxy.ansible.com/ui/repo/published/containers/podman/) (version 1.11.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install containers.podman`.
>
> To use it in a playbook, specify: `containers.podman.podman_unshare`.

New in containers.podman 1.9.0

- [Synopsis](podman_unshare_become.md#synopsis)
- [Parameters](podman_unshare_become.md#parameters)
- [Examples](podman_unshare_become.md#examples)

## [Synopsis](podman_unshare_become.md#id1)

- This become plugins allows your remote/login user to execute commands in its container user namespace. Official documentation: <https://docs.podman.io/en/latest/markdown/podman-unshare.1.html>

## [Parameters](podman_unshare_become.md#id2)

| Parameter | Comments |
| --- | --- |
| **become_exe**  string | Sudo executable  **Default:** `"sudo"`  **Configuration:**   - INI entries:  ```YAML+Jinja   [privilege_escalation]   become_exe = sudo   ```  ```YAML+Jinja   [sudo_become_plugin]   executable = sudo   ``` - Environment variable: [`ANSIBLE_BECOME_EXE`](../../../reference_appendices/config.md#envvar-ANSIBLE_BECOME_EXE) - Environment variable: [`ANSIBLE_SUDO_EXE`](../../environment_variables.md#envvar-ANSIBLE_SUDO_EXE) - Variable: ansible_become_exe - Variable: ansible_sudo_exe |
| **become_pass**  string | Password to pass to sudo  **Configuration:**   - INI entry:  ```YAML+Jinja   [sudo_become_plugin]   password = VALUE   ``` - Environment variable: [`ANSIBLE_BECOME_PASS`](../../environment_variables.md#envvar-ANSIBLE_BECOME_PASS) - Environment variable: [`ANSIBLE_SUDO_PASS`](../../environment_variables.md#envvar-ANSIBLE_SUDO_PASS) - Variable: ansible_become_password - Variable: ansible_become_pass - Variable: ansible_sudo_pass |
| **become_user**  string | User you ‘become’ to execute the task (‘root’ is not a valid value here).  **Configuration:**   - INI entries:  ```YAML+Jinja   [privilege_escalation]   become_user = VALUE   ```  ```YAML+Jinja   [sudo_become_plugin]   user = VALUE   ``` - Environment variable: [`ANSIBLE_BECOME_USER`](../../../reference_appendices/config.md#envvar-ANSIBLE_BECOME_USER) - Environment variable: [`ANSIBLE_SUDO_USER`](../../environment_variables.md#envvar-ANSIBLE_SUDO_USER) - Variable: ansible_become_user - Variable: ansible_sudo_user |

## [Examples](podman_unshare_become.md#id3)

```yaml+jinja
- name: checking uid of file 'foo'
  ansible.builtin.stat:
    path: "{{ test_dir }}/foo"
  register: foo
- ansible.builtin.debug:
    var: foo.stat.uid
# The output shows that it's owned by the login user
# ok: [test_host] => {
#     "foo.stat.uid": "1003"
# }

- name: mounting the file to an unprivileged container and modifying its owner
  containers.podman.podman_container:
    name: chmod_foo
    image: alpine
    rm: true
    volume:
    - "{{ test_dir }}:/opt/test:z"
    command: chown 1000 /opt/test/foo

# Now the file 'foo' is owned by the container uid 1000,
# which is mapped to something completaly different on the host.
# It creates a situation when the file is unaccessible to the host user (uid 1003)
# Running stat again, debug output will be like this:
# ok: [test_host] => {
#     "foo.stat.uid": "328679"
# }

- name: running stat in modified user namespace
  become_method: containers.podman.podman_unshare
  become: true
  ansible.builtin.stat:
    path: "{{ test_dir }}/foo"
  register: foo
# By gathering file stats with podman_ushare
# we can see the uid set in the container:
# ok: [test_host] => {
#     "foo.stat.uid": "1000"
# }

- name: resetting file ownership with podman unshare
  become_method: containers.podman.podman_unshare
  become: true
  ansible.builtin.file:
    state: file
    path: "{{ test_dir }}/foo"
    owner: 0  # in a modified user namespace host uid is mapped to 0
# If we run stat and debug with 'become: false',
# we can see that the file is ours again:
# ok: [test_host] => {
#     "foo.stat.uid": "1003"
# }
```

### Authors

- Janos Gerzson (@grzs)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/containers/ansible-podman-collections/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/containers/ansible-podman-collections.git)
