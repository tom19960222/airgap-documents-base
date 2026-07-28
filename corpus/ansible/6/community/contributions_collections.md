---
collection: ansible
version: "6"
title: "Ansible Collections Contributor Guide"
source_url: https://docs.ansible.com/projects/ansible/6/community/contributions_collections.html
fetched_at: 2026-07-27T16:39:24+00:00
---
# Ansible Collections Contributor Guide

- [The Ansible Collections Development Cycle](collection_development_process.md)
  - [Macro development: roadmaps, releases, and projects](collection_development_process.md#macro-development-roadmaps-releases-and-projects)
  - [Micro development: the lifecycle of a PR](collection_development_process.md#micro-development-the-lifecycle-of-a-pr)
  - [Making your PR merge-worthy](collection_development_process.md#making-your-pr-merge-worthy)
- [Requesting changes to a collection](reporting_collections.md)
  - [Reporting a bug](reporting_collections.md#reporting-a-bug)
  - [Requesting a feature](reporting_collections.md#requesting-a-feature)
- [Creating your first collection pull request](create_pr_quick_start.md)
  - [Prepare your environment](create_pr_quick_start.md#prepare-your-environment)
  - [Change the code](create_pr_quick_start.md#change-the-code)
  - [Fix the bug](create_pr_quick_start.md#fix-the-bug)
  - [Test your changes](create_pr_quick_start.md#test-your-changes)
  - [Submit a pull request](create_pr_quick_start.md#submit-a-pull-request)
- [Testing Collection Contributions](collection_contributors/test_index.md)
  - [How to test a collection PR](collection_contributors/collection_test_pr_locally.md)
  - [Add unit tests to a collection](collection_contributors/collection_unit_tests.md)
  - [Adding integration tests to a collection](collection_contributors/collection_integration_tests.md)
- [Review checklist for collection PRs](collection_contributors/collection_reviewing.md)
  - [Reviewing bug reports](collection_contributors/collection_reviewing.md#reviewing-bug-reports)
  - [Reviewing suggested changes](collection_contributors/collection_reviewing.md#reviewing-suggested-changes)
  - [Review tests in the PR](collection_contributors/collection_reviewing.md#review-tests-in-the-pr)
  - [Review for merge commits and breaking changes](collection_contributors/collection_reviewing.md#review-for-merge-commits-and-breaking-changes)
- [Guidelines for collection maintainers](maintainers.md)
  - [Maintainer responsibilities](maintainers_guidelines.md)
  - [Expanding the collection community](maintainers_guidelines.md#expanding-the-collection-community)
  - [Maintaining good collection documentation](maintainers_guidelines.md#maintaining-good-collection-documentation)
  - [Backporting and Ansible inclusion](maintainers_workflow.md)
  - [Stepping down as a collection maintainer](maintainers_workflow.md#stepping-down-as-a-collection-maintainer)
  - [Releasing collections](collection_contributors/collection_releasing.md)
- [Contributing to Ansible-maintained Collections](contributing_maintained_collections.md)
  - [Ansible-maintained collections](contributing_maintained_collections.md#ansible-maintained-collections)
  - [Deciding where your contribution belongs](contributing_maintained_collections.md#deciding-where-your-contribution-belongs)
  - [Requirements to merge your PR](contributing_maintained_collections.md#requirements-to-merge-your-pr)
- [Ansible Community Steering Committee](steering/steering_index.md)
  - [Steering Committee mission and responsibilities](steering/community_steering_committee.md)
  - [Steering Committee membership guidelines](steering/steering_committee_membership.md)
  - [Steering Committee past members](steering/steering_committee_past_members.md)
- [Contributing to the Ansible Documentation](documentation_contributions.md)
  - [Editing docs directly on GitHub](documentation_contributions.md#editing-docs-directly-on-github)
  - [Reviewing open PRs and issues](documentation_contributions.md#reviewing-open-prs-and-issues)
  - [Opening a new issue and/or PR](documentation_contributions.md#opening-a-new-issue-and-or-pr)
  - [Verifying your documentation PR](documentation_contributions.md#verifying-your-documentation-pr)
  - [Joining the documentation working group](documentation_contributions.md#joining-the-documentation-working-group)
- [Other Tools and Programs](other_tools_and_programs.md)
- [Popular editors](other_tools_and_programs.md#popular-editors)
  - [Atom](other_tools_and_programs.md#atom)
  - [Emacs](other_tools_and_programs.md#emacs)
  - [PyCharm](other_tools_and_programs.md#pycharm)
  - [Sublime](other_tools_and_programs.md#sublime)
  - [Visual studio code](other_tools_and_programs.md#visual-studio-code)
  - [vim](other_tools_and_programs.md#vim)
  - [JetBrains](other_tools_and_programs.md#jetbrains)
- [Development tools](other_tools_and_programs.md#development-tools)
  - [Finding related issues and PRs](other_tools_and_programs.md#finding-related-issues-and-prs)
- [Tools for validating playbooks](other_tools_and_programs.md#tools-for-validating-playbooks)
- [Other tools](other_tools_and_programs.md#other-tools)

If you have a specific Ansible interest or expertise (for example, VMware, Linode, and so on, consider joining a [working group](communication.md#working-group-list).

## Working with the Ansible collection repositories

- How can I find [editors, linters, and other tools](other_tools_and_programs.md#other-tools-and-programs) that will support my Ansible development efforts?
- Where can I find guidance on [coding in Ansible](../dev_guide/index.md#developer-guide)?
- How do I [create a collection](../dev_guide/developing_modules_in_groups.md#developing-modules-in-groups)?
- How do I [rebase my PR](../dev_guide/developing_rebasing.md#rebase-guide)?
- How do I learn about Ansible’s [testing (CI) process](../dev_guide/testing.md#developing-testing)?
- How do I [deprecate a module](../dev_guide/module_lifecycle.md#deprecating-modules)?
- See [Collection developer tutorials](https://www.ansible.com/products/ansible-community-training) for a quick introduction on how to develop and test your collection contributions.
