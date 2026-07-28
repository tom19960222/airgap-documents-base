---
collection: ansible
version: "6"
title: "Using collections"
source_url: https://docs.ansible.com/projects/ansible/6/user_guide/collections_using.html
fetched_at: 2026-07-27T16:40:31+00:00
---
# Using collections

Collections are a distribution format for Ansible content that can include playbooks, roles, modules, and plugins. As modules move from the core Ansible repository into collections, the module documentation will move to the [collections pages](../collections/index.md#list-of-collections).

You can install and use collections through a distribution server, such as [Ansible Galaxy](https://galaxy.ansible.com) or a [Pulp 3 Galaxy server](https://galaxyng.netlify.app/).

- For details on how to *develop* collections see [Developing collections](../dev_guide/developing_collections.md#developing-collections).
- For the current development status of Collections and FAQ see [Ansible Collections Community Guide](https://github.com/ansible-collections/overview/blob/main/README.rst).

- [Installing collections](collections_using.md#installing-collections)

  - [Installing collections with `ansible-galaxy`](collections_using.md#installing-collections-with-ansible-galaxy)
  - [Installing collections with signature verification](collections_using.md#installing-collections-with-signature-verification)
  - [Installing an older version of a collection](collections_using.md#installing-an-older-version-of-a-collection)
  - [Install multiple collections with a requirements file](collections_using.md#install-multiple-collections-with-a-requirements-file)
  - [Downloading a collection for offline use](collections_using.md#downloading-a-collection-for-offline-use)
  - [Installing a collection from source files](collections_using.md#installing-a-collection-from-source-files)
  - [Installing a collection from a git repository](collections_using.md#installing-a-collection-from-a-git-repository)
  - [Configuring the `ansible-galaxy` client](collections_using.md#configuring-the-ansible-galaxy-client)
- [Downloading collections](collections_using.md#downloading-collections)
- [Listing collections](collections_using.md#listing-collections)
- [Verifying collections](collections_using.md#verifying-collections)

  - [Verifying collections with `ansible-galaxy`](collections_using.md#verifying-collections-with-ansible-galaxy)
  - [Verifying signed collections](collections_using.md#verifying-signed-collections)
- [Using collections in a Playbook](collections_using.md#using-collections-in-a-playbook)
- [Simplifying module names with the `collections` keyword](collections_using.md#simplifying-module-names-with-the-collections-keyword)

  - [Using `collections` in roles](collections_using.md#using-collections-in-roles)
  - [Using `collections` in playbooks](collections_using.md#using-collections-in-playbooks)
- [Using a playbook from a collection](collections_using.md#using-a-playbook-from-a-collection)

## [Installing collections](collections_using.md#id3)

> **Note:**
>
> If you install a collection manually as described in this paragraph, the collection will not be upgraded automatically when you upgrade the `ansible` package or `ansible-core`.

### [Installing collections with `ansible-galaxy`](collections_using.md#id4)

By default, `ansible-galaxy collection install` uses <https://galaxy.ansible.com> as the Galaxy server (as listed in the
`ansible.cfg` file under [GALAXY_SERVER](../reference_appendices/config.md#galaxy-server)). You do not need any
further configuration.

See [Configuring the ansible-galaxy client](collections_using.md#galaxy-server-config) if you are using any other Galaxy server, such as Red Hat Automation Hub.

To install a collection hosted in Galaxy:

```bash
ansible-galaxy collection install my_namespace.my_collection
```

To upgrade a collection to the latest available version from the Galaxy server you can use the `--upgrade` option:

```bash
ansible-galaxy collection install my_namespace.my_collection --upgrade
```

You can also directly use the tarball from your build:

```bash
ansible-galaxy collection install my_namespace-my_collection-1.0.0.tar.gz -p ./collections
```

You can build and install a collection from a local source directory. The `ansible-galaxy` utility builds the collection using the `MANIFEST.json` or `galaxy.yml`
metadata in the directory.

```bash
ansible-galaxy collection install /path/to/collection -p ./collections
```

You can also install multiple collections in a namespace directory.

```
ns/
├── collection1/
│   ├── MANIFEST.json
│   └── plugins/
└── collection2/
    ├── galaxy.yml
    └── plugins/
```

```bash
ansible-galaxy collection install /path/to/ns -p ./collections
```

> **Note:**
>
> The install command automatically appends the path `ansible_collections` to the one specified with the `-p` option unless the
> parent directory is already in a folder called `ansible_collections`.

When using the `-p` option to specify the install path, use one of the values configured in [COLLECTIONS_PATHS](../reference_appendices/config.md#collections-paths), as this is
where Ansible itself will expect to find collections. If you don’t specify a path, `ansible-galaxy collection install` installs
the collection to the first path defined in [COLLECTIONS_PATHS](../reference_appendices/config.md#collections-paths), which by default is `~/.ansible/collections`

You can also keep a collection adjacent to the current playbook, under a `collections/ansible_collections/` directory structure.

```
./
├── play.yml
├── collections/
│   └── ansible_collections/
│               └── my_namespace/
│                   └── my_collection/<collection structure lives here>
```

See [Collection structure](../dev_guide/developing_collections_structure.md#collection-structure) for details on the collection directory structure.

### [Installing collections with signature verification](collections_using.md#id5)

If a collection has been signed by a [distribution server](../reference_appendices/glossary.md#term-Distribution-server), the server will provide ASCII armored, detached signatures to verify the authenticity of the `MANIFEST.json` before using it to verify the collection’s contents. This option is not available on all distribution servers. See [Distributing collections](../dev_guide/developing_collections_distributing.md#distributing-collections) for a table listing which servers support collection signing.

To use signature verification for signed collections:

1. [Configured a GnuPG keyring](../reference_appendices/config.md#galaxy-gpg-keyring) for `ansible-galaxy`, or provide the path to the keyring with the `--keyring` option when you install the signed collection.
2. Import the public key from the distribution server into that keyring.

   ```bash
   gpg --import --no-default-keyring --keyring ~/.ansible/pubring.kbx my-public-key.asc
   ```
3. Verify the signature when you install the collection.

   ```bash
   ansible-galaxy collection install my_namespace.my_collection --keyring ~/.ansible/pubring.kbx
   ```

   The `--keyring` option is not necessary if you have [configured a GnuPG keyring](../reference_appendices/config.md#galaxy-gpg-keyring).
4. Optionally, verify the signature at any point after installation to prove the collection has not been tampered with. See [Verifying signed collections](collections_using.md#verify-signed-collections) for details.

You can also include signatures in addition to those provided by the distribution server. Use the `--signature` option to verify the collection’s `MANIFEST.json` with these additional signatures. Supplemental signatures should be provided as URIs.

```bash
ansible-galaxy collection install my_namespace.my_collection --signature https://examplehost.com/detached_signature.asc --keyring ~/.ansible/pubring.kbx
```

GnuPG verification only occurs for collections installed from a distribution server. User-provided signatures are not used to verify collections installed from git repositories, source directories, or URLs/paths to tar.gz files.

You can also include additional signatures in the collection `requirements.yml` file under the `signatures` key.

```yaml
# requirements.yml
collections:
  - name: ns.coll
    version: 1.0.0
    signatures:
      - https://examplehost.com/detached_signature.asc
      - file:///path/to/local/detached_signature.asc
```

See [collection requirements file](collections_using.md#collection-requirements-file) for details on how to install collections with this file.

By default, verification is considered successful if a minimum of 1 signature successfully verifies the collection. The number of required signatures can be configured with `--required-valid-signature-count` or [GALAXY_REQUIRED_VALID_SIGNATURE_COUNT](../reference_appendices/config.md#galaxy-required-valid-signature-count). All signatures can be required by setting the option to `all`. To fail signature verification if no valid signatures are found, prepend the value with `+`, such as `+all` or `+1`.

```bash
export ANSIBLE_GALAXY_GPG_KEYRING=~/.ansible/pubring.kbx
export ANSIBLE_GALAXY_REQUIRED_VALID_SIGNATURE_COUNT=2
ansible-galaxy collection install my_namespace.my_collection --signature https://examplehost.com/detached_signature.asc --signature file:///path/to/local/detached_signature.asc
```

Certain GnuPG errors can be ignored with `--ignore-signature-status-code` or [GALAXY_REQUIRED_VALID_SIGNATURE_COUNT](../reference_appendices/config.md#galaxy-required-valid-signature-count). [GALAXY_REQUIRED_VALID_SIGNATURE_COUNT](../reference_appendices/config.md#galaxy-required-valid-signature-count) should be a list, and `--ignore-signature-status-code` can be provided multiple times to ignore multiple additional error status codes.

This example requires any signatures provided by the distribution server to verify the collection except if they fail due to NO_PUBKEY:

```bash
export ANSIBLE_GALAXY_GPG_KEYRING=~/.ansible/pubring.kbx
export ANSIBLE_GALAXY_REQUIRED_VALID_SIGNATURE_COUNT=all
ansible-galaxy collection install my_namespace.my_collection --ignore-signature-status-code NO_PUBKEY
```

If verification fails for the example above, only errors other than NO_PUBKEY will be displayed.

If verification is unsuccessful, the collection will not be installed. GnuPG signature verification can be disabled with `--disable-gpg-verify` or by configuring [GALAXY_DISABLE_GPG_VERIFY](../reference_appendices/config.md#galaxy-disable-gpg-verify).

### [Installing an older version of a collection](collections_using.md#id6)

You can only have one version of a collection installed at a time. By default `ansible-galaxy` installs the latest available version. If you want to install a specific version, you can add a version range identifier. For example, to install the 1.0.0-beta.1 version of the collection:

```bash
ansible-galaxy collection install my_namespace.my_collection:==1.0.0-beta.1
```

You can specify multiple range identifiers separated by `,`. Use single quotes so the shell passes the entire command, including `>`, `!`, and other operators, along. For example, to install the most recent version that is greater than or equal to 1.0.0 and less than 2.0.0:

```bash
ansible-galaxy collection install 'my_namespace.my_collection:>=1.0.0,<2.0.0'
```

Ansible will always install the most recent version that meets the range identifiers you specify. You can use the following range identifiers:

- `*`: The most recent version. This is the default.
- `!=`: Not equal to the version specified.
- `==`: Exactly the version specified.
- `>=`: Greater than or equal to the version specified.
- `>`: Greater than the version specified.
- `<=`: Less than or equal to the version specified.
- `<`: Less than the version specified.

> **Note:**
>
> By default `ansible-galaxy` ignores pre-release versions. To install a pre-release version, you must use the `==` range identifier to require it explicitly.

### [Install multiple collections with a requirements file](collections_using.md#id7)

You can set up a `requirements.yml` file to install multiple collections in one command. This file is a YAML file in the format:

```yaml+jinja
---
collections:
# With just the collection name
- my_namespace.my_collection

# With the collection name, version, and source options
- name: my_namespace.my_other_collection
  version: 'version range identifiers (default: ``*``)'
  source: 'The Galaxy URL to pull the collection from (default: ``--api-server`` from cmdline)'
```

You can specify the following keys for each collection entry:

> - `name`
> - `version`
> - `signatures`
> - `source`
> - `type`

The `version` key uses the same range identifier format documented in [Installing an older version of a collection](collections_using.md#collections-older-version).

The `signatures` key accepts a list of signature sources that are used to supplement those found on the Galaxy server during collection installation and `ansible-galaxy collection verify`. Signature sources should be URIs that contain the detached signature. The `--keyring` CLI option must be provided if signatures are specified.

Signatures are only used to verify collections on Galaxy servers. User-provided signatures are not used to verify collections installed from git repositories, source directories, or URLs/paths to tar.gz files.

```yaml
collections:
  - name: namespace.name
    version: 1.0.0
    type: galaxy
    signatures:
      - https://examplehost.com/detached_signature.asc
      - file:///path/to/local/detached_signature.asc
```

The `type` key can be set to `file`, `galaxy`, `git`, `url`, `dir`, or `subdirs`. If `type` is omitted, the `name` key is used to implicitly determine the source of the collection.

When you install a collection with `type: git`, the `version` key can refer to a branch or to a [git commit-ish](https://git-scm.com/docs/gitglossary#def_commit-ish) object (commit or tag). For example:

```yaml
collections:
  - name: https://github.com/organization/repo_name.git
    type: git
    version: devel
```

You can also add roles to a `requirements.yml` file, under the `roles` key. The values follow the same format as a requirements file used in older Ansible releases.

```yaml
---
roles:
  # Install a role from Ansible Galaxy.
  - name: geerlingguy.java
    version: 1.9.6

collections:
  # Install a collection from Ansible Galaxy.
  - name: geerlingguy.php_roles
    version: 0.9.3
    source: https://galaxy.ansible.com
```

To install both roles and collections at the same time with one command, run the following:

```bash
$ ansible-galaxy install -r requirements.yml
```

Running `ansible-galaxy collection install -r` or `ansible-galaxy role install -r` will only install collections, or roles respectively.

> **Note:**
>
> Installing both roles and collections from the same requirements file will not work when specifying a custom collection or role install path. In this scenario the collections will be skipped and the command will process each like `ansible-galaxy role install` would.

### [Downloading a collection for offline use](collections_using.md#id8)

To download the collection tarball from Galaxy for offline use:

1. Navigate to the collection page.
2. Click on Download tarball.

You may also need to manually download any dependent collections.

### [Installing a collection from source files](collections_using.md#id9)

Ansible can also install from a source directory in several ways:

```yaml
collections:
  # directory containing the collection
  - source: ./my_namespace/my_collection/
    type: dir

  # directory containing a namespace, with collections as subdirectories
  - source: ./my_namespace/
    type: subdirs
```

Ansible can also install a collection collected with `ansible-galaxy collection build` or downloaded from Galaxy for offline use by specifying the output file directly:

```yaml
collections:
  - name: /tmp/my_namespace-my_collection-1.0.0.tar.gz
    type: file
```

> **Note:**
>
> Relative paths are calculated from the current working directory (where you are invoking `ansible-galaxy install -r` from). They are not taken relative to the `requirements.yml` file.

### [Installing a collection from a git repository](collections_using.md#id10)

You can install a collection from a git repository instead of from Galaxy or Automation Hub. As a developer, installing from a git repository lets you review your collection before you create the tarball and publish the collection. As a user, installing from a git repository lets you use collections or versions that are not in Galaxy or Automation Hub yet.

The repository must contain a `galaxy.yml` or `MANIFEST.json` file. This file provides metadata such as the version number and namespace of the collection.

#### Installing a collection from a git repository at the command line

To install a collection from a git repository at the command line, use the URI of the repository instead of a collection name or path to a `tar.gz` file. Use the prefix `git+`, unless you’re using SSH authentication with the user `git` (for example, `git@github.com:ansible-collections/ansible.windows.git`). You can specify a branch, commit, or tag using the comma-separated [git commit-ish](https://git-scm.com/docs/gitglossary#def_commit-ish) syntax.

For example:

```bash
# Install a collection in a repository using the latest commit on the branch 'devel'
ansible-galaxy collection install git+https://github.com/organization/repo_name.git,devel

# Install a collection from a private github repository
ansible-galaxy collection install git@github.com:organization/repo_name.git

# Install a collection from a local git repository
ansible-galaxy collection install git+file:///home/user/path/to/repo_name.git
```

> **Warning:**
>
> Embedding credentials into a git URI is not secure. Use safe authentication options to prevent your credentials from being exposed in logs or elsewhere.
>
> - Use [SSH](https://help.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh) authentication
> - Use [netrc](https://linux.die.net/man/5/netrc) authentication
> - Use [http.extraHeader](https://git-scm.com/docs/git-config#Documentation/git-config.txt-httpextraHeader) in your git configuration
> - Use [url.<base>.pushInsteadOf](https://git-scm.com/docs/git-config#Documentation/git-config.txt-urlltbasegtpushInsteadOf) in your git configuration

#### Specifying the collection location within the git repository

When you install a collection from a git repository, Ansible uses the collection `galaxy.yml` or `MANIFEST.json` metadata file to build the collection. By default, Ansible searches two paths for collection `galaxy.yml` or `MANIFEST.json` metadata files:

- The top level of the repository.
- Each directory in the repository path (one level deep).

If a `galaxy.yml` or `MANIFEST.json` file exists in the top level of the repository, Ansible uses the collection metadata in that file to install an individual collection.

```
├── galaxy.yml
├── plugins/
│   ├── lookup/
│   ├── modules/
│   └── module_utils/
└─── README.md
```

If a `galaxy.yml` or `MANIFEST.json` file exists in one or more directories in the repository path (one level deep), Ansible installs each directory with a metadata file as a collection. For example, Ansible installs both collection1 and collection2 from this repository structure by default:

```
├── collection1
│   ├── docs/
│   ├── galaxy.yml
│   └── plugins/
│       ├── inventory/
│       └── modules/
└── collection2
    ├── docs/
    ├── galaxy.yml
    ├── plugins/
    |   ├── filter/
    |   └── modules/
    └── roles/
```

If you have a different repository structure or only want to install a subset of collections, you can add a fragment to the end of your URI (before the optional comma-separated version) to indicate the location of the metadata file or files. The path should be a directory, not the metadata file itself. For example, to install only collection2 from the example repository with two collections:

```
ansible-galaxy collection install git+https://github.com/organization/repo_name.git#/collection2/
```

In some repositories, the main directory corresponds to the namespace:

```
namespace/
├── collectionA/
|   ├── docs/
|   ├── galaxy.yml
|   ├── plugins/
|   │   ├── README.md
|   │   └── modules/
|   ├── README.md
|   └── roles/
└── collectionB/
    ├── docs/
    ├── galaxy.yml
    ├── plugins/
    │   ├── connection/
    │   └── modules/
    ├── README.md
    └── roles/
```

You can install all collections in this repository, or install one collection from a specific commit:

```bash
# Install all collections in the namespace
ansible-galaxy collection install git+https://github.com/organization/repo_name.git#/namespace/

# Install an individual collection using a specific commit
ansible-galaxy collection install git+https://github.com/organization/repo_name.git#/namespace/collectionA/,7b60ddc245bc416b72d8ea6ed7b799885110f5e5
```

### [Configuring the `ansible-galaxy` client](collections_using.md#id11)

By default, `ansible-galaxy` uses <https://galaxy.ansible.com> as the Galaxy server (as listed in the `ansible.cfg` file under [GALAXY_SERVER](../reference_appendices/config.md#galaxy-server)).

You can use either option below to configure `ansible-galaxy collection` to use other servers (such as a custom Galaxy server):

- Set the server list in the [GALAXY_SERVER_LIST](../reference_appendices/config.md#galaxy-server-list) configuration option in [The configuration file](../reference_appendices/config.md#ansible-configuration-settings-locations).
- Use the `--server` command line argument to limit to an individual server.

To configure a Galaxy server list in `ansible.cfg`:

1. Add the `server_list` option under the `[galaxy]` section to one or more server names.
2. Create a new section for each server name.
3. Set the `url` option for each server name.
4. Optionally, set the API token for each server name. Go to <https://galaxy.ansible.com/me/preferences> and click Show API key.

> **Note:**
>
> The `url` option for each server name must end with a forward slash `/`. If you do not set the API token in your Galaxy server list, use the `--api-key` argument to pass in the token to the `ansible-galaxy collection publish` command.

The following example shows how to configure multiple servers:

```ini
[galaxy]
server_list = my_org_hub, release_galaxy, test_galaxy, my_galaxy_ng

[galaxy_server.my_org_hub]
url=https://automation.my_org/
username=my_user
password=my_pass

[galaxy_server.release_galaxy]
url=https://galaxy.ansible.com/
token=my_token

[galaxy_server.test_galaxy]
url=https://galaxy-dev.ansible.com/
token=my_test_token

[galaxy_server.my_galaxy_ng]
url=http://my_galaxy_ng:8000/api/automation-hub/
auth_url=http://my_keycloak:8080/auth/realms/myco/protocol/openid-connect/token
client_id=galaxy-ng
token=my_keycloak_access_token
```

> **Note:**
>
> You can use the `--server` command line argument to select an explicit Galaxy server in the `server_list` and
> the value of this argument should match the name of the server. To use a server not in the server list, set the value to the URL to access that server (all servers in the server list will be ignored). Also you cannot use the `--api-key` argument for any of the predefined servers. You can only use the `api_key` argument if you did not define a server list or if you specify a URL in the
> `--server` argument.

**Galaxy server list configuration options**

The [GALAXY_SERVER_LIST](../reference_appendices/config.md#galaxy-server-list) option is a list of server identifiers in a prioritized order. When searching for a
collection, the install process will search in that order, for example, `automation_hub` first, then `my_org_hub`, `release_galaxy`, and
finally `test_galaxy` until the collection is found. The actual Galaxy instance is then defined under the section
`[galaxy_server.{{ id }}]` where `{{ id }}` is the server identifier defined in the list. This section can then
define the following keys:

- `url`: The URL of the Galaxy instance to connect to. Required.
- `token`: An API token key to use for authentication against the Galaxy instance. Mutually exclusive with `username`.
- `username`: The username to use for basic authentication against the Galaxy instance. Mutually exclusive with `token`.
- `password`: The password to use, in conjunction with `username`, for basic authentication.
- `auth_url`: The URL of a Keycloak server ‘token_endpoint’ if using SSO authentication (for example, galaxyNG). Mutually exclusive with `username`. Requires `token`.
- `validate_certs`: Whether or not to verify TLS certificates for the Galaxy server. This defaults to True unless the `--ignore-certs` option is provided or `GALAXY_IGNORE_CERTS` is configured to True.
- `client_id`: The Keycloak token’s client_id to use for authentication. Requires `auth_url` and `token`. The default `client_id` is cloud-services to work with Red Hat SSO.

As well as defining these server options in the `ansible.cfg` file, you can also define them as environment variables.
The environment variable is in the form `ANSIBLE_GALAXY_SERVER_{{ id }}_{{ key }}` where `{{ id }}` is the upper
case form of the server identifier and `{{ key }}` is the key to define. For example I can define `token` for
`release_galaxy` by setting `ANSIBLE_GALAXY_SERVER_RELEASE_GALAXY_TOKEN=secret_token`.

For operations that use only one Galaxy server (for example, the `publish`, `info`, or `install` commands). the `ansible-galaxy collection` command uses the first entry in the
`server_list`, unless you pass in an explicit server with the `--server` argument.

> **Note:**
>
> `ansible-galaxy` can seek out dependencies on other configured Galaxy instances to support the use case where a collection can depend on a collection from another Galaxy instance.

## [Downloading collections](collections_using.md#id12)

To download a collection and its dependencies for an offline install, run `ansible-galaxy collection download`. This
downloads the collections specified and their dependencies to the specified folder and creates a `requirements.yml`
file which can be used to install those collections on a host without access to a Galaxy server. All the collections
are downloaded by default to the `./collections` folder.

Just like the `install` command, the collections are sourced based on the
[configured galaxy server config](collections_using.md#galaxy-server-config). Even if a collection to download was specified by a URL
or path to a tarball, the collection will be redownloaded from the configured Galaxy server.

Collections can be specified as one or multiple collections or with a `requirements.yml` file just like
`ansible-galaxy collection install`.

To download a single collection and its dependencies:

```bash
ansible-galaxy collection download my_namespace.my_collection
```

To download a single collection at a specific version:

```bash
ansible-galaxy collection download my_namespace.my_collection:1.0.0
```

To download multiple collections either specify multiple collections as command line arguments as shown above or use a
requirements file in the format documented with [Install multiple collections with a requirements file](collections_using.md#collection-requirements-file).

```bash
ansible-galaxy collection download -r requirements.yml
```

You can also download a source collection directory. The collection is built with the mandatory `galaxy.yml` file.

```bash
ansible-galaxy collection download /path/to/collection

ansible-galaxy collection download git+file:///path/to/collection/.git
```

You can download multiple source collections from a single namespace by providing the path to the namespace.

```
ns/
├── collection1/
│   ├── galaxy.yml
│   └── plugins/
└── collection2/
    ├── galaxy.yml
    └── plugins/
```

```bash
ansible-galaxy collection install /path/to/ns
```

All the collections are downloaded by default to the `./collections` folder but you can use `-p` or
`--download-path` to specify another path:

```bash
ansible-galaxy collection download my_namespace.my_collection -p ~/offline-collections
```

Once you have downloaded the collections, the folder contains the collections specified, their dependencies, and a
`requirements.yml` file. You can use this folder as is with `ansible-galaxy collection install` to install the
collections on a host without access to a Galaxy server.

```bash
# This must be run from the folder that contains the offline collections and requirements.yml file downloaded
# by the internet-connected host
cd ~/offline-collections
ansible-galaxy collection install -r requirements.yml
```

## [Listing collections](collections_using.md#id13)

To list installed collections, run `ansible-galaxy collection list`. This shows all of the installed collections found in the configured collections search paths. It will also show collections under development which contain a galaxy.yml file instead of a MANIFEST.json. The path where the collections are located are displayed as well as version information. If no version information is available, a `*` is displayed for the version number.

```shell
# /home/astark/.ansible/collections/ansible_collections
Collection                 Version
-------------------------- -------
cisco.aci                  0.0.5
cisco.mso                  0.0.4
sandwiches.ham             *
splunk.es                  0.0.5

# /usr/share/ansible/collections/ansible_collections
Collection        Version
----------------- -------
fortinet.fortios  1.0.6
pureport.pureport 0.0.8
sensu.sensu_go    1.3.0
```

Run with `-vvv` to display more detailed information.

To list a specific collection, pass a valid fully qualified collection name (FQCN) to the command `ansible-galaxy collection list`. All instances of the collection will be listed.

```shell
> ansible-galaxy collection list fortinet.fortios

# /home/astark/.ansible/collections/ansible_collections
Collection       Version
---------------- -------
fortinet.fortios 1.0.1

# /usr/share/ansible/collections/ansible_collections
Collection       Version
---------------- -------
fortinet.fortios 1.0.6
```

To search other paths for collections, use the `-p` option. Specify multiple search paths by separating them with a `:`. The list of paths specified on the command line will be added to the beginning of the configured collections search paths.

```shell
> ansible-galaxy collection list -p '/opt/ansible/collections:/etc/ansible/collections'

# /opt/ansible/collections/ansible_collections
Collection      Version
--------------- -------
sandwiches.club 1.7.2

# /etc/ansible/collections/ansible_collections
Collection     Version
-------------- -------
sandwiches.pbj 1.2.0

# /home/astark/.ansible/collections/ansible_collections
Collection                 Version
-------------------------- -------
cisco.aci                  0.0.5
cisco.mso                  0.0.4
fortinet.fortios           1.0.1
sandwiches.ham             *
splunk.es                  0.0.5

# /usr/share/ansible/collections/ansible_collections
Collection        Version
----------------- -------
fortinet.fortios  1.0.6
pureport.pureport 0.0.8
sensu.sensu_go    1.3.0
```

## [Verifying collections](collections_using.md#id14)

### [Verifying collections with `ansible-galaxy`](collections_using.md#id15)

Once installed, you can verify that the content of the installed collection matches the content of the collection on the server. This feature expects that the collection is installed in one of the configured collection paths and that the collection exists on one of the configured galaxy servers.

```bash
ansible-galaxy collection verify my_namespace.my_collection
```

The output of the `ansible-galaxy collection verify` command is quiet if it is successful. If a collection has been modified, the altered files are listed under the collection name.

```bash
ansible-galaxy collection verify my_namespace.my_collection
Collection my_namespace.my_collection contains modified content in the following files:
my_namespace.my_collection
    plugins/inventory/my_inventory.py
    plugins/modules/my_module.py
```

You can use the `-vvv` flag to display additional information, such as the version and path of the installed collection, the URL of the remote collection used for validation, and successful verification output.

```bash
ansible-galaxy collection verify my_namespace.my_collection -vvv
...
Verifying 'my_namespace.my_collection:1.0.0'.
Installed collection found at '/path/to/ansible_collections/my_namespace/my_collection/'
Remote collection found at 'https://galaxy.ansible.com/download/my_namespace-my_collection-1.0.0.tar.gz'
Successfully verified that checksums for 'my_namespace.my_collection:1.0.0' match the remote collection
```

If you have a pre-release or non-latest version of a collection installed you should include the specific version to verify. If the version is omitted, the installed collection is verified against the latest version available on the server.

```bash
ansible-galaxy collection verify my_namespace.my_collection:1.0.0
```

In addition to the `namespace.collection_name:version` format, you can provide the collections to verify in a `requirements.yml` file. Dependencies listed in `requirements.yml` are not included in the verify process and should be verified separately.

```bash
ansible-galaxy collection verify -r requirements.yml
```

Verifying against `tar.gz` files is not supported. If your `requirements.yml` contains paths to tar files or URLs for installation, you can use the `--ignore-errors` flag to ensure that all collections using the `namespace.name` format in the file are processed.

### [Verifying signed collections](collections_using.md#id16)

If a collection has been signed by a [distribution server](../reference_appendices/glossary.md#term-Distribution-server), the server will provide ASCII armored, detached signatures to verify the authenticity of the MANIFEST.json before using it to verify the collection’s contents. This option is not available on all distribution servers. See [Distributing collections](../dev_guide/developing_collections_distributing.md#distributing-collections) for a table listing which servers support collection signing. See [Installing collections with signature verification](collections_using.md#installing-signed-collections) for how to verify a signed collection when you install it.

To verify a signed installed collection:

```bash
ansible-galaxy collection verify my_namespace.my_collection  --keyring ~/.ansible/pubring.kbx
```

Use the `--signature` option to verify collection name(s) provided on the CLI with an additional signature. This option can be used multiple times to provide multiple signatures.

```bash
ansible-galaxy collection verify my_namespace.my_collection --signature https://examplehost.com/detached_signature.asc --signature file:///path/to/local/detached_signature.asc --keyring ~/.ansible/pubring.kbx
```

Optionally, you can verify a collection signature with a `requirements.yml` file.

```bash
ansible-galaxy collection verify -r requirements.yml --keyring ~/.ansible/pubring.kbx
```

When a collection is installed from a distribution server, the signatures provided by the server to verify the collection’s authenticity are saved alongside the installed collections. This data is used to verify the internal consistency of the collection without querying the distribution server again when the `--offline` option is provided.

```bash
ansible-galaxy collection verify my_namespace.my_collection --offline --keyring ~/.ansible/pubring.kbx
```

## [Using collections in a Playbook](collections_using.md#id17)

Once installed, you can reference a collection content by its fully qualified collection name (FQCN):

```yaml
- hosts: all
  tasks:
    - my_namespace.my_collection.mymodule:
        option1: value
```

This works for roles or any type of plugin distributed within the collection:

```yaml
- hosts: all
  tasks:
    - import_role:
        name: my_namespace.my_collection.role1

    - my_namespace.mycollection.mymodule:
        option1: value

    - debug:
        msg: '{{ lookup("my_namespace.my_collection.lookup1", 'param1')| my_namespace.my_collection.filter1 }}'
```

## [Simplifying module names with the `collections` keyword](collections_using.md#id18)

The `collections` keyword lets you define a list of collections that your role or playbook should search for unqualified module and action names. So you can use the `collections` keyword, then simply refer to modules and action plugins by their short-form names throughout that role or playbook.

> **Warning:**
>
> If your playbook uses both the `collections` keyword and one or more roles, the roles do not inherit the collections set by the playbook. This is one of the reasons we recommend you always use FQCN. See below for roles details.

### [Using `collections` in roles](collections_using.md#id19)

Within a role, you can control which collections Ansible searches for the tasks inside the role using the `collections` keyword in the role’s `meta/main.yml`. Ansible will use the collections list defined inside the role even if the playbook that calls the role defines different collections in a separate `collections` keyword entry. Roles defined inside a collection always implicitly search their own collection first, so you don’t need to use the `collections` keyword to access modules, actions, or other roles contained in the same collection.

```yaml
# myrole/meta/main.yml
collections:
  - my_namespace.first_collection
  - my_namespace.second_collection
  - other_namespace.other_collection
```

### [Using `collections` in playbooks](collections_using.md#id20)

In a playbook, you can control the collections Ansible searches for modules and action plugins to execute. However, any roles you call in your playbook define their own collections search order; they do not inherit the calling playbook’s settings. This is true even if the role does not define its own `collections` keyword.

```yaml
- hosts: all
  collections:
    - my_namespace.my_collection

  tasks:
    - import_role:
        name: role1

    - mymodule:
        option1: value

    - debug:
        msg: '{{ lookup("my_namespace.my_collection.lookup1", "param1")| my_namespace.my_collection.filter1 }}'
```

The `collections` keyword merely creates an ordered ‘search path’ for non-namespaced plugin and role references. It does not install content or otherwise change Ansible’s behavior around the loading of plugins or roles. Note that an FQCN is still required for non-action or module plugins (for example, lookups, filters, tests).

When using the `collections` keyword, it is not necessary to add in `ansible.builtin` as part of the search list. When left omitted, the following content is available by default:

1. Standard ansible modules and plugins available through `ansible-base`/`ansible-core`
2. Support for older 3rd party plugin paths

In general, it is preferable to use a module or plugin’s FQCN over the `collections` keyword and the short name for all content in `ansible-core`

## [Using a playbook from a collection](collections_using.md#id21)

New in version 2.11.

You can also distribute playbooks in your collection and invoke them using the same semantics you use for plugins:

```shell
ansible-playbook my_namespace.my_collection.playbook1 -i ./myinventory
```

From inside a playbook:

```yaml
- import_playbook: my_namespace.my_collection.playbookX
```

A few recommendations when creating such playbooks, `hosts:` should be generic or at least have a variable input.

```yaml
- hosts: all  # Use --limit or customized inventory to restrict hosts targeted

- hosts: localhost  # For things you want to restrict to the controller

- hosts: '{{target|default("webservers")}}'  # Assumes inventory provides a 'webservers' group, but can also use ``-e 'target=host1,host2'``
```

This will have an implied entry in the `collections:` keyword of `my_namespace.my_collection` just as with roles.

> **Note:**
>
> Playbook names, like other collection resources, have a restricted set of valid characters.
> Names can contain only lowercase alphanumeric characters, plus _ and must start with an alpha character. The dash `-` character is not valid for playbook names in collections.
> Playbooks whose names contain invalid characters are not addressable: this is a limitation of the Python importer that is used to load collection resources.

> **See also:**
>
> [Developing collections](../dev_guide/developing_collections.md#developing-collections)
> :   Develop or modify a collection.
>
> [Collection Galaxy metadata structure](../dev_guide/collections_galaxy_meta.md#collections-galaxy-meta)
> :   Understand the collections metadata structure.
>
> [Mailing List](https://groups.google.com/group/ansible-devel)
> :   The development mailing list
>
> [Real-time chat](../community/communication.md#communication-irc)
> :   How to join Ansible chat channels
>
> [Automation Hub](https://access.redhat.com/documentation/en-us/red_hat_ansible_automation_platform/)
> :   Learn how to use collections with Red Hat Automation Hub
