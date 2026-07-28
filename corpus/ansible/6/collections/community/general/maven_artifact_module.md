---
collection: ansible
version: "6"
title: "community.general.maven_artifact module – Downloads an Artifact from a Maven Repository"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/maven_artifact_module.html
fetched_at: 2026-07-27T17:10:53+00:00
---
# community.general.maven_artifact module – Downloads an Artifact from a Maven Repository

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
> see [Requirements](maven_artifact_module.md#ansible-collections-community-general-maven-artifact-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.maven_artifact`.

- [Synopsis](maven_artifact_module.md#synopsis)
- [Requirements](maven_artifact_module.md#requirements)
- [Parameters](maven_artifact_module.md#parameters)
- [Examples](maven_artifact_module.md#examples)

## [Synopsis](maven_artifact_module.md#id1)

- Downloads an artifact from a maven repository given the maven coordinates provided to the module.
- Can retrieve snapshots or release versions of the artifact and will resolve the latest available version if one is not available.

## [Requirements](maven_artifact_module.md#id2)

The below requirements are needed on the host that executes this module.

- lxml
- boto if using a S3 repository (s3://…)

## [Parameters](maven_artifact_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **artifact_id**  string / required | The maven artifactId coordinate |
| **attributes**  aliases: attr  string | The attributes the resulting filesystem object should have.  To get supported flags look at the man page for *chattr* on the target system.  This string should contain the attributes in the same order as the one displayed by *lsattr*.  The `=` operator is assumed as default, otherwise `+` or `-` operators need to be included in the string. |
| **checksum_alg**  string  added in community.general 3.2.0 | If `md5`, checksums will use the MD5 algorithm. This is the default.  If `sha1`, checksums will use the SHA1 algorithm. This can be used on systems configured to use FIPS-compliant algorithms, since MD5 will be blocked on such systems.  Choices:   - `"md5"` ← (default) - `"sha1"` |
| **classifier**  string | The maven classifier coordinate  Default: `""` |
| **client_cert**  path  added in community.general 1.3.0 | PEM formatted certificate chain file to be used for SSL client authentication.  This file can also include the key as well, and if the key is included, *client_key* is not required. |
| **client_key**  path  added in community.general 1.3.0 | PEM formatted file that contains your private key to be used for SSL client authentication.  If *client_cert* contains both the certificate and key, this option is not required. |
| **dest**  path / required | The path where the artifact should be written to  If file mode or ownerships are specified and destination path already exists, they affect the downloaded file |
| **directory_mode**  string | Filesystem permission mode applied recursively to *dest* when it is a directory. |
| **extension**  string | The maven type/extension coordinate  Default: `"jar"` |
| **force_basic_auth**  boolean  added in community.general 0.2.0 | httplib2, the library used by the uri module only sends authentication information when a webservice responds to an initial request with a 401 status. Since some basic auth services do not properly send a 401, logins will fail. This option forces the sending of the Basic authentication header upon initial request.  Choices:   - `false` ← (default) - `true` |
| **group**  string | Name of the group that should own the filesystem object, as would be fed to *chown*.  When left unspecified, it uses the current group of the current user unless you are root, in which case it can preserve the previous ownership. |
| **group_id**  string / required | The Maven groupId coordinate |
| **headers**  dictionary | Add custom HTTP headers to a request in hash/dict format. |
| **keep_name**  boolean | If `true`, the downloaded artifact’s name is preserved, i.e the version number remains part of it.  This option only has effect when `dest` is a directory and `version` is set to `latest` or `version_by_spec` is defined.  Choices:   - `false` ← (default) - `true` |
| **mode**  any | The permissions the resulting filesystem object should have.  For those used to */usr/bin/chmod* remember that modes are actually octal numbers. You must either add a leading zero so that Ansible’s YAML parser knows it is an octal number (like `0644` or `01777`) or quote it (like `'644'` or `'1777'`) so Ansible receives a string and can do its own conversion from string into number.  Giving Ansible a number without following one of these rules will end up with a decimal number which will have unexpected results.  As of Ansible 1.8, the mode may be specified as a symbolic mode (for example, `u+rwx` or `u=rw,g=r,o=r`).  If `mode` is not specified and the destination filesystem object **does not** exist, the default `umask` on the system will be used when setting the mode for the newly created filesystem object.  If `mode` is not specified and the destination filesystem object **does** exist, the mode of the existing filesystem object will be used.  Specifying `mode` is the best way to ensure filesystem objects are created with the correct permissions. See CVE-2020-1736 for further details. |
| **owner**  string | Name of the user that should own the filesystem object, as would be fed to *chown*.  When left unspecified, it uses the current user unless you are root, in which case it can preserve the previous ownership. |
| **password**  aliases: aws_secret_access_key  string | The password to authenticate with to the Maven Repository. Use AWS secret access key of the repository is hosted on S3 |
| **repository_url**  string | The URL of the Maven Repository to download from.  Use s3://… if the repository is hosted on Amazon S3, added in version 2.2.  Use <file://>… if the repository is local, added in version 2.6  Default: `"https://repo1.maven.org/maven2"` |
| **selevel**  string | The level part of the SELinux filesystem object context.  This is the MLS/MCS attribute, sometimes known as the `range`.  When set to `_default`, it will use the `level` portion of the policy if available. |
| **serole**  string | The role part of the SELinux filesystem object context.  When set to `_default`, it will use the `role` portion of the policy if available. |
| **setype**  string | The type part of the SELinux filesystem object context.  When set to `_default`, it will use the `type` portion of the policy if available. |
| **seuser**  string | The user part of the SELinux filesystem object context.  By default it uses the `system` policy, where applicable.  When set to `_default`, it will use the `user` portion of the policy if available. |
| **state**  string | The desired state of the artifact  Choices:   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer | Specifies a timeout in seconds for the connection attempt  Default: `10` |
| **unredirected_headers**  list / elements=string  added in community.general 5.2.0 | A list of headers that should not be included in the redirection. This headers are sent to the fetch_url `fetch_url` function.  On ansible-core version 2.12 or later, the default of this option is `[Authorization, Cookie]`.  Useful if the redirection URL does not need to have sensitive headers in the request.  Requires ansible-core version 2.12 or later. |
| **unsafe_writes**  boolean | Influence when to use atomic operation to prevent data corruption or inconsistent reads from the target filesystem object.  By default this module uses atomic operations to prevent data corruption or inconsistent reads from the target filesystem objects, but sometimes systems are configured or just broken in ways that prevent this. One example is docker mounted filesystem objects, which cannot be updated atomically from inside the container and can only be written in an unsafe manner.  This option allows Ansible to fall back to unsafe methods of updating filesystem objects when atomic operations fail (however, it doesn’t force Ansible to perform unsafe writes).  IMPORTANT! Unsafe writes are subject to race conditions and can lead to data corruption.  Choices:   - `false` ← (default) - `true` |
| **username**  aliases: aws_secret_key  string | The username to authenticate as to the Maven Repository. Use AWS secret key of the repository is hosted on S3 |
| **validate_certs**  boolean | If `false`, SSL certificates will not be validated. This should only be set to `false` when no other option exists.  Choices:   - `false` - `true` ← (default) |
| **verify_checksum**  string | If `never`, the MD5/SHA1 checksum will never be downloaded and verified.  If `download`, the MD5/SHA1 checksum will be downloaded and verified only after artifact download. This is the default.  If `change`, the MD5/SHA1 checksum will be downloaded and verified if the destination already exist, to verify if they are identical. This was the behaviour before 2.6. Since it downloads the checksum before (maybe) downloading the artifact, and since some repository software, when acting as a proxy/cache, return a 404 error if the artifact has not been cached yet, it may fail unexpectedly. If you still need it, you should consider using `always` instead - if you deal with a checksum, it is better to use it to verify integrity after download.  `always` combines `download` and `change`.  Choices:   - `"never"` - `"download"` ← (default) - `"change"` - `"always"` |
| **version**  string | The maven version coordinate  Mutually exclusive with *version_by_spec*. |
| **version_by_spec**  string  added in community.general 0.2.0 | The maven dependency version ranges.  See supported version ranges on <https://cwiki.apache.org/confluence/display/MAVENOLD/Dependency%2BMediation%2Band%2BConflict%2BResolution>  The range type “(,1.0],[1.2,)” and “(,1.1),(1.1,)” is not supported.  Mutually exclusive with *version*. |

## [Examples](maven_artifact_module.md#id4)

```yaml+jinja
- name: Download the latest version of the JUnit framework artifact from Maven Central
  community.general.maven_artifact:
    group_id: junit
    artifact_id: junit
    dest: /tmp/junit-latest.jar

- name: Download JUnit 4.11 from Maven Central
  community.general.maven_artifact:
    group_id: junit
    artifact_id: junit
    version: 4.11
    dest: /tmp/junit-4.11.jar

- name: Download an artifact from a private repository requiring authentication
  community.general.maven_artifact:
    group_id: com.company
    artifact_id: library-name
    repository_url: 'https://repo.company.com/maven'
    username: user
    password: pass
    dest: /tmp/library-name-latest.jar

- name: Download an artifact from a private repository requiring certificate authentication
  community.general.maven_artifact:
    group_id: com.company
    artifact_id: library-name
    repository_url: 'https://repo.company.com/maven'
    client_cert: /path/to/cert.pem
    client_key: /path/to/key.pem
    dest: /tmp/library-name-latest.jar

- name: Download a WAR File to the Tomcat webapps directory to be deployed
  community.general.maven_artifact:
    group_id: com.company
    artifact_id: web-app
    extension: war
    repository_url: 'https://repo.company.com/maven'
    dest: /var/lib/tomcat7/webapps/web-app.war

- name: Keep a downloaded artifact's name, i.e. retain the version
  community.general.maven_artifact:
    version: latest
    artifact_id: spring-core
    group_id: org.springframework
    dest: /tmp/
    keep_name: true

- name: Download the latest version of the JUnit framework artifact from Maven local
  community.general.maven_artifact:
    group_id: junit
    artifact_id: junit
    dest: /tmp/junit-latest.jar
    repository_url: "file://{{ lookup('env','HOME') }}/.m2/repository"

- name: Download the latest version between 3.8 and 4.0 (exclusive) of the JUnit framework artifact from Maven Central
  community.general.maven_artifact:
    group_id: junit
    artifact_id: junit
    version_by_spec: "[3.8,4.0)"
    dest: /tmp/
```

### Authors

- Chris Schmidt (@chrisisbeef)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
