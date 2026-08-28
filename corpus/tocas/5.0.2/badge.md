---
collection: tocas
version: "5.0.2"
title: "計數徽章 - Tocas UI"
source_url: https://github.com/teacat/tocas-docs/blob/e62614c61a3fdb5d75cc5573e66f64dbfdbb7be7/docs/5.0/zh-tw/badge.html
fetched_at: 2025-03-22T01:53:10+08:00
---
```html
<span class="ts-badge">689</span>
```

## 概要

計數徽章僅能呈現基本文字（如：下載人數、等級），若希望帶有關閉按鈕或是圖示、多媒體頭像，請使用[關聯標籤](chip.md)元件。

## 外觀

### [次要的](badge.md#secondary)

以較不重要的方式呈現數值。

```html
<span class="ts-badge is-secondary">16,226</span>
```

### [外框線的](badge.md#outlined)

僅描繪外框線的簡潔徽章。

```html
<span class="ts-badge is-outlined">1,386</span>
```

### [負面的](badge.md#negative)

表達出危險或是負面語氣。

```html
<span class="ts-badge is-negative">320</span>
```

### [尺寸](badge.md#sizes)

更改徽章的大小。

```html
<span class="ts-badge is-small">小的</span>
<span class="ts-badge">預設</span>
<span class="ts-badge is-large">大的</span>
```

### [較密的](badge.md#dense)

變更元件的內距，令元素之間看起來更密集。

```html
<span class="ts-badge is-dense">最新的</span>
```

### [間隔的](badge.md#spaced)

在前或後新增間隔以避免與其他元件相鄰太近。

```html
Yami Odymel <span class="ts-badge is-start-spaced">管理員</span>
<span class="ts-badge is-end-spaced">最新上架</span> 好吃的糖果
這個椅子 <span class="ts-badge is-spaced">特價</span> 目前正大受好評。
```

## 組合應用

### [表格](badge.md#composition-table)

有時候表格裡可以加上計數徽章用以襯托相關標籤資訊。

```html
<div class="ts-box">
    <table class="ts-table">
        <thead>
            <tr>
                <th>主機名稱</th>
                <th>狀態</th>
                <th>標籤</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>主要網站</td>
                <td>正常</td>
                <td>
                    <span class="ts-badge">台灣</span>
                    <span class="ts-badge is-secondary">已啟用資料備援</span>
                </td>
            </tr>
            <tr>
                <td>使用者資料庫</td>
                <td>正常</td>
                <td>
                    <span class="ts-badge">美國</span>
                    <span class="ts-badge is-secondary">已啟用資料備援</span>
                </td>
            </tr>
            <tr>
                <td>影片儲存伺服器</td>
                <td>正常</td>
                <td>
                    <span class="ts-badge">美國</span>
                </td>
            </tr>
        </tbody>
    </table>
</div>
```

### [標題與文字](badge.md#composition-header)

想要強調某些最新消息就可以在標題裡使用計數徽章。

```html
<div class="ts-box">
    <div class="ts-content">
        <div class="ts-header">
            星際效應
            <span class="ts-badge is-start-spaced">新上映</span>
        </div>
        <p>《星際效應》是一部2014年上映的科幻電影，由克里斯多福·諾蘭執導和監製，馬修·麥康納、安·海瑟薇、潔西卡·崔絲坦和米高·肯恩主演。電影講述一組太空人通過穿越蟲洞為人類尋找新家園的冒險故事。</p>
        <div class="ts-text is-secondary">— 維基百科</div>
    </div>
</div>
```

在尋找相似的元件嗎？

- [關聯標籤](chip.md)
