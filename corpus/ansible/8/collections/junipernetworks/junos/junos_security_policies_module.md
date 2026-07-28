---
collection: ansible
version: "8"
title: "junipernetworks.junos.junos_security_policies module – Create and manage security policies on Juniper JUNOS devices"
source_url: https://docs.ansible.com/projects/ansible/8/collections/junipernetworks/junos/junos_security_policies_module.html
fetched_at: 2026-07-28T02:39:54+00:00
---
# junipernetworks.junos.junos_security_policies module – Create and manage security policies on Juniper JUNOS devices

> **Note:**
>
> This module is part of the [junipernetworks.junos collection](https://galaxy.ansible.com/ui/repo/published/junipernetworks/junos/) (version 5.3.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install junipernetworks.junos`.
> You need further requirements to be able to use this module,
> see [Requirements](junos_security_policies_module.md#ansible-collections-junipernetworks-junos-junos-security-policies-module-requirements) for details.
>
> To use it in a playbook, specify: `junipernetworks.junos.junos_security_policies`.

New in junipernetworks.junos 2.9.0

- [Synopsis](junos_security_policies_module.md#synopsis)
- [Requirements](junos_security_policies_module.md#requirements)
- [Parameters](junos_security_policies_module.md#parameters)
- [Notes](junos_security_policies_module.md#notes)
- [Examples](junos_security_policies_module.md#examples)
- [Return Values](junos_security_policies_module.md#return-values)

## [Synopsis](junos_security_policies_module.md#id1)

- This module provides declarative creation and management of security policies on Juniper JUNOS devices

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: security_policies

## [Requirements](junos_security_policies_module.md#id2)

The below requirements are needed on the host that executes this module.

- ncclient (>=v0.6.4)
- xmltodict (>=0.12.0)

## [Parameters](junos_security_policies_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | A dictionary of security policies |
| **from_zones**  list / elements=dictionary | List of security zones from which the traffic originates from |
| **name**  string | The name of the security zone from which the traffic originates from |
| **to_zones**  list / elements=dictionary | List of destination security zones of the traffic |
| **name**  string | The name of the destination security zone of the traffic |
| **policies**  list / elements=dictionary | List of policies defined for the associated category |
| **description**  string | Description of the security policy |
| **match**  dictionary | Configure security policy match criteria |
| **application**  dictionary | Specify the IP or remote procedure call (RPC) application or set of applications to be used as match criteria |
| **any**  boolean | Match any predefined or custom applications or application sets  **Choices:**   - `false` - `true` |
| **names**  list / elements=string | Name of the predefined or custom application or application set used as match criteria |
| **destination_address**  dictionary | Define the matching criteria You can specify one or more IP addresses, address sets, or wildcard addresses |
| **addresses**  list / elements=string | IP address, IP address set, or address book entry, or wildcard address (represented as ABCD/wildcard_mask) |
| **any**  boolean | Any IPv4 or IPv6 address  **Choices:**   - `false` - `true` |
| **any_ipv4**  boolean | Any IPv4 address  **Choices:**   - `false` - `true` |
| **any_ipv6**  boolean | Any IPv6 address  **Choices:**   - `false` - `true` |
| **destination_address_excluded**  boolean | Exclude destination addresses  **Choices:**   - `false` - `true` |
| **dynamic_application**  dictionary | Specify the dynamic applications or dynamic application groups used as match criteria within a security policy |
| **any**  boolean | Configuring the dynamic application as any installs the policy with the application as a wildcard (default)  **Choices:**   - `false` - `true` |
| **names**  list / elements=string | Specify dynamic applications or dynamic application groups |
| **none**  boolean | Configuring the dynamic application as none ignores classification results from AppID and does not use the dynamic application in security policy lookups  **Choices:**   - `false` - `true` |
| **from_zone**  dictionary | Identify a single source zone or multiple source zones to be used as a match criteria for a policy |
| **any**  boolean | Match any zone  **Choices:**   - `false` - `true` |
| **junos_host**  boolean | junos-host  **Choices:**   - `false` - `true` |
| **names**  list / elements=string | Name of single or multiple source zone |
| **source_address**  dictionary | Define the matching criteria You can specify one or more IP addresses, address sets, or wildcard addresses |
| **addresses**  list / elements=string | IP address, IP address set, or address book entry, or wildcard address (represented as ABCD/wildcard_mask) |
| **any**  boolean | Any IPv4 or IPv6 address  **Choices:**   - `false` - `true` |
| **any_ipv4**  boolean | Any IPv4 address  **Choices:**   - `false` - `true` |
| **any_ipv6**  boolean | Any IPv6 address  **Choices:**   - `false` - `true` |
| **source_address_excluded**  boolean | Exclude source addresses  **Choices:**   - `false` - `true` |
| **source_end_user_profile**  string | Source end user profile name |
| **source_identity**  dictionary | Identifies users and roles to be used as match criteria for a policy |
| **any**  boolean | Any user or role, as well as the keywords authenticated_user, unauthenticated_user, and unknown_user  **Choices:**   - `false` - `true` |
| **authenticated_user**  boolean | All users and roles that have been authenticated  **Choices:**   - `false` - `true` |
| **names**  list / elements=string | A list of specific users and roles |
| **unauthenticated_user**  boolean | Any user or role that does not have an IP_address mapped to authentication sources and the authentication source is up and running  **Choices:**   - `false` - `true` |
| **unknown_user**  boolean | Any user or role that does not have an IP address mapped to authentication sources, because the authentication source is disconnected from the SRX Series device  **Choices:**   - `false` - `true` |
| **to_zone**  dictionary | Identify a single destination zone or multiple destination zones to be used as a match criteria for a policy |
| **any**  boolean | Match any zone  **Choices:**   - `false` - `true` |
| **junos_host**  boolean | junos-host  **Choices:**   - `false` - `true` |
| **names**  list / elements=string | Name of single or multiple destination zone |
| **url_category**  dictionary | URL category |
| **any**  boolean | Apply to any url category  **Choices:**   - `false` - `true` |
| **names**  list / elements=string | Names of url category to match |
| **none**  boolean | Do not apply to the url category  **Choices:**   - `false` - `true` |
| **name**  string | Name of the policy |
| **scheduler_name**  string | Name of the scheduler to run this policy |
| **then**  dictionary | Specify the policy action to be performed when packets match the defined criteria |
| **count**  boolean | Enable a count, in bytes or kilobytes, of all network traffic the policy allows to pass through the device in both directions; the originating traffic from the client to the server (from the from_zone to the to_zone), and the return traffic from the server to the originating client  **Choices:**   - `false` - `true` |
| **deny**  boolean | Block the service at the firewall The device drops the packets  **Choices:**   - `false` - `true` |
| **log**  dictionary | Log traffic information for a specific policy Traffic information is logged when a session begins (session_init) or closes (session_close) |
| **session_close**  boolean | Enable logging on session close time  **Choices:**   - `false` - `true` |
| **session_init**  boolean | Enable logging on session initialization time  **Choices:**   - `false` - `true` |
| **permit**  dictionary | Block the service at the firewall The device drops the packets |
| **application_services**  dictionary | Enable application services within a security policy |
| **advanced_anti_malware_policy**  string | Specify advanced_anti_malware policy name |
| **application_firewalls**  list / elements=dictionary | Specify the rule sets configured as part of application firewall to be applied to the permitted traffic |
| **rule_set**  string | name of rule set to use |
| **application_traffic_control_rule_set**  string | Specify the rule set configured as part of AppQoS, application_aware quality of service, to be applied to the permitted traffic |
| **gprs_gtp_profile**  string | Specify GPRS tunneling protocol profile name |
| **gprs_sctp_profile**  string | Specify GPRS stream control protocol profile name |
| **icap_redirect**  string | Specify icap redirect profile name |
| **idp**  boolean | Intrusion Detection and Prevention (IDP)  **Choices:**   - `false` - `true` |
| **idp_policy**  string | Specify IDP policy name |
| **packet_capture**  boolean | Option to enable or disable packet capture  **Choices:**   - `false` - `true` |
| **redirect_wx**  boolean | Specify the WX redirection needed for the packets that arrive from the LAN  **Choices:**   - `false` - `true` |
| **reverse_redirect_wx**  boolean | Specify the WX redirection needed for the reverse flow of the packets that arrive from the WAN  **Choices:**   - `false` - `true` |
| **security_intelligence**  dictionary | Specify the security intelligence feed post action |
| **add_destination_identity_to_feed**  string | Add destination user identity to the security feed |
| **add_destination_ip_to_feed**  string | Add the destination IP address to the security feed |
| **add_source_identity_to_feed**  string | Add source user identity to the security feed |
| **add_source_ip_to_feed**  string | Add the source IP address to the security feed |
| **security_intelligence_policy**  string | Specify security_intelligence policy name |
| **ssl_proxy**  dictionary | You can apply a redirect SSL proxy profile when a policy blocks HTTPS traffic with a reject action |
| **enable**  boolean | Enable SSL proxy  **Choices:**   - `false` - `true` |
| **profile_name**  string | Name of SSL proxy profile |
| **uac_policy**  dictionary | Enable Unified Access Control (UAC) for the security policy |
| **captive_portal**  string | Specify the preconfigured security policy for captive portal on the Junos OS Enforcer to enable the captive portal feature |
| **enable**  boolean | Enable Unified Access Control (UAC)  **Choices:**   - `false` - `true` |
| **utm_policy**  string | Specify UTM policy name |
| **destination_address**  string | Specify whether the traffic permitted by the security policy is limited to packets where the destination IP address has been translated by means of a destination NAT rule or to packets where the destination IP address has not been translated  **Choices:**   - `"drop-translated"` - `"drop-untranslated"` |
| **firewall_authentication**  dictionary | Configure firewall authentication methods |
| **pass_through**  dictionary | Configure pass-through firewall user authentication |
| **access_profile**  string | Specify the name of the access profile |
| **auth_only_browser**  boolean | Configure firewall authentication to ignore non-browser HTTP/HTTPS traffic  **Choices:**   - `false` - `true` |
| **auth_user_agent**  string | Specify a user-agent value to be used to verify that the user’s browser traffic is HTTP/HTTPS traffic |
| **client_match**  string | Specify the name of the users or user groups in a profile who are allowed access by this policy |
| **ssl_termination_profile**  string | Specify the SSL termination profile used for SSL offloading |
| **web_redirect**  boolean | Enable redirecting an HTTP request to the device and redirecting the client system to a webpage for authentication  **Choices:**   - `false` - `true` |
| **web_redirect_to_https**  boolean | Redirect unauthenticated HTTP requests to the internal HTTPS Web server of the device  **Choices:**   - `false` - `true` |
| **push_to_identity_management**  boolean | enables pushing to identity management devices  **Choices:**   - `false` - `true` |
| **user_firewall**  dictionary | Configure user role firewall authentication, and map the source IP address to the username and its associated roles (groups) |
| **access_profile**  string | Specify the name of the access profile to be used for authentication |
| **auth_only_browser**  boolean | Configure firewall authentication to ignore non-browser HTTP/HTTPS traffic  **Choices:**   - `false` - `true` |
| **auth_user_agent**  string | Specify a user-agent value to be used to verify that the user’s browser traffic is HTTP/HTTPS traffic |
| **domain**  string | Specify the name of the domain where firewall authentication occurs in the event that the Windows Management Instrumentation client (WMIC) is not available to get IP_to_user mapping for the integrated user firewall feature |
| **ssl_termination_profile**  string | For HTTPS traffic, specify the name of the SSL termination profile used for SSL offloading |
| **web_redirect**  boolean | Enable webpage redirection  **Choices:**   - `false` - `true` |
| **web_redirect_to_https**  boolean | Enable redirection to HTTPS  **Choices:**   - `false` - `true` |
| **web_authentication**  list / elements=string | Specify that the policy allows access to users or user groups who have previously been authenticated by Web authentication |
| **tcp_options**  dictionary | Specify the TCP options for each policy You can configure sync and sequence checks for each policy based on your requirements, and, because each policy has two directions, you can configure a TCP MSS value for both directions or for just one direction |
| **initial_tcp_mss**  integer | Configure the TCP maximum segment size (MSS) for packets that arrive at the ingress interface (initial direction), match a specific policy, and for which a session is created |
| **reverse_tcp_mss**  integer | Configure the TCP maximum segment size (MSS) for packets that match a specific policy and travel in the reverse direction of a session |
| **sequence_check_required**  boolean | Enable sequence check per policy The sequence_check_required value overrides the global value no_sequence_check  **Choices:**   - `false` - `true` |
| **syn_check_required**  boolean | Enable sync check per policy The syn_check_required value overrides the global value no_syn_check  **Choices:**   - `false` - `true` |
| **window_scale**  boolean | Enable window_scale per policy  **Choices:**   - `false` - `true` |
| **tunnel**  dictionary | Encapsulate outgoing IP packets and decapsulate incoming IP packets |
| **ipsec_vpn**  string | name of the ipsec policy |
| **pair_policy**  string | name of the pair policy |
| **reject**  dictionary | Block the service at the firewall The device drops the packet and sends a TCP reset (RST) segment to the source host for TCP traffic and an ICMP “destination unreachable, port unreachable” message (type 3, code 3) for UDP traffic |
| **enable**  boolean | Enable rejection of packets based on match criteria  **Choices:**   - `false` - `true` |
| **profile**  string | You can chose to provide a notification to the clients or redirect client request to an informative Web page when a policy blocks HTTP or HTTPS traffic with a deny or reject action |
| **ssl_proxy**  dictionary | You can apply a redirect SSL proxy profile when a policy blocks HTTPS traffic with a reject action When you apply am SSL proxy profile, SSL proxy decrypts the traffic and application identification functionality identifies the application |
| **enable**  boolean | Enable SSL proxy  **Choices:**   - `false` - `true` |
| **profile_name**  string | Name of SSL proxy profile |
| **global**  dictionary | List of global security policies |
| **policies**  list / elements=dictionary | List of policies defined for the associated category |
| **description**  string | Description of the security policy |
| **match**  dictionary | Configure security policy match criteria |
| **application**  dictionary | Specify the IP or remote procedure call (RPC) application or set of applications to be used as match criteria |
| **any**  boolean | Match any predefined or custom applications or application sets  **Choices:**   - `false` - `true` |
| **names**  list / elements=string | Name of the predefined or custom application or application set used as match criteria |
| **destination_address**  dictionary | Define the matching criteria You can specify one or more IP addresses, address sets, or wildcard addresses |
| **addresses**  list / elements=string | IP address, IP address set, or address book entry, or wildcard address (represented as ABCD/wildcard_mask) |
| **any**  boolean | Any IPv4 or IPv6 address  **Choices:**   - `false` - `true` |
| **any_ipv4**  boolean | Any IPv4 address  **Choices:**   - `false` - `true` |
| **any_ipv6**  boolean | Any IPv6 address  **Choices:**   - `false` - `true` |
| **destination_address_excluded**  boolean | Exclude destination addresses  **Choices:**   - `false` - `true` |
| **dynamic_application**  dictionary | Specify the dynamic applications or dynamic application groups used as match criteria within a security policy |
| **any**  boolean | Configuring the dynamic application as any installs the policy with the application as a wildcard (default)  **Choices:**   - `false` - `true` |
| **names**  list / elements=string | Specify dynamic applications or dynamic application groups |
| **none**  boolean | Configuring the dynamic application as none ignores classification results from AppID and does not use the dynamic application in security policy lookups  **Choices:**   - `false` - `true` |
| **from_zone**  dictionary | Identify a single source zone or multiple source zones to be used as a match criteria for a policy |
| **any**  boolean | Match any zone  **Choices:**   - `false` - `true` |
| **junos_host**  boolean | junos-host  **Choices:**   - `false` - `true` |
| **names**  list / elements=string | Name of single or multiple source zone |
| **source_address**  dictionary | Define the matching criteria You can specify one or more IP addresses, address sets, or wildcard addresses |
| **addresses**  list / elements=string | IP address, IP address set, or address book entry, or wildcard address (represented as ABCD/wildcard_mask) |
| **any**  boolean | Any IPv4 or IPv6 address  **Choices:**   - `false` - `true` |
| **any_ipv4**  boolean | Any IPv4 address  **Choices:**   - `false` - `true` |
| **any_ipv6**  boolean | Any IPv6 address  **Choices:**   - `false` - `true` |
| **source_address_excluded**  boolean | Exclude source addresses  **Choices:**   - `false` - `true` |
| **source_end_user_profile**  string | Source end user profile name |
| **source_identity**  dictionary | Identifies users and roles to be used as match criteria for a policy |
| **any**  boolean | Any user or role, as well as the keywords authenticated_user, unauthenticated_user, and unknown_user  **Choices:**   - `false` - `true` |
| **authenticated_user**  boolean | All users and roles that have been authenticated  **Choices:**   - `false` - `true` |
| **names**  list / elements=string | A list of specific users and roles |
| **unauthenticated_user**  boolean | Any user or role that does not have an IP_address mapped to authentication sources and the authentication source is up and running  **Choices:**   - `false` - `true` |
| **unknown_user**  boolean | Any user or role that does not have an IP address mapped to authentication sources, because the authentication source is disconnected from the SRX Series device  **Choices:**   - `false` - `true` |
| **to_zone**  dictionary | Identify a single destination zone or multiple destination zones to be used as a match criteria for a policy |
| **any**  boolean | Match any zone  **Choices:**   - `false` - `true` |
| **junos_host**  boolean | junos-host  **Choices:**   - `false` - `true` |
| **names**  list / elements=string | Name of single or multiple destination zone |
| **url_category**  dictionary | URL category |
| **any**  boolean | Apply to any url category  **Choices:**   - `false` - `true` |
| **names**  list / elements=string | Names of url category to match |
| **none**  boolean | Do not apply to the url category  **Choices:**   - `false` - `true` |
| **name**  string | Name of the policy |
| **scheduler_name**  string | Name of the scheduler to run this policy |
| **then**  dictionary | Specify the policy action to be performed when packets match the defined criteria |
| **count**  boolean | Enable a count, in bytes or kilobytes, of all network traffic the policy allows to pass through the device in both directions; the originating traffic from the client to the server (from the from_zone to the to_zone), and the return traffic from the server to the originating client  **Choices:**   - `false` - `true` |
| **deny**  boolean | Block the service at the firewall The device drops the packets  **Choices:**   - `false` - `true` |
| **log**  dictionary | Log traffic information for a specific policy Traffic information is logged when a session begins (session_init) or closes (session_close) |
| **session_close**  boolean | Enable logging on session close time  **Choices:**   - `false` - `true` |
| **session_init**  boolean | Enable logging on session initialization time  **Choices:**   - `false` - `true` |
| **permit**  dictionary | Block the service at the firewall The device drops the packets |
| **application_services**  dictionary | Enable application services within a security policy |
| **advanced_anti_malware_policy**  string | Specify advanced_anti_malware policy name |
| **application_firewalls**  list / elements=dictionary | Specify the rule sets configured as part of application firewall to be applied to the permitted traffic |
| **rule_set**  string | name of rule set to use |
| **application_traffic_control_rule_set**  string | Specify the rule set configured as part of AppQoS, application_aware quality of service, to be applied to the permitted traffic |
| **gprs_gtp_profile**  string | Specify GPRS tunneling protocol profile name |
| **gprs_sctp_profile**  string | Specify GPRS stream control protocol profile name |
| **icap_redirect**  string | Specify icap redirect profile name |
| **idp**  boolean | Intrusion Detection and Prevention (IDP)  **Choices:**   - `false` - `true` |
| **idp_policy**  string | Specify IDP policy name |
| **packet_capture**  boolean | Option to enable or disable packet capture  **Choices:**   - `false` - `true` |
| **redirect_wx**  boolean | Specify the WX redirection needed for the packets that arrive from the LAN  **Choices:**   - `false` - `true` |
| **reverse_redirect_wx**  boolean | Specify the WX redirection needed for the reverse flow of the packets that arrive from the WAN  **Choices:**   - `false` - `true` |
| **security_intelligence**  dictionary | Specify the security intelligence feed post action |
| **add_destination_identity_to_feed**  string | Add destination user identity to the security feed |
| **add_destination_ip_to_feed**  string | Add the destination IP address to the security feed |
| **add_source_identity_to_feed**  string | Add source user identity to the security feed |
| **add_source_ip_to_feed**  string | Add the source IP address to the security feed |
| **security_intelligence_policy**  string | Specify security_intelligence policy name |
| **ssl_proxy**  dictionary | You can apply a redirect SSL proxy profile when a policy blocks HTTPS traffic with a reject action |
| **enable**  boolean | Enable SSL proxy  **Choices:**   - `false` - `true` |
| **profile_name**  string | Name of SSL proxy profile |
| **uac_policy**  dictionary | Enable Unified Access Control (UAC) for the security policy |
| **captive_portal**  string | Specify the preconfigured security policy for captive portal on the Junos OS Enforcer to enable the captive portal feature |
| **enable**  boolean | Enable Unified Access Control (UAC)  **Choices:**   - `false` - `true` |
| **utm_policy**  string | Specify UTM policy name |
| **destination_address**  string | Specify whether the traffic permitted by the security policy is limited to packets where the destination IP address has been translated by means of a destination NAT rule or to packets where the destination IP address has not been translated  **Choices:**   - `"drop-translated"` - `"drop-untranslated"` |
| **firewall_authentication**  dictionary | Configure firewall authentication methods |
| **pass_through**  dictionary | Configure pass-through firewall user authentication |
| **access_profile**  string | Specify the name of the access profile |
| **auth_only_browser**  boolean | Configure firewall authentication to ignore non-browser HTTP/HTTPS traffic  **Choices:**   - `false` - `true` |
| **auth_user_agent**  string | Specify a user-agent value to be used to verify that the user’s browser traffic is HTTP/HTTPS traffic |
| **client_match**  string | Specify the name of the users or user groups in a profile who are allowed access by this policy |
| **ssl_termination_profile**  string | Specify the SSL termination profile used for SSL offloading |
| **web_redirect**  boolean | Enable redirecting an HTTP request to the device and redirecting the client system to a webpage for authentication  **Choices:**   - `false` - `true` |
| **web_redirect_to_https**  boolean | Redirect unauthenticated HTTP requests to the internal HTTPS Web server of the device  **Choices:**   - `false` - `true` |
| **push_to_identity_management**  boolean | enables pushing to identity management devices  **Choices:**   - `false` - `true` |
| **user_firewall**  dictionary | Configure user role firewall authentication, and map the source IP address to the username and its associated roles (groups) |
| **access_profile**  string | Specify the name of the access profile to be used for authentication |
| **auth_only_browser**  boolean | Configure firewall authentication to ignore non-browser HTTP/HTTPS traffic  **Choices:**   - `false` - `true` |
| **auth_user_agent**  string | Specify a user-agent value to be used to verify that the user’s browser traffic is HTTP/HTTPS traffic |
| **domain**  string | Specify the name of the domain where firewall authentication occurs in the event that the Windows Management Instrumentation client (WMIC) is not available to get IP_to_user mapping for the integrated user firewall feature |
| **ssl_termination_profile**  string | For HTTPS traffic, specify the name of the SSL termination profile used for SSL offloading |
| **web_redirect**  boolean | Enable webpage redirection  **Choices:**   - `false` - `true` |
| **web_redirect_to_https**  boolean | Enable redirection to HTTPS  **Choices:**   - `false` - `true` |
| **web_authentication**  list / elements=string | Specify that the policy allows access to users or user groups who have previously been authenticated by Web authentication |
| **tcp_options**  dictionary | Specify the TCP options for each policy You can configure sync and sequence checks for each policy based on your requirements, and, because each policy has two directions, you can configure a TCP MSS value for both directions or for just one direction |
| **initial_tcp_mss**  integer | Configure the TCP maximum segment size (MSS) for packets that arrive at the ingress interface (initial direction), match a specific policy, and for which a session is created |
| **reverse_tcp_mss**  integer | Configure the TCP maximum segment size (MSS) for packets that match a specific policy and travel in the reverse direction of a session |
| **sequence_check_required**  boolean | Enable sequence check per policy The sequence_check_required value overrides the global value no_sequence_check  **Choices:**   - `false` - `true` |
| **syn_check_required**  boolean | Enable sync check per policy The syn_check_required value overrides the global value no_syn_check  **Choices:**   - `false` - `true` |
| **window_scale**  boolean | Enable window_scale per policy  **Choices:**   - `false` - `true` |
| **tunnel**  dictionary | Encapsulate outgoing IP packets and decapsulate incoming IP packets |
| **ipsec_vpn**  string | name of the ipsec policy |
| **pair_policy**  string | name of the pair policy |
| **reject**  dictionary | Block the service at the firewall The device drops the packet and sends a TCP reset (RST) segment to the source host for TCP traffic and an ICMP “destination unreachable, port unreachable” message (type 3, code 3) for UDP traffic |
| **enable**  boolean | Enable rejection of packets based on match criteria  **Choices:**   - `false` - `true` |
| **profile**  string | You can chose to provide a notification to the clients or redirect client request to an informative Web page when a policy blocks HTTP or HTTPS traffic with a deny or reject action |
| **ssl_proxy**  dictionary | You can apply a redirect SSL proxy profile when a policy blocks HTTPS traffic with a reject action When you apply am SSL proxy profile, SSL proxy decrypts the traffic and application identification functionality identifies the application |
| **enable**  boolean | Enable SSL proxy  **Choices:**   - `false` - `true` |
| **profile_name**  string | Name of SSL proxy profile |
| **running_config**  string | This option is used only with state *parsed*  The value of this option should be the output received from the JunOS device by executing the command **show configuration security policies**  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result |
| **state**  string | The state the configuration should be left in  The states *rendered*, *gathered* and *parsed* does not perform any change on the device  The state *rendered* will transform the configuration in `config` option to platform specific CLI commands which will be returned in the *rendered* key within the result For state *rendered* active connection to remote host is not required  The state *replaced* will replace the running configuration with the provided configuration  The state *replaced* and state *overridden* have the same behaviour  The state *gathered* will fetch the running configuration from device and transform it into structured data in the format as per the resource module argspec and the value is returned in the *gathered* key within the result  The state *parsed* reads the configuration from `running_config` option and transforms it into JSON format as per the resource module parameters and the value is returned in the *parsed* key within the result The value of `running_config` option should be the same format as the output of command *show security policies detail* executed on device For state *parsed* active connection to remote host is not required  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"rendered"` - `"gathered"` - `"parsed"` |

## [Notes](junos_security_policies_module.md#id4)

> **Note:**
>
> - This module requires the netconf system service be enabled on the device being managed
> - This module works with connection `netconf`
> - See [the Junos OS Platform Options](https://docsansiblecom/ansible/latest/network/user_guide/platform_junoshtml)
> - Tested against JunOS v18.4R1

## [Examples](junos_security_policies_module.md#id5)

```yaml+jinja
# Using merged
#
# Before state
# ------------
#
# vagrant@vsrx> show security policies
# Default policy: deny-all
# Pre ID default policy: permit-all
# Global policies:
# Policy: test_glob, State: enabled, Index: 4, Scope Policy: 0, Sequence number: 1
#   From zones: any
#     To zones: any
#     Source addresses: any-ipv4
#     Destination addresses: any-ipv4
#     Applications: any
#     Action: deny
#
# vagrant@vsrx> show security zones
#
# Security zone: one
# Send reset for non-SYN session TCP packets: Off
# Policy configurable: Yes
# Interfaces bound: 1
# Interfaces:
# ge-0/0/0.0
#
# Security zone: three
# Send reset for non-SYN session TCP packets: Off
# Policy configurable: Yes
# Interfaces bound: 1
# Interfaces:
# ge-0/0/2.0
#
# Security zone: two
# Send reset for non-SYN session TCP packets: Off
# Policy configurable: Yes
# Interfaces bound: 1
# Interfaces:
# ge-0/0/1.0
#
# Security zone: junos-host
# Send reset for non-SYN session TCP packets: Off
# Policy configurable: Yes
# Interfaces bound: 0
# Interfaces:
#
- junipernetworks.junos.junos_security_policies:
    config:
      from_zones:
        - name: one
          to_zones:
            - name: two
              policies:
                - match:
                    application:
                      names:
                        - junos-dhcp-relay
                        - junos-finger
                    destination_address:
                      addresses:
                        - a2
                        - a4
                    destination_address_excluded: true
                    dynamic_application:
                      names:
                        - any
                    source_address:
                      addresses:
                        - a1
                        - a3
                    source_address_excluded: true
                    source_end_user_profile: test_end_user_profile
                    source_identity:
                      unknown_user: true
                    url_category:
                      names:
                        - Enhanced_Web_Chat
                  name: test_policy_1
                  then:
                    count: true
                    deny: true
                    log: session-close
                - match:
                    application:
                      any: true
                    destination_address:
                      any_ipv6: true
                    source_address:
                      addresses:
                        - a1
                  name: test_policy_2
                  then:
                    reject:
                      enable: true
                      profile: test_dyn_app
                      ssl_proxy:
                        enable: true
                        profile_name: SECURITY-SSL-PROXY
            - name: three
              policies:
                - match:
                    application:
                      any: true
                    destination_address:
                      addresses:
                        - a2
                    source_address:
                      addresses:
                        - a1
                  name: test_policy_3
                  then:
                    permit:
                      application_services:
                        application_traffic_control_rule_set: test_traffic_control
                        gprs_gtp_profile: gtp1
                        icap_redirect: test_icap
                        reverse_redirect_wx: 'True'
                        uac_policy:
                          enable: true
                      firewall_authentication:
                        push_to_identity_management: true
                        web_authentication:
                          - FWClient1
                      tcp_options:
                        initial_tcp_mss: 64
                        window_scale: true
      global:
        policies:
          - match:
              application:
                any: true
              destination_address:
                any_ipv6: true
              source_address:
                any_ipv6: true
            name: test_glob_1
            then:
              deny: true
          - match:
              application:
                any: true
              destination_address:
                any_ipv6: true
              source_address:
                any_ipv6: true
            name: test_glob_2
            then:
              deny: true
    state: merged
#
# -------------------------
# Module Execution Result
# -------------------------
#   "after": {
#     "from_zones": [
#       {
#         "name": "one",
#         "to_zones": [
#           {
#             "name": "two",
#             "policies": [
#               {
#                 "match": {
#                   "application": {
#                     "names": [
#                       "junos-dhcp-relay",
#                       "junos-finger"
#                     ]
#                   },
#                   "destination_address": {
#                     "addresses": [
#                       "a2",
#                       "a4"
#                     ]
#                   },
#                   "destination_address_excluded": true,
#                   "dynamic_application": {
#                     "names": [
#                       "any"
#                     ]
#                   },
#                   "source_address": {
#                     "addresses": [
#                       "a1",
#                       "a3"
#                     ]
#                   },
#                   "source_address_excluded": true,
#                   "source_end_user_profile": "test_end_user_profile",
#                   "source_identity": {
#                     "unknown_user": true
#                   },
#                   "url_category": {
#                     "names": [
#                       "Enhanced_Web_Chat"
#                     ]
#                   }
#                 },
#                 "name": "test_policy_1",
#                 "then": {
#                   "count": true,
#                   "deny": true,
#                   "log": "session-close"
#                 }
#               },
#               {
#                 "match": {
#                   "application": {
#                     "any": true
#                   },
#                   "destination_address": {
#                     "any_ipv6": true
#                   },
#                   "source_address": {
#                     "addresses": [
#                       "a1"
#                     ]
#                   }
#                 },
#                 "name": "test_policy_2",
#                 "then": {
#                   "reject": {
#                     "enable": true,
#                     "profile": "test_dyn_app",
#                     "ssl_proxy": {
#                       "enable": true,
#                       "profile_name": "SECURITY-SSL-PROXY"
#                     }
#                   }
#                 }
#               }
#             ]
#           },
#           {
#             "name": "three",
#             "policies": [
#               {
#                 "match": {
#                   "application": {
#                     "any": true
#                   },
#                   "destination_address": {
#                     "addresses": [
#                       "a2"
#                     ]
#                   },
#                   "source_address": {
#                     "addresses": [
#                       "a1"
#                     ]
#                   }
#                 },
#                 "name": "test_policy_3",
#                 "then": {
#                   "permit": {
#                     "application_services": {
#                       "application_traffic_control_rule_set": "test_traffic_control",
#                       "gprs_gtp_profile": "gtp1",
#                       "icap_redirect": "test_icap",
#                       "reverse_redirect_wx": "True",
#                       "uac_policy": {
#                         "enable": true
#                       }
#                     },
#                     "firewall_authentication": {
#                       "push_to_identity_management": true,
#                       "web_authentication": [
#                         "FWClient1"
#                       ]
#                     },
#                     "tcp_options": {
#                       "initial_tcp_mss": 64,
#                       "window_scale": true
#                     }
#                   }
#                 }
#               }
#             ]
#           }
#         ]
#       }
#     ],
#     "global": {
#       "policies": [
#         {
#           "match": {
#             "application": {
#               "any": true
#             },
#             "destination_address": {
#               "any_ipv4": true
#             },
#             "source_address": {
#               "any_ipv4": true
#             }
#           },
#           "name": "test_glob",
#           "then": {
#             "deny": true
#           }
#         },
#         {
#           "match": {
#             "application": {
#               "any": true
#             },
#             "destination_address": {
#               "any_ipv6": true
#             },
#             "source_address": {
#               "any_ipv6": true
#             }
#           },
#           "name": "test_glob_1",
#           "then": {
#             "deny": true
#           }
#         },
#         {
#           "match": {
#             "application": {
#               "any": true
#             },
#             "destination_address": {
#               "any_ipv6": true
#             },
#             "source_address": {
#               "any_ipv6": true
#             }
#           },
#           "name": "test_glob_2",
#           "then": {
#             "deny": true
#           }
#         }
#       ]
#     }
#   },
#   "before": {
#     "global": {
#       "policies": [
#         {
#           "match": {
#             "application": {
#               "any": true
#             },
#             "destination_address": {
#               "any_ipv4": true
#             },
#             "source_address": {
#               "any_ipv4": true
#             }
#           },
#           "name": "test_glob",
#           "then": {
#             "deny": true
#           }
#         }
#       ]
#     }
#   },
#   "changed": true,
#   "commands": "<nc:security
#                   xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
#                   <nc:policies>
#                     <nc:policy>
#                       <nc:from-zone-name>one</nc:from-zone-name>
#                       <nc:to-zone-name>two</nc:to-zone-name>
#                       <nc:policy>
#                         <nc:name>test_policy_1</nc:name>
#                         <nc:match>
#                           <nc:source-address>a1</nc:source-address>
#                           <nc:source-address>a3</nc:source-address>
#                           <nc:source-address-excluded/>
#                           <nc:destination-address>a2</nc:destination-address>
#                           <nc:destination-address>a4</nc:destination-address>
#                           <nc:destination-address-excluded/>
#                           <nc:application>junos-dhcp-relay</nc:application>
#                           <nc:application>junos-finger</nc:application>
#                           <nc:source-end-user-profile>test_end_user_profile</nc:source-end-user-profile>
#                           <nc:source-identity>unknown-user</nc:source-identity>
#                           <nc:url-category>Enhanced_Web_Chat</nc:url-category>
#                           <nc:dynamic-application>any</nc:dynamic-application>
#                         </nc:match>
#                         <nc:then>
#                           <nc:deny/>
#                           <nc:count></nc:count>
#                           <nc:log>
#                             <nc:session-close/>
#                           </nc:log>
#                         </nc:then>
#                       </nc:policy>
#                       <nc:policy>
#                         <nc:name>test_policy_2</nc:name>
#                         <nc:match>
#                           <nc:source-address>a1</nc:source-address>
#                           <nc:destination-address>any-ipv6</nc:destination-address>
#                           <nc:application>any</nc:application>
#                         </nc:match>
#                         <nc:then>
#                           <nc:reject>
#                             <nc:profile>test_dyn_app</nc:profile>
#                             <nc:ssl-proxy>
#                               <nc:profile-name>SECURITY-SSL-PROXY</nc:profile-name>
#                             </nc:ssl-proxy>
#                           </nc:reject>
#                         </nc:then>
#                       </nc:policy>
#                     </nc:policy>
#                     <nc:policy>
#                       <nc:from-zone-name>one</nc:from-zone-name>
#                       <nc:to-zone-name>three</nc:to-zone-name>
#                       <nc:policy>
#                         <nc:name>test_policy_3</nc:name>
#                         <nc:match>
#                           <nc:source-address>a1</nc:source-address>
#                           <nc:destination-address>a2</nc:destination-address>
#                           <nc:application>any</nc:application>
#                         </nc:match>
#                         <nc:then>
#                           <nc:permit>
#                             <nc:application-services>
#                               <nc:application-traffic-control>
#                                 <nc:rule-set>test_traffic_control</nc:rule-set>
#                               </nc:application-traffic-control>
#                               <nc:gprs-gtp-profile>gtp1</nc:gprs-gtp-profile>
#                               <nc:icap-redirect>test_icap</nc:icap-redirect>
#                               <nc:reverse-redirect-wx/>
#                               <nc:uac-policy></nc:uac-policy>
#                             </nc:application-services>
#                             <nc:firewall-authentication>
#                               <nc:push-to-identity-management/>
#                               <nc:web-authentication>
#                                 <nc:client-match>FWClient1</nc:client-match>
#                               </nc:web-authentication>
#                             </nc:firewall-authentication>
#                             <nc:tcp-options>
#                               <nc:initial-tcp-mss>64</nc:initial-tcp-mss>
#                               <nc:window-scale/>
#                             </nc:tcp-options>
#                           </nc:permit>
#                         </nc:then>
#                       </nc:policy>
#                     </nc:policy>
#                     <nc:global>
#                       <nc:policy>
#                         <nc:name>test_glob_1</nc:name>
#                         <nc:match>
#                           <nc:source-address>any-ipv6</nc:source-address>
#                           <nc:destination-address>any-ipv6</nc:destination-address>
#                           <nc:application>any</nc:application>
#                         </nc:match>
#                         <nc:then>
#                           <nc:deny/>
#                         </nc:then>
#                       </nc:policy>
#                       <nc:policy>
#                         <nc:name>test_glob_2</nc:name>
#                         <nc:match>
#                           <nc:source-address>any-ipv6</nc:source-address>
#                           <nc:destination-address>any-ipv6</nc:destination-address>
#                           <nc:application>any</nc:application>
#                         </nc:match>
#                         <nc:then>
#                           <nc:deny/>
#                         </nc:then>
#                       </nc:policy>
#                     </nc:global>
#                   </nc:policies>
#                 </nc:security>
#                 "
# After state
# -----------
#
# vagrant@vsrx> show security policies
# Default policy: deny-all
# Pre ID default policy: permit-all
# From zone: one, To zone: two
# Policy: test_policy_1, State: enabled, Index: 5, Scope Policy: 0, Sequence number: 1
# Source addresses(excluded): a1, a3
# Destination addresses(excluded): a2, a4
# Source-end-user-profile: test_end_user_profile(1)
# Applications: junos-dhcp-relay, junos-finger
# Dynamic Applications: any
# Url-category: Enhanced_Web_Chat
# Source identities: unknown-user
# Action: deny, log, count
# Policy: test_policy_2, State: enabled, Index: 6, Scope Policy: 0, Sequence number: 2
# Source addresses: a1
# Destination addresses: any-ipv6
# Applications: any
# Action: reject
# dynapp-redir-profile: test_dyn_app(1)
# From zone: one, To zone: three
# Policy: test_policy_3, State: enabled, Index: 7, Scope Policy: 0, Sequence number: 1
# Source addresses: a1
# Destination addresses: a2
# Applications: any
# Action: permit, firewall authentication, application services, unified access control
# Application traffic control: test_traffic_control
# Global policies:
# Policy: test_glob, State: enabled, Index: 4, Scope Policy: 0, Sequence number: 1
# From zones: any
# To zones: any
# Source addresses: any-ipv4
# Destination addresses: any-ipv4
# Applications: any
# Action: deny
# Policy: test_glob_1, State: enabled, Index: 8, Scope Policy: 0, Sequence number: 2
# From zones: any
# To zones: any
# Source addresses: any-ipv6
# Destination addresses: any-ipv6
# Applications: any
# Action: deny
# Policy: test_glob_2, State: enabled, Index: 9, Scope Policy: 0, Sequence number: 3
# From zones: any
# To zones: any
# Source addresses: any-ipv6
# Destination addresses: any-ipv6
# Applications: any
# Action: deny

# Using Replaced
# Before state
# ------------
#
# vagrant@vsrx> show security policies
# Default policy: deny-all
# Pre ID default policy: permit-all
# From zone: one, To zone: two
# Policy: test_policy_1, State: enabled, Index: 5, Scope Policy: 0, Sequence number: 1
# Source addresses(excluded): a1, a3
# Destination addresses(excluded): a2, a4
# Source-end-user-profile: test_end_user_profile(1)
# Applications: junos-dhcp-relay, junos-finger
# Dynamic Applications: any
# Url-category: Enhanced_Web_Chat
# Source identities: unknown-user
# Action: deny, log, count
# Policy: test_policy_2, State: enabled, Index: 6, Scope Policy: 0, Sequence number: 2
# Source addresses: a1
# Destination addresses: any-ipv6
# Applications: any
# Action: reject
# dynapp-redir-profile: test_dyn_app(1)
# From zone: one, To zone: three
# Policy: test_policy_3, State: enabled, Index: 7, Scope Policy: 0, Sequence number: 1
# Source addresses: a1
# Destination addresses: a2
# Applications: any
# Action: permit, firewall authentication, application services, unified access control
# Application traffic control: test_traffic_control
# Global policies:
# Policy: test_glob, State: enabled, Index: 4, Scope Policy: 0, Sequence number: 1
# From zones: any
# To zones: any
# Source addresses: any-ipv4
# Destination addresses: any-ipv4
# Applications: any
# Action: deny
# Policy: test_glob_1, State: enabled, Index: 8, Scope Policy: 0, Sequence number: 2
# From zones: any
# To zones: any
# Source addresses: any-ipv6
# Destination addresses: any-ipv6
# Applications: any
# Action: deny
# Policy: test_glob_2, State: enabled, Index: 9, Scope Policy: 0, Sequence number: 3
# From zones: any
# To zones: any
# Source addresses: any-ipv6
# Destination addresses: any-ipv6
# Applications: any
# Action: deny
#
- junipernetworks.junos.junos_security_policies:
    config:
      global:
        policies:
          - description: test update
            match:
              application:
                any: true
              destination_address:
                any_ipv6: true
              source_address:
                any: true
            name: test_glob_3
            then:
              deny: true
    state: replaced
#
# -------------------------
# Module Execution Result
# -------------------------
#   "after": {
#     "global": {
#       "policies": [
#         {
#           "description": "test update",
#           "match": {
#             "application": {
#               "any": true
#             },
#             "destination_address": {
#               "any_ipv6": true
#             },
#             "source_address": {
#               "any": true
#             }
#           },
#           "name": "test_glob_3",
#           "then": {
#             "deny": true
#           }
#         }
#       ]
#     }
#   },
#   "before": {
#     "from_zones": [
#       {
#         "name": "one",
#         "to_zones": [
#           {
#             "name": "two",
#             "policies": [
#               {
#                 "match": {
#                   "application": {
#                     "names": [
#                       "junos-dhcp-relay",
#                       "junos-finger"
#                     ]
#                   },
#                   "destination_address": {
#                     "addresses": [
#                       "a2",
#                       "a4"
#                     ]
#                   },
#                   "destination_address_excluded": true,
#                   "dynamic_application": {
#                     "names": [
#                       "any"
#                     ]
#                   },
#                   "source_address": {
#                     "addresses": [
#                       "a1",
#                       "a3"
#                     ]
#                   },
#                   "source_address_excluded": true,
#                   "source_end_user_profile": "test_end_user_profile",
#                   "source_identity": {
#                     "unknown_user": true
#                   },
#                   "url_category": {
#                     "names": [
#                       "Enhanced_Web_Chat"
#                     ]
#                   }
#                 },
#                 "name": "test_policy_1",
#                 "then": {
#                   "count": true,
#                   "deny": true,
#                   "log": "session-close"
#                 }
#               },
#               {
#                 "match": {
#                   "application": {
#                     "any": true
#                   },
#                   "destination_address": {
#                     "any_ipv6": true
#                   },
#                   "source_address": {
#                     "addresses": [
#                       "a1"
#                     ]
#                   }
#                 },
#                 "name": "test_policy_2",
#                 "then": {
#                   "reject": {
#                     "enable": true,
#                     "profile": "test_dyn_app",
#                     "ssl_proxy": {
#                       "enable": true,
#                       "profile_name": "SECURITY-SSL-PROXY"
#                     }
#                   }
#                 }
#               }
#             ]
#           },
#           {
#             "name": "three",
#             "policies": [
#               {
#                 "match": {
#                   "application": {
#                     "any": true
#                   },
#                   "destination_address": {
#                     "addresses": [
#                       "a2"
#                     ]
#                   },
#                   "source_address": {
#                     "addresses": [
#                       "a1"
#                     ]
#                   }
#                 },
#                 "name": "test_policy_3",
#                 "then": {
#                   "permit": {
#                     "application_services": {
#                       "application_traffic_control_rule_set": "test_traffic_control",
#                       "gprs_gtp_profile": "gtp1",
#                       "icap_redirect": "test_icap",
#                       "reverse_redirect_wx": "True",
#                       "uac_policy": {
#                         "enable": true
#                       }
#                     },
#                     "firewall_authentication": {
#                       "push_to_identity_management": true,
#                       "web_authentication": [
#                         "FWClient1"
#                       ]
#                     },
#                     "tcp_options": {
#                       "initial_tcp_mss": 64,
#                       "window_scale": true
#                     }
#                   }
#                 }
#               }
#             ]
#           }
#         ]
#       }
#     ],
#     "global": {
#       "policies": [
#         {
#           "match": {
#             "application": {
#               "any": true
#             },
#             "destination_address": {
#               "any_ipv4": true
#             },
#             "source_address": {
#               "any_ipv4": true
#             }
#           },
#           "name": "test_glob",
#           "then": {
#             "deny": true
#           }
#         },
#         {
#           "match": {
#             "application": {
#               "any": true
#             },
#             "destination_address": {
#               "any_ipv6": true
#             },
#             "source_address": {
#               "any_ipv6": true
#             }
#           },
#           "name": "test_glob_1",
#           "then": {
#             "deny": true
#           }
#         },
#         {
#           "match": {
#             "application": {
#               "any": true
#             },
#             "destination_address": {
#               "any_ipv6": true
#             },
#             "source_address": {
#               "any_ipv6": true
#             }
#           },
#           "name": "test_glob_2",
#           "then": {
#             "deny": true
#           }
#         }
#       ]
#     }
#   },
#   "changed": true,
#   "commands": "<nc:security
#                   xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
#                   <nc:policies delete="delete"/>
#                   <nc:policies>
#                     <nc:global>
#                       <nc:policy>
#                         <nc:name>test_glob_3</nc:name>
#                         <nc:description>test update</nc:description>
#                         <nc:match>
#                           <nc:source-address>any</nc:source-address>
#                           <nc:destination-address>any-ipv6</nc:destination-address>
#                           <nc:application>any</nc:application>
#                         </nc:match>
#                         <nc:then>
#                           <nc:deny/>
#                         </nc:then>
#                       </nc:policy>
#                     </nc:global>
#                   </nc:policies>
#                 </nc:security>"
# }
# After state
# -----------
#
# vagrant@vsrx> show security policies
# Default policy: deny-all
# Pre ID default policy: permit-all
# Global policies:
# Policy: test_glob_3, State: enabled, Index: 10, Scope Policy: 0, Sequence number: 1
# From zones: any
# To zones: any
# Source addresses: any
# Destination addresses: any-ipv6
# Applications: any
# Action: deny

# Using overridden
#
# Before state
# ------------
#
# vagrant@vsrx> show security policies
# Default policy: deny-all
# Pre ID default policy: permit-all
# From zone: one, To zone: two
# Policy: test_policy_1, State: enabled, Index: 5, Scope Policy: 0, Sequence number: 1
# Source addresses(excluded): a1, a3
# Destination addresses(excluded): a2, a4
# Source-end-user-profile: test_end_user_profile(1)
# Applications: junos-dhcp-relay, junos-finger
# Dynamic Applications: any
# Url-category: Enhanced_Web_Chat
# Source identities: unknown-user
# Action: deny, log, count
# Policy: test_policy_2, State: enabled, Index: 6, Scope Policy: 0, Sequence number: 2
# Source addresses: a1
# Destination addresses: any-ipv6
# Applications: any
# Action: reject
# dynapp-redir-profile: test_dyn_app(1)
# From zone: one, To zone: three
# Policy: test_policy_3, State: enabled, Index: 7, Scope Policy: 0, Sequence number: 1
# Source addresses: a1
# Destination addresses: a2
# Applications: any
# Action: permit, firewall authentication, application services, unified access control
# Application traffic control: test_traffic_control
# Global policies:
# Policy: test_glob, State: enabled, Index: 4, Scope Policy: 0, Sequence number: 1
# From zones: any
# To zones: any
# Source addresses: any-ipv4
# Destination addresses: any-ipv4
# Applications: any
# Action: deny
# Policy: test_glob_1, State: enabled, Index: 8, Scope Policy: 0, Sequence number: 2
# From zones: any
# To zones: any
# Source addresses: any-ipv6
# Destination addresses: any-ipv6
# Applications: any
# Action: deny
# Policy: test_glob_2, State: enabled, Index: 9, Scope Policy: 0, Sequence number: 3
# From zones: any
# To zones: any
# Source addresses: any-ipv6
# Destination addresses: any-ipv6
# Applications: any
# Action: deny
#
- junipernetworks.junos.junos_security_policies:
    config:
      global:
        policies:
          - description: test update
            match:
              application:
                any: true
              destination_address:
                any_ipv6: true
              source_address:
                any: true
            name: test_glob_3
            then:
              deny: true
    state: overridden
#
# -------------------------
# Module Execution Result
# -------------------------
#   "after": {
#     "global": {
#       "policies": [
#         {
#           "description": "test update",
#           "match": {
#             "application": {
#               "any": true
#             },
#             "destination_address": {
#               "any_ipv6": true
#             },
#             "source_address": {
#               "any": true
#             }
#           },
#           "name": "test_glob_3",
#           "then": {
#             "deny": true
#           }
#         }
#       ]
#     }
#   },
#   "before": {
#     "from_zones": [
#       {
#         "name": "one",
#         "to_zones": [
#           {
#             "name": "two",
#             "policies": [
#               {
#                 "match": {
#                   "application": {
#                     "names": [
#                       "junos-dhcp-relay",
#                       "junos-finger"
#                     ]
#                   },
#                   "destination_address": {
#                     "addresses": [
#                       "a2",
#                       "a4"
#                     ]
#                   },
#                   "destination_address_excluded": true,
#                   "dynamic_application": {
#                     "names": [
#                       "any"
#                     ]
#                   },
#                   "source_address": {
#                     "addresses": [
#                       "a1",
#                       "a3"
#                     ]
#                   },
#                   "source_address_excluded": true,
#                   "source_end_user_profile": "test_end_user_profile",
#                   "source_identity": {
#                     "unknown_user": true
#                   },
#                   "url_category": {
#                     "names": [
#                       "Enhanced_Web_Chat"
#                     ]
#                   }
#                 },
#                 "name": "test_policy_1",
#                 "then": {
#                   "count": true,
#                   "deny": true,
#                   "log": "session-close"
#                 }
#               },
#               {
#                 "match": {
#                   "application": {
#                     "any": true
#                   },
#                   "destination_address": {
#                     "any_ipv6": true
#                   },
#                   "source_address": {
#                     "addresses": [
#                       "a1"
#                     ]
#                   }
#                 },
#                 "name": "test_policy_2",
#                 "then": {
#                   "reject": {
#                     "enable": true,
#                     "profile": "test_dyn_app",
#                     "ssl_proxy": {
#                       "enable": true,
#                       "profile_name": "SECURITY-SSL-PROXY"
#                     }
#                   }
#                 }
#               }
#             ]
#           },
#           {
#             "name": "three",
#             "policies": [
#               {
#                 "match": {
#                   "application": {
#                     "any": true
#                   },
#                   "destination_address": {
#                     "addresses": [
#                       "a2"
#                     ]
#                   },
#                   "source_address": {
#                     "addresses": [
#                       "a1"
#                     ]
#                   }
#                 },
#                 "name": "test_policy_3",
#                 "then": {
#                   "permit": {
#                     "application_services": {
#                       "application_traffic_control_rule_set": "test_traffic_control",
#                       "gprs_gtp_profile": "gtp1",
#                       "icap_redirect": "test_icap",
#                       "reverse_redirect_wx": "True",
#                       "uac_policy": {
#                         "enable": true
#                       }
#                     },
#                     "firewall_authentication": {
#                       "push_to_identity_management": true,
#                       "web_authentication": [
#                         "FWClient1"
#                       ]
#                     },
#                     "tcp_options": {
#                       "initial_tcp_mss": 64,
#                       "window_scale": true
#                     }
#                   }
#                 }
#               }
#             ]
#           }
#         ]
#       }
#     ],
#     "global": {
#       "policies": [
#         {
#           "match": {
#             "application": {
#               "any": true
#             },
#             "destination_address": {
#               "any_ipv4": true
#             },
#             "source_address": {
#               "any_ipv4": true
#             }
#           },
#           "name": "test_glob",
#           "then": {
#             "deny": true
#           }
#         },
#         {
#           "match": {
#             "application": {
#               "any": true
#             },
#             "destination_address": {
#               "any_ipv6": true
#             },
#             "source_address": {
#               "any_ipv6": true
#             }
#           },
#           "name": "test_glob_1",
#           "then": {
#             "deny": true
#           }
#         },
#         {
#           "match": {
#             "application": {
#               "any": true
#             },
#             "destination_address": {
#               "any_ipv6": true
#             },
#             "source_address": {
#               "any_ipv6": true
#             }
#           },
#           "name": "test_glob_2",
#           "then": {
#             "deny": true
#           }
#         }
#       ]
#     }
#   },
#   "changed": true,
#   "commands": "<nc:security
#                   xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
#                   <nc:policies delete="delete"/>
#                   <nc:policies>
#                     <nc:global>
#                       <nc:policy>
#                         <nc:name>test_glob_3</nc:name>
#                         <nc:description>test update</nc:description>
#                         <nc:match>
#                           <nc:source-address>any</nc:source-address>
#                           <nc:destination-address>any-ipv6</nc:destination-address>
#                           <nc:application>any</nc:application>
#                         </nc:match>
#                         <nc:then>
#                           <nc:deny/>
#                         </nc:then>
#                       </nc:policy>
#                     </nc:global>
#                   </nc:policies>
#                 </nc:security>"
# }
# After state
# -----------
#
# vagrant@vsrx> show security policies
# Default policy: deny-all
# Pre ID default policy: permit-all
# Global policies:
# Policy: test_glob_3, State: enabled, Index: 10, Scope Policy: 0, Sequence number: 1
# From zones: any
# To zones: any
# Source addresses: any
# Destination addresses: any-ipv6
# Applications: any
# Action: deny

# Using deleted
#
# Before state
# ------------
#
# vagrant@vsrx> show security policies
# Default policy: deny-all
# Pre ID default policy: permit-all
# Global policies:
# Policy: test_glob_3, State: enabled, Index: 10, Scope Policy: 0, Sequence number: 1
# From zones: any
# To zones: any
# Source addresses: any
# Destination addresses: any-ipv6
# Applications: any
# Action: deny
#
- junipernetworks.junos.junos_security_policies:
    config:
    state: deleted
#
# -------------------------
# Module Execution Result
# -------------------------
#
#   "after": {},
#   "before": {
#     "global": {
#       "policies": [
#         {
#           "description": "test update",
#           "match": {
#             "application": {
#               "any": true
#             },
#             "destination_address": {
#               "any_ipv6": true
#             },
#             "source_address": {
#               "any": true
#             }
#           },
#           "name": "test_glob_3",
#           "then": {
#             "deny": true
#           }
#         }
#       ]
#     }
#   },
#   "changed": true,
#   "commands": "<nc:security xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
#   <nc:policies delete="delete"/></nc:security>"
#
# After state
# -----------
#
# vagrant@vsrx> show security policies
# Default policy: deny-all
# Pre ID default policy: permit-all

# Using parsed
# parsed.cfg
# ------------
# <?xml version="1.0" encoding="UTF-8"?>
# <rpc-reply>
#     <configuration>
#         <version>18.4R1-S3.1</version>
#         <services>
#             <ssl>
#                 <termination>
#                     <profile>
#                         <name>test_ssl_term</name>
#                         <server-certificate>SECURITY-cert</server-certificate>
#                     </profile>
#                 </termination>
#                 <proxy>
#                     <profile>
#                         <name>SECURITY-SSL-PROXY</name>
#                         <root-ca>SECURITY-cert</root-ca>
#                     </profile>
#                 </proxy>
#             </ssl>
#             <icap-redirect>
#                 <profile>
#                     <name>test_icap</name>
#                     <server>
#                         <name>test_icap_server</name>
#                         <host>10.10.10.11</host>
#                     </server>
#                 </profile>
#             </icap-redirect>
#             <user-identification>
#                 <device-information>
#                     <end-user-profile>
#                         <profile-name>
#                             <name>test_end_user_profile</name>
#                             <domain-name>test_domain</domain-name>
#                             <attribute>
#                                 <name>device-identity</name>
#                                 <string>Windows</string>
#                             </attribute>
#                         </profile-name>
#                     </end-user-profile>
#                 </device-information>
#             </user-identification>
#         </services>
#         <security>
#             <address-book>
#                 <name>global</name>
#                 <address>
#                     <name>a1</name>
#                     <ip-prefix>200.0.113.0/24</ip-prefix>
#                 </address>
#                 <address>
#                     <name>a2</name>
#                     <ip-prefix>201.0.113.0/24</ip-prefix>
#                 </address>
#                 <address>
#                     <name>a3</name>
#                     <ip-prefix>202.0.113.0/24</ip-prefix>
#                 </address>
#                 <address>
#                     <name>a4</name>
#                     <ip-prefix>203.0.113.0/24</ip-prefix>
#                 </address>
#             </address-book>
#             <dynamic-application>
#                 <profile>
#                     <name>test_dyn_app</name>
#                     <redirect-message>
#                         <type>
#                             <custom-text>
#                                 <content>hello_world</content>
#                             </custom-text>
#                         </type>
#                     </redirect-message>
#                 </profile>
#             </dynamic-application>
#             <policies>
#                 <policy>
#                     <from-zone-name>one</from-zone-name>
#                     <to-zone-name>two</to-zone-name>
#                     <policy>
#                         <name>test_policy_1</name>
#                         <match>
#                             <source-address>a1</source-address>
#                             <source-address>a3</source-address>
#                             <destination-address>a2</destination-address>
#                             <destination-address>a4</destination-address>
#                             <source-address-excluded />
#                             <destination-address-excluded />
#                             <application>junos-dhcp-relay</application>
#                             <application>junos-finger</application>
#                             <source-identity>authenticated-user</source-identity>
#                             <source-identity>unknown-user</source-identity>
#                             <source-end-user-profile>
#                                 <source-end-user-profile-name>test_end_user_profile</source-end-user-profile-name>
#                             </source-end-user-profile>
#                             <dynamic-application>any</dynamic-application>
#                             <url-category>Enhanced_Web_Chat</url-category>
#                         </match>
#                         <then>
#                             <deny />
#                             <log>
#                                 <session-close />
#                             </log>
#                             <count></count>
#                         </then>
#                     </policy>
#                     <policy>
#                         <name>test_policy_2</name>
#                         <match>
#                             <source-address>a1</source-address>
#                             <destination-address>any-ipv6</destination-address>
#                             <application>any</application>
#                         </match>
#                         <then>
#                             <reject>
#                                 <profile>test_dyn_app</profile>
#                                 <ssl-proxy>
#                                     <profile-name>SECURITY-SSL-PROXY</profile-name>
#                                 </ssl-proxy>
#                             </reject>
#                         </then>
#                     </policy>
#                 </policy>
#                 <policy>
#                     <from-zone-name>one</from-zone-name>
#                     <to-zone-name>three</to-zone-name>
#                     <policy>
#                         <name>test_policy_3</name>
#                         <match>
#                             <source-address>a1</source-address>
#                             <destination-address>a2</destination-address>
#                             <application>any</application>
#                         </match>
#                         <then>
#                             <permit>
#                                 <firewall-authentication>
#                                     <web-authentication>
#                                         <client-match>FWClient1</client-match>
#                                     </web-authentication>
#                                     <push-to-identity-management />
#                                 </firewall-authentication>
#                                 <destination-address>
#                                     <drop-untranslated />
#                                 </destination-address>
#                                 <application-services>
#                                     <gprs-gtp-profile>gtp1</gprs-gtp-profile>
#                                     <uac-policy></uac-policy>
#                                     <icap-redirect>test_icap</icap-redirect>
#                                     <application-traffic-control>
#                                         <rule-set>test_traffic_control</rule-set>
#                                     </application-traffic-control>
#                                     <reverse-redirect-wx />
#                                 </application-services>
#                                 <tcp-options>
#                                     <initial-tcp-mss>64</initial-tcp-mss>
#                                     <window-scale />
#                                 </tcp-options>
#                             </permit>
#                         </then>
#                     </policy>
#                 </policy>
#                 <global>
#                     <policy>
#                         <name>test_glob_1</name>
#                         <match>
#                             <source-address>any-ipv6</source-address>
#                             <destination-address>any-ipv6</destination-address>
#                             <application>any</application>
#                         </match>
#                         <then>
#                             <deny />
#                         </then>
#                     </policy>
#                     <policy>
#                         <name>test_glob_2</name>
#                         <match>
#                             <source-address>any-ipv6</source-address>
#                             <destination-address>any-ipv6</destination-address>
#                             <application>any</application>
#                         </match>
#                         <then>
#                             <deny />
#                         </then>
#                     </policy>
#                 </global>
#             </policies>
#             <zones>
#                 <security-zone>
#                     <name>one</name>
#                     <interfaces>
#                         <name>ge-0/0/0.0</name>
#                     </interfaces>
#                 </security-zone>
#                 <security-zone>
#                     <name>two</name>
#                     <interfaces>
#                         <name>ge-0/0/1.0</name>
#                     </interfaces>
#                 </security-zone>
#                 <security-zone>
#                     <name>three</name>
#                     <interfaces>
#                         <name>ge-0/0/2.0</name>
#                     </interfaces>
#                 </security-zone>
#             </zones>
#             <gprs>
#                 <gtp>
#                     <profile>
#                         <name>gtp1</name>
#                     </profile>
#                 </gtp>
#             </gprs>
#         </security>
#         <interfaces>
#             <interface>
#                 <name>ge-0/0/0</name>
#                 <unit>
#                     <name>0</name>
#                     <family>
#                         <inet>
#                             <address>
#                                 <name>200.0.113.1/24</name>
#                             </address>
#                         </inet>
#                     </family>
#                 </unit>
#             </interface>
#             <interface>
#                 <name>ge-0/0/1</name>
#                 <unit>
#                     <name>0</name>
#                     <family>
#                         <inet>
#                             <address>
#                                 <name>201.0.113.1/24</name>
#                             </address>
#                         </inet>
#                     </family>
#                 </unit>
#             </interface>
#             <interface>
#                 <name>ge-0/0/2</name>
#                 <unit>
#                     <name>0</name>
#                     <family>
#                         <inet>
#                             <address>
#                                 <name>202.0.113.1/24</name>
#                             </address>
#                         </inet>
#                     </family>
#                 </unit>
#             </interface>
#             <interface>
#                 <name>fxp0</name>
#                 <unit>
#                     <name>0</name>
#                     <family>
#                         <inet>
#                             <dhcp></dhcp>
#                         </inet>
#                     </family>
#                 </unit>
#             </interface>
#         </interfaces>
#         <class-of-service>
#             <application-traffic-control>
#                 <rule-sets>
#                     <name>test_traffic_control</name>
#                     <rule>
#                         <name>test_rule</name>
#                         <match>
#                             <application-known />
#                         </match>
#                         <then>
#                             <log />
#                         </then>
#                     </rule>
#                 </rule-sets>
#             </application-traffic-control>
#         </class-of-service>
#         <access>
#             <profile>
#                 <name>WEBAUTH</name>
#                 <client>
#                     <name>FWClient1</name>
#                     <firewall-user>
#                         <password>$9$kq5Ftu1cSe</password>
#                     </firewall-user>
#                 </client>
#             </profile>
#             <firewall-authentication>
#                 <web-authentication>
#                     <default-profile>WEBAUTH</default-profile>
#                 </web-authentication>
#             </firewall-authentication>
#         </access>
#     </configuration>
#     <database-status-information></database-status-information>
# </rpc-reply>
#
- name: Parse NTP global running config
  junipernetworks.junos.junos_security_policies:
    running_config: "{{ lookup('file', './parsed.cfg') }}"
    state: parsed
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#   "parsed": {
#     "from_zones": [
#       {
#         "name": "one",
#         "to_zones": [
#           {
#             "name": "two",
#             "policies": [
#               {
#                 "match": {
#                   "application": {
#                     "names": [
#                       "junos-dhcp-relay",
#                       "junos-finger"
#                     ]
#                   },
#                   "destination_address": {
#                     "addresses": [
#                       "a2",
#                       "a4"
#                     ]
#                   },
#                   "destination_address_excluded": true,
#                   "dynamic_application": {
#                     "names": [
#                       "any"
#                     ]
#                   },
#                   "source_address": {
#                     "addresses": [
#                       "a1",
#                       "a3"
#                     ]
#                   },
#                   "source_address_excluded": true,
#                   "source_end_user_profile": "test_end_user_profile",
#                   "source_identity": {
#                     "unknown_user": true
#                   },
#                   "url_category": {
#                     "names": [
#                       "Enhanced_Web_Chat"
#                     ]
#                   }
#                 },
#                 "name": "test_policy_1",
#                 "then": {
#                   "count": true,
#                   "deny": true,
#                   "log": "session-close"
#                 }
#               },
#               {
#                 "match": {
#                   "application": {
#                     "any": true
#                   },
#                   "destination_address": {
#                     "any_ipv6": true
#                   },
#                   "source_address": {
#                     "addresses": [
#                       "a1"
#                     ]
#                   }
#                 },
#                 "name": "test_policy_2",
#                 "then": {
#                   "reject": {
#                     "enable": true,
#                     "profile": "test_dyn_app",
#                     "ssl_proxy": {
#                       "enable": true,
#                       "profile_name": "SECURITY-SSL-PROXY"
#                     }
#                   }
#                 }
#               }
#             ]
#           },
#           {
#             "name": "three",
#             "policies": [
#               {
#                 "match": {
#                   "application": {
#                     "any": true
#                   },
#                   "destination_address": {
#                     "addresses": [
#                       "a2"
#                     ]
#                   },
#                   "source_address": {
#                     "addresses": [
#                       "a1"
#                     ]
#                   }
#                 },
#                 "name": "test_policy_3",
#                 "then": {
#                   "permit": {
#                     "application_services": {
#                       "application_traffic_control_rule_set": "test_traffic_control",
#                       "gprs_gtp_profile": "gtp1",
#                       "icap_redirect": "test_icap",
#                       "reverse_redirect_wx": "True",
#                       "uac_policy": {
#                         "enable": true
#                       }
#                     },
#                     "firewall_authentication": {
#                       "push_to_identity_management": true,
#                       "web_authentication": [
#                         "FWClient1"
#                       ]
#                     },
#                     "tcp_options": {
#                       "initial_tcp_mss": 64,
#                       "window_scale": true
#                     }
#                   }
#                 }
#               }
#             ]
#           }
#         ]
#       }
#     ],
#     "global": {
#       "policies": [
#         {
#           "match": {
#             "application": {
#               "any": true
#             },
#             "destination_address": {
#               "any_ipv6": true
#             },
#             "source_address": {
#               "any_ipv6": true
#             }
#           },
#           "name": "test_glob_1",
#           "then": {
#             "deny": true
#           }
#         },
#         {
#           "match": {
#             "application": {
#               "any": true
#             },
#             "destination_address": {
#               "any_ipv6": true
#             },
#             "source_address": {
#               "any_ipv6": true
#             }
#           },
#           "name": "test_glob_2",
#           "then": {
#             "deny": true
#           }
#         }
#       ]
#     }
#   }

# Using gathered
#
# Before state
# ------------
#
# vagrant@vsrx> show security policies
# Default policy: deny-all
# Pre ID default policy: permit-all
# From zone: one, To zone: two
# Policy: test_policy_1, State: enabled, Index: 4, Scope Policy: 0, Sequence number: 1
# Source addresses(excluded): a1, a3
# Destination addresses(excluded): a2, a4
# Source-end-user-profile: test_end_user_profile(1)
# Applications: junos-dhcp-relay, junos-finger
# Dynamic Applications: any
# Url-category: Enhanced_Web_Chat
# Source identities: authenticated-user, unknown-user
# Action: deny, log, count
# Policy: test_policy_2, State: enabled, Index: 5, Scope Policy: 0, Sequence number: 2
# Source addresses: a1
# Destination addresses: any-ipv6
# Applications: any
# Action: reject
# dynapp-redir-profile: test_dyn_app(1)
# From zone: one, To zone: three
# Policy: test_policy_3, State: enabled, Index: 6, Scope Policy: 0, Sequence number: 1
# Source addresses: a1
# Destination addresses: a2
# Applications: any
# Action: permit, drop-untranslated, firewall authentication, application services, unified access control
# Application traffic control: test_traffic_control
# Global policies:
# Policy: test_glob_1, State: enabled, Index: 7, Scope Policy: 0, Sequence number: 1
# From zones: any
# To zones: any
# Source addresses: any-ipv6
# Destination addresses: any-ipv6
# Applications: any
# Action: deny
# Policy: test_glob_2, State: enabled, Index: 8, Scope Policy: 0, Sequence number: 2
# From zones: any
# To zones: any
# Source addresses: any-ipv6
# Destination addresses: any-ipv6
# Applications: any
# Action: deny
#
- junipernetworks.junos.junos_security_policies:
    state: gathered
#
# -------------------------
# Module Execution Result
# -------------------------
#
#   "changed": false,
#   "gathered": {
#     "from_zones": [
#       {
#         "name": "one",
#         "to_zones": [
#           {
#             "name": "two",
#             "policies": [
#               {
#                 "match": {
#                   "application": {
#                     "names": [
#                       "junos-dhcp-relay",
#                       "junos-finger"
#                     ]
#                   },
#                   "destination_address": {
#                     "addresses": [
#                       "a2",
#                       "a4"
#                     ]
#                   },
#                   "destination_address_excluded": true,
#                   "dynamic_application": {
#                     "names": [
#                       "any"
#                     ]
#                   },
#                   "source_address": {
#                     "addresses": [
#                       "a1",
#                       "a3"
#                     ]
#                   },
#                   "source_address_excluded": true,
#                   "source_end_user_profile": "test_end_user_profile",
#                   "source_identity": {
#                     "unknown_user": true
#                   },
#                   "url_category": {
#                     "names": [
#                       "Enhanced_Web_Chat"
#                     ]
#                   }
#                 },
#                 "name": "test_policy_1",
#                 "then": {
#                   "count": true,
#                   "deny": true,
#                   "log": "session-close"
#                 }
#               },
#               {
#                 "match": {
#                   "application": {
#                     "any": true
#                   },
#                   "destination_address": {
#                     "any_ipv6": true
#                   },
#                   "source_address": {
#                     "addresses": [
#                       "a1"
#                     ]
#                   }
#                 },
#                 "name": "test_policy_2",
#                 "then": {
#                   "reject": {
#                     "enable": true,
#                     "profile": "test_dyn_app",
#                     "ssl_proxy": {
#                       "enable": true,
#                       "profile_name": "SECURITY-SSL-PROXY"
#                     }
#                   }
#                 }
#               }
#             ]
#           },
#           {
#             "name": "three",
#             "policies": [
#               {
#                 "match": {
#                   "application": {
#                     "any": true
#                   },
#                   "destination_address": {
#                     "addresses": [
#                       "a2"
#                     ]
#                   },
#                   "source_address": {
#                     "addresses": [
#                       "a1"
#                     ]
#                   }
#                 },
#                 "name": "test_policy_3",
#                 "then": {
#                   "permit": {
#                     "application_services": {
#                       "application_traffic_control_rule_set": "test_traffic_control",
#                       "gprs_gtp_profile": "gtp1",
#                       "icap_redirect": "test_icap",
#                       "reverse_redirect_wx": "True",
#                       "uac_policy": {
#                         "enable": true
#                       }
#                     },
#                     "firewall_authentication": {
#                       "push_to_identity_management": true,
#                       "web_authentication": [
#                         "FWClient1"
#                       ]
#                     },
#                     "tcp_options": {
#                       "initial_tcp_mss": 64,
#                       "window_scale": true
#                     }
#                   }
#                 }
#               }
#             ]
#           }
#         ]
#       }
#     ],
#     "global": {
#       "policies": [
#         {
#           "match": {
#             "application": {
#               "any": true
#             },
#             "destination_address": {
#               "any_ipv6": true
#             },
#             "source_address": {
#               "any_ipv6": true
#             }
#           },
#           "name": "test_glob_1",
#           "then": {
#             "deny": true
#           }
#         },
#         {
#           "match": {
#             "application": {
#               "any": true
#             },
#             "destination_address": {
#               "any_ipv6": true
#             },
#             "source_address": {
#               "any_ipv6": true
#             }
#           },
#           "name": "test_glob_2",
#           "then": {
#             "deny": true
#           }
#         }
#       ]
#     }
#   }
# }

# Using rendered
#
# Before state
# ------------
#
- junipernetworks.junos.junos_security_policies:
    config:
      global:
        policies:
          - description: test update
            match:
              application:
                any: true
              destination_address:
                any_ipv6: true
              source_address:
                any: true
            name: test_glob_3
            then:
              deny: true
    state: rendered
#
# -------------------------
# Module Execution Result
# -------------------------
#     "rendered": "<nc:security
#                 xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
#                 <nc:policies>
#                   <nc:global>
#                     <nc:policy>
#                       <nc:name>test_glob_3</nc:name>
#                       <nc:description>test update</nc:description>
#                       <nc:match>
#                         <nc:source-address>any</nc:source-address>
#                         <nc:destination-address>any-ipv6</nc:destination-address>
#                         <nc:application>any</nc:application>
#                       </nc:match>
#                       <nc:then>
#                         <nc:deny/>
#                       </nc:then>
#                     </nc:policy>
#                   </nc:global>
#                 </nc:policies>
#               </nc:security>"
```

## [Return Values](junos_security_policies_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | The resulting configuration after module execution.  **Returned:** when changed  **Sample:** `"This output will always be in the same format as the module argspec.\n"` |
| **before**  dictionary | The configuration prior to the module execution.  **Returned:** when state is *merged*, *replaced*, *overridden* or *deleted*  **Sample:** `"This output will always be in the same format as the module argspec.\n"` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** when state is *merged*, *replaced*, *overridden* or *deleted*  **Sample:** `["<rpc-reply> <configuration> <security> <policies> <global> <policy> <name>test_glob_1</name> <match> <source-address>any-ipv6</source-address> <destination-address>any-ipv6</destination-address> <application>any</application> </match> <then> <deny /> </then> </policy> </global> </policies> </security> </configuration> </rpc-reply>"]` |
| **gathered**  dictionary | Facts about the network resource gathered from the remote device as structured data.  **Returned:** when state is *gathered*  **Sample:** `"This output will always be in the same format as the module argspec.\n"` |
| **parsed**  dictionary | The device native config provided in *running_config* option parsed into structured data as per module argspec.  **Returned:** when state is *parsed*  **Sample:** `"This output will always be in the same format as the module argspec.\n"` |
| **rendered**  dictionary | The provided configuration in the task rendered in device-native format (offline).  **Returned:** when state is *rendered*  **Sample:** `["<rpc-reply> <configuration> <security> <policies> <global> <policy> <name>test_glob_1</name> <match> <source-address>any-ipv6</source-address> <destination-address>any-ipv6</destination-address> <application>any</application> </match> <then> <deny /> </then> </policy> </global> </policies> </security> </configuration> </rpc-reply>"]` |

### Authors

- Pranav Bhatt (@pranav-bhatt)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/junipernetworks.junos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/junipernetworks.junos)
