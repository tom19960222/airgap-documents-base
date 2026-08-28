---
collection: tocas
version: "5.0.2"
title: "按鈕 - Tocas UI"
source_url: https://github.com/teacat/tocas-docs/blob/e62614c61a3fdb5d75cc5573e66f64dbfdbb7be7/docs/5.0/zh-tw/button.html
fetched_at: 2025-03-22T01:53:10+08:00
---
```html
<button class="ts-button">送出</button>
```

## 狀態

### [停用的](button.md#disabled)

使按鈕呈現無法互動、點擊的模樣。若按鈕是超連結，則需套用 `.is-disabled` 樣式。

```html
<button class="ts-button" disabled>停用按鈕</button>
<a class="ts-button is-disabled">停用連結</a>
```

### [讀取中](button.md#loading)

顯示旋轉的讀取圖案，使用需加上 `[disabled]` 屬性以停用按鈕互動功能。

```html
<button class="ts-button is-loading" disabled>載入中</button>
```

## 外觀

### [次要的](button.md#secondary)

較不重要的次級動作按鈕。

```html
<button class="ts-button is-secondary">取消</button>
```

### [外框線的](button.md#outlined)

僅有基本結構的外框線按鈕。

```html
<button class="ts-button is-outlined">前往拜訪</button>
```

### [負面的](button.md#negative)

警示使用者這個行為可能具有危險性。

```html
<button class="ts-button is-negative">永久銷毀資料</button>
<button class="ts-button is-negative is-outlined">放棄草稿</button>
```

### [虛無的](button.md#ghost)

不被考慮或是極少數會被執行的動作。

```html
<button class="ts-button is-ghost">忘記密碼</button>
```

### [圓角的](button.md#circular)

以圓角呈現出一個行動號召按鈕。

```html
<button class="ts-button is-circular">購買</button>
<button class="ts-button is-circular is-outlined">下載最新版本</button>
```

### [圖示的](button.md#icon)

僅帶有圖示的按鈕。

```html
<button class="ts-button is-icon">
    <span class="ts-icon is-magnifying-glass-icon"></span>
</button>
<button class="ts-button is-icon is-negative is-outlined">
    <span class="ts-icon is-trash-icon"></span>
</button>
```

### [側邊圖示的](button.md#side-icon)

按鈕的文字旁邊可以帶有輔助圖示。

```html
<button class="ts-button is-start-icon">
    <span class="ts-icon is-cart-plus-icon"></span>
    加入購物車
</button>
<button class="ts-button is-end-icon is-secondary">
    送出
    <span class="ts-icon is-check-icon"></span>
</button>
```

### [圖示標籤的](button.md#labeled-icon)

以標籤方式展現的圖示會呈現在按鈕的起始或尾端位置。

```html
<button class="ts-button is-start-labeled-icon">
    <span class="ts-icon is-heart-icon"></span>
    收藏
</button>
<button class="ts-button is-start-labeled-icon is-outlined">
    <span class="ts-icon is-paper-plane-icon"></span>
    送出
</button>
<button class="ts-button is-end-labeled-icon is-secondary">
    星號
    <span class="ts-icon is-star-icon"></span>
</button>
```

### [流動的](button.md#fluid)

按鈕的寬度可以填滿整個父容器。

```html
<button class="ts-button is-fluid">登入</button>
```

### [寬度](button.md#width)

變更按鈕的內距寬度。

```html
<button class="ts-button is-short is-outlined">短的</button>
<button class="ts-button is-outlined">預設</button>
<button class="ts-button is-wide is-outlined">寬的</button>
```

### [尺寸](button.md#sizes)

更改按鈕的尺寸與文字大小。

```html
<button class="ts-button is-small">小型按鈕</button>
<button class="ts-button">預設按鈕</button>
<button class="ts-button is-large">大型按鈕</button>
```

### [密度](button.md#density)

變更按鈕的高度，看起來更緊密或是令人感到寬鬆。

```html
<button class="ts-button is-dense">緊密按鈕</button>
<button class="ts-button">預設按鈕</button>
<button class="ts-button is-relaxed">寬鬆按鈕</button>
```

## 群組

### [按鈕群組](button.md#buttons)

將多個按鈕合併成為一個主體，多個按鈕之間會以略微可見的分隔線區隔。

```html
<div class="ts-buttons">
    <button class="ts-button">送出</button>
    <button class="ts-button is-icon">
        <span class="ts-icon is-chevron-down-icon"></span>
    </button>
</div>
<div class="ts-buttons">
    <button class="ts-button is-outlined">送出</button>
    <button class="ts-button is-outlined is-icon">
        <span class="ts-icon is-chevron-down-icon"></span>
    </button>
</div>
```

## 組合應用

### [鄰近按鈕](button.md#composition-buttons)

如果按鈕之間有相鄰另一個按鈕的話，建議使用[間隔容器](wrap.md)元件令按鈕之間帶有間隔。

```html
<div class="ts-wrap">
    <button class="ts-button">發表</button>
    <button class="ts-button is-negative is-outlined">放棄草稿</button>
</div>
```

### [喜歡與不喜歡](button.md#composition-likes)

以按鈕群組來呈現一個喜歡、不喜歡的動作按鈕群組。

```html
<div class="ts-buttons">
    <button class="ts-button is-secondary is-circular is-start-icon">
        <span class="ts-icon is-thumbs-up-icon"></span>
        324
    </button>
    <button class="ts-button is-secondary is-circular is-start-icon">
        <span class="ts-icon is-regular is-thumbs-down-icon"></span>
        7
    </button>
</div>
```

### [功能按鈕](button.md#composition-split-button)

在主要按鈕旁邊擺放會開啟[彈出式選單](dropdown.md)的輔助按鈕。

```html
<div class="ts-buttons">
    <button class="ts-button">開始遊戲</button>
    <button class="ts-button is-icon" data-dropdown="dropdown">
        <span class="ts-icon is-gear-icon"></span>
    </button>
</div>
<div class="ts-dropdown" id="dropdown">
    <button class="item">遊戲設定</button>
    <button class="item">掃描與修復</button>
    <div class="divider"></div>
    <button class="item">移除遊戲</button>
</div>
```

在尋找相似的元件嗎？

- [關閉按鈕](close.md)
