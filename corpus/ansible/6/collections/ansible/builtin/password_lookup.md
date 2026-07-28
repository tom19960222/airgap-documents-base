---
collection: ansible
version: "6"
title: "ansible.builtin.password lookup – retrieve or generate a random password, stored in a file"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/builtin/password_lookup.html
fetched_at: 2026-07-27T16:44:22+00:00
---
# ansible.builtin.password lookup – retrieve or generate a random password, stored in a file

> **Note:**
>
> This lookup plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `password` even without specifying the `collections:` keyword.
> However, we recommend you use the FQCN for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same lookup plugin name.

- [Synopsis](password_lookup.md#synopsis)
- [Terms](password_lookup.md#terms)
- [Keyword parameters](password_lookup.md#keyword-parameters)
- [Notes](password_lookup.md#notes)
- [Examples](password_lookup.md#examples)
- [Return Value](password_lookup.md#return-value)

## [Synopsis](password_lookup.md#id1)

- Generates a random plaintext password and stores it in a file at a given filepath.
- If the file exists previously, it will retrieve its contents, behaving just like with_file.
- Usage of variables like `"{{ inventory_hostname }}"` in the filepath can be used to set up random passwords per host, which simplifies password management in `"host_vars"` variables.
- A special case is using /dev/null as a path. The password lookup will generate a new random password each time, but will not write it to /dev/null. This can be used when you need a password without storing it on the controller.

## [Terms](password_lookup.md#id2)

| Parameter | Comments |
| --- | --- |
| **Terms**  string / required | path to the file that stores/will store the passwords |

## [Keyword parameters](password_lookup.md#id3)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('ansible.builtin.password', key1=value1, key2=value2, ...)` and `query('ansible.builtin.password', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **chars**  list / elements=string | A list of names that compose a custom character set in the generated passwords.  By default generated passwords contain a random mix of upper and lowercase ASCII letters, the numbers 0-9, and punctuation (”. , : - _”).  They can be either parts of Python’s string module attributes or represented literally ( :, -).  Though string modules can vary by Python version, valid values for both major releases include: ‘ascii_lowercase’, ‘ascii_uppercase’, ‘digits’, ‘hexdigits’, ‘octdigits’, ‘printable’, ‘punctuation’ and ‘whitespace’.  Be aware that Python’s ‘hexdigits’ includes lower and upper case versions of a-f, so it is not a good choice as it doubles the chances of those values for systems that won’t distinguish case, distorting the expected entropy.  when using a comma separated string, to enter comma use two commas ‘,,’ somewhere - preferably at the end. Quotes and double quotes are not supported.  Default: `["ascii_letters", "digits", ".,:-_"]` |
| **encrypt**  string | Which hash scheme to encrypt the returning password, should be one hash scheme from `passlib.hash; md5_crypt, bcrypt, sha256_crypt, sha512_crypt`.  If not provided, the password will be returned in plain text.  Note that the password is always stored as plain text, only the returning password is encrypted.  Encrypt also forces saving the salt value for idempotence.  Note that before 2.6 this option was incorrectly labeled as a boolean for a long time. |
| **ident**  string  added in ansible-core 2.12 | Specify version of Bcrypt algorithm to be used while using `encrypt` as `bcrypt`.  The parameter is only available for `bcrypt` - <https://passlib.readthedocs.io/en/stable/lib/passlib.hash.bcrypt.html#passlib.hash.bcrypt>.  Other hash types will simply ignore this parameter.  Valid values for this parameter are: `2`, `2a`, `2y`, `2b`. |
| **length**  integer | The length of the generated password.  Default: `20` |
| **seed**  string  added in ansible-core 2.12 | A seed to initialize the random number generator.  Identical seeds will yield identical passwords.  Use this for random-but-idempotent password generation. |

## [Notes](password_lookup.md#id4)

> **Note:**
>
> - When keyword and positional parameters are used together, positional parameters must be listed before keyword parameters:
>   `lookup('ansible.builtin.password', term1, term2, key1=value1, key2=value2)` and `query('ansible.builtin.password', term1, term2, key1=value1, key2=value2)`
> - A great alternative to the password lookup plugin, if you don’t need to generate random passwords on a per-host basis, would be to use Vault in playbooks. Read the documentation there and consider using it first, it will be more desirable for most applications.
> - If the file already exists, no data will be written to it. If the file has contents, those contents will be read in as the password. Empty files cause the password to return as an empty string.
> - As all lookups, this runs on the Ansible host as the user running the playbook, and “become” does not apply, the target file must be readable by the playbook user, or, if it does not exist, the playbook user must have sufficient privileges to create it. (So, for example, attempts to write into areas such as /etc will fail unless the entire playbook is being run as root).

## [Examples](password_lookup.md#id5)

```yaml+jinja
- name: create a mysql user with a random password
  community.mysql.mysql_user:
    name: "{{ client }}"
    password: "{{ lookup('ansible.builtin.password', 'credentials/' + client + '/' + tier + '/' + role + '/mysqlpassword length=15') }}"
    priv: "{{ client }}_{{ tier }}_{{ role }}.*:ALL"

- name: create a mysql user with a random password using only ascii letters
  community.mysql.mysql_user:
    name: "{{ client }}"
    password: "{{ lookup('ansible.builtin.password', '/tmp/passwordfile chars=ascii_letters') }}"
    priv: '{{ client }}_{{ tier }}_{{ role }}.*:ALL'

- name: create a mysql user with an 8 character random password using only digits
  community.mysql.mysql_user:
    name: "{{ client }}"
    password: "{{ lookup('ansible.builtin.password', '/tmp/passwordfile length=8 chars=digits') }}"
    priv: "{{ client }}_{{ tier }}_{{ role }}.*:ALL"

- name: create a mysql user with a random password using many different char sets
  community.mysql.mysql_user:
    name: "{{ client }}"
    password: "{{ lookup('ansible.builtin.password', '/tmp/passwordfile chars=ascii_letters,digits,punctuation') }}"
    priv: "{{ client }}_{{ tier }}_{{ role }}.*:ALL"

- name: create lowercase 8 character name for Kubernetes pod name
  ansible.builtin.set_fact:
    random_pod_name: "web-{{ lookup('ansible.builtin.password', '/dev/null chars=ascii_lowercase,digits length=8') }}"

- name: create random but idempotent password
  ansible.builtin.set_fact:
    password: "{{ lookup('ansible.builtin.password', '/dev/null', seed=inventory_hostname) }}"
```

## [Return Value](password_lookup.md#id6)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=string | a password  Returned: success |

### Authors

- Daniel Hokka Zakrisson
- Javier Candeira
- Maykel Moya

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible/ansible/issues)
[Repository (Sources)](https://github.com/ansible/ansible)
[Communication](index.md#communication-for-ansible-builtin)
