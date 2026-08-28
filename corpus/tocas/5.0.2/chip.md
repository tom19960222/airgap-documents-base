---
collection: tocas
version: "5.0.2"
title: "關聯標籤 - Tocas UI"
source_url: https://github.com/teacat/tocas-docs/blob/e62614c61a3fdb5d75cc5573e66f64dbfdbb7be7/docs/5.0/zh-tw/chip.html
fetched_at: 2025-03-22T01:53:10+08:00
---
```html
<div class="ts-chip">
    <div class="ts-image">
        <img src="user.png">
    </div>
    Yami Odymel
    <button class="ts-close"></button>
</div>
```

## 種類

### [輸入項目](chip.md#input)

將其當作核取方塊或是單選方塊使用，被核取的標籤會有勾選圖示作為視覺輔助。

```html
<label class="ts-chip is-input">
    <input type="checkbox" checked>
    <div class="content">健身</div>
</label>
<label class="ts-chip is-input">
    <input type="checkbox">
    <div class="content">遊戲</div>
</label>
<label class="ts-chip is-input">
    <input type="checkbox">
    <div class="content">閱讀新聞</div>
</label>
```

### [可切換項目](chip.md#toggle)

切換標籤的開、關狀態。

```html
<label class="ts-chip is-toggle is-circular">
    <input type="checkbox">
    <div class="content">最近熱門</div>
</label>
<label class="ts-chip is-toggle is-circular">
    <input type="checkbox" checked>
    <div class="content">沒去過的地點</div>
</label>
```

## 狀態

### [停用的](chip.md#disabled)

使關聯標籤呈現無法互動、點擊的模樣。若關聯標籤是超連結，則需套用 `.is-disabled` 樣式。

```html
<label class="ts-chip is-input">
    <input type="checkbox" disabled>
    <div class="content">核取標籤</div>
</label>
<button class="ts-chip" disabled>
    按鈕標籤
</button>
<a class="ts-chip is-disabled">
    連結標籤
</a>
```

## 結構

### [關閉按鈕](chip.md#close)

擺放關閉按鈕讓使用者刪除這個選項。

```html
<div class="ts-chip is-circular">
    對空音商事
    <button class="ts-close"></button>
</div>
<div class="ts-chip is-circular is-outlined">
    動態思想
    <button class="ts-close is-secondary"></button>
</div>
```

### [圖片](chip.md#image)

以圖片輔助標籤內容。

```html
<div class="ts-chip is-circular">
    <div class="ts-image is-circular">
        <img src="user.png">
    </div>
    Yami Odymel
</div>
```

## 外觀

### [外框線的](chip.md#outlined)

以簡單的框線結構呈現出一個項目。

```html
<div class="ts-chip is-outlined">
    <span class="ts-flag is-taiwan-flag is-rounded"></span>
    台灣
</div>
<div class="ts-chip is-outlined">
    <span class="ts-flag is-america-flag is-rounded"></span>
    美國
</div>
<div class="ts-chip is-outlined">
    <span class="ts-flag is-hong-kong-flag is-rounded"></span>
    香港
</div>
```

### [次要的](chip.md#secondary)

淡化標籤的核取狀態，適合用於較不醒目的地方。

```html
<label class="ts-chip is-toggle is-outlined is-secondary">
    <input type="checkbox" checked>
    <div class="content">👀 8</div>
</label>
<label class="ts-chip is-input is-outlined is-secondary">
    <input type="checkbox" checked>
    <div class="content">免費 WiFi</div>
</label>
```

### [圓角的](chip.md#circular)

使元件的角落以圓角呈現。

```html
<div class="ts-chip is-circular">影片</div>
<div class="ts-chip is-circular">音樂</div>
```

### [流動的](chip.md#fluid)

選項的寬度可以跟父容器相同。

```html
<div class="ts-grid is-3-columns">
    <div class="column">
        <label class="ts-chip is-fluid is-input is-outlined">
            <input type="checkbox" checked>
            <div class="content">小尺碼</div>
        </label>
    </div>
    <div class="column">
        <label class="ts-chip is-fluid is-input is-outlined">
            <input type="checkbox">
            <div class="content">中等尺寸</div>
        </label>
    </div>
    <div class="column">
        <label class="ts-chip is-fluid is-input is-outlined">
            <input type="checkbox">
            <div class="content">最大</div>
        </label>
    </div>
</div>
```

### [側邊圖示](chip.md#side-icon)

在兩側放置圖示以輔助這個選項。

