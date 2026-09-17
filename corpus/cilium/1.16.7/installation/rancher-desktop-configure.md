---
collection: cilium
version: "1.16.7"
title: "rancher-desktop-configure"
source_url: https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/installation/rancher-desktop-configure.rst
fetched_at: 2025-02-13T12:04:31Z
---
Configuring Rancher Desktop is done using a YAML configuration file.
This step is necessary in order to disable the default CNI and replace it with
Cilium.

Next you need to start Rancher Desktop with ``containerd`` and create a override.yaml <!-- unresolved-rst-link: kind=download target=/installation/rancher-desktop-override.yaml -->:

.. literalinclude:: /installation/rancher-desktop-override.yaml
   :language: yaml

After the file is created move it into your Rancher Desktop's ``lima/_config`` directory:

.. tabs::
   .. group-tab:: Linux

     .. code-block:: shell-session

       cp override.yaml ~/.local/share/rancher-desktop/lima/_config/override.yaml

   .. group-tab:: macOS

     .. code-block:: shell-session

       cp override.yaml ~/Library/Application\ Support/rancher-desktop/lima/_config/override.yaml

Finally, open the Rancher Desktop UI and go to the Troubleshooting panel and click "Reset Kubernetes".

After a few minutes Rancher Desktop will start back up prepared for installing Cilium.
