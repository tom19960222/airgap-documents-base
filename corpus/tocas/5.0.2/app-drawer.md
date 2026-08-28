---
collection: tocas
version: "5.0.2"
title: "邊緣抽屜 - Tocas UI"
source_url: https://github.com/teacat/tocas-docs/blob/e62614c61a3fdb5d75cc5573e66f64dbfdbb7be7/docs/5.0/zh-tw/app-drawer.html
fetched_at: 2025-03-22T01:53:10+08:00
---
```html
<dialog class="ts-app-drawer is-end is-small" open>
    <div class="content">
        <div class="ts-content">
            <div class="ts-header">筆記 #52</div>
            <p>我不想失去這份心情，我什麼都想嘗試。
                當我找到了這份熱情的時候，整個世界瞬間變得亮麗無比。</p>
            <p>但你卻嘆了氣並說道：「正因為我愛你，
                所以我不得不告訴你；你也差不多該長大了吧？」</p>
            <button class="ts-button is-fluid is-outlined">關閉</button>
        </div>
    </div>
</dialog>
```

## 結構

### [內容區塊](app-drawer.md#content)

邊緣抽屜是一個雛型框架，主要內容擺放於內容區塊裡。標題、動作列需搭配其他元件，請參考底部的《[組合應用](app-drawer.md#composition-close)》章節。

```html
<dialog class="ts-app-drawer" open>
    <div class="content">
        <!-- ... -->
    </div>
</dialog>
```

## 狀態

### [打開的](app-drawer.md#open)

被指定 `[open]` 屬性的邊緣抽屜會出現在畫面上。

```html
<dialog class="ts-app-drawer is-start" open>
    <div class="content">
        <div class="ts-content">
            看似最重要的東西卻沒能被妥善利用，<br>
            沒有人能發現這一點，因為他們早已活在過去，<br>
            才剛開始的序章卻被放在頁尾。
        </div>
    </div>
</dialog>
```

## 外觀

### [位置](app-drawer.md#positions)

使用邊緣抽屜時必須指定位置，可用的位置有：`is-start`（起始左側）、`is-end`（結束右側）和 `is-bottom`（底部）。

```html
<dialog class="ts-app-drawer is-bottom" open>
    <div class="content">
        <div class="ts-content">
            <div class="ts-header">最新消息</div>
            <div class="ts-iconset has-top-spaced">
                <span class="ts-icon is-newspaper-icon"></span>
                <div class="content">
                    <div class="title">新的魔法已可供學習</div>
                    <div class="text">現在前往交誼廳就可以打聽相關情報。</div>
                </div>
            </div>
        </div>
    </div>
</dialog>
```

### [尺寸](app-drawer.md#sizes)

更改邊緣抽屜的寬度大小，這個樣式只在使用左右側有效。

|  | 280px | 380px | 580px |
| --- | --- | --- | --- |
| 樣式名稱 | is-small | 預設 | is-large |

```html
<dialog class="ts-app-drawer is-small is-end" open>
    <div class="content">
        <div class="ts-content is-center-aligned">
            小型抽屜
        </div>
    </div>
</dialog>
<dialog class="ts-app-drawer is-end" open>
    <div class="content">
        <div class="ts-content is-center-aligned">
            預設抽屜
        </div>
    </div>
</dialog>
<dialog class="ts-app-drawer is-large is-end" open>
    <div class="content">
        <div class="ts-content is-center-aligned">
            大型抽屜
        </div>
    </div>
</dialog>
```

### [類快顯的](app-drawer.md#modal)

讓邊緣抽屜看起來像快顯視窗並且與螢幕邊緣保留一定的邊距。

```html
<dialog class="ts-app-drawer is-end is-modal" open>
    <div class="content">
        <div class="ts-content">
            <div class="ts-header">抽屜標題</div>
            <p>末日的天災抹去了大部分人類的所有文明，使得少數人在有毒粉塵以及火山灰中勉強生活。在地球遭遇毀滅後，《人類》成了最黑暗的代名詞。</p>
        </div>
    </div>
</dialog>
```

### [全螢幕的](app-drawer.md#fullscreen)

讓邊緣抽屜填滿整個畫面，適合搭配[響應式設計](responsive.md)改善抽屜在行動裝置上的顯示方式。

```html
<dialog class="ts-app-drawer is-fullscreen" open>
    <div class="content">
        <div class="ts-content">
            <div class="ts-header">將二次元文化融入三次元。</div>
            <p>現實生活應該像二次元那樣充滿新鮮的挑戰卻又十分地美好，而計畫這樣的未來正在我們的目標之一。我們正試著找尋多個不同的方式實現這樣的夢想，即便現在不可行，我們也永不放棄。</p>
        </div>
    </div>
</dialog>
```

## 組合應用

### [關閉按鈕](app-drawer.md#composition-close)

使用邊緣抽屜時，通常建議結合[關閉按鈕](close.md)來讓使用者有更明確的方式可以關閉抽屜。

```html
<dialog class="ts-app-drawer is-end is-small" open>
    <div class="content">
        <div class="ts-content">
            <div class="ts-grid">
                <div class="column is-fluid">
                    <div class="ts-header">備註事項</div>
                </div>
                <div class="column">
                    <button class="ts-close is-secondary is-large"></button>
                </div>
            </div>
            <div class="ts-list is-unordered has-top-spaced">
                <div class="item">蘆森詩音</div>
                <div class="item">天野悟美</div>
                <div class="item">佐藤綾</div>
            </div>
        </div>
    </div>
</dialog>
```

### [篩選條件](app-drawer.md#composition-filter)

側邊的邊緣抽屜裡面可以擺放部份表單元件，例如：[輸入欄位](input.md)。

```html
<dialog class="ts-app-drawer is-start is-small" open>
    <div class="content">
        <div class="ts-content">
            <div class="ts-header is-large">篩選條件</div>
            <div class="ts-text is-secondary has-top-spaced">標題</div>
            <div class="ts-input is-underlined has-top-spaced">
                <input type="text" placeholder="標題包含…">
            </div>
            <div class="ts-text is-secondary has-top-spaced">時間範圍</div>
            <div class="ts-input is-underlined is-start-icon has-top-spaced">
                <span class="ts-icon is-calendar-icon"></span>
                <input type="date" value="2018-01-29">
            </div>
            <div class="ts-input is-underlined is-start-icon has-top-spaced">
                <span class="ts-icon is-clock-icon"></span>
                <input type="time" value="12:00">
            </div>
            <button class="ts-button is-fluid has-top-spaced-big">套用</button>
        </div>
    </div>
</dialog>
```

### [標題動作列](app-drawer.md#composition-action)

透過[網格系統](grid.md)在抽屜標題區塊擺放標題與返回、關閉按鈕。

```html
<dialog class="ts-app-drawer is-end is-modal" open>
    <div class="content">
        <div class="ts-content">
            <div class="ts-grid is-middle-aligned">
                <div class="column">
                    <button class="ts-button is-icon is-ghost">
                        <span class="ts-icon is-arrow-left-icon"></span>
                    </button>
                </div>
                <div class="column is-fluid">
                    <div class="ts-header">抽屜標題</div>
                </div>
                <div class="column">
                    <button class="ts-button is-icon is-ghost">
                        <span class="ts-icon is-xmark-icon"></span>
                    </button>
                </div>
            </div>
            <p>這裡可以擺放其他文字內容。</p>
        </div>
    </div>
</dialog>
```

### [底部選單](app-drawer.md#composition-bottom-sheet)

貼齊底部的邊緣抽屜再搭配一個[選單](menu.md)就可以達成像行動裝置的底部彈出選單元件。

```html
<dialog class="ts-app-drawer is-bottom" open>
    <div class="content">
        <div class="ts-menu is-start-icon has-top-spaced">
            <a class="item">
                <span class="ts-icon is-copy-icon"></span>
                複製檔案
            </a>
            <a class="item">
                <span class="ts-icon is-trash-can-icon"></span>
                移至回收桶
            </a>
        </div>
        <div class="ts-content">
            <button class="ts-button is-fluid is-outlined">關閉</button>
        </div>
    </div>
</dialog>
```

## JavaScript 功能

### [透過屬性標籤控制](app-drawer.md#dialog-trigger)

點擊帶有 `[data-dialog]` 屬性的按鈕可以開、關對應 `[id]` 的邊緣抽屜。

```html
<button class="ts-button" data-dialog="drawer">
    打開範例抽屜 ✨
</button>
<dialog class="ts-app-drawer is-end" id="drawer">
    <div class="content">
        <div class="ts-content">
            <div class="ts-header">抽屜標題</div>
            <p>點擊關閉按鈕或是灰色區域來關閉抽屜。</p>
            <button class="ts-button" data-dialog="drawer">關閉</button>
        </div>
    </div>
</dialog>
```

### [透過程式控制](app-drawer.md#js-trigger)

透過瀏覽器原生的 [`.showModal()`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLDialogElement/showModal) 函式打開抽屜，若抽屜本身已有 `[open]` 屬性，這個函式將不會有任何效果。抽屜被關閉時，會觸發 [`close`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLDialogElement/close_event) 或 [`cancel`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/cancel_event) 事件。

```html
// 打開 #drawer 邊緣抽屜。
document.querySelector('#drawer').showModal();

// 關閉 #drawer 邊緣抽屜。
document.querySelector('#drawer').close();
```

## 屬性設定

|  | 說明 | 預設值 | 目標 |
| --- | --- | --- | --- |
| [data-dismissible] | 使用者是否能透過 `Esc` 鍵或是點擊抽屜外的區域關閉邊緣抽屜。 | `true` | `.ts-app-drawer` |

## 樣式變數

|  | 說明 | 預設值 | 目標 |
| --- | --- | --- | --- |
| --width | 邊緣抽屜的內容寬度。 | `380px` | `.ts-app-drawer` |
