---
collection: tocas
version: "5.7.0"
title: "導覽標記 - Tocas UI"
source_url: https://github.com/teacat/tocas-docs/blob/ef8248b165f458215fb8f18bb400c4bfba1767fa/docs/5.7/zh-tw/breadcrumb.html
fetched_at: 2026-02-25T00:25:36+08:00
---
```html
<div class="ts-breadcrumb">
    <a class="item">映画</a>
    <a class="item">受賞作</a>
    <a class="item is-active">聲の形</a>
</div>
```

## 狀態

### [啟用的](breadcrumb.md#active)

表示目前正處於的位置。

```html
<div class="ts-breadcrumb">
    <a class="item">
        <span class="ts-icon is-house-icon"></span>
    </a>
    <a class="item">
        <span class="ts-icon is-users-icon is-end-spaced"></span>會員管理
    </a>
    <a class="item is-active">
        建立使用者
    </a>
</div>
```

## 外觀

### [自訂圖示的](breadcrumb.md#customized)

自訂導覽標記的分隔圖示。

```html
<div class="ts-breadcrumb is-customized">
    <a class="item">網站</a>
    <div class="divider">
        <span class="ts-icon is-caret-right-icon"></span>
    </div>
    <a class="item">註冊程序</a>
    <div class="divider">
        <span class="ts-icon is-caret-right-icon"></span>
    </div>
    <a class="item">個人資料</a>
</div>
```

### [箭頭的](breadcrumb.md#chevroned)

以箭頭分隔項目。

```html
<div class="ts-breadcrumb is-chevroned">
    <a class="item">線上購物</a>
    <a class="item">24H 送達</a>
    <a class="item">智慧型手機</a>
</div>
```

### [連字符的](breadcrumb.md#hyphenated)

以基本的連字符號分隔項目。

```html
<div class="ts-breadcrumb is-hyphenated">
    <a class="item">無線滑鼠</a>
    <a class="item">快速響應</a>
    <a class="item">特價下殺</a>
</div>
```

### [階段的](breadcrumb.md#stepped)

讓導覽標記有階段性的感覺，這會讓非啟用的項目全部淡化呈現。

```html
<div class="ts-breadcrumb is-chevroned is-stepped">
    <a class="item">聯絡我們</a>
    <a class="item">技術問題</a>
    <a class="item is-active">表單</a>
</div>
```

### [尺寸](breadcrumb.md#sizes)

更改導覽標記的大小。

```html
<div class="ts-breadcrumb is-small">
    <a class="item">使用文件</a>
    <a class="item">程式開發</a>
    <a class="item">Golang</a>
</div>
<div class="ts-breadcrumb">
    <a class="item">使用文件</a>
    <a class="item">程式開發</a>
    <a class="item">Golang</a>
</div>
<div class="ts-breadcrumb is-large">
    <a class="item">使用文件</a>
    <a class="item">程式開發</a>
    <a class="item">Golang</a>
</div>
```

## 組合應用

### [區塊導覽標記](breadcrumb.md#composition-block)

搭配[箱型容器](box.md)呈現出一個區塊導覽標記。

```html
<div class="ts-box">
    <div class="ts-content is-secondary">
        <div class="ts-breadcrumb is-chevroned">
            <a class="item">電影</a>
            <a class="item">科幻與冒險</a>
            <a class="item">星際效應</a>
        </div>
    </div>
</div>
```
