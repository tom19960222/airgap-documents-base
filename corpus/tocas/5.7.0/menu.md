---
collection: tocas
version: "5.7.0"
title: "選單 - Tocas UI"
source_url: https://github.com/teacat/tocas-docs/blob/ef8248b165f458215fb8f18bb400c4bfba1767fa/docs/5.7/zh-tw/menu.html
fetched_at: 2026-02-25T00:25:36+08:00
---
```html
<div class="ts-box" style="width: 250px">
    <div class="ts-menu is-start-icon">
        <a class="item">
            <span class="ts-icon is-house-icon"></span> 首頁
        </a>
        <a class="item is-active">
            <span class="ts-icon is-gauge-high-icon"></span> 儀表板
        </a>
        <a class="item">
            <span class="ts-icon is-table-icon"></span> 訂單
        </a>
        <div class="ts-divider"></div>
        <a class="item">
            <span class="ts-icon is-gears-icon"></span> 設定
        </a>
    </div>
</div>
```

## 狀態

### [啟用的](menu.md#active)

表示目前已經被啟用或是正在呈現的相關功能。

```html
<div class="ts-menu">
    <a class="item">個人資料</a>
    <a class="item is-active">位置分享</a>
    <a class="item">設定</a>
</div>
```

### [停用的](menu.md#disabled)

使項目呈現無法互動、點擊的模樣。若項目是超連結，則需套用 `.is-disabled` 樣式。

```html
<div class="ts-menu">
    <a class="item">無線通訊</a>
    <button class="item" disabled>地圖紀錄</button>
    <a class="item is-disabled">導航設定</a>
</div>
```

### [已選擇](menu.md#selected)

表示某個項目被選中。

```html
<div class="ts-menu">
    <a class="item">蘋果</a>
    <a class="item is-selected">鳳梨</a>
    <a class="item">西瓜</a>
</div>
```

## 結構

### [計數徽章](menu.md#badge)

在項目裡擺放計數徽章表示數量。

```html
<div class="ts-box">
    <div class="ts-menu is-start-icon">
        <a class="item is-active">
            <span class="ts-icon is-inbox-icon"></span>
            收件匣
            <div class="badge">3</div>
        </a>
        <a class="item">
            <span class="ts-icon is-bookmark-icon"></span>
            重要郵件
        </a>
        <a class="item">
            <span class="ts-icon is-circle-exclamation-icon"></span>
            垃圾郵件
            <div class="badge">64</div>
        </a>
    </div>
</div>
```

## 項目外觀

### [負面的](menu.md#negative)

表示某個項目的行為具有危險性。

```html
<div class="ts-menu">
    <a class="item">編輯資料</a>
    <a class="item is-negative">關閉此案件</a>
</div>
```

## 外觀

### [次要的](menu.md#secondary)

使啟用的項目會以次要的樣式呈現。

```html
<div class="ts-menu is-secondary is-start-icon">
    <a class="item">
        <span class="ts-icon is-list-icon"></span> 概覽
    </a>
    <a class="item is-active">
        <span class="ts-icon is-note-sticky-icon"></span> 筆記
    </a>
    <a class="item">
        <span class="ts-icon is-car-icon"></span> 行程
    </a>
</div>
```

### [分開的](menu.md#separated)

使項目之間有空白間隔區分而不會相黏。

```html
<div class="ts-menu is-separated is-start-icon">
    <a class="item">
        <span class="ts-icon is-user-icon"></span> 使用者
    </a>
    <a class="item is-active">
        <span class="ts-icon is-house-icon"></span> 首頁
    </a>
    <a class="item">
        <span class="ts-icon is-newspaper-icon"></span> 新聞
    </a>
</div>
```

### [標記的](menu.md#indicated)

使啟用的項目在某一側有特別標記的樣式。如果與「分開的」樣式搭配，則會移除側邊框。

