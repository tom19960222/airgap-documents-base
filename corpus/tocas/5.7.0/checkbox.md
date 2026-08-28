---
collection: tocas
version: "5.7.0"
title: "核取方塊 - Tocas UI"
source_url: https://github.com/teacat/tocas-docs/blob/ef8248b165f458215fb8f18bb400c4bfba1767fa/docs/5.7/zh-tw/checkbox.html
fetched_at: 2026-02-25T00:25:36+08:00
---
```html
<label class="ts-checkbox">
    <input type="checkbox" checked>
    蘋果
</label>
```

## 狀態

### [停用的](checkbox.md#disabled)

使核取方塊呈現無法互動、點擊的模樣。

```html
<label class="ts-checkbox">
    <input type="checkbox" disabled>
    記住我的密碼
</label>
```

### [不定的](checkbox.md#indeterminate)

讓勾選狀態呈現模稜兩可，表示群組裡同時有已勾選、未被勾選的項目。

```html
<label class="ts-checkbox is-indeterminate">
    <input type="checkbox" checked>
    所有檔案
</label>
<div class="ts-content is-dense">
    <div class="ts-wrap is-vertical is-compact">
        <label class="ts-checkbox">
            <input type="checkbox" checked>
            影片
        </label>
        <label class="ts-checkbox">
            <input type="checkbox">
            文件
        </label>
        <label class="ts-checkbox">
            <input type="checkbox" checked>
            音樂
        </label>
    </div>
</div>
```

## 外觀

### [負面的](checkbox.md#negative)

表示一個核取方塊可能沒有被勾選。

```html
<label class="ts-checkbox is-negative">
    <input type="checkbox">
    我同意使用者規範。
</label>
```

### [單獨的](checkbox.md#solo)

核取方塊如果沒有任何標籤文字，可以將其指定為單獨的核取方塊，藉此來移除多餘的間距。

```html
<label class="ts-checkbox is-solo">
    <input type="checkbox">
</label>
```

### [尺寸](checkbox.md#sizes)

更改核取方塊的大小。

```html
<label class="ts-checkbox is-small">
    <input type="checkbox" checked>
    小型選項
</label>
<label class="ts-checkbox">
    <input type="checkbox">
    預設選項
</label>
<label class="ts-checkbox is-large">
    <input type="checkbox">
    大型選項
</label>
```

## 組合應用

### [鄰近核取方塊](checkbox.md#composition-checkboxes)

透過[間隔容器](wrap.md)元件能讓核取方塊以左右、上下排列並保持一定的間距。

```html
<div class="ts-wrap is-vertical">
    <div class="ts-text is-label">持有狀態</div>
    <div class="ts-wrap">
        <label class="ts-checkbox">
            <input type="checkbox" checked>
            已售出
        </label>
        <label class="ts-checkbox">
            <input type="checkbox">
            未販售
        </label>
        <label class="ts-checkbox">
            <input type="checkbox">
            空投限定
        </label>
    </div>
    <div class="ts-text is-label">寵物屬性</div>
    <div class="ts-wrap is-vertical is-compact">
        <label class="ts-checkbox">
            <input type="checkbox" checked>
            火
        </label>
        <label class="ts-checkbox">
            <input type="checkbox">
            水
        </label>
        <label class="ts-checkbox">
            <input type="checkbox">
            土
        </label>
    </div>
</div>
```

在尋找相似的元件嗎？

- [單選方塊](radio.md)
- [項目切換](selection.md)
