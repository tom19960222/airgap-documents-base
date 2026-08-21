---
collection: kernel
version: "6.8"
title: "Family devlink netlink specification"
source_url: https://www.kernel.org/doc/html/v6.8/networking/netlink_spec/devlink.html
fetched_at: 2026-08-21T03:49:14+00:00
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
  - [Attribute sets](devlink.md#attribute-sets)

    - [devlink](devlink.md#devlink)

      - [bus-name (`string`)](devlink.md#bus-name-string)
      - [dev-name (`string`)](devlink.md#dev-name-string)
      - [port-index (`u32`)](devlink.md#port-index-u32)
      - [port-type (`u16`)](devlink.md#port-type-u16)
      - [port-desired-type (`u16`)](devlink.md#port-desired-type-u16)
      - [port-netdev-ifindex (`u32`)](devlink.md#port-netdev-ifindex-u32)
      - [port-netdev-name (`string`)](devlink.md#port-netdev-name-string)
      - [port-ibdev-name (`string`)](devlink.md#port-ibdev-name-string)
      - [port-split-count (`u32`)](devlink.md#port-split-count-u32)
      - [port-split-group (`u32`)](devlink.md#port-split-group-u32)
      - [sb-index (`u32`)](devlink.md#sb-index-u32)
      - [sb-size (`u32`)](devlink.md#sb-size-u32)
      - [sb-ingress-pool-count (`u16`)](devlink.md#sb-ingress-pool-count-u16)
      - [sb-egress-pool-count (`u16`)](devlink.md#sb-egress-pool-count-u16)
      - [sb-ingress-tc-count (`u16`)](devlink.md#sb-ingress-tc-count-u16)
      - [sb-egress-tc-count (`u16`)](devlink.md#sb-egress-tc-count-u16)
      - [sb-pool-index (`u16`)](devlink.md#sb-pool-index-u16)
      - [sb-pool-type (`u8`)](devlink.md#sb-pool-type-u8)
      - [sb-pool-size (`u32`)](devlink.md#sb-pool-size-u32)
      - [sb-pool-threshold-type (`u8`)](devlink.md#sb-pool-threshold-type-u8)
      - [sb-threshold (`u32`)](devlink.md#sb-threshold-u32)
      - [sb-tc-index (`u16`)](devlink.md#sb-tc-index-u16)
      - [sb-occ-cur (`u32`)](devlink.md#sb-occ-cur-u32)
      - [sb-occ-max (`u32`)](devlink.md#sb-occ-max-u32)
      - [eswitch-mode (`u16`)](devlink.md#eswitch-mode-u16)
      - [eswitch-inline-mode (`u16`)](devlink.md#eswitch-inline-mode-u16)
      - [dpipe-tables (`nest`)](devlink.md#dpipe-tables-nest)
      - [dpipe-table (`nest`)](devlink.md#dpipe-table-nest)
      - [dpipe-table-name (`string`)](devlink.md#dpipe-table-name-string)
      - [dpipe-table-size (`u64`)](devlink.md#dpipe-table-size-u64)
      - [dpipe-table-matches (`nest`)](devlink.md#dpipe-table-matches-nest)
      - [dpipe-table-actions (`nest`)](devlink.md#dpipe-table-actions-nest)
      - [dpipe-table-counters-enabled (`u8`)](devlink.md#dpipe-table-counters-enabled-u8)
      - [dpipe-entries (`nest`)](devlink.md#dpipe-entries-nest)
      - [dpipe-entry (`nest`)](devlink.md#dpipe-entry-nest)
      - [dpipe-entry-index (`u64`)](devlink.md#dpipe-entry-index-u64)
      - [dpipe-entry-match-values (`nest`)](devlink.md#dpipe-entry-match-values-nest)
      - [dpipe-entry-action-values (`nest`)](devlink.md#dpipe-entry-action-values-nest)
      - [dpipe-entry-counter (`u64`)](devlink.md#dpipe-entry-counter-u64)
      - [dpipe-match (`nest`)](devlink.md#dpipe-match-nest)
      - [dpipe-match-value (`nest`)](devlink.md#dpipe-match-value-nest)
      - [dpipe-match-type (`u32`)](devlink.md#dpipe-match-type-u32)
      - [dpipe-action (`nest`)](devlink.md#dpipe-action-nest)
      - [dpipe-action-value (`nest`)](devlink.md#dpipe-action-value-nest)
      - [dpipe-action-type (`u32`)](devlink.md#dpipe-action-type-u32)
      - [dpipe-value (`binary`)](devlink.md#dpipe-value-binary)
      - [dpipe-value-mask (`binary`)](devlink.md#dpipe-value-mask-binary)
      - [dpipe-value-mapping (`u32`)](devlink.md#dpipe-value-mapping-u32)
      - [dpipe-headers (`nest`)](devlink.md#dpipe-headers-nest)
      - [dpipe-header (`nest`)](devlink.md#dpipe-header-nest)
      - [dpipe-header-name (`string`)](devlink.md#dpipe-header-name-string)
      - [dpipe-header-id (`u32`)](devlink.md#dpipe-header-id-u32)
      - [dpipe-header-fields (`nest`)](devlink.md#dpipe-header-fields-nest)
      - [dpipe-header-global (`u8`)](devlink.md#dpipe-header-global-u8)
      - [dpipe-header-index (`u32`)](devlink.md#dpipe-header-index-u32)
      - [dpipe-field (`nest`)](devlink.md#dpipe-field-nest)
      - [dpipe-field-name (`string`)](devlink.md#dpipe-field-name-string)
      - [dpipe-field-id (`u32`)](devlink.md#dpipe-field-id-u32)
      - [dpipe-field-bitwidth (`u32`)](devlink.md#dpipe-field-bitwidth-u32)
      - [dpipe-field-mapping-type (`u32`)](devlink.md#dpipe-field-mapping-type-u32)
      - [pad (`pad`)](devlink.md#pad-pad)
      - [eswitch-encap-mode (`u8`)](devlink.md#eswitch-encap-mode-u8)
      - [resource-list (`nest`)](devlink.md#resource-list-nest)
      - [resource (`nest`)](devlink.md#resource-nest)
      - [resource-name (`string`)](devlink.md#resource-name-string)
      - [resource-id (`u64`)](devlink.md#resource-id-u64)
      - [resource-size (`u64`)](devlink.md#resource-size-u64)
      - [resource-size-new (`u64`)](devlink.md#resource-size-new-u64)
      - [resource-size-valid (`u8`)](devlink.md#resource-size-valid-u8)
      - [resource-size-min (`u64`)](devlink.md#resource-size-min-u64)
      - [resource-size-max (`u64`)](devlink.md#resource-size-max-u64)
      - [resource-size-gran (`u64`)](devlink.md#resource-size-gran-u64)
      - [resource-unit (`u8`)](devlink.md#resource-unit-u8)
      - [resource-occ (`u64`)](devlink.md#resource-occ-u64)
      - [dpipe-table-resource-id (`u64`)](devlink.md#dpipe-table-resource-id-u64)
      - [dpipe-table-resource-units (`u64`)](devlink.md#dpipe-table-resource-units-u64)
      - [port-flavour (`u16`)](devlink.md#port-flavour-u16)
      - [port-number (`u32`)](devlink.md#port-number-u32)
      - [port-split-subport-number (`u32`)](devlink.md#port-split-subport-number-u32)
      - [param (`nest`)](devlink.md#param-nest)
      - [param-name (`string`)](devlink.md#param-name-string)
      - [param-generic (`flag`)](devlink.md#param-generic-flag)
      - [param-type (`u8`)](devlink.md#param-type-u8)
      - [param-value-cmode (`u8`)](devlink.md#param-value-cmode-u8)
      - [region-name (`string`)](devlink.md#region-name-string)
      - [region-size (`u64`)](devlink.md#region-size-u64)
      - [region-snapshots (`nest`)](devlink.md#region-snapshots-nest)
      - [region-snapshot (`nest`)](devlink.md#region-snapshot-nest)
      - [region-snapshot-id (`u32`)](devlink.md#region-snapshot-id-u32)
      - [region-chunks (`nest`)](devlink.md#region-chunks-nest)
      - [region-chunk (`nest`)](devlink.md#region-chunk-nest)
      - [region-chunk-data (`binary`)](devlink.md#region-chunk-data-binary)
      - [region-chunk-addr (`u64`)](devlink.md#region-chunk-addr-u64)
      - [region-chunk-len (`u64`)](devlink.md#region-chunk-len-u64)
      - [info-driver-name (`string`)](devlink.md#info-driver-name-string)
      - [info-serial-number (`string`)](devlink.md#info-serial-number-string)
      - [info-version-fixed (`nest`)](devlink.md#info-version-fixed-nest)
      - [info-version-running (`nest`)](devlink.md#info-version-running-nest)
      - [info-version-stored (`nest`)](devlink.md#info-version-stored-nest)
      - [info-version-name (`string`)](devlink.md#info-version-name-string)
      - [info-version-value (`string`)](devlink.md#info-version-value-string)
      - [sb-pool-cell-size (`u32`)](devlink.md#sb-pool-cell-size-u32)
      - [fmsg (`nest`)](devlink.md#fmsg-nest)
      - [fmsg-obj-nest-start (`flag`)](devlink.md#fmsg-obj-nest-start-flag)
      - [fmsg-pair-nest-start (`flag`)](devlink.md#fmsg-pair-nest-start-flag)
      - [fmsg-arr-nest-start (`flag`)](devlink.md#fmsg-arr-nest-start-flag)
      - [fmsg-nest-end (`flag`)](devlink.md#fmsg-nest-end-flag)
      - [fmsg-obj-name (`string`)](devlink.md#fmsg-obj-name-string)
      - [fmsg-obj-value-type (`u8`)](devlink.md#fmsg-obj-value-type-u8)
      - [health-reporter (`nest`)](devlink.md#health-reporter-nest)
      - [health-reporter-name (`string`)](devlink.md#health-reporter-name-string)
      - [health-reporter-state (`u8`)](devlink.md#health-reporter-state-u8)
      - [health-reporter-err-count (`u64`)](devlink.md#health-reporter-err-count-u64)
      - [health-reporter-recover-count (`u64`)](devlink.md#health-reporter-recover-count-u64)
      - [health-reporter-dump-ts (`u64`)](devlink.md#health-reporter-dump-ts-u64)
      - [health-reporter-graceful-period (`u64`)](devlink.md#health-reporter-graceful-period-u64)
      - [health-reporter-auto-recover (`u8`)](devlink.md#health-reporter-auto-recover-u8)
      - [flash-update-file-name (`string`)](devlink.md#flash-update-file-name-string)
      - [flash-update-component (`string`)](devlink.md#flash-update-component-string)
      - [flash-update-status-msg (`string`)](devlink.md#flash-update-status-msg-string)
      - [flash-update-status-done (`u64`)](devlink.md#flash-update-status-done-u64)
      - [flash-update-status-total (`u64`)](devlink.md#flash-update-status-total-u64)
      - [port-pci-pf-number (`u16`)](devlink.md#port-pci-pf-number-u16)
      - [port-pci-vf-number (`u16`)](devlink.md#port-pci-vf-number-u16)
      - [stats (`nest`)](devlink.md#stats-nest)
      - [trap-name (`string`)](devlink.md#trap-name-string)
      - [trap-action (`u8`)](devlink.md#trap-action-u8)
      - [trap-type (`u8`)](devlink.md#trap-type-u8)
      - [trap-generic (`flag`)](devlink.md#trap-generic-flag)
      - [trap-metadata (`nest`)](devlink.md#trap-metadata-nest)
      - [trap-group-name (`string`)](devlink.md#trap-group-name-string)
      - [reload-failed (`u8`)](devlink.md#reload-failed-u8)
      - [health-reporter-dump-ts-ns (`u64`)](devlink.md#health-reporter-dump-ts-ns-u64)
      - [netns-fd (`u32`)](devlink.md#netns-fd-u32)
      - [netns-pid (`u32`)](devlink.md#netns-pid-u32)
      - [netns-id (`u32`)](devlink.md#netns-id-u32)
      - [health-reporter-auto-dump (`u8`)](devlink.md#health-reporter-auto-dump-u8)
      - [trap-policer-id (`u32`)](devlink.md#trap-policer-id-u32)
      - [trap-policer-rate (`u64`)](devlink.md#trap-policer-rate-u64)
      - [trap-policer-burst (`u64`)](devlink.md#trap-policer-burst-u64)
      - [port-function (`nest`)](devlink.md#port-function-nest)
      - [info-board-serial-number (`string`)](devlink.md#info-board-serial-number-string)
      - [port-lanes (`u32`)](devlink.md#port-lanes-u32)
      - [port-splittable (`u8`)](devlink.md#port-splittable-u8)
      - [port-external (`u8`)](devlink.md#port-external-u8)
      - [port-controller-number (`u32`)](devlink.md#port-controller-number-u32)
      - [flash-update-status-timeout (`u64`)](devlink.md#flash-update-status-timeout-u64)
      - [flash-update-overwrite-mask (`bitfield32`)](devlink.md#flash-update-overwrite-mask-bitfield32)
      - [reload-action (`u8`)](devlink.md#reload-action-u8)
      - [reload-actions-performed (`bitfield32`)](devlink.md#reload-actions-performed-bitfield32)
      - [reload-limits (`bitfield32`)](devlink.md#reload-limits-bitfield32)
      - [dev-stats (`nest`)](devlink.md#dev-stats-nest)
      - [reload-stats (`nest`)](devlink.md#reload-stats-nest)
      - [reload-stats-entry (`nest`)](devlink.md#reload-stats-entry-nest)
      - [reload-stats-limit (`u8`)](devlink.md#reload-stats-limit-u8)
      - [reload-stats-value (`u32`)](devlink.md#reload-stats-value-u32)
      - [remote-reload-stats (`nest`)](devlink.md#remote-reload-stats-nest)
      - [reload-action-info (`nest`)](devlink.md#reload-action-info-nest)
      - [reload-action-stats (`nest`)](devlink.md#reload-action-stats-nest)
      - [port-pci-sf-number (`u32`)](devlink.md#port-pci-sf-number-u32)
      - [rate-type (`u16`)](devlink.md#rate-type-u16)
      - [rate-tx-share (`u64`)](devlink.md#rate-tx-share-u64)
      - [rate-tx-max (`u64`)](devlink.md#rate-tx-max-u64)
      - [rate-node-name (`string`)](devlink.md#rate-node-name-string)
      - [rate-parent-node-name (`string`)](devlink.md#rate-parent-node-name-string)
      - [region-max-snapshots (`u32`)](devlink.md#region-max-snapshots-u32)
      - [linecard-index (`u32`)](devlink.md#linecard-index-u32)
      - [linecard-state (`u8`)](devlink.md#linecard-state-u8)
      - [linecard-type (`string`)](devlink.md#linecard-type-string)
      - [linecard-supported-types (`nest`)](devlink.md#linecard-supported-types-nest)
      - [selftests (`nest`)](devlink.md#selftests-nest)
      - [rate-tx-priority (`u32`)](devlink.md#rate-tx-priority-u32)
      - [rate-tx-weight (`u32`)](devlink.md#rate-tx-weight-u32)
      - [region-direct (`flag`)](devlink.md#region-direct-flag)
    - [dl-dev-stats](devlink.md#dl-dev-stats)

      - [reload-stats](devlink.md#reload-stats)
      - [remote-reload-stats](devlink.md#remote-reload-stats)
    - [dl-reload-stats](devlink.md#dl-reload-stats)

      - [reload-action-info](devlink.md#reload-action-info)
    - [dl-reload-act-info](devlink.md#dl-reload-act-info)

      - [reload-action](devlink.md#id1)
      - [reload-action-stats](devlink.md#reload-action-stats)
    - [dl-reload-act-stats](devlink.md#dl-reload-act-stats)

      - [reload-stats-entry](devlink.md#reload-stats-entry)
    - [dl-reload-stats-entry](devlink.md#dl-reload-stats-entry)

      - [reload-stats-limit](devlink.md#reload-stats-limit)
      - [reload-stats-value](devlink.md#reload-stats-value)
    - [dl-info-version](devlink.md#dl-info-version)

      - [info-version-name](devlink.md#info-version-name)
      - [info-version-value](devlink.md#info-version-value)
    - [dl-port-function](devlink.md#dl-port-function)

      - [hw-addr (`binary`)](devlink.md#hw-addr-binary)
      - [state (`u8`)](devlink.md#state-u8)
      - [opstate (`u8`)](devlink.md#opstate-u8)
      - [caps (`bitfield32`)](devlink.md#caps-bitfield32)
    - [dl-dpipe-tables](devlink.md#dl-dpipe-tables)

      - [dpipe-table](devlink.md#dpipe-table)
    - [dl-dpipe-table](devlink.md#dl-dpipe-table)

      - [dpipe-table-name](devlink.md#dpipe-table-name)
      - [dpipe-table-size](devlink.md#dpipe-table-size)
      - [dpipe-table-name](devlink.md#id2)
      - [dpipe-table-size](devlink.md#id3)
      - [dpipe-table-matches](devlink.md#dpipe-table-matches)
      - [dpipe-table-actions](devlink.md#dpipe-table-actions)
      - [dpipe-table-counters-enabled](devlink.md#dpipe-table-counters-enabled)
      - [dpipe-table-resource-id](devlink.md#dpipe-table-resource-id)
      - [dpipe-table-resource-units](devlink.md#dpipe-table-resource-units)
    - [dl-dpipe-table-matches](devlink.md#dl-dpipe-table-matches)

      - [dpipe-match](devlink.md#dpipe-match)
    - [dl-dpipe-table-actions](devlink.md#dl-dpipe-table-actions)

      - [dpipe-action](devlink.md#dpipe-action)
    - [dl-dpipe-entries](devlink.md#dl-dpipe-entries)

      - [dpipe-entry](devlink.md#dpipe-entry)
    - [dl-dpipe-entry](devlink.md#dl-dpipe-entry)

      - [dpipe-entry-index](devlink.md#dpipe-entry-index)
      - [dpipe-entry-match-values](devlink.md#dpipe-entry-match-values)
      - [dpipe-entry-action-values](devlink.md#dpipe-entry-action-values)
      - [dpipe-entry-counter](devlink.md#dpipe-entry-counter)
    - [dl-dpipe-entry-match-values](devlink.md#dl-dpipe-entry-match-values)

      - [dpipe-match-value](devlink.md#dpipe-match-value)
    - [dl-dpipe-entry-action-values](devlink.md#dl-dpipe-entry-action-values)

      - [dpipe-action-value](devlink.md#dpipe-action-value)
    - [dl-dpipe-match](devlink.md#dl-dpipe-match)

      - [dpipe-match-type](devlink.md#id4)
      - [dpipe-header-id](devlink.md#id5)
      - [dpipe-header-global](devlink.md#dpipe-header-global)
      - [dpipe-header-index](devlink.md#dpipe-header-index)
      - [dpipe-field-id](devlink.md#dpipe-field-id)
    - [dl-dpipe-match-value](devlink.md#dl-dpipe-match-value)

      - [dpipe-match](devlink.md#id6)
      - [dpipe-value](devlink.md#dpipe-value)
      - [dpipe-value-mask](devlink.md#dpipe-value-mask)
      - [dpipe-value-mapping](devlink.md#dpipe-value-mapping)
    - [dl-dpipe-action](devlink.md#dl-dpipe-action)

      - [dpipe-action-type](devlink.md#id7)
      - [dpipe-header-id](devlink.md#id8)
      - [dpipe-header-global](devlink.md#id9)
      - [dpipe-header-index](devlink.md#id10)
      - [dpipe-field-id](devlink.md#id11)
    - [dl-dpipe-action-value](devlink.md#dl-dpipe-action-value)

      - [dpipe-action](devlink.md#id12)
      - [dpipe-value](devlink.md#id13)
      - [dpipe-value-mask](devlink.md#id14)
      - [dpipe-value-mapping](devlink.md#id15)
    - [dl-dpipe-headers](devlink.md#dl-dpipe-headers)

      - [dpipe-header](devlink.md#dpipe-header)
    - [dl-dpipe-header](devlink.md#dl-dpipe-header)

      - [dpipe-header-name](devlink.md#dpipe-header-name)
      - [dpipe-header-id](devlink.md#id16)
      - [dpipe-header-global](devlink.md#id17)
      - [dpipe-header-fields](devlink.md#dpipe-header-fields)
    - [dl-dpipe-header-fields](devlink.md#dl-dpipe-header-fields)

      - [dpipe-field](devlink.md#dpipe-field)
    - [dl-dpipe-field](devlink.md#dl-dpipe-field)

      - [dpipe-field-name](devlink.md#dpipe-field-name)
      - [dpipe-field-id](devlink.md#id18)
      - [dpipe-field-bitwidth](devlink.md#dpipe-field-bitwidth)
      - [dpipe-field-mapping-type](devlink.md#id19)
    - [dl-resource](devlink.md#dl-resource)

      - [resource-name](devlink.md#resource-name)
      - [resource-id](devlink.md#resource-id)
      - [resource-size](devlink.md#resource-size)
      - [resource-size-new](devlink.md#resource-size-new)
      - [resource-size-valid](devlink.md#resource-size-valid)
      - [resource-size-min](devlink.md#resource-size-min)
      - [resource-size-max](devlink.md#resource-size-max)
      - [resource-size-gran](devlink.md#resource-size-gran)
      - [resource-unit](devlink.md#id20)
      - [resource-occ](devlink.md#resource-occ)
    - [dl-resource-list](devlink.md#dl-resource-list)

      - [resource](devlink.md#resource)
    - [dl-param](devlink.md#dl-param)

      - [param-name](devlink.md#param-name)
      - [param-generic](devlink.md#param-generic)
      - [param-type](devlink.md#param-type)
    - [dl-region-snapshots](devlink.md#dl-region-snapshots)

      - [region-snapshot](devlink.md#region-snapshot)
    - [dl-region-snapshot](devlink.md#dl-region-snapshot)

      - [region-snapshot-id](devlink.md#region-snapshot-id)
    - [dl-region-chunks](devlink.md#dl-region-chunks)

      - [region-chunk](devlink.md#region-chunk)
    - [dl-region-chunk](devlink.md#dl-region-chunk)

      - [region-chunk-data](devlink.md#region-chunk-data)
      - [region-chunk-addr](devlink.md#region-chunk-addr)
    - [dl-fmsg](devlink.md#dl-fmsg)

      - [fmsg-obj-nest-start](devlink.md#fmsg-obj-nest-start)
      - [fmsg-pair-nest-start](devlink.md#fmsg-pair-nest-start)
      - [fmsg-arr-nest-start](devlink.md#fmsg-arr-nest-start)
      - [fmsg-nest-end](devlink.md#fmsg-nest-end)
      - [fmsg-obj-name](devlink.md#fmsg-obj-name)
    - [dl-health-reporter](devlink.md#dl-health-reporter)

      - [health-reporter-name](devlink.md#health-reporter-name)
      - [health-reporter-state](devlink.md#health-reporter-state)
      - [health-reporter-err-count](devlink.md#health-reporter-err-count)
      - [health-reporter-recover-count](devlink.md#health-reporter-recover-count)
      - [health-reporter-graceful-period](devlink.md#health-reporter-graceful-period)
      - [health-reporter-auto-recover](devlink.md#health-reporter-auto-recover)
      - [health-reporter-dump-ts](devlink.md#health-reporter-dump-ts)
      - [health-reporter-dump-ts-ns](devlink.md#health-reporter-dump-ts-ns)
      - [health-reporter-auto-dump](devlink.md#health-reporter-auto-dump)
    - [dl-attr-stats](devlink.md#dl-attr-stats)

      - [stats-rx-packets (`u64`)](devlink.md#stats-rx-packets-u64)
      - [stats-rx-bytes (`u64`)](devlink.md#stats-rx-bytes-u64)
      - [stats-rx-dropped (`u64`)](devlink.md#stats-rx-dropped-u64)
    - [dl-trap-metadata](devlink.md#dl-trap-metadata)

      - [trap-metadata-type-in-port (`flag`)](devlink.md#trap-metadata-type-in-port-flag)
      - [trap-metadata-type-fa-cookie (`flag`)](devlink.md#trap-metadata-type-fa-cookie-flag)
    - [dl-linecard-supported-types](devlink.md#dl-linecard-supported-types)

      - [linecard-type](devlink.md#linecard-type)
    - [dl-selftest-id](devlink.md#dl-selftest-id)

      - [flash (`flag`)](devlink.md#flash-flag)

## [Summary](devlink.md#id22)

Partial family for Devlink.

## [Operations](devlink.md#id23)

### [get](devlink.md#id24)

Get devlink instances.

attribute-set
:   devlink

dont-validate
:   ['strict', 'dump']

do
:   **pre**

    **post**

    **request**
    :   attributes
        :   [`bus-name`, `dev-name`]

    **reply**
    :   attributes
        :   [`bus-name`, `dev-name`, `reload-failed`, `dev-stats`]

dump
:   **reply**
    :   attributes
        :   [`bus-name`, `dev-name`, `reload-failed`, `dev-stats`]

### [port-get](devlink.md#id25)

Get devlink port instances.

attribute-set
:   devlink

dont-validate
:   ['strict']

do
:   **pre**

    **post**

    **request**
    :   attributes
        :   [`bus-name`, `dev-name`, `port-index`]

    **reply**
    :   attributes
        :   [`bus-name`, `dev-name`, `port-index`]

dump
:   **request**
    :   attributes
        :   [`bus-name`, `dev-name`]

    **reply**
    :   attributes
        :   [`bus-name`, `dev-name`, `port-index`]

### [port-set](devlink.md#id26)

Set devlink port instances.

attribute-set
:   devlink

dont-validate
:   ['strict']

flags
:   ['admin-perm']

do
:   **pre**

    **post**

    **request**
    :   attributes
        :   [`bus-name`, `dev-name`, `port-index`, `port-type`, `port-function`]

### [port-new](devlink.md#id27)

Create devlink port instances.

attribute-set
:   devlink

dont-validate
:   ['strict']

flags
:   ['admin-perm']

do
:   **pre**

    **post**

    **request**
    :   attributes
        :   [`bus-name`, `dev-name`, `port-index`, `port-flavour`, `port-pci-pf-number`, `port-pci-sf-number`, `port-controller-number`]

    **reply**
    :   attributes
        :   [`bus-name`, `dev-name`, `port-index`]

### [port-del](devlink.md#id28)

Delete devlink port instances.

attribute-set
:   devlink

dont-validate
:   ['strict']

flags
:   ['admin-perm']

do
:   **pre**

    **post**

    **request**
    :   attributes
        :   [`bus-name`, `dev-name`, `port-index`]

### [port-split](devlink.md#id29)

Split devlink port instances.

attribute-set
:   devlink

dont-validate
:   ['strict']

flags
:   ['admin-perm']

do
:   **pre**

    **post**

    **request**
    :   attributes
        :   [`bus-name`, `dev-name`, `port-index`, `port-split-count`]

### [port-unsplit](devlink.md#id30)

Unplit devlink port instances.

attribute-set
:   devlink

dont-validate
:   ['strict']

flags
:   ['admin-perm']

do
:   **pre**

    **post**

    **request**
    :   attributes
        :   [`bus-name`, `dev-name`, `port-index`]

### [sb-get](devlink.md#id31)

Get shared buffer instances.

attribute-set
:   devlink

dont-validate
:   ['strict']

do
:   **pre**

    **post**

    **request**
    :   attributes
        :   [`bus-name`, `dev-name`, `sb-index`]

    **reply**
    :   attributes
        :   [`bus-name`, `dev-name`, `sb-index`]

dump
:   **request**
    :   attributes
        :   [`bus-name`, `dev-name`]

    **reply**
    :   attributes
        :   [`bus-name`, `dev-name`, `sb-index`]

### [sb-pool-get](devlink.md#id32)

Get shared buffer pool instances.

attribute-set
:   devlink

dont-validate
:   ['strict']

do
:   **pre**

    **post**

    **request**
    :   attributes
        :   [`bus-name`, `dev-name`, `sb-index`, `sb-pool-index`]

    **reply**
    :   attributes
        :   [`bus-name`, `dev-name`, `sb-index`, `sb-pool-index`]

dump
:   **request**
    :   attributes
        :   [`bus-name`, `dev-name`]

    **reply**
    :   attributes
        :   [`bus-name`, `dev-name`, `sb-index`, `sb-pool-index`]

### [sb-pool-set](devlink.md#id33)

Set shared buffer pool instances.

attribute-set
:   devlink

dont-validate
:   ['strict']

flags
:   ['admin-perm']

do
:   **pre**

    **post**

    **request**
    :   attributes
        :   [`bus-name`, `dev-name`, `sb-index`, `sb-pool-index`, `sb-pool-threshold-type`, `sb-pool-size`]

### [sb-port-pool-get](devlink.md#id34)

Get shared buffer port-pool combinations and threshold.

attribute-set
:   devlink

dont-validate
:   ['strict']

do
:   **pre**

    **post**

    **request**
    :   attributes
        :   [`bus-name`, `dev-name`, `port-index`, `sb-index`, `sb-pool-index`]

    **reply**
    :   attributes
        :   [`bus-name`, `dev-name`, `port-index`, `sb-index`, `sb-pool-index`]

dump
:   **request**
    :   attributes
        :   [`bus-name`, `dev-name`]

    **reply**
    :   attributes
        :   [`bus-name`, `dev-name`, `port-index`, `sb-index`, `sb-pool-index`]

### [sb-port-pool-set](devlink.md#id35)

Set shared buffer port-pool combinations and threshold.

attribute-set
:   devlink

dont-validate
:   ['strict']

flags
:   ['admin-perm']

do
:   **pre**

    **post**

    **request**
    :   attributes
        :   [`bus-name`, `dev-name`, `port-index`, `sb-index`, `sb-pool-index`, `sb-threshold`]

### [sb-tc-pool-bind-get](devlink.md#id36)

Get shared buffer port-TC to pool bindings and threshold.

attribute-set
:   devlink

dont-validate
:   ['strict']

do
:   **pre**

    **post**

    **request**
    :   attributes
        :   [`bus-name`, `dev-name`, `port-index`, `sb-index`, `sb-pool-type`, `sb-tc-index`]

    **reply**
    :   attributes
        :   [`bus-name`, `dev-name`, `port-index`, `sb-index`, `sb-pool-type`, `sb-tc-index`]

dump
:   **request**
    :   attributes
        :   [`bus-name`, `dev-name`]

    **reply**
    :   attributes
        :   [`bus-name`, `dev-name`, `port-index`, `sb-index`, `sb-pool-type`, `sb-tc-index`]

### [sb-tc-pool-bind-set](devlink.md#id37)

Set shared buffer port-TC to pool bindings and threshold.

attribute-set
:   devlink

dont-validate
:   ['strict']

flags
:   ['admin-perm']

do
:   **pre**

    **post**

    **request**
    :   attributes
        :   [`bus-name`, `dev-name`, `port-index`, `sb-index`, `sb-pool-index`, `sb-pool-type`, `sb-tc-index`, `sb-threshold`]

### [sb-occ-snapshot](devlink.md#id38)

Take occupancy snapshot of shared buffer.

attribute-set
:   devlink

dont-validate
:   ['strict']

flags
:   ['admin-perm']

do
:   **pre**

    **post**

    **request**
    :   attributes
        :   [`bus-name`, `dev-name`, `sb-index`]

### [sb-occ-max-clear](devlink.md#id39)

Clear occupancy watermarks of shared buffer.

attribute-set
:   devlink

dont-validate
:   ['strict']

flags
:   ['admin-perm']

do
:   **pre**

    **post**

    **request**
    :   attributes
        :   [`bus-name`, `dev-name`, `sb-index`]

### [eswitch-get](devlink.md#id40)

Get eswitch attributes.

attribute-set
:   devlink

dont-validate
:   ['strict']

flags
:   ['admin-perm']

do
:   **pre**

    **post**

    **request**
    :   attributes
        :   [`bus-name`, `dev-name`]

    **reply**
    :   attributes
        :   [`bus-name`, `dev-name`, `eswitch-mode`, `eswitch-inline-mode`, `eswitch-encap-mode`]

### [eswitch-set](devlink.md#id41)

Set eswitch attributes.

attribute-set
:   devlink

dont-validate
:   ['strict']

flags
:   ['admin-perm']

do
:   **pre**

    **post**

    **request**
    :   attributes
        :   [`bus-name`, `dev-name`, `eswitch-mode`, `eswitch-inline-mode`, `eswitch-encap-mode`]

### [dpipe-table-get](devlink.md#id42)

Get dpipe table attributes.

attribute-set
:   devlink

dont-validate
:   ['strict']

do
:   **pre**

    **post**

    **request**
    :   attributes
        :   [`bus-name`, `dev-name`, `dpipe-table-name`]

    **reply**
    :   attributes
        :   [`bus-name`, `dev-name`, `dpipe-tables`]

### [dpipe-entries-get](devlink.md#id43)

Get dpipe entries attributes.

attribute-set
:   devlink

dont-validate
:   ['strict']

do
:   **pre**

    **post**

    **request**
    :   attributes
        :   [`bus-name`, `dev-name`, `dpipe-table-name`]

    **reply**
    :   attributes
        :   [`bus-name`, `dev-name`, `dpipe-entries`]

### [dpipe-headers-get](devlink.md#id44)

Get dpipe headers attributes.

attribute-set
:   devlink

dont-validate
:   ['strict']

do
:   **pre**

    **post**

    **request**
    :   attributes
        :   [`bus-name`, `dev-name`]

    **reply**
    :   attributes
        :   [`bus-name`, `dev-name`, `dpipe-headers`]

### [dpipe-table-counters-set](devlink.md#id45)

Set dpipe counter attributes.

attribute-set
:   devlink

dont-validate
:   ['strict']

flags
:   ['admin-perm']

do
:   **pre**

    **post**

    **request**
    :   attributes
        :   [`bus-name`, `dev-name`, `dpipe-table-name`, `dpipe-table-counters-enabled`]

### [resource-set](devlink.md#id46)

Set resource attributes.

attribute-set
:   devlink

dont-validate
:   ['strict']

flags
:   ['admin-perm']

do
:   **pre**

    **post**

    **request**
    :   attributes
        :   [`bus-name`, `dev-name`, `resource-id`, `resource-size`]

### [resource-dump](devlink.md#id47)

Get resource attributes.

attribute-set
:   devlink

dont-validate
:   ['strict']

do
:   **pre**

    **post**

    **request**
    :   attributes
        :   [`bus-name`, `dev-name`]

    **reply**
    :   attributes
        :   [`bus-name`, `dev-name`, `resource-list`]

### [reload](devlink.md#id48)

Reload devlink.

attribute-set
:   devlink

dont-validate
:   ['strict']

flags
:   ['admin-perm']

do
:   **pre**

    **post**

    **request**
    :   attributes
        :   [`bus-name`, `dev-name`, `reload-action`, `reload-limits`, `netns-pid`, `netns-fd`, `netns-id`]

    **reply**
    :   attributes
        :   [`bus-name`, `dev-name`, `reload-actions-performed`]

### [param-get](devlink.md#id49)

Get param instances.

attribute-set
:   devlink

dont-validate
:   ['strict']

do
:   **pre**

    **post**

    **request**
    :   attributes
        :   [`bus-name`, `dev-name`, `param-name`]

    **reply**
    :   attributes
        :   [`bus-name`, `dev-name`, `param-name`]

dump
:   **request**
    :   attributes
        :   [`bus-name`, `dev-name`]

    **reply**
    :   attributes
        :   [`bus-name`, `dev-name`, `param-name`]

### [param-set](devlink.md#id50)

Set param instances.

attribute-set
:   devlink

dont-validate
:   ['strict']

flags
:   ['admin-perm']

do
:   **pre**

    **post**

    **request**
    :   attributes
        :   [`bus-name`, `dev-name`, `param-name`, `param-type`, `param-value-cmode`]

### [region-get](devlink.md#id51)

Get region instances.

attribute-set
:   devlink

dont-validate
:   ['strict']

do
:   **pre**

    **post**

    **request**
    :   attributes
        :   [`bus-name`, `dev-name`, `port-index`, `region-name`]

    **reply**
    :   attributes
        :   [`bus-name`, `dev-name`, `port-index`, `region-name`]

dump
:   **request**
    :   attributes
        :   [`bus-name`, `dev-name`]

    **reply**
    :   attributes
        :   [`bus-name`, `dev-name`, `port-index`, `region-name`]

### [region-new](devlink.md#id52)

Create region snapshot.

attribute-set
:   devlink

dont-validate
:   ['strict']

flags
:   ['admin-perm']

do
:   **pre**

    **post**

    **request**
    :   attributes
        :   [`bus-name`, `dev-name`, `port-index`, `region-name`, `region-snapshot-id`]

    **reply**
    :   attributes
        :   [`bus-name`, `dev-name`, `port-index`, `region-name`, `region-snapshot-id`]

### [region-del](devlink.md#id53)

Delete region snapshot.

attribute-set
:   devlink

dont-validate
:   ['strict']

flags
:   ['admin-perm']

do
:   **pre**

    **post**

    **request**
    :   attributes
        :   [`bus-name`, `dev-name`, `port-index`, `region-name`, `region-snapshot-id`]

### [region-read](devlink.md#id54)

Read region data.

attribute-set
:   devlink

dont-validate
:   ['dump-strict']

flags
:   ['admin-perm']

dump
:   **request**
    :   attributes
        :   [`bus-name`, `dev-name`, `port-index`, `region-name`, `region-snapshot-id`, `region-direct`, `region-chunk-addr`, `region-chunk-len`]

    **reply**
    :   attributes
        :   [`bus-name`, `dev-name`, `port-index`, `region-name`]

### [port-param-get](devlink.md#id55)

Get port param instances.

attribute-set
:   devlink

dont-validate
:   ['strict', 'dump-strict']

do
:   **pre**

    **post**

    **request**
    :   attributes
        :   [`bus-name`, `dev-name`, `port-index`]

    **reply**
    :   attributes
        :   [`bus-name`, `dev-name`, `port-index`]

dump
:   **reply**
    :   attributes
        :   [`bus-name`, `dev-name`, `port-index`]

### [port-param-set](devlink.md#id56)

Set port param instances.

attribute-set
:   devlink

dont-validate
:   ['strict']

flags
:   ['admin-perm']

do
:   **pre**

    **post**

    **request**
    :   attributes
        :   [`bus-name`, `dev-name`, `port-index`]

### [info-get](devlink.md#id57)

Get device information, like driver name, hardware and firmware versions etc.

attribute-set
:   devlink

dont-validate
:   ['strict', 'dump']

do
:   **pre**

    **post**

    **request**
    :   attributes
        :   [`bus-name`, `dev-name`]

    **reply**
    :   attributes
        :   [`bus-name`, `dev-name`, `info-driver-name`, `info-serial-number`, `info-version-fixed`, `info-version-running`, `info-version-stored`]

dump
:   **reply**
    :   attributes
        :   [`bus-name`, `dev-name`, `info-driver-name`, `info-serial-number`, `info-version-fixed`, `info-version-running`, `info-version-stored`]

### [health-reporter-get](devlink.md#id58)

Get health reporter instances.

attribute-set
:   devlink

dont-validate
:   ['strict']

do
:   **pre**

    **post**

    **request**
    :   attributes
        :   [`bus-name`, `dev-name`, `port-index`, `health-reporter-name`]

    **reply**
    :   attributes
        :   [`bus-name`, `dev-name`, `port-index`, `health-reporter-name`]

dump
:   **request**
    :   attributes
        :   [`bus-name`, `dev-name`, `port-index`]

    **reply**
    :   attributes
        :   [`bus-name`, `dev-name`, `port-index`, `health-reporter-name`]

### [health-reporter-set](devlink.md#id59)

Set health reporter instances.

attribute-set
:   devlink

dont-validate
:   ['strict']

flags
:   ['admin-perm']

do
:   **pre**

    **post**

    **request**
    :   attributes
        :   [`bus-name`, `dev-name`, `port-index`, `health-reporter-name`, `health-reporter-graceful-period`, `health-reporter-auto-recover`, `health-reporter-auto-dump`]

### [health-reporter-recover](devlink.md#id60)

Recover health reporter instances.

attribute-set
:   devlink

dont-validate
:   ['strict']

flags
:   ['admin-perm']

do
:   **pre**

    **post**

    **request**
    :   attributes
        :   [`bus-name`, `dev-name`, `port-index`, `health-reporter-name`]

### [health-reporter-diagnose](devlink.md#id61)

Diagnose health reporter instances.

attribute-set
:   devlink

dont-validate
:   ['strict']

flags
:   ['admin-perm']

do
:   **pre**

    **post**

    **request**
    :   attributes
        :   [`bus-name`, `dev-name`, `port-index`, `health-reporter-name`]

### [health-reporter-dump-get](devlink.md#id62)

Dump health reporter instances.

attribute-set
:   devlink

dont-validate
:   ['dump-strict']

flags
:   ['admin-perm']

dump
:   **request**
    :   attributes
        :   [`bus-name`, `dev-name`, `port-index`, `health-reporter-name`]

    **reply**
    :   attributes
        :   [`fmsg`]

### [health-reporter-dump-clear](devlink.md#id63)

Clear dump of health reporter instances.

attribute-set
:   devlink

dont-validate
:   ['strict']

flags
:   ['admin-perm']

do
:   **pre**

    **post**

    **request**
    :   attributes
        :   [`bus-name`, `dev-name`, `port-index`, `health-reporter-name`]

### [flash-update](devlink.md#id64)

Flash update devlink instances.

attribute-set
:   devlink

dont-validate
:   ['strict']

flags
:   ['admin-perm']

do
:   **pre**

    **post**

    **request**
    :   attributes
        :   [`bus-name`, `dev-name`, `flash-update-file-name`, `flash-update-component`, `flash-update-overwrite-mask`]

### [trap-get](devlink.md#id65)

Get trap instances.

attribute-set
:   devlink

dont-validate
:   ['strict']

do
:   **pre**

    **post**

    **request**
    :   attributes
        :   [`bus-name`, `dev-name`, `trap-name`]

    **reply**
    :   attributes
        :   [`bus-name`, `dev-name`, `trap-name`]

dump
:   **request**
    :   attributes
        :   [`bus-name`, `dev-name`]

    **reply**
    :   attributes
        :   [`bus-name`, `dev-name`, `trap-name`]

### [trap-set](devlink.md#id66)

Set trap instances.

attribute-set
:   devlink

dont-validate
:   ['strict']

flags
:   ['admin-perm']

do
:   **pre**

    **post**

    **request**
    :   attributes
        :   [`bus-name`, `dev-name`, `trap-name`, `trap-action`]

### [trap-group-get](devlink.md#id67)

Get trap group instances.

attribute-set
:   devlink

dont-validate
:   ['strict']

do
:   **pre**

    **post**

    **request**
    :   attributes
        :   [`bus-name`, `dev-name`, `trap-group-name`]

    **reply**
    :   attributes
        :   [`bus-name`, `dev-name`, `trap-group-name`]

dump
:   **request**
    :   attributes
        :   [`bus-name`, `dev-name`]

    **reply**
    :   attributes
        :   [`bus-name`, `dev-name`, `trap-group-name`]

### [trap-group-set](devlink.md#id68)

Set trap group instances.

attribute-set
:   devlink

dont-validate
:   ['strict']

flags
:   ['admin-perm']

do
:   **pre**

    **post**

    **request**
    :   attributes
        :   [`bus-name`, `dev-name`, `trap-group-name`, `trap-action`, `trap-policer-id`]

### [trap-policer-get](devlink.md#id69)

Get trap policer instances.

attribute-set
:   devlink

dont-validate
:   ['strict']

do
:   **pre**

    **post**

    **request**
    :   attributes
        :   [`bus-name`, `dev-name`, `trap-policer-id`]

    **reply**
    :   attributes
        :   [`bus-name`, `dev-name`, `trap-policer-id`]

dump
:   **request**
    :   attributes
        :   [`bus-name`, `dev-name`]

    **reply**
    :   attributes
        :   [`bus-name`, `dev-name`, `trap-policer-id`]

### [trap-policer-set](devlink.md#id70)

Get trap policer instances.

attribute-set
:   devlink

dont-validate
:   ['strict']

flags
:   ['admin-perm']

do
:   **pre**

    **post**

    **request**
    :   attributes
        :   [`bus-name`, `dev-name`, `trap-policer-id`, `trap-policer-rate`, `trap-policer-burst`]

### [health-reporter-test](devlink.md#id71)

Test health reporter instances.

attribute-set
:   devlink

dont-validate
:   ['strict']

flags
:   ['admin-perm']

do
:   **pre**

    **post**

    **request**
    :   attributes
        :   [`bus-name`, `dev-name`, `port-index`, `health-reporter-name`]

### [rate-get](devlink.md#id72)

Get rate instances.

attribute-set
:   devlink

dont-validate
:   ['strict']

do
:   **pre**

    **post**

    **request**
    :   attributes
        :   [`bus-name`, `dev-name`, `port-index`, `rate-node-name`]

    **reply**
    :   attributes
        :   [`bus-name`, `dev-name`, `port-index`, `rate-node-name`]

dump
:   **request**
    :   attributes
        :   [`bus-name`, `dev-name`]

    **reply**
    :   attributes
        :   [`bus-name`, `dev-name`, `port-index`, `rate-node-name`]

### [rate-set](devlink.md#id73)

Set rate instances.

attribute-set
:   devlink

dont-validate
:   ['strict']

flags
:   ['admin-perm']

do
:   **pre**

    **post**

    **request**
    :   attributes
        :   [`bus-name`, `dev-name`, `rate-node-name`, `rate-tx-share`, `rate-tx-max`, `rate-tx-priority`, `rate-tx-weight`, `rate-parent-node-name`]

### [rate-new](devlink.md#id74)

Create rate instances.

attribute-set
:   devlink

dont-validate
:   ['strict']

flags
:   ['admin-perm']

do
:   **pre**

    **post**

    **request**
    :   attributes
        :   [`bus-name`, `dev-name`, `rate-node-name`, `rate-tx-share`, `rate-tx-max`, `rate-tx-priority`, `rate-tx-weight`, `rate-parent-node-name`]

### [rate-del](devlink.md#id75)

Delete rate instances.

attribute-set
:   devlink

dont-validate
:   ['strict']

flags
:   ['admin-perm']

do
:   **pre**

    **post**

    **request**
    :   attributes
        :   [`bus-name`, `dev-name`, `rate-node-name`]

### [linecard-get](devlink.md#id76)

Get line card instances.

attribute-set
:   devlink

dont-validate
:   ['strict']

do
:   **pre**

    **post**

    **request**
    :   attributes
        :   [`bus-name`, `dev-name`, `linecard-index`]

    **reply**
    :   attributes
        :   [`bus-name`, `dev-name`, `linecard-index`]

dump
:   **request**
    :   attributes
        :   [`bus-name`, `dev-name`]

    **reply**
    :   attributes
        :   [`bus-name`, `dev-name`, `linecard-index`]

### [linecard-set](devlink.md#id77)

Set line card instances.

attribute-set
:   devlink

dont-validate
:   ['strict']

flags
:   ['admin-perm']

do
:   **pre**

    **post**

    **request**
    :   attributes
        :   [`bus-name`, `dev-name`, `linecard-index`, `linecard-type`]

### [selftests-get](devlink.md#id78)

Get device selftest instances.

attribute-set
:   devlink

dont-validate
:   ['strict', 'dump']

do
:   **pre**

    **post**

    **request**
    :   attributes
        :   [`bus-name`, `dev-name`]

    **reply**
    :   attributes
        :   [`bus-name`, `dev-name`]

dump
:   **reply**
    :   attributes
        :   [`bus-name`, `dev-name`]

### [selftests-run](devlink.md#id79)

Run device selftest instances.

attribute-set
:   devlink

dont-validate
:   ['strict']

flags
:   ['admin-perm']

do
:   **pre**

    **post**

    **request**
    :   attributes
        :   [`bus-name`, `dev-name`, `selftests`]

### [notify-filter-set](devlink.md#id80)

Set notification messages socket filter.

attribute-set
:   devlink

do
:   **request**
    :   attributes
        :   [`bus-name`, `dev-name`, `port-index`]

## [Definitions](devlink.md#id81)

### [sb-pool-type](devlink.md#id82)

type
:   enum

entries
:   ingress

    egress

### [port-type](devlink.md#id83)

type
:   enum

entries
:   notset

    auto

    eth

    ib

### [port-flavour](devlink.md#id84)

type
:   enum

entries
:   physical

    cpu

    dsa

    pci_pf

    pci_vf

    virtual

    unused

    pci_sf

### [port-fn-state](devlink.md#id85)

type
:   enum

entries
:   inactive

    active

### [port-fn-opstate](devlink.md#id86)

type
:   enum

entries
:   detached

    attached

### [port-fn-attr-cap](devlink.md#id87)

type
:   enum

entries
:   roce-bit

    migratable-bit

    ipsec-crypto-bit

    ipsec-packet-bit

### [rate-type](devlink.md#id88)

type
:   enum

entries
:   leaf

    node

### [sb-threshold-type](devlink.md#id89)

type
:   enum

entries
:   static

    dynamic

### [eswitch-mode](devlink.md#id90)

type
:   enum

entries
:   legacy

    switchdev

### [eswitch-inline-mode](devlink.md#id91)

type
:   enum

entries
:   none

    link

    network

    transport

### [eswitch-encap-mode](devlink.md#id92)

type
:   enum

entries
:   none

    basic

### [dpipe-header-id](devlink.md#id93)

type
:   enum

entries
:   ethernet

    ipv4

    ipv6

### [dpipe-match-type](devlink.md#id94)

type
:   enum

entries
:   field-exact

### [dpipe-action-type](devlink.md#id95)

type
:   enum

entries
:   field-modify

### [dpipe-field-mapping-type](devlink.md#id96)

type
:   enum

entries
:   none

    ifindex

### [resource-unit](devlink.md#id97)

type
:   enum

entries
:   entry

### [reload-action](devlink.md#id98)

type
:   enum

entries
:   driver-reinit

    fw-activate

### [param-cmode](devlink.md#id99)

type
:   enum

entries
:   runtime

    driverinit

    permanent

### [flash-overwrite](devlink.md#id100)

type
:   enum

entries
:   settings-bit

    identifiers-bit

### [trap-action](devlink.md#id101)

type
:   enum

entries
:   drop

    trap

    mirror

### [trap-type](devlink.md#id102)

type
:   enum

entries
:   drop

    exception

    control

## [Attribute sets](devlink.md#id103)

### [devlink](devlink.md#id104)

#### [bus-name (`string`)](devlink.md#id105)

value
:   1

#### [dev-name (`string`)](devlink.md#id106)

#### [port-index (`u32`)](devlink.md#id107)

#### [port-type (`u16`)](devlink.md#id108)

enum
:   port-type

#### [port-desired-type (`u16`)](devlink.md#id109)

#### [port-netdev-ifindex (`u32`)](devlink.md#id110)

#### [port-netdev-name (`string`)](devlink.md#id111)

#### [port-ibdev-name (`string`)](devlink.md#id112)

#### [port-split-count (`u32`)](devlink.md#id113)

#### [port-split-group (`u32`)](devlink.md#id114)

#### [sb-index (`u32`)](devlink.md#id115)

#### [sb-size (`u32`)](devlink.md#id116)

#### [sb-ingress-pool-count (`u16`)](devlink.md#id117)

#### [sb-egress-pool-count (`u16`)](devlink.md#id118)

#### [sb-ingress-tc-count (`u16`)](devlink.md#id119)

#### [sb-egress-tc-count (`u16`)](devlink.md#id120)

#### [sb-pool-index (`u16`)](devlink.md#id121)

#### [sb-pool-type (`u8`)](devlink.md#id122)

enum
:   sb-pool-type

#### [sb-pool-size (`u32`)](devlink.md#id123)

#### [sb-pool-threshold-type (`u8`)](devlink.md#id124)

enum
:   sb-threshold-type

#### [sb-threshold (`u32`)](devlink.md#id125)

#### [sb-tc-index (`u16`)](devlink.md#id126)

#### [sb-occ-cur (`u32`)](devlink.md#id127)

#### [sb-occ-max (`u32`)](devlink.md#id128)

#### [eswitch-mode (`u16`)](devlink.md#id129)

enum
:   eswitch-mode

#### [eswitch-inline-mode (`u16`)](devlink.md#id130)

enum
:   eswitch-inline-mode

#### [dpipe-tables (`nest`)](devlink.md#id131)

nested-attributes
:   dl-dpipe-tables

#### [dpipe-table (`nest`)](devlink.md#id132)

multi-attr
:   True

nested-attributes
:   dl-dpipe-table

#### [dpipe-table-name (`string`)](devlink.md#id133)

#### [dpipe-table-size (`u64`)](devlink.md#id134)

#### [dpipe-table-matches (`nest`)](devlink.md#id135)

nested-attributes
:   dl-dpipe-table-matches

#### [dpipe-table-actions (`nest`)](devlink.md#id136)

nested-attributes
:   dl-dpipe-table-actions

#### [dpipe-table-counters-enabled (`u8`)](devlink.md#id137)

#### [dpipe-entries (`nest`)](devlink.md#id138)

nested-attributes
:   dl-dpipe-entries

#### [dpipe-entry (`nest`)](devlink.md#id139)

multi-attr
:   True

nested-attributes
:   dl-dpipe-entry

#### [dpipe-entry-index (`u64`)](devlink.md#id140)

#### [dpipe-entry-match-values (`nest`)](devlink.md#id141)

nested-attributes
:   dl-dpipe-entry-match-values

#### [dpipe-entry-action-values (`nest`)](devlink.md#id142)

nested-attributes
:   dl-dpipe-entry-action-values

#### [dpipe-entry-counter (`u64`)](devlink.md#id143)

#### [dpipe-match (`nest`)](devlink.md#id144)

multi-attr
:   True

nested-attributes
:   dl-dpipe-match

#### [dpipe-match-value (`nest`)](devlink.md#id145)

multi-attr
:   True

nested-attributes
:   dl-dpipe-match-value

#### [dpipe-match-type (`u32`)](devlink.md#id146)

enum
:   dpipe-match-type

#### [dpipe-action (`nest`)](devlink.md#id147)

multi-attr
:   True

nested-attributes
:   dl-dpipe-action

#### [dpipe-action-value (`nest`)](devlink.md#id148)

multi-attr
:   True

nested-attributes
:   dl-dpipe-action-value

#### [dpipe-action-type (`u32`)](devlink.md#id149)

enum
:   dpipe-action-type

#### [dpipe-value (`binary`)](devlink.md#id150)

#### [dpipe-value-mask (`binary`)](devlink.md#id151)

#### [dpipe-value-mapping (`u32`)](devlink.md#id152)

#### [dpipe-headers (`nest`)](devlink.md#id153)

nested-attributes
:   dl-dpipe-headers

#### [dpipe-header (`nest`)](devlink.md#id154)

multi-attr
:   True

nested-attributes
:   dl-dpipe-header

#### [dpipe-header-name (`string`)](devlink.md#id155)

#### [dpipe-header-id (`u32`)](devlink.md#id156)

enum
:   dpipe-header-id

#### [dpipe-header-fields (`nest`)](devlink.md#id157)

nested-attributes
:   dl-dpipe-header-fields

#### [dpipe-header-global (`u8`)](devlink.md#id158)

#### [dpipe-header-index (`u32`)](devlink.md#id159)

#### [dpipe-field (`nest`)](devlink.md#id160)

multi-attr
:   True

nested-attributes
:   dl-dpipe-field

#### [dpipe-field-name (`string`)](devlink.md#id161)

#### [dpipe-field-id (`u32`)](devlink.md#id162)

#### [dpipe-field-bitwidth (`u32`)](devlink.md#id163)

#### [dpipe-field-mapping-type (`u32`)](devlink.md#id164)

enum
:   dpipe-field-mapping-type

#### [pad (`pad`)](devlink.md#id165)

#### [eswitch-encap-mode (`u8`)](devlink.md#id166)

enum
:   eswitch-encap-mode

#### [resource-list (`nest`)](devlink.md#id167)

nested-attributes
:   dl-resource-list

#### [resource (`nest`)](devlink.md#id168)

multi-attr
:   True

nested-attributes
:   dl-resource

#### [resource-name (`string`)](devlink.md#id169)

#### [resource-id (`u64`)](devlink.md#id170)

#### [resource-size (`u64`)](devlink.md#id171)

#### [resource-size-new (`u64`)](devlink.md#id172)

#### [resource-size-valid (`u8`)](devlink.md#id173)

#### [resource-size-min (`u64`)](devlink.md#id174)

#### [resource-size-max (`u64`)](devlink.md#id175)

#### [resource-size-gran (`u64`)](devlink.md#id176)

#### [resource-unit (`u8`)](devlink.md#id177)

enum
:   resource-unit

#### [resource-occ (`u64`)](devlink.md#id178)

#### [dpipe-table-resource-id (`u64`)](devlink.md#id179)

#### [dpipe-table-resource-units (`u64`)](devlink.md#id180)

#### [port-flavour (`u16`)](devlink.md#id181)

enum
:   port-flavour

#### [port-number (`u32`)](devlink.md#id182)

#### [port-split-subport-number (`u32`)](devlink.md#id183)

#### [param (`nest`)](devlink.md#id184)

nested-attributes
:   dl-param

#### [param-name (`string`)](devlink.md#id185)

#### [param-generic (`flag`)](devlink.md#id186)

#### [param-type (`u8`)](devlink.md#id187)

#### [param-value-cmode (`u8`)](devlink.md#id188)

enum
:   param-cmode

value
:   87

#### [region-name (`string`)](devlink.md#id189)

#### [region-size (`u64`)](devlink.md#id190)

#### [region-snapshots (`nest`)](devlink.md#id191)

nested-attributes
:   dl-region-snapshots

#### [region-snapshot (`nest`)](devlink.md#id192)

nested-attributes
:   dl-region-snapshot

#### [region-snapshot-id (`u32`)](devlink.md#id193)

#### [region-chunks (`nest`)](devlink.md#id194)

nested-attributes
:   dl-region-chunks

#### [region-chunk (`nest`)](devlink.md#id195)

nested-attributes
:   dl-region-chunk

#### [region-chunk-data (`binary`)](devlink.md#id196)

#### [region-chunk-addr (`u64`)](devlink.md#id197)

#### [region-chunk-len (`u64`)](devlink.md#id198)

#### [info-driver-name (`string`)](devlink.md#id199)

#### [info-serial-number (`string`)](devlink.md#id200)

#### [info-version-fixed (`nest`)](devlink.md#id201)

multi-attr
:   True

nested-attributes
:   dl-info-version

#### [info-version-running (`nest`)](devlink.md#id202)

multi-attr
:   True

nested-attributes
:   dl-info-version

#### [info-version-stored (`nest`)](devlink.md#id203)

multi-attr
:   True

nested-attributes
:   dl-info-version

#### [info-version-name (`string`)](devlink.md#id204)

#### [info-version-value (`string`)](devlink.md#id205)

#### [sb-pool-cell-size (`u32`)](devlink.md#id206)

#### [fmsg (`nest`)](devlink.md#id207)

nested-attributes
:   dl-fmsg

#### [fmsg-obj-nest-start (`flag`)](devlink.md#id208)

#### [fmsg-pair-nest-start (`flag`)](devlink.md#id209)

#### [fmsg-arr-nest-start (`flag`)](devlink.md#id210)

#### [fmsg-nest-end (`flag`)](devlink.md#id211)

#### [fmsg-obj-name (`string`)](devlink.md#id212)

#### [fmsg-obj-value-type (`u8`)](devlink.md#id213)

#### [health-reporter (`nest`)](devlink.md#id214)

value
:   114

nested-attributes
:   dl-health-reporter

#### [health-reporter-name (`string`)](devlink.md#id215)

#### [health-reporter-state (`u8`)](devlink.md#id216)

#### [health-reporter-err-count (`u64`)](devlink.md#id217)

#### [health-reporter-recover-count (`u64`)](devlink.md#id218)

#### [health-reporter-dump-ts (`u64`)](devlink.md#id219)

#### [health-reporter-graceful-period (`u64`)](devlink.md#id220)

#### [health-reporter-auto-recover (`u8`)](devlink.md#id221)

#### [flash-update-file-name (`string`)](devlink.md#id222)

#### [flash-update-component (`string`)](devlink.md#id223)

#### [flash-update-status-msg (`string`)](devlink.md#id224)

#### [flash-update-status-done (`u64`)](devlink.md#id225)

#### [flash-update-status-total (`u64`)](devlink.md#id226)

#### [port-pci-pf-number (`u16`)](devlink.md#id227)

#### [port-pci-vf-number (`u16`)](devlink.md#id228)

#### [stats (`nest`)](devlink.md#id229)

nested-attributes
:   dl-attr-stats

#### [trap-name (`string`)](devlink.md#id230)

#### [trap-action (`u8`)](devlink.md#id231)

enum
:   trap-action

#### [trap-type (`u8`)](devlink.md#id232)

enum
:   trap-type

#### [trap-generic (`flag`)](devlink.md#id233)

#### [trap-metadata (`nest`)](devlink.md#id234)

nested-attributes
:   dl-trap-metadata

#### [trap-group-name (`string`)](devlink.md#id235)

#### [reload-failed (`u8`)](devlink.md#id236)

#### [health-reporter-dump-ts-ns (`u64`)](devlink.md#id237)

#### [netns-fd (`u32`)](devlink.md#id238)

#### [netns-pid (`u32`)](devlink.md#id239)

#### [netns-id (`u32`)](devlink.md#id240)

#### [health-reporter-auto-dump (`u8`)](devlink.md#id241)

#### [trap-policer-id (`u32`)](devlink.md#id242)

#### [trap-policer-rate (`u64`)](devlink.md#id243)

#### [trap-policer-burst (`u64`)](devlink.md#id244)

#### [port-function (`nest`)](devlink.md#id245)

nested-attributes
:   dl-port-function

#### [info-board-serial-number (`string`)](devlink.md#id246)

#### [port-lanes (`u32`)](devlink.md#id247)

#### [port-splittable (`u8`)](devlink.md#id248)

#### [port-external (`u8`)](devlink.md#id249)

#### [port-controller-number (`u32`)](devlink.md#id250)

#### [flash-update-status-timeout (`u64`)](devlink.md#id251)

#### [flash-update-overwrite-mask (`bitfield32`)](devlink.md#id252)

enum
:   flash-overwrite

enum-as-flags
:   True

#### [reload-action (`u8`)](devlink.md#id253)

enum
:   reload-action

#### [reload-actions-performed (`bitfield32`)](devlink.md#id254)

enum
:   reload-action

enum-as-flags
:   True

#### [reload-limits (`bitfield32`)](devlink.md#id255)

enum
:   reload-action

enum-as-flags
:   True

#### [dev-stats (`nest`)](devlink.md#id256)

nested-attributes
:   dl-dev-stats

#### [reload-stats (`nest`)](devlink.md#id257)

nested-attributes
:   dl-reload-stats

#### [reload-stats-entry (`nest`)](devlink.md#id258)

multi-attr
:   True

nested-attributes
:   dl-reload-stats-entry

#### [reload-stats-limit (`u8`)](devlink.md#id259)

#### [reload-stats-value (`u32`)](devlink.md#id260)

#### [remote-reload-stats (`nest`)](devlink.md#id261)

nested-attributes
:   dl-reload-stats

#### [reload-action-info (`nest`)](devlink.md#id262)

multi-attr
:   True

nested-attributes
:   dl-reload-act-info

#### [reload-action-stats (`nest`)](devlink.md#id263)

multi-attr
:   True

nested-attributes
:   dl-reload-act-stats

#### [port-pci-sf-number (`u32`)](devlink.md#id264)

#### [rate-type (`u16`)](devlink.md#id265)

enum
:   rate-type

#### [rate-tx-share (`u64`)](devlink.md#id266)

#### [rate-tx-max (`u64`)](devlink.md#id267)

#### [rate-node-name (`string`)](devlink.md#id268)

#### [rate-parent-node-name (`string`)](devlink.md#id269)

#### [region-max-snapshots (`u32`)](devlink.md#id270)

#### [linecard-index (`u32`)](devlink.md#id271)

#### [linecard-state (`u8`)](devlink.md#id272)

#### [linecard-type (`string`)](devlink.md#id273)

#### [linecard-supported-types (`nest`)](devlink.md#id274)

nested-attributes
:   dl-linecard-supported-types

#### [selftests (`nest`)](devlink.md#id275)

value
:   176

nested-attributes
:   dl-selftest-id

#### [rate-tx-priority (`u32`)](devlink.md#id276)

#### [rate-tx-weight (`u32`)](devlink.md#id277)

#### [region-direct (`flag`)](devlink.md#id278)

### [dl-dev-stats](devlink.md#id279)

#### [reload-stats](devlink.md#id280)

#### [remote-reload-stats](devlink.md#id281)

### [dl-reload-stats](devlink.md#id282)

#### [reload-action-info](devlink.md#id283)

### [dl-reload-act-info](devlink.md#id284)

#### [reload-action](devlink.md#id285)

#### [reload-action-stats](devlink.md#id286)

### [dl-reload-act-stats](devlink.md#id287)

#### [reload-stats-entry](devlink.md#id288)

### [dl-reload-stats-entry](devlink.md#id289)

#### [reload-stats-limit](devlink.md#id290)

#### [reload-stats-value](devlink.md#id291)

### [dl-info-version](devlink.md#id292)

#### [info-version-name](devlink.md#id293)

#### [info-version-value](devlink.md#id294)

### [dl-port-function](devlink.md#id295)

#### [hw-addr (`binary`)](devlink.md#id296)

name-prefix
:   devlink-port-function-attr-

value
:   1

#### [state (`u8`)](devlink.md#id297)

enum
:   port-fn-state

#### [opstate (`u8`)](devlink.md#id298)

enum
:   port-fn-opstate

#### [caps (`bitfield32`)](devlink.md#id299)

enum
:   port-fn-attr-cap

enum-as-flags
:   True

### [dl-dpipe-tables](devlink.md#id300)

#### [dpipe-table](devlink.md#id301)

### [dl-dpipe-table](devlink.md#id302)

#### [dpipe-table-name](devlink.md#id303)

#### [dpipe-table-size](devlink.md#id304)

#### [dpipe-table-name](devlink.md#id305)

#### [dpipe-table-size](devlink.md#id306)

#### [dpipe-table-matches](devlink.md#id307)

#### [dpipe-table-actions](devlink.md#id308)

#### [dpipe-table-counters-enabled](devlink.md#id309)

#### [dpipe-table-resource-id](devlink.md#id310)

#### [dpipe-table-resource-units](devlink.md#id311)

### [dl-dpipe-table-matches](devlink.md#id312)

#### [dpipe-match](devlink.md#id313)

### [dl-dpipe-table-actions](devlink.md#id314)

#### [dpipe-action](devlink.md#id315)

### [dl-dpipe-entries](devlink.md#id316)

#### [dpipe-entry](devlink.md#id317)

### [dl-dpipe-entry](devlink.md#id318)

#### [dpipe-entry-index](devlink.md#id319)

#### [dpipe-entry-match-values](devlink.md#id320)

#### [dpipe-entry-action-values](devlink.md#id321)

#### [dpipe-entry-counter](devlink.md#id322)

### [dl-dpipe-entry-match-values](devlink.md#id323)

#### [dpipe-match-value](devlink.md#id324)

### [dl-dpipe-entry-action-values](devlink.md#id325)

#### [dpipe-action-value](devlink.md#id326)

### [dl-dpipe-match](devlink.md#id327)

#### [dpipe-match-type](devlink.md#id328)

#### [dpipe-header-id](devlink.md#id329)

#### [dpipe-header-global](devlink.md#id330)

#### [dpipe-header-index](devlink.md#id331)

#### [dpipe-field-id](devlink.md#id332)

### [dl-dpipe-match-value](devlink.md#id333)

#### [dpipe-match](devlink.md#id334)

#### [dpipe-value](devlink.md#id335)

#### [dpipe-value-mask](devlink.md#id336)

#### [dpipe-value-mapping](devlink.md#id337)

### [dl-dpipe-action](devlink.md#id338)

#### [dpipe-action-type](devlink.md#id339)

#### [dpipe-header-id](devlink.md#id340)

#### [dpipe-header-global](devlink.md#id341)

#### [dpipe-header-index](devlink.md#id342)

#### [dpipe-field-id](devlink.md#id343)

### [dl-dpipe-action-value](devlink.md#id344)

#### [dpipe-action](devlink.md#id345)

#### [dpipe-value](devlink.md#id346)

#### [dpipe-value-mask](devlink.md#id347)

#### [dpipe-value-mapping](devlink.md#id348)

### [dl-dpipe-headers](devlink.md#id349)

#### [dpipe-header](devlink.md#id350)

### [dl-dpipe-header](devlink.md#id351)

#### [dpipe-header-name](devlink.md#id352)

#### [dpipe-header-id](devlink.md#id353)

#### [dpipe-header-global](devlink.md#id354)

#### [dpipe-header-fields](devlink.md#id355)

### [dl-dpipe-header-fields](devlink.md#id356)

#### [dpipe-field](devlink.md#id357)

### [dl-dpipe-field](devlink.md#id358)

#### [dpipe-field-name](devlink.md#id359)

#### [dpipe-field-id](devlink.md#id360)

#### [dpipe-field-bitwidth](devlink.md#id361)

#### [dpipe-field-mapping-type](devlink.md#id362)

### [dl-resource](devlink.md#id363)

#### [resource-name](devlink.md#id364)

#### [resource-id](devlink.md#id365)

#### [resource-size](devlink.md#id366)

#### [resource-size-new](devlink.md#id367)

#### [resource-size-valid](devlink.md#id368)

#### [resource-size-min](devlink.md#id369)

#### [resource-size-max](devlink.md#id370)

#### [resource-size-gran](devlink.md#id371)

#### [resource-unit](devlink.md#id372)

#### [resource-occ](devlink.md#id373)

### [dl-resource-list](devlink.md#id374)

#### [resource](devlink.md#id375)

### [dl-param](devlink.md#id376)

#### [param-name](devlink.md#id377)

#### [param-generic](devlink.md#id378)

#### [param-type](devlink.md#id379)

### [dl-region-snapshots](devlink.md#id380)

#### [region-snapshot](devlink.md#id381)

### [dl-region-snapshot](devlink.md#id382)

#### [region-snapshot-id](devlink.md#id383)

### [dl-region-chunks](devlink.md#id384)

#### [region-chunk](devlink.md#id385)

### [dl-region-chunk](devlink.md#id386)

#### [region-chunk-data](devlink.md#id387)

#### [region-chunk-addr](devlink.md#id388)

### [dl-fmsg](devlink.md#id389)

#### [fmsg-obj-nest-start](devlink.md#id390)

#### [fmsg-pair-nest-start](devlink.md#id391)

#### [fmsg-arr-nest-start](devlink.md#id392)

#### [fmsg-nest-end](devlink.md#id393)

#### [fmsg-obj-name](devlink.md#id394)

### [dl-health-reporter](devlink.md#id395)

#### [health-reporter-name](devlink.md#id396)

#### [health-reporter-state](devlink.md#id397)

#### [health-reporter-err-count](devlink.md#id398)

#### [health-reporter-recover-count](devlink.md#id399)

#### [health-reporter-graceful-period](devlink.md#id400)

#### [health-reporter-auto-recover](devlink.md#id401)

#### [health-reporter-dump-ts](devlink.md#id402)

#### [health-reporter-dump-ts-ns](devlink.md#id403)

#### [health-reporter-auto-dump](devlink.md#id404)

### [dl-attr-stats](devlink.md#id405)

#### [stats-rx-packets (`u64`)](devlink.md#id406)

value
:   0

#### [stats-rx-bytes (`u64`)](devlink.md#id407)

#### [stats-rx-dropped (`u64`)](devlink.md#id408)

### [dl-trap-metadata](devlink.md#id409)

#### [trap-metadata-type-in-port (`flag`)](devlink.md#id410)

value
:   0

#### [trap-metadata-type-fa-cookie (`flag`)](devlink.md#id411)

### [dl-linecard-supported-types](devlink.md#id412)

#### [linecard-type](devlink.md#id413)

### [dl-selftest-id](devlink.md#id414)

#### [flash (`flag`)](devlink.md#id415)
