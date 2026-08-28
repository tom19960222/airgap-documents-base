---
collection: tocas
version: "5.7.0"
title: "工具提示 - Tocas UI"
source_url: https://github.com/teacat/tocas-docs/blob/ef8248b165f458215fb8f18bb400c4bfba1767fa/docs/5.7/zh-tw/tooltip.html
fetched_at: 2026-02-25T00:25:36+08:00
---
```html
<button class="ts-button is-icon" data-tooltip="收藏">
    <span class="ts-icon is-heart-icon"></span>
</button>
```

## 概要

當使用者的游標移入、聚焦在有 `[data-tooltip]` 屬性的元素，就會顯示工具提示訊息。

## 組合應用

### [輸入欄位提示](tooltip.md#composition-input)

在[輸入欄位](input.md)指定焦點觸發，就能在使用者輸入文字時提示相關規則。

```html
<div class="ts-input is-start-icon" data-tooltip="使用者帳號長度必須在 6 到 24 個字之間。" data-trigger="focus" data-position="bottom-start">
    <span class="ts-icon is-user-icon"></span>
    <input type="text" placeholder="使用者帳號">
</div>
```

### [說明圖示](tooltip.md#composition-info)

帶有 `[tabindex]` 屬性的文字元素能被聚焦，這樣觸控螢幕的使用者就能點擊圖示來開啟工具提示。

```html
這個建築缺少資金 <span class="ts-icon is-circle-question-icon" data-tooltip="你必須分配財政預算才能啟動這項專案。" data-trigger="focus" tabindex="0"><span>
```

## 屬性設定

|  | 說明 | 預設值 |
| --- | --- | --- |
| [data-position] | 工具提示出現時的偏好位置。   - `top` - `top-start` - `top-end` - `bottom` - `bottom-start` - `bottom-end` | `bottom` |
| [data-trigger] | 工具提示被觸發的方式，  使用空白分隔多個觸發方式，如：`hover focus`。   - `hover` 是游標移入時觸發（觸控、行動裝置無作用）。 - `focus` 是取得焦點時觸發，適合用於輸入欄位。 | `hover` |
| [data-delay] | 工具提示從觸發到顯示的延遲時間，單位為毫秒。  設為 `0` 表示立即觸發，`1000` 則是 1 秒。 | `200` |
| [data-html] | 工具提示的文字是否能顯示 HTML 內容，設為 `true` 表示支援。 | `false` |
