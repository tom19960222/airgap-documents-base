---
collection: tocas
version: "5.7.0"
title: "彈出內容 - Tocas UI"
source_url: https://github.com/teacat/tocas-docs/blob/ef8248b165f458215fb8f18bb400c4bfba1767fa/docs/5.7/zh-tw/popover.html
fetched_at: 2026-02-25T00:25:36+08:00
---
```html
<button class="ts-button" popovertarget="popup">
    打開彈出內容 ✨
</button>
<div class="ts-popover" id="popup" popover>
    <div class="ts-content">
        任何人都應該有不受拘束的創作自由，<br>
        這也是我們最致力發展的目標。
    </div>
</div>
```

## 概要

彈出內容使用瀏覽器原生 [Popover API](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API)。彈出內容顯示時，會自動附著在對應的元素上。

## 結構

### [主要內容](popover.md#content)

彈出內容是一個雛型框架，內容可參考底部的《[組合應用](popover.md#composition-inline-edit)》章節。

```html
<div class="ts-popover" popover>
    <!-- ... -->
</div>
```

## 組合應用

### [同行編輯](popover.md#composition-inline-edit)

某些文字被點擊後，會彈出額外的表單供使用者編輯資料。

```html
<button class="ts-text is-editable" popovertarget="edit">
    商品售價：$3,600
</button>
<div class="ts-popover" id="edit" popover>
    <div class="ts-content is-secondary is-dense">
        <div class="ts-text is-bold">編輯價格</div>
    </div>
    <div class="ts-divider"></div>
    <div class="ts-content">
        <div class="ts-grid">
            <div class="column is-fluid">
                <div class="ts-input">
                    <input type="number" value="3600">
                </div>
            </div>
            <div class="column">
                <button class="ts-button is-icon" popovertarget="edit">
                    <span class="ts-icon is-check-icon"></span>
                </button>
            </div>
        </div>
    </div>
</div>
```

### [使用者詳情](popover.md#composition-profile)

點選某個大頭貼之後彈出使用者詳情。

```html
<button class="ts-image" popovertarget="profile">
    <img src="user.png" width="32">
</button>
<div class="ts-popover" id="profile" popover>
    <div class="ts-image">
        <img src="image.png" width="300">
    </div>
    <div class="ts-content">
        <div class="ts-header is-heavy">Yami Odymel</div>
        <div class="ts-meta is-secondary">
            <a class="item">3 天前加入</a>
            <a class="item">5 位好友</a>
        </div>
    </div>
</div>
```

## JavaScript 功能

### [透過屬性標籤控制](popover.md#popover-trigger)

點擊帶有 [`[popovertarget]`](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API/Using) 屬性的按鈕可以開、關對應 `[id]` 的彈出內容。

```html
<button class="ts-button" popovertarget="example">
    打開範例內容 ✨
</button>
<div class="ts-popover" id="example" popover>
    <div class="ts-content">
        點擊彈出內容以外的區域，<br>
        來關閉這個視窗。
    </div>
</div>
```

### [以 JavaScript 控制內容](popover.md#js-trigger)

透過瀏覽器原生的 [`.showPopover()`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/showPopover) 函式打開彈出內容。彈出內容開關時，會觸發 [`toggle`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/toggle_event) 事件。

```html
// 打開 #popover 彈出內容。
document.querySelector('#popover').showPopover();

// 關閉 #popover 彈出內容。
document.querySelector('#popover').hidePopover();
```

## 屬性設定

|  | 說明 | 預設值 | 目標 |
| --- | --- | --- | --- |
| [data-position] | 彈出內容顯示時的偏好位置。   - `top` - `top-start` - `top-end` - `bottom` - `bottom-start` - `bottom-end` | `bottom` | `.ts-popover` |
| [data-anchor] | 彈出內容附著的目標元素 `[id]`。  不指定時，會吸附於觸發元素。 |  | `.ts-popover` |

在尋找相似的元件嗎？

- [彈出式選單](dropdown.md)
- [快顯視窗](modal.md)
