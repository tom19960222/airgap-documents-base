---
collection: tocas
version: "5.7.0"
title: "分頁籤 - Tocas UI"
source_url: https://github.com/teacat/tocas-docs/blob/ef8248b165f458215fb8f18bb400c4bfba1767fa/docs/5.7/zh-tw/tab.html
fetched_at: 2026-02-25T00:25:36+08:00
---
```html
<div class="ts-tab">
    <a class="item">
        <span class="ts-icon is-list-icon"></span>
        項目
    </a>
    <a class="item is-active">
        <span class="ts-icon is-chart-line-icon"></span>
        活動
    </a>
    <a class="item">
        <span class="ts-icon is-scroll-icon"></span>
        合約
    </a>
</div>
```

## 狀態

### [啟用的](tab.md#active)

指示目前所在的位置項目。

```html
<div class="ts-tab">
    <a class="item">通話紀錄</a>
    <a class="item is-active">簡訊</a>
    <a class="item">安全防護</a>
    <a class="item">聯絡人</a>
</div>
```

### [停用的](tab.md#disabled)

使項目呈現無法互動、點擊的模樣。若項目是超連結，則需套用 `.is-disabled` 樣式。

```html
<div class="ts-tab">
    <a class="item">
        <span class="ts-icon is-compass-icon"></span>
        探索
    </a>
    <button class="item" disabled>
        <span class="ts-icon is-car-icon"></span>
        出發
    </button>
    <a class="item is-disabled">
        <span class="ts-icon is-bell-icon"></span>
        最新動態
    </a>
</div>
```

## 外觀

### [藥丸的](tab.md#pilled)

讓分頁項目帶有圓角使其看起來像藥丸。

```html
<div class="ts-tab is-pilled">
    <a class="item">詳細資訊</a>
    <a class="item is-active">擁有者</a>
    <a class="item">區塊鏈資訊</a>
    <a class="item">屬性</a>
</div>
```

### [次要的](tab.md#secondary)

使啟用項目的語氣不會那麼沈重。

```html
<div class="ts-tab is-secondary is-pilled">
    <a class="item">
        <span class="ts-icon is-list-icon"></span>
        交易紀錄
    </a>
    <a class="item">
        <span class="ts-icon is-money-check-dollar-icon"></span>
        內部轉移
    </a>
    <a class="item is-active">
        <span class="ts-icon is-calendar-day-icon"></span>
        事件
    </a>
    <a class="item">
        <span class="ts-icon is-chart-bar-icon"></span>
        分析
    </a>
</div>
```

### [短指示的](tab.md#short-indicated)

指示器不會超過分頁項目本身的長度。

```html
<div class="ts-tab is-short-indicated">
    <a class="item">收藏</a>
    <a class="item is-active">音樂</a>
    <a class="item">影片</a>
</div>
<div class="ts-tab is-very-short-indicated">
    <a class="item">收藏</a>
    <a class="item is-active">音樂</a>
    <a class="item">影片</a>
</div>
```

### [片段的](tab.md#segmented)

以區段的方式呈現出一個切換器的效果。

```html
<div class="ts-tab is-segmented">
    <a class="item">項目</a>
    <a class="item is-active">群組</a>
    <a class="item">資訊</a>
</div>
```

### [顯目指示的](tab.md#highlighted)

啟用的項目會較為明顯，而其他分頁項目則會淡化呈現。

```html
<div class="ts-tab is-highlighted">
    <a class="item">首頁</a>
    <a class="item is-active">通知</a>
    <a class="item">社團</a>
</div>
```

### [流動的](tab.md#fluid)

使整個分頁籤符合父容器的寬度。

```html
<div class="ts-tab is-fluid">
    <a class="item">個人檔案</a>
    <a class="item is-active">裝備</a>
    <a class="item">道具</a>
    <a class="item">技能</a>
</div>
```

### [項目對齊](tab.md#aligns)

更改項目的起始位置。

```html
<div class="ts-tab is-start-aligned">
    <a class="item">相片</a>
    <a class="item is-active">搜尋</a>
    <a class="item">共享</a>
</div>
<div class="ts-tab is-center-aligned">
    <a class="item">相片</a>
    <a class="item is-active">搜尋</a>
    <a class="item">共享</a>
</div>
<div class="ts-tab is-end-aligned">
    <a class="item">相片</a>
    <a class="item is-active">搜尋</a>
    <a class="item">共享</a>
</div>
```

### [尺寸](tab.md#sizes)

