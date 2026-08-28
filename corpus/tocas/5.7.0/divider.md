---
collection: tocas
version: "5.7.0"
title: "分隔線 - Tocas UI"
source_url: https://github.com/teacat/tocas-docs/blob/ef8248b165f458215fb8f18bb400c4bfba1767fa/docs/5.7/zh-tw/divider.html
fetched_at: 2026-02-25T00:25:36+08:00
---
```html
<div class="ts-divider"></div>
```

## 概要

分隔線預設情況下沒有外距，因此能作為線條使用。

## 外觀

### [區段的](divider.md#section)

區段的分隔線上下會有空白間隔。

```html
<p>我是微笑小安安，歡迎來到小安網站。</p>
<div class="ts-divider is-section"></div>
<p>你將會在這裡看見一個魔法師的日常生活。沒錯，只要你能夠單身三十年，你也可以跟我一樣成為魔法師。</p>
```

### [垂直的](divider.md#vertical)

在水平的[箱型容器](box.md)裡可以擺放垂直分隔線來劃分兩個區塊。

```html
<div class="ts-box is-horizontal">
    <div class="ts-content">嗶嗶嗶。</div>
    <div class="ts-divider is-vertical"></div>
    <div class="ts-content">旁邊是國際換日線。</div>
</div>
```

### [文字的](divider.md#text)

分隔線中間能夠插入文字。

```html
<div class="ts-divider is-start-text">2022 年 04 月 01 日</div>
<div class="ts-divider is-center-text">你可能會喜歡這些商品</div>
<div class="ts-divider is-end-text">商品說明</div>
```

## 組合應用

### [界線劃分](divider.md#composition-content)

透過分隔線來劃分[箱型容器](box.md)裡兩個不同的[內容區塊](content.md)。

```html
<div class="ts-box">
    <div class="ts-content">
        Event Store 是一個基於 CQRS 與 Event Sourcing 理念所衍生出來的新概念並由 C Sharp 撰寫。
    </div>
    <div class="ts-divider"></div>
    <div class="ts-content is-secondary">
        6,439,852 觀看次數
    </div>
</div>
```

### [第三方登入](divider.md#composition-form)

在登入表單下方以分隔線告訴使用者有額外方式能登入。

```html
<div class="ts-app-center">
    <div class="content">
        <div class="ts-box" style="width: 280px">
            <div class="ts-content">
                <div class="ts-wrap is-vertical">
                    <div class="ts-text is-label">電子信箱地址</div>
                    <div class="ts-input is-start-icon">
                        <span class="ts-icon is-envelope-icon"></span>
                        <input type="text">
                    </div>
                    <div class="ts-text is-label">密碼</div>
                    <div class="ts-input is-start-icon">
                        <span class="ts-icon is-lock-icon"></span>
                        <input type="password">
                    </div>
                    <button class="ts-button is-fluid">註冊</button>
                    <div class="ts-divider is-center-text">
                        <div class="ts-text is-description">
                            或是透過下列方式登入
                        </div>
                    </div>
                    <button class="ts-button is-fluid is-start-icon is-outlined">
                        <span class="ts-icon is-google-icon"></span> Google
                    </button>
                </div>
            </div>
        </div>
    </div>
</div>
```

## 樣式變數

|  | 說明 | 預設值 | 目標 |
| --- | --- | --- | --- |
| --gap | 分隔線的垂直外距。 | `0` | `.ts-divider` |
