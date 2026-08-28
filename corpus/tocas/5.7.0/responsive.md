---
collection: tocas
version: "5.7.0"
title: "響應式設計 - Tocas UI"
source_url: https://github.com/teacat/tocas-docs/blob/ef8248b165f458215fb8f18bb400c4bfba1767fa/docs/5.7/zh-tw/responsive.html
fetched_at: 2026-02-25T00:25:36+08:00
---
## 裝置定義

### [中斷點尺寸](responsive.md#default-breakpoints)

Tocas UI 預設提供四個裝置中斷點。

|  | 狀態指示 | 當螢幕尺寸 .. 時 | 出現時機 |
| --- | --- | --- | --- |
| mobile | 目前 | ≥ 0px 和 ≤ 767px | ⮃ 手機直向握持。 |
| tablet | 目前 | ≥ 768px 和 ≤ 1023px | ⮂ 多數手機的橫向。  ⮃ 平板電腦的直向。 |
| desktop | 目前 | ≥ 1024px 和 ≤ 1279px | ⮂ 平板電腦的橫向。  縮小的瀏覽器視窗。  通常可視為電腦裝置的起始點。 |
| widescreen | 目前 | ≥ 1280px | ⮂ 大型平板電腦的橫向（如：iPad Pro 或 Surface Pro）。  筆記型電腦、桌上型電腦。 |

## 使用方式

### [基本使用](responsive.md#responsive-usage)

將 `中斷點:樣式` 套用到元素上，就能使用響應式功能。

|  | 範例 | 生效時機 |
| --- | --- | --- |
| 中斷點 | `mobile` | 只在「某個中斷點」生效。 |
| 中斷點+ | `mobile+` | 在「某個中斷點」與「以上」生效。 |
| 中斷點- | `tablet-` | 在「某個中斷點」與「以下」生效。 |
| 中斷點-中斷點 | `tablet-widescreen` | 在「某個中斷點」與「某個中斷點」之間生效。 |

```html
<!-- 只在 mobile 套用 is-small -->
<div class="ts-button mobile:is-small"></div>

<!-- 在 tablet, desktop, widescreen 套用 is-small -->
<div class="ts-button tablet+:is-small"></div>
```

### [臨時尺寸](responsive.md#responsive-arbitrary)

透過方括號 `[尺寸]` 取代原本的中斷點名稱，就能使用像 `100px` 或 `450px` 這種臨時尺寸。

|  | 範例 | 生效時機 |
| --- | --- | --- |
| [尺寸+] | `[450px]+` | 在「某個尺寸」與「以上」生效。 |
| [尺寸-] | `[800px]-` | 在「某個尺寸」與「以下」生效。 |
| [尺寸-尺寸] | `[300px-400px]` | 在「某個尺寸」與「某個尺寸」之間生效。 |

```html
<!-- 螢幕在 300px 或以下套用 is-small -->
<div class="ts-button [300px]-:is-small"></div>

<!-- 螢幕在 300px 到 400px 之間套用 is-small -->
<div class="ts-button [300px-400px]:is-small"></div>
```

## 實際應用

### [在 … 時隱藏/顯示元素](responsive.md#responsive-visibility)

在指定中斷點套用 [`.has-hidden`](utilities.md) 就能隱藏元素，善用此功能可以讓元素只在特定裝置顯示。

```html
<!-- 在 tablet, desktop, widescreen 隱藏 -->
<!-- 等同於：只在 mobile 顯示 -->
<div class="ts-badge tablet+:has-hidden">Mobile 📱</div>

<!-- 在 mobile, desktop, widescreen 隱藏 -->
<!-- 等同於：只在 tablet 顯示 -->
<div class="ts-badge mobile:has-hidden desktop+:has-hidden">Tablet 💻</div>

<!-- 在 mobile, tablet, widescreen 隱藏 -->
<!-- 等同於：只在 desktop 顯示 -->
<div class="ts-badge tablet-:has-hidden widescreen:has-hidden">Desktop 🖥️</div>

<!-- 在 mobile, tablet, desktop 隱藏 -->
<!-- 等同於：只在 widescreen 顯示 -->
<div class="ts-badge desktop-:has-hidden">Widescreen 📺</div>
```

### [響應網格系統](responsive.md#responsive-grid)

讓欄位寬度隨著螢幕尺寸變動，但 `mobile` 中斷點設置的樣式**不會**往上沿用，所以你必須指定每個階段的樣式。

```html
<div class="ts-grid">
    <div class="column mobile:is-16-wide tablet+:is-8-wide"></div>
    <div class="column mobile:is-16-wide tablet+:is-8-wide"></div>
    <div class="column mobile:is-16-wide tablet+:is-8-wide"></div>
    <div class="column mobile:is-16-wide tablet+:is-8-wide"></div>
</div>
```

## 進階功能

### [自訂中斷點](responsive.md#responsive-customize)

透過 CSS 變數覆寫、新增 Tocas UI 的中斷點尺寸。新增中斷點時，必須同時指定兩個 CSS 變數：

`--ts-breakpoint-名稱-min`：該中斷點的最小、起始尺寸。

`--ts-breakpoint-名稱-min`：該中斷點的最大、結束尺寸。

套用響應式功能時，Tocas UI 會找離這個元素最近的中斷點定義。

```html
<style type="text/css">
    html {
        /** 建立名為 computer 的中斷點 */
        --ts-breakpoint-computer-min: 768px;
        --ts-breakpoint-computer-max: 1280px;
    }
</style>

<!-- 螢幕在 768px ~ 1280px 之間套用 is-small 樣式 -->
<div class="ts-button computer:is-small"></div>
```

### [基於容器的中斷點](responsive.md#responsive-container-query)

讓元素依據容器的寬度來當作中斷點基準，而非螢幕大小；這也被稱作 Container Query。

在中斷點前面加上 `@` 符號（例如：`@mobile`、`@[400px]+`），元素就會依據最鄰近的 `@container` 容器寬度來做為響應式的判斷依據。

```html
<div class="ts-content @container">
    <!-- 如果 ts-content 的寬度在 300px 或以上就套用 is-small -->
    <div class="ts-button @[300px+]:is-small"></div>
</div>
```
