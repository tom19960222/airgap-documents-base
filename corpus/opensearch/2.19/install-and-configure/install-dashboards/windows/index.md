---
collection: "opensearch"
version: "2.19"
title: "Windows"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_install-and-configure/install-dashboards/windows.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_install-and-configure/install-dashboards/windows.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/install-and-configure/install-dashboards/windows/"
canonical_url: "https://docs.opensearch.org/latest/install-and-configure/install-dashboards/windows/"
canonical_route: "/install-and-configure/install-dashboards/windows/"
redirect_from: ["/dashboards/install/windows/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 37
parent: "Installing OpenSearch Dashboards"
---
# Run OpenSearch Dashboards on Windows

Perform the following steps to install OpenSearch Dashboards on Windows.

Make sure you have a zip utility installed.
{: .note }

1. Download the [`opensearch-dashboards-{{site.opensearch_version}}-windows-x64.zip`](https://artifacts.opensearch.org/releases/bundle/opensearch-dashboards/2.19.3/opensearch-dashboards-2.19.3-windows-x64.zip){:target='\_blank'} archive.

1. To extract the archive contents, right-click to select **Extract All**.

   **Note**: Some versions of the Windows operating system limit the file path length. If you encounter a path-length-related error when unzipping the archive, perform the following steps to enable long path support:

   1. Open Powershell by entering `powershell` in the search box next to **Start** on the taskbar.
   1. Run the following command in Powershell:
      ```bat
      Set-ItemProperty -Path HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem LongPathsEnabled -Type DWORD -Value 1 -Force
      ```
   1. Restart your computer.

1. Run OpenSearch Dashboards.

   There are two ways of running OpenSearch Dashboards:

   1. Run the batch script using the Windows UI:

      1. Navigate to the top directory of your OpenSearch Dashboards installation and open the `opensearch-dashboards-{{site.opensearch_version}}` folder.
      1. If desired, modify `opensearch_dashboards.yml` located in the `config` folder, to change the default OpenSearch Dashboards settings.
      1. Open the `bin` folder and run the batch script by double-clicking the `opensearch-dashboards.bat` file. This opens a command prompt with an OpenSearch Dashboards instance running.

   1. Run the batch script from Command Prompt or Powershell:

      1. Open Command Prompt by entering `cmd`, or Powershell by entering `powershell`, in the search box next to **Start** on the taskbar.
      1. Change to the top directory of your OpenSearch Dashboards installation.
         ```bat
         cd \path\to\opensearch-dashboards-2.19.3
         ```
      1. If desired, modify `config\opensearch_dashboards.yml`.
      1. Run the batch script to start OpenSearch Dashboards.
         ```bat
         .\bin\opensearch-dashboards.bat
         ```

To stop OpenSearch Dashboards, press `Ctrl+C` in Command Prompt or Powershell, or simply close the Command Prompt or Powershell window.
{: .tip}
