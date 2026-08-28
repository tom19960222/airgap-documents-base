---
collection: tocas
version: "5.7.0"
title: "彈出式選單 - Tocas UI"
source_url: https://github.com/teacat/tocas-docs/blob/ef8248b165f458215fb8f18bb400c4bfba1767fa/docs/5.7/zh-tw/dropdown.html
fetched_at: 2026-02-25T00:25:36+08:00
---
```html
<button class="ts-button is-start-icon" data-dropdown="dropdown">
    <span class="ts-icon is-chevron-down-icon"></span>
    打開選單
</button>
<div class="ts-dropdown" id="dropdown">
    <button class="item">新增檔案</button>
    <button class="item">移至回收桶</button>
    <button class="item">檢視資訊</button>
</div>
```

## 概要

點擊帶有 `[data-dropdown]` 屬性的按鈕可以開、關對應 `[id]` 的彈出式選單。

## 狀態

### [停用的](dropdown.md#disabled)

使項目呈現無法互動、點擊的模樣。若項目是超連結，則需套用 `.is-disabled` 樣式。

```html
<div class="ts-dropdown is-visible">
    <button class="item">無線通訊</button>
    <button class="item" disabled>地圖紀錄</button>
    <a class="item is-disabled">導航設定</a>
</div>
```

### [啟用的](dropdown.md#active)

表示目前已經被啟用或是正在呈現的相關功能。

```html
<div class="ts-dropdown is-visible">
    <a class="item">個人資料</a>
    <a class="item is-active">位置分享</a>
    <a class="item">設定</a>
</div>
```

### [已選擇](dropdown.md#selected)

表示某個項目被選中。

```html
<div class="ts-dropdown is-visible">
    <button class="item">5 分鐘後提醒我</button>
    <button class="item is-selected">1 小時候提醒我</button>
    <button class="item">永不提醒</button>
</div>
```

## 結構

### [註釋](dropdown.md#description)

以較淺的文字說明特定項目。

```html
<div class="ts-dropdown is-visible">
    <button class="item">
        下載
        <span class="description">Ctrl + D</span>
    </button>
    <button class="item">
        儲存圖片
        <span class="description">Ctrl + S</span>
    </button>
    <button class="item">
        全選
        <span class="description">Ctrl + A</span>
    </button>
</div>
```

### [標題](dropdown.md#header)

分類項目並且帶有標題。

```html
<div class="ts-dropdown is-visible">
    <div class="header">台灣</div>
    <button class="item">高雄市, 鳳山區</button>
    <button class="item">台北市, 大安區</button>
    <div class="header">香港</div>
    <button class="item">長沙灣, 海麗街</button>
    <button class="item">元朗, 福順街</button>
</div>
```

### [分隔線](dropdown.md#divider)

以線段區隔不同種類的項目。

```html
<div class="ts-dropdown is-visible">
    <button class="item">遊戲設定</button>
    <button class="item">掃描與修復</button>
    <div class="divider"></div>
    <button class="item">移除遊戲</button>
</div>
```

## 項目外觀

### [負面的](dropdown.md#negative)

表示某個項目的行為具有危險性。

```html
<div class="ts-dropdown is-visible">
    <a class="item">檢視文件</a>
    <a class="item is-negative">刪除</a>
</div>
```

## 外觀

### [分開的](dropdown.md#separated)

使項目不再緊鄰邊緣且有空白區隔。

```html
<div class="ts-dropdown is-separated is-visible">
    <button class="item">
        <span class="ts-icon is-user-icon"></span> 使用者
    </button>
    <button class="item is-active">
        <span class="ts-icon is-house-icon"></span> 首頁
    </button>
    <button class="item">
        <span class="ts-icon is-newspaper-icon"></span> 新聞
    </button>
</div>
```

### [縮排的](dropdown.md#indented)

使項目往內縮排，適合與標題項目一同使用。