```html
<div class="ts-menu is-start-indicated">
    <a class="item">收藏</a>
    <a class="item is-active">影片</a>
    <a class="item">音樂</a>
</div>
<div class="ts-menu is-end-indicated is-separated">
    <a class="item">收藏</a>
    <a class="item is-active">影片</a>
    <a class="item">音樂</a>
</div>
```

### [最小寬度的](menu.md#collapsed)

由於此元件預設為流動寬度，若希望寬度以內容為主，則可以將其設為最小寬度。

```html
<div class="ts-menu is-collapsed is-separated is-start-icon">
    <a class="item">
        <span class="ts-icon is-envelope-icon"></span> 信件
    </a>
    <a class="item is-active">
        <span class="ts-icon is-comment-icon"></span> 聊天
    </a>
    <a class="item">
        <span class="ts-icon is-users-icon"></span> 社群
    </a>
</div>
```

### [帶圖示的](menu.md#icon)

選單項目的起始或結束位置可以帶有圖示輔助。

```html
<div class="ts-box">
    <div class="ts-menu is-start-icon">
        <a class="item">
            <span class="ts-icon is-magnifying-glass-icon"></span> 搜尋
        </a>
        <a class="item">
            <span class="ts-icon is-vials-icon"></span> 實驗區
        </a>
        <a class="item">
            <span class="ts-icon is-atom-icon"></span> 原子測試
        </a>
    </div>
</div>
<div class="ts-box">
    <div class="ts-menu is-end-icon">
        <a class="item">
            我的最愛 <span class="ts-icon is-heart-icon"></span>
        </a>
        <a class="item">
            已讚好內容 <span class="ts-icon is-thumbs-up-icon"></span>
        </a>
        <a class="item">
            封存項目 <span class="ts-icon is-box-archive-icon"></span>
        </a>
    </div>
</div>
```

### [增加水平內距](menu.md#horizontally-padded)

加大項目的水平內距，適合用於排版或給予視覺上更大的空間或是與[內容區塊](content.md)一同排列時使用。

```html
<div class="ts-box">
    <div class="ts-menu">
        <a class="item">
            預設
        </a>
        <a class="item">
            預設
        </a>
    </div>
</div>
<div class="ts-box">
    <div class="ts-menu is-horizontally-padded">
        <a class="item">
            增加內距
        </a>
        <a class="item">
            增加內距
        </a>
    </div>
</div>
<div class="ts-box">
    <div class="ts-menu is-horizontally-very-padded">
        <a class="item">
            非常增加內距
        </a>
        <a class="item">
            非常增加內距
        </a>
    </div>
</div>
```

### [尺寸](menu.md#sizes)

更改選單項目的大小。

```html
<div class="ts-box">
    <div class="ts-menu is-large is-start-icon">
        <a class="item">
            <span class="ts-icon is-star-icon"></span> 常用聯絡人
        </a>
        <a class="item">
            <span class="ts-icon is-users-icon"></span> 聯絡人
        </a>
    </div>
</div>
<div class="ts-box">
    <div class="ts-menu is-start-icon">
        <a class="item">
            <span class="ts-icon is-star-icon"></span> 常用聯絡人
        </a>
        <a class="item">
            <span class="ts-icon is-users-icon"></span> 聯絡人
        </a>
    </div>
</div>
<div class="ts-box">
    <div class="ts-menu is-small is-start-icon">
        <a class="item">
            <span class="ts-icon is-star-icon"></span> 常用聯絡人
        </a>
        <a class="item">
            <span class="ts-icon is-users-icon"></span> 聯絡人
        </a>
    </div>
</div>
```

### [密度](menu.md#density)

選單裡項目的間距可以更密或是更寬鬆。

