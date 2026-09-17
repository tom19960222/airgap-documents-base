---
collection: alertmanager
version: "0.27.0"
title: "Alerting overview"
source_url: https://github.com/prometheus/alertmanager/blob/0aa3c2aad14cff039931923ab16b26b7481783b5/docs/overview.md
fetched_at: 2024-02-28T11:35:54Z
---
# Alerting Overview

Alerting with Prometheus is separated into two parts. Alerting rules in
Prometheus servers send alerts to an Alertmanager. The [Alertmanager](alertmanager.md)
then manages those alerts, including silencing, inhibition, aggregation and
sending out notifications via methods such as email, on-call notification systems, and chat platforms.

The main steps to setting up alerting and notifications are:

* Setup and [configure](configuration.md) the Alertmanager
* [Configure Prometheus](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#alertmanager_config) to talk to the Alertmanager
* Create [alerting rules](https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/) in Prometheus
