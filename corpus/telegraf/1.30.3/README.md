---
collection: telegraf
version: "1.30.3"
title: "![tiger](assets/TelegrafTigerSmall.png \"tiger\") Telegraf"
source_url: https://github.com/influxdata/telegraf/blob/fd4af886672c8256ff17c888935a801d941894c4/README.md
fetched_at: 2024-05-20T10:00:01-06:00
---
# ![tiger](assets/TelegrafTigerSmall.png "tiger") <!-- unresolved-source-link: target=assets/TelegrafTigerSmall.png "tiger" --> Telegraf

[![GoDoc](https://img.shields.io/badge/doc-reference-00ADD8.svg?logo=go)](https://godoc.org/github.com/influxdata/telegraf)  [![Docker pulls](https://img.shields.io/docker/pulls/library/telegraf.svg)](https://hub.docker.com/_/telegraf/) [![Go Report Card](https://goreportcard.com/badge/github.com/influxdata/telegraf)](https://goreportcard.com/report/github.com/influxdata/telegraf) [![Circle CI](https://circleci.com/gh/influxdata/telegraf.svg?style=svg)](https://circleci.com/gh/influxdata/telegraf)

Telegraf is an agent for collecting, processing, aggregating, and writing
metrics, logs, and other arbitrary data.

* Offers a comprehensive suite of over 300 plugins, covering a wide range of
  functionalities including system monitoring, cloud services, and message
  passing
* Enables the integration of user-defined code to collect, transform, and
  transmit data efficiently
* Compiles into a standalone static binary without any external dependencies,
  ensuring a streamlined deployment process
* Utilizes TOML for configuration, providing a user-friendly and unambiguous
  setup experience
* Developed with contributions from a diverse community of over 1,200
  contributors

Users can choose plugins from a wide range of topics, including but not limited
to:

* Devices: [OPC UA][], [Modbus][]
* Logs: [File][], [Tail][], [Directory Monitor][]
* Messaging: [AMQP][], [Kafka][], [MQTT][]
* Monitoring: [OpenTelemetry][], [Prometheus][]
* Networking: [Cisco TelemetryMDT][], [gNMI][]
* System monitoring: [CPU][], [Memory][], [Disk][], [Network][], [SMART][],
  [Docker][], [Nvidia SMI][], etc.
* Universal: [Exec][], [HTTP][], [HTTP Listener][], [SNMP][], [SQL][]
* Windows: [Event Log][], [Management Instrumentation][],
  [Performance Counters][]

## 🔨 Installation

For binary builds, Docker images, RPM & DEB packages, and other builds of
Telegraf, please see the [install guide](/docs/INSTALL_GUIDE.md).

See the [releases documentation](/docs/RELEASES.md) for details on versioning
and when releases are made.

## 💻 Usage

Users define a TOML configuration with the plugins and settings they wish to
use, then pass that configuration to Telegraf. The Telegraf agent then
collects data from inputs at each interval and sends data to outputs at each
flush interval.

For a basic walkthrough see [quick start](/docs/QUICK_START.md).

## 📖 Documentation

For a full list of documentation including tutorials, reference and other
material, start with the [/docs directory](/docs/README.md).

Additionally, each plugin has its own README that includes details about how to
configure, use, and sometimes debug or troubleshoot. Look under the
[/plugins directory](/plugins/) for specific plugins.

Here are some commonly used documents:

* [Changelog](/CHANGELOG.md)
* [Configuration](/docs/CONFIGURATION.md)
* [FAQ](/docs/FAQ.md)
* [Releases](https://github.com/influxdata/telegraf/releases)
* [Security](/SECURITY.md)

## ❤️ Contribute

[![Contribute](https://img.shields.io/badge/contribute-to_telegraf-blue.svg?logo=influxdb)](https://github.com/influxdata/telegraf/blob/fd4af886672c8256ff17c888935a801d941894c4/CONTRIBUTING.md)

We love our community of over 1,200 contributors! Many of the plugins included
in Telegraf were originally contributed by community members. Check out
our [contributing guide](CONTRIBUTING.md) <!-- unresolved-source-link: target=CONTRIBUTING.md --> if you are interested in helping out.
Also, join us on our [Community Slack](https://influxdata.com/slack) or
[Community Forums](https://community.influxdata.com/) if you have questions or
comments for our engineering teams.

If you are completely new to Telegraf and InfluxDB, you can also enroll for free at
[InfluxDB university](https://www.influxdata.com/university/) to take courses to
learn more.

## ℹ️ Support

[![Slack](https://img.shields.io/badge/slack-join_chat-blue.svg?logo=slack)](https://www.influxdata.com/slack) [![Forums](https://img.shields.io/badge/discourse-join_forums-blue.svg?logo=discourse)](https://community.influxdata.com/)

Please use the [Community Slack](https://influxdata.com/slack) or
[Community Forums](https://community.influxdata.com/) if you have questions or
comments for our engineering teams. GitHub issues are limited to actual issues
and feature requests only.

## 📜 License

[![MIT](https://img.shields.io/badge/license-MIT-blue)](https://github.com/influxdata/telegraf/blob/fd4af886672c8256ff17c888935a801d941894c4/LICENSE)

[OPC UA]: https://github.com/influxdata/telegraf/tree/fd4af886672c8256ff17c888935a801d941894c4/plugins/inputs/opcua
[Modbus]: https://github.com/influxdata/telegraf/tree/fd4af886672c8256ff17c888935a801d941894c4/plugins/inputs/modbus
[File]: https://github.com/influxdata/telegraf/tree/fd4af886672c8256ff17c888935a801d941894c4/plugins/inputs/file
[Tail]: https://github.com/influxdata/telegraf/tree/fd4af886672c8256ff17c888935a801d941894c4/plugins/inputs/tail
[Directory Monitor]: https://github.com/influxdata/telegraf/tree/fd4af886672c8256ff17c888935a801d941894c4/plugins/inputs/directory_monitor
[AMQP]: https://github.com/influxdata/telegraf/tree/fd4af886672c8256ff17c888935a801d941894c4/plugins/inputs/amqp_consumer
[Kafka]: https://github.com/influxdata/telegraf/tree/fd4af886672c8256ff17c888935a801d941894c4/plugins/inputs/kafka_consumer
[MQTT]: https://github.com/influxdata/telegraf/tree/fd4af886672c8256ff17c888935a801d941894c4/plugins/inputs/mqtt_consumer
[OpenTelemetry]: https://github.com/influxdata/telegraf/tree/fd4af886672c8256ff17c888935a801d941894c4/plugins/inputs/opentelemetry
[Prometheus]: https://github.com/influxdata/telegraf/tree/fd4af886672c8256ff17c888935a801d941894c4/plugins/inputs/prometheus
[Cisco TelemetryMDT]: https://github.com/influxdata/telegraf/tree/fd4af886672c8256ff17c888935a801d941894c4/plugins/inputs/cisco_telemetry_mdt
[gNMI]: https://github.com/influxdata/telegraf/tree/fd4af886672c8256ff17c888935a801d941894c4/plugins/inputs/gnmi
[CPU]: https://github.com/influxdata/telegraf/tree/fd4af886672c8256ff17c888935a801d941894c4/plugins/inputs/cpu
[Memory]: https://github.com/influxdata/telegraf/tree/fd4af886672c8256ff17c888935a801d941894c4/plugins/inputs/mem
[Disk]: https://github.com/influxdata/telegraf/tree/fd4af886672c8256ff17c888935a801d941894c4/plugins/inputs/disk
[Network]: https://github.com/influxdata/telegraf/tree/fd4af886672c8256ff17c888935a801d941894c4/plugins/inputs/net
[SMART]: https://github.com/influxdata/telegraf/tree/fd4af886672c8256ff17c888935a801d941894c4/plugins/inputs/smartctl
[Docker]: https://github.com/influxdata/telegraf/tree/fd4af886672c8256ff17c888935a801d941894c4/plugins/inputs/docker
[Nvidia SMI]: https://github.com/influxdata/telegraf/tree/fd4af886672c8256ff17c888935a801d941894c4/plugins/inputs/nvidia_smi
[Exec]: https://github.com/influxdata/telegraf/tree/fd4af886672c8256ff17c888935a801d941894c4/plugins/inputs/exec
[HTTP]: https://github.com/influxdata/telegraf/tree/fd4af886672c8256ff17c888935a801d941894c4/plugins/inputs/http
[HTTP Listener]: https://github.com/influxdata/telegraf/tree/fd4af886672c8256ff17c888935a801d941894c4/plugins/inputs/http_listener_v2
[SNMP]: https://github.com/influxdata/telegraf/tree/fd4af886672c8256ff17c888935a801d941894c4/plugins/inputs/snmp
[SQL]: https://github.com/influxdata/telegraf/tree/fd4af886672c8256ff17c888935a801d941894c4/plugins/inputs/sql
[Event Log]: https://github.com/influxdata/telegraf/tree/fd4af886672c8256ff17c888935a801d941894c4/plugins/inputs/win_eventlog
[Management Instrumentation]: https://github.com/influxdata/telegraf/tree/fd4af886672c8256ff17c888935a801d941894c4/plugins/inputs/win_wmi
[Performance Counters]: https://github.com/influxdata/telegraf/tree/fd4af886672c8256ff17c888935a801d941894c4/plugins/inputs/win_perf_counters
