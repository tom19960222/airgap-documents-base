---
collection: ansible
version: "6"
title: "f5networks.f5_modules.bigip_profile_http module – Manage HTTP profiles on a BIG-IP"
source_url: https://docs.ansible.com/projects/ansible/6/collections/f5networks/f5_modules/bigip_profile_http_module.html
fetched_at: 2026-07-27T17:27:30+00:00
---
# f5networks.f5_modules.bigip_profile_http module – Manage HTTP profiles on a BIG-IP

> **Note:**
>
> This module is part of the [f5networks.f5_modules collection](https://galaxy.ansible.com/f5networks/f5_modules) (version 1.21.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install f5networks.f5_modules`.
>
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_profile_http`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_profile_http_module.md#synopsis)
- [Parameters](bigip_profile_http_module.md#parameters)
- [Notes](bigip_profile_http_module.md#notes)
- [Examples](bigip_profile_http_module.md#examples)
- [Return Values](bigip_profile_http_module.md#return-values)

## [Synopsis](bigip_profile_http_module.md#id1)

- Manage HTTP profiles on a BIG-IP device.

## [Parameters](bigip_profile_http_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **accept_xff**  boolean | Enables or disables trusting the client IP address, and statistics from the client IP address, based on the request’s XFF (X-forwarded-for) headers, if they exist.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile.  Choices:   - `false` - `true` |
| **description**  string | Description of the profile. |
| **dns_resolver**  string | Specifies the name of a configured DNS resolver, this option is mandatory when `proxy_type` is set to `explicit`.  Format of the name can be either be prepended by partition (`/Common/foo`), or specified just as an object name (`foo`).  To remove the entry, you can set a value of `none` or `''`, however the profile `proxy_type` must not be set as `explicit`. |
| **encrypt_cookie_secret**  string | Passphrase for cookie encryption.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile. |
| **encrypt_cookies**  list / elements=string | Cookie names for the system to encrypt.  To remove the entry completely, set a value of `none` or `''`.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile. |
| **enforcement**  dictionary | Specifies protocol enforcement settings for the HTTP profile.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile. |
| **excess_client_headers**  string | Specifies the behavior when too many client headers are received.  If set to `pass-through`, it switches to pass-through mode, when `reject`, the connection is rejected.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile.  Choices:   - `"reject"` - `"pass-through"` |
| **excess_server_headers**  string | Specifies the behavior when too many server headers are received.  If set to `pass-through`, it switches to pass-through mode, when `reject` the connection is rejected.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile.  Choices:   - `"reject"` - `"pass-through"` |
| **known_methods**  list / elements=string | Specifies which HTTP methods count as being known, removing RFC-defined methods from this list will cause the HTTP filter to not recognize them.  The default list provided with the system include: `CONNECT`, `DELETE`, `GET`, `HEAD`, `LOCK`, `OPTIONS`, `POST`, `PROPFIND`, `PUT`, `TRACE` ,`UNLOCK`. The list can be appended by by specifying the `default` keyword as one of the list elements.  The `default` keyword can also be used to restore the default `known_methods` on the system.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile. |
| **max_header_count**  string | Specifies the maximum number of headers allowed in HTTP request/response.  The valid value range is between 16 and 4096 inclusive.  When set to `default`, the value is `64`.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile. |
| **max_header_size**  string | Specifies the maximum header size specified in bytes.  The valid value range is between 0 and 4294967295 inclusive.  When set to `default`, the value is `32768` bytes  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile. |
| **max_requests**  string | Specifies the number of requests the system accepts on a per-connection basis.  The valid value range is between 0 and 4294967295 inclusive.  When set to `default`, the value is `0`, which means the system will not limit the number of requests per connection.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile. |
| **oversize_client_headers**  string | Specifies the behavior when too-large client headers are received.  If set to `pass-through`,it switches to pass-through mode, when `reject` the connection is rejected.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile.  Choices:   - `"reject"` - `"pass-through"` |
| **oversize_server_headers**  string | Specifies the behavior when too-large server headers are received.  If set to `pass-through`, it switches to pass-through mode, when `reject` the connection is rejected.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile.  Choices:   - `"reject"` - `"pass-through"` |
| **pipeline**  string | Enables HTTP/1.1 pipelining, allowing clients to make requests even when prior requests have not received a response.  In order for this to succeed, destination servers must include support for pipelining.  If set to `pass-through`, pipelined data causes the BIG-IP to immediately switch to pass-through mode and disable the HTTP filter.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile.  Choices:   - `"allow"` - `"reject"` - `"pass-through"` |
| **truncated_redirects**  boolean | Specifies what happens if a truncated redirect is seen from a server.  If `yes`, the redirect is forwarded to the client, otherwise the malformed HTTP is silently ignored.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile.  Choices:   - `false` - `true` |
| **unknown_method**  string | Specifies whether to allow, reject or switch to pass-through mode when an unknown HTTP method is parsed.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile.  Choices:   - `"allow"` - `"reject"` - `"pass-through"` |
| **fallback_host**  string | Specifies an HTTP fallback host.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile. |
| **fallback_status_codes**  list / elements=string | Specifies one or more HTTP error codes from server responses that should trigger a redirection to the fallback host.  The accepted valid error codes are as defined by RFC2616.  The codes can be specified as individual items or as valid ranges, for example `400-417` or `500-505`.  Mixing response code range across error types is invalid, for example defining `400-505` will raise an error.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile. |
| **header_erase**  string | The name of a header in an HTTP request, which the system removes from request.  To remove the entry completely, set a value of `none` or `''`.  The format of the header must be in `KEY:VALUE` format, otherwise an error occurs.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile. |
| **header_insert**  string | A string the system inserts as a header in an HTTP request.  To remove the entry completely, set a value of `none` or `''`.  The format of the header must be in `KEY:VALUE` format, otherwise an error occurs.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile. |
| **hsts_mode**  boolean | When set to `yes`, enables the HSTS settings.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile.  Choices:   - `false` - `true` |
| **include_subdomains**  boolean | When set to `yes`, applies the HSTS policy to the HSTS host and its sub-domains.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile.  Choices:   - `false` - `true` |
| **insert_xforwarded_for**  boolean | Specifies the system inserts an X-Forwarded-For header in an HTTP request with the client IP address, to use with connection pooling.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile.  Choices:   - `false` - `true` |
| **maximum_age**  string | Specifies the maximum length of time, in seconds, that HSTS functionality requests clients only use HTTPS to connect to the current host and any sub-domains of the current host’s domain name.  The accepted value range is `0 - 4294967295` seconds. A value of `0` seconds re-enables plaintext HTTP access, while specifying `indefinite` sets it to the maximum value.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile. |
| **name**  string / required | Specifies the name of the profile. |
| **oneconnect_transformations**  boolean | Enables the system to perform HTTP header transformations for keeping server-side connections open. This feature requires a OneConnect profile.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile.  Choices:   - `false` - `true` |
| **parent**  string | Specifies the profile from which this profile inherits settings.  When creating a new profile, if this parameter is not specified, the default is the system-supplied `http` profile. |
| **partition**  string | Device partition to manage resources on.  Default: `"Common"` |
| **provider**  dictionary  added in f5networks.f5_modules 1.0.0 | A dict object containing connection details. |
| **auth_provider**  string | Configures the auth provider for to obtain authentication tokens from the remote device.  This option is really used when working with BIG-IQ devices. |
| **no_f5_teem**  boolean | If `yes`, TEEM telemetry data is not sent to F5.  You may omit this option by setting the environment variable `F5_TELEMETRY_OFF`.  Previously used variable `F5_TEEM` is deprecated as its name was confusing.  Choices:   - `false` ← (default) - `true` |
| **password**  aliases: pass, pwd  string / required | The password for the user account used to connect to the BIG-IP.  You may omit this option by setting the environment variable `F5_PASSWORD`. |
| **server**  string / required | The BIG-IP host.  You may omit this option by setting the environment variable `F5_SERVER`. |
| **server_port**  integer | The BIG-IP server port.  You may omit this option by setting the environment variable `F5_SERVER_PORT`.  Default: `443` |
| **timeout**  integer | Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands. If the timeout is exceeded before the operation is completed, the module will error. |
| **transport**  string | Configures the transport connection to use when connecting to the remote device.  Choices:   - `"rest"` ← (default) |
| **user**  string / required | The username to connect to the BIG-IP with. This user must have administrative privileges on the device.  You may omit this option by setting the environment variable `F5_USER`. |
| **validate_certs**  boolean | If `no`, SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.  You may omit this option by setting the environment variable `F5_VALIDATE_CERTS`.  Choices:   - `false` - `true` ← (default) |
| **proxy_type**  string | Specifies the proxy mode for the profile.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile.  Choices:   - `"reverse"` - `"transparent"` - `"explicit"` |
| **redirect_rewrite**  string | Specifies whether the system rewrites the URIs that are part of HTTP redirect (3XX) responses.  When set to `none`, the system will not rewrite the URI in any HTTP redirect responses.  When set to `all`, the system rewrites the URI in all HTTP redirect responses.  When set to `matching`, the system rewrites the URI in any HTTP redirect responses that match the request URI.  When set to `nodes`, if the URI contains a node IP address instead of a host name, the system changes it to the virtual server address.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile.  Choices:   - `"none"` - `"all"` - `"matching"` - `"nodes"` |
| **request_chunking**  string | Specifies how to handle chunked and unchunked requests.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile.  Choices:   - `"rechunk"` - `"selective"` - `"preserve"` - `"sustain"` - `"unchunk"` |
| **response_chunking**  string | Specifies how to handle chunked and unchunked responses.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile.  Choices:   - `"rechunk"` - `"selective"` - `"preserve"` - `"sustain"` - `"unchunk"` |
| **server_agent_name**  string | Specifies the string used as the server name in traffic generated by BIG-IP.  To remove the entry completely, set a value of `none` or `''`.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile. |
| **sflow**  dictionary | Specifies sFlow settings for the HTTP profile.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile. |
| **poll_interval**  integer | Specifies the maximum interval in seconds between two pollings.  The valid value range is between 0 and 4294967295 seconds inclusive.  For this setting to take effect the `poll_interval_global` parameter must be set to `no`.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile. |
| **poll_interval_global**  boolean | Specifies whether the global HTTP poll-interval setting overrides the object-level `poll-interval` setting.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile.  Choices:   - `false` - `true` |
| **sampling_rate**  integer | Specifies the ratio of packets observed to the samples generated. For example, a sampling rate of `2000` specifies 1 sample will be randomly generated for every 2000 packets observed.  The valid value range is between 0 and 4294967295 packets inclusive.  For this setting to take effect the `sampling_rate_global` parameter must be set to `no`.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile. |
| **sampling_rate_global**  boolean | Specifies whether the global HTTP sampling-rate setting overrides the object-level sampling-rate setting.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile.  Choices:   - `false` - `true` |
| **state**  string | When `present`, ensures the profile exists.  When `absent`, ensures the profile is removed.  Choices:   - `"present"` ← (default) - `"absent"` |
| **update_password**  string | `always` will update passwords if the `encrypt_cookie_secret` is specified.  `on_create` will only set the password for newly created profiles.  Choices:   - `"always"` ← (default) - `"on_create"` |
| **xff_alternative_names**  list / elements=string | Specifies alternative XFF headers instead of the default X-forwarded-for header.  When creating a new profile, if this parameter is not specified, the default is provided by the parent profile. |

## [Notes](bigip_profile_http_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_profile_http_module.md#id4)

```yaml+jinja
- name: Create HTTP profile
  bigip_profile_http:
    name: my_profile
    insert_xforwarded_for: yes
    redirect_rewrite: all
    state: present
    provider:
      user: admin
      password: secret
      server: lb.mydomain.com
  delegate_to: localhost

- name: Remove HTTP profile
  bigip_profile_http:
    name: my_profile
    state: absent
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Add HTTP profile for transparent proxy
  bigip_profile_http:
    name: my_profile
    proxy_type: transparent
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost
```

## [Return Values](bigip_profile_http_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **accept_xff**  boolean | Enables or disables trusting the client IP address and statistics from the client IP address.  Returned: changed  Sample: `true` |
| **description**  string | Description of the profile.  Returned: changed  Sample: `"My profile"` |
| **dns_resolver**  string | Configured dns resolver.  Returned: changed  Sample: `"/Common/FooBar"` |
| **encrypt_cookies**  list / elements=string | Cookie names to encrypt.  Returned: changed  Sample: `["MyCookie1", "MyCookie2"]` |
| **enforcement**  complex | Specifies protocol enforcement settings for the HTTP profile.  Returned: changed  Sample: `"hash/dictionary of values"` |
| **excess_server_headers**  string | Specifies the behavior when too many server headers are received.  Returned: changed  Sample: `"pass-through"` |
| **known_methods**  list / elements=string | The list of known HTTP methods.  Returned: changed  Sample: `["default", "FOO", "BAR"]` |
| **max_header_count**  string | The maximum number of headers allowed in HTTP request/response.  Returned: changed  Sample: `"4096"` |
| **max_header_size**  string | The maximum header size specified in bytes.  Returned: changed  Sample: `"default"` |
| **max_requests**  string | The number of requests the system accepts on a per-connection basis.  Returned: changed  Sample: `"default"` |
| **oversize_client_headers**  string | Specifies the behavior when too-large client headers are received.  Returned: changed  Sample: `"reject"` |
| **oversize_server_headers**  string | Specifies the behavior when too-large server headers are received.  Returned: changed  Sample: `"reject"` |
| **pipeline**  string | Allows, rejects. or switches to pass-through mode when dealing with pipelined data.  Returned: changed  Sample: `"allow"` |
| **truncated_redirects**  boolean | Specifies what happens if a truncated redirect is seen from a server.  Returned: changed  Sample: `true` |
| **unknown_method**  string | Allows, rejects. or switches to pass-through mode when an unknown HTTP method is parsed.  Returned: changed  Sample: `"allow"` |
| **fallback_host**  string | Specifies an HTTP fallback host.  Returned: changed  Sample: `"foobar.com"` |
| **fallback_status_codes**  list / elements=string | HTTP error codes from server responses that should trigger a redirection to the fallback host.  Returned: changed  Sample: `["400-404", "500", "501"]` |
| **header_erase**  string | The name of a header in an HTTP request, which the system removes from request.  Returned: changed  Sample: `"FOO:BAR"` |
| **header_insert**  string | The string the system inserts as a header in an HTTP request.  Returned: changed  Sample: `"FOO:BAR"` |
| **hsts_mode**  boolean | Enables the HSTS settings.  Returned: changed  Sample: `false` |
| **include_subdomains**  boolean | Applies the HSTS policy to the HSTS host and its sub-domains.  Returned: changed  Sample: `true` |
| **insert_xforwarded_for**  boolean | Insert X-Forwarded-For-Header.  Returned: changed  Sample: `true` |
| **maximum_age**  string | The maximum length of time, in seconds, that HSTS functionality requests that clients only use HTTPS.  Returned: changed  Sample: `"indefinite"` |
| **oneconnect_transformations**  boolean | Enables or disables HTTP header transformations.  Returned: changed  Sample: `false` |
| **parent**  string | Specifies the profile from which this profile inherits settings.  Returned: changed  Sample: `"/Common/http"` |
| **proxy_type**  string | Specify proxy mode of the profile.  Returned: changed  Sample: `"explicit"` |
| **redirect_rewrite**  string | Rewrite URI that are part of 3xx responses.  Returned: changed  Sample: `"all"` |
| **request_chunking**  string | Specifies how to handle chunked and unchunked requests.  Returned: changed  Sample: `"rechunk"` |
| **response_chunking**  string | Specifies how to handle chunked and unchunked responses.  Returned: changed  Sample: `"rechunk"` |
| **server_agent_name**  string | The string used as the server name in traffic generated by BIG-IP.  Returned: changed  Sample: `"foobar"` |
| **sflow**  complex | Specifies sFlow settings for the HTTP profile.  Returned: changed  Sample: `"hash/dictionary of values"` |
| **poll_interval**  integer | Specifies the maximum interval in seconds between two pollings.  Returned: changed  Sample: `30` |
| **poll_interval_global**  boolean | Enables/Disables overriding HTTP poll-interval setting.  Returned: changed  Sample: `true` |
| **sampling_rate**  integer | Specifies the ratio of packets observed to the samples generated.  Returned: changed  Sample: `2000` |
| **sampling_rate_global**  boolean | Enables/Disables overriding HTTP sampling-rate setting.  Returned: changed  Sample: `true` |
| **xff_alternative_names**  list / elements=string | Specifies alternative XFF headers instead of the default X-forwarded-for header.  Returned: changed  Sample: `["FooBar", "client1"]` |

### Authors

- Wojciech Wypior (@wojtek0806)

### Collection links

[Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
[Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
[Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