```html
<div class="ts-chip is-start-icon">
    <span class="ts-icon is-video-icon"></span>
    影片
</div>
<div class="ts-chip is-end-icon">
    自行車活動
    <span class="ts-icon is-person-biking-icon"></span>
</div>
```

### [尺寸](chip.md#sizes)

更改關聯標籤的大小。

```html
<div class="ts-chip is-small">
    <span class="ts-icon is-heart-icon"></span>
    小型標籤
</div>
<div class="ts-chip">
    <span class="ts-icon is-heart-icon"></span>
    預設標籤
</div>
<div class="ts-chip is-large">
    <span class="ts-icon is-heart-icon"></span>
    大型標籤
</div>
```

### [較密的](chip.md#dense)

變更元件的內距，令元素之間看起來更密集。

```html
<div class="ts-chip is-dense is-outlined">
    Caris Events
</div>
```

### [間隔的](chip.md#spaced)

在前或後新增間隔以避免與其他元件相鄰太近。

```html
文章發表者為 <span class="ts-chip is-start-spaced">
    <img src="user.png">
    Mac Taylor
</span>
<span class="ts-chip is-end-spaced">
    <img src="user.png">
    Sciuridae Li
</span> 是這個社團的管理員。
記得向 <span class="ts-chip is-spaced">
    <img src="user.png">
    Sean Wei
</span> 說聲早安！
```

## 組合應用

### [反應](chip.md#composition-reactions)

在某些內容底下能夠擺放關聯標籤作為對該訊息的反應。

```html
<div class="ts-box">
    <div class="ts-content">
        <p>如果你有去釣魚大賽，你可能會被禁止進入：「我們不歡迎職業選手」</p>
        <div class="ts-wrap is-compact">
            <label class="ts-chip is-toggle is-secondary is-outlined">
                <input type="checkbox" checked>
                <div class="content">👌 21</div>
            </label>
            <label class="ts-chip is-toggle is-secondary is-outlined">
                <input type="checkbox">
                <div class="content">👀 8</div>
            </label>
            <div class="ts-chip is-outlined">
                <span class="ts-icon is-plus-icon"></span>
            </div>
        </div>
    </div>
</div>
```

### [標題功能](chip.md#composition-header)

標題下方可以擺放輔助功能讓使用者有更多選擇。

```html
<div class="ts-header is-center-aligned is-large">
    歡迎回家
</div>
<div class="ts-text is-center-aligned is-description">
    溫度 32°C、濕度 48%
</div>
<div class="ts-wrap is-center-aligned is-compact has-top-spaced">
    <button class="ts-chip is-outlined">
        <span class="ts-icon is-sun-icon"></span>
        打開所有燈光
    </button>
    <button class="ts-chip is-outlined">
        <span class="ts-icon is-stopwatch-icon"></span>
        設定鬧鐘
    </button>
</div>
```

### [卡片選項](chip.md#composition-actions)

有卡片裡擺放關聯標籤作為附屬功能選項。

```html
<div class="ts-box" style="max-width: 360px">
    <img class="ts-image" src="image.png">
    <div class="ts-content">
        <div class="ts-header">爭鮮 PLUS</div>
        <div class="ts-meta is-secondary is-small">
            <span class="item">迴轉壽司餐廳</span>
            <span class="item">$$</span>
            <span class="item">4.5 <span class="ts-icon is-star-icon"></span></span>
        </div>
        <div class="ts-divider is-section"></div>
        <div class="ts-wrap is-compact">
            <button class="ts-chip is-circular">
                <span class="ts-icon is-utensils-icon"></span>
                預訂桌位
            </button>
            <button class="ts-chip is-circular">
                <span class="ts-icon is-motorcycle-icon"></span>
                透過外送訂餐
            </button>
        </div>
    </div>
</div>
```

### [文字建議](chip.md#composition-input)

類似某些應用程式會在回覆訊息時提出的文字自動完成建議。

```html
<div class="ts-grid">
    <div class="column">
        <div class="ts-image">
            <img src="user.png" width="48">
        </div>
    </div>
    <div class="column is-fluid">
        <div class="ts-input">
            <textarea placeholder="回覆這封電子郵件…"></textarea>
        </div>
        <div class="ts-grid is-compact has-top-spaced">
            <div class="column">
                <div class="ts-wrap is-compact">
                    <button class="ts-chip is-circular">
                        沒問題！
                    </button>
                    <button class="ts-chip is-circular">
                        抱歉，我那天有事。
                    </button>
                </div>
            </div>
            <div class="column is-fluid is-end-aligned">
                <button class="ts-button">送出</button>
            </div>
        </div>
    </div>
</div>
```

在尋找相似的元件嗎？

- [計數徽章](badge.md)
