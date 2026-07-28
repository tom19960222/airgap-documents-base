---
collection: ansible
version: "6"
title: "community.general.passwordstore lookup – manage passwords with passwordstore.org’s pass utility"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/passwordstore_lookup.html
fetched_at: 2026-07-27T17:15:09+00:00
---
# community.general.passwordstore lookup – manage passwords with passwordstore.org’s pass utility

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
> To use it in a playbook, specify: `community.general.passwordstore`.

- [Synopsis](passwordstore_lookup.md#synopsis)
- [Terms](passwordstore_lookup.md#terms)
- [Keyword parameters](passwordstore_lookup.md#keyword-parameters)
- [Notes](passwordstore_lookup.md#notes)
- [Examples](passwordstore_lookup.md#examples)
- [Return Value](passwordstore_lookup.md#return-value)

## [Synopsis](passwordstore_lookup.md#id1)

- Enables Ansible to retrieve, create or update passwords from the passwordstore.org pass utility. It also retrieves YAML style keys stored as multilines in the passwordfile.
- To avoid problems when accessing multiple secrets at once, add `auto-expand-secmem` to `~/.gnupg/gpg-agent.conf`. Where this is not possible, consider using *lock=readwrite* instead.

## [Terms](passwordstore_lookup.md#id2)

| Parameter | Comments |
| --- | --- |
| **Terms**  string / required | query key. |

## [Keyword parameters](passwordstore_lookup.md#id3)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('community.general.passwordstore', key1=value1, key2=value2, ...)` and `query('community.general.passwordstore', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **backend**  string  added in community.general 5.2.0 | Specify which backend to use.  Defaults to `pass`, passwordstore.org’s original pass utility.  `gopass` support is incomplete.  Choices:   - `"pass"` ← (default) - `"gopass"`   Configuration:   - INI entry:  ```YAML+Jinja   [passwordstore_lookup]   backend = pass   ``` - Variable: passwordstore_backend |
| **backup**  boolean | Used with `overwrite=true`. Backup the previous password in a subkey.  Choices:   - `false` ← (default) - `true` |
| **create**  boolean | Create the password if it does not already exist. Takes precedence over `missing`.  Choices:   - `false` ← (default) - `true` |
| **directory**  string | The directory of the password store.  Configuration:   - Environment variable: [`PASSWORD_STORE_DIR`](../../environment_variables.md#envvar-PASSWORD_STORE_DIR) |
| **length**  integer | The length of the generated password.  Default: `16` |
| **lock**  string  added in community.general 4.5.0 | How to synchronize operations.  The default of `write` only synchronizes write operations.  `readwrite` synchronizes all operations (including read). This makes sure that gpg-agent is never called in parallel.  `none` does not do any synchronization.  Choices:   - `"readwrite"` - `"write"` ← (default) - `"none"`   Configuration:   - INI entry:  ```YAML+Jinja   [passwordstore_lookup]   lock = write   ``` |
| **locktimeout**  string  added in community.general 4.5.0 | Lock timeout applied when *lock* is not `none`.  Time with a unit suffix, `s`, `m`, `h` for seconds, minutes, and hours, respectively. For example, `900s` equals `15m`.  Correlates with `pinentry-timeout` in `~/.gnupg/gpg-agent.conf`, see `man gpg-agent` for details.  Default: `"15m"`  Configuration:   - INI entry:  ```YAML+Jinja   [passwordstore_lookup]   locktimeout = 15m   ``` |
| **missing**  string  added in community.general 3.1.0 | List of preference about what to do if the password file is missing.  If *create=true*, the value for this option is ignored and assumed to be `create`.  If set to `error`, the lookup will error out if the passname does not exist.  If set to `create`, the passname will be created with the provided length *length* if it does not exist.  If set to `empty` or `warn`, will return a `none` in case the passname does not exist. When using `lookup` and not `query`, this will be translated to an empty string.  Choices:   - `"error"` ← (default) - `"warn"` - `"empty"` - `"create"` |
| **nosymbols**  boolean | use alphanumeric characters.  Choices:   - `false` ← (default) - `true` |
| **overwrite**  boolean | Overwrite the password if it does already exist.  Choices:   - `false` ← (default) - `true` |
| **passwordstore**  string | Location of the password store.  The value is decided by checking the following in order:  If set, this value is used.  If `directory` is set, that value will be used.  If *backend=pass*, then `~/.password-store` is used.  If *backend=gopass*, then the `path` field in `~/.config/gopass/config.yml` is used, falling back to `~/.local/share/gopass/stores/root` if not defined. |
| **returnall**  boolean | Return all the content of the password, not only the first line.  Choices:   - `false` ← (default) - `true` |
| **subkey**  string | Return a specific subkey of the password. When set to `password`, always returns the first line.  Default: `"password"` |
| **umask**  string  added in community.general 1.3.0 | Sets the umask for the created .gpg files. The first octed must be greater than 3 (user readable).  Note pass’ default value is `'077'`.  Configuration:   - Environment variable: [`PASSWORD_STORE_UMASK`](../../environment_variables.md#envvar-PASSWORD_STORE_UMASK) |
| **userpass**  string | Specify a password to save, instead of a generated one. |

## [Notes](passwordstore_lookup.md#id4)

> **Note:**
>
> - When keyword and positional parameters are used together, positional parameters must be listed before keyword parameters:
>   `lookup('community.general.passwordstore', term1, term2, key1=value1, key2=value2)` and `query('community.general.passwordstore', term1, term2, key1=value1, key2=value2)`

## [Examples](passwordstore_lookup.md#id5)

```yaml+jinja
ansible.cfg: |
  [passwordstore_lookup]
  lock=readwrite
  locktimeout=45s

playbook.yml: |
  ---

  # Debug is used for examples, BAD IDEA to show passwords on screen
  - name: Basic lookup. Fails if example/test does not exist
    ansible.builtin.debug:
      msg: "{{ lookup('community.general.passwordstore', 'example/test')}}"

  - name: Basic lookup. Warns if example/test does not exist and returns empty string
    ansible.builtin.debug:
      msg: "{{ lookup('community.general.passwordstore', 'example/test missing=warn')}}"

  - name: Create pass with random 16 character password. If password exists just give the password
    ansible.builtin.debug:
      var: mypassword
    vars:
      mypassword: "{{ lookup('community.general.passwordstore', 'example/test create=true')}}"

  - name: Create pass with random 16 character password. If password exists just give the password
    ansible.builtin.debug:
      var: mypassword
    vars:
      mypassword: "{{ lookup('community.general.passwordstore', 'example/test missing=create')}}"

  - name: Prints 'abc' if example/test does not exist, just give the password otherwise
    ansible.builtin.debug:
      var: mypassword
    vars:
      mypassword: "{{ lookup('community.general.passwordstore', 'example/test missing=empty') | default('abc', true) }}"

  - name: Different size password
    ansible.builtin.debug:
      msg: "{{ lookup('community.general.passwordstore', 'example/test create=true length=42')}}"

  - name: Create password and overwrite the password if it exists. As a bonus, this module includes the old password inside the pass file
    ansible.builtin.debug:
      msg: "{{ lookup('community.general.passwordstore', 'example/test create=true overwrite=true')}}"

  - name: Create an alphanumeric password
    ansible.builtin.debug:
      msg: "{{ lookup('community.general.passwordstore', 'example/test create=true nosymbols=true') }}"

  - name: Return the value for user in the KV pair user, username
    ansible.builtin.debug:
      msg: "{{ lookup('community.general.passwordstore', 'example/test subkey=user')}}"

  - name: Return the entire password file content
    ansible.builtin.set_fact:
      passfilecontent: "{{ lookup('community.general.passwordstore', 'example/test returnall=true')}}"
```

## [Return Value](passwordstore_lookup.md#id6)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=string | a password  Returned: success |

### Authors

- Patrick Deelman

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
