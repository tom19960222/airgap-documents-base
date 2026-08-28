---
collection: tocas
version: "5.0.2"
title: "箱型容器 - Tocas UI"
source_url: https://github.com/teacat/tocas-docs/blob/e62614c61a3fdb5d75cc5573e66f64dbfdbb7be7/docs/5.0/zh-tw/box.html
fetched_at: 2025-03-22T01:53:10+08:00
---
```html
<div class="ts-box">
    <div class="ts-image">
        <img src="image.png">
    </div>
    <div class="ts-content">
        <div class="ts-header is-heavy">好吃的千層蛋糕！</div>
        <p>在 5 月之前於線上網路門市訂購，現在還特別加贈限量環保袋。</p>
    </div>
</div>
```

## 概要

箱型容器會與[內容區塊](content.md)、[表格](table.md)、[圖片](image.md)這種貼邊元件一起使用。

## 結構

### [象徵圖示](box.md#symbol)

在角落擺放一個圖示作為其象徵。

```html
<div class="ts-box">
    <div class="ts-content">
        任何已發布或是計畫中之產品及服務，<br>
        皆不得用來刻意偏頗大眾想法、喜好、甚至混淆視聽，<br>
        且該產品及服務不得擁有自我立場。
    </div>
    <div class="symbol">
        <span class="ts-icon is-circle-exclamation-icon"></span>
    </div>
</div>
```

## 外觀

### [水平的](box.md#horizontal)

容器裡的元素排列預設為上下垂直，但若排版需要則可以將其改為左右水平排列。

```html
<div class="ts-box is-horizontal">
    <div class="ts-image is-covered">
        <img src="image.png" width="90" height="100%">
    </div>
    <div class="ts-content">
        <div class="ts-header">
            Zedd - Papercut (Audio) ft. Troye Sivan
        </div>
        <p>Get "True Colors" on iTunes: http://smarturl.it/ZeddTrueColors</p>
    </div>
</div>
```

### [最小寬度的](box.md#collapsed)

箱型容器預設是流動寬度，但也能以內容寬度為主。

```html
<div class="ts-box is-collapsed">
    <div class="ts-content">
        <p>這是一個來自台灣的社群網站，在這裡我們並沒有「讚」或是「已讀」。</p>
    </div>
</div>
```

### [標記的](box.md#indicated)

讓容器的某個邊緣有特別標記的樣式。

```html
<div class="ts-box is-top-indicated">
    <div class="ts-content">上部標記</div>
</div>
<div class="ts-box is-bottom-indicated">
    <div class="ts-content">下部標記</div>
</div>
<div class="ts-box is-start-indicated">
    <div class="ts-content">左邊標記</div>
</div>
<div class="ts-box is-end-indicated">
    <div class="ts-content">右部標記</div>
</div>
```

### [語意](box.md#emphasises)

更改標記的顏色語意，必須搭配「標記的」使用。

```html
<div class="ts-box is-negative is-top-indicated">
    <div class="ts-content">負面的</div>
</div>
<div class="ts-box is-positive is-top-indicated">
    <div class="ts-content">正面的</div>
</div>
<div class="ts-box is-warning is-top-indicated">
    <div class="ts-content">警告的</div>
</div>
```

### [抬升的](box.md#raised)

透過陰影讓容器看起來有浮起的感覺。

```html
<div class="ts-box is-raised">
    <div class="ts-content">抬升的</div>
</div>
```

### [直角的](box.md#sharp)

讓邊角以直角呈現而不再圓潤。

```html
<div class="ts-box is-sharp">
    <div class="ts-content">直角箱型容器</div>
</div>
```

### [空虛的](box.md#dashed)

透過加粗虛線描繪外框，通常用以呈現空的區塊。

```html
<div class="ts-box is-hollowed">
    <div class="ts-blankslate is-interactive">
        <div class="header">上傳圖片或影音</div>
        <div class="description">將圖片拖拉至此處進行上傳</div>
    </div>
</div>
```

## 組合應用

### [資訊概要](box.md#composition-information)

透過搭配[網格系統](grid.md)、象徵圖示可以營造出系統儀表板頂部常有的統計數據概要資訊。

```html
<div class="ts-grid is-2-columns">
    <div class="column">
        <div class="ts-box">
            <div class="ts-content">
                <div class="ts-statistic">
                    <div class="value">42,689</div>
                    <div class="comparison is-increased">32</div>
                </div>
                本月拜訪次數
            </div>
            <div class="symbol">
                <span class="ts-icon is-eye-icon"></span>
            </div>
        </div>
    </div>
    <div class="column">
        <div class="ts-box">
            <div class="ts-content">
                <div class="ts-statistic">
                    <div class="value">8,652</div>
                    <div class="comparison is-increased">351</div>
                </div>
                總會員數
            </div>
            <div class="symbol">
                <span class="ts-icon is-users-icon"></span>
            </div>
        </div>
    </div>
</div>
```

### [警示卡片](box.md#composition-alert)

帶有負面語意的標記卡片可以用來警示使用者。

```html
<div class="ts-box is-negative is-start-indicated">
    <div class="ts-content">
        <div class="ts-header is-negative">可用餘額不足</div>
        <p>你的錢包餘額已經不夠支付本次的伺服器租賃費用。若超過付款期限仍未儲值，資料將會暫時無法存取。</p>
    </div>
</div>
```

### [連結預覽卡片](box.md#composition-link-preview)

在箱型容器裡擺放貼邊圖片和文字與標題就可以達成像 Facebook、Twitter 那樣的連結預覽卡片。

```html
<div class="ts-box" style="max-width: 360px">
    <div class="ts-image">
        <img src="image.png">
    </div>
    <div class="ts-content is-secondary">
        <div class="ts-text is-description">yami.io/rog-and-hololive/</div>
        <div class="ts-header is-truncated is-heavy">華碩自稱「中國公司」，中國分部發言誓死阻撓日本工商</div>
        <div class="ts-text is-2-lines is-description">在微博上的《ROG玩家国度》小編便發文了，誓死也會阻止這次日本華碩與 Hololive 的工商互動。多數中國網友表示期待且「買不買華碩就看這次了」。</div>
    </div>
</div>
```

在尋找相似的元件嗎？

- [內容區塊](content.md)
