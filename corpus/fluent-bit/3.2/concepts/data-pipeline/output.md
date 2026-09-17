---
collection: fluent-bit
version: "3.2"
title: "Output"
source_url: https://github.com/fluent/fluent-bit-docs/blob/36106a0740d3f62f05d0e9e69b2c0e21dfa9de21/concepts/data-pipeline/output.md
fetched_at: 2025-03-27T12:50:23+02:00
app_version: "3.2.10"
---
# Output

The output interface lets you define destinations for your data. Common destinations
are remote services, local file systems, or other standard interfaces. Outputs are
implemented as plugins.

```mermaid
graph LR
    accTitle: Fluent Bit data pipeline
    accDescr: A diagram of the Fluent Bit data pipeline, which includes input, a parser, a filter, a buffer, routing, and various outputs.
    A[Input] --> B[Parser]
    B --> C[Filter]
    C --> D[Buffer]
    D --> E((Routing))
    E --> F[Output 1]
    E --> G[Output 2]
    E --> H[Output 3]
    style F stroke:darkred,stroke-width:2px;
    style G stroke:darkred,stroke-width:2px;
    style H stroke:darkred,stroke-width:2px;
```

When an output plugin is loaded, an internal _instance_ is created. Every instance
has its own independent configuration. Configuration keys are often called
_properties_.

Every output plugin has its own documentation section specifying how it can be used and what properties are available.

For more details, see [Output Plugins](https://docs.fluentbit.io/manual/pipeline/outputs).