```html
<div class="ts-dropdown is-visible">
    <div class="header">攻擊魔法</div>
    <button class="item is-indented">火球術</button>
    <button class="item is-indented">隕石術</button>
</div>
```

### [帶圖示的](dropdown.md#icon)

選單項目的起始或結束位置可以帶有圖示輔助。

```html
<div class="ts-dropdown is-start-icon is-visible">
    <button class="item">
        <span class="ts-icon is-magnifying-glass-icon"></span> 搜尋
    </button>
    <button class="item">
        <span class="ts-icon is-vials-icon"></span> 實驗區
    </button>
    <button class="item">
        <span class="ts-icon is-atom-icon"></span> 原子測試
    </button>
</div>
<div class="ts-dropdown is-end-icon is-visible" style="margin-left: 11rem">
    <button class="item">
        我的最愛 <span class="ts-icon is-heart-icon"></span>
    </button>
    <button class="item">
        已讚好內容 <span class="ts-icon is-thumbs-up-icon"></span>
    </button>
    <button class="item">
        封存項目 <span class="ts-icon is-box-archive-icon"></span>
    </button>
</div>
```

### [密度](dropdown.md#density)

下拉式選單裡項目的間距可以更密或是更寬鬆。

```html
<div class="ts-dropdown is-relaxed is-visible">
    <button class="item">寬鬆項目</button>
    <button class="item is-active">寬鬆項目</button>
    <button class="item">寬鬆項目</button>
</div>
<div class="ts-dropdown is-visible" style="margin-left: 11rem">
    <button class="item">預設項目</button>
    <button class="item is-active">預設項目</button>
    <button class="item">預設項目</button>
</div>
<div class="ts-dropdown is-dense is-visible" style="margin-left: 22rem">
    <button class="item">緊密項目</button>
    <button class="item is-active">緊密項目</button>
    <button class="item">緊密項目</button>
</div>
```

## 組合應用

### [頂部列選單](dropdown.md#composition-topbar)

[頂部列](app-topbar.md)的尾側可以擺放一個帶有進階功能的選單。

```html
<div class="ts-app-topbar">
    <div class="start">
        <div class="item is-text">應用程式</div>
    </div>
    <div class="end">
        <button class="item" data-dropdown="dropdown-menu">
            <span class="ts-icon is-ellipsis-vertical-icon"></span>
        </button>
    </div>
</div>
<div class="ts-dropdown" id="dropdown-menu" data-position="bottom-end">
    <button class="item">關於</button>
    <button class="item">檢查更新</button>
</div>
```

### [分頁選單](dropdown.md#composition-tab)

有時候[分頁籤](tab.md)的項目太多，可以考慮收納進下拉式選單中。

```html
<div class="ts-tab is-pilled">
    <button class="item">主打內容</button>
    <button class="item">最新</button>
    <button class="item" data-dropdown="dropdown-links">
        <span class="ts-icon is-ellipsis-icon"></span>
        更多
    </button>
</div>
<div class="ts-dropdown" id="dropdown-links">
    <button class="item">遊戲</button>
    <button class="item">音樂</button>
    <button class="item">影片</button>
</div>
```

## 屬性設定

|  | 說明 | 預設值 | 目標 |
| --- | --- | --- | --- |
| [data-position] | 彈出式選單展開時的偏好位置。   - `top` - `top-start` - `top-end` - `bottom` - `bottom-start` - `bottom-end` | `bottom-start` | `.ts-dropdown` |
| [data-collapse] | 指定選單何時會關閉，  使用空白分隔多個觸發方式，如：`trigger item`。   - `trigger` 當觸發按鈕被按下。 - `item` 當項目被按下。 | `trigger item` | `.ts-dropdown` |

## 樣式變數

|  | 說明 | 預設值 | 目標 |
| --- | --- | --- | --- |
| --min-width | 選單最小的寬度。 | `10rem` | `.ts-dropdown` |

在尋找相似的元件嗎？

- [選單](menu.md)
- [下拉式選擇](select.md)
