---
collection: fluent-bit
version: "3.2"
title: "JSON"
source_url: https://github.com/fluent/fluent-bit-docs/blob/36106a0740d3f62f05d0e9e69b2c0e21dfa9de21/pipeline/parsers/json.md
fetched_at: 2025-03-27T12:50:23+02:00
app_version: "3.2.10"
---
# JSON

The JSON parser is the simplest option: if the original log source is a JSON map string, it will take its structure and convert it directly to the internal binary representation.

A simple configuration that can be found in the default parsers configuration file, is the entry to parse Docker log files \(when the tail input plugin is used\):

```python
[PARSER]
    Name        docker
    Format      json
    Time_Key    time
    Time_Format %Y-%m-%dT%H:%M:%S %z
```

The following log entry is a valid content for the parser defined above:

```javascript
{"key1": 12345, "key2": "abc", "time": "2006-07-28T13:22:04Z"}
```

After processing, its internal representation will be:

```text
[1154103724, {"key1"=>12345, "key2"=>"abc"}]
```

The time has been converted to Unix timestamp \(UTC\) and the map reduced to each component of the original message.
