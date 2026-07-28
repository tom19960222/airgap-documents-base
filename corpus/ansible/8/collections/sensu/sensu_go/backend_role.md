---
collection: ansible
version: "8"
title: "sensu.sensu_go.backend role – Install, configure, and start Sensu Go backend"
source_url: https://docs.ansible.com/projects/ansible/8/collections/sensu/sensu_go/backend_role.html
fetched_at: 2026-07-28T02:53:44+00:00
---
# sensu.sensu_go.backend role – Install, configure, and start Sensu Go backend

> **Note:**
>
> This role is part of the [sensu.sensu_go collection](https://galaxy.ansible.com/ui/repo/published/sensu/sensu_go/) (version 1.14.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it use: `ansible-galaxy collection install sensu.sensu_go`.
>
> To use it in a playbook, specify: `sensu.sensu_go.backend`.

- [Entry point `configure` – Configure Sensu Go backend](backend_role.md#entry-point-configure-configure-sensu-go-backend)

  - [Synopsis](backend_role.md#synopsis)
  - [Parameters](backend_role.md#parameters)
- [Entry point `main` – Install, configure, and start Sensu Go backend](backend_role.md#entry-point-main-install-configure-and-start-sensu-go-backend)

  - [Synopsis](backend_role.md#id1)
  - [Parameters](backend_role.md#id2)
- [Entry point `start` – Start Sensu Go backend](backend_role.md#entry-point-start-start-sensu-go-backend)

  - [Synopsis](backend_role.md#id3)
  - [Parameters](backend_role.md#id4)

## [Entry point `configure` – Configure Sensu Go backend](backend_role.md#id5)

### [Synopsis](backend_role.md#id6)

- Write the Sensu Go backend configuration file and optionally copy the keys and certificates over.

### [Parameters](backend_role.md#id7)

| Parameter | Comments |
| --- | --- |
| **api_cert_file**  string | Path to the certificate used to secure the Sensu Go API. |
| **api_key_file**  string | Path to the private key corresponding to the Sensu Go API certificate. Must be unencrypted. |
| **api_trusted_ca_file**  string | Path to the trusted certificate authority for the Sensu Go API certificates. |
| **backend_config**  dictionary | Any option that is valid for the Sensu Go backend version we are installing.  All valid options are listed at <https://docs.sensu.io/sensu-go/latest/reference/backend/#configuration>.  Role copies the key-value pairs from the *backend_config* variable verbatim to the configuration file. This means that we must copy the key names **exactly** as they appear in the configuration reference. In a way, the *backend_config* variable should contain a properly indented copy of the `/etc/sensu/backend.yml` file. |
| **dashboard_cert_file**  string | Path to the certificate used for SSL/TLS connections to the dashboard. |
| **dashboard_key_file**  string | Path to the private key corresponding to the dashboard certificate. Must be unencrypted. |
| **etcd_cert_file**  string | Path to the certificate used for SSL/TLS connections **to** etcd. This is a client certificate. |
| **etcd_key_file**  string | Path to the private key for the etcd client certificate file. Must be unencrypted. |
| **etcd_peer_cert_file**  string | Path to the certificate used for SSL/TLS connections between peers. This will be used both for listening on the peer address as well as sending requests to other peers. |
| **etcd_peer_key_file**  string | Path to the peer certificate’s key. Must be unencrypted. |
| **etcd_peer_trusted_ca_file**  string | Path to the trusted certificate authority for the peer certificates. |
| **etcd_trusted_ca_file**  string | Path to the trusted certificate authority for the etcd client certificates. |

## [Entry point `main` – Install, configure, and start Sensu Go backend](backend_role.md#id8)

### [Synopsis](backend_role.md#id9)

- Install, configure, and start the Sensu Go backend service and initialize it on the first run.

### [Parameters](backend_role.md#id10)

| Parameter | Comments |
| --- | --- |
| **api_cert_file**  string | Path to the certificate used to secure the Sensu Go API. |
| **api_key_file**  string | Path to the private key corresponding to the Sensu Go API certificate. Must be unencrypted. |
| **api_trusted_ca_file**  string | Path to the trusted certificate authority for the Sensu Go API certificates. |
| **backend_config**  dictionary | Any option that is valid for the Sensu Go backend version we are installing.  All valid options are listed at <https://docs.sensu.io/sensu-go/latest/reference/backend/#configuration>.  Role copies the key-value pairs from the *backend_config* variable verbatim to the configuration file. This means that we must copy the key names **exactly** as they appear in the configuration reference. In a way, the *backend_config* variable should contain a properly indented copy of the `/etc/sensu/backend.yml` file. |
| **build**  string | Package build to install.  Can be any valid build string such as `8290` or a special value latest.  If the *version* variable is set to latest, this variable is ignored and the latest available build is installed.  **Default:** `"latest"` |
| **channel**  string | Repository channel that serves as a source of packages.  Visit the packagecloud site to find all available channels.  **Default:** `"stable"` |
| **cluster_admin_password**  string | Initial admin password to create when initializing backend for the first time.  **Default:** `"P@ssw0rd!"` |
| **cluster_admin_username**  string | Initial admin user to create when initializing backend for the first time.  **Default:** `"admin"` |
| **dashboard_cert_file**  string | Path to the certificate used for SSL/TLS connections to the dashboard. |
| **dashboard_key_file**  string | Path to the private key corresponding to the dashboard certificate. Must be unencrypted. |
| **etcd_cert_file**  string | Path to the certificate used for SSL/TLS connections **to** etcd. This is a client certificate. |
| **etcd_key_file**  string | Path to the private key for the etcd client certificate file. Must be unencrypted. |
| **etcd_peer_cert_file**  string | Path to the certificate used for SSL/TLS connections between peers. This will be used both for listening on the peer address as well as sending requests to other peers. |
| **etcd_peer_key_file**  string | Path to the peer certificate’s key. Must be unencrypted. |
| **etcd_peer_trusted_ca_file**  string | Path to the trusted certificate authority for the peer certificates. |
| **etcd_trusted_ca_file**  string | Path to the trusted certificate authority for the etcd client certificates. |
| **version**  string | Package version to install.  Can be any valid version string such as `6.2.5` or special value `latest`.  **Default:** `"latest"` |

## [Entry point `start` – Start Sensu Go backend](backend_role.md#id11)

### [Synopsis](backend_role.md#id12)

- Start the Sensu Go backend service and initialize it on the first run.

### [Parameters](backend_role.md#id13)

| Parameter | Comments |
| --- | --- |
| **cluster_admin_password**  string | Initial admin password to create when initializing backend for the first time.  **Default:** `"P@ssw0rd!"` |
| **cluster_admin_username**  string | Initial admin user to create when initializing backend for the first time.  **Default:** `"admin"` |

#### Collection links

- [Issue Tracker](https://github.com/sensu/sensu-go-ansible/issues)
- [Repository (Sources)](https://github.com/sensu/sensu-go-ansible)
