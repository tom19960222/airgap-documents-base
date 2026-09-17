---
collection: "opensearch"
version: "2.19"
title: "OpenSearch CLI"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_tools/cli.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_tools/cli.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/tools/cli/"
canonical_url: "https://docs.opensearch.org/latest/tools/cli/"
canonical_route: "/tools/cli/"
redirect_from: ["/clients/cli/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_children: false
layout: "default"
nav_order: 70
---
# OpenSearch CLI

The OpenSearch CLI command line interface (opensearch-cli) lets you manage your OpenSearch cluster from the command line and automate tasks.

Currently, opensearch-cli supports the [Anomaly Detection](../../observing-your-data/ad/index.md) and [k-NN](../../vector-search/vector-search-techniques/index.md) plugins, along with arbitrary REST API paths. Among other things, you can use opensearch-cli to create and delete detectors, start and stop them, and check k-NN statistics.

Profiles let you easily access different clusters or sign requests with different credentials. opensearch-cli supports unauthenticated requests, HTTP basic signing, and IAM signing for Amazon Web Services.

This example moves a detector (`ecommerce-count-quantity`) from a staging cluster to a production cluster:

```bash
opensearch-cli ad get ecommerce-count-quantity --profile staging > ecommerce-count-quantity.json
opensearch-cli ad create ecommerce-count-quantity.json --profile production
opensearch-cli ad start ecommerce-count-quantity.json --profile production
opensearch-cli ad stop ecommerce-count-quantity --profile staging
opensearch-cli ad delete ecommerce-count-quantity --profile staging
```

## Install

1. [Download](https://opensearch.org/downloads.html){:target='\_blank'} and extract the appropriate installation package for your computer.

1. Make the `opensearch-cli` file executable:

   ```bash
   chmod +x ./opensearch-cli
   ```

1. Add the command to your path:

   ```bash
   export PATH=$PATH:$(pwd)
   ```

1. Confirm the CLI is working properly:

   ```bash
   opensearch-cli --version
   ```

## Profiles

Profiles let you easily switch between different clusters and user credentials. To get started, run `opensearch-cli profile create` with the `--auth-type`, `--endpoint`, and `--name` options:

```bash
opensearch-cli profile create --auth-type basic --endpoint https://localhost:9200 --name docker-local
```

Alternatively, save a configuration file to `~/.opensearch-cli/config.yaml`:

```yaml
profiles:
    - name: docker-local
      endpoint: https://localhost:9200
      user: admin
      password: foobar
    - name: aws
      endpoint: https://some-cluster.us-east-1.es.amazonaws.com
      aws_iam:
        profile: ""
        service: es
```

## Usage

opensearch-cli commands use the following syntax:

```bash
opensearch-cli <command> <subcommand> <flags>
```

For example, the following command retrieves information about a detector:

```bash
opensearch-cli ad get my-detector --profile docker-local
```

For a request to the OpenSearch CAT API, try the following command:

```bash
opensearch-cli curl get --path _cat/plugins --profile aws
```

Use the `-h` or `--help` flag to see all supported commands, subcommands, or usage for a specific command:

```bash
opensearch-cli -h
opensearch-cli ad -h
opensearch-cli ad get -h
```
