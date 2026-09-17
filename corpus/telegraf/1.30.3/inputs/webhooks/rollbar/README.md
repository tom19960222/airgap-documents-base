---
collection: telegraf
version: "1.30.3"
title: "rollbar webhooks"
source_url: https://github.com/influxdata/telegraf/blob/fd4af886672c8256ff17c888935a801d941894c4/plugins/inputs/webhooks/rollbar/README.md
fetched_at: 2024-05-20T10:00:01-06:00
---
# rollbar webhooks

You should configure your Rollbar's Webhooks to point at the `webhooks` service. To do this go to [rollbar.com](https://rollbar.com/) and click `Settings > Notifications > Webhook`. In the resulting page set `URL` to `http://<my_ip>:1619/rollbar`, and click on `Enable Webhook Integration`.

## Events

The titles of the following sections are links to the full payloads and details for each event. The body contains what information from the event is persisted. The format is as follows:

```toml
# TAGS
* 'tagKey' = `tagValue` type
# FIELDS
* 'fieldKey' = `fieldValue` type
```

The tag values and field values show the place on the incoming JSON object where the data is sourced from.

See [webhook doc](https://rollbar.com/docs/webhooks/)

### `new_item` event

**Tags:**

* 'event' = `event.event_name` string
* 'environment' = `event.data.item.environment` string
* 'project_id = `event.data.item.project_id` int
* 'language' = `event.data.item.last_occurence.language` string
* 'level' = `event.data.item.last_occurence.level` string

**Fields:**

* 'id' = `event.data.item.id` int

### `occurrence` event

**Tags:**

* 'event' = `event.event_name` string
* 'environment' = `event.data.item.environment` string
* 'project_id = `event.data.item.project_id` int
* 'language' = `event.data.occurrence.language` string
* 'level' = `event.data.occurrence.level` string

**Fields:**

* 'id' = `event.data.item.id` int

### `deploy` event

**Tags:**

* 'event' = `event.event_name` string
* 'environment' = `event.data.deploy.environment` string
* 'project_id = `event.data.deploy.project_id` int

**Fields:**

* 'id' = `event.data.item.id` int
