---
collection: tocas
version: "5.0.2"
title: "輔助樣式 - Tocas UI"
source_url: https://github.com/teacat/tocas-docs/blob/e62614c61a3fdb5d75cc5573e66f64dbfdbb7be7/docs/5.0/zh-tw/utilities.html
fetched_at: 2025-03-22T01:53:10+08:00
---
## 概要

全域輔助樣式的前輟一定是 `has-`，這些樣式可以在所有元件使用。若你需要更多輔助樣式，可以考慮使用 [Tailwind CSS](https://tailwindcss.com/)。

## 使用方式

### [可見度](utilities.md#visibility)

隱藏某個元素，可以搭配[響應式設計](responsive.md)來在某些裝置上隱藏元素。

| 樣式 | 屬性 |
| --- | --- |
| has-invisible | `visibility: hidden;` |
| has-hidden | `display: none;` |
| has-hidden-light | 在亮色主題下會套用 `display: none;` |
| has-hidden-dark | 在暗色主題下會套用 `display: none;` |

### [增加內距](utilities.md#padded)

增加任意元素的內距，在實際應用中並不會看到範例背景色。

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| padding-top | has-top-padded | -small | -large | -big | -huge |
| padding-bottom | has-bottom-padded | -small | -large | -big | -huge |
| padding-left | has-start-padded | -small | -large | -big | -huge |
| padding-right | has-end-padded | -small | -large | -big | -huge |
| padding | has-padded | -small | -large | -big | -huge |
| padding-top padding-bottom | has-vertically-padded | -small | -large | -big | -huge |
| padding-left padding-right | has-horizontally-padded | -small | -large | -big | -huge |
|  | 1rem | 0.5rem | 1.5rem | 3rem | 4.5rem |
| --- | --- | --- | --- | --- | --- |

```html
<div class="has-padded">增加內距。</div>
<div class="has-padded-large">增加更大的內距。</div>
```

### [增加外距](utilities.md#spaced)

增加任意元素的外距，這些樣式還有 `-auto` 可以套用 `auto;`。

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| margin-top | has-top-spaced | -small | -large | -big | -huge |
| margin-bottom | has-bottom-spaced | -small | -large | -big | -huge |
| margin-left | has-start-spaced | -small | -large | -big | -huge |
| margin-right | has-end-spaced | -small | -large | -big | -huge |
| margin | has-spaced | -small | -large | -big | -huge |
| margin-top margin-bottom | has-vertically-spaced | -small | -large | -big | -huge |
| margin-left margin-right | has-horizontally-spaced | -small | -large | -big | -huge |
|  | 1rem | 0.5rem | 1.5rem | 3rem | 4.5rem |
| --- | --- | --- | --- | --- | --- |

### [行距高度](utilities.md#leading)

變更元素的行距高度以便對齊或是以更緊緻的方式呈現而節省空間運用。

| 樣式 | 屬性 |
| --- | --- |
| has-leading-none | `line-height: 1;` |
| has-leading-small | `line-height: 1.4;` |
| has-leading-large | `line-height: 1.9;` |
