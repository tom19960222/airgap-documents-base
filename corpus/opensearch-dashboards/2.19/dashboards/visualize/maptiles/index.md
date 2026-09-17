---
collection: "opensearch-dashboards"
version: "2.19"
title: "Configuring a Web Map Service (WMS)"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_dashboards/visualize/maptiles.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_dashboards/visualize/maptiles.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/dashboards/visualize/maptiles/"
canonical_url: "https://docs.opensearch.org/latest/dashboards/visualize/visualize-app/maptiles/"
canonical_route: "/dashboards/visualize/visualize-app/maptiles/"
redirect_from: ["/dashboards/maptiles/","/dashboards/visualize/visualize-app/maptiles/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.1"
chart_version: ""
grand_parent: "Building data visualizations"
layout: "default"
nav_order: 30
parent: "Coordinate and region maps"
---
# Configuring a Web Map Service (WMS)

The Open Geospatial Consortium (OGC) Web Map Service (WMS) specification is an international specification for requesting dynamic maps on the web. OpenSearch Dashboards includes default map tiles. For specialized maps, you can configure a WMS on OpenSearch Dashboards following these steps:

1. Log in to OpenSearch Dashboards at `https://<host>:<port>`. For example, you can connect to OpenSearch Dashboards by connecting to [https://localhost:5601](https://localhost:5601). The default username and password are `admin`.
2. Choose **Management** > **Advanced Settings**.
3. Locate `visualization:tileMap:WMSdefaults`.
4. Change `enabled` to `true` and add the URL of a valid WMS server, as shown in the following example:

   ```json
   {
     "enabled": true,
     "url": "<wms-map-server-url>",
     "options": {
       "format": "image/png",
       "transparent": true
     }
   }
   ```

Web map services may have licensing fees or restrictions, and you are responsible for complying with any such fees or restrictions.
{: .note }
