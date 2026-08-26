---
collection: gitlab
version: "17.9.8"
title: "Topology Service"
source_url: https://gitlab.com/gitlab-org/gitlab/-/blob/v17.9.8-ee/doc/development/cells/topology_service.md
fetched_at: 2025-05-07T10:05:15Z
---
## Updating the Topology Service Gem

The Topology Service is developed in its [own repository](https://gitlab.com/gitlab-org/cells/topology-service)
We generate the Ruby Gem there, and manually copy the Gem to GitLab vendors folder, in
`vendor/gems/gitlab-topology-service-client`.

To make it easy, you can just run this bash script:

```shell
bash scripts/update-topology-service-gem.sh
```

This script is going to:

1. Clone the topology service repository into a temporary folder.
1. Check if the Ruby Gem has a newer code.
1. If so, it will update the Gem in `vendor/gems/gitlab-topology-service-client` and create a commit.
1. Clean up the temporary repository.
