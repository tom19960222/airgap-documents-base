---
collection: tocas
version: "5.0.2"
title: "關閉按鈕 - Tocas UI"
source_url: https://github.com/teacat/tocas-docs/blob/e62614c61a3fdb5d75cc5573e66f64dbfdbb7be7/docs/5.0/zh-tw/close.html
fetched_at: 2025-03-22T01:53:10+08:00
---
```html
<button class="ts-close"></button>
```

## 狀態

### [停用的](close.md#disabled)

使關閉按鈕呈現無法互動、點擊的模樣。若關閉按鈕是超連結，則需套用 `.is-disabled` 樣式。

```html
<button class="ts-close" disabled></button>
<a class="ts-close is-disabled"></a>
```

## 外觀

### [次要的](close.md#secondary)

較不顯眼的樣式。

```html
<button class="ts-close is-secondary"></button>
```

### [不重要的](close.md#tertiary)

可有可無的樣式。

```html
<button class="ts-close is-tertiary"></button>
```

### [圓角的](close.md#rounded)

使按鈕的四個角落都變得稍微有點圓角修飾。

```html
<button class="ts-close is-rounded"></button>
```

### [尺寸](close.md#sizes)

更改關閉按鈕的大小。

```html
<button class="ts-close is-small"></button>
<button class="ts-close"></button>
<button class="ts-close is-large"></button>
<button class="ts-close is-big"></button>
```

### [間隔的](close.md#spaced)

在前或後新增間隔以避免與其他元件相鄰太近。

```html
解決 Docker Alpine 與 Puppeteer 的 Error <button class="ts-close is-start-spaced"></button>
<button class="ts-close is-end-spaced"></button> 讓 NextCloud 支援影片縮圖預覽
羅技電競滑鼠 G603 <button class="ts-close is-spaced"></button> 和 G304 的心得
```

## 組合應用

### [選項移除](close.md#composition-chip)

在[關聯標籤](chip.md)裡可以擺放關閉按鈕，看起來就像是能被刪除的選項。

```html
<div class="ts-chip is-circular">
    卡莉絲伊繁星
    <button class="ts-close"></button>
</div>
<div class="ts-chip is-circular is-outlined">
    雷莉雅
    <button class="ts-close is-secondary"></button>
</div>
```

### [表格](close.md#composition-table)

放置在[表格](table.md)裡面可以讓使用者逐行刪除。

```html
<div class="ts-box">
    <table class="ts-table">
        <thead>
            <tr>
                <th class="is-collapsed"></th>
                <th>說明項目</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>
                    <button class="ts-close is-secondary"></button>
                </td>
                <td>多國語元支援的函式庫，協助網站跨國交際。</td>
            </tr>
            <tr>
                <td>
                    <button class="ts-close is-secondary"></button>
                </td>
                <td>協助圖像處理的類別，必須要安裝 Imagick。</td>
            </tr>
            <tr>
                <td>
                    <button class="ts-close is-secondary"></button>
                </td>
                <td>一個基於 HTML5 的遊戲引擎。</td>
            </tr>
        </tbody>
    </table>
</div>
```

在尋找相似的元件嗎？

- [按鈕](button.md)
