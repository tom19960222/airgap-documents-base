---
collection: ansible
version: "8"
title: "ansible-core Contributors Guide"
source_url: https://docs.ansible.com/projects/ansible/8/community/contributions.html
fetched_at: 2026-07-28T00:57:47+00:00
---
# ansible-core Contributors Guide

- [Reporting bugs and requesting features](reporting_bugs_and_features.md)
  - [Reporting a bug](reporting_bugs_and_features.md#reporting-a-bug)
  - [Requesting a feature](reporting_bugs_and_features.md#requesting-a-feature)
- [Contributing to the Ansible Documentation](documentation_contributions.md)
  - [Editing docs directly on GitHub](documentation_contributions.md#editing-docs-directly-on-github)
  - [Reviewing or solving open issues](documentation_contributions.md#reviewing-or-solving-open-issues)
  - [Reviewing open PRs](documentation_contributions.md#reviewing-open-prs)
  - [Opening a new issue and/or PR](documentation_contributions.md#opening-a-new-issue-and-or-pr)
  - [Verifying your documentation PR](documentation_contributions.md#verifying-your-documentation-pr)
  - [Joining the documentation working group](documentation_contributions.md#joining-the-documentation-working-group)
- [The Ansible Development Cycle](development_process.md)
  - [Macro development: `ansible-core` roadmaps, releases, and projects](development_process.md#macro-development-ansible-core-roadmaps-releases-and-projects)
  - [Micro development: the lifecycle of a PR](development_process.md#micro-development-the-lifecycle-of-a-pr)
  - [Making your PR merge-worthy](development_process.md#making-your-pr-merge-worthy)
  - [Backporting merged PRs in `ansible-core`](development_process.md#backporting-merged-prs-in-ansible-core)
- [Other Tools and Programs](other_tools_and_programs.md)
  - [Popular editors](other_tools_and_programs.md#popular-editors)
  - [Development tools](other_tools_and_programs.md#development-tools)
  - [Tools for validating playbooks](other_tools_and_programs.md#tools-for-validating-playbooks)
  - [Other tools](other_tools_and_programs.md#other-tools)

If you have a specific Ansible interest or expertise (for example, VMware, Linode, and so on, consider joining a [working group](communication.md#working-group-list).

## Working with the Ansible repo

- I want to make my first code changes to a collection or to `ansible-core`. How do I [set up my Python development environment](../dev_guide/developing_modules_general.md#environment-setup)?
- I would like to get more efficient as a developer. How can I find [editors, linters, and other tools](other_tools_and_programs.md#other-tools-and-programs) that will support my Ansible development efforts?
- I want my code to meet Ansible’s guidelines. Where can I find guidance on [coding in Ansible](../dev_guide/index.md#developer-guide)?
- I would like to connect Ansible to a new API or other resource. How do I [create a collection](../dev_guide/developing_modules_in_groups.md#developing-modules-in-groups)?
- My pull request is marked `needs_rebase`. How do I [rebase my PR](../dev_guide/developing_rebasing.md#rebase-guide)?
- I am using an older version of Ansible and want a bug fixed in my version that has already been fixed on the `devel` branch. How do I [backport a bugfix PR](development_process.md#backport-process)?
- I have an open pull request with a failing test. How do I learn about Ansible’s [testing (CI) process](../dev_guide/testing.md#developing-testing)?
- I am ready to step up as a collection maintainer. What are the [guidelines for maintainers](maintainers.md#maintainers)?
- A module in a collection I maintain is obsolete. How do I [deprecate a module](../dev_guide/module_lifecycle.md#deprecating-modules)?
