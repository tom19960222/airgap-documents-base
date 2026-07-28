---
collection: ansible
version: "6"
title: "f5networks.f5_modules.bigip_device_info module – Collect information from F5 BIG-IP devices"
source_url: https://docs.ansible.com/projects/ansible/6/collections/f5networks/f5_modules/bigip_device_info_module.html
fetched_at: 2026-07-27T17:26:30+00:00
---
# f5networks.f5_modules.bigip_device_info module – Collect information from F5 BIG-IP devices

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
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_device_info`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_device_info_module.md#synopsis)
- [Parameters](bigip_device_info_module.md#parameters)
- [Notes](bigip_device_info_module.md#notes)
- [Examples](bigip_device_info_module.md#examples)
- [Return Values](bigip_device_info_module.md#return-values)

## [Synopsis](bigip_device_info_module.md#id1)

- Collect information from F5 BIG-IP devices.
- This module was called `bigip_device_facts` before Ansible 2.9. The usage did not change.

## [Parameters](bigip_device_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **gather_subset**  aliases: include  list / elements=string / required | When supplied, this argument will restrict the information returned to a given subset.  You can specify a list of values to include a larger subset.  Values can also be used with an initial `!` to specify that a specific subset should not be collected.  Choices:   - `"all"` - `"monitors"` - `"profiles"` - `"apm-access-profiles"` - `"apm-access-policies"` - `"as3"` - `"asm-policy-stats"` - `"asm-policies"` - `"asm-server-technologies"` - `"asm-signature-sets"` - `"client-ssl-profiles"` - `"cfe"` - `"devices"` - `"device-groups"` - `"do"` - `"external-monitors"` - `"fasthttp-profiles"` - `"fastl4-profiles"` - `"gateway-icmp-monitors"` - `"gtm-pools"` - `"gtm-servers"` - `"gtm-wide-ips"` - `"gtm-a-pools"` - `"gtm-a-wide-ips"` - `"gtm-aaaa-pools"` - `"gtm-aaaa-wide-ips"` - `"gtm-cname-pools"` - `"gtm-cname-wide-ips"` - `"gtm-mx-pools"` - `"gtm-mx-wide-ips"` - `"gtm-naptr-pools"` - `"gtm-naptr-wide-ips"` - `"gtm-srv-pools"` - `"gtm-srv-wide-ips"` - `"gtm-topology-regions"` - `"http-monitors"` - `"https-monitors"` - `"http-profiles"` - `"iapp-services"` - `"iapplx-packages"` - `"icmp-monitors"` - `"interfaces"` - `"internal-data-groups"` - `"irules"` - `"ltm-pools"` - `"ltm-policies"` - `"management-routes"` - `"nodes"` - `"oneconnect-profiles"` - `"packages"` - `"partitions"` - `"provision-info"` - `"remote-syslog"` - `"route-domains"` - `"self-ips"` - `"server-ssl-profiles"` - `"software-volumes"` - `"software-images"` - `"software-hotfixes"` - `"ssl-certs"` - `"ssl-keys"` - `"sync-status"` - `"system-db"` - `"system-info"` - `"ts"` - `"tcp-monitors"` - `"tcp-half-open-monitors"` - `"tcp-profiles"` - `"traffic-groups"` - `"trunks"` - `"udp-profiles"` - `"users"` - `"ucs"` - `"vcmp-guests"` - `"virtual-addresses"` - `"virtual-servers"` - `"vlans"` - `"!all"` - `"!as3"` - `"!do"` - `"!ts"` - `"!cfe"` - `"!monitors"` - `"!profiles"` - `"!apm-access-profiles"` - `"!apm-access-policies"` - `"!asm-policy-stats"` - `"!asm-policies"` - `"!asm-server-technologies"` - `"!asm-signature-sets"` - `"!client-ssl-profiles"` - `"!devices"` - `"!device-groups"` - `"!external-monitors"` - `"!fasthttp-profiles"` - `"!fastl4-profiles"` - `"!gateway-icmp-monitors"` - `"!gtm-pools"` - `"!gtm-servers"` - `"!gtm-wide-ips"` - `"!gtm-a-pools"` - `"!gtm-a-wide-ips"` - `"!gtm-aaaa-pools"` - `"!gtm-aaaa-wide-ips"` - `"!gtm-cname-pools"` - `"!gtm-cname-wide-ips"` - `"!gtm-mx-pools"` - `"!gtm-mx-wide-ips"` - `"!gtm-naptr-pools"` - `"!gtm-naptr-wide-ips"` - `"!gtm-srv-pools"` - `"!gtm-srv-wide-ips"` - `"!gtm-topology-regions"` - `"!http-monitors"` - `"!https-monitors"` - `"!http-profiles"` - `"!iapp-services"` - `"!iapplx-packages"` - `"!icmp-monitors"` - `"!interfaces"` - `"!internal-data-groups"` - `"!irules"` - `"!ltm-pools"` - `"!ltm-policies"` - `"!management-routes"` - `"!nodes"` - `"!oneconnect-profiles"` - `"!packages"` - `"!partitions"` - `"!provision-info"` - `"!remote-syslog"` - `"!route-domains"` - `"!self-ips"` - `"!server-ssl-profiles"` - `"!software-volumes"` - `"!software-images"` - `"!software-hotfixes"` - `"!ssl-certs"` - `"!ssl-keys"` - `"!sync-status"` - `"!system-db"` - `"!system-info"` - `"!tcp-monitors"` - `"!tcp-half-open-monitors"` - `"!tcp-profiles"` - `"!traffic-groups"` - `"!trunks"` - `"!udp-profiles"` - `"!users"` - `"!ucs"` - `"!vcmp-guests"` - `"!virtual-addresses"` - `"!virtual-servers"` - `"!vlans"` |
| **partition**  string  added in f5networks.f5_modules 1.14.0 | Specifies the partition to gather the resource information from.  The default value for the partition is taken as Common.  Default: `"Common"` |
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

## [Notes](bigip_device_info_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_device_info_module.md#id4)

```yaml+jinja
- name: Collect BIG-IP information
  bigip_device_info:
    gather_subset:
      - interfaces
      - vlans
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Collect all BIG-IP information
  bigip_device_info:
    gather_subset:
      - all
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost

- name: Collect all BIG-IP information except trunks
  bigip_device_info:
    gather_subset:
      - all
      - "!trunks"
    provider:
      server: lb.mydomain.com
      user: admin
      password: secret
  delegate_to: localhost
