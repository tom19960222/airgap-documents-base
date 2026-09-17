---
collection: kernel
version: "6.17"
title: "Family devlink netlink specification"
source_url: https://www.kernel.org/doc/html/v6.17/networking/netlink_spec/devlink.html
fetched_at: 2026-09-16T16:40:45+00:00
---
# [Family `devlink` netlink specification](devlink.md#id21)

Contents

- [Family `devlink` netlink specification](devlink.md#family-devlink-netlink-specification)

  - [Summary](devlink.md#summary)
  - [Operations](devlink.md#operations)

    - [get](devlink.md#get)
    - [port-get](devlink.md#port-get)
    - [port-set](devlink.md#port-set)
    - [port-new](devlink.md#port-new)
    - [port-del](devlink.md#port-del)
    - [port-split](devlink.md#port-split)
    - [port-unsplit](devlink.md#port-unsplit)
    - [sb-get](devlink.md#sb-get)
    - [sb-pool-get](devlink.md#sb-pool-get)
    - [sb-pool-set](devlink.md#sb-pool-set)
    - [sb-port-pool-get](devlink.md#sb-port-pool-get)
    - [sb-port-pool-set](devlink.md#sb-port-pool-set)
    - [sb-tc-pool-bind-get](devlink.md#sb-tc-pool-bind-get)
    - [sb-tc-pool-bind-set](devlink.md#sb-tc-pool-bind-set)
    - [sb-occ-snapshot](devlink.md#sb-occ-snapshot)
    - [sb-occ-max-clear](devlink.md#sb-occ-max-clear)
    - [eswitch-get](devlink.md#eswitch-get)
    - [eswitch-set](devlink.md#eswitch-set)
    - [dpipe-table-get](devlink.md#dpipe-table-get)
    - [dpipe-entries-get](devlink.md#dpipe-entries-get)
    - [dpipe-headers-get](devlink.md#dpipe-headers-get)
    - [dpipe-table-counters-set](devlink.md#dpipe-table-counters-set)
    - [resource-set](devlink.md#resource-set)
    - [resource-dump](devlink.md#resource-dump)
    - [reload](devlink.md#reload)
    - [param-get](devlink.md#param-get)
    - [param-set](devlink.md#param-set)
    - [region-get](devlink.md#region-get)
    - [region-new](devlink.md#region-new)
    - [region-del](devlink.md#region-del)
    - [region-read](devlink.md#region-read)
    - [port-param-get](devlink.md#port-param-get)
    - [port-param-set](devlink.md#port-param-set)
    - [info-get](devlink.md#info-get)
    - [health-reporter-get](devlink.md#health-reporter-get)
    - [health-reporter-set](devlink.md#health-reporter-set)
    - [health-reporter-recover](devlink.md#health-reporter-recover)
    - [health-reporter-diagnose](devlink.md#health-reporter-diagnose)
    - [health-reporter-dump-get](devlink.md#health-reporter-dump-get)
    - [health-reporter-dump-clear](devlink.md#health-reporter-dump-clear)
    - [flash-update](devlink.md#flash-update)
    - [trap-get](devlink.md#trap-get)
    - [trap-set](devlink.md#trap-set)
    - [trap-group-get](devlink.md#trap-group-get)
    - [trap-group-set](devlink.md#trap-group-set)
    - [trap-policer-get](devlink.md#trap-policer-get)
    - [trap-policer-set](devlink.md#trap-policer-set)
    - [health-reporter-test](devlink.md#health-reporter-test)
    - [rate-get](devlink.md#rate-get)
    - [rate-set](devlink.md#rate-set)
    - [rate-new](devlink.md#rate-new)
    - [rate-del](devlink.md#rate-del)
    - [linecard-get](devlink.md#linecard-get)
    - [linecard-set](devlink.md#linecard-set)
    - [selftests-get](devlink.md#selftests-get)
    - [selftests-run](devlink.md#selftests-run)
    - [notify-filter-set](devlink.md#notify-filter-set)
  - [Definitions](devlink.md#definitions)

    - [sb-pool-type](devlink.md#sb-pool-type)
    - [port-type](devlink.md#port-type)
    - [port-flavour](devlink.md#port-flavour)
    - [port-fn-state](devlink.md#port-fn-state)
    - [port-fn-opstate](devlink.md#port-fn-opstate)
    - [port-fn-attr-cap](devlink.md#port-fn-attr-cap)
    - [rate-type](devlink.md#rate-type)
    - [sb-threshold-type](devlink.md#sb-threshold-type)
    - [eswitch-mode](devlink.md#eswitch-mode)
    - [eswitch-inline-mode](devlink.md#eswitch-inline-mode)
    - [eswitch-encap-mode](devlink.md#eswitch-encap-mode)
    - [dpipe-header-id](devlink.md#dpipe-header-id)
    - [dpipe-match-type](devlink.md#dpipe-match-type)
    - [dpipe-action-type](devlink.md#dpipe-action-type)
    - [dpipe-field-mapping-type](devlink.md#dpipe-field-mapping-type)
    - [resource-unit](devlink.md#resource-unit)
    - [reload-action](devlink.md#reload-action)
    - [param-cmode](devlink.md#param-cmode)
    - [flash-overwrite](devlink.md#flash-overwrite)
    - [trap-action](devlink.md#trap-action)
    - [trap-type](devlink.md#trap-type)
    - [var-attr-type](devlink.md#var-attr-type)
    - [rate-tc-index-max](devlink.md#rate-tc-index-max)
  - [Attribute sets](devlink.md#attribute-sets)

    - [devlink](devlink.md#devlink)
    - [dl-dev-stats](devlink.md#dl-dev-stats)
    - [dl-reload-stats](devlink.md#dl-reload-stats)
    - [dl-reload-act-info](devlink.md#dl-reload-act-info)
    - [dl-reload-act-stats](devlink.md#dl-reload-act-stats)
    - [dl-reload-stats-entry](devlink.md#dl-reload-stats-entry)
    - [dl-info-version](devlink.md#dl-info-version)
    - [dl-port-function](devlink.md#dl-port-function)
    - [dl-dpipe-tables](devlink.md#dl-dpipe-tables)
    - [dl-dpipe-table](devlink.md#dl-dpipe-table)
    - [dl-dpipe-table-matches](devlink.md#dl-dpipe-table-matches)
    - [dl-dpipe-table-actions](devlink.md#dl-dpipe-table-actions)
    - [dl-dpipe-entries](devlink.md#dl-dpipe-entries)
    - [dl-dpipe-entry](devlink.md#dl-dpipe-entry)
    - [dl-dpipe-entry-match-values](devlink.md#dl-dpipe-entry-match-values)
    - [dl-dpipe-entry-action-values](devlink.md#dl-dpipe-entry-action-values)
    - [dl-dpipe-match](devlink.md#dl-dpipe-match)
    - [dl-dpipe-match-value](devlink.md#dl-dpipe-match-value)
    - [dl-dpipe-action](devlink.md#dl-dpipe-action)
    - [dl-dpipe-action-value](devlink.md#dl-dpipe-action-value)
    - [dl-dpipe-headers](devlink.md#dl-dpipe-headers)
    - [dl-dpipe-header](devlink.md#dl-dpipe-header)
    - [dl-dpipe-header-fields](devlink.md#dl-dpipe-header-fields)
    - [dl-dpipe-field](devlink.md#dl-dpipe-field)
    - [dl-resource](devlink.md#dl-resource)
    - [dl-resource-list](devlink.md#dl-resource-list)
    - [dl-param](devlink.md#dl-param)
    - [dl-region-snapshots](devlink.md#dl-region-snapshots)
    - [dl-region-snapshot](devlink.md#dl-region-snapshot)
    - [dl-region-chunks](devlink.md#dl-region-chunks)
    - [dl-region-chunk](devlink.md#dl-region-chunk)
    - [dl-fmsg](devlink.md#dl-fmsg)
    - [dl-health-reporter](devlink.md#dl-health-reporter)
    - [dl-attr-stats](devlink.md#dl-attr-stats)
    - [dl-trap-metadata](devlink.md#dl-trap-metadata)
    - [dl-linecard-supported-types](devlink.md#dl-linecard-supported-types)
    - [dl-selftest-id](devlink.md#dl-selftest-id)
    - [dl-rate-tc-bws](devlink.md#dl-rate-tc-bws)

## [Summary](devlink.md#id22)

Partial family for Devlink.

## [Operations](devlink.md#id23)

### [get](devlink.md#id24)

Get devlink instances.

attribute-set:
:   [devlink](devlink.md#devlink-attribute-set-devlink)

dont-validate:
:   [‘strict’, ‘dump’]

do:
:   **pre**
    :   devlink-nl-pre-doit

    **post**
    :   devlink-nl-post-doit

    **request**
    :   attributes:
        :   [`bus-name`, `dev-name`]

    **reply**
    :   attributes:
        :   [`bus-name`, `dev-name`, `reload-failed`, `dev-stats`]

dump:
:   **reply**
    :   attributes:
        :   [`bus-name`, `dev-name`, `reload-failed`, `dev-stats`]

### [port-get](devlink.md#id25)

Get devlink port instances.

attribute-set:
:   [devlink](devlink.md#devlink-attribute-set-devlink)

dont-validate:
:   [‘strict’]

do:
:   **pre**
    :   devlink-nl-pre-doit-port

    **post**
    :   devlink-nl-post-doit

    **request**
    :   attributes:
        :   [`bus-name`, `dev-name`, `port-index`]

    **reply**
    :   attributes:
        :   [`bus-name`, `dev-name`, `port-index`]

dump:
:   **request**
    :   attributes:
        :   [`bus-name`, `dev-name`]

    **reply**
    :   attributes:
        :   [`bus-name`, `dev-name`, `port-index`]

### [port-set](devlink.md#id26)

Set devlink port instances.

attribute-set:
:   [devlink](devlink.md#devlink-attribute-set-devlink)

dont-validate:
:   [‘strict’]

flags:
:   [`admin-perm`]

do:
:   **pre**
    :   devlink-nl-pre-doit-port

    **post**
    :   devlink-nl-post-doit

    **request**
    :   attributes:
        :   [`bus-name`, `dev-name`, `port-index`, `port-type`, `port-function`]

### [port-new](devlink.md#id27)

Create devlink port instances.

attribute-set:
:   [devlink](devlink.md#devlink-attribute-set-devlink)

dont-validate:
:   [‘strict’]

flags:
:   [`admin-perm`]

do:
:   **pre**
    :   devlink-nl-pre-doit

    **post**
    :   devlink-nl-post-doit

    **request**
    :   attributes:
        :   [`bus-name`, `dev-name`, `port-index`, `port-flavour`, `port-pci-pf-number`, `port-pci-sf-number`, `port-controller-number`]

    **reply**
    :   attributes:
        :   [`bus-name`, `dev-name`, `port-index`]

### [port-del](devlink.md#id28)

Delete devlink port instances.

attribute-set:
:   [devlink](devlink.md#devlink-attribute-set-devlink)

dont-validate:
:   [‘strict’]

flags:
:   [`admin-perm`]

do:
:   **pre**
    :   devlink-nl-pre-doit-port

    **post**
    :   devlink-nl-post-doit

    **request**
    :   attributes:
        :   [`bus-name`, `dev-name`, `port-index`]

### [port-split](devlink.md#id29)

Split devlink port instances.

attribute-set:
:   [devlink](devlink.md#devlink-attribute-set-devlink)

dont-validate:
:   [‘strict’]

flags:
:   [`admin-perm`]

do:
:   **pre**
    :   devlink-nl-pre-doit-port

    **post**
    :   devlink-nl-post-doit

    **request**
    :   attributes:
        :   [`bus-name`, `dev-name`, `port-index`, `port-split-count`]

### [port-unsplit](devlink.md#id30)

Unplit devlink port instances.

attribute-set:
:   [devlink](devlink.md#devlink-attribute-set-devlink)

dont-validate:
:   [‘strict’]

flags:
:   [`admin-perm`]

do:
:   **pre**
    :   devlink-nl-pre-doit-port

    **post**
    :   devlink-nl-post-doit

    **request**
    :   attributes:
        :   [`bus-name`, `dev-name`, `port-index`]

### [sb-get](devlink.md#id31)

Get shared buffer instances.

attribute-set:
:   [devlink](devlink.md#devlink-attribute-set-devlink)

dont-validate:
:   [‘strict’]

do:
:   **pre**
    :   devlink-nl-pre-doit

    **post**
    :   devlink-nl-post-doit

    **request**
    :   attributes:
        :   [`bus-name`, `dev-name`, `sb-index`]

    **reply**
    :   attributes:
        :   [`bus-name`, `dev-name`, `sb-index`]

dump:
:   **request**
    :   attributes:
        :   [`bus-name`, `dev-name`]

    **reply**
    :   attributes:
        :   [`bus-name`, `dev-name`, `sb-index`]

### [sb-pool-get](devlink.md#id32)

Get shared buffer pool instances.

attribute-set:
:   [devlink](devlink.md#devlink-attribute-set-devlink)

dont-validate:
:   [‘strict’]

do:
:   **pre**
    :   devlink-nl-pre-doit

    **post**
    :   devlink-nl-post-doit

    **request**
    :   attributes:
        :   [`bus-name`, `dev-name`, `sb-index`, `sb-pool-index`]

    **reply**
    :   attributes:
        :   [`bus-name`, `dev-name`, `sb-index`, `sb-pool-index`]

dump:
:   **request**
    :   attributes:
        :   [`bus-name`, `dev-name`]

    **reply**
    :   attributes:
        :   [`bus-name`, `dev-name`, `sb-index`, `sb-pool-index`]

### [sb-pool-set](devlink.md#id33)

Set shared buffer pool instances.

attribute-set:
:   [devlink](devlink.md#devlink-attribute-set-devlink)

dont-validate:
:   [‘strict’]

flags:
:   [`admin-perm`]

do:
:   **pre**
    :   devlink-nl-pre-doit

    **post**
    :   devlink-nl-post-doit

    **request**
    :   attributes:
        :   [`bus-name`, `dev-name`, `sb-index`, `sb-pool-index`, `sb-pool-threshold-type`, `sb-pool-size`]

### [sb-port-pool-get](devlink.md#id34)

Get shared buffer port-pool combinations and threshold.

attribute-set:
:   [devlink](devlink.md#devlink-attribute-set-devlink)

dont-validate:
:   [‘strict’]

do:
:   **pre**
    :   devlink-nl-pre-doit-port

    **post**
    :   devlink-nl-post-doit

    **request**
    :   attributes:
        :   [`bus-name`, `dev-name`, `port-index`, `sb-index`, `sb-pool-index`]

    **reply**
    :   attributes:
        :   [`bus-name`, `dev-name`, `port-index`, `sb-index`, `sb-pool-index`]

dump:
:   **request**
    :   attributes:
        :   [`bus-name`, `dev-name`]

    **reply**
    :   attributes:
        :   [`bus-name`, `dev-name`, `port-index`, `sb-index`, `sb-pool-index`]

### [sb-port-pool-set](devlink.md#id35)

Set shared buffer port-pool combinations and threshold.

attribute-set:
:   [devlink](devlink.md#devlink-attribute-set-devlink)

dont-validate:
:   [‘strict’]

flags:
:   [`admin-perm`]

do:
:   **pre**
    :   devlink-nl-pre-doit-port

    **post**
    :   devlink-nl-post-doit

    **request**
    :   attributes:
        :   [`bus-name`, `dev-name`, `port-index`, `sb-index`, `sb-pool-index`, `sb-threshold`]

### [sb-tc-pool-bind-get](devlink.md#id36)

Get shared buffer port-TC to pool bindings and threshold.

attribute-set:
:   [devlink](devlink.md#devlink-attribute-set-devlink)

dont-validate:
:   [‘strict’]

do:
:   **pre**
    :   devlink-nl-pre-doit-port

    **post**
    :   devlink-nl-post-doit

    **request**
    :   attributes:
        :   [`bus-name`, `dev-name`, `port-index`, `sb-index`, `sb-pool-type`, `sb-tc-index`]

    **reply**
    :   attributes:
        :   [`bus-name`, `dev-name`, `port-index`, `sb-index`, `sb-pool-type`, `sb-tc-index`]

dump:
:   **request**
    :   attributes:
        :   [`bus-name`, `dev-name`]

    **reply**
    :   attributes:
        :   [`bus-name`, `dev-name`, `port-index`, `sb-index`, `sb-pool-type`, `sb-tc-index`]

### [sb-tc-pool-bind-set](devlink.md#id37)

Set shared buffer port-TC to pool bindings and threshold.

attribute-set:
:   [devlink](devlink.md#devlink-attribute-set-devlink)

dont-validate:
:   [‘strict’]

flags:
:   [`admin-perm`]

do:
:   **pre**
    :   devlink-nl-pre-doit-port

    **post**
    :   devlink-nl-post-doit

    **request**
    :   attributes:
        :   [`bus-name`, `dev-name`, `port-index`, `sb-index`, `sb-pool-index`, `sb-pool-type`, `sb-tc-index`, `sb-threshold`]

### [sb-occ-snapshot](devlink.md#id38)

Take occupancy snapshot of shared buffer.

attribute-set:
:   [devlink](devlink.md#devlink-attribute-set-devlink)

dont-validate:
:   [‘strict’]

flags:
:   [`admin-perm`]

do:
:   **pre**
    :   devlink-nl-pre-doit

    **post**
    :   devlink-nl-post-doit

    **request**
    :   attributes:
        :   [`bus-name`, `dev-name`, `sb-index`]

### [sb-occ-max-clear](devlink.md#id39)

Clear occupancy watermarks of shared buffer.

attribute-set:
:   [devlink](devlink.md#devlink-attribute-set-devlink)

dont-validate:
:   [‘strict’]

flags:
:   [`admin-perm`]

do:
:   **pre**
    :   devlink-nl-pre-doit

    **post**
    :   devlink-nl-post-doit

    **request**
    :   attributes:
        :   [`bus-name`, `dev-name`, `sb-index`]

### [eswitch-get](devlink.md#id40)

Get eswitch attributes.

attribute-set:
:   [devlink](devlink.md#devlink-attribute-set-devlink)

dont-validate:
:   [‘strict’]

flags:
:   [`admin-perm`]

do:
:   **pre**
    :   devlink-nl-pre-doit

    **post**
    :   devlink-nl-post-doit

    **request**
    :   attributes:
        :   [`bus-name`, `dev-name`]

    **reply**
    :   attributes:
        :   [`bus-name`, `dev-name`, `eswitch-mode`, `eswitch-inline-mode`, `eswitch-encap-mode`]

### [eswitch-set](devlink.md#id41)

Set eswitch attributes.

attribute-set:
:   [devlink](devlink.md#devlink-attribute-set-devlink)

dont-validate:
:   [‘strict’]

flags:
:   [`admin-perm`]

do:
:   **pre**
    :   devlink-nl-pre-doit

    **post**
    :   devlink-nl-post-doit

    **request**
    :   attributes:
        :   [`bus-name`, `dev-name`, `eswitch-mode`, `eswitch-inline-mode`, `eswitch-encap-mode`]

### [dpipe-table-get](devlink.md#id42)

Get dpipe table attributes.

attribute-set:
:   [devlink](devlink.md#devlink-attribute-set-devlink)

dont-validate:
:   [‘strict’]

do:
:   **pre**
    :   devlink-nl-pre-doit

    **post**
    :   devlink-nl-post-doit

    **request**
    :   attributes:
        :   [`bus-name`, `dev-name`, `dpipe-table-name`]

    **reply**
    :   attributes:
        :   [`bus-name`, `dev-name`, `dpipe-tables`]

### [dpipe-entries-get](devlink.md#id43)

Get dpipe entries attributes.

attribute-set:
:   [devlink](devlink.md#devlink-attribute-set-devlink)

dont-validate:
:   [‘strict’]

do:
:   **pre**
    :   devlink-nl-pre-doit

    **post**
    :   devlink-nl-post-doit

    **request**
    :   attributes:
        :   [`bus-name`, `dev-name`, `dpipe-table-name`]

    **reply**
    :   attributes:
        :   [`bus-name`, `dev-name`, `dpipe-entries`]

### [dpipe-headers-get](devlink.md#id44)

Get dpipe headers attributes.

attribute-set:
:   [devlink](devlink.md#devlink-attribute-set-devlink)

dont-validate:
:   [‘strict’]

do:
:   **pre**
    :   devlink-nl-pre-doit

    **post**
    :   devlink-nl-post-doit

    **request**
    :   attributes:
        :   [`bus-name`, `dev-name`]

    **reply**
    :   attributes:
        :   [`bus-name`, `dev-name`, `dpipe-headers`]

### [dpipe-table-counters-set](devlink.md#id45)

Set dpipe counter attributes.

attribute-set:
:   [devlink](devlink.md#devlink-attribute-set-devlink)

dont-validate:
:   [‘strict’]

flags:
:   [`admin-perm`]

do:
:   **pre**
    :   devlink-nl-pre-doit

    **post**
    :   devlink-nl-post-doit

    **request**
    :   attributes:
        :   [`bus-name`, `dev-name`, `dpipe-table-name`, `dpipe-table-counters-enabled`]

### [resource-set](devlink.md#id46)

Set resource attributes.

attribute-set:
:   [devlink](devlink.md#devlink-attribute-set-devlink)

dont-validate:
:   [‘strict’]

flags:
:   [`admin-perm`]

do:
:   **pre**
    :   devlink-nl-pre-doit

    **post**
    :   devlink-nl-post-doit

    **request**
    :   attributes:
        :   [`bus-name`, `dev-name`, `resource-id`, `resource-size`]

### [resource-dump](devlink.md#id47)

Get resource attributes.

attribute-set:
:   [devlink](devlink.md#devlink-attribute-set-devlink)

dont-validate:
:   [‘strict’]

do:
:   **pre**
    :   devlink-nl-pre-doit

    **post**
    :   devlink-nl-post-doit

    **request**
    :   attributes:
        :   [`bus-name`, `dev-name`]

    **reply**
    :   attributes:
        :   [`bus-name`, `dev-name`, `resource-list`]

### [reload](devlink.md#id48)

Reload devlink.

attribute-set:
:   [devlink](devlink.md#devlink-attribute-set-devlink)

dont-validate:
:   [‘strict’]

flags:
:   [`admin-perm`]

do:
:   **pre**
    :   devlink-nl-pre-doit-dev-lock

    **post**
    :   devlink-nl-post-doit-dev-lock

    **request**
    :   attributes:
        :   [`bus-name`, `dev-name`, `reload-action`, `reload-limits`, `netns-pid`, `netns-fd`, `netns-id`]

    **reply**
    :   attributes:
        :   [`bus-name`, `dev-name`, `reload-actions-performed`]

### [param-get](devlink.md#id49)

Get param instances.

attribute-set:
:   [devlink](devlink.md#devlink-attribute-set-devlink)

dont-validate:
:   [‘strict’]

do:
:   **pre**
    :   devlink-nl-pre-doit

    **post**
    :   devlink-nl-post-doit

    **request**
    :   attributes:
        :   [`bus-name`, `dev-name`, `param-name`]

    **reply**
    :   attributes:
        :   [`bus-name`, `dev-name`, `param-name`]

dump:
:   **request**
    :   attributes:
        :   [`bus-name`, `dev-name`]

    **reply**
    :   attributes:
        :   [`bus-name`, `dev-name`, `param-name`]

### [param-set](devlink.md#id50)

Set param instances.

attribute-set:
:   [devlink](devlink.md#devlink-attribute-set-devlink)

dont-validate:
:   [‘strict’]

flags:
:   [`admin-perm`]

do:
:   **pre**
    :   devlink-nl-pre-doit

    **post**
    :   devlink-nl-post-doit

    **request**
    :   attributes:
        :   [`bus-name`, `dev-name`, `param-name`, `param-type`, `param-value-cmode`]

### [region-get](devlink.md#id51)

Get region instances.

attribute-set:
:   [devlink](devlink.md#devlink-attribute-set-devlink)

dont-validate:
:   [‘strict’]

do:
:   **pre**
    :   devlink-nl-pre-doit-port-optional

    **post**
    :   devlink-nl-post-doit

    **request**
    :   attributes:
        :   [`bus-name`, `dev-name`, `port-index`, `region-name`]

    **reply**
    :   attributes:
        :   [`bus-name`, `dev-name`, `port-index`, `region-name`]

dump:
:   **request**
    :   attributes:
        :   [`bus-name`, `dev-name`]

    **reply**
    :   attributes:
        :   [`bus-name`, `dev-name`, `port-index`, `region-name`]

### [region-new](devlink.md#id52)

Create region snapshot.

attribute-set:
:   [devlink](devlink.md#devlink-attribute-set-devlink)

dont-validate:
:   [‘strict’]

flags:
:   [`admin-perm`]

do:
:   **pre**
    :   devlink-nl-pre-doit-port-optional

    **post**
    :   devlink-nl-post-doit

    **request**
    :   attributes:
        :   [`bus-name`, `dev-name`, `port-index`, `region-name`, `region-snapshot-id`]

    **reply**
    :   attributes:
        :   [`bus-name`, `dev-name`, `port-index`, `region-name`, `region-snapshot-id`]

### [region-del](devlink.md#id53)

Delete region snapshot.

attribute-set:
:   [devlink](devlink.md#devlink-attribute-set-devlink)

dont-validate:
:   [‘strict’]

flags:
:   [`admin-perm`]

do:
:   **pre**
    :   devlink-nl-pre-doit-port-optional

    **post**
    :   devlink-nl-post-doit

    **request**
    :   attributes:
        :   [`bus-name`, `dev-name`, `port-index`, `region-name`, `region-snapshot-id`]

### [region-read](devlink.md#id54)

Read region data.

attribute-set:
:   [devlink](devlink.md#devlink-attribute-set-devlink)

dont-validate:
:   [‘dump-strict’]

flags:
:   [`admin-perm`]

dump:
:   **request**
    :   attributes:
        :   [`bus-name`, `dev-name`, `port-index`, `region-name`, `region-snapshot-id`, `region-direct`, `region-chunk-addr`, `region-chunk-len`]

    **reply**
    :   attributes:
        :   [`bus-name`, `dev-name`, `port-index`, `region-name`]

### [port-param-get](devlink.md#id55)

Get port param instances.

attribute-set:
:   [devlink](devlink.md#devlink-attribute-set-devlink)

dont-validate:
:   [‘strict’, ‘dump-strict’]

do:
:   **pre**
    :   devlink-nl-pre-doit-port

    **post**
    :   devlink-nl-post-doit

    **request**
    :   attributes:
        :   [`bus-name`, `dev-name`, `port-index`]

    **reply**
    :   attributes:
        :   [`bus-name`, `dev-name`, `port-index`]

dump:
:   **reply**
    :   attributes:
        :   [`bus-name`, `dev-name`, `port-index`]

### [port-param-set](devlink.md#id56)

Set port param instances.

attribute-set:
:   [devlink](devlink.md#devlink-attribute-set-devlink)

dont-validate:
:   [‘strict’]

flags:
:   [`admin-perm`]

do:
:   **pre**
    :   devlink-nl-pre-doit-port

    **post**
    :   devlink-nl-post-doit

    **request**
    :   attributes:
        :   [`bus-name`, `dev-name`, `port-index`]

### [info-get](devlink.md#id57)

Get device information, like driver name, hardware and firmware versions
etc.

attribute-set:
:   [devlink](devlink.md#devlink-attribute-set-devlink)

dont-validate:
:   [‘strict’, ‘dump’]

do:
:   **pre**
    :   devlink-nl-pre-doit

    **post**
    :   devlink-nl-post-doit

    **request**
    :   attributes:
        :   [`bus-name`, `dev-name`]

    **reply**
    :   attributes:
        :   [`bus-name`, `dev-name`, `info-driver-name`, `info-serial-number`, `info-version-fixed`, `info-version-running`, `info-version-stored`, `info-board-serial-number`]

dump:
:   **reply**
    :   attributes:
        :   [`bus-name`, `dev-name`, `info-driver-name`, `info-serial-number`, `info-version-fixed`, `info-version-running`, `info-version-stored`, `info-board-serial-number`]

### [health-reporter-get](devlink.md#id58)

Get health reporter instances.

attribute-set:
:   [devlink](devlink.md#devlink-attribute-set-devlink)

dont-validate:
:   [‘strict’]

do:
:   **pre**
    :   devlink-nl-pre-doit-port-optional

    **post**
    :   devlink-nl-post-doit

    **request**
    :   attributes:
        :   [`bus-name`, `dev-name`, `port-index`, `health-reporter-name`]

    **reply**
    :   attributes:
        :   [`bus-name`, `dev-name`, `port-index`, `health-reporter-name`]

dump:
:   **request**
    :   attributes:
        :   [`bus-name`, `dev-name`, `port-index`]

    **reply**
    :   attributes:
        :   [`bus-name`, `dev-name`, `port-index`, `health-reporter-name`]

### [health-reporter-set](devlink.md#id59)

Set health reporter instances.

attribute-set:
:   [devlink](devlink.md#devlink-attribute-set-devlink)

dont-validate:
:   [‘strict’]

flags:
:   [`admin-perm`]

do:
:   **pre**
    :   devlink-nl-pre-doit-port-optional

    **post**
    :   devlink-nl-post-doit

    **request**
    :   attributes:
        :   [`bus-name`, `dev-name`, `port-index`, `health-reporter-name`, `health-reporter-graceful-period`, `health-reporter-auto-recover`, `health-reporter-auto-dump`]

### [health-reporter-recover](devlink.md#id60)

Recover health reporter instances.

attribute-set:
:   [devlink](devlink.md#devlink-attribute-set-devlink)

dont-validate:
:   [‘strict’]

flags:
:   [`admin-perm`]

do:
:   **pre**
    :   devlink-nl-pre-doit-port-optional

    **post**
    :   devlink-nl-post-doit

    **request**
    :   attributes:
        :   [`bus-name`, `dev-name`, `port-index`, `health-reporter-name`]

### [health-reporter-diagnose](devlink.md#id61)

Diagnose health reporter instances.

attribute-set:
:   [devlink](devlink.md#devlink-attribute-set-devlink)

dont-validate:
:   [‘strict’]

flags:
:   [`admin-perm`]

do:
:   **pre**
    :   devlink-nl-pre-doit-port-optional

    **post**
    :   devlink-nl-post-doit

    **request**
    :   attributes:
        :   [`bus-name`, `dev-name`, `port-index`, `health-reporter-name`]

### [health-reporter-dump-get](devlink.md#id62)

Dump health reporter instances.

attribute-set:
:   [devlink](devlink.md#devlink-attribute-set-devlink)

dont-validate:
:   [‘dump-strict’]

flags:
:   [`admin-perm`]

dump:
:   **request**
    :   attributes:
        :   [`bus-name`, `dev-name`, `port-index`, `health-reporter-name`]

    **reply**
    :   attributes:
        :   [`fmsg`]

### [health-reporter-dump-clear](devlink.md#id63)

Clear dump of health reporter instances.

attribute-set:
:   [devlink](devlink.md#devlink-attribute-set-devlink)

dont-validate:
:   [‘strict’]

flags:
:   [`admin-perm`]

do:
:   **pre**
    :   devlink-nl-pre-doit-port-optional

    **post**
    :   devlink-nl-post-doit

    **request**
    :   attributes:
        :   [`bus-name`, `dev-name`, `port-index`, `health-reporter-name`]

### [flash-update](devlink.md#id64)

Flash update devlink instances.

attribute-set:
:   [devlink](devlink.md#devlink-attribute-set-devlink)

dont-validate:
:   [‘strict’]

flags:
:   [`admin-perm`]

do:
:   **pre**
    :   devlink-nl-pre-doit

    **post**
    :   devlink-nl-post-doit

    **request**
    :   attributes:
        :   [`bus-name`, `dev-name`, `flash-update-file-name`, `flash-update-component`, `flash-update-overwrite-mask`]

### [trap-get](devlink.md#id65)

Get trap instances.

attribute-set:
:   [devlink](devlink.md#devlink-attribute-set-devlink)

dont-validate:
:   [‘strict’]

do:
:   **pre**
    :   devlink-nl-pre-doit

    **post**
    :   devlink-nl-post-doit

    **request**
    :   attributes:
        :   [`bus-name`, `dev-name`, `trap-name`]

    **reply**
    :   attributes:
        :   [`bus-name`, `dev-name`, `trap-name`]

dump:
:   **request**
    :   attributes:
        :   [`bus-name`, `dev-name`]

    **reply**
    :   attributes:
        :   [`bus-name`, `dev-name`, `trap-name`]

### [trap-set](devlink.md#id66)

Set trap instances.

attribute-set:
:   [devlink](devlink.md#devlink-attribute-set-devlink)

dont-validate:
:   [‘strict’]

flags:
:   [`admin-perm`]

do:
:   **pre**
    :   devlink-nl-pre-doit

    **post**
    :   devlink-nl-post-doit

    **request**
    :   attributes:
        :   [`bus-name`, `dev-name`, `trap-name`, `trap-action`]

### [trap-group-get](devlink.md#id67)

Get trap group instances.

attribute-set:
:   [devlink](devlink.md#devlink-attribute-set-devlink)

dont-validate:
:   [‘strict’]

do:
:   **pre**
    :   devlink-nl-pre-doit

    **post**
    :   devlink-nl-post-doit

    **request**
    :   attributes:
        :   [`bus-name`, `dev-name`, `trap-group-name`]

    **reply**
    :   attributes:
        :   [`bus-name`, `dev-name`, `trap-group-name`]

dump:
:   **request**
    :   attributes:
        :   [`bus-name`, `dev-name`]

    **reply**
    :   attributes:
        :   [`bus-name`, `dev-name`, `trap-group-name`]

### [trap-group-set](devlink.md#id68)

Set trap group instances.

attribute-set:
:   [devlink](devlink.md#devlink-attribute-set-devlink)

dont-validate:
:   [‘strict’]

flags:
:   [`admin-perm`]

do:
:   **pre**
    :   devlink-nl-pre-doit

    **post**
    :   devlink-nl-post-doit

    **request**
    :   attributes:
        :   [`bus-name`, `dev-name`, `trap-group-name`, `trap-action`, `trap-policer-id`]

### [trap-policer-get](devlink.md#id69)

Get trap policer instances.

attribute-set:
:   [devlink](devlink.md#devlink-attribute-set-devlink)

dont-validate:
:   [‘strict’]

do:
:   **pre**
    :   devlink-nl-pre-doit

    **post**
    :   devlink-nl-post-doit

    **request**
    :   attributes:
        :   [`bus-name`, `dev-name`, `trap-policer-id`]

    **reply**
    :   attributes:
        :   [`bus-name`, `dev-name`, `trap-policer-id`]

dump:
:   **request**
    :   attributes:
        :   [`bus-name`, `dev-name`]

    **reply**
    :   attributes:
        :   [`bus-name`, `dev-name`, `trap-policer-id`]

### [trap-policer-set](devlink.md#id70)

Get trap policer instances.

attribute-set:
:   [devlink](devlink.md#devlink-attribute-set-devlink)

dont-validate:
:   [‘strict’]

flags:
:   [`admin-perm`]

do:
:   **pre**
    :   devlink-nl-pre-doit

    **post**
    :   devlink-nl-post-doit

    **request**
    :   attributes:
        :   [`bus-name`, `dev-name`, `trap-policer-id`, `trap-policer-rate`, `trap-policer-burst`]

### [health-reporter-test](devlink.md#id71)

Test health reporter instances.

attribute-set:
:   [devlink](devlink.md#devlink-attribute-set-devlink)

dont-validate:
:   [‘strict’]

flags:
:   [`admin-perm`]

do:
:   **pre**
    :   devlink-nl-pre-doit-port-optional

    **post**
    :   devlink-nl-post-doit

    **request**
    :   attributes:
        :   [`bus-name`, `dev-name`, `port-index`, `health-reporter-name`]

### [rate-get](devlink.md#id72)

Get rate instances.

attribute-set:
:   [devlink](devlink.md#devlink-attribute-set-devlink)

dont-validate:
:   [‘strict’]

do:
:   **pre**
    :   devlink-nl-pre-doit

    **post**
    :   devlink-nl-post-doit

    **request**
    :   attributes:
        :   [`bus-name`, `dev-name`, `port-index`, `rate-node-name`]

    **reply**
    :   attributes:
        :   [`bus-name`, `dev-name`, `port-index`, `rate-node-name`]

dump:
:   **request**
    :   attributes:
        :   [`bus-name`, `dev-name`]

    **reply**
    :   attributes:
        :   [`bus-name`, `dev-name`, `port-index`, `rate-node-name`]

### [rate-set](devlink.md#id73)

Set rate instances.

attribute-set:
:   [devlink](devlink.md#devlink-attribute-set-devlink)

dont-validate:
:   [‘strict’]

flags:
:   [`admin-perm`]

do:
:   **pre**
    :   devlink-nl-pre-doit

    **post**
    :   devlink-nl-post-doit

    **request**
    :   attributes:
        :   [`bus-name`, `dev-name`, `rate-node-name`, `rate-tx-share`, `rate-tx-max`, `rate-tx-priority`, `rate-tx-weight`, `rate-parent-node-name`, `rate-tc-bws`]

### [rate-new](devlink.md#id74)

Create rate instances.

attribute-set:
:   [devlink](devlink.md#devlink-attribute-set-devlink)

dont-validate:
:   [‘strict’]

flags:
:   [`admin-perm`]

do:
:   **pre**
    :   devlink-nl-pre-doit

    **post**
    :   devlink-nl-post-doit

    **request**
    :   attributes:
        :   [`bus-name`, `dev-name`, `rate-node-name`, `rate-tx-share`, `rate-tx-max`, `rate-tx-priority`, `rate-tx-weight`, `rate-parent-node-name`, `rate-tc-bws`]

### [rate-del](devlink.md#id75)

Delete rate instances.

attribute-set:
:   [devlink](devlink.md#devlink-attribute-set-devlink)

dont-validate:
:   [‘strict’]

flags:
:   [`admin-perm`]

do:
:   **pre**
    :   devlink-nl-pre-doit

    **post**
    :   devlink-nl-post-doit

    **request**
    :   attributes:
        :   [`bus-name`, `dev-name`, `rate-node-name`]

### [linecard-get](devlink.md#id76)

Get line card instances.

attribute-set:
:   [devlink](devlink.md#devlink-attribute-set-devlink)

dont-validate:
:   [‘strict’]

do:
:   **pre**
    :   devlink-nl-pre-doit

    **post**
    :   devlink-nl-post-doit

    **request**
    :   attributes:
        :   [`bus-name`, `dev-name`, `linecard-index`]

    **reply**
    :   attributes:
        :   [`bus-name`, `dev-name`, `linecard-index`]

dump:
:   **request**
    :   attributes:
        :   [`bus-name`, `dev-name`]

    **reply**
    :   attributes:
        :   [`bus-name`, `dev-name`, `linecard-index`]

### [linecard-set](devlink.md#id77)

Set line card instances.

attribute-set:
:   [devlink](devlink.md#devlink-attribute-set-devlink)

dont-validate:
:   [‘strict’]

flags:
:   [`admin-perm`]

do:
:   **pre**
    :   devlink-nl-pre-doit

    **post**
    :   devlink-nl-post-doit

    **request**
    :   attributes:
        :   [`bus-name`, `dev-name`, `linecard-index`, `linecard-type`]

### [selftests-get](devlink.md#id78)

Get device selftest instances.

attribute-set:
:   [devlink](devlink.md#devlink-attribute-set-devlink)

dont-validate:
:   [‘strict’, ‘dump’]

do:
:   **pre**
    :   devlink-nl-pre-doit

    **post**
    :   devlink-nl-post-doit

    **request**
    :   attributes:
        :   [`bus-name`, `dev-name`]

    **reply**
    :   attributes:
        :   [`bus-name`, `dev-name`]

dump:
:   **reply**
    :   attributes:
        :   [`bus-name`, `dev-name`]

### [selftests-run](devlink.md#id79)

Run device selftest instances.

attribute-set:
:   [devlink](devlink.md#devlink-attribute-set-devlink)

dont-validate:
:   [‘strict’]

flags:
:   [`admin-perm`]

do:
:   **pre**
    :   devlink-nl-pre-doit

    **post**
    :   devlink-nl-post-doit

    **request**
    :   attributes:
        :   [`bus-name`, `dev-name`, `selftests`]

### [notify-filter-set](devlink.md#id80)

Set notification messages socket filter.

attribute-set:
:   [devlink](devlink.md#devlink-attribute-set-devlink)

do:
:   **request**
    :   attributes:
        :   [`bus-name`, `dev-name`, `port-index`]

## [Definitions](devlink.md#id81)

### [sb-pool-type](devlink.md#id82)

type:
:   enum

entries:
:   ingress:

    egress:

### [port-type](devlink.md#id83)

type:
:   enum

entries:
:   notset:

    auto:

    eth:

    ib:

### [port-flavour](devlink.md#id84)

type:
:   enum

entries:
:   physical:

    cpu:

    dsa:

    pci-pf:

    pci-vf:

    virtual:

    unused:

    pci-sf:

### [port-fn-state](devlink.md#id85)

type:
:   enum

entries:
:   inactive:

    active:

### [port-fn-opstate](devlink.md#id86)

type:
:   enum

entries:
:   detached:

    attached:

### [port-fn-attr-cap](devlink.md#id87)

type:
:   enum

entries:
:   roce-bit:

    migratable-bit:

    ipsec-crypto-bit:

    ipsec-packet-bit:

### [rate-type](devlink.md#id88)

type:
:   enum

entries:
:   leaf:

    node:

### [sb-threshold-type](devlink.md#id89)

type:
:   enum

entries:
:   static:

    dynamic:

### [eswitch-mode](devlink.md#id90)

type:
:   enum

entries:
:   legacy:

    switchdev:

### [eswitch-inline-mode](devlink.md#id91)

type:
:   enum

entries:
:   none:

    link:

    network:

    transport:

### [eswitch-encap-mode](devlink.md#id92)

type:
:   enum

entries:
:   none:

    basic:

### [dpipe-header-id](devlink.md#id93)

type:
:   enum

entries:
:   ethernet:

    ipv4:

    ipv6:

### [dpipe-match-type](devlink.md#id94)

type:
:   enum

entries:
:   field-exact:

### [dpipe-action-type](devlink.md#id95)

type:
:   enum

entries:
:   field-modify:

### [dpipe-field-mapping-type](devlink.md#id96)

type:
:   enum

entries:
:   none:

    ifindex:

### [resource-unit](devlink.md#id97)

type:
:   enum

entries:
:   entry:

### [reload-action](devlink.md#id98)

type:
:   enum

entries:
:   driver-reinit:

    fw-activate:

### [param-cmode](devlink.md#id99)

type:
:   enum

entries:
:   runtime:

    driverinit:

    permanent:

### [flash-overwrite](devlink.md#id100)

type:
:   enum

entries:
:   settings-bit:

    identifiers-bit:

### [trap-action](devlink.md#id101)

type:
:   enum

entries:
:   drop:

    trap:

    mirror:

### [trap-type](devlink.md#id102)

type:
:   enum

entries:
:   drop:

    exception:

    control:

### [var-attr-type](devlink.md#id103)

type:
:   enum

entries:
:   u8:

    u16:

    u32:

    u64:

    string:

    flag:

    nul-string:

    binary:

### [rate-tc-index-max](devlink.md#id104)

type:
:   const

value:
:   7

## [Attribute sets](devlink.md#id105)

### [devlink](devlink.md#id106)

#### bus-name (`string`)

value:
:   1

#### dev-name (`string`)

#### port-index (`u32`)

#### port-type (`u16`)

enum:
:   [port-type](devlink.md#devlink-definition-port-type)

#### port-desired-type (`u16`)

#### port-netdev-ifindex (`u32`)

#### port-netdev-name (`string`)

#### port-ibdev-name (`string`)

#### port-split-count (`u32`)

#### port-split-group (`u32`)

#### sb-index (`u32`)

#### sb-size (`u32`)

#### sb-ingress-pool-count (`u16`)

#### sb-egress-pool-count (`u16`)

#### sb-ingress-tc-count (`u16`)

#### sb-egress-tc-count (`u16`)

#### sb-pool-index (`u16`)

#### sb-pool-type (`u8`)

enum:
:   [sb-pool-type](devlink.md#devlink-definition-sb-pool-type)

#### sb-pool-size (`u32`)

#### sb-pool-threshold-type (`u8`)

enum:
:   [sb-threshold-type](devlink.md#devlink-definition-sb-threshold-type)

#### sb-threshold (`u32`)

#### sb-tc-index (`u16`)

#### sb-occ-cur (`u32`)

#### sb-occ-max (`u32`)

#### eswitch-mode (`u16`)

enum:
:   [eswitch-mode](devlink.md#devlink-definition-eswitch-mode)

#### eswitch-inline-mode (`u8`)

enum:
:   [eswitch-inline-mode](devlink.md#devlink-definition-eswitch-inline-mode)

#### dpipe-tables (`nest`)

nested-attributes:
:   [dl-dpipe-tables](devlink.md#devlink-attribute-set-dl-dpipe-tables)

#### dpipe-table (`nest`)

multi-attr:
:   True

nested-attributes:
:   [dl-dpipe-table](devlink.md#devlink-attribute-set-dl-dpipe-table)

#### dpipe-table-name (`string`)

#### dpipe-table-size (`u64`)

#### dpipe-table-matches (`nest`)

nested-attributes:
:   [dl-dpipe-table-matches](devlink.md#devlink-attribute-set-dl-dpipe-table-matches)

#### dpipe-table-actions (`nest`)

nested-attributes:
:   [dl-dpipe-table-actions](devlink.md#devlink-attribute-set-dl-dpipe-table-actions)

#### dpipe-table-counters-enabled (`u8`)

#### dpipe-entries (`nest`)

nested-attributes:
:   [dl-dpipe-entries](devlink.md#devlink-attribute-set-dl-dpipe-entries)

#### dpipe-entry (`nest`)

multi-attr:
:   True

nested-attributes:
:   [dl-dpipe-entry](devlink.md#devlink-attribute-set-dl-dpipe-entry)

#### dpipe-entry-index (`u64`)

#### dpipe-entry-match-values (`nest`)

nested-attributes:
:   [dl-dpipe-entry-match-values](devlink.md#devlink-attribute-set-dl-dpipe-entry-match-values)

#### dpipe-entry-action-values (`nest`)

nested-attributes:
:   [dl-dpipe-entry-action-values](devlink.md#devlink-attribute-set-dl-dpipe-entry-action-values)

#### dpipe-entry-counter (`u64`)

#### dpipe-match (`nest`)

multi-attr:
:   True

nested-attributes:
:   [dl-dpipe-match](devlink.md#devlink-attribute-set-dl-dpipe-match)

#### dpipe-match-value (`nest`)

multi-attr:
:   True

nested-attributes:
:   [dl-dpipe-match-value](devlink.md#devlink-attribute-set-dl-dpipe-match-value)

#### dpipe-match-type (`u32`)

enum:
:   [dpipe-match-type](devlink.md#devlink-definition-dpipe-match-type)

#### dpipe-action (`nest`)

multi-attr:
:   True

nested-attributes:
:   [dl-dpipe-action](devlink.md#devlink-attribute-set-dl-dpipe-action)

#### dpipe-action-value (`nest`)

multi-attr:
:   True

nested-attributes:
:   [dl-dpipe-action-value](devlink.md#devlink-attribute-set-dl-dpipe-action-value)

#### dpipe-action-type (`u32`)

enum:
:   [dpipe-action-type](devlink.md#devlink-definition-dpipe-action-type)

#### dpipe-value (`binary`)

#### dpipe-value-mask (`binary`)

#### dpipe-value-mapping (`u32`)

#### dpipe-headers (`nest`)

nested-attributes:
:   [dl-dpipe-headers](devlink.md#devlink-attribute-set-dl-dpipe-headers)

#### dpipe-header (`nest`)

multi-attr:
:   True

nested-attributes:
:   [dl-dpipe-header](devlink.md#devlink-attribute-set-dl-dpipe-header)

#### dpipe-header-name (`string`)

#### dpipe-header-id (`u32`)

enum:
:   [dpipe-header-id](devlink.md#devlink-definition-dpipe-header-id)

#### dpipe-header-fields (`nest`)

nested-attributes:
:   [dl-dpipe-header-fields](devlink.md#devlink-attribute-set-dl-dpipe-header-fields)

#### dpipe-header-global (`u8`)

#### dpipe-header-index (`u32`)

#### dpipe-field (`nest`)

multi-attr:
:   True

nested-attributes:
:   [dl-dpipe-field](devlink.md#devlink-attribute-set-dl-dpipe-field)

#### dpipe-field-name (`string`)

#### dpipe-field-id (`u32`)

#### dpipe-field-bitwidth (`u32`)

#### dpipe-field-mapping-type (`u32`)

enum:
:   [dpipe-field-mapping-type](devlink.md#devlink-definition-dpipe-field-mapping-type)

#### pad (`pad`)

#### eswitch-encap-mode (`u8`)

enum:
:   [eswitch-encap-mode](devlink.md#devlink-definition-eswitch-encap-mode)

#### resource-list (`nest`)

nested-attributes:
:   [dl-resource-list](devlink.md#devlink-attribute-set-dl-resource-list)

#### resource (`nest`)

multi-attr:
:   True

nested-attributes:
:   [dl-resource](devlink.md#devlink-attribute-set-dl-resource)

#### resource-name (`string`)

#### resource-id (`u64`)

#### resource-size (`u64`)

#### resource-size-new (`u64`)

#### resource-size-valid (`u8`)

#### resource-size-min (`u64`)

#### resource-size-max (`u64`)

#### resource-size-gran (`u64`)

#### resource-unit (`u8`)

enum:
:   [resource-unit](devlink.md#devlink-definition-resource-unit)

#### resource-occ (`u64`)

#### dpipe-table-resource-id (`u64`)

#### dpipe-table-resource-units (`u64`)

#### port-flavour (`u16`)

enum:
:   [port-flavour](devlink.md#devlink-definition-port-flavour)

#### port-number (`u32`)

#### port-split-subport-number (`u32`)

#### param (`nest`)

nested-attributes:
:   [dl-param](devlink.md#devlink-attribute-set-dl-param)

#### param-name (`string`)

#### param-generic (`flag`)

#### param-type (`u8`)

enum:
:   [var-attr-type](devlink.md#devlink-definition-var-attr-type)

#### param-value-cmode (`u8`)

enum:
:   [param-cmode](devlink.md#devlink-definition-param-cmode)

value:
:   87

#### region-name (`string`)

#### region-size (`u64`)

#### region-snapshots (`nest`)

nested-attributes:
:   [dl-region-snapshots](devlink.md#devlink-attribute-set-dl-region-snapshots)

#### region-snapshot (`nest`)

nested-attributes:
:   [dl-region-snapshot](devlink.md#devlink-attribute-set-dl-region-snapshot)

#### region-snapshot-id (`u32`)

#### region-chunks (`nest`)

nested-attributes:
:   [dl-region-chunks](devlink.md#devlink-attribute-set-dl-region-chunks)

#### region-chunk (`nest`)

nested-attributes:
:   [dl-region-chunk](devlink.md#devlink-attribute-set-dl-region-chunk)

#### region-chunk-data (`binary`)

#### region-chunk-addr (`u64`)

#### region-chunk-len (`u64`)

#### info-driver-name (`string`)

#### info-serial-number (`string`)

#### info-version-fixed (`nest`)

multi-attr:
:   True

nested-attributes:
:   [dl-info-version](devlink.md#devlink-attribute-set-dl-info-version)

#### info-version-running (`nest`)

multi-attr:
:   True

nested-attributes:
:   [dl-info-version](devlink.md#devlink-attribute-set-dl-info-version)

#### info-version-stored (`nest`)

multi-attr:
:   True

nested-attributes:
:   [dl-info-version](devlink.md#devlink-attribute-set-dl-info-version)

#### info-version-name (`string`)

#### info-version-value (`string`)

#### sb-pool-cell-size (`u32`)

#### fmsg (`nest`)

nested-attributes:
:   [dl-fmsg](devlink.md#devlink-attribute-set-dl-fmsg)

#### fmsg-obj-nest-start (`flag`)

#### fmsg-pair-nest-start (`flag`)

#### fmsg-arr-nest-start (`flag`)

#### fmsg-nest-end (`flag`)

#### fmsg-obj-name (`string`)

#### fmsg-obj-value-type (`u8`)

enum:
:   [var-attr-type](devlink.md#devlink-definition-var-attr-type)

#### health-reporter (`nest`)

value:
:   114

nested-attributes:
:   [dl-health-reporter](devlink.md#devlink-attribute-set-dl-health-reporter)

#### health-reporter-name (`string`)

#### health-reporter-state (`u8`)

#### health-reporter-err-count (`u64`)

#### health-reporter-recover-count (`u64`)

#### health-reporter-dump-ts (`u64`)

#### health-reporter-graceful-period (`u64`)

#### health-reporter-auto-recover (`u8`)

#### flash-update-file-name (`string`)

#### flash-update-component (`string`)

#### flash-update-status-msg (`string`)

#### flash-update-status-done (`u64`)

#### flash-update-status-total (`u64`)

#### port-pci-pf-number (`u16`)

#### port-pci-vf-number (`u16`)

#### stats (`nest`)

nested-attributes:
:   [dl-attr-stats](devlink.md#devlink-attribute-set-dl-attr-stats)

#### trap-name (`string`)

#### trap-action (`u8`)

enum:
:   [trap-action](devlink.md#devlink-definition-trap-action)

#### trap-type (`u8`)

enum:
:   [trap-type](devlink.md#devlink-definition-trap-type)

#### trap-generic (`flag`)

#### trap-metadata (`nest`)

nested-attributes:
:   [dl-trap-metadata](devlink.md#devlink-attribute-set-dl-trap-metadata)

#### trap-group-name (`string`)

#### reload-failed (`u8`)

#### health-reporter-dump-ts-ns (`u64`)

#### netns-fd (`u32`)

#### netns-pid (`u32`)

#### netns-id (`u32`)

#### health-reporter-auto-dump (`u8`)

#### trap-policer-id (`u32`)

#### trap-policer-rate (`u64`)

#### trap-policer-burst (`u64`)

#### port-function (`nest`)

nested-attributes:
:   [dl-port-function](devlink.md#devlink-attribute-set-dl-port-function)

#### info-board-serial-number (`string`)

#### port-lanes (`u32`)

#### port-splittable (`u8`)

#### port-external (`u8`)

#### port-controller-number (`u32`)

#### flash-update-status-timeout (`u64`)

#### flash-update-overwrite-mask (`bitfield32`)

enum:
:   [flash-overwrite](devlink.md#devlink-definition-flash-overwrite)

enum-as-flags:
:   True

#### reload-action (`u8`)

enum:
:   [reload-action](devlink.md#devlink-definition-reload-action)

#### reload-actions-performed (`bitfield32`)

enum:
:   [reload-action](devlink.md#devlink-definition-reload-action)

enum-as-flags:
:   True

#### reload-limits (`bitfield32`)

enum:
:   [reload-action](devlink.md#devlink-definition-reload-action)

enum-as-flags:
:   True

#### dev-stats (`nest`)

nested-attributes:
:   [dl-dev-stats](devlink.md#devlink-attribute-set-dl-dev-stats)

#### reload-stats (`nest`)

nested-attributes:
:   [dl-reload-stats](devlink.md#devlink-attribute-set-dl-reload-stats)

#### reload-stats-entry (`nest`)

multi-attr:
:   True

nested-attributes:
:   [dl-reload-stats-entry](devlink.md#devlink-attribute-set-dl-reload-stats-entry)

#### reload-stats-limit (`u8`)

#### reload-stats-value (`u32`)

#### remote-reload-stats (`nest`)

nested-attributes:
:   [dl-reload-stats](devlink.md#devlink-attribute-set-dl-reload-stats)

#### reload-action-info (`nest`)

multi-attr:
:   True

nested-attributes:
:   [dl-reload-act-info](devlink.md#devlink-attribute-set-dl-reload-act-info)

#### reload-action-stats (`nest`)

multi-attr:
:   True

nested-attributes:
:   [dl-reload-act-stats](devlink.md#devlink-attribute-set-dl-reload-act-stats)

#### port-pci-sf-number (`u32`)

#### rate-type (`u16`)

enum:
:   [rate-type](devlink.md#devlink-definition-rate-type)

#### rate-tx-share (`u64`)

#### rate-tx-max (`u64`)

#### rate-node-name (`string`)

#### rate-parent-node-name (`string`)

#### region-max-snapshots (`u32`)

#### linecard-index (`u32`)

#### linecard-state (`u8`)

#### linecard-type (`string`)

#### linecard-supported-types (`nest`)

nested-attributes:
:   [dl-linecard-supported-types](devlink.md#devlink-attribute-set-dl-linecard-supported-types)

#### selftests (`nest`)

value:
:   176

nested-attributes:
:   [dl-selftest-id](devlink.md#devlink-attribute-set-dl-selftest-id)

#### rate-tx-priority (`u32`)

#### rate-tx-weight (`u32`)

#### region-direct (`flag`)

#### rate-tc-bws (`nest`)

multi-attr:
:   True

nested-attributes:
:   [dl-rate-tc-bws](devlink.md#devlink-attribute-set-dl-rate-tc-bws)

### [dl-dev-stats](devlink.md#id107)

#### reload-stats

#### remote-reload-stats

### [dl-reload-stats](devlink.md#id108)

#### reload-action-info

### [dl-reload-act-info](devlink.md#id109)

#### reload-action

#### reload-action-stats

### [dl-reload-act-stats](devlink.md#id110)

#### reload-stats-entry

### [dl-reload-stats-entry](devlink.md#id111)

#### reload-stats-limit

#### reload-stats-value

### [dl-info-version](devlink.md#id112)

#### info-version-name

#### info-version-value

### [dl-port-function](devlink.md#id113)

#### hw-addr (`binary`)

name-prefix:
:   devlink-port-function-attr-

value:
:   1

#### state (`u8`)

enum:
:   [port-fn-state](devlink.md#devlink-definition-port-fn-state)

#### opstate (`u8`)

enum:
:   [port-fn-opstate](devlink.md#devlink-definition-port-fn-opstate)

#### caps (`bitfield32`)

enum:
:   [port-fn-attr-cap](devlink.md#devlink-definition-port-fn-attr-cap)

enum-as-flags:
:   True

### [dl-dpipe-tables](devlink.md#id114)

#### dpipe-table

### [dl-dpipe-table](devlink.md#id115)

#### dpipe-table-name

#### dpipe-table-size

#### dpipe-table-name

#### dpipe-table-size

#### dpipe-table-matches

#### dpipe-table-actions

#### dpipe-table-counters-enabled

#### dpipe-table-resource-id

#### dpipe-table-resource-units

### [dl-dpipe-table-matches](devlink.md#id116)

#### dpipe-match

### [dl-dpipe-table-actions](devlink.md#id117)

#### dpipe-action

### [dl-dpipe-entries](devlink.md#id118)

#### dpipe-entry

### [dl-dpipe-entry](devlink.md#id119)

#### dpipe-entry-index

#### dpipe-entry-match-values

#### dpipe-entry-action-values

#### dpipe-entry-counter

### [dl-dpipe-entry-match-values](devlink.md#id120)

#### dpipe-match-value

### [dl-dpipe-entry-action-values](devlink.md#id121)

#### dpipe-action-value

### [dl-dpipe-match](devlink.md#id122)

#### dpipe-match-type

#### dpipe-header-id

#### dpipe-header-global

#### dpipe-header-index

#### dpipe-field-id

### [dl-dpipe-match-value](devlink.md#id123)

#### dpipe-match

#### dpipe-value

#### dpipe-value-mask

#### dpipe-value-mapping

### [dl-dpipe-action](devlink.md#id124)

#### dpipe-action-type

#### dpipe-header-id

#### dpipe-header-global

#### dpipe-header-index

#### dpipe-field-id

### [dl-dpipe-action-value](devlink.md#id125)

#### dpipe-action

#### dpipe-value

#### dpipe-value-mask

#### dpipe-value-mapping

### [dl-dpipe-headers](devlink.md#id126)

#### dpipe-header

### [dl-dpipe-header](devlink.md#id127)

#### dpipe-header-name

#### dpipe-header-id

#### dpipe-header-global

#### dpipe-header-fields

### [dl-dpipe-header-fields](devlink.md#id128)

#### dpipe-field

### [dl-dpipe-field](devlink.md#id129)

#### dpipe-field-name

#### dpipe-field-id

#### dpipe-field-bitwidth

#### dpipe-field-mapping-type

### [dl-resource](devlink.md#id130)

#### resource-name

#### resource-id

#### resource-size

#### resource-size-new

#### resource-size-valid

#### resource-size-min

#### resource-size-max

#### resource-size-gran

#### resource-unit

#### resource-occ

### [dl-resource-list](devlink.md#id131)

#### resource

### [dl-param](devlink.md#id132)

#### param-name

#### param-generic

#### param-type

### [dl-region-snapshots](devlink.md#id133)

#### region-snapshot

### [dl-region-snapshot](devlink.md#id134)

#### region-snapshot-id

### [dl-region-chunks](devlink.md#id135)

#### region-chunk

### [dl-region-chunk](devlink.md#id136)

#### region-chunk-data

#### region-chunk-addr

### [dl-fmsg](devlink.md#id137)

#### fmsg-obj-nest-start

#### fmsg-pair-nest-start

#### fmsg-arr-nest-start

#### fmsg-nest-end

#### fmsg-obj-name

### [dl-health-reporter](devlink.md#id138)

#### health-reporter-name

#### health-reporter-state

#### health-reporter-err-count

#### health-reporter-recover-count

#### health-reporter-graceful-period

#### health-reporter-auto-recover

#### health-reporter-dump-ts

#### health-reporter-dump-ts-ns

#### health-reporter-auto-dump

### [dl-attr-stats](devlink.md#id139)

#### stats-rx-packets (`u64`)

value:
:   0

#### stats-rx-bytes (`u64`)

#### stats-rx-dropped (`u64`)

### [dl-trap-metadata](devlink.md#id140)

#### trap-metadata-type-in-port (`flag`)

value:
:   0

#### trap-metadata-type-fa-cookie (`flag`)

### [dl-linecard-supported-types](devlink.md#id141)

#### linecard-type

### [dl-selftest-id](devlink.md#id142)

#### flash (`flag`)

### [dl-rate-tc-bws](devlink.md#id143)

#### index (`u8`)

#### bw (`u32`)

doc:
:   Specifies the bandwidth share assigned to the Traffic Class. The bandwidth for the traffic class is determined in proportion to the sum of the shares of all configured classes.