更改分頁籤的大小。

```html
<div class="ts-tab is-small is-pilled">
    <a class="item">詳細資訊</a>
    <a class="item is-active">擁有者</a>
    <a class="item">區塊鏈資訊</a>
</div>
<div class="ts-tab is-pilled">
    <a class="item">詳細資訊</a>
    <a class="item is-active">擁有者</a>
    <a class="item">區塊鏈資訊</a>
</div>
<div class="ts-tab is-large is-pilled">
    <a class="item">詳細資訊</a>
    <a class="item is-active">擁有者</a>
    <a class="item">區塊鏈資訊</a>
</div>
```

### [寬鬆的](tab.md#relaxed)

使項目之間看起來更寬鬆。

```html
<div class="ts-tab">
    <a class="item is-active">未讀</a>
    <a class="item">全部通知</a>
    <a class="item">封存</a>
</div>
<div class="ts-tab is-relaxed">
    <a class="item is-active">未讀</a>
    <a class="item">全部通知</a>
    <a class="item">封存</a>
</div>
```

### [較密的](tab.md#dense)

變更元件的內距，令元素之間看起來更密集。

```html
<div class="ts-tab is-dense is-segmented">
    <a class="item">實際效果</a>
    <a class="item is-active">預覽</a>
</div>
```

### [更高的](tab.md#tall)

讓分頁項目有更高的上下內距，在某些樣式下會使項目文字距離指示器更遠。

```html
<div class="ts-tab">
    <a class="item is-active">閒聊</a>
    <a class="item">同人</a>
    <a class="item">官方</a>
</div>
<div class="ts-tab is-tall">
    <a class="item is-active">閒聊</a>
    <a class="item">同人</a>
    <a class="item">官方</a>
</div>
```

## 組合應用

### [分頁內容](tab.md#composition-tab)

擺放在某些區塊的上方，可以就像真的在進行分頁切換一樣。

```html
<div class="ts-box">
    <div class="ts-content is-fitted is-secondary">
        <div class="ts-tab">
            <a class="item">音樂</a>
            <a class="item is-active">貼文</a>
            <a class="item">影片</a>
        </div>
    </div>
    <div class="ts-divider"></div>
    <div class="ts-content">
        早安，我的朋友！
    </div>
</div>
```

### [切換面板](tab.md#composition-switch)

片段分頁籤和表格放置在一起，可以用來切換項目的檢視狀態。

```html
<div class="ts-box">
    <div class="ts-content is-dense">
        <div class="ts-grid">
            <div class="column is-fluid">
                <div class="ts-tab is-segmented">
                    <a class="item">項目</a>
                    <a class="item is-active">分類</a>
                </div>
            </div>
            <div class="column">
                <button class="ts-button is-outlined is-short is-end-icon">
                    編輯
                    <span class="ts-icon is-pen-to-square-icon"></span>
                </button>
            </div>
        </div>
    </div>
    <div class="ts-divider"></div>
    <table class="ts-table">
        <thead>
            <tr>
                <th>名稱</th>
                <th class="is-end-aligned">數量</th>
                <th class="is-end-aligned">金額</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>磁力共振掃描</td>
                <td class="is-end-aligned">1</td>
                <td class="is-end-aligned">$ 40,222</td>
            </tr>
            <tr>
                <td>電腦斷層掃描</td>
                <td class="is-end-aligned">1</td>
                <td class="is-end-aligned">$ 20,000</td>
            </tr>
            <tr>
                <td>正電子發射斷層掃描</td>
                <td class="is-end-aligned">1</td>
                <td class="is-end-aligned">$ 31,000</td>
            </tr>
        </tbody>
    </table>
</div>
```

## JavaScript 功能

### [透過屬性標籤控制](tab.md#module-tab)

點擊帶有 `[data-tab]` 屬性的按鈕可以切換對應 `[id]` 的元素。

```html
<div class="ts-box">
    <div class="ts-tab">
        <button class="item" data-tab="tab-transfer">
            轉帳
        </button>
        <button class="item is-active" data-tab="tab-activities">
            紀錄
        </button>
        <button class="item" disabled>
            停用項目
        </button>
    </div>
    <div class="ts-divider"></div>
    <div class="ts-content" id="tab-transfer">
        這是「轉帳」頁面。
    </div>
    <div class="ts-content" id="tab-activities">
        這是「紀錄」頁面。
    </div>
</div>
```

在尋找相似的元件嗎？

- [項目切換](selection.md)