```

## [Return Values](bigip_device_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **apm_access_policies**  complex | Information about APM Access Policies.  Returned: When `apm-access-policies` is specified in `gather_subset`. |
| **full_path**  string | Full name of the resource as known to the BIG-IP.  Returned: queried  Sample: `"/Common/foo_policy"` |
| **name**  string | Relative name of the resource in the BIG-IP.  Returned: queried  Sample: `"foo_policy"` |
| **apm_access_profiles**  complex | Information about APM Access Profiles.  Returned: When `apm-access-profiles` is specified in `gather_subset`. |
| **access_policy**  string | APM Access Policy attached to this Access Profile.  Returned: queried  Sample: `"foo_policy"` |
| **full_path**  string | Full name of the resource as known to the BIG-IP.  Returned: queried  Sample: `"/Common/foo_policy"` |
| **name**  string | Relative name of the resource in the BIG-IP.  Returned: queried  Sample: `"foo_policy"` |
| **asm_policies**  complex | Detailed information for ASM policies present on device.  Returned: When `asm-policies` is specified in `gather_subset`.  Sample: `"hash/dictionary of values"` |
| **active**  boolean | Indicates if an ASM policy is active. In TMOS 13.x and above, this setting indicates if the policy is bound to any Virtual Server.  Returned: queried  Sample: `true` |
| **allowed_response_codes**  list / elements=string | Lists the response status codes between 400 and 599 that the security profile considers legal.  Returned: queried  Sample: `["400", "404"]` |
| **application_language**  string | The language encoding for the web application.  Returned: queried  Sample: `"utf-8"` |
| **apply**  boolean | In TMOS 13.x and above, this setting indicates if an ASM policy has pending changes that need to be applied.  Returned: queried  Sample: `true` |
| **case_insensitive**  boolean | Indicates if the ASM policy treats file types, URLs, and parameters as case sensitive.  Returned: queried  Sample: `true` |
| **csrf_protection_enabled**  boolean | Specifies if CSRF protection is active on the ASM policy.  Returned: queried  Sample: `true` |
| **csrf_protection_expiration_time_in_seconds**  integer | Specifies how long, in seconds, a configured CSRF token is valid before it expires.  Returned: queried  Sample: `600` |
| **csrf_protection_ssl_only**  boolean | Specifies that only HTTPS URLs will be checked for CSRF protection.  Returned: queried  Sample: `true` |
| **csrf_urls**  complex | Specifies a list of URLs for CSRF token verification.  In version 13.0.0 and later, this has become a sub-collection and a list of dictionaries.  In version 12.x, this is a list of simple strings.  Returned: queried |
| **csrf_url**  string | Specifies an URL to protect.  Returned: queried  Sample: `"['/foo.html']"` |
| **csrf_url_enforcement_action**  string | Indicates the action specified for the system to take when the URL entry matches.  Returned: queried  Sample: `"none"` |
| **csrf_url_id**  string | Specifies the generated ID for the configured CSRF URL resource.  Returned: queried  Sample: `"l0Ckxe-7yHsXp8U5tTgbFQ"` |
| **csrf_url_method**  string | Method for the specified URL.  Returned: queried  Sample: `"POST"` |
| **csrf_url_parameters_list**  list / elements=string | List of parameters to look for in a request when checking if the URL entry matches the request.  Returned: queried  Sample: `["fooparam"]` |
| **csrf_url_required_parameters**  string | Indicates whether to ignore or require one of the specified parameters is present in a request when checking if the URL entry matches the request.  Returned: queried  Sample: `"ignore"` |
| **csrf_url_wildcard_order**  string | Specifies the order in which the wildcard URLs are enforced.  Returned: queried  Sample: `"1"` |
| **custom_xff_headers**  string | List of custom XFF headers trusted by the system.  Returned: queried  Sample: `"asm-proxy1"` |
| **description**  string | Description of the resource.  Returned: queried  Sample: `"Significant Policy Description"` |
| **disallowed_geolocations**  string | Displays countries that may not access the web application.  Returned: queried  Sample: `"Argentina"` |
| **enforcement_mode**  string | Specifies whether blocking is active or inactive for the ASM policy.  Returned: queried  Sample: `"blocking"` |
| **enforcement_readiness_period**  integer | Period in days both security policy entities and attack signatures remain in staging mode before the system suggests to enforce them.  Returned: queried  Sample: `8` |
| **full_path**  string | Full name of the resource as known to the BIG-IP.  Returned: queried  Sample: `"/Common/foo_policy"` |
| **has_parent**  boolean | Indicates if the ASM policy is a child of another ASM policy.  Returned: queried  Sample: `false` |
| **inspect_http_uploads**  boolean | Specifies whether the system should inspect all HTTP uploads.  Returned: queried  Sample: `true` |
| **learning_mode**  string | Determine how the policy is built.  Returned: queried  Sample: `"manual"` |
| **manual_virtual_servers**  list / elements=string | The virtual servers that have Advanced LTM policy configuration which, in turn, have rule(s) built with ASM control actions enabled.  Returned: queried  Sample: `["/Common/test_VS/"]` |
| **mask_credit_card_numbers_in_request**  boolean | Indicates if the system masks credit card numbers.  Returned: queried  Sample: `false` |
| **maximum_cookie_header_length**  integer | Maximum length of a cookie header name and value that the system processes.  Returned: queried  Sample: `8192` |
| **maximum_http_header_length**  integer | Maximum length of an HTTP header name and value that the system processes.  Returned: queried  Sample: `8192` |
| **name**  string | Relative name of the resource in the BIG-IP.  Returned: queried  Sample: `"foo_policy"` |
| **path_parameter_handling**  string | Specifies how the system handles path parameters that are attached to path segments in URIs.  Returned: queried  Sample: `"ignore"` |
| **place_signatures_in_staging**  boolean | Specifies if the system places new or updated signatures in staging for the number of days specified in the enforcement readiness period.  Returned: queried  Sample: `false` |
| **policy_id**  string | Generated ID of the ASM policy resource.  Returned: queried  Sample: `"l0Ckxe-7yHsXp8U5tTgbFQ"` |
| **protocol_independent**  boolean | Indicates if the ASM policy differentiates between HTTP/WS and HTTPS/WSS URLs.  Returned: queried  Sample: `false` |
| **signature_staging**  boolean | Specifies if the staging feature is active on the ASM policy.  Returned: queried  Sample: `true` |
| **trigger_asm_irule_event**  string | Indicates if iRule event is enabled.  Returned: queried  Sample: `"disabled"` |
| **trust_xff**  boolean | Indicates the system has confidence in an XFF (X-Forwarded-For) header in the request.  Returned: queried  Sample: `true` |
| **type**  string | The type of policy, can be `Security` or `Parent`.  Returned: queried  Sample: `"security"` |
| **use_dynamic_session_id_in_url**  boolean | Specifies how the security policy processes URLs that use dynamic sessions.  Returned: queried  Sample: `false` |
| **virtual_servers**  list / elements=string | Virtual server or servers which have this policy assigned to them.  Returned: queried  Sample: `["/Common/foo_VS/"]` |
| **asm_policy_stats**  complex | Miscellaneous ASM policy related information.  Returned: When `asm-policy-stats` is specified in `gather_subset`.  Sample: `"hash/dictionary of values"` |
| **parent_policies**  integer | The total number of ASM parent policies on the device.  Returned: queried  Sample: `2` |
| **policies**  integer | The total number of ASM policies on the device.  Returned: queried  Sample: `3` |
| **policies_active**  integer | The number of ASM policies that are marked as active. From TMOS 13.x and above this setting equals to `policies_attached`.  Returned: queried  Sample: `3` |
| **policies_attached**  integer | The number of ASM policies that are attached to virtual servers.  Returned: queried  Sample: `1` |
| **policies_inactive**  integer | The number of ASM policies that are marked as inactive. From TMOS 13.x and above this setting equals to `policies_unattached`.  Returned: queried  Sample: `0` |
| **policies_pending_changes**  integer | The total number of ASM policies with pending changes on the device.  Returned: queried  Sample: `2` |
| **policies_unattached**  integer | The number of ASM policies that are not attached to a virtual server.  Returned: queried  Sample: `3` |
| **asm_server_technologies**  complex | Detailed information for ASM server technologies present on the device.  Returned: When `asm-server-technologies` is specified in `gather_subset`.  Sample: `"hash/dictionary of values"` |
| **id**  string | Displays the generated ID for the server technology resource.  Returned: queried  Sample: `"l0Ckxe-7yHsXp8U5tTgbFQ"` |
| **server_technology_name**  string | Friendly name of the server technology resource.  Returned: queried  Sample: `"Wordpress"` |
| **server_technology_references**  complex | List of dictionaries containing API self links of the associated technology resources.  Returned: queried |
| **link**  string | A self link to an associated server technology.  Returned: queried  Sample: `"https://localhost/mgmt/tm/asm/server-technologies/NQG7CT02OBC2cQWbnP7T-A?ver=13.1.0"` |
| **asm_signature_sets**  complex | Detailed information for ASM signature sets present on device.  Returned: When `asm-signature-sets` is specified in `gather_subset`.  Sample: `"hash/dictionary of values"` |
| **assign_to_policy_by_default**  boolean | Indicates whether the system assigns this signature set to a new created security policy by default.  Returned: queried  Sample: `true` |
| **category**  string | Displays the category of the signature set.  Returned: queried  Sample: `"filter-based"` |
| **default_alarm**  boolean | Displays whether the security policy logs the request data in the Statistics screen if a request matches a signature that is included in the signature set.  Returned: queried  Sample: `true` |
| **default_block**  boolean | When the security policy enforcement mode is Blocking, displays how the system treats requests that match a signature included in the signature set.  Returned: queried  Sample: `true` |
| **default_learn**  boolean | Displays whether the security policy learns all requests that match a signature that is included in the signature set.  Returned: queried  Sample: `true` |
| **id**  string | Displays the generated ID for the signature set resource.  Returned: queried  Sample: `"l0Ckxe-7yHsXp8U5tTgbFQ"` |
| **is_user_defined**  boolean | Specifies this signature set was added by a user.  Returned: queried  Sample: `false` |
| **name**  string | Name of the signature set.  Returned: queried  Sample: `"WebSphere signatures"` |
| **type**  string | The method used to select signatures to be a part of the signature set.  Returned: queried  Sample: `"filter-based"` |
| **client_ssl_profiles**  complex | Client SSL Profile related information.  Returned: When `client-ssl-profiles` is specified in `gather_subset`.  Sample: `"hash/dictionary of values"` |
| **alert_timeout**  integer | Maximum time period, in seconds, to keep the SSL session active after an alert message is sent, or indefinite.  Returned: queried  Sample: `0` |
| **allow_non_ssl**  boolean | Enables or disables non-SSL connections.  Returned: queried  Sample: `true` |
| **authenticate_depth**  integer | Specifies the authenticate depth. This is the client certificate chain maximum traversal depth.  Returned: queried  Sample: `9` |
| **authenticate_frequency**  string | Specifies how often the system authenticates a user.  Returned: queried  Sample: `"once"` |
| **ca_file**  string | Specifies the certificate authority (CA) file name.  Returned: queried  Sample: `"/Common/default-ca.crt"` |
| **cache_size**  integer | Specifies the SSL session cache size.  Returned: queried  Sample: `262144` |
| **cache_timeout**  integer | Specifies the SSL session cache timeout value.  Returned: queried  Sample: `3600` |
| **certificate_file**  string | Specifies the name of the certificate installed on the traffic management system for the purpose of terminating or initiating an SSL connection.  Returned: queried  Sample: `"/Common/default.crt"` |
| **chain_file**  string | Specifies or builds a certificate chain file that a client can use to authenticate the profile.  Returned: queried  Sample: `"/Common/ca-chain.crt"` |
| **ciphers**  string | Specifies a list of cipher names.  Returned: queried  Sample: `"['DEFAULT']"` |
| **crl_file**  string | Specifies the certificate revocation list file name.  Returned: queried  Sample: `"/Common/default.crl"` |
| **description**  string | Description of the profile.  Returned: queried  Sample: `"My profile"` |
| **forward_proxy_ca_certificate_file**  string | Specifies the name of the certificate file that is used as the certification authority certificate when SSL forward proxy feature is enabled.  Returned: queried |
| **forward_proxy_ca_key_file**  string | Specifies the name of the key file that is used as the certification authority key when SSL forward proxy feature is enabled.  Returned: queried |
| **forward_proxy_ca_passphrase**  string | Specifies the passphrase of the key file that is used as the certification authority key when SSL forward proxy feature is enabled.  Returned: queried |
| **forward_proxy_certificate_extension_include**  list / elements=string | Specifies the extensions of the web server certificates to be included in the generated certificates using SSL Forward Proxy.  Returned: queried  Sample: `["basic-constraints", "subject-alternative-name"]` |
| **forward_proxy_certificate_lifespan**  integer | Specifies the lifespan of the certificate generated using the SSL forward proxy feature.  Returned: queried  Sample: `30` |
| **forward_proxy_enabled**  boolean | Enables or disables SSL forward proxy feature.  Returned: queried  Sample: `true` |
| **forward_proxy_lookup_by_ipaddr_port**  boolean | Specifies whether to perform certificate look up by IP address and port number.  Returned: queried  Sample: `false` |
| **full_path**  string | Full name of the resource as known to the BIG-IP.  Returned: queried  Sample: `"/Common/bigip02.internal"` |
| **handshake_timeout**  integer | Specifies the handshake timeout in seconds.  Returned: queried  Sample: `10` |
| **key_file**  string | Specifies the name of the key installed on the traffic management system for the purpose of terminating or initiating an SSL connection.  Returned: queried  Sample: `"/Common/default.key"` |
| **modssl_methods**  boolean | Enables or disables ModSSL method emulation.  Returned: queried  Sample: `false` |
| **name**  string | Relative name of the resource in the BIG-IP.  Returned: queried  Sample: `"bigip02.internal"` |
| **parent**  string | Parent of the profile  Returned: queried  Sample: `"/Common/clientssl"` |
| **peer_certification_mode**  string | Specifies the peer certificate mode.  Returned: queried  Sample: `"ignore"` |
| **profile_mode_enabled**  boolean | Specifies the profile mode, which enables or disables SSL processing.  Returned: queried  Sample: `true` |
| **renegotiation**  boolean | Specifies whether renegotiations are enabled.  Returned: queried  Sample: `true` |
| **renegotiation_maximum_record_delay**  integer | Maximum number of SSL records that the traffic management system can receive before it renegotiates an SSL session.  Returned: queried  Sample: `0` |
| **renegotiation_period**  integer | Number of seconds required to renegotiate an SSL session.  Returned: queried  Sample: `0` |
| **retain_certificate**  boolean | APM module requires storing certificate in SSL session. When `no`, certificate will not be stored in SSL session.  Returned: queried  Sample: `true` |
| **secure_renegotiation_mode**  string | Specifies the secure renegotiation mode.  Returned: queried  Sample: `"require"` |
| **server_name**  string | Specifies the server names to be matched with SNI (server name indication) extension information in ClientHello from a client connection.  Returned: queried  Sample: `"bigip01"` |
| **session_ticket**  boolean | Enables or disables session-ticket.  Returned: queried  Sample: `false` |
| **sni_default**  boolean | When `yes`, this profile is the default SSL profile when the server name in a client connection does not match any configured server names, or a client connection does not specify any server name at all.  Returned: queried  Sample: `true` |
| **sni_require**  boolean | When this option is `yes`, a client connection that does not specify a known server name or does not support SNI extension will be rejected.  Returned: queried  Sample: `false` |
| **strict_resume**  boolean | Enables or disables strict-resume.  Returned: queried  Sample: `true` |
| **unclean_shutdown**  boolean | Whether to force the SSL profile to perform a clean shutdown of all SSL connections or not  Returned: queried  Sample: `false` |
| **device_groups**  complex | Device group related information.  Returned: When `device-groups` is specified in `gather_subset`.  Sample: `"hash/dictionary of values"` |
| **asm_sync_enabled**  boolean | Specifies whether to synchronize ASM configurations of device group members.  Returned: queried  Sample: `true` |
| **autosync_enabled**  boolean | Whether the device group automatically synchronizes configuration data to its members.  Returned: queried  Sample: `false` |
| **description**  string | Description of the device group.  Returned: queried  Sample: `"My device group"` |
| **devices**  list / elements=string | List of devices in the group. Devices are listed by their `full_path`.  Returned: queried  Sample: `["/Common/bigip02.internal"]` |
| **full_load_on_sync**  boolean | Specifies the entire configuration for a device group is sent when configuration synchronization is performed.  Returned: queried  Sample: `true` |
| **full_path**  string | Full name of the resource as known to the BIG-IP.  Returned: queried  Sample: `"/Common/fasthttp"` |
| **incremental_config_sync_size_maximum**  integer | Specifies the maximum size (in KB) to devote to incremental config sync cached transactions.  Returned: queried  Sample: `1024` |
| **name**  string | Relative name of the resource in the BIG-IP.  Returned: queried  Sample: `"fasthttp"` |
| **network_failover_enabled**  boolean | Specifies whether network failover is used.  Returned: queried  Sample: `true` |
| **type**  string | Specifies the type of device group.  Returned: queried  Sample: `"sync-only"` |
| **devices**  complex | Device related information.  Returned: When `devices` is specified in `gather_subset`.  Sample: `"hash/dictionary of values"` |
| **active_modules**  list / elements=string | The currently licensed and provisioned modules on the device.  Returned: queried  Sample: `["DNS Services (LAB)", "PSM, VE"]` |
| **base_mac_address**  string | Media Access Control address (MAC address) of the device.  Returned: queried  Sample: `"fa:16:3e:c3:42:6f"` |
| **build**  string | The minor version information of the total product version.  Returned: queried  Sample: `"0.0.1"` |
| **chassis_id**  string | Serial number of the device.  Returned: queried  Sample: `"11111111-2222-3333-444444444444"` |
| **chassis_type**  string | Displays the chassis type. The possible values are `individual` and `viprion`.  Returned: queried  Sample: `"individual"` |
| **comment**  string | User comments about the device.  Returned: queried  Sample: `"My device"` |
| **configsync_address**  string | IP address used for configuration synchronization.  Returned: queried  Sample: `"10.10.10.10"` |
| **contact**  string | Administrator contact information.  Returned: queried  Sample: `"The User"` |
| **description**  string | Description of the device.  Returned: queried  Sample: `"My device"` |
| **edition**  string | Displays the software edition.  Returned: queried  Sample: `"Point Release 7"` |
| **failover_state**  string | Device failover state.  Returned: queried  Sample: `"active"` |
| **full_path**  string | Full name of the resource as known to the BIG-IP.  Returned: queried  Sample: `"/Common/bigip02.internal"` |
| **hostname**  string | Device hostname  Returned: queried  Sample: `"bigip02.internal"` |
| **location**  string | Specifies the physical location of the device.  Returned: queried  Sample: `"London"` |
| **management_address**  string | IP address of the management interface.  Returned: queried  Sample: `"3.3.3.3"` |
| **marketing_name**  string | Marketing name of the device platform.  Returned: queried  Sample: `"BIG-IP Virtual Edition"` |
| **multicast_address**  string | Specifies the multicast IP address used for failover.  Returned: queried  Sample: `"4.4.4.4"` |
| **name**  string | Relative name of the resource in the BIG-IP.  Returned: queried  Sample: `"bigip02.internal"` |
| **optional_modules**  list / elements=string | Modules that are available for the current platform, but are not currently licensed.  Returned: queried  Sample: `["App Mode (TMSH Only, No Root/Bash)", "BIG-IP VE, Multicast Routing"]` |
| **platform_id**  string | Displays the device platform identifier.  Returned: queried  Sample: `"Z100"` |
| **primary_mirror_address**  string | Specifies the IP address used for state mirroring.  Returned: queried  Sample: `"5.5.5.5"` |
| **product**  string | Displays the software product name.  Returned: queried  Sample: `"BIG-IP"` |
| **secondary_mirror_address**  string | Secondary IP address used for state mirroring.  Returned: queried  Sample: `"2.2.2.2"` |
| **self**  boolean | Whether or not this device is the one that was queried for information.  Returned: queried  Sample: `true` |
| **software_version**  string | Displays the software version number.  Returned: queried  Sample: `"13.1.0.7"` |
| **timelimited_modules**  list / elements=string | Displays the licensed modules that are time-limited.  Returned: queried  Sample: `["IP Intelligence, 3Yr, ...", "PEM URL Filtering, 3Yr, ..."]` |
| **timezone**  string | Displays the time zone configured on the device.  Returned: queried  Sample: `"UTC"` |
| **unicast_addresses**  complex | Specifies the entire set of unicast addresses used for failover.  Returned: queried |
| **effective_ip**  string | The IP address that peers can use to reach this unicast address IP.  Returned: queried  Sample: `"5.4.3.5"` |
| **effective_port**  integer | The port that peers can use to reach this unicast address.  Returned: queried  Sample: `1026` |
| **ip**  string | The IP address the failover daemon will listen on for packets from its peers.  Returned: queried  Sample: `"5.4.3.5"` |
| **port**  integer | The IP port the failover daemon uses to accept packets from its peers.  Returned: queried  Sample: `1026` |
| **external_monitors**  complex | External monitor related information.  Returned: When `external-monitors` is specified in `gather_subset`.  Sample: `"hash/dictionary of values"` |
| **args**  string | Specifies any command-line arguments the script requires.  Returned: queried  Sample: `"arg1 arg2 arg3"` |
| **description**  string | Description of the resource.  Returned: queried  Sample: `"My monitor"` |
| **destination**  string | Specifies the IP address and service port of the resource that is the destination of this monitor.  Returned: queried  Sample: `"*:*"` |
| **external_program**  string | Specifies the name of the file for the monitor to use.  Returned: queried  Sample: `"/Common/arg_example"` |
| **full_path**  string | Full name of the resource as known to the BIG-IP.  Returned: queried  Sample: `"/Common/external"` |
| **interval**  integer | Specifies, in seconds, the frequency at which the system issues the monitor check when either the resource is down or the status of the resource is unknown.  Returned: queried  Sample: `5` |
| **manual_resume**  boolean | Specifies whether the system automatically changes the status of a resource to **up** at the next successful monitor check.  Returned: queried  Sample: `true` |
| **name**  string | Relative name of the resource in the BIG-IP.  Returned: queried  Sample: `"external"` |
| **parent**  string | Profile from which this profile inherits settings.  Returned: queried  Sample: `"external"` |
| **time_until_up**  integer | Specifies the amount of time, in seconds, after the first successful response before a node is marked up.  Returned: queried  Sample: `0` |
| **timeout**  integer | Specifies the number of seconds the target has in which to respond to the monitor request.  Returned: queried  Sample: `16` |
| **up_interval**  integer | Specifies, in seconds, the frequency at which the system issues the monitor check when the resource is up.  Returned: queried  Sample: `0` |
| **variables**  dictionary | Specifies any variables the script requires.  Returned: success  Sample: `{"key1": "val", "key_2": "val 2"}` |
| **fasthttp_profiles**  complex | FastHTTP profile related information.  Returned: When `fasthttp-profiles` is specified in `gather_subset`.  Sample: `"hash/dictionary of values"` |
| **client_close_timeout**  integer | Number of seconds after which the system closes a client connection, when the system either receives a client FIN packet or sends a FIN packet to the client.  Returned: queried  Sample: `5` |
| **description**  string | Description of the resource.  Returned: queried  Sample: `"My profile"` |
| **force_http_1_0_response**  boolean | When `yes`, specifies the server sends responses to clients in the HTTP/1.0 format.  Returned: queried  Sample: `false` |
| **full_path**  string | Full name of the resource as known to the BIG-IP.  Returned: queried  Sample: `"/Common/fasthttp"` |
| **http_1_1_close_workarounds**  boolean | When `yes`, specifies the server uses workarounds for HTTP 1.1 close issues.  Returned: queried  Sample: `false` |
| **idle_timeout**  integer | Length of time that a connection is idle (has no traffic) before the connection is eligible for deletion.  Returned: queried  Sample: `300` |
| **insert_xforwarded_for**  boolean | Whether the system inserts the X-Forwarded-For header in an HTTP request with the client IP address, to use with connection pooling.  Returned: queried  Sample: `false` |
| **maximum_header_size**  integer | Maximum amount of HTTP header data the system buffers before making a load balancing decision.  Returned: queried  Sample: `32768` |
| **maximum_requests**  integer | Maximum number of requests the system can receive on a client-side connection, before the system closes the connection.  Returned: queried  Sample: `0` |
| **maximum_segment_size_override**  integer | Maximum segment size (MSS) override for server-side connections.  Returned: queried  Sample: `0` |
| **name**  string | Relative name of the resource in the BIG-IP.  Returned: queried  Sample: `"fasthttp"` |
| **oneconnect_idle_timeout_override**  integer | Number of seconds after which a server-side connection in a OneConnect pool is eligible for deletion, when the connection has no traffic.  Returned: queried  Sample: `0` |
| **oneconnect_maximum_pool_size**  integer | Maximum number of connections to a load balancing pool.  Returned: queried  Sample: `2048` |
| **oneconnect_maximum_reuse**  integer | Maximum number of times the system can re-use a current connection.  Returned: queried  Sample: `0` |
| **oneconnect_minimum_pool_size**  integer | Minimum number of connections to a load balancing pool.  Returned: queried  Sample: `0` |
| **oneconnect_ramp_up_increment**  integer | The increment in which the system makes additional connections available, when all available connections are in use.  Returned: queried  Sample: `4` |
| **oneconnect_replenish’**  boolean | When `yes`, specifies the system will not keep a steady-state maximum of connections to the back-end, unless the number of connections to the pool have dropped beneath the `minimum_pool_size` specified in the profile.  Returned: queried  Sample: `true` |
| **parent**  string | Profile from which this profile inherits settings.  Returned: queried  Sample: `"fasthttp"` |
| **receive_window_size**  integer | Amount of data the BIG-IP system can accept without acknowledging the server.  Returned: queried  Sample: `0` |
| **request_header_insert**  string | A string the system inserts as a header in an HTTP request. If the header already exists, the system does not replace it.  Returned: queried  Sample: `"X-F5-Authentication: foo"` |
| **reset_on_timeout**  boolean | When `yes`, specifies the system sends a reset packet (RST) in addition to deleting the connection, when a connection exceeds the idle timeout value.  Returned: queried  Sample: `true` |
| **server_close_timeout**  integer | Number of seconds after which the system closes a client connection, when the system either receives a server FIN packet or sends a FIN packet to the server.  Returned: queried  Sample: `5` |
| **server_sack**  boolean | Whether the BIG-IP system processes Selective ACK (Sack) packets in cookie responses from the server.  Returned: queried  Sample: `false` |
| **server_timestamp**  boolean | Whether the BIG-IP system processes timestamp request packets in cookie responses from the server.  Returned: queried  Sample: `false` |
| **unclean_shutdown**  string | How the system handles closing connections. Values provided may be `enabled`, `disabled`, or `fast`.  Returned: queried  Sample: `"enabled"` |
| **fastl4_profiles**  complex | FastL4 profile related information.  Returned: When `fastl4-profiles` is specified in `gather_subset`.  Sample: `"hash/dictionary of values"` |
| **client_timeout**  integer | Specifies late binding client timeout in seconds.  This is the number of seconds allowed for a client to transmit enough data to select a server pool.  If this timeout expires, the timeout-recovery option dictates whether to drop the connection or fallback to the normal FastL4 load balancing method to pick a server pool.  Returned: queried  Sample: `30` |
| **description**  string | Description of the resource.  Returned: queried  Sample: `"My profile"` |
| **dont_fragment_flag**  string | Describes the Don’t Fragment (DF) bit setting in the IP Header of the outgoing TCP packet.  When `pmtu`, sets the outgoing IP Header DF bit based on the IP pmtu setting(tm.pathmtudiscovery).  When `preserve`, sets the outgoing packet’s IP Header DF bit to be the same as the incoming IP Header DF bit.  When `set`, sets the outgoing packet’s IP Header DF bit.  When `clear`, clears the outgoing packet’s IP Header DF bit.  Returned: queried  Sample: `"pmtu"` |
| **explicit_flow_migration**  boolean | Specifies whether to have the iRule code determine exactly when the FIX stream drops down to the ePVA hardware.  Returned: queried  Sample: `true` |
| **full_path**  string | Full name of the resource as known to the BIG-IP.  Returned: queried  Sample: `"/Common/fastl4"` |
| **generate_init_seq_number**  boolean | Specifies whether you want to generate TCP sequence numbers on all SYNs that conform with RFC1948, and allow timestamp recycling.  Returned: queried  Sample: `true` |
| **hardware_syn_cookie**  boolean | Enables or disables hardware SYN cookie support when PVA10 is present on the system.  This option is deprecated in version 13.0.0 and is replaced by `syn-cookie-enable`.  Returned: queried  Sample: `false` |
| **idle_timeout**  integer | Specifies the number of seconds a connection is idle before the connection is eligible for deletion.  Values are in the range of 0 to 4294967295 (inclusive).  `0` is equivalent to the TMUI value “immediate”.  `4294967295` is equivalent to the TMUI value “indefinite”.  Returned: queried  Sample: `300` |
| **ip_tos_to_client**  string | Specifies an IP Type of Service (ToS) number for the client-side.  This option specifies the ToS level the traffic management system assigns to IP packets when sending them to clients.  Returned: queried  Sample: `"200"` |
| **ip_tos_to_server**  string | Specifies an IP ToS number for the server side.  This option specifies the ToS level the traffic management system assigns to IP packets when sending them to servers.  Returned: queried  Sample: `"pass-through"` |
| **keep_alive_interval**  integer | Specifies the keep-alive probe interval, in seconds.  A value of 0 indicates keep-alive is disabled.  Returned: queried  Sample: `10` |
| **late_binding**  boolean | Specifies whether to enable or disable the intelligent selection of a back-end server pool.  Returned: queried  Sample: `true` |
| **link_qos_to_client**  integer | Specifies a Link Quality of Service (QoS) (VLAN priority) number for the client side.  This option specifies the QoS level the system assigns to packets when sending them to clients.  Returned: queried  Sample: `7` |
| **link_qos_to_server**  integer | Specifies a Link QoS (VLAN priority) number for the server side.  This option specifies the QoS level the system assigns to packets when sending them to servers.  Returned: queried  Sample: `5` |
| **loose_close**  boolean | Specifies the system closes a loosely-initiated connection when it receives the first FIN packet from either the client or the server.  Returned: queried  Sample: `false` |
| **loose_init**  boolean | Specifies the system initializes a connection when it receives any Transmission Control Protocol (TCP) packet, rather than requiring a SYN packet for connection initiation.  Returned: queried  Sample: `true` |
| **mss_override**  integer | Specifies a maximum segment size (MSS) override for server connections. Note this is also the MSS advertised to a client when a client first connects.  `0` (zero), means the option is disabled. Otherwise, the value will be between 256 and 9162.  Returned: queried  Sample: `500` |
| **name**  string | Relative name of the resource in the BIG-IP.  Returned: queried  Sample: `"fastl4"` |
| **parent**  string | Profile from which this profile inherits settings.  Returned: queried  Sample: `"fastl4"` |
| **priority_to_client**  integer | Specifies the internal packet priority for the client side.  This option specifies the internal packet priority the system assigns to packets when sending them to clients.  Returned: queried  Sample: `300` |
| **priority_to_server**  integer | Specifies the internal packet priority for the server side.  This option specifies the internal packet priority the system assigns to packets when sending them to servers.  Returned: queried  Sample: `200` |
| **pva_acceleration**  string | Specifies the Packet Velocity(r) ASIC acceleration policy.  Returned: queried  Sample: `"full"` |
| **pva_dynamic_client_packets**  integer | Specifies the number of client packets before dynamic ePVA hardware re-offloading occurs.  Values are between 0 and 10.  Returned: queried  Sample: `8` |
| **pva_dynamic_server_packets**  integer | Specifies the number of server packets before dynamic ePVA hardware re-offloading occurs.  Values are between 0 and 10.  Returned: queried  Sample: `5` |
| **pva_flow_aging**  boolean | Specifies if automatic aging from ePVA flow cache is enabled or not.  Returned: queried  Sample: `true` |
| **pva_flow_evict**  boolean | Specifies if this flow can be evicted upon hash collision with a new flow learn snoop request.  Returned: queried  Sample: `false` |
| **pva_offload_dynamic**  boolean | Specifies whether PVA flow dynamic offloading is enabled or not.  Returned: queried  Sample: `true` |
| **pva_offload_state**  string | Specifies at what stage the ePVA performs hardware offload.  When `embryonic`, applies at TCP CSYN or the first client UDP packet.  When `establish`, applies TCP 3WAY handshaking or UDP CS round trip are confirmed.  Returned: queried  Sample: `"embryonic"` |
| **reassemble_fragments**  boolean | Specifies whether to reassemble fragments.  Returned: queried  Sample: `true` |
| **receive_window**  integer | Specifies the window size to use, in bytes.  The maximum is 2^31 for window scale enabling.  Returned: queried  Sample: `1000` |
| **reset_on_timeout**  boolean | Specifies whether you want to reset connections on timeout.  Returned: queried  Sample: `true` |
| **rtt_from_client**  boolean | Enables or disables the TCP timestamp options to measure the round trip time to the client.  Returned: queried  Sample: `false` |
| **rtt_from_server**  boolean | Enables or disables the TCP timestamp options to measure the round trip time to the server.  Returned: queried  Sample: `true` |
| **server_sack**  boolean | Specifies whether to support the server sack option in cookie responses by default.  Returned: queried  Sample: `false` |
| **server_timestamp**  boolean | Specifies whether to support the server timestamp option in cookie responses by default.  Returned: queried  Sample: `true` |
| **software_syn_cookie**  boolean | Enables or disables software SYN cookie support when PVA10 is not present on the system.  This option is deprecated in version 13.0.0 and is replaced by `syn_cookie_enabled`.  Returned: queried  Sample: `true` |
| **strip_sack**  boolean | Specifies whether you want to block the TCP SackOK option from passing to the server on an initiating SYN.  Returned: queried  Sample: `true` |
| **syn_cookie_enabled**  boolean | Enables syn-cookies capability on this virtual server.  Returned: queried  Sample: `false` |
| **syn_cookie_mss**  integer | Specifies a maximum segment size (MSS) for server connections when SYN Cookie is enabled.  Returned: queried  Sample: `2000` |
| **syn_cookie_whitelist**  boolean | Specifies whether or not to use a SYN Cookie WhiteList when doing software SYN Cookies.  Returned: queried  Sample: `false` |
| **tcp_close_timeout**  integer | Specifies a TCP close timeout in seconds.  Returned: queried  Sample: `100` |
| **tcp_handshake_timeout**  integer | Specifies a TCP handshake timeout in seconds.  Returned: queried  Sample: `5` |
| **tcp_time_wait_timeout**  integer | Specifies a TCP time_wait timeout in milliseconds.  Returned: queried  Sample: `60` |
| **tcp_timestamp_mode**  string | Specifies how you want to handle the TCP timestamp.  Returned: queried  Sample: `"preserve"` |
| **tcp_window_scale_mode**  string | Specifies how you want to handle the TCP window scale.  Returned: queried  Sample: `"preserve"` |
| **timeout_recovery**  string | Specifies late binding timeout recovery mode. This is the action to take when late binding timeout occurs on a connection.  When `disconnect`, only the L7 iRule actions are acceptable to pick a server.  When `fallback`, the normal FastL4 load balancing methods are acceptable to pick a server.  Returned: queried  Sample: `"fallback"` |
| **ttl_mode**  string | Describes the outgoing TCP packet’s IP Header TTL mode.  When `proxy`, sets the outgoing IP Header TTL value to 255/64 for IPv4/IPv6 respectively.  When `preserve`, sets the outgoing IP Header TTL value to be same as the incoming IP Header TTL value.  When `decrement`, sets the outgoing IP Header TTL value to be one less than the incoming TTL value.  When `set`, sets the outgoing IP Header TTL value to a specific value (as specified by `ttl_v4` or `ttl_v6`.  Returned: queried  Sample: `"preserve"` |
| **ttl_v4**  integer | Specifies the outgoing packet’s IP Header TTL value for IPv4 traffic.  Maximum value is 255.  Returned: queried  Sample: `200` |
| **ttl_v6**  integer | Specify the outgoing packet’s IP Header TTL value for IPv6. traffic.  Maximum value is 255.  Returned: queried  Sample: `300` |
| **gateway_icmp_monitors**  complex | Gateway ICMP monitor related information.  Returned: When `gateway-icmp-monitors` is specified in `gather_subset`.  Sample: `"hash/dictionary of values"` |
| **adaptive**  boolean | Whether adaptive response time monitoring is enabled for this monitor.  Returned: queried  Sample: `false` |
| **adaptive_divergence_type**  string | Specifies whether the adaptive-divergence-value is `relative` or `absolute`.  Returned: queried  Sample: `"relative"` |
| **adaptive_divergence_value**  integer | Specifies how far from mean latency each monitor probe is allowed to be.  Returned: queried  Sample: `25` |
| **adaptive_limit**  integer | Specifies the hard limit, in milliseconds, which the probe is not allowed to exceed, regardless of the divergence value.  Returned: queried  Sample: `200` |
| **adaptive_sampling_timespan**  integer | Specifies the size of the sliding window, in seconds, which records probe history.  Returned: queried  Sample: `300` |
| **description**  string | Description of the resource.  Returned: queried  Sample: `"My monitor"` |
| **destination**  string | Specifies the IP address and service port of the resource that is the destination of this monitor.  Returned: queried  Sample: `"*:*"` |
| **full_path**  string | Full name of the resource as known to the BIG-IP.  Returned: queried  Sample: `"/Common/gateway_icmp"` |
| **interval**  integer | Specifies, in seconds, the frequency at which the system issues the monitor check when either the resource is down or the status of the resource is unknown.  Returned: queried  Sample: `5` |
| **manual_resume**  boolean | Specifies whether the system automatically changes the status of a resource to (B)up at the next successful monitor check.  Returned: queried  Sample: `true` |
| **name**  string | Relative name of the resource in the BIG-IP.  Returned: queried  Sample: `"gateway_icmp"` |
| **parent**  string | Profile from which this profile inherits settings.  Returned: queried  Sample: `"gateway_icmp"` |
| **time_until_up**  integer | Specifies the amount of time, in seconds, after the first successful response before a node is marked up.  Returned: queried  Sample: `0` |
| **timeout**  integer | Specifies the number of seconds the target has in which to respond to the monitor request.  Returned: queried  Sample: `16` |
| **transparent**  boolean | Specifies whether the monitor operates in transparent mode.  Returned: queried  Sample: `false` |
| **up_interval**  integer | Specifies, in seconds, the frequency at which the system issues the monitor check when the resource is up.  Returned: queried  Sample: `0` |
| **gtm_pools**  complex | GTM pool related information.  Every “type” of pool has the exact same list of possible information. Therefore, the list of information here is presented once instead of 6 times.  Returned: When any of `gtm-pools` or `gtm-*-pools` is specified in `gather_subset`.  Sample: `"hash/dictionary of values"` |
| **alternate_mode**  string | The load balancing mode the system uses to load balance name resolution requests among the members of the pool.  Returned: queried  Sample: `"drop-packet"` |
| **disabled**  boolean | Specifies the pool is disabled.  Returned: queried |
| **dynamic_ratio**  boolean | Specifies whether the dynamic ratio load balancing algorithm is enabled for this pool.  Returned: queried  Sample: `true` |
| **enabled**  boolean | Specifies the pool is enabled.  Returned: queried |
| **fallback_mode**  string | Specifies the load balancing mode the system uses to load balance name resolution among the pool members if the preferred and alternate modes are unsuccessful in picking a pool.  Returned: queried |
| **full_path**  string | Full name of the resource as known to the BIG-IP.  Returned: queried  Sample: `"/Common/pool1"` |
| **load_balancing_mode**  string | Specifies the preferred load balancing mode the system uses to load balance requests across pool members.  Returned: queried |
| **manual_resume**  boolean | Whether manual resume is enabled for this pool.  Returned: queried |
| **max_answers_returned**  integer | Maximum number of available virtual servers the system lists in a response.  Returned: queried |
| **members**  dictionary | Lists of members (and their configurations) in the pool.  Returned: queried |
| **name**  string | Relative name of the resource in the BIG-IP.  Returned: queried  Sample: `"pool1"` |
| **partition**  string | Partition on which the pool exists.  Returned: queried |
| **qos_hit_ratio**  integer | Weight of the Hit Ratio performance factor for the QoS dynamic load balancing method.  Returned: queried |
| **qos_hops**  integer | Weight of the Hops performance factor when load balancing mode or fallback mode is QoS.  Returned: queried |
| **qos_kilobytes_second**  integer | Weight assigned to the Kilobytes per Second performance factor when the load balancing option is QoS.  Returned: queried |
| **qos_lcs**  integer | Weight assigned to the Link Capacity performance factor when the load balacing option is QoS.  Returned: queried |
| **qos_packet_rate**  integer | Weight assigned to the Packet Rate performance factor when the load balacing option is QoS.  Returned: queried |
| **qos_rtt**  integer | Weight assigned to the Round Trip Time performance factor when the load balacing option is QoS.  Returned: queried |
| **qos_topology**  integer | Weight assigned to the Topology performance factor when the load balacing option is QoS.  Returned: queried |
| **qos_vs_capacity**  integer | Weight assigned to the Virtual Server performance factor when the load balacing option is QoS.  Returned: queried |
| **qos_vs_score**  integer | Weight assigned to the Virtual Server Score performance factor when the load balacing option is QoS.  Returned: queried |
| **ttl**  integer | Number of seconds the IP address, once found, is valid.  Returned: queried |
| **verify_member_availability**  boolean | Whether or not the system verifies the availability of the members before sending a connection to them.  Returned: queried |
| **gtm_servers**  complex | GTM server related information.  Returned: When `gtm-servers` is specified in `gather_subset`.  Sample: `"hash/dictionary of values"` |
| **addresses**  dictionary | Specifies the server IP addresses.  Returned: queried |
| **datacenter**  string | Full name of the datacenter to which this server belongs.  Returned: queried |
| **devices**  dictionary | Specifies the names of the devices that represent this server.  Returned: queried |
| **disabled**  boolean | Specifies the server is disabled.  Returned: queried |
| **enabled**  boolean | Specifies the server is enabled.  Returned: queried |
| **expose_route_domains**  boolean | Allow the GTM server to auto-discover the LTM virtual servers from all route domains.  Returned: queried |
| **full_path**  string | Full name of the resource as known to the BIG-IP.  Returned: queried  Sample: `"/Common/server1"` |
| **iq_allow_path**  boolean | Whether the GTM uses this BIG-IP system to conduct a path probe before delegating traffic to it.  Returned: queried |
| **iq_allow_service_check**  boolean | Whether the GTM uses this BIG-IP system to conduct a service check probe before delegating traffic to it.  Returned: queried |
| **iq_allow_snmp**  boolean | Whether the GTM uses this BIG-IP system to conduct an SNMP probe before delegating traffic to it.  Returned: queried |
| **limit_cpu_usage**  integer | For a server configured as a generic host, specifies the percent of CPU usage, otherwise this has no effect.  Returned: queried |
| **limit_cpu_usage_status**  boolean | Whether `limit_cpu_usage` is enabled for this server.  Returned: queried |
| **limit_max_bps**  integer | Maximum allowable data throughput rate in bits per second for this server.  Returned: queried |
| **limit_max_bps_status**  boolean | Whether `limit_max_bps` is enabled for this server.  Returned: queried |
| **limit_max_connections**  integer | Maximum number of concurrent connections, combined, for this server.  Returned: queried |
| **limit_max_connections_status**  boolean | Whether `limit_max_connections` is enabled for this server.  Returned: success |
| **limit_max_pps**  integer | Maximum allowable data transfer rate for this server, in packets per second.  Returned: queried |
| **limit_max_pps_status**  boolean | Whether `limit_max_pps` is enabled for this server.  Returned: queried |
| **limit_mem_available**  integer | For a server configured as a generic host, specifies the available memory required by the virtual servers on the server.  If available memory falls below this limit, the system marks the server as unavailable.  Returned: queried |
| **limit_mem_available_status**  boolean | Whether `limit_mem_available` is enabled for this server.  Returned: queried |
| **link_discovery**  string | Specifies whether the system auto-discovers the links for this server.  Returned: queried |
| **monitor_type**  string | Whether one or more monitors need to pass, or all monitors need to pass.  Returned: queried  Sample: `"and_list"` |
| **monitors**  list / elements=string | Specifies health monitors that the system uses to determine whether this server is available for load balancing.  Returned: queried  Sample: `["/Common/https_443", "/Common/icmp"]` |
| **name**  string | Relative name of the resource in the BIG-IP.  Returned: queried  Sample: `"server1"` |
| **prober_fallback**  string | The type of prober to use to monitor this server’s resources when the preferred type is not available.  Returned: queried |
| **prober_preference**  string | Specifies the type of prober to use to monitor this server’s resources.  Returned: queried |
| **product**  string | Specifies the server type.  Returned: queried |
| **virtual_server_discovery**  string | Whether the system auto-discovers the virtual servers for this server.  Returned: queried |
| **virtual_servers**  dictionary | Specifies the virtual servers that are resources for this server.  Returned: queried |
| **gtm_topology_regions**  complex | GTM regions related information.  Returned: When `gtm-topology-regions` is specified in `gather_subset`  Sample: `"hash/dictionary of values"` |
| **full_path**  string | Full name of the resource as known to the BIG-IP.  Returned: queried  Sample: `"/Common/region1"` |
| **name**  string | Relative name of the resource in the BIG-IP.  Returned: queried  Sample: `"region1"` |
| **region_members**  complex | The list of region members.  Returned: success  Sample: `"hash/dictionary of values"` |
| **continent**  string | The name of one of the seven continents in ISO format, along with the `Unknown` setting.  Returned: when configured for the region member.  Sample: `"AF"` |
| **country**  string | The country name returned as an ISO country code.  Valid country codes can be found here <https://countrycode.org/>.  Returned: when configured for the region member.  Sample: `"US"` |
| **datacenter**  string | The name of a GTM data center already defined in the configuration.  Returned: when configured for the region member.  Sample: `"/Common/dc1"` |
| **geo_isp**  string | Specifies a geolocation ISP.  Returned: when configured for the region member.  Sample: `"/Common/FOO_ISP"` |
| **isp**  string | Specifies an Internet service provider.  Returned: when configured for the region member.  Sample: `"/Common/AOL"` |
| **negate**  boolean | Indicates if the region member is a `IS-NOT` negative. In a BIG-IP configuration, the region members can be `IS` or `IS-NOT`.  Returned: when configured for the region member.  Sample: `true` |
| **pool**  string | The name of a GTM pool already defined in the configuration.  Returned: when configured for the region member.  Sample: `"/Common/pool1"` |
| **region**  string | The name of region already defined in the configuration.  Returned: when configured for the region member.  Sample: `"/Common/region1"` |
| **state**  string | The state in a given country.  Returned: when configured for the region member.  Sample: `"AD/Sant Julia de Loria"` |
| **subnet**  string | An IP address and network mask in the CIDR format.  Returned: when configured for the region member.  Sample: `"10.10.10.0/24"` |
| **gtm_wide_ips**  complex | GTM Wide IP related information.  Every “type” of Wide IP has the exact same list of possible information. Therefore, the list of information here is presented once instead of 6 times.  Returned: When any of `gtm-wide-ips` or `gtm-*-wide-ips` is specified in `gather_subset`.  Sample: `"hash/dictionary of values"` |
| **description**  string | Description of the Wide IP.  Returned: queried |
| **disabled**  boolean | Whether the Wide IP is disabled.  Returned: queried |
| **enabled**  boolean | Whether the Wide IP is enabled.  Returned: queried |
| **failure_rcode**  integer | Specifies the DNS RCODE used when `failure_rcode_response` is `yes`.  Returned: queried |
| **failure_rcode_response**  boolean | When `yes`, specifies the system returns a RCODE response to Wide IP requests after exhausting all load balancing methods.  Returned: queried |
| **failure_rcode_ttl**  integer | Specifies the negative caching TTL of the SOA for the RCODE response.  Returned: queried |
| **full_path**  string | Full name of the resource as known to the BIG-IP.  Returned: queried  Sample: `"/Common/wide1"` |
| **last_resort_pool**  string | Specifies which pool, as listed in Pool List, for the system to use as the last resort pool for the Wide IP.  Returned: queried |
| **minimal_response**  string | Specifies the system forms the smallest allowable DNS response to a query.  Returned: queried |
| **name**  string | Relative name of the resource in the BIG-IP.  Returned: queried  Sample: `"wide1"` |
| **persist_cidr_ipv4**  integer | Specifies the number of bits the system uses to identify IPv4 addresses when persistence is enabled.  Returned: queried |
| **persist_cidr_ipv6**  integer | Specifies the number of bits the system uses to identify IPv6 addresses when persistence is enabled.  Returned: queried |
| **pool_lb_mode**  string | Specifies the load balancing method used to select a pool in this Wide IP.  Returned: queried |
| **pools**  dictionary | Specifies the pools this Wide IP uses for load balancing.  Returned: queried |
| **ttl_persistence**  integer | Specifies, in seconds, the length of time for which the persistence entry is valid.  Returned: queried |
| **http_monitors**  complex | HTTP monitor related information.  Returned: When `http-monitors` is specified in `gather_subset`.  Sample: `"hash/dictionary of values"` |
| **adaptive**  boolean | Whether adaptive response time monitoring is enabled for this monitor.  Returned: queried  Sample: `false` |
| **adaptive_divergence_type**  string | Specifies whether the adaptive-divergence-value is `relative` or `absolute`.  Returned: queried  Sample: `"relative"` |
| **adaptive_divergence_value**  integer | Specifies how far from mean latency each monitor probe is allowed to be.  Returned: queried  Sample: `25` |
| **adaptive_limit**  integer | Specifies the hard limit, in milliseconds, which the probe is not allowed to exceed, regardless of the divergence value.  Returned: queried  Sample: `200` |
| **adaptive_sampling_timespan**  integer | Specifies the size of the sliding window, in seconds, which records probe history.  Returned: queried  Sample: `300` |
| **description**  string | Description of the resource.  Returned: queried  Sample: `"My monitor"` |
| **destination**  string | Specifies the IP address and service port of the resource that is the destination of this monitor.  Returned: queried  Sample: `"*:*"` |
| **full_path**  string | Full name of the resource as known to the BIG-IP.  Returned: queried  Sample: `"/Common/http"` |
| **interval**  integer | Specifies, in seconds, the frequency at which the system issues the monitor check when either the resource is down or the status of the resource is unknown.  Returned: queried  Sample: `5` |
| **ip_dscp**  integer | Specifies the differentiated services code point (DSCP).  Returned: queried  Sample: `0` |
| **manual_resume**  boolean | Specifies whether the system automatically changes the status of a resource to (B)up at the next successful monitor check.  Returned: queried  Sample: `true` |
| **name**  string | Relative name of the resource in the BIG-IP.  Returned: queried  Sample: `"http"` |
| **parent**  string | Profile from which this profile inherits settings.  Returned: queried  Sample: `"http"` |
| **receive_disable_string**  string | Specifies a text string the monitor looks for in the returned resource. If the text string is matched in the returned resource, the corresponding node or pool member is marked session disabled.  Returned: queried  Sample: `"check disable string"` |
| **receive_string**  string | Specifies the text string the monitor looks for in the returned resource.  Returned: queried  Sample: `"check string"` |
| **reverse**  boolean | Specifies whether the monitor operates in reverse mode. When the monitor is in reverse mode, a successful check marks the monitored object down instead of up.  Returned: queried  Sample: `false` |
| **send_string**  string | Specifies the text string the monitor sends to the target object.  Returned: queried  Sample: `"GET /\\r\\n"` |
| **time_until_up**  integer | Specifies the amount of time, in seconds, after the first successful response before a node is marked up.  Returned: queried  Sample: `0` |
| **timeout**  integer | Specifies the number of seconds the target has in which to respond to the monitor request.  Returned: queried  Sample: `16` |
| **transparent**  boolean | Specifies whether the monitor operates in transparent mode.  Returned: queried  Sample: `false` |
| **up_interval**  integer | Specifies, in seconds, the frequency at which the system issues the monitor check when the resource is up.  Returned: queried  Sample: `0` |
| **username**  string | Specifies the username, if the monitored target requires authentication.  Returned: queried  Sample: `"user1"` |
| **http_profiles**  complex | HTTP profile related information.  Returned: When `http-profiles` is specified in `gather_subset`.  Sample: `"hash/dictionary of values"` |
| **accept_xff**  boolean | Enables or disables trusting the client IP address, and statistics from the client IP address, based on the request’s X-Forwarded-For (XFF) headers, if they exist.  Returned: queried  Sample: `true` |
| **allow_truncated_redirects**  boolean | Specifies the pass-through behavior when a redirect lacking the trailing carriage-return and line feed pair at the end of the headers is parsed.  When `no`, the system will silently drop the invalid HTTP.  Returned: queried  Sample: `false` |
| **default_connect_handling**  string | Specifies the behavior of the proxy service when handling outbound requests.  Returned: queried  Sample: `"deny"` |
| **description**  string | Description of the resource.  Returned: queried  Sample: `"My profile"` |
| **excess_client_headers**  string | Specifies the pass-through behavior when the `max_header_count` value is exceeded by the client.  When `reject`, the system rejects the connection.  Returned: queried  Sample: `"reject"` |
| **excess_server_headers**  string | Specifies the pass-through behavior when `max_header_count` value is exceeded by the server.  When `reject`, the system rejects the connection.  Returned: queried  Sample: `"reject"` |
| **full_path**  string | Full name of the resource as known to the BIG-IP.  Returned: queried  Sample: `"/Common/http"` |
| **hsts_enabled**  boolean | When `yes`, enables the HTTP Strict Transport Security settings.  Returned: queried  Sample: `true` |
| **hsts_include_subdomains**  boolean | When `yes`, applies the HSTS policy to the HSTS host and its subdomains.  Returned: queried  Sample: `true` |
| **insert_xforwarded_for**  boolean | When `yes`, specifies the system inserts an X-Forwarded-For header in an HTTP request with the client IP address, to use with connection pooling.  Returned: queried  Sample: `false` |
| **known_methods**  list / elements=string | Optimizes the behavior of a known HTTP method in the list.  The default methods include the following HTTP/1.1 methods. CONNECT, DELETE, GET, HEAD, LOCK, OPTIONS, POST, PROPFIND, PUT, TRACE, UNLOCK.  If a known method is deleted from the `known_methods` list, the BIG-IP system applies the `unknown_method` setting to manage that traffic.  Returned: queried  Sample: `["CONNECT", "DELETE", "..."]` |
| **lws_max_columns**  integer | Specifies the maximum column width for any given line, when inserting an HTTP header in an HTTP request.  Returned: queried  Sample: `80` |
| **max_header_count**  integer | Specifies the maximum number of headers the system supports.  Returned: queried  Sample: `64` |
| **max_header_size**  integer | Specifies the maximum size, in bytes, the system allows for all HTTP request headers combined, including the request line.  Returned: queried  Sample: `32768` |
| **max_requests**  integer | Specifies the number of requests the system accepts on a per-connection basis.  Returned: queried  Sample: `0` |
| **name**  string | Relative name of the resource in the BIG-IP.  Returned: queried  Sample: `"http"` |
| **onconnect_transformations**  boolean | When `yes`, specifies the system performs HTTP header transformations for the purpose of keeping connections open.  Returned: queried  Sample: `true` |
| **oversize_client_headers**  string | Specifies the pass-through behavior when the `max_header_size` value is exceeded by the client.  Returned: queried  Sample: `"reject"` |
| **oversize_server_headers**  string | Specifies the pass-through behavior when the `max_header_size` value is exceeded by the server.  Returned: queried  Sample: `"reject"` |
| **parent**  string | Profile from which this profile inherits settings.  Returned: queried  Sample: `"http"` |
| **pipeline_action**  string | Enables or disables HTTP/1.1 pipelining.  Returned: queried  Sample: `"allow"` |
| **proxy_mode**  string | Specifies the proxy mode for this profile. Either reverse, explicit, or transparent.  Returned: queried  Sample: `"reverse"` |
| **redirect_rewrite**  string | Specifies whether the system rewrites the URIs that are part of HTTP redirect (3XX) responses.  Returned: queried  Sample: `"none"` |
| **request_chunking**  string | Specifies how the system handles HTTP content that is chunked by a client.  Returned: queried  Sample: `"preserve"` |
| **response_chunking**  string | Specifies how the system handles HTTP content that is chunked by a server.  Returned: queried  Sample: `"selective"` |
| **server_agent_name**  string | Specifies the string used as the server name in traffic generated by LTM.  Returned: queried  Sample: `"BigIP"` |
| **sflow_poll_interval**  integer | The maximum interval in seconds between two pollings.  Returned: queried  Sample: `0` |
| **sflow_sampling_rate**  integer | Specifies the ratio of packets observed to the samples generated.  Returned: queried  Sample: `0` |
| **unknown_method**  string | Specifies the behavior (allow, reject, or pass through) when an unknown HTTP method is parsed.  Returned: queried  Sample: `"allow"` |
| **via_request**  string | Specifies whether to Remove, Preserve, or Append Via headers included in a client request to an origin web server.  Returned: queried  Sample: `"preserve"` |
| **via_response**  string | Specifies whether to Remove, Preserve, or Append Via headers included in an origin web server response to a client.  Returned: queried  Sample: `"preserve"` |
| **https_monitors**  complex | HTTPS monitor related information.  Returned: When `https-monitors` is specified in `gather_subset`.  Sample: `"hash/dictionary of values"` |
| **adaptive**  boolean | Whether adaptive response time monitoring is enabled for this monitor.  Returned: queried  Sample: `false` |
| **adaptive_divergence_type**  string | Specifies whether the adaptive-divergence-value is `relative` or `absolute`.  Returned: queried  Sample: `"relative"` |
| **adaptive_divergence_value**  integer | Specifies how far from mean latency each monitor probe is allowed to be.  Returned: queried  Sample: `25` |
| **adaptive_limit**  integer | Specifies the hard limit, in milliseconds, which the probe is not allowed to exceed, regardless of the divergence value.  Returned: queried  Sample: `200` |
| **adaptive_sampling_timespan**  integer | Specifies the size of the sliding window, in seconds, which records probe history.  Returned: queried  Sample: `300` |
| **description**  string | Description of the resource.  Returned: queried  Sample: `"My monitor"` |
| **destination**  string | Specifies the IP address and service port of the resource that is the destination of this monitor.  Returned: queried  Sample: `"*:*"` |
| **full_path**  string | Full name of the resource as known to the BIG-IP.  Returned: queried  Sample: `"/Common/http"` |
| **interval**  integer | Specifies, in seconds, the frequency at which the system issues the monitor check when either the resource is down or the status of the resource is unknown.  Returned: queried  Sample: `5` |
| **ip_dscp**  integer | Specifies the differentiated services code point (DSCP).  Returned: queried  Sample: `0` |
| **manual_resume**  boolean | Specifies whether the system automatically changes the status of a resource to up at the next successful monitor check.  Returned: queried  Sample: `true` |
| **name**  string | Relative name of the resource in the BIG-IP.  Returned: queried  Sample: `"http"` |
| **parent**  string | Profile from which this profile inherits settings.  Returned: queried  Sample: `"http"` |
| **receive_disable_string**  string | Specifies a text string the monitor looks for in the returned resource. If the text string is matched in the returned resource, the corresponding node or pool member is marked session disabled.  Returned: queried  Sample: `"check disable string"` |
| **receive_string**  string | Specifies the text string the monitor looks for in the returned resource.  Returned: queried  Sample: `"check string"` |
| **reverse**  boolean | Specifies whether the monitor operates in reverse mode. When the monitor is in reverse mode, a successful check marks the monitored object down instead of up.  Returned: queried  Sample: `false` |
| **send_string**  string | Specifies the text string the monitor sends to the target object.  Returned: queried  Sample: `"GET /\\r\\n"` |
| **ssl_profile**  string | Specifies the SSL profile to use for the HTTPS monitor.  Returned: queried  Sample: `"/Common/serverssl"` |
| **time_until_up**  integer | Specifies the amount of time, in seconds, after the first successful response before a node is marked up.  Returned: queried  Sample: `0` |
| **timeout**  integer | Specifies the number of seconds the target has in which to respond to the monitor request.  Returned: queried  Sample: `16` |
| **transparent**  boolean | Specifies whether the monitor operates in transparent mode.  Returned: queried  Sample: `false` |
| **up_interval**  integer | Specifies, in seconds, the frequency at which the system issues the monitor check when the resource is up.  Returned: queried  Sample: `0` |
| **username**  string | Specifies the username, if the monitored target requires authentication.  Returned: queried  Sample: `"user1"` |
| **iapp_services**  complex | iApp v1 service related information.  Returned: When `iapp-services` is specified in `gather_subset`.  Sample: `"hash/dictionary of values"` |
| **description**  string | Description of the service.  Returned: queried  Sample: `"My service"` |
| **device_group**  string | The device group the iApp service is part of.  Returned: queried  Sample: `"/Common/dg1"` |
| **full_path**  string | Full name of the resource as known to the BIG-IP.  Returned: queried  Sample: `"/Common/service1"` |
| **inherited_device_group**  boolean | Whether the device group is inherited or not.  Returned: queried  Sample: `true` |
| **inherited_traffic_group**  boolean | Whether the traffic group is inherited or not.  Returned: queried  Sample: `true` |
| **lists**  list / elements=string | List of the lists data used to create the service.  Returned: queried  Sample: `[{"name": "irules__irules"}, {"value": []}, "..."]` |
| **metadata**  list / elements=string | List of the metadata data used to create the service.  Returned: queried  Sample: `[{"name": "var1"}, {"persist": "true"}, "..."]` |
| **name**  string | Relative name of the resource in the BIG-IP.  Returned: queried  Sample: `"service1"` |
| **strict_updates**  boolean | Whether strict updates are enabled or not.  Returned: queried  Sample: `true` |
| **tables**  list / elements=string | List of the tabular data used to create the service.  Returned: queried  Sample: `[{"name": "basic__snatpool_members"}, "..."]` |
| **template_modified**  boolean | Whether template the service is based on is modified from its default value, or not.  Returned: queried  Sample: `true` |
| **traffic_group**  string | Traffic group the service is a part of.  Returned: queried  Sample: `"/Common/tg"` |
| **variables**  list / elements=string | List of the variable data used to create the service.  Returned: queried  Sample: `[{"name": "afm__policy"}, {"encrypted": "no"}, {"value": "/#no_not_use#"}, "..."]` |
| **icmp_monitors**  complex | ICMP monitor related information.  Returned: When `icmp-monitors` is specified in `gather_subset`.  Sample: `"hash/dictionary of values"` |
| **adaptive**  boolean | Whether adaptive response time monitoring is enabled for this monitor.  Returned: queried  Sample: `false` |
| **adaptive_divergence_type**  string | Specifies whether the adaptive-divergence-value is `relative` or `absolute`.  Returned: queried  Sample: `"relative"` |
| **adaptive_divergence_value**  integer | Specifies how far from mean latency each monitor probe is allowed to be.  Returned: queried  Sample: `25` |
| **adaptive_limit**  integer | Specifies the hard limit, in milliseconds, which the probe is not allowed to exceed, regardless of the divergence value.  Returned: queried  Sample: `200` |
| **adaptive_sampling_timespan**  integer | Specifies the size of the sliding window, in seconds, which records probe history.  Returned: queried  Sample: `300` |
| **description**  string | Description of the resource.  Returned: queried  Sample: `"My monitor"` |
| **destination**  string | Specifies the IP address and service port of the resource that is the destination of this monitor.  Returned: queried  Sample: `"*:*"` |
| **full_path**  string | Full name of the resource as known to the BIG-IP.  Returned: queried  Sample: `"/Common/icmp"` |
| **interval**  integer | Specifies, in seconds, the frequency at which the system issues the monitor check when either the resource is down or the status of the resource is unknown.  Returned: queried  Sample: `5` |
| **manual_resume**  boolean | Specifies whether the system automatically changes the status of a resource to (B)up at the next successful monitor check.  Returned: success  Sample: `true` |
| **name**  string | Relative name of the resource in the BIG-IP.  Returned: queried  Sample: `"icmp"` |
| **parent**  string | Profile from which this profile inherits settings.  Returned: queried  Sample: `"icmp"` |
| **time_until_up**  integer | Specifies the amount of time, in seconds, after the first successful response before a node is marked up.  Returned: queried  Sample: `0` |
| **timeout**  integer | Specifies the number of seconds the target has in which to respond to the monitor request.  Returned: queried  Sample: `16` |
| **transparent**  boolean | Specifies whether the monitor operates in transparent mode.  Returned: queried  Sample: `false` |
| **up_interval**  integer | Specifies, in seconds, the frequency at which the system issues the monitor check when the resource is up.  Returned: queried  Sample: `0` |
| **interfaces**  complex | Interface related information.  Returned: When `interfaces` is specified in `gather_subset`.  Sample: `"hash/dictionary of values"` |
| **active_media_type**  string | Displays the current media setting for the interface.  Returned: queried  Sample: `"100TX-FD"` |
| **bundle**  string | The bundle capability on the port.  Returned: queried  Sample: `"not-supported"` |
| **bundle_speed**  string | The bundle-speed on the port when bundle capability is enabled.  Returned: queried  Sample: `"100G"` |
| **description**  string | Description of the interface.  Returned: queried  Sample: `"My interface"` |
| **enabled**  boolean | Whether the interface is enabled or not.  Returned: queried  Sample: `true` |
| **flow_control**  string | Specifies how the system controls the sending of PAUSE frames for flow control.  Returned: queried  Sample: `"tx-rx"` |
| **full_path**  string | Full name of the resource as known to the BIG-IP.  Returned: queried  Sample: `"/Common/interface1"` |
| **if_index**  integer | The index assigned to this interface.  Returned: queried  Sample: `32` |
| **lldp_admin**  string | Sets the sending or receiving of LLDP packets on that interface. Should be one of `disable`, `txonly`, `rxonly` or `txrx`.  Returned: queried  Sample: `"txonly"` |
| **mac_address**  string | Displays the 6-byte ethernet address in non-case-sensitive hexadecimal colon notation.  Returned: queried  Sample: `"00:0b:09:88:00:9a"` |
| **media_sfp**  string | The settings for an SFP (pluggable) interface.  Returned: queried  Sample: `"auto"` |
| **mtu**  integer | Displays the Maximum Transmission Unit (MTU) of the interface, which is the maximum number of bytes in a frame without IP fragmentation.  Returned: queried  Sample: `1500` |
| **name**  string | Relative name of the resource in the BIG-IP.  Returned: queried  Sample: `"interface1"` |
| **prefer_port**  string | Indicates which side of a combo port the interface uses, if both sides of the port have the potential for external links.  Returned: queried  Sample: `"sfp"` |
| **sflow_poll_interval**  integer | Specifies the maximum interval in seconds between two pollings.  Returned: queried  Sample: `0` |
| **sflow_poll_interval_global**  boolean | Specifies whether the global interface poll-interval setting overrides the object-level poll-interval setting.  Returned: queried  Sample: `true` |
| **stp_auto_edge_port**  boolean | STP edge port detection.  Returned: queried  Sample: `true` |
| **stp_enabled**  boolean | Whether STP is enabled or not.  Returned: queried  Sample: `false` |
| **stp_link_type**  string | Specifies the STP link type for the interface.  Returned: queried  Sample: `"auto"` |
| **irules**  complex | iRule related information.  Returned: When `irules` is specified in `gather_subset`.  Sample: `"hash/dictionary of values"` |
| **checksum**  string | Checksum of the iRule as calculated by BIG-IP.  Returned: queried  Sample: `"d41d8cd98f00b204e9800998ecf8427e"` |
| **definition**  string | The actual definition of the iRule.  Returned: queried  Sample: `"when HTTP_REQUEST ..."` |
| **full_path**  string | Full name of the resource as known to the BIG-IP.  Returned: queried  Sample: `"/Common/irule1"` |
| **ignore_verification**  boolean | Whether the verification of the iRule should be ignored or not.  Returned: queried  Sample: `false` |
| **name**  string | Relative name of the resource in the BIG-IP.  Returned: queried  Sample: `"irule1"` |
| **signature**  string | The calculated signature of the iRule.  Returned: queried  Sample: `"WsYy2M6xMqvosIKIEH/FSsvhtWMe6xKOA6i7f..."` |
| **ltm_policies**  complex | List of LTM (Local Traffic Manager) policies.  Returned: When `ltm-policies` is specified in `gather_subset`.  Sample: `"hash/dictionary of values"` |
| **controls**  list / elements=string | Aspects of the system controlled by this policy.  Returned: queried  Sample: `["forwarding"]` |
| **description**  string | Description of the policy.  Returned: queried  Sample: `"My policy"` |
| **full_path**  string | Full name of the resource as known to the BIG-IP.  Returned: queried  Sample: `"/Common/policy1"` |
| **name**  string | Relative name of the resource in the BIG-IP.  Returned: queried  Sample: `"policy1"` |
| **requires**  list / elements=string | Aspects of the system required by this policy.  Returned: queried  Sample: `["http"]` |
| **rules**  complex | List of LTM (Local Traffic Manager) policy rules.  Returned: when rules are defined in the policy.  Sample: `"hash/dictionary of values"` |
| **actions**  complex | The actions the policy will take when a match is encountered.  Returned: when actions are defined in the rule.  Sample: `"hash/dictionary of values"` |
| **http_reply**  boolean | Indicates if the action affects a reply to a given HTTP request.  Returned: when defined in the action.  Sample: `true` |
| **location**  string | This action will come from the given location.  Returned: when defined in the action.  Sample: `"tcl:https://[getfield [HTTP::host] \\\":\\\" 1][HTTP::uri]"` |
| **redirect**  boolean | This action will redirect a request.  Returned: when defined in the action.  Sample: `false` |
| **request**  boolean | This policy action is performed on connection requests.  Returned: when defined in the action.  Sample: `false` |
| **conditions**  complex | The conditions a policy will match on.  Returned: when conditions are defined in the rule.  Sample: `"hash/dictionary of values"` |
| **address**  boolean | This condition matches on a TCP address.  Returned: when defined in the condition.  Sample: `false` |
| **all**  boolean | Matches all.  Returned: when defined in the condition.  Sample: `true` |
| **case_insensitive**  boolean | Specifies the value matched on is case insensitive.  Returned: when defined in the condition.  Sample: `false` |
| **case_sensitive**  boolean | Specifies the value matched on is case sensitive.  Returned: when defined in the condition.  Sample: `true` |
| **contains_string**  boolean | Specifies the value matches if it contains a certain string.  Returned: when defined in the condition.  Sample: `true` |
| **datagroup**  string | This condition matches on an HTTP URI.  Returned: when defined in the condition.  Sample: `"/Common/policy_using_datagroup"` |
| **external**  boolean | Specifies the value matched on is from the external side of a connection.  Returned: when defined in the condition.  Sample: `true` |
| **http_basic_auth**  boolean | This condition matches on basic HTTP authorization.  Returned: when defined in the condition.  Sample: `false` |
| **http_host**  boolean | This condition matches on an HTTP host.  Returned: when defined in the condition.  Sample: `true` |
| **http_uri**  boolean | This condition matches on an HTTP URI.  Returned: when defined in the condition.  Sample: `false` |
| **matches**  boolean | This condition matches on an address.  Returned: when defined in the condition.  Sample: `false` |
| **proxy_connect**  boolean | Specifies the value matched on is proxyConnect.  Returned: when defined in the condition.  Sample: `false` |
| **proxy_request**  boolean | Specifies the value matched on is proxyRequest.  Returned: when defined in the condition.  Sample: `false` |
| **remote**  boolean | Specifies the value matched on is remote.  Returned: when defined in the condition.  Sample: `false` |
| **request**  boolean | This policy matches on a request.  Returned: when defined in the condition.  Sample: `true` |
| **tcp**  boolean | This condition matches on TCP parameters.  Returned: when defined in the condition.  Sample: `false` |
| **username**  boolean | Matches on a username.  Returned: when defined in the condition.  Sample: `true` |
| **values**  list / elements=string | The specified values will be matched on.  Returned: when defined in the condition.  Sample: `["foo.bar.com", "baz.cool.com"]` |
| **status**  string | Indicates published or draft policy status.  Returned: queried  Sample: `"draft"` |
| **strategy**  string | The match strategy for the policy.  Returned: queried  Sample: `"/Common/first-match"` |
| **ltm_pools**  complex | List of LTM (Local Traffic Manager) pools.  Returned: When `ltm-pools` is specified in `gather_subset`.  Sample: `"hash/dictionary of values"` |
| **active_member_count**  integer | The number of active pool members in the pool.  Returned: queried  Sample: `3` |
| **all_avg_queue_entry_age**  integer | Average queue entry age, for both the pool and its members.  Returned: queried  Sample: `5` |
| **all_max_queue_entry_age_ever**  integer | Maximum queue entry age ever, for both the pool and its members.  Returned: queried  Sample: `2` |
| **all_max_queue_entry_age_recently**  integer | Maximum queue entry age recently, for both the pool and its members.  Returned: queried  Sample: `5` |
| **all_num_connections_queued_now**  integer | Number of connections queued now, for both the pool and its members.  Returned: queried  Sample: `20` |
| **all_num_connections_serviced**  integer | Number of connections serviced, for both the pool and its members.  Returned: queried  Sample: `15` |
| **all_queue_head_entry_age**  integer | Queue head entry age, for both the pool and its members.  Returned: queried  Sample: `4` |
| **allow_nat**  boolean | Whether NATs are automatically enabled or disabled for any connections using this pool.  Returned: queried  Sample: `true` |
| **allow_snat**  boolean | Whether SNATs are automatically enabled or disabled for any connections using this pool.  Returned: queried  Sample: `true` |
| **availability_status**  string | The availability of the pool.  Returned: queried  Sample: `"offline"` |
| **available_member_count**  integer | The number of available pool members in the pool.  Returned: queried  Sample: `4` |
| **client_ip_tos**  string | Whether the system sets a Type of Service (ToS) level within a packet sent to the client, based on the targeted pool.  Values can range from `0` to `255`, or be set to `pass-through` or `mimic`.  Returned: queried  Sample: `"pass-through"` |
| **client_link_qos**  string | Whether the system sets a Quality of Service (QoS) level within a packet sent to the client, based on the targeted pool.  Values can range from `0` to `7`, or be set to `pass-through`.  Returned: queried  Sample: `"pass-through"` |
| **current_sessions**  integer | Current sessions.  Returned: queried  Sample: `2` |
| **description**  string | Description of the pool.  Returned: queried  Sample: `"my pool"` |
| **enabled_status**  string | The enabled status of the pool.  Returned: queried  Sample: `"enabled"` |
| **full_path**  string | Full name of the resource as known to the BIG-IP.  Returned: queried  Sample: `"/Common/pool1"` |
| **ignore_persisted_weight**  boolean | Specifies not to count the weight of persisted connections on pool members when making load balancing decisions.  Returned: queried  Sample: `false` |
| **lb_method**  string | Load balancing method used by the pool.  Returned: queried  Sample: `"round-robin"` |
| **member_count**  integer | Total number of members in the pool.  Returned: queried  Sample: `50` |
| **members**  complex | List of LTM (Local Traffic Manager) pools.  Returned: when members exist in the pool. |
| **address**  string | IP address of the pool member.  Returned: queried  Sample: `"1.1.1.1"` |
| **connection_limit**  integer | The maximum number of concurrent connections allowed for a pool member.  Returned: queried  Sample: `0` |
| **description**  string | The description of the pool member.  Returned: queried  Sample: `"pool member 1"` |
| **dynamic_ratio**  integer | A range of numbers you want the system to use in conjunction with the ratio load balancing method.  Returned: queried  Sample: `1` |
| **encapsulation_profile**  string | The encapsulation profile to use for the pool member.  Returned: queried  Sample: `"ip4ip4"` |
| **ephemeral**  boolean | Whether the node backing the pool member is ephemeral or not.  Returned: queried  Sample: `true` |
| **fqdn_autopopulate**  boolean | Whether the node should scale to the IP address set returned by DNS.  Returned: queried  Sample: `true` |
| **full_path**  string | Full name of the resource as known to the BIG-IP.  Includes the port in the name.  Returned: queried  Sample: `"/Common/member:80"` |
| **inherit_profile**  boolean | Whether the pool member inherits the encapsulation profile from the parent pool.  Returned: queried  Sample: `false` |
| **logging**  boolean | Whether the monitor applied should log its actions.  Returned: queried  Sample: `false` |
| **monitors**  list / elements=string | The Monitors active on the pool member. Monitor names are in their “full_path” form.  Returned: queried  Sample: `["/Common/http"]` |
| **name**  string | Relative name of the resource in the BIG-IP.  Returned: queried  Sample: `"member:80"` |
| **partition**  string | Partition the member exists on.  Returned: queried  Sample: `"Common"` |
| **priority_group**  integer | The priority group within the pool for this pool member.  Returned: queried  Sample: `0` |
| **rate_limit**  boolean | The maximum number of connections per second allowed for a pool member.  Returned: queried  Sample: `false` |
| **ratio**  integer | The weight of the pool for load balancing purposes.  Returned: queried  Sample: `1` |
| **session**  string | Enables or disables the pool member for new sessions.  Returned: queried  Sample: `"monitor-enabled"` |
| **state**  string | Controls the state of the pool member, overriding any monitors.  Returned: queried  Sample: `"down"` |
| **metadata**  dictionary | Dictionary of arbitrary key/value pairs set on the pool.  Returned: queried  Sample: `"hash/dictionary of values"` |
| **minimum_active_members**  integer | Whether the system load balances traffic according to the priority number assigned to the pool member.  This parameter is identical to `priority_group_activation` and is just an alias for it.  Returned: queried  Sample: `2` |
| **minimum_up_members**  integer | The minimum number of pool members that must be up.  Returned: queried  Sample: `1` |
| **minimum_up_members_action**  string | The action to take if the `minimum_up_members_checking` is enabled and the number of active pool members falls below the number specified in `minimum_up_members`.  Returned: queried  Sample: `"failover"` |
| **minimum_up_members_checking**  boolean | Enables or disables the `minimum_up_members` feature.  Returned: queried  Sample: `false` |
| **name**  string | Relative name of the resource in the BIG-IP.  Returned: queried  Sample: `"pool1"` |
| **pool_avg_queue_entry_age**  integer | Average queue entry age, for the pool only.  Returned: queried  Sample: `5` |
| **pool_max_queue_entry_age_ever**  integer | Maximum queue entry age ever, for the pool only.  Returned: queried  Sample: `2` |
| **pool_max_queue_entry_age_recently**  integer | Maximum queue entry age recently, for the pool only.  Returned: queried  Sample: `5` |
| **pool_num_connections_queued_now**  integer | Number of connections queued now, for the pool only.  Returned: queried  Sample: `20` |
| **pool_num_connections_serviced**  integer | Number of connections serviced, for the pool only.  Returned: queried  Sample: `15` |
| **pool_queue_head_entry_age**  integer | Queue head entry age, for the pool only.  Returned: queried  Sample: `4` |
| **priority_group_activation**  integer | Whether the system load balances traffic according to the priority number assigned to the pool member.  This parameter is identical to `minimum_active_members` and is just an alias for it.  Returned: queried  Sample: `2` |
| **queue_depth_limit**  integer | The maximum number of connections that may simultaneously be queued to go to any member of this pool.  Returned: queried  Sample: `3` |
| **queue_on_connection_limit**  boolean | Enable or disable queuing connections when pool member or node connection limits are reached.  Returned: queried  Sample: `true` |
| **queue_time_limit**  integer | Specifies the maximum time, in milliseconds, a connection will remain queued.  Returned: queried  Sample: `0` |
| **real_session**  string | The actual REST API value for the `session` attribute.  This is different from the `state` return value, as the return value can be considered a generalization of all available sessions, instead of the specific value of the session.  Returned: queried  Sample: `"monitor-enabled"` |
| **real_state**  string | The actual REST API value for the `state` attribute.  This is different from the `state` return value, as the return value can be considered a generalization of all available states, instead of the specific value of the state.  Returned: queried  Sample: `"up"` |
| **reselect_tries**  integer | The number of times the system tries to contact a pool member after a passive failure.  Returned: queried  Sample: `0` |
| **server_ip_tos**  string | The Type of Service (ToS) level to use when sending packets to a server.  Returned: queried  Sample: `"pass-through"` |
| **server_link_qos**  string | The Quality of Service (QoS) level to use when sending packets to a server.  Returned: queried  Sample: `"pass-through"` |
| **server_side_bits_in**  integer | Number of server-side ingress bits.  Returned: queried  Sample: `1000` |
| **server_side_bits_out**  integer | Number of server-side egress bits.  Returned: queried  Sample: `200` |
| **server_side_current_connections**  integer | Number of current connections server-side.  Returned: queried  Sample: `300` |
| **server_side_max_connections**  integer | Maximum number of connections server-side.  Returned: queried  Sample: `40` |
| **server_side_pkts_in**  integer | Number of server-side ingress packets.  Returned: queried  Sample: `1098384` |
| **server_side_pkts_out**  integer | Number of server-side egress packets.  Returned: queried  Sample: `3484734` |
| **server_side_total_connections**  integer | Total number of server-side connections.  Returned: queried  Sample: `24` |
| **service_down_action**  string | The action to take if the service specified in the pool is marked down.  Returned: queried  Sample: `"none"` |
| **slow_ramp_time**  integer | The ramp time for the pool.  This provides the ability for a pool member that is newly enabled or marked up to receive proportionally less traffic than other members in the pool.  Returned: queried  Sample: `10` |
| **status_reason**  string | If there is a problem with the status of the pool, it is reported here.  Returned: queried  Sample: `"The children pool member(s) are down."` |
| **total_requests**  integer | Total requests.  Returned: queried  Sample: `8` |
| **management_routes**  complex | Management route related information.  Returned: When `management-routes` is specified in `gather_subset`.  Sample: `"hash/dictionary of values"` |
| **description**  string | User defined description of the route.  Returned: queried  Sample: `"route-1-external"` |
| **full_path**  string | Full name of the resource as known to the BIG-IP.  Returned: queried  Sample: `"/Common/default"` |
| **gateway**  string | The gateway IP address through which the system forwards packets to the destination.  Returned: queried  Sample: `"192.168.0.1"` |
| **mtu**  string | The maximum transmission unit for the management interface.  Returned: queried  Sample: `"0"` |
| **name**  string | Relative name of the resource in the BIG-IP.  Returned: queried  Sample: `"default"` |
| **network**  string | The destination subnet and netmask, also specified as default or default-inet6.  Returned: queried  Sample: `"default"` |
| **nodes**  complex | Node related information.  Returned: When `nodes` is specified in `gather_subset`.  Sample: `"hash/dictionary of values"` |
| **address**  string | IP address of the node.  Returned: queried  Sample: `"2.3.4.5"` |
| **availability_status**  string | The availability of the node.  Returned: queried  Sample: `"offline"` |
| **connection_limit**  integer | Maximum number of connections the node can handle.  Returned: queried  Sample: `100` |
| **description**  string | Description of the node.  Returned: queried  Sample: `"My node"` |
| **dynamic_ratio**  integer | Dynamic ratio number for the node used when doing `Dynamic Ratio` load balancing.  Returned: queried  Sample: `200` |
| **enabled_status**  string | The enabled status of the node.  Returned: queried  Sample: `"enabled"` |
| **fqdn_address_type**  string | The address family of the automatically created ephemeral nodes.  Returned: queried  Sample: `"ipv4"` |
| **fqdn_auto_populate**  boolean | Indicates if the system automatically creates ephemeral nodes using DNS discovered IPs.  Returned: queried  Sample: `true` |
| **fqdn_down_interval**  integer | The interval in which a query occurs when the DNS server is down.  Returned: queried  Sample: `15` |
| **fqdn_name**  string | FQDN name of the node.  Returned: queried  Sample: `"sample.host.foo.com"` |
| **fqdn_up_interval**  integer | The interval at which a query occurs when the DNS server is up.  Returned: queried  Sample: `3600` |
| **full_path**  string | Full name of the resource as known to the BIG-IP.  Returned: queried  Sample: `"/Common/5.6.7.8"` |
| **monitor_rule**  string | A string representation of the full monitor rule.  Returned: queried  Sample: `"/Common/https_443 and /Common/icmp"` |
| **monitor_status**  string | Status of the node as reported by the monitor(s) associated with it.  This value is also used in determining node `state`.  Returned: queried  Sample: `"down"` |
| **monitor_type**  string | The `monitor_type` field related to the `bigip_node` module, for this nodes monitors.  Returned: queried  Sample: `"and_list"` |
| **monitors**  list / elements=string | A list of the monitors identified in the `monitor_rule`.  Returned: queried  Sample: `["/Common/https_443", "/Common/icmp"]` |
| **name**  string | Relative name of the resource in the BIG-IP.  Returned: queried  Sample: `"5.6.7.8"` |
| **rate_limit**  integer | Maximum number of connections per second allowed for the node.  Returned: queried  Sample: `1000` |
| **ratio**  integer | Fixed size ratio used for node during `Ratio` load balancing.  Returned: queried  Sample: `10` |
| **session_status**  string | This value is also used in determining node `state`.  Returned: queried  Sample: `"enabled"` |
| **status_reason**  string | If there is a problem with the status of the node, it is reported here.  Returned: queried  Sample: `"/Common/https_443 No successful responses received..."` |
| **oneconnect_profiles**  complex | OneConnect profile related information.  Returned: When `oneconnect-profiles` is specified in `gather_subset`.  Sample: `"hash/dictionary of values"` |
| **description**  string | Description of the resource.  Returned: queried  Sample: `"My profile"` |
| **full_path**  string | Full name of the resource as known to the BIG-IP.  Returned: queried  Sample: `"/Common/oneconnect"` |
| **idle_timeout_override**  integer | Specifies the number of seconds that a connection is idle before the connection flow is eligible for deletion.  Returned: queried  Sample: `1000` |
| **limit_type**  string | When `none`, simultaneous in-flight requests and responses over TCP connections to a pool member are counted toward the limit.  When `idle`, idle connections will be dropped as the TCP connection limit is reached.  When `strict`, the TCP connection limit is honored with no exceptions. This means idle connections will prevent new TCP connections from being made until they expire, even if they could otherwise be reused.  Returned: queried  Sample: `"idle"` |
| **max_age**  integer | Specifies the maximum age, in seconds, of a connection in the connection reuse pool.  Returned: queried  Sample: `100` |
| **max_reuse**  integer | Specifies the maximum number of times a server connection can be reused.  Returned: queried  Sample: `1000` |
| **max_size**  integer | Specifies the maximum number of connections the system holds in the connection reuse pool.  If the pool is already full, then the server connection closes after the response is completed.  Returned: queried  Sample: `1000` |
| **name**  string | Relative name of the resource in the BIG-IP.  Returned: queried  Sample: `"oneconnect"` |
| **parent**  string | Profile from which this profile inherits settings.  Returned: queried  Sample: `"oneconnect"` |
| **share_pools**  boolean | Indicates connections may be shared not only within a virtual server, but also among similar virtual servers.  Returned: queried  Sample: `true` |
| **source_mask**  string | Specifies a source IP mask.  If no mask is provided, the value `any6` is used.  Returned: queried  Sample: `"255.255.255.0"` |
| **partitions**  complex | Partition related information.  Returned: When `partitions` is specified in `gather_subset`.  Sample: `"hash/dictionary of values"` |
| **default_route_domain**  integer | ID of the route domain that is associated with the IP addresses that reside in the partition.  Returned: queried  Sample: `0` |
| **description**  string | Description of the partition.  Returned: queried  Sample: `"Tenant 1"` |
| **full_path**  string | Full name of the resource as known to the BIG-IP.  Returned: queried  Sample: `"Common"` |
| **name**  string | Relative name of the resource in the BIG-IP.  Returned: queried  Sample: `"Common"` |
| **provision_info**  complex | Module provisioning related information.  Returned: When `provision-info` is specified in `gather_subset`.  Sample: `"hash/dictionary of values"` |
| **cpu_ratio**  integer | Ratio of CPU allocated to this module.  Only relevant if `level` was specified as `custom`. Otherwise, this value will be reported as `0`.  Returned: queried  Sample: `0` |
| **disk_ratio**  integer | Ratio of disk allocated to this module.  Only relevant if `level` was specified as `custom`. Otherwise, this value will be reported as `0`.  Returned: queried  Sample: `0` |
| **full_path**  string | Full name of the resource as known to the BIG-IP.  Returned: queried  Sample: `"asm"` |
| **level**  integer | Provisioned level of the module on BIG-IP.  Valid return values can include `none`, `minimum`, `nominal`, `dedicated` and `custom`.  Returned: queried  Sample: `0` |
| **memory_ratio**  integer | Ratio of memory allocated to this module.  Only relevant if `level` was specified as `custom`. Otherwise, this value will be reported as `0`.  Returned: queried  Sample: `0` |
| **name**  string | Relative name of the resource in the BIG-IP.  Returned: queried  Sample: `"asm"` |
| **remote_syslog**  complex | Remote Syslog related information.  Returned: When `remote-syslog` is specified in `gather_subset`.  Sample: `"hash/dictionary of values"` |
| **servers**  complex | Configured remote syslog servers.  Returned: queried  Sample: `"hash/dictionary of values"` |
| **local_ip**  string | The local IP address of the remote syslog server.  Returned: queried  Sample: `"10.10.10.10"` |
| **name**  string | Name of remote syslog server as configured on the system.  Returned: queried  Sample: `"/Common/foobar1"` |
| **remote_host**  string | The IP address or hostname of the remote syslog server.  Returned: queried  Sample: `"192.168.1.1"` |
| **remote_port**  integer | Remote port of the remote syslog server.  Returned: queried  Sample: `514` |
| **route_domains**  complex | Route domain related information.  Returned: When `self-ips` is specified in `gather_subset`.  Sample: `"hash/dictionary of values"` |
| **bwc_policy**  string | The bandwidth controller for the route domain.  Returned: queried  Sample: `"/Common/foo"` |
| **connection_limit**  integer | The new connection limit for the route domain.  Returned: queried  Sample: `100` |
| **description**  string | Description of the Route Domain.  Returned: queried  Sample: `"My route domain"` |
| **flow_eviction_policy**  string | The new eviction policy to use with this route domain.  Returned: queried  Sample: `"/Common/default-eviction-policy"` |
| **full_path**  string | Full name of the resource as known to the BIG-IP.  Returned: queried  Sample: `"/Common/rd1"` |
| **id**  integer | The unique identifying integer representing the route domain.  Returned: queried  Sample: `10` |
| **name**  string | Relative name of the resource in the BIG-IP.  Returned: queried  Sample: `"rd1"` |
| **parent**  string | The route domain the system searches when it cannot find a route in the configured domain.  Returned: queried  Sample: `"0"` |
| **routing_protocol**  list / elements=string | List of routing protocols applied to the route domain.  Returned: queried  Sample: `["bfd", "bgp"]` |
| **service_policy**  string | The new service policy to use with this route domain.  Returned: queried  Sample: `"/Common-my-service-policy"` |
| **strict**  string | The new strict isolation setting.  Returned: queried  Sample: `"enabled"` |
| **vlans**  list / elements=string | List of new VLANs the route domain is applied to.  Returned: queried  Sample: `["/Common/http-tunnel", "/Common/socks-tunnel"]` |
| **self_ips**  complex | Self IP related information.  Returned: When `self-ips` is specified in `gather_subset`.  Sample: `"hash/dictionary of values"` |
| **allow_access_list**  list / elements=string | List of protocols, and optionally their ports, that are allowed to access the Self IP. Also known as port-lockdown in the web interface.  Items in the list are in the format of “protocol:port”. Some items may not have a port associated with them and in those cases the port is `0`.  Returned: queried  Sample: `["tcp:80", "egp:0"]` |
| **description**  string | Description of the Self IP.  Returned: queried  Sample: `"My self-ip"` |
| **floating**  boolean | Whether the Self IP is a floating address or not.  Returned: queried  Sample: `true` |
| **full_path**  string | Full name of the resource as known to the BIG-IP.  Returned: queried  Sample: `"/Common/self1"` |
| **name**  string | Relative name of the resource in the BIG-IP.  Returned: queried  Sample: `"self1"` |
| **netmask**  string | Netmask portion of the IP address, in dotted notation.  Returned: queried  Sample: `"255.255.255.0"` |
| **netmask_cidr**  integer | Netmask portion of the IP address, in CIDR notation.  Returned: queried  Sample: `24` |
| **service_policy**  string | Service policy assigned to the Self IP.  Returned: queried  Sample: `"/Common/service1"` |
| **traffic_group**  string | Traffic group the Self IP is associated with.  Returned: queried  Sample: `"/Common/traffic-group-local-only"` |
| **traffic_group_inherited**  boolean | Whether or not the traffic group is inherited.  Returned: queried  Sample: `false` |
| **vlan**  string | VLAN associated with the Self IP.  Returned: queried  Sample: `"/Common/vlan1"` |
| **server_ssl_profiles**  complex | Server SSL related information.  Returned: When `server-ssl-profiles` is specified in `gather_subset`.  Sample: `"hash/dictionary of values"` |
| **alert_timeout**  string | Maximum time period in seconds to keep the SSL session active after an alert message is sent, or indefinite.  Returned: queried  Sample: `"100"` |
| **allow_expired_crl**  boolean | Use the specified CRL file, even if it has expired.  Returned: queried  Sample: `true` |
| **authenticate_depth**  integer | The client certificate chain maximum traversal depth  Returned: queried  Sample: `9` |
| **authenticate_name**  string | Common Name (CN) embedded in a server certificate.  The system authenticates a server based on the specified CN.  Returned: queried  Sample: `"foo"` |
| **authentication_frequency**  string | Specifies the frequency of authentication.  Returned: queried  Sample: `"once"` |
| **bypass_on_client_cert_fail**  boolean | Enables or disables SSL forward proxy bypass on failing to get client certificate that the server asks for.  Returned: queried  Sample: `true` |
| **bypass_on_handshake_alert**  boolean | Enables or disables SSL forward proxy bypass on receiving handshake_failure, protocol_version or unsupported_extension alert message during the serverside SSL handshake.  Returned: queried  Sample: `false` |
| **c3d_ca_cert**  string | Name of the certificate file used as the certification authority certificate when SSL client certificate constrained delegation is enabled.  Returned: queried  Sample: `"/Common/cacert.crt"` |
| **c3d_ca_key**  string | Name of the key file used as the certification authority key when SSL client certificate constrained delegation is enabled.  Returned: queried  Sample: `"/Common/default.key"` |
| **c3d_cert_extension_includes**  list / elements=string | Extensions of the client certificates to be included in the generated certificates using SSL client certificate constrained delegation.  Returned: queried  Sample: `["basic-constraints", "extended-key-usage", "..."]` |
| **c3d_cert_lifespan**  integer | Lifespan of the certificate generated using the SSL client certificate constrained delegation.  Returned: queried  Sample: `24` |
| **ca_file**  string | Certificate authority file name.  Returned: queried  Sample: `"default.crt"` |
| **cache_size**  integer | The SSL session cache size.  Returned: queried  Sample: `262144` |
| **cache_timeout**  integer | The SSL session cache timeout value, which is the usable lifetime seconds of negotiated SSL session IDs.  Returned: queried  Sample: `86400` |
| **cert**  string | The name of the certificate installed on the traffic management system for the purpose of terminating or initiating an SSL connection.  Returned: queried  Sample: `"/Common/default.crt"` |
| **chain**  string | Specifies or builds a certificate chain file that a client can use to authenticate the profile.  Returned: queried  Sample: `"/Common/default.crt"` |
| **cipher_group**  string | Specifies a cipher group.  Returned: queried |
| **ciphers**  string | Specifies a cipher name.  Returned: queried  Sample: `"DEFAULT"` |
| **crl_file**  string | Specifies the certificate revocation list file name.  Returned: queried |
| **description**  string | Description of the resource.  Returned: queried  Sample: `"My profile"` |
| **expire_cert_response_control**  string | Specifies the BIGIP action when the server certificate has expired.  Returned: queried  Sample: `"drop"` |
| **full_path**  string | Full name of the resource as known to the BIG-IP.  Returned: queried  Sample: `"serverssl"` |
| **generic_alert**  boolean | Enables or disables generic-alert.  Returned: queried  Sample: `true` |
| **handshake_timeout**  string | Specifies the handshake timeout in seconds.  Returned: queried  Sample: `"10"` |
| **key**  string | Specifies the name of the key installed on the traffic management system for the purpose of terminating or initiating an SSL connection.  Returned: queried  Sample: `"/Common/default.key"` |
| **max_active_handshakes**  string | Specifies the maximum number of allowed active SSL handshakes.  Returned: queried  Sample: `"100"` |
| **mod_ssl_methods**  boolean | Enables or disables ModSSL methods.  Returned: queried  Sample: `true` |
| **mode**  boolean | Enables or disables SSL processing.  Returned: queried  Sample: `false` |
| **name**  string | Relative name of the resource in the BIG-IP.  Returned: queried  Sample: `"serverssl"` |
| **ocsp**  string | Specifies the name of the OCSP profile for validating the status of the server certificate.  Returned: queried |
| **options**  list / elements=string | Enables options, including some industry-related workarounds.  Returned: queried  Sample: `["netscape-reuse-cipher-change-bug", "dont-insert-empty-fragments"]` |
| **parent**  string | Profile from which this profile inherits settings.  Returned: queried  Sample: `"serverssl"` |
| **peer_cert_mode**  string | Specifies the peer certificate mode.  Returned: queried  Sample: `"ignore"` |
| **proxy_ssl**  boolean | Allows further modification of application traffic within an SSL tunnel while still allowing the server to perform necessary authorization, authentication, auditing steps.  Returned: queried  Sample: `true` |
| **proxy_ssl_passthrough**  boolean | Allows Proxy SSL to passthrough the traffic when ciphersuite negotiated between the client and server is not supported.  Returned: queried  Sample: `true` |
| **renegotiate_period**  string | Number of seconds from the initial connect time after which the system renegotiates an SSL session.  Returned: queried  Sample: `"indefinite"` |
| **renegotiate_size**  string | Specifies a throughput size of SSL renegotiation, in megabytes.  Returned: queried  Sample: `"indefinite"` |
| **renegotiation**  boolean | Whether renegotiations are enabled.  Returned: queried  Sample: `true` |
| **retain_certificate**  boolean | APM module requires storing certificates in the SSL session. When `no`, a certificate will not be stored in the SSL session.  Returned: queried  Sample: `false` |
| **secure_renegotiation**  string | Specifies the secure renegotiation mode.  Returned: queried  Sample: `"require"` |
| **server_name**  string | Server name to be included in the SNI (server name indication) extension during SSL handshake in ClientHello.  Returned: queried |
| **session_mirroring**  boolean | Enables or disables the mirroring of sessions to the high availability peer.  Returned: queried  Sample: `true` |
| **session_ticket**  boolean | Enables or disables session-ticket.  Returned: queried  Sample: `false` |
| **sni_default**  boolean | When `yes`, this profile is the default SSL profile when the server name in a client connection does not match any configured server names, or a client connection does not specify any server name at all.  Returned: queried  Sample: `true` |
| **sni_require**  boolean | When `yes`, connections to a server that do not support SNI extension will be rejected.  Returned: queried  Sample: `false` |
| **ssl_c3d**  boolean | Enables or disables SSL Client certificate constrained delegation.  Returned: queried  Sample: `true` |
| **ssl_forward_proxy_bypass**  boolean | Enables or disables the ssl-forward-proxy-bypass feature.  Returned: queried  Sample: `true` |
| **ssl_forward_proxy_enabled**  boolean | Enables or disables the ssl-forward-proxy feature.  Returned: queried  Sample: `false` |
| **ssl_sign_hash**  string | Specifies the SSL sign hash algorithm which is used to sign and verify SSL Server Key Exchange and Certificate Verify messages for the specified SSL profiles.  Returned: queried  Sample: `"sha1"` |
| **strict_resume**  boolean | Enables or disables the resumption of SSL sessions after an unclean shutdown.  Returned: queried  Sample: `false` |
| **unclean_shutdown**  boolean | Specifies, when `yes`, that the SSL profile performs unclean shutdowns of all SSL connections. This means underlying TCP connections are closed without exchanging the required SSL shutdown alerts.  Returned: queried  Sample: `true` |
| **untrusted_cert_response_control**  string | Specifies the BIG-IP action when the server certificate has an untrusted CA.  Returned: queried  Sample: `"drop"` |
| **software_hotfixes**  complex | List of software hotfixes.  Returned: When `software-hotfixes` is specified in `gather_subset`.  Sample: `"hash/dictionary of values"` |
| **build**  string | Build number of the image.  This is usually a sub-string of the `name`.  Returned: queried  Sample: `"3.0.1679"` |
| **checksum**  string | MD5 checksum of the image.  Note that this is the checksum stored inside the ISO. It is not the actual checksum of the ISO.  Returned: queried  Sample: `"df1ec715d2089d0fa54c0c4284656a98"` |
| **full_path**  string | Full name of the resource as known to the BIG-IP.  Returned: queried  Sample: `"Hotfix-BIGIP-13.0.0.3.0.1679-HF3.iso"` |
| **id**  string | ID component of the image.  This is usually a sub-string of the `name`.  Returned: queried  Sample: `"HF3"` |
| **name**  string | Name of the image.  Returned: queried  Sample: `"Hotfix-BIGIP-13.0.0.3.0.1679-HF3.iso"` |
| **product**  string | Product contained in the ISO.  Returned: queried  Sample: `"BIG-IP"` |
| **title**  string | Human friendly name of the image.  Returned: queried  Sample: `"Hotfix Version 3.0.1679"` |
| **verified**  boolean | Specifies whether the system has verified this image.  Returned: queried  Sample: `true` |
| **version**  string | Version of software contained in the image.  This is a sub-string of the `name`.  Returned: queried  Sample: `"13.0.0"` |
| **software_images**  complex | List of software images.  Returned: When `software-images` is specified in `gather_subset`.  Sample: `"hash/dictionary of values"` |
| **build**  string | Build number of the image.  This is usually a sub-string of the `name`.  Returned: queried  Sample: `"0.0.1"` |
| **build_date**  string | Date of the build.  Returned: queried  Sample: `"2018-05-05T15:26:30"` |
| **checksum**  string | MD5 checksum of the image.  Note that this is the checksum stored inside the ISO. It is not the actual checksum of the ISO.  Returned: queried  Sample: `"df1ec715d2089d0fa54c0c4284656a98"` |
| **file_size**  integer | Size of the image, in megabytes.  Returned: queried  Sample: `1938` |
| **full_path**  string | Full name of the resource as known to the BIG-IP.  Returned: queried  Sample: `"BIGIP-13.1.0.7-0.0.1.iso"` |
| **last_modified**  string | Last modified date of the ISO.  Returned: queried  Sample: `"2018-05-05T15:26:30"` |
| **name**  string | Name of the image.  Returned: queried  Sample: `"BIGIP-13.1.0.7-0.0.1.iso"` |
| **product**  string | Product contained in the ISO.  Returned: queried  Sample: `"BIG-IP"` |
| **verified**  boolean | Whether or not the system has verified this image.  Returned: queried  Sample: `true` |
| **version**  string | Version of software contained in the image.  This is a sub-string of the `name`.  Returned: queried  Sample: `"13.1.0.7"` |
| **software_volumes**  complex | List of software volumes.  Returned: When `software-volumes` is specified in `gather_subset`.  Sample: `"hash/dictionary of values"` |
| **active**  boolean | Whether the volume is currently active or not.  An active volume contains the currently running version of software.  Returned: queried  Sample: `true` |
| **base_build**  string | Base build version of the software installed in the volume.  When a hotfix is installed, this refers to the base version of software that the hotfix requires.  Returned: queried  Sample: `"0.0.6"` |
| **build**  string | Build version of the software installed in the volume.  Returned: queried  Sample: `"0.0.6"` |
| **default_boot_location**  boolean | Whether this volume is the default boot location or not.  Returned: queried  Sample: `true` |
| **full_path**  string | Full name of the resource as known to the BIG-IP.  Returned: queried  Sample: `"HD1.1"` |
| **name**  string | Relative name of the resource in the BIG-IP.  This usually matches the `full_name`.  Returned: queried  Sample: `"HD1.1"` |
| **product**  string | The F5 product installed in this slot.  This should always be BIG-IP.  Returned: queried  Sample: `"BIG-IP"` |
| **status**  string | Status of the software installed, or being installed, in the volume.  When `complete`, indicates the software has completed installing.  Returned: queried  Sample: `"complete"` |
| **version**  string | Version of software installed in the volume, excluding the `build` number.  Returned: queried  Sample: `"13.1.0.4"` |
| **ssl_certs**  complex | SSL certificate related information.  Returned: When `ssl-certs` is specified in `gather_subset`.  Sample: `"hash/dictionary of values"` |
| **create_time**  string | Specifies the time the file-object was created.  Returned: queried  Sample: `"2018-05-15T21:11:15Z"` |
| **expiration_date**  string | Specifies a string representation of the expiration date of the certificate.  Returned: queried  Sample: `"Aug 13 21:21:29 2031 GMT"` |
| **expiration_timestamp**  integer | Specifies the date this certificate expires. Stored as a POSIX time.  Returned: queried  Sample: `1944422489` |
| **fingerprint**  string | Displays the SHA-256 fingerprint of the certificate.  Returned: queried  Sample: `"SHA256/88:A3:05:...:59:01:EA:5D:B0"` |
| **full_path**  string | Full name of the resource as known to the BIG-IP.  Returned: queried  Sample: `"/Common/cert1"` |
| **is_bundle**  boolean | Specifies whether the certificate file is a bundle (that is, whether it contains more than one certificate).  Returned: queried  Sample: `false` |
| **issuer**  string | Specifies X509 information of the certificate’s issuer.  Returned: queried  Sample: `"emailAddress=support@f5.com,...CN=support.f5.com,"` |
| **key_size**  integer | Specifies the size (in bytes) of the file associated with this file object.  Returned: queried  Sample: `2048` |
| **key_type**  string | Specifies the type of cryptographic key associated with this certificate.  Returned: queried  Sample: `"rsa-private"` |
| **last_update_time**  string | Specifies the last time the file-object was updated/modified.  Returned: queried  Sample: `"2018-05-15T21:11:15Z"` |
| **name**  string | Relative name of the resource in the BIG-IP.  Returned: queried  Sample: `"cert1"` |
| **serial_no**  string | Specifies certificate’s serial number  Returned: queried  Sample: `"1234567890"` |
| **sha1_checksum**  string | SHA1 checksum of the certificate.  Returned: queried  Sample: `"1306e84e1e6a2da53816cefe1f684b80d6be1e3e"` |
| **subject**  string | Specifies X509 information of the certificate’s subject.  Returned: queried  Sample: `"emailAddress=support@f5.com,CN=..."` |
| **subject_alternative_name**  string | Displays the Subject Alternative Name for the certificate.  The X509v3 Subject Alternative Name is embedded in the certificate for X509 extension purposes.  Returned: queried  Sample: `"DNS:www.example.com, DNS:www.example.internal.net"` |
| **system_path**  string | Path on the BIG-IP where the cert can be found.  Returned: queried  Sample: `"/config/ssl/ssl.crt/f5-irule.crt"` |
| **ssl_keys**  complex | SSL certificate related information.  Returned: When `ssl-keys` is specified in `gather_subset`.  Sample: `"hash/dictionary of values"` |
| **full_path**  string | Full name of the resource as known to the BIG-IP.  Returned: queried  Sample: `"/Common/key1"` |
| **key_size**  integer | Specifies the size of the cryptographic key associated with this file object, in bits.  Returned: queried  Sample: `2048` |
| **key_type**  string | Specifies the cryptographic type of the key. That is, which algorithm this key is compatible with.  Returned: queried  Sample: `"rsa-private"` |
| **name**  string | Relative name of the resource in the BIG-IP.  Returned: queried  Sample: `"key1"` |
| **security_type**  string | Specifies the type of security used to handle or store the key.  Returned: queried  Sample: `"normal"` |
| **sha1_checksum**  string | The SHA1 checksum of the key.  Returned: queried  Sample: `"1fcf7de3dd8e834d613099d8e10b2060cd9ecc9f"` |
| **system_path**  string | The path on the filesystem where the key is stored.  Returned: queried  Sample: `"/config/ssl/ssl.key/default.key"` |
| **sync_status**  complex | Configuration Synchronization Status across all Device Groups.  Note that the sync-status works across all device groups - a specific device group cannot be queried for its sync-status.  In general the device-group with the ‘worst’ sync-status will be shown.  Returned: When `sync-status` is specified in `gather_subset`.  Sample: `"hash/dictionary of values"` |
| **color**  string | Sync status color.  Eg. red, blue, green, yellow  Returned: queried  Sample: `"red"` |
| **details**  list / elements=string | A list of all details provided for the current sync-status of the device  Returned: queried  Sample: `[{"Optional action": "Add a device to the trust domain"}]` |
| **mode**  string | Device operation mode (high-availability, standalone)  Returned: queried  Sample: `"['high-availability', 'standalone']"` |
| **recommended_action**  string | The next recommended action to take on the current sync-status.  This field might be empty.  Returned: queried  Sample: `"Synchronize bigip-a.example.com to group some-device-group"` |
| **status**  string | Synchronization Status  Returned: queried  Sample: `"['Changes Pending', 'In Sync', 'Standalone', 'Disconnected']"` |
| **summary**  string | The configuration synchronization status summary  Returned: queried  Sample: `"['The device group is awaiting the initial config sync', 'There is a possible change conflict between ...']"` |
| **system_db**  complex | System DB related information.  Returned: When `system-db` is specified in `gather_subset`.  Sample: `"hash/dictionary of values"` |
| **default**  string | Default value of the key.  Returned: queried  Sample: `"www.f5.com"` |
| **full_path**  string | Full name of the resource as known to the BIG-IP.  Returned: queried  Sample: `"vendor.wwwurl"` |
| **name**  string | Relative name of the resource in the BIG-IP.  Returned: queried  Sample: `"vendor.wwwurl"` |
| **scf_config**  string | Whether the database key would be found in an SCF config or not.  Returned: queried  Sample: `"False"` |
| **value**  string | The value of the key.  Returned: queried  Sample: `"www.f5.com"` |
| **value_range**  string | The accepted range of values for the key.  Returned: queried  Sample: `"string"` |
| **system_info**  complex | Traffic group related information.  Returned: When `traffic-groups` is specified in `gather_subset`.  Sample: `"hash/dictionary of values"` |
| **base_mac_address**  string | Media Access Control address (MAC address) of the device.  Returned: queried  Sample: `"fa:16:3e:c3:42:6f"` |
| **chassis_serial**  string | Serial of the chassis.  Returned: queried  Sample: `"11111111-2222-3333-444444444444"` |
| **hardware_information**  complex | Information related to the hardware (drives and CPUs) of the system.  Returned: queried |
| **model**  string | The model of the hardware.  Returned: queried  Sample: `"Virtual Disk"` |
| **name**  string | The name of the hardware.  Returned: queried  Sample: `"HD1"` |
| **type**  string | The type of hardware.  Returned: queried  Sample: `"physical-disk"` |
| **versions**  complex | Hardware specific properties.  Returned: queried |
| **name**  string | Name of the property.  Returned: queried  Sample: `"Size"` |
| **version**  string | Value of the property.  Returned: queried  Sample: `"154.00G"` |
| **host_board_part_revision**  string | Revision of the host board.  Returned: queried |
| **host_board_serial**  string | Serial of the host board.  Returned: queried |
| **marketing_name**  string | Marketing name of the device platform.  Returned: queried  Sample: `"BIG-IP Virtual Edition"` |
| **package_edition**  string | Displays the software edition.  Returned: queried  Sample: `"Point Release 7"` |
| **package_version**  string | A string combining the `product_build` and `product_build_date`.  Returned: queried  Sample: `"Build 0.0.1 - Tue May 15 15:26:30 PDT 2018"` |
| **platform**  string | Platform identifier.  Returned: queried  Sample: `"Z100"` |
| **product_build**  string | Build version of the release version.  Returned: queried  Sample: `"0.0.1"` |
| **product_build_date**  string | Human readable build date.  Returned: queried  Sample: `"Tue May 15 15:26:30 PDT 2018"` |
| **product_built**  integer | UNIX timestamp of when the product was built.  Returned: queried  Sample: `180515152630` |
| **product_changelist**  integer | Changelist the product branches from.  Returned: queried  Sample: `2557198` |
| **product_code**  string | Code identifying the product.  Returned: queried  Sample: `"BIG-IP"` |
| **product_jobid**  integer | ID of the job that built the product version.  Returned: queried  Sample: `1012030` |
| **product_version**  string | Major product version of the running software.  Returned: queried  Sample: `"13.1.0.7"` |
| **switch_board_part_revision**  string | Switch board revision.  Returned: queried |
| **switch_board_serial**  string | Serial of the switch board.  Returned: queried |
| **time**  complex | Mapping of the current time information to specific time-named keys.  Returned: queried |
| **day**  integer | The current day of the month, in numeric form.  Returned: queried  Sample: `7` |
| **hour**  integer | The current hour of the day in 24-hour format.  Returned: queried  Sample: `18` |
| **minute**  integer | The current minute of the hour.  Returned: queried  Sample: `16` |
| **month**  integer | The current month, in numeric form.  Returned: queried  Sample: `6` |
| **second**  integer | The current second of the minute.  Returned: queried  Sample: `51` |
| **year**  integer | The current year in 4-digit format.  Returned: queried  Sample: `2018` |
| **uptime**  integer | Time since the system booted, in seconds.  Returned: queried  Sample: `603202` |
| **tcp_half_open_monitors**  complex | TCP Half-open monitor related information.  Returned: When `tcp-half-open-monitors` is specified in `gather_subset`.  Sample: `"hash/dictionary of values"` |
| **description**  string | Description of the resource.  Returned: queried  Sample: `"My monitor"` |
| **destination**  string | Specifies the IP address and service port of the resource that is the destination of this monitor.  Returned: queried  Sample: `"*:*"` |
| **full_path**  string | Full name of the resource as known to the BIG-IP.  Returned: queried  Sample: `"/Common/tcp"` |
| **interval**  integer | Specifies, in seconds, the frequency at which the system issues the monitor check when either the resource is down or the status of the resource is unknown.  Returned: queried  Sample: `5` |
| **manual_resume**  boolean | Specifies whether the system automatically changes the status of a resource to up at the next successful monitor check.  Returned: queried  Sample: `true` |
| **name**  string | Relative name of the resource in the BIG-IP.  Returned: queried  Sample: `"tcp"` |
| **parent**  string | Profile from which this profile inherits settings.  Returned: queried  Sample: `"tcp"` |
| **time_until_up**  integer | Specifies the amount of time, in seconds, after the first successful response before a node is marked up.  Returned: queried  Sample: `0` |
| **timeout**  integer | Specifies the number of seconds the target has in which to respond to the monitor request.  Returned: queried  Sample: `16` |
| **transparent**  boolean | Specifies whether the monitor operates in transparent mode.  Returned: queried  Sample: `false` |
| **up_interval**  integer | Specifies, in seconds, the frequency at which the system issues the monitor check when the resource is up.  Returned: queried  Sample: `0` |
| **tcp_monitors**  complex | TCP monitor related information.  Returned: When `tcp-monitors` is specified in `gather_subset`.  Sample: `"hash/dictionary of values"` |
| **adaptive**  boolean | Whether adaptive response time monitoring is enabled for this monitor.  Returned: queried  Sample: `false` |
| **adaptive_divergence_type**  string | Specifies whether the adaptive-divergence-value is `relative` or `absolute`.  Returned: queried  Sample: `"relative"` |
| **adaptive_divergence_value**  integer | Specifies how far from mean latency each monitor probe is allowed to be.  Returned: queried  Sample: `25` |
| **adaptive_limit**  integer | Specifies the hard limit, in milliseconds, which the probe is not allowed to exceed, regardless of the divergence value.  Returned: queried  Sample: `200` |
| **adaptive_sampling_timespan**  integer | Specifies the size of the sliding window, in seconds, which records probe history.  Returned: queried  Sample: `300` |
| **description**  string | Description of the resource.  Returned: queried  Sample: `"My monitor"` |
| **destination**  string | Specifies the IP address and service port of the resource that is the destination of this monitor.  Returned: queried  Sample: `"*:*"` |
| **full_path**  string | Full name of the resource as known to the BIG-IP.  Returned: queried  Sample: `"/Common/tcp"` |
| **interval**  integer | Specifies, in seconds, the frequency at which the system issues the monitor check when either the resource is down or the status of the resource is unknown.  Returned: queried  Sample: `5` |
| **ip_dscp**  integer | Specifies the differentiated services code point (DSCP).  Returned: queried  Sample: `0` |
| **manual_resume**  boolean | Specifies whether the system automatically changes the status of a resource to up at the next successful monitor check.  Returned: queried  Sample: `true` |
| **name**  string | Relative name of the resource in the BIG-IP.  Returned: queried  Sample: `"tcp"` |
| **parent**  string | Profile from which this profile inherits settings.  Returned: queried  Sample: `"tcp"` |
| **reverse**  boolean | Specifies whether the monitor operates in reverse mode. When the monitor is in reverse mode, a successful check marks the monitored object down instead of up.  Returned: queried  Sample: `false` |
| **time_until_up**  integer | Specifies the amount of time, in seconds, after the first successful response before a node is marked up.  Returned: queried  Sample: `0` |
| **timeout**  integer | Specifies the number of seconds the target has in which to respond to the monitor request.  Returned: queried  Sample: `16` |
| **transparent**  boolean | Specifies whether the monitor operates in transparent mode.  Returned: queried  Sample: `false` |
| **up_interval**  integer | Specifies, in seconds, the frequency at which the system issues the monitor check when the resource is up.  Returned: queried  Sample: `0` |
| **tcp_profiles**  complex | TCP profile related information.  Returned: When `tcp-profiles` is specified in `gather_subset`.  Sample: `"hash/dictionary of values"` |
| **abc**  boolean | Appropriate Byte Counting (RFC 3465)  When `yes`, increases the congestion window by basing the amount to increase on the number of previously unacknowledged bytes that each ACK covers.  Returned: queried  Sample: `true` |
| **ack_on_push**  boolean | When `yes`, specifies significantly improved performance to Microsoft Windows and MacOS peers who are writing out on a very small send buffer.  Returned: queried  Sample: `false` |
| **auto_proxy_buffer**  boolean | When `yes`, specifies the system uses the network measurements to set the optimal proxy buffer size.  Returned: queried  Sample: `true` |
| **auto_receive_window**  boolean | When `yes`, specifies the system uses the network measurements to set the optimal receive window size.  Returned: queried  Sample: `false` |
| **auto_send_buffer**  boolean | When `yes`, specifies the system uses the network measurements to set the optimal send buffer size.  Returned: queried  Sample: `true` |
| **close_wait**  string | Specifies the length of time a TCP connection remains in the LAST-ACK state before quitting.  In addition to a numeric value, the value of this fact may also be one of `immediate` or `indefinite`.  When `immediate`, specifies the TCP connection closes immediately after entering the LAST-ACK state.  When `indefinite`, specifies that TCP connections in the LAST-ACK state do not close until they meet the maximum retransmissions timeout.  Returned: queried  Sample: `"indefinite"` |
| **congestion_control**  string | Specifies the algorithm to use to share network resources among competing users to reduce congestion.  Return values may include, `high-speed`, `cdg`, `chd`, `none`, `cubic`, `illinois`, `new-reno`, `reno`, `scalable`, `vegas`, `westwood`, and `woodside`.  Returned: queried  Sample: `"high-speed"` |
| **congestion_metrics_cache**  boolean | When `yes`, specifies the system uses a cache for storing congestion metrics.  Subsequently, because these metrics are already known and cached, the initial slow-start ramp for previously-encountered peers improves.  Returned: queried  Sample: `true` |
| **congestion_metrics_cache_timeout**  integer | Specifies the number of seconds for which entries in the congestion metrics cache are valid.  Returned: queried  Sample: `0` |
| **deferred_accept**  boolean | When `yes`, specifies the system defers allocation of the connection chain context until the system has received the payload from the client.  Enabling this setting is useful in dealing with 3-way handshake denial-of-service attacks.  Returned: queried  Sample: `true` |
| **delay_window_control**  boolean | Specifies the system uses an estimate of queuing delay as a measure of congestion to control, in addition to the normal loss-based control, the amount of data sent.  Returned: queried  Sample: `true` |
| **delayed_acks**  boolean | When checked (enabled), specifies the system can send fewer than one ACK (acknowledgment) segment per data segment received.  Returned: queried  Sample: `true` |
| **description**  string | Description of the resource.  Returned: queried  Sample: `"My profile"` |
| **dont_fragment_flag**  string | Specifies the Don’t Fragment (DF) bit setting in the IP Header of the outgoing TCP packet.  Returned: queried  Sample: `"pmtu"` |
| **dsack**  boolean | D-SACK (RFC 2883)  When `yes`, specifies the use of the selective ACK (SACK) option to acknowledge duplicate segments.  Returned: queried  Sample: `true` |
| **early_retransmit**  boolean | When `yes`, specifies the system uses early retransmit (as specified in RFC 5827) to reduce the recovery time for connections that are receive- buffer or user-data limited.  Returned: queried  Sample: `true` |
| **enhanced_loss_recovery**  boolean | Specifies whether the system uses enhanced loss recovery to recover from random packet losses more effectively.  Returned: queried  Sample: `true` |
| **explicit_congestion_notification**  boolean | When `yes`, specifies the system uses the TCP flags CWR (congestion window reduction) and ECE (ECN-Echo) to notify its peer of congestion and congestion counter-measures.  Returned: queried  Sample: `true` |
| **fast_open**  boolean | When `yes`, specifies, the system supports TCP Fast Open, which reduces latency by allowing a client to include the first packet of data with the SYN  Returned: queried  Sample: `true` |
| **fast_open_cookie_expiration**  integer | Specifies the number of seconds that a Fast Open Cookie delivered to a client is valid for SYN packets from that client.  Returned: queried  Sample: `1000` |
| **fin_wait_1**  string | Specifies the length of time that a TCP connection is in the FIN-WAIT-1 or CLOSING state before quitting.  Returned: queried  Sample: `"indefinite"` |
| **fin_wait_2**  string | Specifies the length of time a TCP connection is in the FIN-WAIT-2 state before quitting.  Returned: queried  Sample: `"100"` |
| **full_path**  string | Full name of the resource as known to the BIG-IP.  Returned: queried  Sample: `"tcp"` |
| **idle_timeout**  string | Specifies the length of time a connection is idle (has no traffic) before the connection is eligible for deletion.  Returned: queried  Sample: `"300"` |
| **initial_congestion_window_size**  integer | Specifies the initial congestion window size for connections to this destination.  Returned: queried  Sample: `3` |
| **initial_receive_window_size**  integer | Specifies the initial receive window size for connections to this destination.  Returned: queried  Sample: `5` |
| **ip_tos**  string | Specifies the L3 Type of Service (ToS) level the system inserts in TCP packets destined for clients.  Returned: queried  Sample: `"mimic"` |
| **keep_alive_interval**  string | Specifies how frequently the system sends data over an idle TCP connection, to determine whether the connection is still valid.  Returned: queried  Sample: `"50"` |
| **limited_transmit_recovery**  boolean | When `yes`, specifies the system uses limited transmit recovery revisions for fast retransmits (as specified in RFC 3042) to reduce the recovery time for connections on a lossy network.  Returned: queried  Sample: `true` |
| **link_qos**  string | Specifies the L2 Quality of Service (QoS) level the system inserts in TCP packets destined for clients.  Returned: queried  Sample: `"200"` |
| **max_segment_retrans**  integer | Specifies the maximum number of times that the system resends data segments.  Returned: queried  Sample: `8` |
| **max_segment_size**  integer | Specifies the largest amount of data the system can receive in a single TCP segment, not including the TCP and IP headers.  Returned: queried  Sample: `1460` |
| **max_syn_retrans**  integer | Specifies the maximum number of times the system resends a SYN packet when it does not receive a corresponding SYN-ACK.  Returned: queried  Sample: `3` |
| **md5_signature**  boolean | When `yes`, specifies to use RFC2385 TCP-MD5 signatures to protect TCP traffic against intermediate tampering.  Returned: queried  Sample: `true` |
| **minimum_rto**  integer | Specifies the minimum length of time the system waits for acknowledgements of data sent before resending the data.  Returned: queried  Sample: `1000` |
| **mptcp_checksum**  boolean | When `yes`, specifies the system calculates the checksum for MPTCP connections.  Returned: queried  Sample: `false` |
| **mptcp_checksum_verify**  boolean | When `yes`, specifies the system verifies the checksum for MPTCP connections.  Returned: queried  Sample: `false` |
| **mptcp_fallback**  string | Specifies an action on fallback, that is, when MPTCP transitions to regular TCP, because something prevents MPTCP from working correctly.  Returned: queried  Sample: `"reset"` |
| **mptcp_fast_join**  boolean | When `yes`, specifies a FAST join, allowing data to be sent on the MP_JOIN_SYN, which can allow a server response to occur in parallel with the JOIN.  Returned: queried  Sample: `false` |
| **mptcp_idle_timeout**  integer | Specifies the number of seconds that an MPTCP connection is idle before the connection is eligible for deletion.  Returned: queried  Sample: `300` |
| **mptcp_join_max**  integer | Specifies the highest number of MPTCP connections that can join to a given connection.  Returned: queried  Sample: `5` |
| **mptcp_make_after_break**  boolean | Specifies make-after-break functionality is supported, allowing for long-lived MPTCP sessions.  Returned: queried  Sample: `false` |
| **mptcp_no_join_dss_ack**  boolean | When checked (enabled), specifies no DSS option is sent on the JOIN ACK.  Returned: queried  Sample: `false` |
| **mptcp_retransmit_min**  integer | Specifies the minimum value (in msec) of the retransmission timer for these MPTCP flows.  Returned: queried  Sample: `1000` |
| **mptcp_rto_max**  integer | Specifies the number of RTOs (retransmission timeouts) before declaring the subflow dead.  Returned: queried  Sample: `5` |
| **mptcp_subflow_max**  integer | Specifies the maximum number of MPTCP subflows for a single flow.  Returned: queried  Sample: `6` |
| **mptcp_timeout**  integer | Specifies, in seconds, the timeout value to discard long-lived sessions that do not have an active flow.  Returned: queried  Sample: `3600` |
| **multipath_tcp**  boolean | When `yes`, specifies the system accepts Multipath TCP (MPTCP) connections, which allow multiple client-side flows to connect to a single server-side flow.  Returned: queried  Sample: `true` |
| **nagle_algorithm**  boolean | Specifies whether the system applies Nagle’s algorithm to reduce the number of short segments on the network.  Returned: queried  Sample: `false` |
| **name**  string | Relative name of the resource in the BIG-IP.  Returned: queried  Sample: `"/Common/tcp"` |
| **parent**  string | Profile from which this profile inherits settings.  Returned: queried  Sample: `"tcp"` |
| **pkt_loss_ignore_burst**  integer | Specifies the probability of performing congestion control when multiple packets are lost, even if the Packet Loss Ignore Rate was not exceeded.  Returned: queried  Sample: `0` |
| **pkt_loss_ignore_rate**  integer | Specifies the threshold of packets lost per million at which the system performs congestion control.  Returned: queried  Sample: `0` |
| **proxy_buffer_high**  integer | Specifies the proxy buffer level, in bytes, at which the receive window is closed.  Returned: queried  Sample: `49152` |
| **proxy_buffer_low**  integer | Specifies the proxy buffer level, in bytes, at which the receive window is opened.  Returned: queried  Sample: `32768` |
| **proxy_max_segment**  boolean | When `yes`, specifies the system attempts to advertise the same maximum segment size (MSS) to the server-side connection as that of the client-side connection.  Returned: queried  Sample: `true` |
| **proxy_options**  boolean | When `yes`, specifies the system advertises an option (such as time stamps) to the server only when the option is negotiated with the client.  Returned: queried  Sample: `false` |
| **push_flag**  string | Specifies how the BIG-IP system receives ACKs.  Returned: queried  Sample: `"default"` |
| **rate_pace**  boolean | When `yes`, specifies the system paces the egress packets to avoid dropping packets, allowing for optimum goodput.  Returned: queried  Sample: `true` |
| **rate_pace_max_rate**  integer | Specifies the maximum rate in bytes per second to which the system paces TCP data transmission.  Returned: queried  Sample: `0` |
| **receive_window**  integer | Specifies the maximum advertised RECEIVE window size.  Returned: queried  Sample: `65535` |
| **reset_on_timeout**  boolean | When `yes`, specifies the system sends a reset packet (RST) in addition to deleting the connection, when a connection exceeds the idle timeout value.  Returned: queried  Sample: `true` |
| **retransmit_threshold**  integer | Specifies the number of duplicate ACKs (retransmit threshold) to start fast recovery.  Returned: queried  Sample: `3` |
| **selective_acks**  boolean | When `yes`, specifies the system processes data using selective ACKs (SACKs) whenever possible, to improve system performance.  Returned: queried  Sample: `true` |
| **selective_nack**  boolean | When `yes`, specifies the system processes data using a selective negative acknowledgment (SNACK) whenever possible, to improve system performance.  Returned: queried  Sample: `true` |
| **send_buffer**  integer | Specifies the SEND window size.  Returned: queried  Sample: `65535` |
| **slow_start**  boolean | When `yes`, specifies the system uses Slow-Start Congestion Avoidance as described in RFC3390 in order to ramp up traffic without causing excessive congestion on the link.  Returned: queried  Sample: `true` |
| **syn_cookie_enable**  boolean | Specifies the default (if no DoS profile is associated) number of embryonic connections that are allowed on any virtual server, before SYN Cookie challenges are enabled for that virtual server.  Returned: queried  Sample: `true` |
| **syn_cookie_white_list**  boolean | Specifies whether or not to use a SYN Cookie WhiteList when doing software SYN Cookies.  Returned: queried  Sample: `false` |
| **syn_retrans_to_base**  integer | Specifies the initial RTO (Retransmission TimeOut) base multiplier for SYN retransmissions.  Returned: queried  Sample: `3000` |
| **tail_loss_probe**  boolean | When `yes`, specifies the system uses Tail Loss Probe to reduce the number of retransmission timeouts.  Returned: queried  Sample: `true` |
| **time_to_live**  string | Specifies the outgoing TCP packet’s IP Header TTL mode.  Returned: queried  Sample: `"proxy"` |
| **time_to_live_v4**  integer | Specifies the outgoing packet’s IP Header TTL value for IPv4 traffic.  Returned: queried  Sample: `255` |
| **time_to_live_v6**  integer | Specifies the outgoing packet’s IP Header TTL value for IPv6 traffic.  Returned: queried  Sample: `64` |
| **time_wait**  string | Specifies the length of time that a TCP connection remains in the TIME-WAIT state before entering the CLOSED state.  Returned: queried  Sample: `"2000"` |
| **time_wait_recycle**  boolean | When `yes`, specifies that connections in a TIME-WAIT state are reused when the system receives a SYN packet, indicating a request for a new connection.  Returned: queried  Sample: `true` |
| **timestamps**  boolean | When `yes`, specifies the system uses the timestamps extension for TCP (as specified in RFC 1323) to enhance high-speed network performance.  Returned: queried  Sample: `true` |
| **verified_accept**  boolean | When `yes`, specifies the system can actually communicate with the server before establishing a client connection.  Returned: queried  Sample: `true` |
| **zero_window_timeout**  string | Specifies the timeout in milliseconds for terminating a connection with an effective zero length TCP transmit window.  Returned: queried  Sample: `"2000"` |
| **traffic_groups**  complex | Traffic group related information.  Returned: When `traffic-groups` is specified in `gather_subset`.  Sample: `"hash/dictionary of values"` |
| **auto_failback_enabled**  boolean | Specifies whether the traffic group fails back to the default device.  Returned: queried  Sample: `true` |
| **auto_failback_time**  integer | Specifies the time required to fail back.  Returned: queried  Sample: `60` |
| **description**  string | Description of the traffic group.  Returned: queried  Sample: `"My traffic group"` |
| **full_path**  string | Full name of the resource as known to the BIG-IP.  Returned: queried  Sample: `"/Common/tg1"` |
| **ha_load_factor**  integer | Specifies a number for this traffic group that represents the load this traffic group presents to the system relative to other traffic groups.  Returned: queried  Sample: `1` |
| **ha_order**  list / elements=string | This list of devices specifies the order in which the devices will become active for the traffic group when a failure occurs.  Returned: queried  Sample: `["/Common/device1", "/Common/device2"]` |
| **is_floating**  boolean | Indicates whether the traffic group can fail over to other devices in the device group.  Returned: queried  Sample: `false` |
| **mac_masquerade_address**  string | Specifies a MAC address for the traffic group.  Returned: queried  Sample: `"00:98:76:54:32:10"` |
| **name**  string | Relative name of the resource in the BIG-IP.  Returned: queried  Sample: `"tg1"` |
| **trunks**  complex | Trunk related information.  Returned: When `trunks` is specified in `gather_subset`.  Sample: `"hash/dictionary of values"` |
| **configured_member_count**  integer | The number of configured members that are associated with the trunk.  Returned: queried  Sample: `1` |
| **description**  string | Description of the Trunk.  Returned: queried  Sample: `"My trunk"` |
| **distribution_hash**  string | The basis for the hash that the system uses as the frame distribution algorithm.  The system uses this hash to determine which interface to use for forwarding traffic.  Returned: queried  Sample: `"src-dst-ipport"` |
| **full_path**  string | Full name of the resource as known to the BIG-IP.  Returned: queried  Sample: `"/Common/trunk1"` |
| **interfaces**  list / elements=string | The list of interfaces that are part of the trunk.  Returned: queried  Sample: `["1.2", "1.3"]` |
| **lacp_enabled**  boolean | Whether LACP is enabled or not.  Returned: queried  Sample: `true` |
| **lacp_mode**  string | The operation mode for LACP.  Returned: queried  Sample: `"passive"` |
| **lacp_timeout**  integer | The rate at which the system sends the LACP control packets.  Returned: queried  Sample: `10` |
| **link_selection_policy**  string | The LACP policy the trunk uses to determine which member link can handle new traffic.  Returned: queried  Sample: `"maximum-bandwidth"` |
| **media_speed**  integer | Speed of the media attached to the trunk.  Returned: queried  Sample: `10000` |
| **media_status**  boolean | Whether the media that is part of the trunk is up or not.  Returned: queried  Sample: `true` |
| **name**  string | Relative name of the resource in the BIG-IP.  Returned: queried  Sample: `"trunk1"` |
| **operational_member_count**  integer | Number of working members associated with the trunk.  Returned: queried  Sample: `1` |
| **stp_enabled**  boolean | Whether Spanning Tree Protocol (STP) is enabled or not.  Returned: queried  Sample: `true` |
| **ucs**  complex  added in f5networks.f5_modules 1.15.0 | UCS backup related information  Returned: When `ucs` is specified in `gather_subset`  Sample: `"hash/dictionary of values"` |
| **encrypted**  boolean | Whether the file is encrypted or not.  Returned: queried  Sample: `false` |
| **file_created_date**  string | Date and time when the ucs file was created.  Returned: queried  Sample: `"2022-03-10T09:30:19Z"` |
| **file_name**  string | Name of the UCS backup file.  Returned: queried  Sample: `"backup.ucs"` |
| **file_size**  string | Size of the UCS file in bytes.  Returned: queried  Sample: `"3"` |
| **udp_profiles**  complex | UDP profile related information.  Returned: When `udp-profiles` is specified in `gather_subset`.  Sample: `"hash/dictionary of values"` |
| **allow_no_payload**  boolean | Allow the passage of datagrams that contain header information, but no essential data.  Returned: queried  Sample: `true` |
| **buffer_max_bytes**  integer | Ingress buffer byte limit. Maximum allowed value is 16777215.  Returned: queried  Sample: `655350` |
| **buffer_max_packets**  integer | Ingress buffer packet limit. Maximum allowed value is 255.  Returned: queried  Sample: `0` |
| **datagram_load_balancing**  boolean | Load balance UDP datagram by datagram  Returned: queried  Sample: `true` |
| **description**  string | Description of the resource.  Returned: queried  Sample: `"My profile"` |
| **full_path**  string | Full name of the resource as known to the BIG-IP.  Returned: queried  Sample: `"udp"` |
| **idle_timeout**  boolean | Number of seconds that a connection is idle before the connection is eligible for deletion.  In addition to a number, may be one of the values `indefinite` or `immediate`.  Returned: queried  Sample: `200` |
| **ip_df_mode**  string | Describes the Don’t Fragment (DF) bit setting in the outgoing UDP packet.  May be one of `pmtu`, `preserve`, `set`, or `clear`.  When `pmtu`, sets the outgoing UDP packet DF big based on the ip pmtu setting.  When `preserve`, preserves the incoming UDP packet Don’t Fragment bit.  When `set`, sets the outgoing UDP packet DF bit.  When `clear`, clears the outgoing UDP packet DF bit.  Returned: queried  Sample: `"pmtu"` |
| **ip_tos_to_client**  string | The Type of Service level the traffic management system assigns to UDP packets when sending them to clients.  May be numeric, or the values `pass-through` or `mimic`.  Returned: queried  Sample: `"mimic"` |
| **ip_ttl_mode**  string | The outgoing UDP packet’s TTL mode.  Valid modes are `proxy`, `preserve`, `decrement`, and `set`.  When `proxy`, sets the IP TTL of IPv4 to the default value of 255 and IPv6 to the default value of 64.  When `preserve`, sets the IP TTL to the original packet TTL value.  When `decrement`, sets the IP TTL to the original packet TTL value minus 1.  When `set`, sets the IP TTL with the specified values in `ip_ttl_v4` and `ip_ttl_v6` values in the same profile.  Returned: queried  Sample: `"proxy"` |
| **ip_ttl_v4**  integer | IPv4 TTL.  Returned: queried  Sample: `10` |
| **ip_ttl_v6**  integer | IPv6 TTL.  Returned: queried  Sample: `100` |
| **link_qos_to_client**  string | The Quality of Service level the system assigns to UDP packets when sending them to clients.  May be either numberic or the value `pass-through`.  Returned: queried  Sample: `"pass-through"` |
| **name**  string | Relative name of the resource in the BIG-IP.  Returned: queried  Sample: `"/Common/udp"` |
| **no_checksum**  boolean | Whether checksum processing is enabled or disabled.  Note that if the datagram is IPv6, the system always performs checksum processing.  Returned: queried  Sample: `true` |
| **parent**  string | Profile from which this profile inherits settings.  Returned: queried  Sample: `"udp"` |
| **proxy_mss**  boolean | When `yes`, specifies the system advertises the same mss to the server as was negotiated with the client.  Returned: queried  Sample: `true` |
| **users**  complex | Details of the users on the system.  Returned: When `users` is specified in `gather_subset`. |
| **description**  string | Description of the resource.  Returned: queried  Sample: `"Admin user"` |
| **full_path**  string | Full name of the resource as known to the BIG-IP.  Returned: queried  Sample: `"admin"` |
| **name**  string | Relative name of the resource in the BIG-IP.  Returned: queried  Sample: `"admin"` |
| **partition_access**  complex | Partition that user has access to, including user role.  Returned: queried |
| **name**  string | Name of partition.  Returned: queried  Sample: `"all-partitions"` |
| **role**  string | Role allowed to user on partition.  Returned: queried  Sample: `"auditor"` |
| **shell**  string | The shell assigned to the user account.  Returned: queried  Sample: `"tmsh"` |
| **vcmp_guests**  complex | vCMP related information.  Returned: When `vcmp-guests` is specified in `gather_subset`.  Sample: `"hash/dictionary of values"` |
| **allowed_slots**  list / elements=string | List of slots the guest is allowed to be assigned to.  Returned: queried  Sample: `[0, 1, 3]` |
| **assigned_slots**  list / elements=string | Slots the guest is assigned to.  Returned: queried  Sample: `[0]` |
| **boot_priority**  integer | Specifies the boot priority of the guest. A lower number means earlier to boot.  Returned: queried  Sample: `65535` |
| **cores_per_slot**  integer | Number of cores the system allocates to the guest.  Returned: queried  Sample: `2` |
| **full_path**  string | Full name of the resource as known to the BIG-IP.  Returned: queried  Sample: `"guest1"` |
| **hostname**  string | FQDN assigned to the guest.  Returned: queried  Sample: `"guest1.localdomain"` |
| **hotfix_image**  string | Hotfix image to install onto any of this guest’s newly created virtual disks.  Returned: queried  Sample: `"Hotfix-BIGIP-12.1.3.4-0.0.2-hf1.iso"` |
| **initial_image**  string | Software image to install onto any of this guest’s newly created virtual disks.  Returned: queried  Sample: `"BIGIP-12.1.3.4-0.0.2.iso"` |
| **mgmt_address**  string | Management IP address configuration for the guest.  Returned: queried  Sample: `"2.3.2.3"` |
| **mgmt_network**  string | Accessibility of this vCMP guest’s management network.  Returned: queried  Sample: `"bridged"` |
| **mgmt_route**  string | Management gateway IP address for the guest.  Returned: queried  Sample: `"2.2.2.1"` |
| **min_number_of_slots**  integer | Specifies the minimum number of slots the guest must be assigned to.  Returned: queried  Sample: `2` |
| **name**  string | Relative name of the resource in the BIG-IP.  Returned: queried  Sample: `"guest1"` |
| **number_of_slots**  integer | Specifies the number of slots the guest should be assigned to.  This number is always greater than, or equal to, `min_number_of_slots`.  Returned: queried  Sample: `2` |
| **ssl_mode**  string | The SSL hardware allocation mode for the guest.  Returned: queried  Sample: `"shared"` |
| **state**  string | Specifies the state of the guest.  May be one of `configured`, `provisioned`, or `deployed`.  Each state implies the actions of all states before it.  Returned: queried  Sample: `"provisioned"` |
| **virtual_disk**  string | The filename of the virtual disk to use for this guest.  Returned: queried  Sample: `"guest1.img"` |
| **vlans**  list / elements=string | List of VLANs on which the guest is either enabled or disabled.  Returned: queried  Sample: `["/Common/vlan1", "/Common/vlan2"]` |
| **virtual_addresses**  complex | Virtual address related information.  Returned: When `virtual-addresses` is specified in `gather_subset`.  Sample: `"hash/dictionary of values"` |
| **address**  string | The virtual IP address.  Returned: queried  Sample: `"2.3.4.5"` |
| **arp_enabled**  boolean | Whether or not ARP is enabled for the specified virtual address.  Returned: queried  Sample: `true` |
| **auto_delete_enabled**  boolean | Indicates if the virtual address will be deleted automatically on deletion of the last associated virtual server or not.  Returned: queried  Sample: `false` |
| **connection_limit**  integer | Concurrent connection limit for one or more virtual servers.  Returned: queried  Sample: `0` |
| **description**  string | The description of the virtual address.  Returned: queried  Sample: `"My virtual address"` |
| **enabled**  boolean | Whether the virtual address is enabled or not.  Returned: queried  Sample: `true` |
| **floating**  boolean | Property derived from the traffic group. A floating virtual address is a virtual address for a VLAN that serves as a shared address by all devices of a BIG-IP traffic-group.  Returned: queried  Sample: `true` |
| **full_path**  string | Full name of the resource as known to the BIG-IP.  Returned: queried  Sample: `"/Common/2.3.4.5"` |
| **icmp_echo**  boolean | Whether the virtual address should reply to ICMP echo requests.  Returned: queried  Sample: `true` |
| **inherited_traffic_group**  boolean | Indicates if the traffic group is inherited from the parent folder.  Returned: queried  Sample: `false` |
| **name**  string | Relative name of the resource in the BIG-IP.  Returned: queried  Sample: `"2.3.4.5"` |
| **netmask**  string | Netmask of the virtual address.  Returned: queried  Sample: `"255.255.255.255"` |
| **route_advertisement**  boolean | Specifies the route advertisement setting for the virtual address.  Returned: queried  Sample: `false` |
| **spanning**  boolean | Whether or not spanning is enabled for the specified virtual address.  Returned: queried  Sample: `false` |
| **traffic_group**  string | Traffic group on which the virtual address is active.  Returned: queried  Sample: `"/Common/traffic-group-1"` |
| **virtual_servers**  complex | Virtual address related information.  Returned: When `virtual-addresses` is specified in `gather_subset`.  Sample: `"hash/dictionary of values"` |
| **authentication_profile**  list / elements=string | Specifies a list of authentication profile names, separated by spaces, that the virtual server uses to manage authentication.  Returned: queried  Sample: `["/Common/ssl_drldp"]` |
| **auto_lasthop**  string | When enabled, allows the system to send return traffic to the MAC address that transmitted the request, even if the routing table points to a different network or interface.  Returned: queried  Sample: `"default"` |
| **availability_status**  string | The availability of the virtual server.  Returned: queried  Sample: `"offline"` |
| **bw_controller_policy**  string | The bandwidth controller for the system to use to enforce a throughput policy for incoming network traffic.  Returned: queried  Sample: `"/Common/bw1"` |
| **client_side_bits_in**  integer | Number of client-side ingress bits.  Returned: queried  Sample: `1000` |
| **client_side_bits_out**  integer | Number of client-side egress bits.  Returned: queried  Sample: `200` |
| **client_side_current_connections**  integer | Number of current connections client-side.  Returned: queried  Sample: `300` |
| **client_side_evicted_connections**  integer | Number of evicted connections client-side.  Returned: queried  Sample: `100` |
| **client_side_max_connections**  integer | Maximum number of connections client-side.  Returned: queried  Sample: `40` |
| **client_side_pkts_in**  integer | Number of client-side ingress packets.  Returned: queried  Sample: `1098384` |
| **client_side_pkts_out**  integer | Number of client-side egress packets.  Returned: queried  Sample: `3484734` |
| **client_side_slow_killed**  integer | Number of slow connections killed, client-side.  Returned: queried  Sample: `234` |
| **client_side_total_connections**  integer | Total number of connections.  Returned: queried  Sample: `24` |
| **cmp_enabled**  boolean | Whether or not clustered multi-processor (CMP) acceleration is enabled.  Returned: queried  Sample: `true` |
| **cmp_mode**  string | The clustered-multiprocessing mode.  Returned: queried  Sample: `"all-cpus"` |
| **connection_limit**  integer | Maximum number of concurrent connections you want to allow for the virtual server.  Returned: queried  Sample: `100` |
| **connection_mirror_enabled**  boolean | Whether or not connection mirroring is enabled.  Returned: queried  Sample: `true` |
| **cpu_usage_ratio_last_1_min**  integer | CPU Usage Ratio (%) Last 1 Minute.  Returned: queried  Sample: `0` |
| **cpu_usage_ratio_last_5_min**  integer | CPU Usage Ratio (%) Last 5 Minutes.  Returned: queried  Sample: `0` |
| **cpu_usage_ratio_last_5_sec**  integer | CPU Usage Ratio (%) Last 5 Seconds.  Returned: queried  Sample: `0` |
| **current_syn_cache**  integer | Current SYN Cache.  Returned: queried  Sample: `0` |
| **default_pool**  string | Pool name you want the virtual server to use as the default pool.  Returned: queried  Sample: `"/Common/pool1"` |
| **description**  string | The description of the virtual server.  Returned: queried  Sample: `"My virtual"` |
| **destination**  string | Name of the virtual address and service on which the virtual server listens for connections.  Returned: queried  Sample: `"/Common/2.2.3.3%1:76"` |
| **destination_address**  string | Address portion of the `destination`.  Returned: queried  Sample: `"2.3.3.2"` |
| **destination_port**  integer | Port potion of the `destination`.  Returned: queried  Sample: `80` |
| **enabled**  boolean | Whether or not the virtual is enabled.  Returned: queried  Sample: `true` |
| **ephemeral_bits_in**  integer | Number of ephemeral ingress bits.  Returned: queried  Sample: `1000` |
| **ephemeral_bits_out**  integer | Number of ephemeral egress bits.  Returned: queried  Sample: `200` |
| **ephemeral_current_connections**  integer | Number of ephemeral current connections.  Returned: queried  Sample: `300` |
| **ephemeral_evicted_connections**  integer | Number of ephemeral evicted connections.  Returned: queried  Sample: `100` |
| **ephemeral_max_connections**  integer | Maximum number of ephemeral connections.  Returned: queried  Sample: `40` |
| **ephemeral_pkts_in**  integer | Number of ephemeral ingress packets.  Returned: queried  Sample: `1098384` |
| **ephemeral_pkts_out**  integer | Number of ephemeral egress packets.  Returned: queried  Sample: `3484734` |
| **ephemeral_slow_killed**  integer | Number of ephemeral slow connections killed.  Returned: queried  Sample: `234` |
| **ephemeral_total_connections**  integer | Total number of ephemeral connections.  Returned: queried  Sample: `24` |
| **fallback_persistence_profile**  string | Fallback persistence profile for the virtual server to use when the default persistence profile is not available.  Returned: queried  Sample: `"/Common/fallback1"` |
| **full_path**  string | Full name of the resource as known to the BIG-IP.  Returned: queried  Sample: `"/Common/2.3.4.5"` |
| **gtm_score**  integer | Specifies a score that is associated with the virtual server.  Returned: queried  Sample: `0` |
| **hardware_syn_cookie_instances**  integer | Hardware SYN Cookie Instances.  Returned: queried  Sample: `0` |
| **ip_intelligence_policy**  string | IP Intelligence policy assigned to the virtual.  Returned: queried  Sample: `"/Common/ip1"` |
| **irules**  list / elements=string | List of iRules that customize the virtual server to direct and manage traffic.  Returned: queried  Sample: `["/Common/rule1", "/Common/rule2'"]` |
| **last_hop_pool**  string | Name of the last hop pool you want the virtual server to use to direct reply traffic to the last hop router.  Returned: queried  Sample: `"/Common/pool1"` |
| **max_conn_duration**  integer | Max Conn Duration/msec.  Returned: queried  Sample: `0` |
| **mean_conn_duration**  integer | Mean Conn Duration/msec.  Returned: queried  Sample: `0` |
| **min_conn_duration**  integer | Min Conn Duration/msec.  Returned: queried  Sample: `0` |
| **name**  string | Relative name of the resource in the BIG-IP.  Returned: queried  Sample: `"2.3.4.5"` |
| **nat64_enabled**  boolean | Whether or not NAT64 is enabled.  Returned: queried  Sample: `true` |
| **persistence_profile**  string | The persistence profile you want the system to use as the default for this virtual server.  Returned: queried  Sample: `"/Common/persist1"` |
| **policies**  list / elements=string | List of LTM policies attached to the virtual server.  Returned: queried  Sample: `["/Common/policy1", "/Common/policy2'"]` |
| **profiles**  complex | List of the profiles attached to the virtual.  Returned: success |
| **context**  string | Which side of the connection the profile affects; either `all`, `client-side` or `server-side`.  Returned: queried  Sample: `"client-side"` |
| **full_path**  string | Full name of the resource as known to the BIG-IP.  Returned: queried  Sample: `"/Common/tcp"` |
| **name**  string | Relative name of the resource in the BIG-IP.  Returned: queried  Sample: `"tcp"` |
| **protocol**  string | IP protocol for which you want the virtual server to direct traffic.  Returned: queried  Sample: `"tcp"` |
| **rate_class**  string | Name of an existing rate class you want the virtual server to use to enforce a throughput policy for incoming network traffic.  Returned: queried |
| **rate_limit**  integer | Maximum number of connections per second allowed for a virtual server.  Returned: queried  Sample: `34` |
| **rate_limit_destination_mask**  integer | Specifies a mask, in bits, to be applied to the destination address as part of the rate limiting.  Returned: queried  Sample: `32` |
| **rate_limit_mode**  string | Indicates whether the rate limit is applied per virtual object, per source address, per destination address, or some combination thereof.  Returned: queried  Sample: `"object"` |
| **rate_limit_source_mask**  integer | Specifies a mask, in bits, to be applied to the source address as part of the rate limiting.  Returned: queried  Sample: `0` |
| **security_log_profiles**  list / elements=string | Specifies the log profile applied to the virtual server.  Returned: queried  Sample: `["/Common/global-network", "/Common/local-dos"]` |
| **snat_pool**  string | Specifies the name of a LSN or SNAT pool used by the specified virtual server.  Returned: queried  Sample: `"/Common/pool1"` |
| **snat_type**  string | Specifies the type of source address translation associated with the specified virtual server.  Returned: queried  Sample: `"none"` |
| **software_syn_cookie_instances**  integer | Software SYN Cookie Instances.  Returned: queried  Sample: `0` |
| **source_address**  string | Specifies an IP address or network from which the virtual server will accept traffic.  Returned: queried  Sample: `"0.0.0./0"` |
| **source_port_behavior**  string | Specifies whether the system preserves the source port of the connection.  Returned: queried  Sample: `"preserve"` |
| **status_reason**  string | If there is a problem with the status of the virtual, it is reported here.  Returned: queried  Sample: `"The children pool member(s) either don't have service checking..."` |
| **syn_cache_overflow**  integer | SYN Cache Overflow.  Returned: queried  Sample: `0` |
| **syn_cookies_status**  string | SYN Cookies Status.  Returned: queried  Sample: `"not-activated"` |
| **total_hardware_accepted_syn_cookies**  integer | SYN Cookies Total Hardware Accepted.  Returned: queried  Sample: `0` |
| **total_hardware_syn_cookies**  integer | SYN Cookies Total Hardware.  Returned: queried  Sample: `0` |
| **total_requests**  integer | Total requests.  Returned: queried  Sample: `8` |
| **total_software_accepted_syn_cookies**  integer | SYN Cookies Total Software Accepted.  Returned: queried  Sample: `0` |
| **total_software_rejected_syn_cookies**  integer | Total Software Rejected.  Returned: queried  Sample: `0` |
| **total_software_syn_cookies**  integer | Total Software SYN Cookies  Returned: queried  Sample: `0` |
| **translate_address**  boolean | Enables or disables address translation for the virtual server.  Returned: queried  Sample: `true` |
| **translate_port**  boolean | Enables or disables port translation.  Returned: queried  Sample: `true` |
| **type**  string | Virtual server type.  Returned: queried  Sample: `"standard"` |
| **vlans**  list / elements=string | List of VLANs on which the virtual server is either enabled or disabled.  Returned: queried  Sample: `["/Common/vlan1", "/Common/vlan2"]` |
| **vlans**  complex | List of VLAN information.  Returned: When `vlans` is specified in `gather_subset`.  Sample: `"hash/dictionary of values"` |
| **auto_lasthop**  string | Allows the system to send return traffic to the MAC address that transmitted the request, even if the routing table points to a different network or interface.  Returned: queried  Sample: `"enabled"` |
| **cmp_hash_algorithm**  string | Specifies how the traffic on the VLAN will be disaggregated.  Returned: queried  Sample: `"default"` |
| **description**  string | Description of the VLAN.  Returned: queried  Sample: `"My vlan"` |
| **failsafe_action**  string | Action for the system to take when the fail-safe mechanism is triggered.  Returned: queried  Sample: `"reboot"` |
| **failsafe_enabled**  boolean | Whether failsafe is enabled or not.  Returned: queried  Sample: `true` |
| **failsafe_timeout**  integer | Number of seconds that an active unit can run without detecting network traffic on this VLAN before it starts a failover.  Returned: queried  Sample: `90` |
| **if_index**  integer | Index assigned to this VLAN. It is a unique identifier assigned for all objects displayed in the SNMP IF-MIB.  Returned: queried  Sample: `176` |
| **interfaces**  complex | List of tagged or untagged interfaces and trunks that you want to configure for the VLAN.  Returned: queried |
| **full_path**  string | Full name of the resource as known to the BIG-IP.  Returned: queried  Sample: `"1.3"` |
| **name**  string | Relative name of the resource in the BIG-IP.  Returned: queried  Sample: `"1.3"` |
| **tagged**  boolean | Whether the interface is tagged or not.  Returned: queried  Sample: `false` |
| **learning_mode**  string | Whether switch ports placed in the VLAN are configured for switch learning, forwarding only, or dropped.  Returned: queried  Sample: `"enable-forward"` |
| **mtu**  integer | Specific maximum transition unit (MTU) for the VLAN.  Returned: queried  Sample: `1500` |
| **sflow_poll_interval**  integer | Maximum interval in seconds between two pollings.  Returned: queried  Sample: `0` |
| **sflow_poll_interval_global**  boolean | Whether the global VLAN poll-interval setting overrides the object-level poll-interval setting.  Returned: queried  Sample: `false` |
| **sflow_sampling_rate**  integer | Ratio of packets observed to the samples generated.  Returned: queried  Sample: `0` |
| **sflow_sampling_rate_global**  boolean | Whether the global VLAN sampling-rate setting overrides the object-level sampling-rate setting.  Returned: queried  Sample: `true` |
| **source_check_enabled**  boolean | Specifies that only connections that have a return route in the routing table are accepted.  Returned: queried  Sample: `true` |
| **tag**  integer | Tag number for the VLAN.  Returned: queried  Sample: `30` |
| **true_mac_address**  string | Media access control (MAC) address for the lowest-numbered interface assigned to this VLAN.  Returned: queried  Sample: `"fa:16:3e:10:da:ff"` |

### Authors

- Tim Rupp (@caphrim007)
- Wojciech Wypior (@wojtek0806)

### Collection links

[Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
[Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
[Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
