---
collection: tocas
version: "5.7.0"
title: "頂部列 - Tocas UI"
source_url: https://github.com/teacat/tocas-docs/blob/ef8248b165f458215fb8f18bb400c4bfba1767fa/docs/5.7/zh-tw/app-topbar.html
fetched_at: 2026-02-25T00:25:36+08:00
---
```html
<div class="ts-app-topbar">
    <div class="start">
        <div class="item is-text">應用程式</div>
    </div>
    <div class="end">
        <button class="item">
            <span class="ts-icon is-magnifying-glass-icon"></span>
        </button>
        <button class="item">
            <span class="ts-icon is-ellipsis-vertical-icon"></span>
        </button>
    </div>
</div>
```

## 概要

通常被擺放在應用程式的最上方，可與[格局劃分](app-layout.md)一起使用。

## 結構

### [區塊](app-topbar.md#positions)

頂部列被劃分為 `start`（起始）、`center`（中間）和 `end`（尾端）三個區塊，可以用來擺放不同內容。

```html
<div class="ts-app-topbar">
    <div class="start">
        <button class="item">
            <span class="ts-icon is-chevron-left-icon"></span>
        </button>
    </div>
    <div class="center">
        <div class="item is-text">我的相簿</div>
    </div>
    <div class="end">
        <button class="item">
            <span class="ts-icon is-magnifying-glass-icon"></span>
        </button>
        <button class="item">
            <span class="ts-icon is-ellipsis-vertical-icon"></span>
        </button>
    </div>
</div>
```

### [文字項目](app-topbar.md#text-item)

專門呈現文字的項目，通常用以擺放應用程式的標題名稱。

```html
<div class="ts-app-topbar">
    <div class="start">
        <div class="item is-text">檢視 PDF 文件</div>
    </div>
    <div class="end">
        <button class="item">
            <span class="ts-icon is-circle-question-icon"></span>
        </button>
    </div>
</div>
```

### [內容](app-topbar.md#content)

頂部列可以擺放額外的內容或選單。

```html
<div class="ts-app-topbar">
    <div class="start">
        <button class="item">
            <span class="ts-icon is-arrow-left-icon"></span>
        </button>
    </div>
    <div class="end">
        <button class="item">
            <span class="ts-icon is-magnifying-glass-icon"></span>
        </button>
        <button class="item">
            <span class="ts-icon is-ellipsis-vertical-icon"></span>
        </button>
    </div>
    <div class="content">
        <div class="ts-header is-large">我的檔案</div>
    </div>
</div>
```

## 組合應用

### [功能選單](app-topbar.md#composition-dropdown)

使用[彈出式選單](dropdown.md)讓尾端的額外功能選單起作用。

```html
<div class="ts-app-topbar">
    <div class="start">
        <div class="item is-text">遊戲存檔修改器</div>
    </div>
    <div class="end">
        <button class="item" data-dropdown="dropdown">
            <span class="ts-icon is-ellipsis-vertical-icon"></span>
        </button>
    </div>
</div>
<div class="ts-dropdown" id="dropdown" data-position="bottom-end">
    <button class="item">檢查最新版本</button>
    <button class="item">使用說明</button>
    <button class="item">關於版本</button>
</div>
```
