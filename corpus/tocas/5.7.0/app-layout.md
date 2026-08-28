---
collection: tocas
version: "5.7.0"
title: "格局劃分 - Tocas UI"
source_url: https://github.com/teacat/tocas-docs/blob/ef8248b165f458215fb8f18bb400c4bfba1767fa/docs/5.7/zh-tw/app-layout.html
fetched_at: 2026-02-25T00:25:36+08:00
---
```html
<div class="ts-app-layout is-horizontal">
    <div class="cell">
        <div class="ts-content">側邊欄</div>
    </div>
    <div class="cell is-fluid is-vertical">
        <div class="cell">
            <div class="ts-content">頂部欄</div>
        </div>
        <div class="cell">
            <div class="ts-content">內容欄</div>
        </div>
    </div>
</div>
```

## 概要

通常用於規劃單頁應用程式的主要格局，預設會以 `100%` 的寬高填滿父容器。

格局劃分經常與[側邊導覽](app-sidebar.md)和[導航列](app-navbar.md)元件一同使用。

## 外觀

### [水平排列的](app-layout.md#horizontal)

格局內的子欄位會依照左右排列。

```html
<div class="ts-app-layout is-horizontal">
    <div class="cell is-fluid">
        <div class="ts-content">左</div>
    </div>
    <div class="cell is-fluid">
        <div class="ts-content">中</div>
    </div>
    <div class="cell is-fluid">
        <div class="ts-content">右</div>
    </div>
</div>
```

### [垂直排列的](app-layout.md#vertical)

格局內的子欄位會依照上下排列。

```html
<div class="ts-app-layout is-vertical">
    <div class="cell">
        <div class="ts-content">上</div>
    </div>
    <div class="cell">
        <div class="ts-content">中</div>
    </div>
    <div class="cell">
        <div class="ts-content">下</div>
    </div>
</div>
```

### [全螢幕的](app-layout.md#fullscreen)

使格局劃分貼滿整個螢幕，而不只是父容器。

```html
<div class="ts-app-layout is-horizontal is-fullscreen">
    <div class="cell">
        <div class="ts-content">欄位</div>
    </div>
</div>
```

## 欄位外觀

### [流動的](app-layout.md#fluid-cell)

預設的欄位寬度會以其最小內容為主，若要某個欄位填滿剩餘空間則需使用此樣式。

```html
<div class="ts-app-layout is-horizontal">
    <div class="cell">
        <div class="ts-content">一般欄位</div>
    </div>
    <div class="cell is-fluid">
        <div class="ts-content">流動欄位</div>
    </div>
</div>
```

### [水平排列的](app-layout.md#horizontal-cell)

欄位裡的巢狀子欄位會依照左右排列。

```html
<div class="ts-app-layout is-vertical">
    <div class="cell">
        <div class="ts-content">上</div>
    </div>
    <div class="cell is-horizontal">
        <div class="cell is-fluid">
            <div class="ts-content">左</div>
        </div>
        <div class="cell is-fluid">
            <div class="ts-content">中</div>
        </div>
        <div class="cell is-fluid">
            <div class="ts-content">右</div>
        </div>
    </div>
</div>
```

### [垂直排列的](app-layout.md#vertical-cell)

欄位裡的巢狀子欄位會依照上下排列。

```html
<div class="ts-app-layout is-horizontal">
    <div class="cell">
        <div class="ts-content">左</div>
    </div>
    <div class="cell is-vertical is-fluid">
        <div class="cell">
            <div class="ts-content">上</div>
        </div>
        <div class="cell">
            <div class="ts-content">中</div>
        </div>
        <div class="cell">
            <div class="ts-content">下</div>
        </div>
    </div>
</div>
```

### [可捲動的](app-layout.md#scrollable-cell)

使其中一個欄位在內容過長時可以上下捲動其捲軸。

```html
<div class="ts-app-layout is-vertical" style="height: 260px">
    <div class="cell">
        <div class="ts-content">頁頭</div>
    </div>
    <div class="cell is-scrollable is-fluid">
        <div class="ts-content">
            <p>Fusce non enim egestas, lobortis diam et, congue felis.</p>
            <p>Rhoncus est sed laoreet facilisis. Suspendisse ante odio,</p>
            <p>pulvinar non nulla sed, consequat lacinia risus.</p>
            <p>Aliquam mollis pulvinar lorem sed efficitur.</p>
        </div>
    </div>
    <div class="cell">
        <div class="ts-content">頁腳</div>
    </div>
</div>
```

### [次要的](app-layout.md#secondary-cell)

其次的背景色調令使用者知道這不是內容主體。

```html
<div class="ts-app-layout is-horizontal">
    <div class="cell is-secondary">
        <div class="ts-content">側邊欄</div>
    </div>
    <div class="cell is-fluid">
        <div class="ts-content">內容欄</div>
    </div>
</div>
```

### [不重要的](app-layout.md#tertiary-cell)

最不重要的背景色能夠使主體突出。

```html
<div class="ts-app-layout is-horizontal">
    <div class="cell">
        <div class="ts-content">側邊欄</div>
    </div>
    <div class="cell is-tertiary is-fluid">
        <div class="ts-content">
            <div class="ts-box">
                <div class="ts-content">
                    早安，我的朋友！
                </div>
            </div>
        </div>
    </div>
</div>
```

## 組合應用

### [單頁應用程式](app-layout.md#composition-app)

透過搭配[側邊導覽](app-sidebar.md)和[導航列](app-navbar.md)就能夠很輕鬆地做出一個單頁應用程式的框架。

```html
<div class="ts-app-layout is-horizontal">
    <div class="cell" style="width: 245px">
        <div class="ts-content">
            <div class="ts-header is-big is-heavy">
                TEACAT DEVELOPERS
            </div>
            <div class="ts-text is-description is-heavy">
                VERSION 1.3.4
            </div>
        </div>
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
            <div class="header">
                系統
            </div>
            <a class="item">
                <span class="ts-icon is-gears-icon"></span> 偏好設定
            </a>
        </div>
        <div class="ts-content">
            <button class="ts-button is-outlined is-fluid">
                登出
            </button>
        </div>
    </div>
    <div class="cell is-fluid is-vertical">
        <div class="cell is-fluid is-secondary"></div>
        <div class="cell">
            <div class="ts-content">
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
            </div>
        </div>
    </div>
</div>
```

在尋找相似的元件嗎？

- [網格系統](grid.md)
