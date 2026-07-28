---
collection: ansible
version: "6"
title: "changelog"
source_url: https://docs.ansible.com/projects/ansible/6/dev_guide/testing/sanity/changelog.html
fetched_at: 2026-07-27T16:42:23+00:00
---
# changelog

Basic linting of changelog fragments with [antsibull-changelog lint](https://pypi.org/project/antsibull-changelog/).

One or more of the following sections are required:

- major_changes
- minor_changes
- breaking_changes
- deprecated_features
- removed_features
- security_fixes
- bugfixes
- known_issues

New modules and plugins must not be included in changelog fragments.

See [Generating changelogs and porting guide entries in a collection](../../developing_collections_changelogs.md#collection-changelogs) for details.
