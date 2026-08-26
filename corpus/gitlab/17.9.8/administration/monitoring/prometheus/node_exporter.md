---
collection: gitlab
version: "17.9.8"
title: "Node exporter"
source_url: https://gitlab.com/gitlab-org/gitlab/-/blob/v17.9.8-ee/doc/administration/monitoring/prometheus/node_exporter.md
fetched_at: 2025-05-07T10:05:15Z
---
- Tier: Free, Premium, Ultimate
- Offering: GitLab Self-Managed

The [node exporter](https://github.com/prometheus/node_exporter) enables you to measure
various machine resources such as memory, disk and CPU utilization.

For self-compiled installations, you must install and configure it yourself.

To enable the node exporter:

1. [Enable Prometheus](_index.md#configuring-prometheus).
1. Edit `/etc/gitlab/gitlab.rb`.
1. Add (or find and uncomment) the following line, making sure it's set to `true`:

   ```ruby
   node_exporter['enable'] = true
   ```

1. Save the file, and [reconfigure GitLab](../../restart_gitlab.md#reconfigure-a-linux-package-installation)
   for the changes to take effect.

Prometheus begins collecting performance data from the node exporter
exposed at `localhost:9100`.
