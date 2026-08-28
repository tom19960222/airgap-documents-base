---
collection: tocas
version: "5.0.2"
title: "進度條 - Tocas UI"
source_url: https://github.com/teacat/tocas-docs/blob/e62614c61a3fdb5d75cc5573e66f64dbfdbb7be7/docs/5.0/zh-tw/progress.html
fetched_at: 2025-03-22T01:53:10+08:00
---
```html
<div class="ts-progress">
    <div class="bar" style="--value: 50">
        <div class="text">50%</div>
    </div>
</div>
```

## 結構

### [文字](progress.md#text)

進度列裡可以擺放一個文字作為百分比標籤。

```html
<div class="ts-progress">
    <div class="bar" style="--value: 80">
        <div class="text">80%</div>
    </div>
</div>
```

## 狀態

### [啟用的](progress.md#active)

讓進度列表現出正在活動的效果。

```html
<div class="ts-progress is-active">
    <div class="bar" style="--value: 70"></div>
</div>
```

### [處理中](progress.md#processing)

明確地讓使用者知道目前的進度正在被妥善處理中。

```html
<div class="ts-progress is-processing">
    <div class="bar" style="--value: 40"></div>
</div>
```

### [不定的](progress.md#indeterminate)

請求正在傳送且等待伺服器接收。

```html
<div class="ts-progress is-indeterminate">
    <div class="bar" style="--value: 50"></div>
</div>
```

### [佇列的](progress.md#queried)

正在等待伺服器回傳結果。

```html
<div class="ts-progress is-queried">
    <div class="bar" style="--value: 30"></div>
</div>
```

## 外觀

### [空的](progress.md#empty)

當進度為零時，可以指定其狀態為空並隱藏進度條的背景。

```html
<div class="ts-progress is-empty">
    <div class="bar" style="--value: 0">
        <div class="text">0%</div>
    </div>
</div>
```

### [次要列](progress.md#secondary)

次要的進度列可以作為緩衝值或是輔助使用。

```html
<div class="ts-progress">
    <div class="bar" style="--value: 40">
        <div class="text">40%</div>
    </div>
    <div class="bar is-secondary" style="--value: 60">
        <div class="text">60%</div>
    </div>
</div>
```

### [尺寸](progress.md#sizes)

以不同的大小尺寸呈現進度條。

```html
<div class="ts-progress is-tiny">
    <div class="bar" style="--value: 50">
        <div class="text">50%</div>
    </div>
</div>
<div class="ts-progress is-small">
    <div class="bar" style="--value: 50">
        <div class="text">50%</div>
    </div>
</div>
<div class="ts-progress">
    <div class="bar" style="--value: 50">
        <div class="text">50%</div>
    </div>
</div>
<div class="ts-progress is-large">
    <div class="bar" style="--value: 50">
        <div class="text">50%</div>
    </div>
</div>
```

## 組合應用

### [相簿上傳佇列](progress.md#composition-upload)

上傳相簿照片時，通常會有一個上傳進度列和輔助文字。

```html
<div class="ts-box">
    <div class="ts-content is-secondary">
        <div class="ts-progress is-processing">
            <div class="bar" style="--value: 70">
                <div class="text">70%</div>
            </div>
        </div>
        <div class="ts-text is-description has-top-spaced-small">
            共 4 張照片，3 張正在處理中。
        </div>
    </div>
    <div class="ts-divider"></div>
    <div class="ts-content">
        <div class="ts-grid">
            <div class="column">
                <img src="image.png" width="145">
            </div>
            <div class="column is-fluid">
                <div class="ts-grid">
                    <div class="column is-fluid">
                        <div class="ts-input">
                            <input type="text" placeholder="照片標題">
                        </div>
                    </div>
                    <div class="column">
                        <button class="ts-button is-icon is-outlined">
                            <span class="ts-icon is-trash-icon"></span>
                        </button>
                    </div>
                </div>
                <div class="ts-input has-top-spaced">
                    <textarea placeholder="描述一下這張照片…"></textarea>
                </div>
            </div>
        </div>
    </div>
</div>
```

## 樣式變數

|  | 範例 | 說明 | 預設值 | 目標 |
| --- | --- | --- | --- | --- |
| --value | `50` | 進度列的百分比值。 | `0` | `.bar` |

在尋找相似的元件嗎？

- [圓形量測計](gauge.md)
- [讀取狀態](loading.md)
