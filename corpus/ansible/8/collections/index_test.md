---
collection: ansible
version: "8"
title: "Index of all Test Plugins"
source_url: https://docs.ansible.com/projects/ansible/8/collections/index_test.html
fetched_at: 2026-07-28T01:03:16+00:00
---
# Index of all Test Plugins

## ansible.builtin

- [ansible.builtin.abs](ansible/builtin/abs_test.md#ansible-collections-ansible-builtin-abs-test) – is the path absolute
- [ansible.builtin.all](ansible/builtin/all_test.md#ansible-collections-ansible-builtin-all-test) – are all conditions in a list true
- [ansible.builtin.any](ansible/builtin/any_test.md#ansible-collections-ansible-builtin-any-test) – is any conditions in a list true
- [ansible.builtin.changed](ansible/builtin/changed_test.md#ansible-collections-ansible-builtin-changed-test) – did the task require changes
- [ansible.builtin.contains](ansible/builtin/contains_test.md#ansible-collections-ansible-builtin-contains-test) – does the list contain this element
- [ansible.builtin.directory](ansible/builtin/directory_test.md#ansible-collections-ansible-builtin-directory-test) – does the path resolve to an existing directory
- [ansible.builtin.exists](ansible/builtin/exists_test.md#ansible-collections-ansible-builtin-exists-test) – does the path exist, follow symlinks
- [ansible.builtin.failed](ansible/builtin/failed_test.md#ansible-collections-ansible-builtin-failed-test) – did the task fail
- [ansible.builtin.falsy](ansible/builtin/falsy_test.md#ansible-collections-ansible-builtin-falsy-test) – Pythonic false
- [ansible.builtin.file](ansible/builtin/file_test.md#ansible-collections-ansible-builtin-file-test) – does the path resolve to an existing file
- [ansible.builtin.finished](ansible/builtin/finished_test.md#ansible-collections-ansible-builtin-finished-test) – Did async task finish
- [ansible.builtin.link](ansible/builtin/link_test.md#ansible-collections-ansible-builtin-link-test) – does the path reference existing symbolic link
- [ansible.builtin.link_exists](ansible/builtin/link_exists_test.md#ansible-collections-ansible-builtin-link-exists-test) – does the path exist, no follow
- [ansible.builtin.match](ansible/builtin/match_test.md#ansible-collections-ansible-builtin-match-test) – Does string match regular expression from the start
- [ansible.builtin.mount](ansible/builtin/mount_test.md#ansible-collections-ansible-builtin-mount-test) – does the path resolve to mount point
- [ansible.builtin.nan](ansible/builtin/nan_test.md#ansible-collections-ansible-builtin-nan-test) – is this not a number (NaN)
- [ansible.builtin.reachable](ansible/builtin/reachable_test.md#ansible-collections-ansible-builtin-reachable-test) – Task did not end due to unreachable host
- [ansible.builtin.regex](ansible/builtin/regex_test.md#ansible-collections-ansible-builtin-regex-test) – Does string match regular expression from the start
- [ansible.builtin.same_file](ansible/builtin/same_file_test.md#ansible-collections-ansible-builtin-same-file-test) – compares two paths to see if they resolve to the same filesystem object
- [ansible.builtin.search](ansible/builtin/search_test.md#ansible-collections-ansible-builtin-search-test) – Does string match a regular expression
- [ansible.builtin.skipped](ansible/builtin/skipped_test.md#ansible-collections-ansible-builtin-skipped-test) – Was task skipped
- [ansible.builtin.started](ansible/builtin/started_test.md#ansible-collections-ansible-builtin-started-test) – Was async task started
- [ansible.builtin.subset](ansible/builtin/subset_test.md#ansible-collections-ansible-builtin-subset-test) – is the list a subset of this other list
- [ansible.builtin.success](ansible/builtin/success_test.md#ansible-collections-ansible-builtin-success-test) – check task success
- [ansible.builtin.superset](ansible/builtin/superset_test.md#ansible-collections-ansible-builtin-superset-test) – is the list a superset of this other list
- [ansible.builtin.truthy](ansible/builtin/truthy_test.md#ansible-collections-ansible-builtin-truthy-test) – Pythonic true
- [ansible.builtin.unreachable](ansible/builtin/unreachable_test.md#ansible-collections-ansible-builtin-unreachable-test) – Did task end due to the host was unreachable
- [ansible.builtin.uri](ansible/builtin/uri_test.md#ansible-collections-ansible-builtin-uri-test) – is the string a valid URI
- [ansible.builtin.url](ansible/builtin/url_test.md#ansible-collections-ansible-builtin-url-test) – is the string a valid URL
- [ansible.builtin.urn](ansible/builtin/urn_test.md#ansible-collections-ansible-builtin-urn-test) – is the string a valid URN
- [ansible.builtin.vault_encrypted](ansible/builtin/vault_encrypted_test.md#ansible-collections-ansible-builtin-vault-encrypted-test) – Is this an encrypted vault
- [ansible.builtin.version](ansible/builtin/version_test.md#ansible-collections-ansible-builtin-version-test) – compare version strings

## ansible.utils

- [ansible.utils.in_any_network](ansible/utils/in_any_network_test.md#ansible-collections-ansible-utils-in-any-network-test) – Test if an IP or network falls in any network
- [ansible.utils.in_network](ansible/utils/in_network_test.md#ansible-collections-ansible-utils-in-network-test) – Test if IP address falls in the network
- [ansible.utils.in_one_network](ansible/utils/in_one_network_test.md#ansible-collections-ansible-utils-in-one-network-test) – Test if IP address belongs in any one of the networks in the list
- [ansible.utils.ip](ansible/utils/ip_test.md#ansible-collections-ansible-utils-ip-test) – Test if something in an IP address or network
- [ansible.utils.ip_address](ansible/utils/ip_address_test.md#ansible-collections-ansible-utils-ip-address-test) – Test if something in an IP address
- [ansible.utils.ipv4](ansible/utils/ipv4_test.md#ansible-collections-ansible-utils-ipv4-test) – Test if something is an IPv4 address or network
- [ansible.utils.ipv4_address](ansible/utils/ipv4_address_test.md#ansible-collections-ansible-utils-ipv4-address-test) – Test if something is an IPv4 address
- [ansible.utils.ipv4_hostmask](ansible/utils/ipv4_hostmask_test.md#ansible-collections-ansible-utils-ipv4-hostmask-test) – Test if an address is a valid hostmask
- [ansible.utils.ipv4_netmask](ansible/utils/ipv4_netmask_test.md#ansible-collections-ansible-utils-ipv4-netmask-test) – Test if an address is a valid netmask
- [ansible.utils.ipv6](ansible/utils/ipv6_test.md#ansible-collections-ansible-utils-ipv6-test) – Test if something is an IPv6 address or network
- [ansible.utils.ipv6_address](ansible/utils/ipv6_address_test.md#ansible-collections-ansible-utils-ipv6-address-test) – Test if something is an IPv6 address
- [ansible.utils.ipv6_ipv4_mapped](ansible/utils/ipv6_ipv4_mapped_test.md#ansible-collections-ansible-utils-ipv6-ipv4-mapped-test) – Test if something appears to be a mapped IPv6 to IPv4 mapped address
- [ansible.utils.ipv6_sixtofour](ansible/utils/ipv6_sixtofour_test.md#ansible-collections-ansible-utils-ipv6-sixtofour-test) – Test if something appears to be a 6to4 address
- [ansible.utils.ipv6_teredo](ansible/utils/ipv6_teredo_test.md#ansible-collections-ansible-utils-ipv6-teredo-test) – Test if something appears to be an IPv6 teredo address
- [ansible.utils.loopback](ansible/utils/loopback_test.md#ansible-collections-ansible-utils-loopback-test) – Test if an IP address is a loopback
- [ansible.utils.mac](ansible/utils/mac_test.md#ansible-collections-ansible-utils-mac-test) – Test if something appears to be a valid MAC address
- [ansible.utils.multicast](ansible/utils/multicast_test.md#ansible-collections-ansible-utils-multicast-test) – Test for a multicast IP address
- [ansible.utils.private](ansible/utils/private_test.md#ansible-collections-ansible-utils-private-test) – Test if an IP address is private
- [ansible.utils.public](ansible/utils/public_test.md#ansible-collections-ansible-utils-public-test) – Test if an IP address is public
- [ansible.utils.reserved](ansible/utils/reserved_test.md#ansible-collections-ansible-utils-reserved-test) – Test for a reserved IP address
- [ansible.utils.resolvable](ansible/utils/resolvable_test.md#ansible-collections-ansible-utils-resolvable-test) – Test if an IP or name can be resolved via /etc/hosts or DNS
- [ansible.utils.subnet_of](ansible/utils/subnet_of_test.md#ansible-collections-ansible-utils-subnet-of-test) – Test if a network is a subnet of another network
- [ansible.utils.supernet_of](ansible/utils/supernet_of_test.md#ansible-collections-ansible-utils-supernet-of-test) – Test if a network is a supernet of another network
- [ansible.utils.unspecified](ansible/utils/unspecified_test.md#ansible-collections-ansible-utils-unspecified-test) – Test for an unspecified IP address
- [ansible.utils.validate](ansible/utils/validate_test.md#ansible-collections-ansible-utils-validate-test) – Validate data with provided criteria

## community.general

- [community.general.a_module](community/general/a_module_test.md#ansible-collections-community-general-a-module-test) – Test whether a given string refers to an existing module or action plugin

## ovirt.ovirt

- [ovirt.ovirt.proxied](ovirt/ovirt/proxied_test.md#ansible-collections-ovirt-ovirt-proxied-test) –
