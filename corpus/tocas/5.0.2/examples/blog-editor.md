---
collection: tocas
version: "5.0.2"
title: "發文後台 - Tocas UI"
source_url: https://github.com/teacat/tocas-docs/blob/e62614c61a3fdb5d75cc5573e66f64dbfdbb7be7/docs/5.0/zh-tw/examples/blog-editor.html
fetched_at: 2025-03-22T01:53:10+08:00
---
我的超級
神奇部落格

目前身份為 YAMI ODYMEL

帳號

[使用者](blog-editor.md#!)

內容

[文章](blog-editor.md#!)
[分類](blog-editor.md#!)
[多媒體](blog-editor.md#!)

系統

[偏好設定](blog-editor.md#!)
[主題與外觀](blog-editor.md#!)

登出

在 Unity 中，目前分為兩個撰寫遊戲的方式：[ECS](https://learn.unity.com/tutorial/entity-component-system)（Entity、Component、System）與傳統的 [MonoBehaviour](https://docs.unity3d.com/ScriptReference/MonoBehaviour.html)。
前者是 Unity 在 2018 年所推出的新程式結構撰寫理念，主要是為了解決多數的程式碼都在主執行緒上執行，而導致 CPU 分配率不彰、程式效率降低、執行緒鎖死的問題。但 ECS 基本上到年底，都還不是一個完善的狀態，更不是萬能仙丹；事實上，ECS 就算進入了正式版，也有可能是在下一個產物出來之前的過渡期設計。
話雖如此，ECS 的設計理念還是值得參考與借鑒的。在前端網頁設計中，其實已經運用了類似的理念有至少二、三年之久，那東西耳熟能詳的名稱是：[Vuex](https://vuex.vuejs.org/) 與 [Redux](https://redux.js.org/)。
簡單來說，ECS 嘗試地想要將：「把所有邏輯全部塞進同一個 MonoBehaviour 元件」的這種問題給解決。設想看看，如果遊戲內有一百個物件，而且那些物件都是 NPC 玩家，但角色大多都是相同的邏輯與行為方式，在傳統寫法這會造成每個元件都有自己的邏輯，而導致效能不彰。
說到每個元件都有自己的邏輯，ECS 的解決方法顯而易見：
> 讓元件本身只保有狀態資料，而邏輯獨立成一個中央系統。
如果這聽起來牛頭不對馬嘴、不曉得到底是在說什麼東西，那麼你一定會喜歡接下來的程式碼範例章節。
# 現有問題
讓我們假設現在有個 `CreatureObject` 生物物件，這是一個很標準的 `MonoBehaviour` 物件，他會被套用到任何生物的 `GameObject` 上。
這個程式碼說來簡單：也就是一個生物能夠在受到傷害的時候，把自己的生命值減低一定的數值而已。
```
// CreatureObject 是一個生物的物件。
class CreatureObject : MonoBehaviour {
// health 是這個生物的生命值。
int health;
// TakeDamage 會讓此生物受傷害，即會讓此生物的生命值減低一定的數值。
void TakeDamage(int damage) {
// 將生命值扣除受到的傷害。
health -= damage;
}
}
```
這看起來沒有什麼問題，但實際上會在後期演變成更肥大的遊戲物件，甚至有可能會需要為了不同場景而寫出多個不同但最終卻有著相同效果的函式。
# 解決方法
為了下一代著想，我們需要把邏輯拆分出來成為一個獨立的中央共享系統，然後讓物件本身只帶有狀態資料，其他什麼都沒有。
```
// CreatureObject 是一個生物的物件。
class CreatureObject : MonoBehaviour {
// health 是這個生物的生命值。
int health;
}
// StatsSystem 是狀態系統，能夠與生物之間的資料有所互動。
class StatsSystem : MonoBehaviour {
// TakeDamage 會讓指定的生物受傷害，即會讓指定生物的生命值減低一定的數值。
void TakeDamage(CreatureObject creature, int damage) {
// 將生命值扣除受到的傷害。
creature.health -= damage;
}
}
```
在上述程式碼中，就是將狀態變動邏輯獨立成一個中央系統的最好例子，由這個方式可以額外延伸更多的系統…像是：控制系統、動畫系統、道具系統、對話系統等。
雖然說 ECS 不完全僅是這樣的東西，但這卻是其中最重要的一環；而另一件事情不得不提到的就是 ECS 在多工上的優勢，同時也是最為麻煩與嚴謹的一部分，不過那又是另一個話題了。

文章資訊

標題

發佈時間

標籤

前言

又有新的東西要學了，學不動了。

摘要

Unity 在 2018 年所推出的新程式結構撰寫理念，主要是為了解決多數的程式碼都在主執行緒上執行，而導致 CPU 分配率不彰、程式效率降低、執行緒鎖死的問題。

作者

YamiOdymel

發表文章
