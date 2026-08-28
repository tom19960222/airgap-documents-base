---
collection: tocas
version: "5.7.0"
title: "內容區塊 - Tocas UI"
source_url: https://github.com/teacat/tocas-docs/blob/ef8248b165f458215fb8f18bb400c4bfba1767fa/docs/5.7/zh-tw/content.html
fetched_at: 2026-02-25T00:25:36+08:00
---
```html
<div class="ts-box">
    <div class="ts-content is-dense has-dark">
        透過 CSS Variable 取代 Sass 並設計一個臻至完美的動態色彩主題系統
    </div>
    <div class="ts-divider"></div>
    <div class="ts-content">
        色彩佈景系統在前端實作時常常都是個不小的問題，直到 Sass、Less 這種預先處理器的出現才解決了不少的麻煩，因為你能夠透過短短幾行程式碼就讓程式幫你自動處理顏色的部份，而這方面的教學在國外網站中也不是少數。
    </div>
</div>
```

## 概要

讓某個區塊帶有內距，這個元件很常與[箱型容器](box.md)一同使用。

## 狀態

### [啟用的](content.md#active)

表示某個內容區塊被選中。

```html
<div class="ts-box">
    <div class="ts-content is-dense">蘋果</div>
    <div class="ts-content is-active is-dense">菠羅</div>
    <div class="ts-content is-dense">麵包</div>
</div>
```

### [停用的](content.md#disabled)

表示目前已不再提供可用的功能。

```html
<div class="ts-box">
    <div class="ts-content is-dense">卡莉絲</div>
    <div class="ts-content is-disabled is-dense">雷莉亞</div>
    <div class="ts-content is-dense">依可諾爾</div>
</div>
```

## 外觀

### [次要的](content.md#secondary)

淡化的內容區塊會以較不顯眼的方式出現，通常用以呈現次要資訊。

```html
<div class="ts-box">
    <div class="ts-content">
        Event Store 是一個基於 CQRS 與 Event Sourcing 理念所衍生出來的新概念並由 C Sharp 撰寫。這是一個微服務事件儲藏中心，這可能很難懂，但別緊張，這些都會在本文中得到答案。
    </div>
    <div class="ts-divider"></div>
    <div class="ts-content is-secondary is-dense">
        <span class="ts-icon is-end-spaced is-eye-icon"></span> 6,439,852 觀看次數
    </div>
</div>
```

### [非主要的](content.md#tertiary)

較為沈重的內容區塊，通常不會作為主要內容。

```html
<div class="ts-content is-tertiary is-vertically-very-padded">
    <div class="ts-header is-large is-center-aligned">
        這個故事結束了
    </div>
    <div class="ts-text is-secondary is-center-aligned">
        所有人不是死亡就是離開了，也許有一天會有人替這個遺跡找到新的用處。
    </div>
</div>
```

### [文字對齊](content.md#aligns)

更改文字的對齊方式。

```html
<div class="ts-box">
    <div class="ts-content is-start-aligned">
        置起始位置
    </div>
    <div class="ts-content is-center-aligned">
        置中間位置
    </div>
    <div class="ts-content is-end-aligned">
        置結束位置
    </div>
</div>
```

### [可互動的](content.md#interactive)

增加視覺效果令使用者能夠透過滑鼠、觸控得知這個區塊可以被點擊或是互動。

```html
<div class="ts-box">
    <a class="ts-content is-interactive is-dense">
        <span class="ts-icon is-end-spaced is-download-icon"></span> 下載
    </a>
    <a class="ts-content is-interactive is-active is-dense">
        <span class="ts-icon is-end-spaced is-heart-icon"></span> 最愛
    </a>
    <a class="ts-content is-interactive is-dense">
        <span class="ts-icon is-end-spaced is-box-archive-icon"></span> 彙整
    </a>
</div>
```

### [增加內距](content.md#padded)

加大內容區塊的內距，適合用於排版。

```html
<div class="ts-box">
    <div class="ts-content is-very-padded">
        這個區塊的內距是原本的 3 倍。
    </div>
</div>
<div class="ts-box">
    <div class="ts-content is-padded">
        這個區塊的內距是原本的 1.5 倍。
    </div>
</div>
<div class="ts-box">
    <div class="ts-content is-horizontally-padded">
        僅有增加左右水平內距。
    </div>
</div>
<div class="ts-box">
    <div class="ts-content is-vertically-padded">
        僅有增加上下垂直內距。
    </div>
</div>
```

### [圓角的](content.md#rounded)

使區塊本身的四個角落以圓角呈現，避免太過尖銳。

```html
<div class="ts-content is-rounded is-tertiary">
    透過網路改變現實生活中的事件。比起創新我們更喜歡革新並找出大家真正所需。
</div>
```

### [無內距](content.md#fitted)

移除區塊的內距。

```html
<div class="ts-box">
    <div class="ts-content is-fitted">
        移除所有內距。
    </div>
</div>
<div class="ts-box">
    <div class="ts-content is-horizontally-fitted">
        移除左右水平內距。
    </div>
</div>
<div class="ts-box">
    <div class="ts-content is-vertically-fitted">
        移除上下垂直內距。
    </div>
</div>
```

### [較密的](content.md#dense)

變更元件的內距，令元素之間看起來更密集。

```html
<div class="ts-box">
    <div class="ts-content is-dense">
        <div class="ts-header">圖像複用、反轉、鏡射：怎麼將遊戲壓縮在 40 KB 以下還同時保持關卡獨特性？</div>
        Micro Mages 為了保持關卡的獨特性，開發者還特別精心設計了一個「偏移索引」系統，而遊戲中的種種設計都值得令人仔細觀察一番，而這就成為 Micro Mages 對這款遊戲最直接的廣告賣點。
    </div>
</div>
```

## 組合應用

### [暗色區塊](content.md#composition-dark)

以暗色主題呈現某個特定區塊，檢視[主題色系](colors.md)頁面以獲得更多資訊。

```html
<div class="ts-box">
    <div class="ts-content is-dense has-dark">
        けものフレンズ
    </div>
    <div class="ts-content">
        Welcome to ようこそジャパリパーク！<br>
        今日もドッタンバッタン大騒ぎ
    </div>
</div>
```

在尋找相似的元件嗎？

- [箱型容器](box.md)
