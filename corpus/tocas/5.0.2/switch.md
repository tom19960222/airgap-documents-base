---
collection: tocas
version: "5.0.2"
title: "指撥開關 - Tocas UI"
source_url: https://github.com/teacat/tocas-docs/blob/e62614c61a3fdb5d75cc5573e66f64dbfdbb7be7/docs/5.0/zh-tw/switch.html
fetched_at: 2025-03-22T01:53:10+08:00
---
```html
<label class="ts-switch">
    <input type="checkbox" checked>
    斷路保護措施
</label>
```

## 狀態

### [停用的](switch.md#disabled)

使指撥開關呈現無法互動、點擊的模樣。

```html
<label class="ts-switch">
    <input type="checkbox" disabled>
    進階模式
</label>
```

## 外觀

### [負面的](switch.md#negative)

表示一個指撥開關可能沒有被啟用。

```html
<label class="ts-switch is-negative">
    <input type="checkbox">
    自動偵測垃圾訊息
</label>
```

### [單獨的](switch.md#solo)

指撥開關如果沒有任何標籤文字，可以將其指定為單獨的開關，藉此來移除多餘的間距。

```html
<label class="ts-switch is-solo">
    <input type="checkbox">
</label>
```

### [尺寸](switch.md#sizes)

更改指撥開關的大小。

```html
<label class="ts-switch is-small">
    <input type="checkbox" checked>
    小型開關
</label>
<label class="ts-switch">
    <input type="checkbox" checked>
    預設開關
</label>
<label class="ts-switch is-large">
    <input type="checkbox" checked>
    大型開關
</label>
```

在尋找相似的元件嗎？

- [核取方塊](checkbox.md)
