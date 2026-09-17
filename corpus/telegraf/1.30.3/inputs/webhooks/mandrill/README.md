---
collection: telegraf
version: "1.30.3"
title: "mandrill webhook"
source_url: https://github.com/influxdata/telegraf/blob/fd4af886672c8256ff17c888935a801d941894c4/plugins/inputs/webhooks/mandrill/README.md
fetched_at: 2024-05-20T10:00:01-06:00
---
# mandrill webhook

You should configure your Mandrill's Webhooks to point at the `webhooks` service. To do this go to [mandrillapp.com](https://mandrillapp.com) and click `Settings > Webhooks`. In the resulting page, click on `Add a Webhook`, select all events, and set the `URL` to `http://<my_ip>:1619/mandrill`, and click on `Create Webhook`.

## Events

See the [webhook doc](https://mandrill.zendesk.com/hc/en-us/articles/205583307-Message-Event-Webhook-format).

All events for logs the original timestamp, the event name and the unique identifier of the message that generated the event.

**Tags:**

* 'event' = `event.event` string

**Fields:**

* 'id' = `event._id` string
