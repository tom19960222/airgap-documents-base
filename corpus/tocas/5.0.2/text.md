---
collection: tocas
version: "5.0.2"
title: "文字 - Tocas UI"
source_url: https://github.com/teacat/tocas-docs/blob/e62614c61a3fdb5d75cc5573e66f64dbfdbb7be7/docs/5.0/zh-tw/text.html
fetched_at: 2025-03-22T01:53:10+08:00
---
```html
<span class="ts-text">Hello, world!</span>
```

## 種類

### [連結](text.md#link)

基本的連結樣式可套用在一般文字上，這能讓使用者一目瞭然這是個超連結。

```html
<a class="ts-text is-link">Hello, world!</a>
```

### [外部連結](text.md#external-link)

以圖示輔助告訴使用者點擊這個連結將會另開視窗。

```html
關於更多消息，請參閱<a class="ts-text is-external-link">區塊鏈白皮書</a>。
```

### [圖示連結](text.md#icon-link)

在側邊帶有圖示的連結。

```html
<a class="ts-text is-icon-link">
    <span class="ts-icon is-arrow-left-icon"></span>
    返回上一頁
</a>
```

### [無連結裝飾的](text.md#undecorated)

透過移除連結裝飾，可以移除連結常態時的底線。

```html
<a class="ts-text is-undecorated">這個連結</a>只有滑過時才有底線。
```

### [程式碼](text.md#code)

展示一個程式碼片段。

```html
透過 <span class="ts-text is-code">ts-button</span> 能夠讓你的按鈕看起來特別像按鈕，蒸蚌！
```

### [標籤](text.md#label)

作為某個物體的標籤，例如：輸入欄位、數據。

```html
<span class="ts-text is-label">使用者帳號</span>
<div class="ts-input has-top-spaced-small">
    <input type="text">
</div>
```

### [註釋](text.md#description)

用來說明某些行為的小型不起眼文字。

```html
<button class="ts-button">儲存變更</button>
<div class="ts-text is-description has-top-spaced-small">
    由於系統快取的緣故，你所造成的變更會在 24 小時之後才生效。
</div>
```

### [上標與下標](text.md#sup-and-sub)

將指定文字偏上或偏下。

```html
<p>朋友買了一件衣料，綠色的底子帶白色方格，當她拿給我們看時<span class="ts-text is-sup">[8]</span>：</p>
<p>「關我屁事？」我說。</p>
<p>我們不禁哄堂大笑，同樣的一件衣料<span class="ts-text is-sub">[9]</span>到底關其他人屁事。</p>
```

### [快捷鍵的](text.md#key)

類似鍵盤快捷鍵的提示文字。

```html
按下 <span class="ts-text is-key">shift</span> + <span class="ts-text is-key">H</span> 以開始。
```

### [螢光標記的](text.md#mark)

讓文字看起來就像被螢光筆標記一樣。

```html
當我閉上眼，我，什麼都<span class="ts-text is-mark">看不見</span>
```

## 狀態

### [停用的](text.md#disabled)

已經不再作為可參考的文字敘述。

```html
<span class="ts-text is-disabled">我們從不懷疑自己是不是沒殺人的殺人犯。</span>
```

### [必要的](text.md#required)

以紅色的星號在文字尾端作為必填提示，通常會和標籤一起搭配表示某個輸入欄位不得留空。

```html
<label class="ts-checkbox">
    <input type="checkbox" checked>
    <span class="ts-text is-required">我已年滿 18 歲</span>
</label>
```

## 外觀

### [可編輯的](text.md#editable)

以虛線和游標提示使用者點擊這段文字也許可以即時編輯。

```html
金額為：<span class="ts-text is-editable">$ 3,600</span>
```

### [次要的](text.md#secondary)

以較不重要的顏色使文字淡化呈現。

```html
<span class="ts-text is-secondary">程式正在執行中…</span>
```

### [粗體的](text.md#bold)

以粗體的方式標註某個文字讓使用者知道重點為何。

```html
是時候按下前面的<span class="ts-text is-bold">按鈕</span>來揭曉這一切了！
```

### [沈重的](text.md#heavy)

以最粗的方式標註某段文字。

```html
<span class="ts-text is-heavy">噢不</span>！今天是芥末日！
```

### [斜體的](text.md#italic)

令文字傾斜，通常用於特別標註某個代名詞或是該注意的事物。

```html
我不建議你打開後面的那扇門，在那裡面有一個他親自打造的<span class="ts-text is-italic">世界</span>。
```

### [刪除線的](text.md#deleted)

在中間劃條刪除線表示以不再提供參考。

```html
<span class="ts-text is-deleted">這段文字已經不再具有參考價值。</span>
```

### [底線的](text.md#underlined)

在底部下劃一條線，通常用以標註特別名稱。

```html
在<span class="ts-text is-underlined">卡萊迪亞</span>的中央重生區有著一個巨大的水晶。
```

### [截斷的](text.md#truncated)

文字超過一定寬度之後就會被截斷而不會換行或溢出，通常父容器需要有個固定寬度。

```html
<div class="ts-text is-truncated" style="max-width: 300px">
    豔陽高照，前方的道路什麼都看不見。明明不清楚前方的事物，卻感覺自己正在邁向的是一個新世界。
</div>
```

### [負面的](text.md#negative)

表達這個文字帶有危險、負面的意味，可以用來敘述某個物體的狀態或是顯示錯誤訊息。

```html
<span class="ts-text is-negative">伺服器已經損毀！</span>
```

### [大、小寫的](text.md#uppercased-and-lowercased)

強制使某段文字大小寫，僅能用於英文。

```html
<div class="ts-text is-uppercased">Here comes another world.</div>
<div class="ts-text is-lowercased">Here comes another world.</div>
```

### [對齊](text.md#aligns)

更改文字的對齊方式。

```html
<div class="ts-text is-start-aligned">置起始位置</div>
<div class="ts-text is-center-aligned">置中對齊</div>
<div class="ts-text is-end-aligned">置結束位置</div>
```

### [均衡對齊](text.md#justify-aligned)

在文字換行時，自動均衡字元之間的空白寬度來避免結尾有視覺上不平衡的空白。

```html
<div class="ts-text is-justify-aligned">
    This paragraph uses "Justify" to automatically equalize the gaps between characters for a more balanced and comfortable visual appearance. 這段文字使用了《均衡對齊》能夠自動均衡字元之間的空白，使視覺上看起來更平衡舒適。
</div>
```

### [尺寸](text.md#sizes)

更改文字的大小。

```html
<div class="ts-text is-tiny">(微小) Tocas UI 來自台灣。</div>
<div class="ts-text is-small">(小的) Tocas UI 來自台灣。</div>
<div class="ts-text is-medium">(預設) Tocas UI 來自台灣。</div>
<div class="ts-text is-large">(大的) Tocas UI 來自台灣。</div>
<div class="ts-text is-big">(更大) Tocas UI 來自台灣。</div>
<div class="ts-text is-huge">(巨大) Tocas UI 來自台灣。</div>
<div class="ts-text is-massive">(重量級) Tocas UI 來自台灣。</div>
```

在尋找相似的元件嗎？

- [標題](header.md)
