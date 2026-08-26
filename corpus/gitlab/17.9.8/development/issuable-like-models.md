---
collection: gitlab
version: "17.9.8"
title: "Issuable-like Rails models utilities"
source_url: https://gitlab.com/gitlab-org/gitlab/-/blob/v17.9.8-ee/doc/development/issuable-like-models.md
fetched_at: 2025-05-07T10:05:15Z
---
GitLab Rails codebase contains several models that hold common functionality and behave similarly to
[Issues](../user/project/issues/_index.md). Other examples of "issuables"
are [merge requests](../user/project/merge_requests/_index.md) and
[Epics](../user/group/epics/_index.md).

This guide accumulates guidelines on working with such Rails models.

## Important text fields

There are maximum length constraints for the most important text fields for issuables:

- `title`: 255 characters
- `description`: 1 megabyte
