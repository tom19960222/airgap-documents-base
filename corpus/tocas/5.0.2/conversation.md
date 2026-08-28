---
collection: tocas
version: "5.0.2"
title: "交談會話 - Tocas UI"
source_url: https://github.com/teacat/tocas-docs/blob/e62614c61a3fdb5d75cc5573e66f64dbfdbb7be7/docs/5.0/zh-tw/conversation.html
fetched_at: 2025-03-22T01:53:10+08:00
---
```html
<div class="ts-conversation is-sent">
    <div class="avatar">
        <img src="user.png">
    </div>
    <div class="content">
        <div class="bubble">
            <div class="author">星乃菖蒲</div>
            <div class="text">
                你看著這個人，有點可笑，<br>
                現在的他好像和以前的他不是一個人。
            </div>
            <div class="meta">
                <div class="item">下午 11:58</div>
            </div>
        </div>
    </div>
</div>
```

## 訊息狀態

### [已送出](conversation.md#sent)

表示這個訊息已經送至伺服器但對方並沒有讀取。

```html
<div class="ts-conversation is-sent">
    <div class="avatar">
        <img src="user.png">
    </div>
    <div class="content">
        <div class="bubble">
            <div class="author">君島翔</div>
            <div class="text">
                你以為這些年你已經習慣了。<br>
                但那句話你始終說不出口。
            </div>
            <div class="meta">
                <div class="item">下午 10:04</div>
            </div>
        </div>
    </div>
</div>
```

### [發送中](conversation.md#sending)

訊息還正在發送至伺服器，可能是網際網路速度過慢而尚未發送完畢。

```html
<div class="ts-conversation is-sending">
    <div class="avatar">
        <img src="user.png">
    </div>
    <div class="content">
        <div class="bubble">
            <div class="author">夏杞文實</div>
            <div class="text">
                你們還是存在分歧，還是在爭吵，<br>
                某個瞬間，你覺得這樣可能也挺好。
            </div>
            <div class="meta">
                <div class="item">上午 12:04</div>
            </div>
        </div>
    </div>
</div>
```

### [已讀的](conversation.md#read)

對方已經接收到訊息且閱讀過了。

```html
<div class="ts-conversation is-read">
    <div class="avatar">
        <img src="user.png">
    </div>
    <div class="content">
        <div class="bubble">
            <div class="author">河居織鶴</div>
            <div class="text">
                你說著那些曾經你最討厭的話，你們從交流變成了爭吵。
            </div>
            <div class="meta">
                <div class="item">下午 05:26</div>
            </div>
        </div>
    </div>
</div>
```

### [出錯的](conversation.md#error)

發送訊息時發生錯誤。

```html
<div class="ts-conversation is-error">
    <div class="avatar">
        <img src="user.png">
    </div>
    <div class="content">
        <div class="bubble">
            <div class="author">喜羽正明</div>
            <div class="text">
                幾年後你卻反了過來，你說不要妥協。
            </div>
            <div class="meta">
                <div class="item">下午 08:14</div>
            </div>
        </div>
    </div>
</div>
```

## 結構

### [引言](conversation.md#quote)

提及另一個訊息的內容。

```html
<div class="ts-conversation">
    <div class="avatar">
        <img src="user.png">
    </div>
    <div class="content">
        <div class="bubble">
            <div class="author">八馬奏</div>
            <div class="quote">
                <div class="author">天草月乃</div>
                <div class="text">
                    要有偉大的夢想，<br>
                    我老是這麼說，對吧？
                </div>
            </div>
            <div class="text">
                我一直都有機會，<br>
                只是從來沒膽做正確的選擇。
            </div>
            <div class="meta">
                <div class="item">下午 04:58</div>
            </div>
        </div>
    </div>
</div>
```

### [連結預覽](conversation.md#link-preview)

訊息裡如果包含超連結的話，則可以帶有連結預覽區塊。

```html
<div class="ts-conversation" style="max-width: 400px">
    <div class="avatar">
        <img src="user.png">
    </div>
    <div class="content">
        <div class="bubble">
            <div class="author">影山星一</div>
            <div class="text">
                五月的北京 4 點就天亮了，<br>
                而我就像個寄居動物般已經三天沒回家。
            </div>
            <div class="preview">
                <div class="site">電腦玩瞎咪</div>
                <div class="title">華碩自稱「中國公司」，中國分部發言誓死阻撓日本工商</div>
                <div class="content">在微博上的《ROG玩家国度》小編便發文了，誓死也會阻止這次日本華碩與 Hololive 的工商互動。多數中國網友表示期待且「買不買華碩就看這次了」。「難道不知道華碩是中國的品牌嗎？」而說出這句話的也不僅網友，連華碩小編本身也如此說道。</div>
                <div class="embed">
                    <img src="image.png">
                </div>
            </div>
            <div class="meta">
                <div class="item">下午 03:04</div>
            </div>
        </div>
    </div>
</div>
```

### [外置物件](conversation.md#object)

能夠擺放其他元件，例如：[多媒體照片](image.md)、[圖片組合](imageset.md)。

