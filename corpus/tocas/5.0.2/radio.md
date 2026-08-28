---
collection: tocas
version: "5.0.2"
title: "單選方塊 - Tocas UI"
source_url: https://github.com/teacat/tocas-docs/blob/e62614c61a3fdb5d75cc5573e66f64dbfdbb7be7/docs/5.0/zh-tw/radio.html
fetched_at: 2025-03-22T01:53:10+08:00
---
```html
<label class="ts-radio">
    <input name="eat" type="radio" checked>
    早餐
</label>
```

## 狀態

### [停用的](radio.md#disabled)

使單選方塊呈現無法互動、點擊的模樣。

```html
<label class="ts-radio">
    <input name="linux" type="radio" disabled>
    Arch Linux
</label>
```

## 外觀

### [負面的](radio.md#negative)

表示一個單選方塊可能沒有被選取。

```html
<label class="ts-radio is-negative">
    <input name="love" type="radio">
    愛情摩天輪
</label>
```

### [單獨的](radio.md#solo)

單選方塊如果沒有任何標籤文字，可以將其指定為單獨的單選方塊，藉此來移除多餘的間距。

```html
<label class="ts-radio is-solo">
    <input name="solo" type="radio">
</label>
```

### [尺寸](radio.md#sizes)

更改選項按鈕的大小。

```html
<label class="ts-radio is-small">
    <input name="size" type="radio" checked>
    小型選項
</label>
<label class="ts-radio">
    <input name="size" type="radio">
    預設選項
</label>
<label class="ts-radio is-large">
    <input name="size" type="radio">
    大型選項
</label>
```

## 組合應用

### [鄰近選項按鈕](radio.md#composition-radios)

透過[間隔容器](wrap.md)元件能讓核取方塊以左右、上下排列並保持一定的間距。

```html
<div class="ts-wrap is-vertical">
    <div class="ts-text is-label">性別</div>
    <div class="ts-wrap">
        <label class="ts-radio">
            <input name="gender" type="radio" checked>
            男性
        </label>
        <label class="ts-radio">
            <input name="gender" type="radio">
            女性
        </label>
        <label class="ts-radio">
            <input name="gender" type="radio">
            其它
        </label>
    </div>
    <div class="ts-text is-label">來電狀態</div>
    <div class="ts-wrap is-vertical is-compact">
        <label class="ts-radio">
            <input name="ring" type="radio" checked>
            響鈴
        </label>
        <label class="ts-radio">
            <input name="ring" type="radio">
            震動
        </label>
        <label class="ts-radio">
            <input name="ring" type="radio">
            靜音
        </label>
    </div>
</div>
```

在尋找相似的元件嗎？

- [核取方塊](checkbox.md)
- [項目切換](selection.md)
