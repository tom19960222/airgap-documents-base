---
collection: ansible
version: "6"
title: "community.general.mqtt module – Publish a message on an MQTT topic for the IoT"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/mqtt_module.html
fetched_at: 2026-07-27T17:11:00+00:00
---
# community.general.mqtt module – Publish a message on an MQTT topic for the IoT

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](mqtt_module.md#ansible-collections-community-general-mqtt-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.mqtt`.

- [Synopsis](mqtt_module.md#synopsis)
- [Requirements](mqtt_module.md#requirements)
- [Parameters](mqtt_module.md#parameters)
- [Notes](mqtt_module.md#notes)
- [Examples](mqtt_module.md#examples)

## [Synopsis](mqtt_module.md#id1)

- Publish a message on an MQTT topic.

## [Requirements](mqtt_module.md#id2)

The below requirements are needed on the host that executes this module.

- mosquitto

## [Parameters](mqtt_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_cert**  aliases: ca_certs  path | The path to the Certificate Authority certificate files that are to be treated as trusted by this client. If this is the only option given then the client will operate in a similar manner to a web browser. That is to say it will require the broker to have a certificate signed by the Certificate Authorities in ca_certs and will communicate using TLS v1, but will not attempt any form of authentication. This provides basic network encryption but may not be sufficient depending on how the broker is configured. |
| **client_cert**  aliases: certfile  path | The path pointing to the PEM encoded client certificate. If this is not None it will be used as client information for TLS based authentication. Support for this feature is broker dependent. |
| **client_id**  string | MQTT client identifier  If not specified, a value `hostname + pid` will be used. |
| **client_key**  aliases: keyfile  path | The path pointing to the PEM encoded client private key. If this is not None it will be used as client information for TLS based authentication. Support for this feature is broker dependent. |
| **password**  string | Password for `username` to authenticate against the broker. |
| **payload**  string / required | Payload. The special string `"None"` may be used to send a NULL (i.e. empty) payload which is useful to simply notify with the *topic* or to clear previously retained messages. |
| **port**  integer | MQTT broker port number  Default: `1883` |
| **qos**  string | QoS (Quality of Service)  Choices:   - `"0"` ← (default) - `"1"` - `"2"` |
| **retain**  boolean | Setting this flag causes the broker to retain (i.e. keep) the message so that applications that subsequently subscribe to the topic can received the last retained message immediately.  Choices:   - `false` ← (default) - `true` |
| **server**  string | MQTT broker address/name  Default: `"localhost"` |
| **tls_version**  string | Specifies the version of the SSL/TLS protocol to be used.  By default (if the python version supports it) the highest TLS version is detected. If unavailable, TLS v1 is used.  Choices:   - `"tlsv1.1"` - `"tlsv1.2"` |
| **topic**  string / required | MQTT topic name |
| **username**  string | Username to authenticate against the broker. |

## [Notes](mqtt_module.md#id4)

> **Note:**
>
> - This module requires a connection to an MQTT broker such as Mosquitto <http://mosquitto.org> and the *Paho* `mqtt` Python client (<https://pypi.org/project/paho-mqtt/>).

## [Examples](mqtt_module.md#id5)

```yaml+jinja
- name: Publish a message on an MQTT topic
  community.general.mqtt:
    topic: 'service/ansible/{{ ansible_hostname }}'
    payload: 'Hello at {{ ansible_date_time.iso8601 }}'
    qos: 0
    retain: false
    client_id: ans001
  delegate_to: localhost
```

### Authors

- Jan-Piet Mens (@jpmens)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
