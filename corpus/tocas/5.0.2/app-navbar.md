---
collection: tocas
version: "5.0.2"
title: "導航列 - Tocas UI"
source_url: https://github.com/teacat/tocas-docs/blob/e62614c61a3fdb5d75cc5573e66f64dbfdbb7be7/docs/5.0/zh-tw/app-navbar.html
fetched_at: 2025-03-22T01:53:10+08:00
---
```html
<div class="ts-app-navbar is-fluid">
    <a class="item">
        <span class="ts-icon is-user-icon"></span>
        <div class="label">使用者</div>
    </a>
    <a class="item">
        <span class="ts-icon is-house-icon"></span>
        <div class="label">首頁</div>
    </a>
    <a class="item is-active">
        <span class="ts-icon is-newspaper-icon"></span>
        <div class="label">新聞</div>
    </a>
</div>
```

## 概要

通常擺放在畫面下方，如果項目過多則可以改用[側邊導覽](app-sidebar.md)。

使用此元件時必須要有一個被啟用的項目，沒有被啟用的項目會淡化呈現。

## 結構

### [標籤](app-navbar.md#label)

圖示下方可以擺放標籤，但僅能是單行文字。

```html
<div class="ts-app-navbar">
    <a class="item">
        <span class="ts-icon is-magnifying-glass-icon"></span>
        <div class="label">搜尋</div>
    </a>
    <a class="item is-active">
        <span class="ts-icon is-vials-icon"></span>
        <div class="label">實驗區</div>
    </a>
    <a class="item">
        <span class="ts-icon is-atom-icon"></span>
        <div class="label">原子測試</div>
    </a>
</div>
```

## 狀態

### [啟用的](app-navbar.md#active)

表示目前頁面正處於的位置項目。

```html
<div class="ts-app-navbar">
    <a class="item">
        <span class="ts-icon is-star-icon"></span>
        <div class="label">常用聯絡人</div>
    </a>
    <a class="item is-active">
        <span class="ts-icon is-clock-icon"></span>
        <div class="label">近期通話</div>
    </a>
    <a class="item">
        <span class="ts-icon is-users-icon"></span>
        <div class="label">聯絡人</div>
    </a>
</div>
```

### [停用的](app-navbar.md#disabled)

使項目呈現無法互動、點擊的模樣。若項目是超連結，則需套用 `.is-disabled` 樣式。

```html
<div class="ts-app-navbar is-indicated">
    <a class="item">
        <span class="ts-icon is-newspaper-icon"></span>
        <div class="label">刊登啟示</div>
    </a>
    <button class="item" disabled>
        <span class="ts-icon is-list-check-icon"></span>
        <div class="label">未完成項目</div>
    </button>
    <a class="item is-disabled">
        <span class="ts-icon is-handshake-angle-icon"></span>
        <div class="label">請求協助</div>
    </a>
</div>
```

## 外觀

### [標記的](app-navbar.md#indicated)

令啟用的項目以較醒目的方式呈現，而這會讓沒被啟用的項目以正常方式呈現而不會被淡化。

```html
<div class="ts-app-navbar is-indicated">
    <a class="item">
        <span class="ts-icon is-shoe-prints-icon"></span>
        <div class="label">步數</div>
    </a>
    <a class="item is-active">
        <span class="ts-icon is-stopwatch-icon"></span>
        <div class="label">活動分鐘</div>
    </a>
    <a class="item">
        <span class="ts-icon is-heart-icon"></span>
        <div class="label">心律</div>
    </a>
</div>
```

### [無標籤](app-navbar.md#unlabeled)

在這個模式下，所有沒被啟用的項目其標籤都會被隱藏。這可以有效地減短導航列的寬度。

```html
<div class="ts-app-navbar is-unlabeled">
    <a class="item">
        <span class="ts-icon is-image-icon"></span>
        <div class="label">相片</div>
    </a>
    <a class="item is-active">
        <span class="ts-icon is-magnifying-glass-icon"></span>
        <div class="label">搜尋</div>
    </a>
    <a class="item">
        <span class="ts-icon is-users-icon"></span>
        <div class="label">共享</div>
    </a>
    <a class="item">
        <span class="ts-icon is-box-archive-icon"></span>
        <div class="label">彙整</div>
    </a>
</div>
```

### [垂直的](app-navbar.md#vertical)

以上下垂直的方式陳列項目。

```html
<div class="ts-app-navbar is-vertical is-indicated">
    <a class="item">
        <span class="ts-icon is-boxes-stacked-icon"></span>
        <div class="label">服務結構</div>
    </a>
    <a class="item is-active">
        <span class="ts-icon is-database-icon"></span>
        <div class="label">SQL 指令</div>
    </a>
    <a class="item">
        <span class="ts-icon is-scroll-icon"></span>
        <div class="label">常用片段</div>
    </a>
</div>
```

### [流動](app-navbar.md#fluid)

導航列的寬度可以與父容器相同。

```html
<div class="ts-app-navbar is-fluid">
    <a class="item">
        <span class="ts-icon is-house-icon"></span>
        <div class="label">首頁</div>
    </a>
    <a class="item is-active">
        <span class="ts-icon is-flag-icon"></span>
        <div class="label">粉絲專頁</div>
    </a>
    <a class="item">
        <span class="ts-icon is-bell-icon"></span>
        <div class="label">通知</div>
    </a>
</div>
```

### [較密的](app-navbar.md#dense)

變更元件的內距，令元素之間看起來更密集。

```html
<div class="ts-app-navbar is-dense is-indicated">
    <a class="item">
        <span class="ts-icon is-envelope-icon"></span>
        <div class="label">信件</div>
    </a>
    <a class="item is-active">
        <span class="ts-icon is-comment-icon"></span>
        <div class="label">聊天</div>
    </a>
    <a class="item">
        <span class="ts-icon is-users-icon"></span>
        <div class="label">社群</div>
    </a>
</div>
```

在尋找相似的元件嗎？

- [分頁籤](tab.md)
