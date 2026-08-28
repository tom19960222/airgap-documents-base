---
collection: tocas
version: "5.0.2"
title: "中央區塊 - Tocas UI"
source_url: https://github.com/teacat/tocas-docs/blob/e62614c61a3fdb5d75cc5573e66f64dbfdbb7be7/docs/5.0/zh-tw/app-center.html
fetched_at: 2025-03-22T01:53:10+08:00
---
```html
<div class="ts-app-center">
    <div class="content">
        <div class="ts-box">
            <div class="ts-content is-padded">
                這個區塊會置中出現在畫面正中央。
            </div>
        </div>
    </div>
</div>
```

## 概要

適合將表單、區塊置中在畫面中央，但這不適合用來置中文字。

## 結構

### [內容區塊](app-center.md#content)

中央區塊的主要內容擺放於內容區塊裡。

```html
<div class="ts-app-center">
    <div class="content">
        <!-- ... -->
    </div>
</div>
```

## 組合應用

### [登入表單](app-center.md#composition-form)

登入頁面會有置中的表單與輸入欄位。

```html
<div class="ts-app-center">
    <div class="content">
        <div class="ts-box" style="width: 270px">
            <div class="ts-content">
                <div class="ts-wrap is-vertical">
                    <div class="ts-text is-label">使用者帳號</div>
                    <div class="ts-input is-start-icon">
                        <span class="ts-icon is-user-icon"></span>
                        <input type="text">
                    </div>
                    <div class="ts-text is-label">密碼</div>
                    <div class="ts-input is-start-icon">
                        <span class="ts-icon is-lock-icon"></span>
                        <input type="password">
                    </div>
                    <button class="ts-button is-fluid">登入</button>
                </div>
            </div>
        </div>
    </div>
</div>
```

### [初始建議行為](app-center.md#composition-startup)

某些應用程式啟動的時候，畫面中央會有建議行為或上次開啟的檔案路徑。

```html
<div class="ts-app-layout is-vertical">
    <div class="cell is-secondary" style="height: 300px">
        <div class="ts-app-center">
            <div class="content">
                <div class="ts-content is-rounded is-padded is-tertiary">
                    <div class="ts-header">選擇初始專案…</div>
                    <div class="ts-list is-unordered has-top-spaced">
                        <a class="item">C:\Users\Yami\Spring-2016</a>
                        <a class="item">C:\Users\Yami\Caris-Events</a>
                        <a class="item">D:\Casino-Dev</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="cell">
        <div class="ts-content">
            <div class="ts-app-navbar is-fluid">
                <a class="item">
                    <span class="ts-icon is-diagram-project-icon"></span>
                    <div class="label">專案</div>
                </a>
                <a class="item">
                    <span class="ts-icon is-bug-icon"></span>
                    <div class="label">除錯</div>
                </a>
                <a class="item">
                    <span class="ts-icon is-gear-icon"></span>
                    <div class="label">設定</div>
                </a>
            </div>
        </div>
    </div>
</div>
```
