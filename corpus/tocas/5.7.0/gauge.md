---
collection: tocas
version: "5.7.0"
title: "圓形量測計 - Tocas UI"
source_url: https://github.com/teacat/tocas-docs/blob/ef8248b165f458215fb8f18bb400c4bfba1767fa/docs/5.7/zh-tw/gauge.html
fetched_at: 2026-02-25T00:25:36+08:00
---
```html
<div class="ts-gauge">
    <div class="bar" style="--value: 40">
        <div class="text">40%</div>
    </div>
</div>
```

## 外觀

### [圓形的](gauge.md#circular)

以全圓形無缺口的方式呈現整個量測計。

```html
<div class="ts-gauge is-circular">
    <div class="bar" style="--value: 70">
        <div class="text">70%</div>
    </div>
</div>
```

### [上升的](gauge.md#uplifted)

呈現出類似上升數值的計數器，如：劑量、溫度、濕度。

```html
<div class="ts-gauge is-uplifted">
    <div class="bar" style="--value: 50">
        <div class="text">50%</div>
    </div>
</div>
```

### [置中的](gauge.md#centered)

使其置中顯示。

```html
<div class="ts-gauge is-centered">
    <div class="bar" style="--value: 40">
        <div class="text">40%</div>
    </div>
</div>
```

### [尺寸](gauge.md#sizes)

更改圓形量測計的大小。

```html
<div class="ts-gauge is-small">
    <div class="bar" style="--value: 30">
        <div class="text">30%</div>
    </div>
</div>
<div class="ts-gauge">
    <div class="bar" style="--value: 30">
        <div class="text">30%</div>
    </div>
</div>
<div class="ts-gauge is-large">
    <div class="bar" style="--value: 30">
        <div class="text">30%</div>
    </div>
</div>
```

## 組合應用

### [傳輸計量](gauge.md#composition-usage)

雲端檔案傳輸空間通常會有一個顯示目前剩餘額度與流量的相關計數器。

```html
<div class="ts-grid is-evenly-divided">
    <div class="column">
        <div class="ts-wrap is-middle-aligned">
            <div class="ts-gauge is-small is-circular">
                <div class="bar" style="--value: 38">
                    <div class="text">38%</div>
                </div>
            </div>
            <div>
                <div class="ts-text is-bold">空間</div>
                19.12 GB / 50 GB
            </div>
        </div>
    </div>
    <div class="column">
        <div class="ts-wrap is-middle-aligned">
            <div class="ts-gauge is-small is-circular">
                <div class="bar" style="--value: 100">
                    <div class="text">---</div>
                </div>
            </div>
            <div>
                <div class="ts-text is-bold">傳輸</div>
                0 B 已使用
            </div>
        </div>
    </div>
</div>
```

### [智慧家庭](gauge.md#composition-temperature)

用以指示目前溫度、濕度的測量計。

```html
<div class="ts-wrap is-middle-aligned">
    <div class="ts-gauge is-uplifted">
        <div class="bar" style="--value: 80">
            <div class="text">
                <span class="ts-icon is-big is-temperature-full-icon"></span>
            </div>
        </div>
    </div>
    <div>
        <div class="ts-statistic">
            <div class="value">32 °C</div>
            <div class="comparison is-increased">2 °C</div>
        </div>
        房間溫度
    </div>
</div>
```

## 樣式變數

|  | 說明 | 預設值 | 目標 |
| --- | --- | --- | --- |
| --value | 進度列的百分比值。 | `0` | `.bar` |

在尋找相似的元件嗎？

- [讀取狀態](loading.md)
- [進度條](progress.md)
