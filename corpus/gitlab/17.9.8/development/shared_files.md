---
collection: gitlab
version: "17.9.8"
title: "Shared files"
source_url: https://gitlab.com/gitlab-org/gitlab/-/blob/v17.9.8-ee/doc/development/shared_files.md
fetched_at: 2025-05-07T10:05:15Z
---
Historically, GitLab supported storing files that could be accessed from multiple application
servers in `shared/`, using a shared storage solution like NFS. Although this is still an option for
some GitLab installations, it must not be the only file storage option for a given feature. This is
because [cloud-native GitLab installations do not support it](architecture.md#adapting-existing-and-introducing-new-components).

Our [uploads documentation](uploads/_index.md) describes how to handle file storage in
such a way that it supports both options: direct disk access and object storage.
