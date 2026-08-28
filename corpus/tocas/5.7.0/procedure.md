---
collection: tocas
version: "5.7.0"
title: "步驟指示器 - Tocas UI"
source_url: https://github.com/teacat/tocas-docs/blob/ef8248b165f458215fb8f18bb400c4bfba1767fa/docs/5.7/zh-tw/procedure.html
fetched_at: 2026-02-25T00:25:36+08:00
---
```html
<div class="ts-procedure">
    <div class="item">
        <div class="content">
            <div class="indicator"></div>
            <div class="label">帳單對象</div>
        </div>
    </div>
    <div class="item">
        <div class="content">
            <div class="indicator"></div>
            <div class="label">購物車</div>
        </div>
    </div>
    <div class="item">
        <div class="content">
            <div class="indicator"></div>
            <div class="label">付款</div>
        </div>
    </div>
</div>
```

## 結構

### [圖示](procedure.md#icon)

每個步驟都可以帶有象徵圖示。

```html
<div class="ts-procedure">
    <a class="item is-completed">
        <div class="content">
            <div class="indicator">
                <span class="ts-icon is-user-icon"></span>
            </div>
            <div class="label">帳號建立</div>
        </div>
    </a>
    <a class="item is-active">
        <div class="content">
            <div class="indicator">
                <span class="ts-icon is-id-card-icon"></span>
            </div>
            <div class="label">身份驗證</div>
        </div>
    </a>
    <a class="item">
        <div class="content">
            <div class="indicator">
                <span class="ts-icon is-eye-icon"></span>
            </div>
            <div class="label">等待審核</div>
        </div>
    </a>
</div>
```

### [註釋](procedure.md#description)

以註釋大略解釋某個步驟的行為。

```html
<div class="ts-procedure">
    <a class="item">
        <div class="content">
            <div class="indicator"></div>
            <div class="label">
                下標
                <div class="description">決定此標的物價格。</div>
            </div>
        </div>
    </a>
    <a class="item">
        <div class="content">
            <div class="indicator"></div>
            <div class="label">
                付款
                <div class="description">支付相關費用。</div>
            </div>
        </div>
    </a>
    <a class="item">
        <div class="content">
            <div class="indicator"></div>
            <div class="label">
                領回
                <div class="description">取得已得標商品。</div>
            </div>
        </div>
    </a>
</div>
```

## 狀態

### [已完成](procedure.md#completed)

表示某個步驟已經完成。

```html
<div class="ts-procedure">
    <a class="item is-completed">
        <div class="content">
            <div class="indicator"></div>
            <div class="label">連接電源</div>
        </div>
    </a>
    <a class="item">
        <div class="content">
            <div class="indicator"></div>
            <div class="label">啟用 WiFi</div>
        </div>
    </a>
    <a class="item">
        <div class="content">
            <div class="indicator"></div>
            <div class="label">掃描 QR Code</div>
        </div>
    </a>
</div>
```

### [啟用的](procedure.md#active)

標明目前正處於的步驟狀態。

```html
<div class="ts-procedure">
    <a class="item is-completed">
        <div class="content">
            <div class="indicator"></div>
            <div class="label">建立訂單</div>
        </div>
    </a>
    <a class="item is-active">
        <div class="content">
            <div class="indicator"></div>
            <div class="label">配送貨物</div>
        </div>
    </a>
    <a class="item">
        <div class="content">
            <div class="indicator"></div>
            <div class="label">完成訂單</div>
        </div>
    </a>
</div>
```

### [處理中](procedure.md#processing)

表示目前背景正在處理的步驟。

```html
<div class="ts-procedure">
    <a class="item is-completed">
        <div class="content">
            <div class="indicator"></div>
            <div class="label">提出修正</div>
        </div>
    </a>
    <a class="item is-processing">
        <div class="content">
            <div class="indicator"></div>
            <div class="label">等待通知</div>
        </div>
    </a>
    <a class="item">
        <div class="content">
            <div class="indicator"></div>
            <div class="label">獲得獎勵</div>
        </div>
    </a>
</div>
```

### [停用的](procedure.md#disabled)

淡化某個步驟令使用者無法回頭或是表示尚未有能夠到達該步驟的條件。

```html
<div class="ts-procedure">
    <a class="item is-completed">
        <div class="content">
            <div class="indicator"></div>
            <div class="label">建立 PIN 碼</div>
        </div>
    </a>
    <a class="item is-processing">
        <div class="content">
            <div class="indicator"></div>
            <div class="label">初始化指紋辨識</div>
        </div>
    </a>
    <a class="item is-disabled">
        <div class="content">
            <div class="indicator"></div>
            <div class="label">配置重設密碼</div>
        </div>
    </a>
</div>
```

## 外觀

### [緊緻的](procedure.md#compact)

以更小化的方式呈現步驟指示。

