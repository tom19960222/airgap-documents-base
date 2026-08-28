---
collection: tocas
version: "5.0.2"
title: "快顯視窗 - Tocas UI"
source_url: https://github.com/teacat/tocas-docs/blob/e62614c61a3fdb5d75cc5573e66f64dbfdbb7be7/docs/5.0/zh-tw/modal.html
fetched_at: 2025-03-22T01:53:10+08:00
---
```html
<dialog class="ts-modal" open>
    <div class="content">
        <div class="ts-content">
            <div class="ts-header">視窗標題</div>
        </div>
        <div class="ts-divider"></div>
        <div class="ts-content">
            在工地上，劈哩啪啦的聲音不斷地響起，
            工人們忙碌地進行各種建築工作，喧囂的聲音彷彿是建築的樂章。
        </div>
    </div>
</dialog>
```

## 結構

### [內容區塊](modal.md#content)

快顯視窗是一個雛型框架，主要內容擺放於內容區塊裡。標題、動作列需搭配其他元件，請參考底部的《[組合應用](modal.md#composition-close)》章節。

```html
<dialog class="ts-modal" open>
    <div class="content">
        <!-- ... -->
    </div>
</dialog>
```

## 狀態

### [打開的](modal.md#open)

被指定 `[open]` 屬性的快顯視窗會出現在畫面上。

```html
<dialog class="ts-modal" open>
    <div class="content">
        <div class="ts-content">
            如果你有去釣魚大賽，你可能會被禁止進入：「我們不歡迎職業選手」
        </div>
    </div>
</dialog>
```

## 外觀

### [尺寸](modal.md#sizes)

更改視窗的寬度大小。

|  | 280px | 380px | 580px | 780px |
| --- | --- | --- | --- | --- |
| 樣式名稱 | is-small | 預設 | is-large | is-big |

```html
<dialog class="ts-modal is-small" open>
    <div class="content">
        <div class="ts-content is-center-aligned">
            小型視窗
        </div>
    </div>
</dialog>
<dialog class="ts-modal" open>
    <div class="content">
        <div class="ts-content is-center-aligned">
            預設視窗
        </div>
    </div>
</dialog>
<dialog class="ts-modal is-large" open>
    <div class="content">
        <div class="ts-content is-center-aligned">
            大型視窗
        </div>
    </div>
</dialog>
```

### [全螢幕的](modal.md#fullscreen)

讓快顯視窗填滿整個畫面，適合搭配[響應式設計](responsive.md)改善視窗在行動裝置上的顯示方式。

```html
<dialog class="ts-modal is-fullscreen" open>
    <div class="content">
        <div class="ts-content">
            <div class="ts-header">建立社群網路與情感社交的聯繫。</div>
        </div>
        <div class="ts-divider"></div>
        <div class="ts-content">
            建立人與人之間的聯繫並提供一個良好的內容創作環境是我們的首要目標。任何人都應該有不受拘束的創作自由，這也是我們最致力發展的目標。其次是協助推廣創作者們得到更大的迴響進而推動整個產業的發展。
        </div>
        <div class="ts-divider"></div>
        <div class="ts-content is-tertiary">
            <button class="ts-button">關閉</button>
        </div>
    </div>
</dialog>
```

## 組合應用

### [標題列、關閉按鈕](modal.md#composition-close)

使用[網格系統](grid.md)替視窗加上[標題](header.md)與[關閉按鈕](close.md)。

```html
<dialog class="ts-modal" open>
    <div class="content">
        <div class="ts-content">
            <div class="ts-grid">
                <div class="column is-fluid">
                    <div class="ts-header">伊繁星最高協議</div>
                </div>
                <div class="column">
                    <button class="ts-close is-large is-secondary"></button>
                </div>
            </div>
        </div>
        <div class="ts-divider"></div>
        <div class="ts-content">
            我們希望透過這個協議能夠避免未來誤入歧途朝著並非當初的理想道路前進；顧名思義，最高協議中的所有定義都是旗下服務所必須遵循的核心條件，而且沒有任何規則可以覆蓋這些最上級的規定。這些協議在定制的時候參考了許多世界人權宣言的部份。
        </div>
    </div>
</dialog>
```

### [動作列](modal.md#composition-action)

透過次要的[內容區塊](content.md)與[按鈕](button.md)和一個對齊尾端的[間隔容器](wrap.md)打造出一個動作列。

```html
<dialog class="ts-modal" open>
    <div class="content">
        <div class="ts-content">
            <div class="ts-header">輸入使用者名稱</div>
        </div>
        <div class="ts-divider"></div>
        <div class="ts-content">
            <div class="ts-input">
                <input type="text" value="Yami Odymel">
            </div>
        </div>
        <div class="ts-divider"></div>
        <div class="ts-content is-tertiary">
            <div class="ts-wrap is-end-aligned">
                <button class="ts-button">確定</button>
                <button class="ts-button is-outlined">取消</button>
            </div>
        </div>
    </div>
</dialog>
```

### [警告視窗](modal.md#composition-warning)

搭配帶有圖示的[標題](header.md)營造出一個警告視窗。

```html
<dialog class="ts-modal" open>
    <div class="content">
        <div class="ts-content is-center-aligned is-padded">
            <div class="ts-header is-icon">
                <span class="ts-icon is-bomb-icon"></span>
                你正要重新啟動伺服器
            </div>
            <p>這個手續將會花上至少半小時，在這段期間內你將無法執行任何動作。</p>
        </div>
        <div class="ts-divider"></div>
        <div class="ts-content is-tertiary">
            <button class="ts-button is-fluid">了解</button>
        </div>
    </div>
</dialog>
```

### [可捲動內容](modal.md#composition-scrollable)

賦予 `overflow-y: auto` 樣式給過長的[內容區塊](content.md)讓其文字過長時可以捲動。

```html
<dialog class="ts-modal" open>
    <div class="content">
        <div class="ts-content">
            <div class="ts-header">使用者條約</div>
        </div>
        <div class="ts-divider"></div>
        <div class="ts-content" style="max-height: 170px; overflow-y: auto">
            <p>我們希望透過這個協議能夠避免未來誤入歧途朝著並非當初的理想道路前進；顧名思義，最高協議中的所有定義都是旗下服務所必須遵循的核心條件，而且沒有任何規則可以覆蓋這些最上級的規定。這些協議在定制的時候參考了許多世界人權宣言的部份。在探討之後，這個協議主要能夠被區分為三個環節，分別是：「設計」時所該顧慮到的全面盤局、自我期許還有看待事物的「態度」，以及最為重要的「執行」手段。但無論如何—設計的時候應該為全民、大眾所設計、運作並傾聽；向著夢想的態度應該永不放棄；對事執行的時候則莫忘初衷。</p>
        </div>
        <div class="ts-divider"></div>
        <div class="ts-content">
            <label class="ts-checkbox">
                <input type="checkbox" checked>
                我已閱讀上述所有內容且同意。
            </label>
        </div>
        <div class="ts-divider"></div>
        <div class="ts-content is-tertiary">
            <button class="ts-button is-fluid">確定</button>
        </div>
    </div>
</dialog>
```

## JavaScript 功能

### [透過屬性標籤控制](modal.md#dialog-trigger)

點擊帶有 `[data-dialog]` 屬性的按鈕可以開、關對應 `[id]` 的快顯視窗。

```html
<button class="ts-button" data-dialog="modal">
    打開範例視窗 ✨
</button>
<dialog class="ts-modal" id="modal">
    <div class="content">
        <div class="ts-content">
            <div class="ts-header">視窗標題</div>
        </div>
        <div class="ts-divider"></div>
        <div class="ts-content">
            <p>點擊關閉按鈕或是灰色區域來關閉視窗。</p>
        </div>
        <div class="ts-divider"></div>
        <div class="ts-content is-tertiary is-end-aligned">
            <button class="ts-button" data-dialog="modal">關閉</button>
        </div>
    </div>
</dialog>
```

### [透過程式控制](modal.md#js-trigger)

透過瀏覽器原生的 [`.showModal()`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLDialogElement/showModal) 函式打開視窗，若視窗本身已有 `[open]` 屬性，這個函式將不會有任何效果。快顯視窗被關閉時，會觸發 [`close`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLDialogElement/close_event) 或 [`cancel`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/cancel_event) 事件。

```html
// 打開 #modal 快顯視窗。
document.querySelector("#modal").showModal();

// 關閉 #modal 快顯視窗。
document.querySelector("#modal").close();
```

## 屬性設定

|  | 說明 | 預設值 | 目標 |
| --- | --- | --- | --- |
| [data-dismissible] | 使用者是否能透過 `Esc` 鍵或是點擊視窗外的區域關閉快顯視窗。 | `true` | `.ts-modal` |

## 樣式變數

|  | 說明 | 預設值 | 目標 |
| --- | --- | --- | --- |
| --width | 快顯視窗的內容寬度。 | `380px` | `.ts-modal` |
