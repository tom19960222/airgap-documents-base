---
collection: kernel
version: "6.17"
title: "Family nftables netlink specification"
source_url: https://www.kernel.org/doc/html/v6.17/networking/netlink_spec/nftables.html
fetched_at: 2026-09-16T16:40:51+00:00
---
# [Family `nftables` netlink specification](nftables.md#id87)

Contents

- [Family `nftables` netlink specification](nftables.md#family-nftables-netlink-specification)

  - [Summary](nftables.md#summary)
  - [Operations](nftables.md#operations)

    - [batch-begin](nftables.md#batch-begin)
    - [batch-end](nftables.md#batch-end)
    - [newtable](nftables.md#newtable)
    - [gettable](nftables.md#gettable)
    - [deltable](nftables.md#deltable)
    - [destroytable](nftables.md#destroytable)
    - [newchain](nftables.md#newchain)
    - [getchain](nftables.md#getchain)
    - [delchain](nftables.md#delchain)
    - [destroychain](nftables.md#destroychain)
    - [newrule](nftables.md#newrule)
    - [getrule](nftables.md#getrule)
    - [getrule-reset](nftables.md#getrule-reset)
    - [delrule](nftables.md#delrule)
    - [destroyrule](nftables.md#destroyrule)
    - [newset](nftables.md#newset)
    - [getset](nftables.md#getset)
    - [delset](nftables.md#delset)
    - [destroyset](nftables.md#destroyset)
    - [newsetelem](nftables.md#newsetelem)
    - [getsetelem](nftables.md#getsetelem)
    - [getsetelem-reset](nftables.md#getsetelem-reset)
    - [delsetelem](nftables.md#delsetelem)
    - [destroysetelem](nftables.md#destroysetelem)
    - [getgen](nftables.md#getgen)
    - [newobj](nftables.md#newobj)
    - [getobj](nftables.md#getobj)
    - [delobj](nftables.md#delobj)
    - [destroyobj](nftables.md#destroyobj)
    - [newflowtable](nftables.md#newflowtable)
    - [getflowtable](nftables.md#getflowtable)
    - [delflowtable](nftables.md#delflowtable)
    - [destroyflowtable](nftables.md#destroyflowtable)
  - [Multicast groups](nftables.md#multicast-groups)
  - [Definitions](nftables.md#definitions)

    - [nfgenmsg](nftables.md#nfgenmsg)
    - [meta-keys](nftables.md#meta-keys)
    - [bitwise-ops](nftables.md#bitwise-ops)
    - [cmp-ops](nftables.md#cmp-ops)
    - [object-type](nftables.md#object-type)
    - [nat-range-flags](nftables.md#nat-range-flags)
    - [table-flags](nftables.md#table-flags)
    - [chain-flags](nftables.md#chain-flags)
    - [set-flags](nftables.md#set-flags)
    - [lookup-flags](nftables.md#lookup-flags)
    - [ct-keys](nftables.md#ct-keys)
    - [ct-direction](nftables.md#ct-direction)
    - [quota-flags](nftables.md#quota-flags)
    - [verdict-code](nftables.md#verdict-code)
    - [fib-result](nftables.md#fib-result)
    - [fib-flags](nftables.md#fib-flags)
    - [reject-types](nftables.md#reject-types)
  - [Attribute sets](nftables.md#attribute-sets)

    - [empty-attrs](nftables.md#empty-attrs)
    - [batch-attrs](nftables.md#batch-attrs)
    - [table-attrs](nftables.md#table-attrs)
    - [chain-attrs](nftables.md#chain-attrs)
    - [counter-attrs](nftables.md#counter-attrs)
    - [nft-hook-attrs](nftables.md#nft-hook-attrs)
    - [hook-dev-attrs](nftables.md#hook-dev-attrs)
    - [nft-counter-attrs](nftables.md#nft-counter-attrs)
    - [rule-attrs](nftables.md#rule-attrs)
    - [expr-list-attrs](nftables.md#expr-list-attrs)
    - [expr-attrs](nftables.md#expr-attrs)
    - [rule-compat-attrs](nftables.md#rule-compat-attrs)
    - [set-attrs](nftables.md#set-attrs)
    - [set-desc-attrs](nftables.md#set-desc-attrs)
    - [set-desc-concat-attrs](nftables.md#set-desc-concat-attrs)
    - [set-field-attrs](nftables.md#set-field-attrs)
    - [set-list-attrs](nftables.md#set-list-attrs)
    - [setelem-attrs](nftables.md#setelem-attrs)
    - [setelem-list-elem-attrs](nftables.md#setelem-list-elem-attrs)
    - [setelem-list-attrs](nftables.md#setelem-list-attrs)
    - [gen-attrs](nftables.md#gen-attrs)
    - [obj-attrs](nftables.md#obj-attrs)
    - [quota-attrs](nftables.md#quota-attrs)
    - [flowtable-attrs](nftables.md#flowtable-attrs)
    - [flowtable-hook-attrs](nftables.md#flowtable-hook-attrs)
    - [expr-bitwise-attrs](nftables.md#expr-bitwise-attrs)
    - [expr-cmp-attrs](nftables.md#expr-cmp-attrs)
    - [data-attrs](nftables.md#data-attrs)
    - [verdict-attrs](nftables.md#verdict-attrs)
    - [expr-counter-attrs](nftables.md#expr-counter-attrs)
    - [expr-fib-attrs](nftables.md#expr-fib-attrs)
    - [expr-ct-attrs](nftables.md#expr-ct-attrs)
    - [expr-flow-offload-attrs](nftables.md#expr-flow-offload-attrs)
    - [expr-immediate-attrs](nftables.md#expr-immediate-attrs)
    - [expr-lookup-attrs](nftables.md#expr-lookup-attrs)
    - [expr-meta-attrs](nftables.md#expr-meta-attrs)
    - [expr-nat-attrs](nftables.md#expr-nat-attrs)
    - [expr-payload-attrs](nftables.md#expr-payload-attrs)
    - [expr-reject-attrs](nftables.md#expr-reject-attrs)
    - [expr-target-attrs](nftables.md#expr-target-attrs)
    - [expr-tproxy-attrs](nftables.md#expr-tproxy-attrs)
    - [expr-objref-attrs](nftables.md#expr-objref-attrs)
  - [Sub-messages](nftables.md#sub-messages)

    - [expr-ops](nftables.md#expr-ops)
    - [obj-data](nftables.md#obj-data)

## [Summary](nftables.md#id88)

Netfilter nftables configuration over netlink.

## [Operations](nftables.md#id89)

### [batch-begin](nftables.md#id90)

Start a batch of operations

attribute-set:
:   [batch-attrs](nftables.md#nftables-attribute-set-batch-attrs)

fixed-header:
:   [nfgenmsg](nftables.md#nftables-definition-nfgenmsg)

do:
:   **request**
    :   attributes:
        :   [`genid`]

    **reply**
    :   attributes:
        :   [`genid`]

### [batch-end](nftables.md#id91)

Finish a batch of operations

attribute-set:
:   [batch-attrs](nftables.md#nftables-attribute-set-batch-attrs)

fixed-header:
:   [nfgenmsg](nftables.md#nftables-definition-nfgenmsg)

do:
:   **request**
    :   attributes:
        :   [`genid`]

### [newtable](nftables.md#id92)

Create a new table.

attribute-set:
:   [table-attrs](nftables.md#nftables-attribute-set-table-attrs)

fixed-header:
:   [nfgenmsg](nftables.md#nftables-definition-nfgenmsg)

do:
:   **request**
    :   attributes:
        :   [`name`]

### [gettable](nftables.md#id93)

Get / dump tables.

attribute-set:
:   [table-attrs](nftables.md#nftables-attribute-set-table-attrs)

fixed-header:
:   [nfgenmsg](nftables.md#nftables-definition-nfgenmsg)

do:
:   **request**
    :   attributes:
        :   [`name`]

    **reply**
    :   attributes:
        :   [`name`]

### [deltable](nftables.md#id94)

Delete an existing table.

attribute-set:
:   [table-attrs](nftables.md#nftables-attribute-set-table-attrs)

fixed-header:
:   [nfgenmsg](nftables.md#nftables-definition-nfgenmsg)

do:
:   **request**
    :   attributes:
        :   [`name`]

### [destroytable](nftables.md#id95)

Delete an existing table with destroy semantics (ignoring ENOENT
errors).

attribute-set:
:   [table-attrs](nftables.md#nftables-attribute-set-table-attrs)

fixed-header:
:   [nfgenmsg](nftables.md#nftables-definition-nfgenmsg)

do:
:   **request**
    :   attributes:
        :   [`name`]

### [newchain](nftables.md#id96)

Create a new chain.

attribute-set:
:   [chain-attrs](nftables.md#nftables-attribute-set-chain-attrs)

fixed-header:
:   [nfgenmsg](nftables.md#nftables-definition-nfgenmsg)

do:
:   **request**
    :   attributes:
        :   [`name`]

### [getchain](nftables.md#id97)

Get / dump chains.

attribute-set:
:   [chain-attrs](nftables.md#nftables-attribute-set-chain-attrs)

fixed-header:
:   [nfgenmsg](nftables.md#nftables-definition-nfgenmsg)

do:
:   **request**
    :   attributes:
        :   [`name`]

    **reply**
    :   attributes:
        :   [`name`]

### [delchain](nftables.md#id98)

Delete an existing chain.

attribute-set:
:   [chain-attrs](nftables.md#nftables-attribute-set-chain-attrs)

fixed-header:
:   [nfgenmsg](nftables.md#nftables-definition-nfgenmsg)

do:
:   **request**
    :   attributes:
        :   [`name`]

### [destroychain](nftables.md#id99)

Delete an existing chain with destroy semantics (ignoring ENOENT
errors).

attribute-set:
:   [chain-attrs](nftables.md#nftables-attribute-set-chain-attrs)

fixed-header:
:   [nfgenmsg](nftables.md#nftables-definition-nfgenmsg)

do:
:   **request**
    :   attributes:
        :   [`name`]

### [newrule](nftables.md#id100)

Create a new rule.

attribute-set:
:   [rule-attrs](nftables.md#nftables-attribute-set-rule-attrs)

fixed-header:
:   [nfgenmsg](nftables.md#nftables-definition-nfgenmsg)

do:
:   **request**
    :   attributes:
        :   [`name`]

### [getrule](nftables.md#id101)

Get / dump rules.

attribute-set:
:   [rule-attrs](nftables.md#nftables-attribute-set-rule-attrs)

fixed-header:
:   [nfgenmsg](nftables.md#nftables-definition-nfgenmsg)

do:
:   **request**
    :   attributes:
        :   [`name`]

    **reply**
    :   attributes:
        :   [`name`]

### [getrule-reset](nftables.md#id102)

Get / dump rules and reset stateful expressions.

attribute-set:
:   [rule-attrs](nftables.md#nftables-attribute-set-rule-attrs)

fixed-header:
:   [nfgenmsg](nftables.md#nftables-definition-nfgenmsg)

do:
:   **request**
    :   attributes:
        :   [`name`]

    **reply**
    :   attributes:
        :   [`name`]

### [delrule](nftables.md#id103)

Delete an existing rule.

attribute-set:
:   [rule-attrs](nftables.md#nftables-attribute-set-rule-attrs)

fixed-header:
:   [nfgenmsg](nftables.md#nftables-definition-nfgenmsg)

do:
:   **request**
    :   attributes:
        :   [`name`]

### [destroyrule](nftables.md#id104)

Delete an existing rule with destroy semantics (ignoring ENOENT errors).

attribute-set:
:   [rule-attrs](nftables.md#nftables-attribute-set-rule-attrs)

fixed-header:
:   [nfgenmsg](nftables.md#nftables-definition-nfgenmsg)

do:
:   **request**
    :   attributes:
        :   [`name`]

### [newset](nftables.md#id105)

Create a new set.

attribute-set:
:   [set-attrs](nftables.md#nftables-attribute-set-set-attrs)

fixed-header:
:   [nfgenmsg](nftables.md#nftables-definition-nfgenmsg)

do:
:   **request**
    :   attributes:
        :   [`name`]

### [getset](nftables.md#id106)

Get / dump sets.

attribute-set:
:   [set-attrs](nftables.md#nftables-attribute-set-set-attrs)

fixed-header:
:   [nfgenmsg](nftables.md#nftables-definition-nfgenmsg)

do:
:   **request**
    :   attributes:
        :   [`name`]

    **reply**
    :   attributes:
        :   [`name`]

### [delset](nftables.md#id107)

Delete an existing set.

attribute-set:
:   [set-attrs](nftables.md#nftables-attribute-set-set-attrs)

fixed-header:
:   [nfgenmsg](nftables.md#nftables-definition-nfgenmsg)

do:
:   **request**
    :   attributes:
        :   [`name`]

### [destroyset](nftables.md#id108)

Delete an existing set with destroy semantics (ignoring ENOENT errors).

attribute-set:
:   [set-attrs](nftables.md#nftables-attribute-set-set-attrs)

fixed-header:
:   [nfgenmsg](nftables.md#nftables-definition-nfgenmsg)

do:
:   **request**
    :   attributes:
        :   [`name`]

### [newsetelem](nftables.md#id109)

Create a new set element.

attribute-set:
:   [setelem-list-attrs](nftables.md#nftables-attribute-set-setelem-list-attrs)

fixed-header:
:   [nfgenmsg](nftables.md#nftables-definition-nfgenmsg)

do:
:   **request**
    :   attributes:
        :   [`name`]

### [getsetelem](nftables.md#id110)

Get / dump set elements.

attribute-set:
:   [setelem-list-attrs](nftables.md#nftables-attribute-set-setelem-list-attrs)

fixed-header:
:   [nfgenmsg](nftables.md#nftables-definition-nfgenmsg)

do:
:   **request**
    :   attributes:
        :   [`name`]

    **reply**
    :   attributes:
        :   [`name`]

### [getsetelem-reset](nftables.md#id111)

Get / dump set elements and reset stateful expressions.

attribute-set:
:   [setelem-list-attrs](nftables.md#nftables-attribute-set-setelem-list-attrs)

fixed-header:
:   [nfgenmsg](nftables.md#nftables-definition-nfgenmsg)

do:
:   **request**
    :   attributes:
        :   [`name`]

    **reply**
    :   attributes:
        :   [`name`]

### [delsetelem](nftables.md#id112)

Delete an existing set element.

attribute-set:
:   [setelem-list-attrs](nftables.md#nftables-attribute-set-setelem-list-attrs)

fixed-header:
:   [nfgenmsg](nftables.md#nftables-definition-nfgenmsg)

do:
:   **request**
    :   attributes:
        :   [`name`]

### [destroysetelem](nftables.md#id113)

Delete an existing set element with destroy semantics.

attribute-set:
:   [setelem-list-attrs](nftables.md#nftables-attribute-set-setelem-list-attrs)

fixed-header:
:   [nfgenmsg](nftables.md#nftables-definition-nfgenmsg)

do:
:   **request**
    :   attributes:
        :   [`name`]

### [getgen](nftables.md#id114)

Get / dump rule-set generation.

attribute-set:
:   [gen-attrs](nftables.md#nftables-attribute-set-gen-attrs)

fixed-header:
:   [nfgenmsg](nftables.md#nftables-definition-nfgenmsg)

do:
:   **request**
    :   attributes:
        :   [`name`]

    **reply**
    :   attributes:
        :   [`name`]

### [newobj](nftables.md#id115)

Create a new stateful object.

attribute-set:
:   [obj-attrs](nftables.md#nftables-attribute-set-obj-attrs)

fixed-header:
:   [nfgenmsg](nftables.md#nftables-definition-nfgenmsg)

do:
:   **request**
    :   attributes:
        :   [`name`]

### [getobj](nftables.md#id116)

Get / dump stateful objects.

attribute-set:
:   [obj-attrs](nftables.md#nftables-attribute-set-obj-attrs)

fixed-header:
:   [nfgenmsg](nftables.md#nftables-definition-nfgenmsg)

do:
:   **request**
    :   attributes:
        :   [`name`]

    **reply**
    :   attributes:
        :   [`name`]

### [delobj](nftables.md#id117)

Delete an existing stateful object.

attribute-set:
:   [obj-attrs](nftables.md#nftables-attribute-set-obj-attrs)

fixed-header:
:   [nfgenmsg](nftables.md#nftables-definition-nfgenmsg)

do:
:   **request**
    :   attributes:
        :   [`name`]

### [destroyobj](nftables.md#id118)

Delete an existing stateful object with destroy semantics.

attribute-set:
:   [obj-attrs](nftables.md#nftables-attribute-set-obj-attrs)

fixed-header:
:   [nfgenmsg](nftables.md#nftables-definition-nfgenmsg)

do:
:   **request**
    :   attributes:
        :   [`name`]

### [newflowtable](nftables.md#id119)

Create a new flow table.

attribute-set:
:   [flowtable-attrs](nftables.md#nftables-attribute-set-flowtable-attrs)

fixed-header:
:   [nfgenmsg](nftables.md#nftables-definition-nfgenmsg)

do:
:   **request**
    :   attributes:
        :   [`name`]

### [getflowtable](nftables.md#id120)

Get / dump flow tables.

attribute-set:
:   [flowtable-attrs](nftables.md#nftables-attribute-set-flowtable-attrs)

fixed-header:
:   [nfgenmsg](nftables.md#nftables-definition-nfgenmsg)

do:
:   **request**
    :   attributes:
        :   [`name`]

    **reply**
    :   attributes:
        :   [`name`]

### [delflowtable](nftables.md#id121)

Delete an existing flow table.

attribute-set:
:   [flowtable-attrs](nftables.md#nftables-attribute-set-flowtable-attrs)

fixed-header:
:   [nfgenmsg](nftables.md#nftables-definition-nfgenmsg)

do:
:   **request**
    :   attributes:
        :   [`name`]

### [destroyflowtable](nftables.md#id122)

Delete an existing flow table with destroy semantics.

attribute-set:
:   [flowtable-attrs](nftables.md#nftables-attribute-set-flowtable-attrs)

fixed-header:
:   [nfgenmsg](nftables.md#nftables-definition-nfgenmsg)

do:
:   **request**
    :   attributes:
        :   [`name`]

## [Multicast groups](nftables.md#id123)

- mgmt

## [Definitions](nftables.md#id124)

### [nfgenmsg](nftables.md#id125)

type:
:   struct

members:
:   nfgen-family (`u8`):

    version (`u8`):

    res-id (`u16`):

### [meta-keys](nftables.md#id126)

type:
:   enum

entries:
:   - `len`
    - `protocol`
    - `priority`
    - `mark`
    - `iif`
    - `oif`
    - `iifname`
    - `oifname`
    - `iftype`
    - `oiftype`
    - `skuid`
    - `skgid`
    - `nftrace`
    - `rtclassid`
    - `secmark`
    - `nfproto`
    - `l4-proto`
    - `bri-iifname`
    - `bri-oifname`
    - `pkttype`
    - `cpu`
    - `iifgroup`
    - `oifgroup`
    - `cgroup`
    - `prandom`
    - `secpath`
    - `iifkind`
    - `oifkind`
    - `bri-iifpvid`
    - `bri-iifvproto`
    - `time-ns`
    - `time-day`
    - `time-hour`
    - `sdif`
    - `sdifname`
    - `bri-broute`

### [bitwise-ops](nftables.md#id127)

type:
:   enum

entries:
:   - `bool`
    - `lshift`
    - `rshift`

### [cmp-ops](nftables.md#id128)

type:
:   enum

entries:
:   - `eq`
    - `neq`
    - `lt`
    - `lte`
    - `gt`
    - `gte`

### [object-type](nftables.md#id129)

type:
:   enum

entries:
:   - `unspec`
    - `counter`
    - `quota`
    - `ct-helper`
    - `limit`
    - `connlimit`
    - `tunnel`
    - `ct-timeout`
    - `secmark`
    - `ct-expect`
    - `synproxy`

### [nat-range-flags](nftables.md#id130)

type:
:   flags

entries:
:   - `map-ips`
    - `proto-specified`
    - `proto-random`
    - `persistent`
    - `proto-random-fully`
    - `proto-offset`
    - `netmap`

### [table-flags](nftables.md#id131)

type:
:   flags

entries:
:   - `dormant`
    - `owner`
    - `persist`

### [chain-flags](nftables.md#id132)

type:
:   flags

entries:
:   - `base`
    - `hw-offload`
    - `binding`

### [set-flags](nftables.md#id133)

type:
:   flags

entries:
:   - `anonymous`
    - `constant`
    - `interval`
    - `map`
    - `timeout`
    - `eval`
    - `object`
    - `concat`
    - `expr`

### [lookup-flags](nftables.md#id134)

type:
:   flags

entries:
:   - `invert`

### [ct-keys](nftables.md#id135)

type:
:   enum

entries:
:   - `state`
    - `direction`
    - `status`
    - `mark`
    - `secmark`
    - `expiration`
    - `helper`
    - `l3protocol`
    - `src`
    - `dst`
    - `protocol`
    - `proto-src`
    - `proto-dst`
    - `labels`
    - `pkts`
    - `bytes`
    - `avgpkt`
    - `zone`
    - `eventmask`
    - `src-ip`
    - `dst-ip`
    - `src-ip6`
    - `dst-ip6`
    - `ct-id`

### [ct-direction](nftables.md#id136)

type:
:   enum

entries:
:   - `original`
    - `reply`

### [quota-flags](nftables.md#id137)

type:
:   flags

entries:
:   - `invert`
    - `depleted`

### [verdict-code](nftables.md#id138)

type:
:   enum

entries:
:   continue:

    break:

    jump:

    goto:

    return:

    drop:

    accept:

    stolen:

    queue:

    repeat:

### [fib-result](nftables.md#id139)

type:
:   enum

entries:
:   - `oif`
    - `oifname`
    - `addrtype`

### [fib-flags](nftables.md#id140)

type:
:   flags

entries:
:   - `saddr`
    - `daddr`
    - `mark`
    - `iif`
    - `oif`
    - `present`

### [reject-types](nftables.md#id141)

type:
:   enum

entries:
:   - `icmp-unreach`
    - `tcp-rst`
    - `icmpx-unreach`

## [Attribute sets](nftables.md#id142)

### [empty-attrs](nftables.md#id143)

#### name (`string`)

### [batch-attrs](nftables.md#id144)

#### genid (`u32`)

byte-order:
:   big-endian

### [table-attrs](nftables.md#id145)

#### name (`string`)

doc:
:   name of the table

#### flags (`u32`)

byte-order:
:   big-endian

doc:
:   bitmask of flags

enum:
:   [table-flags](nftables.md#nftables-definition-table-flags)

enum-as-flags:
:   True

#### use (`u32`)

byte-order:
:   big-endian

doc:
:   number of chains in this table

#### handle (`u64`)

byte-order:
:   big-endian

doc:
:   numeric handle of the table

#### userdata (`binary`)

doc:
:   user data

### [chain-attrs](nftables.md#id146)

#### table (`string`)

doc:
:   name of the table containing the chain

#### handle (`u64`)

byte-order:
:   big-endian

doc:
:   numeric handle of the chain

#### name (`string`)

doc:
:   name of the chain

#### hook (`nest`)

nested-attributes:
:   [nft-hook-attrs](nftables.md#nftables-attribute-set-nft-hook-attrs)

doc:
:   hook specification for basechains

#### policy (`u32`)

byte-order:
:   big-endian

doc:
:   numeric policy of the chain

#### use (`u32`)

byte-order:
:   big-endian

doc:
:   number of references to this chain

#### type (`string`)

doc:
:   type name of the chain

#### counters (`nest`)

nested-attributes:
:   [nft-counter-attrs](nftables.md#nftables-attribute-set-nft-counter-attrs)

doc:
:   counter specification of the chain

#### flags (`u32`)

byte-order:
:   big-endian

doc:
:   chain flags

enum:
:   [chain-flags](nftables.md#nftables-definition-chain-flags)

enum-as-flags:
:   True

#### id (`u32`)

byte-order:
:   big-endian

doc:
:   uniquely identifies a chain in a transaction

#### userdata (`binary`)

doc:
:   user data

### [counter-attrs](nftables.md#id147)

#### bytes (`u64`)

byte-order:
:   big-endian

#### packets (`u64`)

byte-order:
:   big-endian

#### pad (`pad`)

### [nft-hook-attrs](nftables.md#id148)

#### num (`u32`)

byte-order:
:   big-endian

#### priority (`s32`)

byte-order:
:   big-endian

#### dev (`string`)

doc:
:   net device name

#### devs (`nest`)

nested-attributes:
:   [hook-dev-attrs](nftables.md#nftables-attribute-set-hook-dev-attrs)

doc:
:   list of net devices

### [hook-dev-attrs](nftables.md#id149)

#### name (`string`)

multi-attr:
:   True

### [nft-counter-attrs](nftables.md#id150)

#### bytes (`u64`)

#### packets (`u64`)

### [rule-attrs](nftables.md#id151)

#### table (`string`)

doc:
:   name of the table containing the rule

#### chain (`string`)

doc:
:   name of the chain containing the rule

#### handle (`u64`)

byte-order:
:   big-endian

doc:
:   numeric handle of the rule

#### expressions (`nest`)

nested-attributes:
:   [expr-list-attrs](nftables.md#nftables-attribute-set-expr-list-attrs)

doc:
:   list of expressions

#### compat (`nest`)

nested-attributes:
:   [rule-compat-attrs](nftables.md#nftables-attribute-set-rule-compat-attrs)

doc:
:   compatibility specifications of the rule

#### position (`u64`)

byte-order:
:   big-endian

doc:
:   numeric handle of the previous rule

#### userdata (`binary`)

doc:
:   user data

#### id (`u32`)

doc:
:   uniquely identifies a rule in a transaction

#### position-id (`u32`)

doc:
:   transaction unique identifier of the previous rule

#### chain-id (`u32`)

doc:
:   add the rule to chain by ID, alternative to chain name

### [expr-list-attrs](nftables.md#id152)

#### elem (`nest`)

nested-attributes:
:   [expr-attrs](nftables.md#nftables-attribute-set-expr-attrs)

multi-attr:
:   True

### [expr-attrs](nftables.md#id153)

#### name (`string`)

doc:
:   name of the expression type

#### data (`sub-message`)

sub-message:
:   [expr-ops](nftables.md#nftables-sub-message-expr-ops)

selector:
:   name

doc:
:   type specific data

### [rule-compat-attrs](nftables.md#id154)

#### proto (`binary`)

doc:
:   numeric value of the handled protocol

#### flags (`binary`)

doc:
:   bitmask of flags

### [set-attrs](nftables.md#id155)

#### table (`string`)

doc:
:   table name

#### name (`string`)

doc:
:   set name

#### flags (`u32`)

enum:
:   [set-flags](nftables.md#nftables-definition-set-flags)

byte-order:
:   big-endian

doc:
:   bitmask of `enum nft_set_flags`

#### key-type (`u32`)

byte-order:
:   big-endian

doc:
:   key data type, informational purpose only

#### key-len (`u32`)

byte-order:
:   big-endian

doc:
:   key data length

#### data-type (`u32`)

byte-order:
:   big-endian

doc:
:   mapping data type

#### data-len (`u32`)

byte-order:
:   big-endian

doc:
:   mapping data length

#### policy (`u32`)

byte-order:
:   big-endian

doc:
:   selection policy

#### desc (`nest`)

nested-attributes:
:   [set-desc-attrs](nftables.md#nftables-attribute-set-set-desc-attrs)

doc:
:   set description

#### id (`u32`)

doc:
:   uniquely identifies a set in a transaction

#### timeout (`u64`)

doc:
:   default timeout value

#### gc-interval (`u32`)

doc:
:   garbage collection interval

#### userdata (`binary`)

doc:
:   user data

#### pad (`pad`)

#### obj-type (`u32`)

byte-order:
:   big-endian

doc:
:   stateful object type

#### handle (`u64`)

byte-order:
:   big-endian

doc:
:   set handle

#### expr (`nest`)

nested-attributes:
:   [expr-attrs](nftables.md#nftables-attribute-set-expr-attrs)

doc:
:   set expression

multi-attr:
:   True

#### expressions (`nest`)

nested-attributes:
:   [set-list-attrs](nftables.md#nftables-attribute-set-set-list-attrs)

doc:
:   list of expressions

### [set-desc-attrs](nftables.md#id156)

#### size (`u32`)

byte-order:
:   big-endian

doc:
:   number of elements in set

#### concat (`nest`)

nested-attributes:
:   [set-desc-concat-attrs](nftables.md#nftables-attribute-set-set-desc-concat-attrs)

doc:
:   description of field concatenation

multi-attr:
:   True

### [set-desc-concat-attrs](nftables.md#id157)

#### elem (`nest`)

nested-attributes:
:   [set-field-attrs](nftables.md#nftables-attribute-set-set-field-attrs)

### [set-field-attrs](nftables.md#id158)

#### len (`u32`)

byte-order:
:   big-endian

### [set-list-attrs](nftables.md#id159)

#### elem (`nest`)

nested-attributes:
:   [expr-attrs](nftables.md#nftables-attribute-set-expr-attrs)

multi-attr:
:   True

### [setelem-attrs](nftables.md#id160)

#### key (`nest`)

nested-attributes:
:   [data-attrs](nftables.md#nftables-attribute-set-data-attrs)

doc:
:   key value

#### data (`nest`)

nested-attributes:
:   [data-attrs](nftables.md#nftables-attribute-set-data-attrs)

doc:
:   data value of mapping

#### flags (`binary`)

doc:
:   bitmask of nft_set_elem_flags

#### timeout (`u64`)

doc:
:   timeout value

#### expiration (`u64`)

doc:
:   expiration time

#### userdata (`binary`)

doc:
:   user data

#### expr (`nest`)

nested-attributes:
:   [expr-attrs](nftables.md#nftables-attribute-set-expr-attrs)

doc:
:   expression

#### objref (`string`)

doc:
:   stateful object reference

#### key-end (`nest`)

nested-attributes:
:   [data-attrs](nftables.md#nftables-attribute-set-data-attrs)

doc:
:   closing key value

#### expressions (`nest`)

nested-attributes:
:   [expr-list-attrs](nftables.md#nftables-attribute-set-expr-list-attrs)

doc:
:   list of expressions

### [setelem-list-elem-attrs](nftables.md#id161)

#### elem (`nest`)

nested-attributes:
:   [setelem-attrs](nftables.md#nftables-attribute-set-setelem-attrs)

multi-attr:
:   True

### [setelem-list-attrs](nftables.md#id162)

#### table (`string`)

#### set (`string`)

#### elements (`nest`)

nested-attributes:
:   [setelem-list-elem-attrs](nftables.md#nftables-attribute-set-setelem-list-elem-attrs)

#### set-id (`u32`)

### [gen-attrs](nftables.md#id163)

#### id (`u32`)

byte-order:
:   big-endian

doc:
:   ruleset generation id

#### proc-pid (`u32`)

byte-order:
:   big-endian

#### proc-name (`string`)

### [obj-attrs](nftables.md#id164)

#### table (`string`)

doc:
:   name of the table containing the expression

#### name (`string`)

doc:
:   name of this expression type

#### type (`u32`)

enum:
:   [object-type](nftables.md#nftables-definition-object-type)

byte-order:
:   big-endian

doc:
:   stateful object type

#### data (`sub-message`)

sub-message:
:   [obj-data](nftables.md#nftables-sub-message-obj-data)

selector:
:   type

doc:
:   stateful object data

#### use (`u32`)

byte-order:
:   big-endian

doc:
:   number of references to this expression

#### handle (`u64`)

byte-order:
:   big-endian

doc:
:   object handle

#### pad (`pad`)

#### userdata (`binary`)

doc:
:   user data

### [quota-attrs](nftables.md#id165)

#### bytes (`u64`)

byte-order:
:   big-endian

#### flags (`u32`)

byte-order:
:   big-endian

enum:
:   [quota-flags](nftables.md#nftables-definition-quota-flags)

#### pad (`pad`)

#### consumed (`u64`)

byte-order:
:   big-endian

### [flowtable-attrs](nftables.md#id166)

#### table (`string`)

#### name (`string`)

#### hook (`nest`)

nested-attributes:
:   [flowtable-hook-attrs](nftables.md#nftables-attribute-set-flowtable-hook-attrs)

#### use (`u32`)

byte-order:
:   big-endian

#### handle (`u64`)

byte-order:
:   big-endian

#### pad (`pad`)

#### flags (`u32`)

byte-order:
:   big-endian

### [flowtable-hook-attrs](nftables.md#id167)

#### num (`u32`)

byte-order:
:   big-endian

#### priority (`u32`)

byte-order:
:   big-endian

#### devs (`nest`)

nested-attributes:
:   [hook-dev-attrs](nftables.md#nftables-attribute-set-hook-dev-attrs)

### [expr-bitwise-attrs](nftables.md#id168)

#### sreg (`u32`)

byte-order:
:   big-endian

#### dreg (`u32`)

byte-order:
:   big-endian

#### len (`u32`)

byte-order:
:   big-endian

#### mask (`nest`)

nested-attributes:
:   [data-attrs](nftables.md#nftables-attribute-set-data-attrs)

#### xor (`nest`)

nested-attributes:
:   [data-attrs](nftables.md#nftables-attribute-set-data-attrs)

#### op (`u32`)

byte-order:
:   big-endian

enum:
:   [bitwise-ops](nftables.md#nftables-definition-bitwise-ops)

#### data (`nest`)

nested-attributes:
:   [data-attrs](nftables.md#nftables-attribute-set-data-attrs)

### [expr-cmp-attrs](nftables.md#id169)

#### sreg (`u32`)

byte-order:
:   big-endian

#### op (`u32`)

byte-order:
:   big-endian

enum:
:   [cmp-ops](nftables.md#nftables-definition-cmp-ops)

#### data (`nest`)

nested-attributes:
:   [data-attrs](nftables.md#nftables-attribute-set-data-attrs)

### [data-attrs](nftables.md#id170)

#### value (`binary`)

#### verdict (`nest`)

nested-attributes:
:   [verdict-attrs](nftables.md#nftables-attribute-set-verdict-attrs)

### [verdict-attrs](nftables.md#id171)

#### code (`u32`)

byte-order:
:   big-endian

enum:
:   [verdict-code](nftables.md#nftables-definition-verdict-code)

#### chain (`string`)

#### chain-id (`u32`)

### [expr-counter-attrs](nftables.md#id172)

#### bytes (`u64`)

doc:
:   Number of bytes

#### packets (`u64`)

doc:
:   Number of packets

#### pad (`pad`)

### [expr-fib-attrs](nftables.md#id173)

#### dreg (`u32`)

byte-order:
:   big-endian

#### result (`u32`)

byte-order:
:   big-endian

enum:
:   [fib-result](nftables.md#nftables-definition-fib-result)

#### flags (`u32`)

byte-order:
:   big-endian

enum:
:   [fib-flags](nftables.md#nftables-definition-fib-flags)

### [expr-ct-attrs](nftables.md#id174)

#### dreg (`u32`)

byte-order:
:   big-endian

#### key (`u32`)

byte-order:
:   big-endian

enum:
:   [ct-keys](nftables.md#nftables-definition-ct-keys)

#### direction (`u8`)

enum:
:   [ct-direction](nftables.md#nftables-definition-ct-direction)

#### sreg (`u32`)

byte-order:
:   big-endian

### [expr-flow-offload-attrs](nftables.md#id175)

#### name (`string`)

doc:
:   Flow offload table name

### [expr-immediate-attrs](nftables.md#id176)

#### dreg (`u32`)

byte-order:
:   big-endian

#### data (`nest`)

nested-attributes:
:   [data-attrs](nftables.md#nftables-attribute-set-data-attrs)

### [expr-lookup-attrs](nftables.md#id177)

#### set (`string`)

doc:
:   Name of set to use

#### set id (`u32`)

byte-order:
:   big-endian

doc:
:   ID of set to use

#### sreg (`u32`)

byte-order:
:   big-endian

#### dreg (`u32`)

byte-order:
:   big-endian

#### flags (`u32`)

byte-order:
:   big-endian

enum:
:   [lookup-flags](nftables.md#nftables-definition-lookup-flags)

### [expr-meta-attrs](nftables.md#id178)

#### dreg (`u32`)

byte-order:
:   big-endian

#### key (`u32`)

byte-order:
:   big-endian

enum:
:   [meta-keys](nftables.md#nftables-definition-meta-keys)

#### sreg (`u32`)

byte-order:
:   big-endian

### [expr-nat-attrs](nftables.md#id179)

#### type (`u32`)

byte-order:
:   big-endian

#### family (`u32`)

byte-order:
:   big-endian

#### reg-addr-min (`u32`)

byte-order:
:   big-endian

#### reg-addr-max (`u32`)

byte-order:
:   big-endian

#### reg-proto-min (`u32`)

byte-order:
:   big-endian

#### reg-proto-max (`u32`)

byte-order:
:   big-endian

#### flags (`u32`)

byte-order:
:   big-endian

enum:
:   [nat-range-flags](nftables.md#nftables-definition-nat-range-flags)

enum-as-flags:
:   True

### [expr-payload-attrs](nftables.md#id180)

#### dreg (`u32`)

byte-order:
:   big-endian

#### base (`u32`)

byte-order:
:   big-endian

#### offset (`u32`)

byte-order:
:   big-endian

#### len (`u32`)

byte-order:
:   big-endian

#### sreg (`u32`)

byte-order:
:   big-endian

#### csum-type (`u32`)

byte-order:
:   big-endian

#### csum-offset (`u32`)

byte-order:
:   big-endian

#### csum-flags (`u32`)

byte-order:
:   big-endian

### [expr-reject-attrs](nftables.md#id181)

#### type (`u32`)

byte-order:
:   big-endian

enum:
:   [reject-types](nftables.md#nftables-definition-reject-types)

#### icmp-code (`u8`)

### [expr-target-attrs](nftables.md#id182)

#### name (`string`)

#### rev (`u32`)

byte-order:
:   big-endian

#### info (`binary`)

### [expr-tproxy-attrs](nftables.md#id183)

#### family (`u32`)

byte-order:
:   big-endian

#### reg-addr (`u32`)

byte-order:
:   big-endian

#### reg-port (`u32`)

byte-order:
:   big-endian

### [expr-objref-attrs](nftables.md#id184)

#### imm-type (`u32`)

byte-order:
:   big-endian

#### imm-name (`string`)

doc:
:   object name

#### set-sreg (`u32`)

byte-order:
:   big-endian

#### set-name (`string`)

doc:
:   name of object map

#### set-id (`u32`)

byte-order:
:   big-endian

doc:
:   id of object map

## [Sub-messages](nftables.md#id185)

### [expr-ops](nftables.md#id186)

- **bitwise**
  :   attribute-set:
      :   [expr-bitwise-attrs](nftables.md#nftables-attribute-set-expr-bitwise-attrs)
- **cmp**
  :   attribute-set:
      :   [expr-cmp-attrs](nftables.md#nftables-attribute-set-expr-cmp-attrs)
- **counter**
  :   attribute-set:
      :   [expr-counter-attrs](nftables.md#nftables-attribute-set-expr-counter-attrs)
- **ct**
  :   attribute-set:
      :   [expr-ct-attrs](nftables.md#nftables-attribute-set-expr-ct-attrs)
- **fib**
  :   attribute-set:
      :   [expr-fib-attrs](nftables.md#nftables-attribute-set-expr-fib-attrs)
- **flow_offload**
  :   attribute-set:
      :   [expr-flow-offload-attrs](nftables.md#nftables-attribute-set-expr-flow-offload-attrs)
- **immediate**
  :   attribute-set:
      :   [expr-immediate-attrs](nftables.md#nftables-attribute-set-expr-immediate-attrs)
- **lookup**
  :   attribute-set:
      :   [expr-lookup-attrs](nftables.md#nftables-attribute-set-expr-lookup-attrs)
- **meta**
  :   attribute-set:
      :   [expr-meta-attrs](nftables.md#nftables-attribute-set-expr-meta-attrs)
- **nat**
  :   attribute-set:
      :   [expr-nat-attrs](nftables.md#nftables-attribute-set-expr-nat-attrs)
- **objref**
  :   attribute-set:
      :   [expr-objref-attrs](nftables.md#nftables-attribute-set-expr-objref-attrs)
- **payload**
  :   attribute-set:
      :   [expr-payload-attrs](nftables.md#nftables-attribute-set-expr-payload-attrs)
- **quota**
  :   attribute-set:
      :   [quota-attrs](nftables.md#nftables-attribute-set-quota-attrs)
- **reject**
  :   attribute-set:
      :   [expr-reject-attrs](nftables.md#nftables-attribute-set-expr-reject-attrs)
- **target**
  :   attribute-set:
      :   [expr-target-attrs](nftables.md#nftables-attribute-set-expr-target-attrs)
- **tproxy**
  :   attribute-set:
      :   [expr-tproxy-attrs](nftables.md#nftables-attribute-set-expr-tproxy-attrs)

### [obj-data](nftables.md#id187)

- **counter**
  :   attribute-set:
      :   [counter-attrs](nftables.md#nftables-attribute-set-counter-attrs)
- **quota**
  :   attribute-set:
      :   [quota-attrs](nftables.md#nftables-attribute-set-quota-attrs)
