---
collection: ansible
version: "8"
title: "Ansible.Utils"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/utils/index.html
fetched_at: 2026-07-28T01:01:50+00:00
---
# Ansible.Utils

Collection version 2.12.0

- [Description](index.md#description)
- [ansible.utils Scenario Guide](index.md#ansible-utils-scenario-guide)
- [Plugin Index](index.md#plugin-index)

## [Description](index.md#id1)

Ansible Collection with utilities to ease the management, manipulation, and validation of data within a playbook

**Author:**

- Ansible Community

**Supported ansible-core versions:**

- 2.9.10 or newer

- [Issue Tracker](https://github.com/ansible-collections/ansible.utils/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.utils)

## [ansible.utils Scenario Guide](index.md#id2)

- [Using the ipaddr filter](docsite/filters_ipaddr.md)

## [Plugin Index](index.md#id3)

These are the plugins in the ansible.utils collection:

### Modules

- [cli_parse module](cli_parse_module.md#ansible-collections-ansible-utils-cli-parse-module) – Parse cli output or text using a variety of parsers
- [fact_diff module](fact_diff_module.md#ansible-collections-ansible-utils-fact-diff-module) – Find the difference between currently set facts
- [update_fact module](update_fact_module.md#ansible-collections-ansible-utils-update-fact-module) – Update currently set facts
- [validate module](validate_module.md#ansible-collections-ansible-utils-validate-module) – Validate data with provided criteria

### Filter Plugins

- [cidr_merge filter](cidr_merge_filter.md#ansible-collections-ansible-utils-cidr-merge-filter) – This filter can be used to merge subnets or individual addresses.
- [consolidate filter](consolidate_filter.md#ansible-collections-ansible-utils-consolidate-filter) – Consolidate facts together on common attributes.
- [fact_diff filter](fact_diff_filter.md#ansible-collections-ansible-utils-fact-diff-filter) – Find the difference between currently set facts
- [from_xml filter](from_xml_filter.md#ansible-collections-ansible-utils-from-xml-filter) – Convert given XML string to native python dictionary.
- [get_path filter](get_path_filter.md#ansible-collections-ansible-utils-get-path-filter) – Retrieve the value in a variable using a path
- [hwaddr filter](hwaddr_filter.md#ansible-collections-ansible-utils-hwaddr-filter) – HWaddr / MAC address filters
- [index_of filter](index_of_filter.md#ansible-collections-ansible-utils-index-of-filter) – Find the indices of items in a list matching some criteria
- [ip4_hex filter](ip4_hex_filter.md#ansible-collections-ansible-utils-ip4-hex-filter) – This filter is designed to convert IPv4 address to Hexadecimal notation with optional delimiter.
- [ipaddr filter](ipaddr_filter.md#ansible-collections-ansible-utils-ipaddr-filter) – This filter is designed to return the input value if a query is True, else False.
- [ipcut filter](ipcut_filter.md#ansible-collections-ansible-utils-ipcut-filter) – This filter is designed to get 1st or last few bits of IP address.
- [ipmath filter](ipmath_filter.md#ansible-collections-ansible-utils-ipmath-filter) – This filter is designed to do simple IP math/arithmetic.
- [ipsubnet filter](ipsubnet_filter.md#ansible-collections-ansible-utils-ipsubnet-filter) – This filter can be used to manipulate network subnets in several ways.
- [ipv4 filter](ipv4_filter.md#ansible-collections-ansible-utils-ipv4-filter) – To filter only Ipv4 addresses Ipv4 filter is used.
- [ipv6 filter](ipv6_filter.md#ansible-collections-ansible-utils-ipv6-filter) – To filter only Ipv6 addresses Ipv6 filter is used.
- [ipv6form filter](ipv6form_filter.md#ansible-collections-ansible-utils-ipv6form-filter) –
- [ipwrap filter](ipwrap_filter.md#ansible-collections-ansible-utils-ipwrap-filter) – This filter is designed to Wrap IPv6 addresses in [ ] brackets.
- [keep_keys filter](keep_keys_filter.md#ansible-collections-ansible-utils-keep-keys-filter) – Keep specific keys from a data recursively.
- [macaddr filter](macaddr_filter.md#ansible-collections-ansible-utils-macaddr-filter) – macaddr / MAC address filters
- [network_in_network filter](network_in_network_filter.md#ansible-collections-ansible-utils-network-in-network-filter) – This filter returns whether an address or a network passed as argument is in a network.
- [network_in_usable filter](network_in_usable_filter.md#ansible-collections-ansible-utils-network-in-usable-filter) – The network_in_usable filter returns whether an address passed as an argument is usable in a network.
- [next_nth_usable filter](next_nth_usable_filter.md#ansible-collections-ansible-utils-next-nth-usable-filter) – This filter returns the next nth usable ip within a network described by value.
- [nthhost filter](nthhost_filter.md#ansible-collections-ansible-utils-nthhost-filter) – This filter returns the nth host within a network described by value.
- [param_list_compare filter](param_list_compare_filter.md#ansible-collections-ansible-utils-param-list-compare-filter) – Generate the final param list combining/comparing base and provided parameters.
- [previous_nth_usable filter](previous_nth_usable_filter.md#ansible-collections-ansible-utils-previous-nth-usable-filter) – This filter returns the previous nth usable ip within a network described by value.
- [reduce_on_network filter](reduce_on_network_filter.md#ansible-collections-ansible-utils-reduce-on-network-filter) – This filter reduces a list of addresses to only the addresses that match a given network.
- [remove_keys filter](remove_keys_filter.md#ansible-collections-ansible-utils-remove-keys-filter) – Remove specific keys from a data recursively.
- [replace_keys filter](replace_keys_filter.md#ansible-collections-ansible-utils-replace-keys-filter) – Replaces specific keys with their after value from a data recursively.
- [slaac filter](slaac_filter.md#ansible-collections-ansible-utils-slaac-filter) – This filter returns the SLAAC address within a network for a given HW/MAC address.
- [to_paths filter](to_paths_filter.md#ansible-collections-ansible-utils-to-paths-filter) – Flatten a complex object into a dictionary of paths and values
- [to_xml filter](to_xml_filter.md#ansible-collections-ansible-utils-to-xml-filter) – Convert given JSON string to XML
- [usable_range filter](usable_range_filter.md#ansible-collections-ansible-utils-usable-range-filter) – Expand the usable IP addresses
- [validate filter](validate_filter.md#ansible-collections-ansible-utils-validate-filter) – Validate data with provided criteria

### Lookup Plugins

- [get_path lookup](get_path_lookup.md#ansible-collections-ansible-utils-get-path-lookup) – Retrieve the value in a variable using a path
- [index_of lookup](index_of_lookup.md#ansible-collections-ansible-utils-index-of-lookup) – Find the indices of items in a list matching some criteria
- [to_paths lookup](to_paths_lookup.md#ansible-collections-ansible-utils-to-paths-lookup) – Flatten a complex object into a dictionary of paths and values
- [validate lookup](validate_lookup.md#ansible-collections-ansible-utils-validate-lookup) – Validate data with provided criteria

### Test Plugins

- [in_any_network test](in_any_network_test.md#ansible-collections-ansible-utils-in-any-network-test) – Test if an IP or network falls in any network
- [in_network test](in_network_test.md#ansible-collections-ansible-utils-in-network-test) – Test if IP address falls in the network
- [in_one_network test](in_one_network_test.md#ansible-collections-ansible-utils-in-one-network-test) – Test if IP address belongs in any one of the networks in the list
- [ip test](ip_test.md#ansible-collections-ansible-utils-ip-test) – Test if something in an IP address or network
- [ip_address test](ip_address_test.md#ansible-collections-ansible-utils-ip-address-test) – Test if something in an IP address
- [ipv4 test](ipv4_test.md#ansible-collections-ansible-utils-ipv4-test) – Test if something is an IPv4 address or network
- [ipv4_address test](ipv4_address_test.md#ansible-collections-ansible-utils-ipv4-address-test) – Test if something is an IPv4 address
- [ipv4_hostmask test](ipv4_hostmask_test.md#ansible-collections-ansible-utils-ipv4-hostmask-test) – Test if an address is a valid hostmask
- [ipv4_netmask test](ipv4_netmask_test.md#ansible-collections-ansible-utils-ipv4-netmask-test) – Test if an address is a valid netmask
- [ipv6 test](ipv6_test.md#ansible-collections-ansible-utils-ipv6-test) – Test if something is an IPv6 address or network
- [ipv6_address test](ipv6_address_test.md#ansible-collections-ansible-utils-ipv6-address-test) – Test if something is an IPv6 address
- [ipv6_ipv4_mapped test](ipv6_ipv4_mapped_test.md#ansible-collections-ansible-utils-ipv6-ipv4-mapped-test) – Test if something appears to be a mapped IPv6 to IPv4 mapped address
- [ipv6_sixtofour test](ipv6_sixtofour_test.md#ansible-collections-ansible-utils-ipv6-sixtofour-test) – Test if something appears to be a 6to4 address
- [ipv6_teredo test](ipv6_teredo_test.md#ansible-collections-ansible-utils-ipv6-teredo-test) – Test if something appears to be an IPv6 teredo address
- [loopback test](loopback_test.md#ansible-collections-ansible-utils-loopback-test) – Test if an IP address is a loopback
- [mac test](mac_test.md#ansible-collections-ansible-utils-mac-test) – Test if something appears to be a valid MAC address
- [multicast test](multicast_test.md#ansible-collections-ansible-utils-multicast-test) – Test for a multicast IP address
- [private test](private_test.md#ansible-collections-ansible-utils-private-test) – Test if an IP address is private
- [public test](public_test.md#ansible-collections-ansible-utils-public-test) – Test if an IP address is public
- [reserved test](reserved_test.md#ansible-collections-ansible-utils-reserved-test) – Test for a reserved IP address
- [resolvable test](resolvable_test.md#ansible-collections-ansible-utils-resolvable-test) – Test if an IP or name can be resolved via /etc/hosts or DNS
- [subnet_of test](subnet_of_test.md#ansible-collections-ansible-utils-subnet-of-test) – Test if a network is a subnet of another network
- [supernet_of test](supernet_of_test.md#ansible-collections-ansible-utils-supernet-of-test) – Test if a network is a supernet of another network
- [unspecified test](unspecified_test.md#ansible-collections-ansible-utils-unspecified-test) – Test for an unspecified IP address
- [validate test](validate_test.md#ansible-collections-ansible-utils-validate-test) – Validate data with provided criteria

> **See also:**
>
> List of [collections](../../index.md#list-of-collections) with docs hosted here.
