---
collection: tocas
version: "5.0.2"
title: "欄位分組 - Tocas UI"
source_url: https://github.com/teacat/tocas-docs/blob/e62614c61a3fdb5d75cc5573e66f64dbfdbb7be7/docs/5.0/zh-tw/fieldset.html
fetched_at: 2025-03-22T01:53:10+08:00
---
```html
<fieldset class="ts-fieldset">
    <legend>額外附註</legend>
    <div class="ts-list is-unordered">
        <div class="item">這個世界只是一個假象，所有肉眼可見的東西都不是真的。</div>
        <div class="item">你從來沒有到過這個地方。</div>
        <div class="item">如果你覺得這一切都很眼熟，請務必聯繫服務人員。</div>
    </div>
</fieldset>
```

## 狀態

### [停用的](fieldset.md#disabled)

使欄位分組呈現無法互動、點擊的模樣，裡面的表單欄位都會被停用且無法互動。

```html
<fieldset class="ts-fieldset" disabled>
    <legend>被停用的表單</legend>
    <div class="ts-grid is-2-columns">
        <div class="column">
            <div class="ts-text is-label">收件人</div>
            <div class="ts-input has-top-spaced">
                <input type="text" value="Yami Odymel">
            </div>
        </div>
        <div class="column">
            <div class="ts-text is-label">聯絡電話</div>
            <div class="ts-input has-top-spaced">
                <input type="text" value="0987123456">
            </div>
        </div>
    </div>
</fieldset>
```

## 外觀

### [較密的](fieldset.md#dense)

變更元件的內距，令元素之間看起來更密集。

```html
<fieldset class="ts-fieldset is-dense">
    <legend>伊繁星最高協議</legend>
    所有隸屬卡莉絲伊繁星旗下已發佈或是正於計劃中之產品其開發者人員皆須遵守的規則。
</fieldset>
```

## 組合應用

### [表單群組](fieldset.md#composition-fieldset)

在表單裡可以透過欄位群組將某些輸入欄位獨立成一個群組。

```html
<div class="ts-grid is-2-columns">
    <div class="column">
        <div class="ts-text is-label">申辦人姓名</div>
        <div class="ts-input has-top-spaced">
            <input type="text">
        </div>
    </div>
    <div class="column">
        <div class="ts-text is-label">監護人姓名</div>
        <div class="ts-input has-top-spaced">
            <input type="text">
        </div>
    </div>
</div>
<fieldset class="ts-fieldset has-top-spaced">
    <legend>機密資料</legend>
    <div class="ts-grid is-3-columns">
        <div class="column">
            <div class="ts-text is-label">信用卡卡號</div>
            <div class="ts-input has-top-spaced">
                <input type="text">
            </div>
        </div>
        <div class="column">
            <div class="ts-text is-label">到期日</div>
            <div class="ts-input has-top-spaced">
                <input type="text">
            </div>
        </div>
        <div class="column">
            <div class="ts-text is-label">安全碼</div>
            <div class="ts-input has-top-spaced">
                <input type="text">
            </div>
        </div>
    </div>
</fieldset>
```
