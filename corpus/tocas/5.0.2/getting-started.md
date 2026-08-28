---
collection: tocas
version: "5.0.2"
title: "開始使用 - Tocas UI"
source_url: https://github.com/teacat/tocas-docs/blob/e62614c61a3fdb5d75cc5573e66f64dbfdbb7be7/docs/5.0/zh-tw/getting-started.html
fetched_at: 2025-03-22T01:53:10+08:00
---
## 安裝與使用

### [引用檔案](getting-started.md#style-installation)

將下列標籤放置於 HTML 中的 `<head> .. </head>` 處即可使用 Tocas UI，你也可以至 [GitHub](https://github.com/teacat/tocas) 下載離線使用。

```html
<!-- 核心：Tocas UI -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/tocas-ui/5.0.2/tocas.min.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/tocas-ui/5.0.2/tocas.min.js"></script>

<!-- 字體：Noto Sans TC -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;500;700&display=swap" rel="stylesheet">

<!-- 啟用：響應式設計 -->
<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
```

## 全域設定

### [亮暗主題](getting-started.md#color-scheme)

Tocas UI 預設會依照使用者的系統設定自動變更亮暗主題，你可以覆寫這個設定。

|  | 說明 |
| --- | --- |
| is-light | 強制使用亮色主題。 |
| is-dark | 強制使用暗色主題。 |

```html
<!-- 指定 `is-dark` 會讓整個頁面使用暗色主題 -->
<html class="is-dark">
```

### [圓角程度](getting-started.md#roundness)

變更元件的圓角程度，令其看起來更尖銳或是圓潤。

|  | 圓角尺寸 | 說明 |
| --- | --- | --- |
| is-sharp | 0rem | 沒有任何圓角且看似生硬。 |
|  | 0.4rem | Tocas UI 的預設圓角設定值。 |
| is-rounded | 1rem | 更有現代感的圓潤邊角。 |

```html
<!-- 指定 `is-sharp` 會移除頁面裡所有元件的圓角 -->
<html class="is-sharp">
```

### [字體大小](getting-started.md#scales)

更改所有元件與頁面的字體大小。

|  | 字體大小 | 說明 |
| --- | --- | --- |
| is-small | 14px | 適用於手機或是行動裝置應用程式。 |
|  | 15px | Tocas UI 的預設尺寸，適合一般網頁。 |
| is-large | 16px | 可用在專注於文字閱讀的網站。 |

```html
<!-- 指定 `is-large` 會讓網頁使用 16px 字體基礎 -->
<html class="is-large">
```
