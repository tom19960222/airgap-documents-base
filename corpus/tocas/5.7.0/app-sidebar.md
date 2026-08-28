---
collection: tocas
version: "5.7.0"
title: "側邊導覽 - Tocas UI"
source_url: https://github.com/teacat/tocas-docs/blob/ef8248b165f458215fb8f18bb400c4bfba1767fa/docs/5.7/zh-tw/app-sidebar.html
fetched_at: 2026-02-25T00:25:36+08:00
---
```html
<div class="ts-app-sidebar">
    <div class="header">
        啟動
    </div>
    <a class="item">
        <span class="ts-icon is-house-icon"></span> 首頁
    </a>
    <div class="header">
        管理
    </div>
    <a class="item is-active">
        <span class="ts-icon is-user-icon"></span> 使用者
    </a>
    <a class="item">
        <span class="ts-icon is-download-icon"></span> 下載檔案
    </a>
</div>
```

## 概要

側邊導覽預設填滿父容器的寬度，建議將其擺放至有固定寬度的區塊。

## 結構

### [標題](app-sidebar.md#header)

以標題文字區分每個功能區塊。

```html
<div class="ts-app-sidebar">
    <div class="header">
        常用
    </div>
    <a class="item">
        <span class="ts-icon is-compass-icon"></span> 探索
    </a>
    <a class="item">
        <span class="ts-icon is-film-icon"></span> 訂閱項目
    </a>
    <div class="header">
        管理
    </div>
    <a class="item">
        <span class="ts-icon is-user-icon"></span> 個人檔案
    </a>
</div>
```

## 狀態

### [啟用的](app-sidebar.md#active)

啟用某個特定項目可以告訴使用者目前頁面屬於哪個功能。

```html
<div class="ts-app-sidebar">
    <div class="header">
        管理
    </div>
    <a class="item">
        <span class="ts-icon is-scissors-icon"></span> 精選剪輯
    </a>
    <a class="item">
        <span class="ts-icon is-star-icon"></span> 收藏項目
    </a>
    <a class="item is-active">
        <span class="ts-icon is-thumbs-up-icon"></span> 讚好影片
    </a>
</div>
```

### [停用的](app-sidebar.md#disabled)

使項目呈現無法互動、點擊的模樣。若項目是超連結，則需套用 `.is-disabled` 樣式。

```html
<div class="ts-app-sidebar">
    <div class="header">
        時間軸
    </div>
    <a class="item">
        <span class="ts-icon is-shoe-prints-icon"></span> 旅程足跡
    </a>
    <button class="item" disabled>
        <span class="ts-icon is-stopwatch-icon"></span> 限時活動
    </button>
    <a class="item is-disabled">
        <span class="ts-icon is-heart-icon"></span> 我的最愛
    </a>
</div>
```

## 外觀

### [較密的](app-sidebar.md#dense)

變更元件的內距，令元素之間看起來更密集。

```html
<div class="ts-app-sidebar is-dense">
    <div class="header">
        系統
    </div>
    <a class="item">
        <span class="ts-icon is-users-icon"></span> 會員管理
    </a>
    <div class="header">
        管理
    </div>
    <a class="item">
        <span class="ts-icon is-file-icon"></span> 檔案總覽
    </a>
    <a class="item is-active">
        <span class="ts-icon is-upload-icon"></span> 上傳新檔
    </a>
</div>
```
