---
collection: "opensearch"
version: "2.19"
title: "Experimental feature flags"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_install-and-configure/configuring-opensearch/experimental.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_install-and-configure/configuring-opensearch/experimental.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/install-and-configure/configuring-opensearch/experimental/"
canonical_url: "https://docs.opensearch.org/latest/install-and-configure/configuring-opensearch/experimental/"
canonical_route: "/install-and-configure/configuring-opensearch/experimental/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 120
parent: "Configuring OpenSearch"
---
# Experimental feature flags

OpenSearch releases may contain experimental features that you can enable or disable as needed. There are several methods for enabling feature flags, depending on the installation type.

## Enable in opensearch.yml

If you are running an OpenSearch cluster and want to enable feature flags in the config file, add the following line to `opensearch.yml`:

```yaml
opensearch.experimental.feature.<feature_name>.enabled: true
```

## Enable on Docker containers

If you’re running Docker, add the following line to `docker-compose.yml` under the `opensearch-node` > `environment` section:

```bash
OPENSEARCH_JAVA_OPTS="-Dopensearch.experimental.feature.<feature_name>.enabled=true"
```

## Enable on a tarball installation

To enable feature flags on a tarball installation, provide the new JVM parameter either in `config/jvm.options` or `OPENSEARCH_JAVA_OPTS`.

### Option 1: Modify jvm.options

Add the following lines to `config/jvm.options` before starting the `opensearch` process to enable the feature and its dependency:

```bash
-Dopensearch.experimental.feature.<feature_name>.enabled=true
```

Then run OpenSearch:

```bash
./bin/opensearch
```

### Option 2: Enable with an environment variable

As an alternative to directly modifying `config/jvm.options`, you can define the properties by using an environment variable. This can be done using a single command when you start OpenSearch or by defining the variable with `export`.

To add the feature flags inline when starting OpenSearch, run the following command:

```bash
OPENSEARCH_JAVA_OPTS="-Dopensearch.experimental.feature.<feature_name>.enabled=true" ./opensearch-2.19.3/bin/opensearch
```

If you want to define the environment variable separately prior to running OpenSearch, run the following commands:

```bash
export OPENSEARCH_JAVA_OPTS="-Dopensearch.experimental.feature.<feature_name>.enabled=true"
```

```bash
./bin/opensearch
```

## Enable for OpenSearch development

To enable feature flags for development, you must add the correct properties to `run.gradle` before building OpenSearch. See the [Developer Guide](https://github.com/opensearch-project/OpenSearch/blob/main/DEVELOPER_GUIDE.md) for information about to use how Gradle to build OpenSearch.

Add the following properties to run.gradle to enable the feature:

```gradle
testClusters {
    runTask {
      testDistribution = 'archive'
      if (numZones > 1) numberOfZones = numZones
      if (numNodes > 1) numberOfNodes = numNodes
      systemProperty 'opensearch.experimental.feature.<feature_name>.enabled', 'true'
    }
  }
```
