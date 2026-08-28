---
collection: tocas
version: "5.7.0"
title: "表單控制項 - Tocas UI"
source_url: https://github.com/teacat/tocas-docs/blob/ef8248b165f458215fb8f18bb400c4bfba1767fa/docs/5.7/zh-tw/control.html
fetched_at: 2026-02-25T00:25:36+08:00
---
```html
<div class="ts-control">
    <div class="label">使用者名稱</div>
    <div class="content">
        <div class="ts-input">
            <input type="text">
        </div>
    </div>
</div>
```

## 外觀

### [標籤對齊](control.md#label-aligns)

標籤文字可以置起始位置。

```html
<div class="ts-control">
    <div class="label is-start-aligned">年齡</div>
    <div class="content">
        <div class="ts-input">
            <input type="number">
        </div>
    </div>
</div>
```

### [內距增高的](control.md#padded)

若內容欄位有文字或是較矮的元素，需要增高內距才能與一旁的標籤對齊。

```html
<div class="ts-control">
    <div class="label">電子信箱地址</div>
    <div class="content is-padded">
        yamiodymel@example.com
    </div>
</div>
<div class="ts-control">
    <div class="label">封鎖廣告內容</div>
    <div class="content is-padded">
        <label class="ts-switch">
            <input type="checkbox" checked>
            啟用
        </label>
    </div>
</div>
```

### [流動的](control.md#fluid)

讓內容欄位的寬度填滿父容器。

```html
<div class="ts-control">
    <div class="label">暱稱</div>
    <div class="content is-fluid">
        <div class="ts-input">
            <input type="text">
        </div>
    </div>
</div>
```

### [較寬的](control.md#wide)

使整個控制項運用更多的空白，適合較窄的容器。

```html
<div class="ts-control">
    <div class="label">標籤</div>
    <div class="content">
        <div class="ts-input">
            <input type="text">
        </div>
    </div>
</div>
<div class="ts-control is-wide">
    <div class="label">標籤</div>
    <div class="content">
        <div class="ts-input">
            <input type="text">
        </div>
    </div>
</div>
```

### [層疊的](control.md#stacked)

讓標籤與內容改為上下層疊，適合搭配[響應式設計](responsive.md)在行動裝置上層疊所有欄位。

```html
<div class="ts-control is-stacked">
    <div class="label">使用者名稱</div>
    <div class="content">
        <div class="ts-input">
            <input type="text">
        </div>
    </div>
</div>
```

## 組合應用

### [區段分隔線](control.md#composition-divider)

如果有兩個控制項欄位互不相關，可以考慮透過區段分隔線將其分開。

```html
<div class="ts-wrap is-vertical">
    <div class="ts-control">
        <div class="label">使用者名稱</div>
        <div class="content">
            <div class="ts-input">
                <input type="text">
            </div>
        </div>
    </div>
    <div class="ts-control">
        <div class="label">密碼</div>
        <div class="content">
            <div class="ts-input">
                <input type="password">
            </div>
        </div>
    </div>
    <div class="ts-divider"></div>
    <div class="ts-control">
        <div class="label">行銷通知</div>
        <div class="content is-padded">
            <label class="ts-switch">
                <input type="checkbox" checked>
                我想接收到更多的電子信箱通知。
            </label>
        </div>
    </div>
</div>
```

### [特別區塊](control.md#composition-block)

透過[內容區塊](content.md)點綴也能讓某個控制項看起來像一個獨立的邏輯區塊。

```html
<div class="ts-wrap is-vertical">
    <div class="ts-control">
        <div class="label">真實姓名</div>
        <div class="content">
            <div class="ts-input">
                <input type="text">
            </div>
        </div>
    </div>
    <div class="ts-divider"></div>
    <div class="ts-control">
        <div class="label">危險地區</div>
        <div class="content">
            <div class="ts-content is-rounded is-secondary is-padded">
                <button class="ts-button is-outlined is-negative">
                    移除使用者
                </button>
                <div class="ts-text is-description has-top-spaced-small">
                    注意，你將無法復原這項行為。
                </div>
            </div>
        </div>
    </div>
</div>
```

## 樣式變數

|  | 說明 | 預設值 | 目標 |
| --- | --- | --- | --- |
| --label-width | 標籤欄位的寬度。 | `220px` | `.ts-control` |

在尋找相似的元件嗎？

- [網格系統](grid.md)
