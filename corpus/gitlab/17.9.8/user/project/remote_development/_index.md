---
collection: gitlab
version: "17.9.8"
title: "Remote development"
source_url: https://gitlab.com/gitlab-org/gitlab/-/blob/v17.9.8-ee/doc/user/project/remote_development/_index.md
fetched_at: 2025-05-07T10:05:15Z
---
- Tier: Free, Premium, Ultimate
- Offering: GitLab.com, GitLab Self-Managed, GitLab Dedicated

Remote development is a set of features you can use to make code changes
without having to install any dependencies or clone any repositories locally.
These features include:

- [Web IDE](#web-ide)
- [Workspaces](#workspaces)

## Web IDE

You can use the [Web IDE](../web_ide/_index.md) to make, commit, and push changes to a project directly from your web browser.
This way, you can update any project without having to install any dependencies or clone any repositories locally.

The Web IDE, however, lacks a native runtime environment where you could compile code, run tests, or generate real-time feedback.

## Workspaces

- Tier: Premium, Ultimate

You can use [workspaces](../../workspace/_index.md) to create a fully featured development environment directly from GitLab.
This environment runs on a remote server and provides you with a complete IDE experience
without having to install any dependencies or clone repositories locally.

With workspaces, you can:

- Create a new development environment.
- Access a fully featured IDE, including a code editor, terminal, and build tools.
- Integrate your workspace with the rest of GitLab, including merge requests and CI/CD pipelines.
