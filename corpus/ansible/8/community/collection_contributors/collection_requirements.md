---
collection: ansible
version: "8"
title: "Ansible community package collections requirements"
source_url: https://docs.ansible.com/projects/ansible/8/community/collection_contributors/collection_requirements.html
fetched_at: 2026-07-28T00:58:56+00:00
---
# Ansible community package collections requirements

This section describes the requirements for maintainers of Ansible community collections in the [ansible-collections](https://github.com/ansible-collections) repository or included in the Ansible community package.

- [Overview](collection_requirements.md#overview)
- [Feedback and communications](collection_requirements.md#feedback-and-communications)
- [Keeping informed](collection_requirements.md#keeping-informed)
- [Collection infrastructure](collection_requirements.md#collection-infrastructure)
- [Python Compatibility](collection_requirements.md#python-compatibility)

  - [Python Requirements](collection_requirements.md#python-requirements)

    - [Controller environment](collection_requirements.md#controller-environment)
    - [Other environment](collection_requirements.md#other-environment)
    - [Python documentation requirements](collection_requirements.md#python-documentation-requirements)
- [Standards for developing module and plugin utilities](collection_requirements.md#standards-for-developing-module-and-plugin-utilities)
- [Repository structure requirements](collection_requirements.md#repository-structure-requirements)

  - [galaxy.yml](collection_requirements.md#galaxy-yml)
  - [README.md](collection_requirements.md#readme-md)
  - [meta/runtime.yml](collection_requirements.md#meta-runtime-yml)
  - [Modules & Plugins](collection_requirements.md#modules-plugins)
  - [Other directories](collection_requirements.md#other-directories)

    - [Documentation requirements](collection_requirements.md#documentation-requirements)
- [Contributor Workflow](collection_requirements.md#contributor-workflow)

  - [Changelogs](collection_requirements.md#changelogs)

    - [Versioning and deprecation](collection_requirements.md#versioning-and-deprecation)
- [Naming](collection_requirements.md#naming)

  - [Collection naming](collection_requirements.md#collection-naming)
  - [Module naming](collection_requirements.md#module-naming)
- [Collection licensing requirements](collection_requirements.md#collection-licensing-requirements)
- [Contributor License Agreements](collection_requirements.md#contributor-license-agreements)
- [Repository management](collection_requirements.md#repository-management)

  - [Branch name and configuration](collection_requirements.md#branch-name-and-configuration)
- [CI Testing](collection_requirements.md#ci-testing)
- [Collections and Working Groups](collection_requirements.md#collections-and-working-groups)
- [When moving modules between collections](collection_requirements.md#when-moving-modules-between-collections)
- [Development conventions](collection_requirements.md#development-conventions)
- [Collection Dependencies](collection_requirements.md#collection-dependencies)

  - [Examples](collection_requirements.md#examples)
- [Requirements for collections to be included in the Ansible Package](collection_requirements.md#requirements-for-collections-to-be-included-in-the-ansible-package)
- [Other requirements](collection_requirements.md#other-requirements)

## [Overview](collection_requirements.md#id8)

This section provides help, advice, and guidance on making sure your collections are correct and ready for inclusion in the Ansible community package.

> **Note:**
>
> [Inclusion of a new collection](https://github.com/ansible-collections/ansible-inclusion) in the Ansible package is ultimately at the discretion of the [Ansible Community Steering Committee](../steering/steering_index.md#community-steering-committee). Every rejected candidate will get feedback. Differences of opinion should be taken to a dedicated [Community Topic](https://github.com/ansible-community/community-topics/issues) for discussion and a final vote.

## [Feedback and communications](collection_requirements.md#id9)

As with any project it is very important that we get feedback from users, contributors, and maintainers. You can get feedback and help as follows:

- Discussing in the [#community:ansible.com Matrix room](https://matrix.to/#/#community:ansible.com), which is bridged with the `#ansible-community` channel on Libera.Chat IRC. See the [Ansible Communication Guide](../communication.md#communication-irc) for details.
- Discussing in the [Community Working Group meeting](https://github.com/ansible/community/blob/main/meetings/README.md#wednesdays).
- Creating [GitHub Issues](https://github.com/ansible-collections/overview/issues) in the `ansible-collections` repository.

## [Keeping informed](collection_requirements.md#id10)

You should subscribe to:

- The [news-for-maintainers repository](https://github.com/ansible-collections/news-for-maintainers) to track changes that collection maintainers should be aware of. Subscribe only to issues if you want less traffic.
- The [Bullhorn](https://github.com/ansible/community/wiki/News#the-bullhorn) Ansible contributor newsletter.

## [Collection infrastructure](collection_requirements.md#id11)

The following guidelines describe the required structure for your collection:

- MUST have a publicly available issue tracker that does not require a paid level of service to create an account or view issues.
- MUST have a Code of Conduct (CoC).

  - The collection’s CoC MUST be compatible with the [Community Code of Conduct](../code_of_conduct.md#code-of-conduct).
  - The collections SHOULD consider using the Ansible CoC if they do not have a CoC that they consider better.
  - The [Diversity and Inclusion working group](../communication.md#working-group-list) may evaluate all CoCs and object to a collection’s inclusion based on the CoCs contents.
  - The CoC MUST be linked from the `README.md` file, or MUST be present or linked from the `CODE_OF_CONDUCT.md` file in the collection root.
- MUST be published to [Ansible Galaxy](https://galaxy.ansible.com).
- SHOULD NOT contain any large objects (binaries) comparatively to the current Galaxy tarball size limit of 20 MB, For example, do not include package installers for testing purposes.
- SHOULD NOT contain any unnecessary files such as temporary files.
- MUST only contain objects that follow the [Licensing rules](collection_requirements.md#coll-licensing-req).

## [Python Compatibility](collection_requirements.md#id12)

A collection MUST be developed and tested using the below Python requirements as Ansible supports a wide variety of machines.

The collection should adhere to the tips at ansible-and-python-3.

### [Python Requirements](collection_requirements.md#id13)

Python requirements for a collection vary between **controller environment** and **other environment**. On the controller-environment, the Python versions required may be higher than what is required on the other-environment. While developing a collection, you need to understand the definitions of both the controller-environment and other-environment to help you choose Python versions accordingly:

- controller environment: The plugins/modules always run in the same environment (Python interpreter, venv, host, and so on) as ansible-core itself.
- other environment: It is possible, even if uncommon in practice, for the plugins/modules to run in a different environment than ansible-core itself.

One example scenario where the “even if” clause comes into play is when using cloud modules. These modules mostly run on the controller node but in some environments, the controller might run on one machine inside a demilitarized zone which cannot directly access the cloud machines. The user has to have the cloud modules run on a bastion host/jump server which has access to the cloud machines.

An **eligible controller Python version** for a collection is a Python version that is supported on the controller side by at least one ansible-core version that the collection supports. Similarly, an **eligible target Python version** for a collection is a Python version that is supported on the target side by at least one ansible-core version that the collection supports. The eligible controller and target Python versions can be determined from the [ansible-core support matrix](../../reference_appendices/release_and_maintenance.md#ansible-core-support-matrix) and from the `requires_ansible` value in `meta/runtime.yml` in the collection.

#### [Controller environment](collection_requirements.md#id14)

Collections MUST support all eligible controller Python versions in the controller environment, unless required libraries do not support these Python versions. The [Steering Committee](../steering/community_steering_committee.md#steering-responsibilities) can grant other exceptions on a case-by-case basis.

The collection MUST document all eligible controller Python versions that are not supported in the controller environment. See [Python documentation requirements](collection_requirements.md#coll-python-docs-req) for details.

#### [Other environment](collection_requirements.md#id15)

Collections MUST support all eligible controller Python versions in the other environment, unless required libraries do not support these Python versions. The [Steering Committee](../steering/community_steering_committee.md#steering-responsibilities) can grant other exceptions on a case-by-case basis.

Collections SHOULD support all eligible target Python versions in the other environment.

The collection MUST document all eligible target Python versions that are not supported in the other environment. See [Python documentation requirements](collection_requirements.md#coll-python-docs-req) for details.

> **Note:**
>
> Note that dropping support for a Python version for an existing module/plugin is a breaking change, and thus requires a major release. A collection MUST announce dropping support for Python versions in their changelog, if possible in advance (for example, in previous versions before support is dropped).

#### [Python documentation requirements](collection_requirements.md#id16)

- If everything in your collection supports all eligible controller/target Python versions, you do not need to document supported Python versions.
- If your collection does not support those Python versions, you MUST document which versions it supports in the README.
- If most of your collection supports the same Python versions as ansible-core, but some modules and plugins do not, you MUST include the supported Python versions in the documentation for those modules and plugins.

For example, if your collection supports Ansible 2.9 to ansible-core 2.13, the Python versions supported for modules are 2.6, 2.7, and 3.5 and newer (until at least 3.10), while the Python versions supported for plugins are 2.7 and 3.5 and newer (until at least 3.10). So if the modules in your collection do not support Python 2.6, you have to document this in the README, for example `The content in this collection supports Python 2.7, Python 3.5 and newer.`.

## [Standards for developing module and plugin utilities](collection_requirements.md#id17)

- `module_utils` and `plugin_utils` can be marked for only internal use in the collection, but they MUST document this and MUST use a leading underscore for filenames.
- It is a breaking change when you make an existing `module_utils` private and in that case the collection requires a major version bump.
- Below are some recommendations for `module_utils` documentation:

  - No docstring: everything we recommend for `other-environment` is supported.
  - The docstring `'Python versions supported: same as for controller-environment'`: everything we recommend for `controller-environment` is supported.
  - The docstring with specific versions otherwise: `'Python versions supported: '`.

## [Repository structure requirements](collection_requirements.md#id18)

### [galaxy.yml](collection_requirements.md#id19)

- The `tags` field MUST be set.
- Collection dependencies must meet a set of rules. See the section on Collection Dependencies <collection_dependencies_> for details.
- The `ansible` package MUST NOT depend on collections not shipped in the package.
- If you plan to split up your collection, the new collection MUST be approved for inclusion before the smaller collections replace the larger in Ansible.
- If you plan to add other collections as dependencies, they MUST run through the formal application process.

### [README.md](collection_requirements.md#id20)

Your collection repository MUST have a `README.md` in the root of the collection, see [collection_template/README.md](https://github.com/ansible-collections/collection_template/blob/main/README.md) for an example.

### [meta/runtime.yml](collection_requirements.md#id21)

Example: [meta/runtime.yml](https://github.com/ansible-collections/collection_template/blob/main/meta/runtime.yml)

- The `meta/runtime.yml` MUST define the minimum version of Ansible which this collection works with.

  - If the collection works with Ansible 2.9, then this should be set to >=2.9.10
  - It is usually better to avoid adding <2.11 as a restriction, since this for example makes it impossible to use the collection with the current ansible-base devel branch (which has version 2.11.0.dev0)

### [Modules & Plugins](collection_requirements.md#id22)

- Collections MUST only use the directories specified below in the `plugins/` directory and
  only for the purposes listed:

  Those recognized by ansible-core:
  :   `doc_fragments`, `modules`, `module_utils`, `terminal`, and those listed in [Working with plugins](../../plugins/plugins.md#working-with-plugins). This list can be verified by looking at the last element of the package argument of each `*_loader` in <https://github.com/ansible/ansible/blob/devel/lib/ansible/plugins/loader.py#L1126>

  plugin_utils:
  :   For shared code which is only used controller-side, not in modules.

  sub_plugins:
  :   For other plugins which are managed by plugins inside of collections instead of ansible-core. We use a subfolder so there aren’t conflicts when ansible-core adds new plugin types.

  The core team (which maintains ansible-core) has committed not to use these directories for
  anything which would conflict with the uses specified here.

### [Other directories](collection_requirements.md#id23)

Collections MUST not use files outside `meta/`, `plugins/`, `roles/` and `playbooks/` in any plugin, role, or playbook that can be called by FQCN, used from other collections, or used from user playbooks and roles. A collection must work if every file or directory is deleted from the installed collection except those four directories and their contents.

Internal plugins, roles and playbooks (artifacts used only in testing, or only to release the collection, or only for some other internal purpose and not used externally) are exempt from this rule and may rely on files in other directories.

#### [Documentation requirements](collection_requirements.md#id24)

All modules and plugins MUST:

- Include a DOCUMENTATION block.
- Include an EXAMPLES block (except where not relevant for the plugin type).
- Use FQCNs when referring to modules, plugins and documentation fragments inside and outside the collection (including `ansible.builtin` for the listed entities from ansible-core.

When using `version_added` in the documentation:

- Declare the version of the collection in which the options were added – NOT the version of Ansible.
- If you for some reason really have to specify version numbers of Ansible or of another collection, you also have to provide `version_added_collection: collection_name`. We strongly recommend to NOT do this.
- Include `version_added` when you add new content (modules, plugins, options) to an existing collection. The values are shown in the documentation, and can be useful, but you do not need to add `version_added` to every option, module, and plugin when creating a new collection.

Other items:

- The `CONTRIBUTING.md` (or `README.md`) file MUST state what types of contributions (pull requests, feature requests, and so on) are accepted and any relevant contributor guidance. Issues (bugs and feature request) reports must always be accepted.
- Collections are encouraged to use z:ref:links and formatting macros <linking-and-other-format-macros-within-module-documentation>
- Including a RETURN block for modules is strongly encouraged but not required.

## [Contributor Workflow](collection_requirements.md#id25)

### [Changelogs](collection_requirements.md#id26)

Collections are required to include a changelog. To give a consistent feel for changelogs across collections and ensure changelogs exist for collections included in the `ansible` package we suggest you use [antsibull-changelog](https://github.com/ansible-community/antsibull-changelog) to maintain and generate this but other options exist. Preferred (in descending order):

1. Use antsibull-changelog (preferred).
2. Provide `changelogs/changelog.yaml` in the [correct format](https://github.com/ansible-community/antsibull-changelog/blob/main/docs/changelog.yaml-format.md). (You can use `antsibull-lint changelog-yaml /path/to/changelog.yaml` to validate the format.)
3. Provide a link to the changelog file (self-hosted) (not recommended).

Note that the porting guide is compiled from `changelogs/changelog.yaml` (sections `breaking_changes`, `major_changes`, `deprecated_features`, `removed_features`). So if you use option 3, you will not be able to add something to the porting guide.

#### [Versioning and deprecation](collection_requirements.md#id27)

- Collections MUST adhere to [semantic versioning](https://semver.org/).
- To preserve backward compatibility for users, every Ansible minor version series (x.Y.z) will keep the major version of a collection constant. If ansible 3.0.0 includes `community.general` 2.2.0, then each 3.Y.z (3.1.z, 3.2.z, and so on) release will include the latest `community.general` 2.y.z release available at build time. Ansible 3.y.z will **never** include a `community.general` 3.y.z release, even if it is available. Major collection version changes will be included in the next Ansible major release (4.0.0 in this example).
- Therefore, ensure that the current major release of your collection included in 3.0.0 receives at least bugfixes as long as new 3.Y.Z releases are produced.
- Since new minor releases are included, you can include new features, modules and plugins. You must make sure that you do not break backwards compatibility! (See [semantic versioning](https://semver.org/).) This means in particular:

  - You can fix bugs in patch releases, but not add new features or deprecate things.
  - You can add new features and deprecate things in minor releases, but not remove things or change behavior of existing features.
  - You can only remove things or make breaking changes in major releases.
- We recommend that you ensure that if a deprecation is added in a collection version that is included in Ansible 3.y.z, the removal itself will only happen in a collection version included in Ansible 5.0.0 or later, but not in a collection version included in Ansible 4.0.0.
- Content moved from ansible/ansible that was scheduled for removal in 2.11 or later MUST NOT be removed in the current major release available when ansible 2.10.0 is released. Otherwise it would already be removed in 2.10, unexpectedly for users! Deprecation cycles can be shortened (since they are now uncoupled from ansible or ansible-base versions), but existing ones must not be unexpectedly terminated.
- We recommend you announce your policy of releasing, versioning and deprecation to contributors and users in some way. For an example of how to do this, see [the announcement in community.general](https://github.com/ansible-collections/community.general/issues/582). You could also do this in the README.

## [Naming](collection_requirements.md#id28)

### [Collection naming](collection_requirements.md#id29)

For collections under ansible-collections the repository SHOULD be named `NAMESPACE.COLLECTION`.

To create a new collection and corresponding repository, first, a new namespace in Galaxy has to be created by submitting [Request a namespace](https://github.com/ansible/galaxy/issues/new/choose).

[Namespace limitations](https://galaxy.ansible.com/docs/contributing/namespaces.html#galaxy-namespace-limitations) lists requirements for namespaces in Galaxy.

For collections created for working with a particular entity, they should contain the entity name, for example `community.mysql`.

For corporate maintained collections, the repository can be named `COMPANY_NAME.PRODUCT_NAME`, for example `ibm.db2`.

We should avoid FQCN / repository names:

- which are unnecessary long: try to make it compact but clear.
- contain the same words / collocations in `NAMESPACE` and `COLLECTION` parts, for example `my_system.my_system`.

If your collection is planned to be certified on **Red Hat Automation Hub**, please consult with Red Hat Partner Engineering through `ansiblepartners@redhat.com` to ensure collection naming compatibility between the community collection on **Galaxy**.

### [Module naming](collection_requirements.md#id30)

Modules that only gather information MUST be named `<something>_info`. Modules that return `ansible_facts` are named `<something>_facts` and do not return non-facts.
For more information, refer to the Developing modules guidelines.

## [Collection licensing requirements](collection_requirements.md#id31)

> **Note:**
>
> The guidelines below are more restrictive than strictly necessary. We will try to add a larger list of acceptable licenses once we have approval from Red Hat Legal.

There are four types of content in collections which licensing has to address in different
ways:

modules:
:   must be licensed with a free software license that is compatible with the
    [GPL-3.0-or-later](https://www.gnu.org/licenses/gpl-3.0-standalone.html)

module_utils:
:   must be licensed with a free software license that is compatible with the
    [GPL-3.0-or-later](https://www.gnu.org/licenses/gpl-3.0-standalone.html). Ansible
    itself typically uses the [BSD-2-clause](https://opensource.org/licenses/BSD-2-Clause) license to make it possible for
    third-party modules which are licensed incompatibly with the GPLv3 to use them.
    Please consider this use case when licensing your own `module_utils`.

All other code in `plugins/`:
:   All other code in `plugins/` must be under the [GPL-3.0-or-later](https://www.gnu.org/licenses/gpl-3.0-standalone.html). These plugins
    are run inside of the Ansible controller process which is licensed under
    the `GPL-3.0-or-later` and often must import code from the controller.
    For these reasons, `GPL-3.0-or-later` must be used.

All other code:
:   Code outside `plugins/` may be licensed under another free software license that is compatible
    with the [GPL-3.0-or-later](https://www.gnu.org/licenses/gpl-3.0-standalone.html),
    provided that such code does not import any other code that is licensed under
    the `GPL-3.0-or-later`. If the file does import other `GPL-3.0-or-later` code,
    then it must similarly be licensed under `GPL-3.0-or-later`. Note that this applies in
    particular to unit tests; these often import code from ansible-core, plugins, module utils,
    or modules, and such code is often licensed under `GPL-3.0-or-later`.

Non code content:
:   At the moment, these must also be under the [GPL-3.0-or-later](https://www.gnu.org/licenses/gpl-3.0-standalone.html).

Use [this table of licenses from the Fedora Project](https://fedoraproject.org/wiki/Licensing:Main#Software_License_List) to find which licenses are
compatible with the GPLv3+. The license must be considered open source on both the Fedora License
table and the [Debian Free Software Guidelines](https://wiki.debian.org/DFSGLicenses) to be
allowed.

These guidelines are the policy for inclusion in the Ansible package and are in addition to any
licensing and legal concerns that may otherwise affect your code.

## [Contributor License Agreements](collection_requirements.md#id32)

Collections MUST NOT require community contributors to sign any type of
contributor license agreement (CLA) other than the
[Developer Certificate of Origin](https://developercertificate.org/)
or similar agreements that only require confirming the provenance of contributions.
This requirement seeks to preserve the community’s ownership over its contributions,
prevent unwelcome licensing changes that can occur when one entity
owns the copyrights for an entire project,
and lower barriers to contribution.

## [Repository management](collection_requirements.md#id33)

Every collection MUST have a public git repository. Releases of the collection MUST be tagged in said repository. This means that releases MUST be `git tag`ed and that the tag name MUST exactly match the Galaxy version number. Tag names MAY have a `v` prefix, but a collection’s tag names MUST have a consistent format from release to release.

Additionally, collection artifacts released to Galaxy MUST be built from the sources that are tagged in the collection’s git repository as that release. Any changes made during the build process MUST be clearly documented so the collection artifact can be reproduced.

We are open to allowing other SCM software once our tooling supports them.

### [Branch name and configuration](collection_requirements.md#id34)

This subsection is **only** for repositories under [ansible-collections](https://github.com/ansible-collections)! Other collection repositories can also follow these guidelines, but do not have to.

All new repositories MUST have `main` as the default branch.

Existing repositories SHOULD be converted to use `main`.

Repository Protections:

- Allow merge commits: disallowed

Branch protections MUST be enforced:

- Require linear history
- Include administrators

## [CI Testing](collection_requirements.md#id35)

> **Note:**
>
> You can copy the free-to-use [GitHub action workflow file](https://github.com/ansible-collections/collection_template/blob/main/.github/workflows/ansible-test.yml) from the [Collection Template repository](https://github.com/ansible-collections/collection_template/) to the .github/workflows directory in your collection to set up testing through GitHub actions. The workflow covers all the requirements below.

- You MUST run the `ansible-test sanity` command from the [latest stable ansible-base/ansible-core branch](https://github.com/ansible/ansible/branches/all?query=stable-).

  - Collections MUST run an equivalent of the `ansible-test sanity --docker` command.
  - If they do not use `--docker`, they must make sure that all tests run, in particular the compile and import tests (which should run for all supported Python versions).
  - Collections can choose to skip certain Python versions that they explicitly do not support; this needs to be documented in `README.md` and in every module and plugin (hint: use a docs fragment). However we strongly recommend you follow the Ansible Python Compatibility section for more details.
- You SHOULD suggest to *additionally* run `ansible-test sanity` from the ansible/ansible `devel` branch so that you find out about new linting requirements earlier.
- The sanity tests MUST pass.

  - Adding some entries to the `test/sanity/ignore*.txt` file is an allowed method of getting them to pass, except cases listed below.
  - You SHOULD not have ignored test entries. A reviewer can manually evaluate and approve your collection if they deem an ignored entry to be valid.
  - You MUST not ignore the following validations. They must be fixed before approval:
    :   - `validate-modules:doc-choices-do-not-match-spec`
        - `validate-modules:doc-default-does-not-match-spec`
        - `validate-modules:doc-missing-type`
        - `validate-modules:doc-required-mismatch`
        - `validate-modules:mutually_exclusive-unknown`
        - `validate-modules:no-log-needed` (use `no_log=False` in the argument spec to flag false positives!)
        - `validate-modules:nonexistent-parameter-documented`
        - `validate-modules:parameter-list-no-elements`
        - `validate-modules:parameter-type-not-in-doc`
        - `validate-modules:undocumented-parameter`
  - All entries in ignores.txt MUST have a justification in a comment in the ignore.txt file for each entry. For example `plugins/modules/docker_container.py use-argspec-type-path # uses colon-separated paths, can't use type=path`.
  - Reviewers can block acceptance of a new collection if they don’t agree with the ignores.txt entries.
- You MUST run CI against each of the “major versions” (2.10, 2.11, 2.12, etc) of `ansible-base`/`ansible-core` that the collection supports. (Usually the `HEAD` of the stable-xxx branches.)
- All CI tests MUST run against every pull request and SHOULD pass before merge.
- At least sanity tests MUST run against a commit that releases the collection; if they do not pass, the collection will NOT be released.

  - If the collection has integration/unit tests, they SHOULD run too; if they do not pass, the errors SHOULD be analyzed to decide whether they should block the release or not.
- All CI tests MUST run regularly (nightly, or at least once per week) to ensure that repositories without regular commits are tested against the latest version of ansible-test from each ansible-base/ansible-core version tested. The results from the regular CI runs MUST be checked regularly.

All of the above can be achieved by using the [GitHub Action template](https://github.com/ansible-collections/collection_template/tree/main/.github/workflows).

To learn how to add tests to your collection, see:

- [Adding integration tests to a collection](collection_integration_tests.md#collection-integration-tests)
- [Add unit tests to a collection](collection_unit_tests.md#collection-unit-tests)

## [Collections and Working Groups](collection_requirements.md#id36)

The collections have:

- Working group page(s) on a corresponding wiki if needed. Makes sense if there is a group of modules for working with one common entity, for example postgresql, zabbix, grafana, and so on.
- Issue for agenda (or pinboard if there are not regular meetings) as a pinned issue in the repository.

## [When moving modules between collections](collection_requirements.md#id37)

All related entities must be moved/copied including:

- Related plugins and module_utils files (when moving, be sure it is not used by other modules, otherwise copy).
- CI and unit tests.
- Corresponding documentation fragments from `plugins/doc_fragments`.

Also:

- Change `M()`, examples, `seealso`, `extended_documentation_fragments` to use actual FQCNs in moved content and in other collections that have references to the content.
- Move all related issues, pull requests, and wiki pages.
- Look through `docs/docsite` directory of [ansible-base GitHub repository](https://github.com/ansible/ansible) (for example, using the `grep` command-line utility) to check if there are examples using the moved modules and plugins to update their FQCNs.

See Migrating content to a different collection for complete details.

## [Development conventions](collection_requirements.md#id38)

Besides all the requirements listed in the [Conventions, tips, and pitfalls](../../dev_guide/developing_modules_best_practices.md#module-dev-conventions), be sure:

- Your modules satisfy the concept of idempotency: if a module repeatedly runs with the same set of inputs, it will not make any changes on the system.
- Your modules do not query information using special `state` option values like `get`, `list`, `query`, or `info` -
  create new `_info` or `_facts` modules instead (for more information, refer to the Developing modules guidelines).
- `check_mode` is supported in all `*_info` and `*_facts` modules (for more information, refer to the Development conventions).

## [Collection Dependencies](collection_requirements.md#id39)

**Notation:** if foo.bar has a dependency on baz.bam, we say that baz.bam is the collection *depended on*, and foo.bar is the *dependent collection*.

- Collection dependencies must have a lower bound on the version which is at least 1.0.0.

  - This means that all collection dependencies have to specify lower bounds on the versions, and these lower bounds should be stable releases, and not versions of the form 0.x.y.
  - When creating new collections where collection dependencies are also under development, you need to watch out since Galaxy checks whether dependencies exist in the required versions:

    1. Assume that `foo.bar` depends on `foo.baz`.
    2. First release `foo.baz` as 1.0.0.
    3. Then modify `foo.bar`’s `galaxy.yml` to specify `'>=1.0.0'` for `foo.baz`.
    4. Finally release `foo.bar` as 1.0.0.
- The dependencies between collections included in Ansible must be valid. If a dependency is violated, the involved collections must be pinned so that all dependencies are valid again. This means that the version numbers from the previous release are kept or only partially incremented so that the resulting set of versions has no invalid dependencies.
- If a collection has a too strict dependency for a longer time, and forces another collection depended on to be held back, that collection will be removed from the next major Ansible release. What “longer time” means depends on when the next Ansible major release happens. If a dependent collection prevents a new major version of a collection it depends on to be included in the next major Ansible release, the dependent collection will be removed from that major release to avoid blocking the collection being depended on.
- We strongly suggest that collections also test against the `main` branches of their dependencies to ensure that incompatibilities with future releases of these are detected as early as possible and can be resolved in time to avoid such problems. Collections depending on other collections must understand that they bear the risk of being removed when they do not ensure compatibility with the latest releases of their dependencies.
- Collections included in Ansible must not depend on other collections except if they satisfy one of the following cases:

  1. They have a loose dependency on one (or more) major versions of other collections included in Ansible. For example, `ansible.netcommon: >=1.0.0`, or `ansible.netcommon: >=2.0.0, <3.0.0`. In case the collection depended on releases a new major version outside of this version range that will be included in the next major Ansible release, the dependent collection will be removed from the next major Ansible release. The cut-off date for this is feature freeze.
  2. They are explicitly being allowed to do so by the Steering Committee.

### [Examples](collection_requirements.md#id40)

1. `community.foo 1.2.0` has a dependency on `community.bar >= 1.0.0, < 1.3.0`.

   - Now `community.bar` creates a new release `1.3.0`. When `community.foo` does not create a new release with a relaxed dependency, we have to include `community.bar 1.2.x` in the next Ansible release despite `1.3.0` being available.
   - If `community.foo` does not relax its dependency on `community.bar` for some time, `community.foo` will be removed from the next Ansible major release.
   - Unfortunately `community.bar` has to stay at `1.2.x` until either `community.foo` is removed (in the next major release), or loosens its requirements so that newer `community.bar 1.3.z` releases can be included.
2. `community.foonetwork` depends on `ansible.netcommon >= 2.0.0, <3.0.0`.

   - `ansible.netcommon 4.0.0` is released during this major Ansible release cycle.
   - `community.foonetwork` either releases a new version before feature freeze of the next major Ansible release that allows depending on all `ansible.netcommon 4.x.y` releases, or it will be removed from the next major Ansible release.

## [Requirements for collections to be included in the Ansible Package](collection_requirements.md#id41)

To be included in the ansible package, collections must meet the following criteria:

- [Development conventions](../../dev_guide/developing_modules_best_practices.md#module-dev-conventions).
- [Collection requirements](https://docs.ansible.com/ansible/devel/community/collection_contributors/collection_requirements.html) (this document).

  - The [Collection Inclusion Criteria Checklist](https://github.com/ansible-collections/overview/blob/main/collection_checklist.md) covers most of the criteria from this document.
- [Ansible documentation format](../../dev_guide/developing_modules_documenting.md#module-documenting) and the style guide.
- To pass the Ansible sanity tests.
- To have unit according to the corresponding sections of this document.

## [Other requirements](collection_requirements.md#id42)

- After content is moved out of another currently included collection such as `community.general` or `community.network` OR a new collection satisfies all the requirements, add the collection to the `ansible.in` file in a corresponding directory of the [ansible-build-data repository](https://github.com/ansible-community/ansible-build-data/).
