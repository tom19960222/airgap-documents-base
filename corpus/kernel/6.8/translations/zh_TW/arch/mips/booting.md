---
collection: kernel
version: "6.8"
title: "1. BMIPS設備樹引導"
source_url: https://www.kernel.org/doc/html/v6.8/translations/zh_TW/arch/mips/booting.html
fetched_at: 2026-08-21T03:58:38+00:00
---
Chinese (Traditional)

- [English](../../../../arch/mips/booting.md)
- [Chinese (Simplified)](../../../zh_CN/arch/mips/booting.md)

> **Warning:**
>
> 此文件的目的是爲讓中文讀者更容易閱讀和理解，而不是作爲一個分支。因此，
> 如果您對此文件有任何意見或改動，請先嘗試更新原始英文文件。如果要更改或
> 修正某處翻譯文件，請將意見或補丁發送給維護者（聯繫方式見下）。

> **Note:**
>
> 如果您發現本文檔與原始文件有任何不同或者有翻譯問題，請聯繫該文件的譯者，
> 或者發送電子郵件給胡皓文以獲取幫助：<[2023002089@link.tyut.edu.cn](mailto:2023002089%40link.tyut.edu.cn)>。

Original
:   [BMIPS DeviceTree Booting](../../../../arch/mips/booting.md)

翻譯
:   司延騰 Yanteng Si <[siyanteng@loongson.cn](mailto:siyanteng%40loongson.cn)>

# 1. BMIPS設備樹引導

> 一些bootloaders只支持在內核鏡像開始地址處的單一入口點。而其它
> bootloaders將跳轉到ELF的開始地址處。兩種方案都支持的；因爲
> CONFIG_BOOT_RAW=y and CONFIG_NO_EXCEPT_FILL=y, 所以第一條指令
> 會立即跳轉到kernel_entry()入口處執行。
>
> 與arch/arm情況(b)類似，dt感知的引導加載程序需要設置以下寄存器:
>
> > a0 : 0
> >
> > a1 : 0xffffffff
> >
> > a2RAM中指向設備樹塊的物理指針(在chapterII中定義)。
> > :   設備樹可以位於前512MB物理地址空間(0x00000000 -
> >     0x1fffffff)的任何位置，以64位邊界對齊。
>
> 傳統bootloaders不會使用這樣的約定，並且它們不傳入DT塊。
> 在這種情況下，Linux將通過選中CONFIG_DT_\*查找DTB。
>
> 以上約定只在32位系統中定義，因爲目前沒有任何64位的BMIPS實現。