```html
<div class="ts-conversation" style="max-width: 400px">
    <div class="avatar">
        <img src="user.png">
    </div>
    <div class="content">
        <div class="bubble">
            <div class="author">東雲鈴音</div>
            <div class="object">
                <div class="ts-image">
                    <img src="image.png">
                </div>
            </div>
            <div class="text">
                我不忍也不敢告訴他們，今天的差評又多了一些。
            </div>
        </div>
    </div>
</div>
<div class="ts-conversation" style="max-width: 400px">
    <div class="avatar">
        <img src="user.png">
    </div>
    <div class="content">
        <div class="bubble">
            <div class="author">山崎颯太</div>
            <div class="object">
                <div class="ts-imageset is-compact is-3-images">
                    <div class="item">
                        <img src="image.png">
                    </div>
                    <div class="item">
                        <img src="image.png">
                    </div>
                    <div class="item">
                        <img src="image.png">
                    </div>
                </div>
            </div>
            <div class="text">
                現在是凌晨 2:55 分，<br>
                對於我來說，今天才過了一半。
            </div>
        </div>
    </div>
</div>
```

## 外觀

### [自己的](conversation.md#self)

讓訊息置右並更改其語意，使用者便能一眼看出這是自己所發送的訊息。

```html
<div class="ts-conversation is-self">
    <div class="avatar">
        <img src="user.png">
    </div>
    <div class="content">
        <div class="bubble">
            <div class="author">新田司</div>
            <div class="text">
                原因應該先於結果發生，<br>
                但這取決於你怎麼看待時間。
            </div>
            <div class="meta">
                <div class="item">下午 05:18</div>
            </div>
        </div>
    </div>
</div>
```

### [僅有物件的](conversation.md#object-only)

如果訊息裡只有外置物件而沒有其他內容，則可以讓訊息看起來更緊緻並移除多餘空白。

```html
<div class="ts-conversation is-object-only is-sent">
    <div class="avatar">
        <img src="user.png">
    </div>
    <div class="content">
        <div class="bubble">
            <div class="object">
                <div class="ts-image">
                    <img src="image.png">
                </div>
            </div>
            <div class="meta">
                <div class="item">上午 06:37</div>
            </div>
        </div>
    </div>
</div>
```

## 組合應用

### [反應](conversation.md#composition-reactions)

在訊息底下擺放[關聯標籤](chip.md)能夠營造出一個讓使用者表態對該訊息的反應。

```html
<div class="ts-conversation">
    <div class="avatar">
        <img src="user.png">
    </div>
    <div class="content">
        <div class="bubble">
            <div class="author">佐藤理人</div>
            <div class="text">
                大家也要生存，也要生活，<br>
                不是每個人都有孤注一擲的勇氣。
            </div>
        </div>
        <div class="ts-wrap is-compact has-top-spaced-small">
            <label class="ts-chip is-toggle is-secondary is-circular is-outlined">
                <input type="checkbox" checked="">
                <div class="content">👌 21</div>
            </label>
            <label class="ts-chip is-toggle is-secondary is-circular is-outlined">
                <input type="checkbox">
                <div class="content">👀 8</div>
            </label>
            <div class="ts-chip is-outlined is-circular" style="padding: 0.1rem 0.5rem">
                <span class="ts-icon is-regular is-face-smile-icon"></span>
            </div>
        </div>
    </div>
</div>
```

### [中繼資料](conversation.md#composition-meta)

透過[中繼資料](meta.md)元件可以呈現和訊息有關的詳細資訊或是部份動作行為。

```html
<div class="ts-conversation">
    <div class="avatar">
        <img src="user.png">
    </div>
    <div class="content">
        <div class="bubble">
            <div class="author">米莉亞</div>
            <div class="text">
                你突然問自己，我到底是什麼時候死掉的呢？<br>
                最後一秒你努力的回憶著，你終於想起了一個畫面。
            </div>
        </div>
        <div class="ts-meta is-small is-secondary">
            <a class="item">讚</a>
            <a class="item">回覆</a>
            <a class="item">3 分前</a>
        </div>
    </div>
</div>
```

### [動作按鈕](conversation.md#composition-callbacks)

搭配[按鈕](button.md)和[網格系統](grid.md)，可以製造出對該訊息的動作按鈕。適合應用在聊天機器人的情境上。

```html
<div class="ts-conversation">
    <div class="avatar">
        <img src="user.png">
    </div>
    <div class="content">
        <div class="bubble">
            <div class="author">文字冒險 RPG 遊戲機器人</div>
            <div class="text">
                你目前在：<b>特雅蘭 提斯市</b><br>
                這裡有 11 位玩家，<br>
                前方不遠的地方看起來像是這個城鎮的出口。
            </div>
            <div class="meta">
                <div class="item">下午 01:02</div>
            </div>
        </div>
        <div class="ts-grid is-compact is-evenly-divided has-top-spaced-small">
            <div class="column">
                <button class="ts-button is-small is-secondary is-fluid">
                    ⬆️ 往前
                </button>
            </div>
            <div class="column">
                <button class="ts-button is-small is-secondary is-fluid">
                    ↩️ 返回巷弄
                </button>
            </div>
            <div class="column">
                <button class="ts-button is-small is-secondary is-fluid">
                    👁️‍🗨️ 調查
                </button>
            </div>
        </div>
    </div>
</div>
```
