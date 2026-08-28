---
collection: tocas
version: "5.7.0"
title: "主題色系 - Tocas UI"
source_url: https://github.com/teacat/tocas-docs/blob/ef8248b165f458215fb8f18bb400c4bfba1767fa/docs/5.7/zh-tw/colors.html
fetched_at: 2026-02-25T00:25:36+08:00
---
## 色票系統

### [動態顏色](colors.md#dynamic-colors)

Tocas UI 使用動態色調，會依據使用者系統的亮暗主題設定而有所變化。善用這些 CSS 變數可以協助你應付兩種不同主題的介面。

|  | gray 目前 | gray 反色 | primary | warning | positive | negative |
| --- | --- | --- | --- | --- | --- | --- |
| ts-x-50 |  |  |  |  |  |  |
| ts-x-75 |  |  |  |  |  |  |
| ts-x-100 |  |  |  |  |  |  |
| ts-x-200 |  |  |  |  |  |  |
| ts-x-300 |  |  |  |  |  |  |
| ts-x-400 |  |  |  |  |  |  |
| ts-x-500 |  |  |  |  |  |  |
| ts-x-600 |  |  |  |  |  |  |
| ts-x-700 |  |  |  |  |  |  |
| ts-x-800 |  |  |  |  |  |  |
| ts-x-900 |  |  |  |  |  |  |

```html
<div style="color: var(--ts-gray-300)">這樣套用 CSS 變數作為顏色</div>
```

### [靜態顏色](colors.md#static-colors)

靜態顏色不會在亮暗主題變更時而有所變化。

|  | light-gray | dark-gray |
| --- | --- | --- |
| ts-x-50 |  |  |
| ts-x-75 |  |  |
| ts-x-100 |  |  |
| ts-x-200 |  |  |
| ts-x-300 |  |  |
| ts-x-400 |  |  |
| ts-x-500 |  |  |
| ts-x-600 |  |  |
| ts-x-700 |  |  |
| ts-x-800 |  |  |
| ts-x-900 |  |  |

```html
<div style="color: var(--ts-light-gray-300)">這樣套用 CSS 變數作為顏色</div>
```

## 輔助樣式

因為這些樣式可以套用在任何元素，所以命名開頭一定是 `has-`；相關說明請參閱[輔助樣式](utilities.md)頁面。

### [指定反色](colors.md#inverted-scheme)

使該元素的色調與目前全域色系相反。亮色主題中的反色是暗色，反之亦然。

```html
<div class="ts-box has-inverted" style="color: var(--ts-gray-800)">
    <div class="ts-content">
        在亮色主題中，這個元素會是黑色的；在暗色主題中，這個元素會是白色的。
    </div>
</div>
```

### [強制色系](colors.md#force-scheme)

覆寫某個元素的色系而不受使用者系統設定的影響。

```html
<div class="ts-box has-dark" style="color: var(--ts-gray-800)">
    <div class="ts-content">
        這個元素不論是在什麼環境，都一定是暗色的。
    </div>
</div>
<div class="ts-box has-light" style="color: var(--ts-gray-800)">
    <div class="ts-content">
        這個元素不論是在什麼環境，都一定是亮色的。
    </div>
</div>
```
