---
collection: ansible
version: "6"
title: "community.postgresql.postgresql_pg_hba module – Add, remove or modify a rule in a pg_hba file"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/postgresql/postgresql_pg_hba_module.html
fetched_at: 2026-07-27T17:20:21+00:00
---
# community.postgresql.postgresql_pg_hba module – Add, remove or modify a rule in a pg_hba file

> **Note:**
>
> This module is part of the [community.postgresql collection](https://galaxy.ansible.com/community/postgresql) (version 2.3.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.postgresql`.
> You need further requirements to be able to use this module,
> see [Requirements](postgresql_pg_hba_module.md#ansible-collections-community-postgresql-postgresql-pg-hba-module-requirements) for details.
>
> To use it in a playbook, specify: `community.postgresql.postgresql_pg_hba`.

- [Synopsis](postgresql_pg_hba_module.md#synopsis)
- [Requirements](postgresql_pg_hba_module.md#requirements)
- [Parameters](postgresql_pg_hba_module.md#parameters)
- [Notes](postgresql_pg_hba_module.md#notes)
- [See Also](postgresql_pg_hba_module.md#see-also)
- [Examples](postgresql_pg_hba_module.md#examples)
- [Return Values](postgresql_pg_hba_module.md#return-values)

## [Synopsis](postgresql_pg_hba_module.md#id1)

- The fundamental function of the module is to create, or delete lines in pg_hba files.
- The lines in the file should be in a typical pg_hba form and lines should be unique per key (type, databases, users, source). If they are not unique and the SID is ‘the one to change’, only one for *state=present* or none for *state=absent* of the SID’s will remain.

## [Requirements](postgresql_pg_hba_module.md#id2)

The below requirements are needed on the host that executes this module.

- ipaddress

## [Parameters](postgresql_pg_hba_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **address**  aliases: source, src  string | The source address/net where the connections could come from.  Will not be used for entries of *type*=`local`.  You can also use keywords `all`, `samehost`, and `samenet`.  Default: `"samehost"` |
| **attributes**  aliases: attr  string | The attributes the resulting filesystem object should have.  To get supported flags look at the man page for *chattr* on the target system.  This string should contain the attributes in the same order as the one displayed by *lsattr*.  The `=` operator is assumed as default, otherwise `+` or `-` operators need to be included in the string. |
| **backup**  boolean | If set, create a backup of the `pg_hba` file before it is modified. The location of the backup is returned in the (backup) variable by this module.  Choices:   - `false` ← (default) - `true` |
| **backup_file**  string | Write backup to a specific backupfile rather than a temp file. |
| **comment**  string  added in community.postgresql 1.5.0 | A comment that will be placed in the same line behind the rule. See also the *keep_comments_at_rules* parameter. |
| **contype**  string | Type of the rule. If not set, `postgresql_pg_hba` will only return contents.  Choices:   - `"local"` - `"host"` - `"hostnossl"` - `"hostssl"` - `"hostgssenc"` - `"hostnogssenc"` |
| **create**  boolean | Create an `pg_hba` file if none exists.  When set to false, an error is raised when the `pg_hba` file doesn’t exist.  Choices:   - `false` ← (default) - `true` |
| **databases**  string | Databases this line applies to.  Default: `"all"` |
| **dest**  path / required | Path to `pg_hba` file to modify. |
| **group**  string | Name of the group that should own the filesystem object, as would be fed to *chown*.  When left unspecified, it uses the current group of the current user unless you are root, in which case it can preserve the previous ownership. |
| **keep_comments_at_rules**  boolean  added in community.postgresql 1.5.0 | If `true`, comments that stand together with a rule in one line are kept behind that line.  If `false`, such comments are moved to the beginning of the file, like all other comments.  Choices:   - `false` ← (default) - `true` |
| **method**  string | Authentication method to be used.  Choices:   - `"cert"` - `"gss"` - `"ident"` - `"krb5"` - `"ldap"` - `"md5"` ← (default) - `"pam"` - `"password"` - `"peer"` - `"radius"` - `"reject"` - `"scram-sha-256"` - `"sspi"` - `"trust"` |
| **mode**  any | The permissions the resulting filesystem object should have.  For those used to */usr/bin/chmod* remember that modes are actually octal numbers. You must either add a leading zero so that Ansible’s YAML parser knows it is an octal number (like `0644` or `01777`) or quote it (like `'644'` or `'1777'`) so Ansible receives a string and can do its own conversion from string into number.  Giving Ansible a number without following one of these rules will end up with a decimal number which will have unexpected results.  As of Ansible 1.8, the mode may be specified as a symbolic mode (for example, `u+rwx` or `u=rw,g=r,o=r`).  If `mode` is not specified and the destination filesystem object **does not** exist, the default `umask` on the system will be used when setting the mode for the newly created filesystem object.  If `mode` is not specified and the destination filesystem object **does** exist, the mode of the existing filesystem object will be used.  Specifying `mode` is the best way to ensure filesystem objects are created with the correct permissions. See CVE-2020-1736 for further details. |
| **netmask**  string | The netmask of the source address. |
| **options**  string | Additional options for the authentication *method*. |
| **order**  string | The entries will be written out in a specific order. With this option you can control by which field they are ordered first, second and last. s=source, d=databases, u=users. This option is deprecated since 2.9 and will be removed in community.postgresql 3.0.0. Sortorder is now hardcoded to sdu.  Choices:   - `"sdu"` ← (default) - `"sud"` - `"dsu"` - `"dus"` - `"usd"` - `"uds"` |
| **overwrite**  boolean | Remove all existing rules before adding rules. (Like *state=absent* for all pre-existing rules.)  Choices:   - `false` ← (default) - `true` |
| **owner**  string | Name of the user that should own the filesystem object, as would be fed to *chown*.  When left unspecified, it uses the current user unless you are root, in which case it can preserve the previous ownership. |
| **rules**  list / elements=dictionary | A list of objects, specifying rules for the pg_hba.conf. Use this to manage multiple rules at once.  Each object can have the following keys (the ‘rule-specific arguments’), which are treated the same as if they were arguments of this module:  `address`, `comment`, `contype`, `databases`, `method`, `netmask`, `options`, `state`, `users`  See also `rules_behavior`. |
| **rules_behavior**  string | Configure how the *rules* argument works together with the rule-specific arguments outside the *rules* argument.  See *rules* for the complete list of rule-specific arguments.  When set to `conflict`, fail if *rules* and, for example, *address* are set.  If `combine`, the normal rule-specific arguments are not defining a rule, but are used as defaults for the arguments in the *rules* argument.  Is used only when *rules* is specified, ignored otherwise.  Choices:   - `"conflict"` ← (default) - `"combine"` |
| **selevel**  string | The level part of the SELinux filesystem object context.  This is the MLS/MCS attribute, sometimes known as the `range`.  When set to `_default`, it will use the `level` portion of the policy if available. |
| **serole**  string | The role part of the SELinux filesystem object context.  When set to `_default`, it will use the `role` portion of the policy if available. |
| **setype**  string | The type part of the SELinux filesystem object context.  When set to `_default`, it will use the `type` portion of the policy if available. |
| **seuser**  string | The user part of the SELinux filesystem object context.  By default it uses the `system` policy, where applicable.  When set to `_default`, it will use the `user` portion of the policy if available. |
| **state**  string | The lines will be added/modified when `state=present` and removed when `state=absent`.  Choices:   - `"absent"` - `"present"` ← (default) |
| **unsafe_writes**  boolean | Influence when to use atomic operation to prevent data corruption or inconsistent reads from the target filesystem object.  By default this module uses atomic operations to prevent data corruption or inconsistent reads from the target filesystem objects, but sometimes systems are configured or just broken in ways that prevent this. One example is docker mounted filesystem objects, which cannot be updated atomically from inside the container and can only be written in an unsafe manner.  This option allows Ansible to fall back to unsafe methods of updating filesystem objects when atomic operations fail (however, it doesn’t force Ansible to perform unsafe writes).  IMPORTANT! Unsafe writes are subject to race conditions and can lead to data corruption.  Choices:   - `false` ← (default) - `true` |
| **users**  string | Users this line applies to.  Default: `"all"` |

## [Notes](postgresql_pg_hba_module.md#id4)

> **Note:**
>
> - The default authentication assumes that on the host, you are either logging in as or sudo’ing to an account with appropriate permissions to read and modify the file.
> - This module also returns the pg_hba info. You can use this module to only retrieve it by only specifying *dest*. The info can be found in the returned data under key pg_hba, being a list, containing a dict per rule.
> - This module will sort resulting `pg_hba` files if a rule change is required. This could give unexpected results with manual created hba files, if it was improperly sorted. For example a rule was created for a net first and for a ip in that net range next. In that situation, the ‘ip specific rule’ will never hit, it is in the `pg_hba` file obsolete. After the `pg_hba` file is rewritten by the [community.postgresql.postgresql_pg_hba](postgresql_pg_hba_module.md#ansible-collections-community-postgresql-postgresql-pg-hba-module) module, the ip specific rule will be sorted above the range rule. And then it will hit, which will give unexpected results.
> - With the ‘order’ parameter you can control which field is used to sort first, next and last.
> - The module supports a check mode and a diff mode.

## [See Also](postgresql_pg_hba_module.md#id5)

> **See also:**
>
> [PostgreSQL pg_hba.conf file reference](https://www.postgresql.org/docs/current/auth-pg-hba-conf.html)
> :   Complete reference of the PostgreSQL pg_hba.conf file documentation.

## [Examples](postgresql_pg_hba_module.md#id6)

```yaml+jinja
- name: Grant users joe and simon access to databases sales and logistics from ipv6 localhost ::1/128 using peer authentication
  community.postgresql.postgresql_pg_hba:
    dest: /var/lib/postgres/data/pg_hba.conf
    contype: host
    users: joe,simon
    source: ::1
    databases: sales,logistics
    method: peer
    create: true

- name: Grant user replication from network 192.168.0.100/24 access for replication with client cert authentication
  community.postgresql.postgresql_pg_hba:
    dest: /var/lib/postgres/data/pg_hba.conf
    contype: host
    users: replication
    source: 192.168.0.100/24
    databases: replication
    method: cert

- name: Revoke access from local user mary on database mydb
  community.postgresql.postgresql_pg_hba:
    dest: /var/lib/postgres/data/pg_hba.conf
    contype: local
    users: mary
    databases: mydb
    state: absent

- name: Grant some_user access to some_db, comment that and keep other rule-specific comments attached to their rules
  community.postgresql.postgresql_pg_hba:
    dest: /var/lib/postgres/data/pg_hba.conf
    contype: host
    users: some_user
    databases: some_db
    method: md5
    source: ::/0
    keep_comments_at_rules: true
    comment: "this rule is an example"

- name: Replace everything with a new set of rules
  community.postgresql.postgresql_pg_hba:
    dest: /var/lib/postgres/data/pg_hba.conf
    overwrite: true # remove preexisting rules

    # custom defaults
    rules_behavior: combine
    contype: hostssl
    address: 2001:db8::/64
    comment: added in bulk

    rules:
    - users: user1
      databases: db1
      # contype, address and comment come from custom default
    - users: user2
      databases: db2
      comment: added with love # overwrite custom default for this rule
      # contype and address come from custom default
    - users: user3
      databases: db3
      # contype, address and comment come from custom default
```

## [Return Values](postgresql_pg_hba_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **backup_file**  string | File that the original pg_hba file was backed up to.  Returned: changed  Sample: `"/tmp/pg_hba_jxobj_p"` |
| **msgs**  list / elements=string | List of textual messages what was done.  Returned: always  Sample: `{"msgs": ["Removing", "Changed", "Writing"]}` |
| **pg_hba**  list / elements=string | List of the pg_hba rules as they are configured in the specified hba file.  Returned: always  Sample: `{"pg_hba": [{"db": "all", "method": "md5", "src": "samehost", "type": "host", "usr": "all"}]}` |

### Authors

- Sebastiaan Mannem (@sebasmannem)
- Felix Hamme (@betanummeric)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.postgresql/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.postgresql)
[Report an issue](https://github.com/ansible-collections/community.postgresql/issues/new/choose)
[Communication](index.md#communication-for-community-postgresql)