```html
<div class="ts-menu is-relaxed is-start-icon is-separated">
    <a class="item">
        <span class="ts-icon is-house-icon"></span> 首頁
    </a>
    <a class="item is-active">
        <span class="ts-icon is-gauge-high-icon"></span> 儀表板
    </a>
    <a class="item">
        <span class="ts-icon is-table-icon"></span> 訂單
    </a>
</div>
<div class="ts-menu is-start-icon is-separated">
    <a class="item">
        <span class="ts-icon is-house-icon"></span> 首頁
    </a>
    <a class="item is-active">
        <span class="ts-icon is-gauge-high-icon"></span> 儀表板
    </a>
    <a class="item">
        <span class="ts-icon is-table-icon"></span> 訂單
    </a>
</div>
<div class="ts-menu is-dense is-start-icon is-separated">
    <a class="item">
        <span class="ts-icon is-house-icon"></span> 首頁
    </a>
    <a class="item is-active">
        <span class="ts-icon is-gauge-high-icon"></span> 儀表板
    </a>
    <a class="item">
        <span class="ts-icon is-table-icon"></span> 訂單
    </a>
</div>
```

## 組合應用

### [側邊選單](menu.md#composition-sidebar)

透過結合[輸入欄位](input.md)和[內容區塊](content.md)可以打造出一個輕便的側邊選單。

```html
<div class="ts-box" style="width: 250px">
    <div class="ts-content">
        <div class="ts-input">
            <input type="text" placeholder="搜尋…">
        </div>
    </div>
    <div class="ts-divider"></div>
    <div class="ts-menu is-start-icon">
        <a class="item">
            <span class="ts-icon is-house-icon"></span> 首頁
        </a>
        <a class="item is-active">
            <span class="ts-icon is-gauge-high-icon"></span> 儀表板
        </a>
        <a class="item">
            <span class="ts-icon is-table-icon"></span> 訂單
        </a>
        <div class="ts-divider"></div>
        <a class="item">
            <span class="ts-icon is-gears-icon"></span> 設定
        </a>
    </div>
</div>
```

### [非貼齊選單](menu.md#composition-padded)

將選單放入[內容區塊](content.md)，能夠與[箱型容器](box.md)的邊框有間隔。

```html
<div class="ts-box" style="width: 250px">
    <div class="ts-content">
        <div class="ts-menu is-start-icon is-separated">
            <a class="item">
                <span class="ts-icon is-globe-icon"></span> 網域名稱
            </a>
            <a class="item is-active">
                <span class="ts-icon is-id-card-icon"></span> SSL 憑證
            </a>
            <a class="item">
                <span class="ts-icon is-credit-card-icon"></span> 帳務
            </a>
            <div class="ts-divider"></div>
            <a class="item">
                <span class="ts-icon is-circle-user-icon"></span> 個人資料
            </a>
        </div>
    </div>
</div>
```

### [項目選單](menu.md#composition-function-navigation)

選單的項目可以擺入[標題](header.md)、[網格系統](grid.md)或是[圖示](icon.md)。

```html
<div class="ts-box is-collapsed">
    <div class="ts-menu is-collapsed">
        <a class="item">
            <div class="ts-iconset is-outlined">
                <span class="ts-icon is-bullhorn-icon"></span>
                <div class="content">
                    <div class="title">促銷活動</div>
                    <div class="text">查看我們最新的促銷商品！</div>
                </div>
            </div>
        </a>
        <div class="ts-divider"></div>
        <a class="item">
            <div class="ts-iconset is-outlined">
                <span class="ts-icon is-ticket-simple-icon"></span>
                <div class="content">
                    <div class="title">優惠券</div>
                    <div class="text">看看我們所販售的優惠券。</div>
                </div>
            </div>
        </a>
        <div class="ts-divider"></div>
        <a class="item">
            <div class="ts-iconset is-outlined">
                <span class="ts-icon is-truck-icon"></span>
                <div class="content">
                    <div class="title">退貨</div>
                    <div class="text">
                        不滿意商品？查看我們的無條件退貨機制。
                    </div>
                </div>
            </div>
        </a>
    </div>
</div>
```

在尋找相似的元件嗎？

- [彈出式選單](dropdown.md)
- [分頁籤](tab.md)
