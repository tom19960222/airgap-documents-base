---
collection: ansible
version: "8"
title: "f5networks.f5_modules.bigip_ssl_ocsp module – Manage OCSP configurations on BIG-IP"
source_url: https://docs.ansible.com/projects/ansible/8/collections/f5networks/f5_modules/bigip_ssl_ocsp_module.html
fetched_at: 2026-07-28T02:07:23+00:00
---
# f5networks.f5_modules.bigip_ssl_ocsp module – Manage OCSP configurations on BIG-IP

> **Note:**
>
> This module is part of the [f5networks.f5_modules collection](https://galaxy.ansible.com/ui/repo/published/f5networks/f5_modules/) (version 1.27.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install f5networks.f5_modules`.
>
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_ssl_ocsp`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_ssl_ocsp_module.md#synopsis)
- [Parameters](bigip_ssl_ocsp_module.md#parameters)
- [Notes](bigip_ssl_ocsp_module.md#notes)
- [Examples](bigip_ssl_ocsp_module.md#examples)
- [Return Values](bigip_ssl_ocsp_module.md#return-values)

## [Synopsis](bigip_ssl_ocsp_module.md#id1)

- Manage OCSP configurations on a BIG-IP system.

## [Parameters](bigip_ssl_ocsp_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **cache_error_timeout**  integer | Specifies the lifetime of an error response in the cache, in seconds. |
| **cache_timeout**  string | Specifies the lifetime of the OCSP response in the cache, in seconds. |
| **certificate**  string | Specifies a certificate used to sign an OCSP request. |
| **clock_skew**  integer | Specifies the tolerable absolute difference in the clocks of the responder and the BIG-IP system, in seconds. |
| **connection_timeout**  integer | Specifies the time interval the BIG-IP system waits for before ending the connection to the OCSP responder, in seconds. |
| **connections_limit**  integer | Specifies the maximum number of connections per second allowed for the OCSP certificate validator. |
| **dns_resolver**  string | Specifies the internal DNS resolver the BIG-IP system uses to fetch the OCSP response.  This involves specifying one or more DNS servers in the DNS resolver configuration.  Use this option when either there is a DNS server that can do the name-resolution of the OCSP responders, or the OCSP responder can be reached on one of BIG-IP system’s interfaces. |
| **hash_algorithm**  string | Specifies a hash algorithm used to sign an OCSP request.  **Choices:**   - `"sha256"` - `"sha1"` |
| **key**  string | Specifies a key used to sign an OCSP request. |
| **name**  string / required | Specifies the name of the OCSP certificate validator. |
| **partition**  string | Device partition to manage resources on.  **Default:** `"Common"` |
| **passphrase**  string | Specifies a passphrase used to sign an OCSP request. |
| **provider**  dictionary  *added in f5networks.f5_modules 1.0.0* | A dict object containing connection details. |
| **auth_provider**  string | Configures the auth provider for to obtain authentication tokens from the remote device.  This option is really used when working with BIG-IQ devices. |
| **no_f5_teem**  boolean | If `yes`, TEEM telemetry data is not sent to F5.  You may omit this option by setting the environment variable `F5_TELEMETRY_OFF`.  Previously used variable `F5_TEEM` is deprecated as its name was confusing.  **Choices:**   - `false` ← (default) - `true` |
| **password**  aliases: pass, pwd  string / required | The password for the user account used to connect to the BIG-IP or the BIG-IQ.  You may omit this option by setting the environment variable `F5_PASSWORD`. |
| **server**  string / required | The BIG-IP host or the BIG-IQ host.  You may omit this option by setting the environment variable `F5_SERVER`. |
| **server_port**  integer | The BIG-IP server port.  You may omit this option by setting the environment variable `F5_SERVER_PORT`.  **Default:** `443` |
| **timeout**  integer | Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands. If the timeout is exceeded before the operation is completed, the module will error. |
| **transport**  string | Configures the transport connection to use when connecting to the remote device.  **Choices:**   - `"rest"` ← (default) |
| **user**  string / required | The username to connect to the BIG-IP or the BIG-IQ. This user must have administrative privileges on the device.  You may omit this option by setting the environment variable `F5_USER`. |
| **validate_certs**  boolean | If `no`, SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.  You may omit this option by setting the environment variable `F5_VALIDATE_CERTS`.  **Choices:**   - `false` - `true` ← (default) |
| **proxy_server_pool**  string | Specifies the proxy server pool the BIG-IP system uses to fetch the OCSP response.  This involves creating a pool with proxy-servers.  Use this option when either the OCSP responder cannot be reached on any of BIG-IP system’s interfaces, or one or more servers can proxy an HTTP request to an external server and fetch the response. |
| **responder_url**  string | Specifies the absolute URL that overrides the OCSP responder URL obtained from the certificate’s AIA extensions. This should be an HTTP-based URL. |
| **route_domain**  string | Specifies the route domain for fetching an OCSP response using HTTP forward proxy. |
| **state**  string | When `present`, ensures the resource exists.  When `absent`, ensures the resource does not exist.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **status_age**  integer | Specifies the maximum allowed lag time the BIG-IP system accepts for the ‘thisUpdate’ time in the OCSP response. |
| **strict_responder_checking**  boolean | Specifies whether the responder’s certificate is checked for an OCSP signing extension.  **Choices:**   - `false` - `true` |
| **trusted_responders**  string | Specifies the certificates used for validating the OCSP response when the responder’s certificate has been omitted from the response. |
| **update_password**  string | `always` allows the user to update passwords. `on_create` only sets the password for newly created OCSP validators.  **Choices:**   - `"always"` ← (default) - `"on_create"` |

## [Notes](bigip_ssl_ocsp_module.md#id3)

> **Note:**
>
> - Requires BIG-IP >= 13.x.
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_ssl_ocsp_module.md#id4)

```yaml+jinja
- name: Create a OCSP validator
  bigip_ssl_ocsp:
    name: foo
    proxy_server_pool: validators-pool
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost
```

## [Return Values](bigip_ssl_ocsp_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cache_error_timeout**  integer | The new Response Caching Error Timeout value.  **Returned:** changed  **Sample:** `3600` |
| **cache_timeout**  string | The new Response Caching Timeout value.  **Returned:** changed  **Sample:** `"indefinite"` |
| **certificate**  string | The new Request Signing Certificate value.  **Returned:** changed  **Sample:** `"/Common/cert1"` |
| **clock_skew**  integer | The new Response Validation Clock Skew value.  **Returned:** changed  **Sample:** `300` |
| **connection_timeout**  integer | The new Connection Timeout value.  **Returned:** changed  **Sample:** `8` |
| **connections_limit**  integer | The new Concurrent Connections Limit value.  **Returned:** changed  **Sample:** `50` |
| **dns_resolver**  string | The new DNS Resolver value.  **Returned:** changed  **Sample:** `"/Common/resolver1"` |
| **hash_algorithm**  string | The new Request Signing Hash Algorithm value.  **Returned:** changed  **Sample:** `"sha256"` |
| **key**  string | The new Request Signing Key value.  **Returned:** changed  **Sample:** `"/Common/key1"` |
| **proxy_server_pool**  string | The new Proxy Server Pool value.  **Returned:** changed  **Sample:** `"/Common/pool1"` |
| **responder_url**  string | The new Connection Responder URL value.  **Returned:** changed  **Sample:** `"http://responder.site.com"` |
| **route_domain**  string | The new Route Domain value.  **Returned:** changed  **Sample:** `"/Common/0"` |
| **status_age**  integer | The new Response Validation Status Age value.  **Returned:** changed  **Sample:** `0` |
| **strict_responder_checking**  boolean | The new Response Validation Strict Responder Certificate Checking value.  **Returned:** changed  **Sample:** `true` |
| **trusted_responders**  integer | The new Response Validation Trusted Responders value.  **Returned:** changed  **Sample:** `"/Common/default"` |

### Authors

- Tim Rupp (@caphrim007)

### Collection links

- [Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
- [Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
- [Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