```html
<div class="ts-procedure is-compact">
    <a class="item is-completed">
        <div class="content">
            <div class="indicator"></div>
            <div class="label">上傳檔案</div>
        </div>
    </a>
    <a class="item is-processing">
        <div class="content">
            <div class="indicator"></div>
            <div class="label">設定密碼</div>
        </div>
    </a>
    <a class="item">
        <div class="content">
            <div class="indicator"></div>
            <div class="label">分享給朋友</div>
        </div>
    </a>
</div>
```

### [層疊的](procedure.md#stacked)

文字可以與指示器層疊，這樣就不會使用過多的寬度空間。

```html
<div class="ts-procedure is-stacked">
    <a class="item is-completed">
        <div class="content">
            <div class="indicator"></div>
            <div class="label">建立伺服器</div>
        </div>
    </a>
    <a class="item is-processing">
        <div class="content">
            <div class="indicator"></div>
            <div class="label">設定 IP 位址</div>
        </div>
    </a>
    <a class="item">
        <div class="content">
            <div class="indicator"></div>
            <div class="label">封鎖來源</div>
        </div>
    </a>
</div>
```

### [負面的](procedure.md#negative)

表示某個環節出錯了。

```html
<div class="ts-procedure">
    <a class="item is-negative">
        <div class="content">
            <div class="indicator"></div>
            <div class="label">建立帳號</div>
        </div>
    </a>
    <a class="item">
        <div class="content">
            <div class="indicator"></div>
            <div class="label">驗證信箱</div>
        </div>
    </a>
    <a class="item">
        <div class="content">
            <div class="indicator"></div>
            <div class="label">歡迎使用</div>
        </div>
    </a>
</div>
```

### [無序的](procedure.md#unordered)

讓使用者知道能夠在任意步驟來回穿越而不須按照順序，在這個狀況下完成的步驟不會有線條指示。

```html
<div class="ts-procedure is-unordered">
    <a class="item is-completed">
        <div class="content">
            <div class="indicator"></div>
            <div class="label">影片資訊</div>
        </div>
    </a>
    <a class="item is-active">
        <div class="content">
            <div class="indicator"></div>
            <div class="label">廣告營利</div>
        </div>
    </a>
    <a class="item">
        <div class="content">
            <div class="indicator"></div>
            <div class="label">隱私設定</div>
        </div>
    </a>
</div>
<div class="ts-procedure is-unordered is-compact">
    <a class="item is-completed">
        <div class="content">
            <div class="indicator"></div>
            <div class="label">影片資訊</div>
        </div>
    </a>
    <a class="item is-active">
        <div class="content">
            <div class="indicator"></div>
            <div class="label">廣告營利</div>
        </div>
    </a>
    <a class="item">
        <div class="content">
            <div class="indicator"></div>
            <div class="label">隱私設定</div>
        </div>
    </a>
</div>
```

### [垂直的](procedure.md#vertical)

以上下垂直的方式展示每個步驟，適合放於側邊給予指示。

```html
<div class="ts-procedure is-vertical">
    <a class="item is-completed">
        <div class="content">
            <div class="indicator"></div>
            <div class="label">分割磁碟</div>
        </div>
    </a>
    <a class="item is-active">
        <div class="content">
            <div class="indicator"></div>
            <div class="label">安裝系統</div>
        </div>
    </a>
    <a class="item">
        <div class="content">
            <div class="indicator"></div>
            <div class="label">初始化環境</div>
        </div>
    </a>
</div>
```

### [尺寸](procedure.md#sizes)

更改步驟指示器的大小。

```html
<div class="ts-procedure is-small">
    <div class="item">
        <div class="content">
            <div class="indicator"></div>
            <div class="label">確認資訊</div>
        </div>
    </div>
    <div class="item">
        <div class="content">
            <div class="indicator"></div>
            <div class="label">選擇上車地點</div>
        </div>
    </div>
    <div class="item">
        <div class="content">
            <div class="indicator"></div>
            <div class="label">付款</div>
        </div>
    </div>
</div>
<div class="ts-procedure">
    <div class="item">
        <div class="content">
            <div class="indicator"></div>
            <div class="label">確認資訊</div>
        </div>
    </div>
    <div class="item">
        <div class="content">
            <div class="indicator"></div>
            <div class="label">選擇上車地點</div>
        </div>
    </div>
    <div class="item">
        <div class="content">
            <div class="indicator"></div>
            <div class="label">付款</div>
        </div>
    </div>
</div>
<div class="ts-procedure is-large">
    <div class="item">
        <div class="content">
            <div class="indicator"></div>
            <div class="label">確認資訊</div>
        </div>
    </div>
    <div class="item">
        <div class="content">
            <div class="indicator"></div>
            <div class="label">選擇上車地點</div>
        </div>
    </div>
    <div class="item">
        <div class="content">
            <div class="indicator"></div>
            <div class="label">付款</div>
        </div>
    </div>
</div>
```
