---
collection: fluent-bit
version: "3.2"
title: "Getting Started"
source_url: https://github.com/fluent/fluent-bit-docs/blob/36106a0740d3f62f05d0e9e69b2c0e21dfa9de21/stream-processing/getting-started/README.md
fetched_at: 2025-03-27T12:50:23+02:00
app_version: "3.2.10"
---
# Getting Started

The following guide assumes that you are familiar with [Fluent Bit](https://fluentbit.io), if that is not the case we suggest you review the official manual first:

* [Fluent Bit Manual](https://docs.fluentbit.io/manual/)

## Requirements

* [Fluent Bit](https://fluentbit.io) &gt;= v1.1.0 or Fluent Bit from [GIT Master](https://github.com/fluent/fluent-bit)
* Basic understanding of Structured Query Language \(SQL\)

## Technical Concepts

| Concept | Description |
| :--- | :--- |
| Stream | A Stream represents an unique flow of data being ingested by an Input plugin. By default Streams get a name using the plugin name plus an internal numerical identification, e.g: tail.0 . Stream name can be changed setting the _alias_ property. |
| Task | Stream Processor configuration have the notion of Tasks that represents an execution unit, for short: SQL queries are configured in a Task. |
| Results | When Stream Processor runs a SQL query, results are generated. These results can be re-ingested back into the main Fluent Bit pipeline or simply redirected to the standard output interfaces for debugging purposes. |
| Tag | Fluent Bit group records and associate a Tag to them. Tags are used to define routing rules or in the case of the stream processor to attach to specific Tag that matches a pattern. |
| Match | Matching rule that can use a wildcard to match specific records associated to a Tag. |
