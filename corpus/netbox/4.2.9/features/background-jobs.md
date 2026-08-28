---
collection: netbox
version: "4.2.9"
title: "Background Jobs"
source_url: https://github.com/netbox-community/netbox/blob/v4.2.9/docs/features/background-jobs.md
fetched_at: 2025-04-30T14:31:30-04:00
---
# Background Jobs

NetBox includes the ability to execute certain functions as background tasks. These include:

* [Report](../customization/reports.md) execution
* [Custom script](../customization/custom-scripts.md) execution
* Synchronization of [remote data sources](../integrations/synchronized-data.md)

Additionally, NetBox plugins can enqueue their own background tasks. This is accomplished using the [Job model](../models/core/job.md). Background tasks are executed by the `rqworker` process(es).

## Scheduled Jobs

Background jobs can be configured to run immediately, or at a set time in the future. Scheduled jobs can also be configured to repeat at a set interval.
