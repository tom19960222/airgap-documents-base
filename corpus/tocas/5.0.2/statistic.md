---
collection: tocas
version: "5.0.2"
title: "統計數據 - Tocas UI"
source_url: https://github.com/teacat/tocas-docs/blob/e62614c61a3fdb5d75cc5573e66f64dbfdbb7be7/docs/5.0/zh-tw/statistic.html
fetched_at: 2025-03-22T01:53:10+08:00
---
```html
<div class="ts-statistic">
    <div class="value">8,964</div>
    <div class="comparison is-increased">32</div>
</div>
```

## 結構

### [數值](statistic.md#value)

數值會以較大的字體呈現。

```html
<div class="ts-statistic">
    <div class="value">19,293</div>
</div>
```

### [比較數值](statistic.md#comparison)

表示這個數據自上次以來的差別值。

```html
<div class="ts-statistic">
    <div class="value">42,689</div>
    <div class="comparison is-increased">195</div>
</div>
<div class="ts-statistic">
    <div class="value">1,998</div>
    <div class="comparison is-decreased">13</div>
</div>
```

### [單位](statistic.md#unit)

指出這個數據的單位為何。

```html
<div class="ts-statistic">
    <div class="value">10,000</div>
    <div class="unit">次</div>
</div>
```

### [圖示](statistic.md#icon)

在數值旁擺放輔助用的圖示。

```html
<div class="ts-statistic">
    <span class="ts-icon is-eye-icon"></span>
    <div class="value">30,000</div>
</div>
```

## 組合應用

### [標籤文字](statistic.md#composition-label)

使用統計數據時，通常會建議在其上、下方擺放文字元素表明這個數據是什麼。

```html
<div class="ts-text is-label">下載次數</div>
<div class="ts-statistic">
    <div class="value">10,000</div>
    <div class="unit">次</div>
</div>
```
