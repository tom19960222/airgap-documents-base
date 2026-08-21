---
collection: kernel
version: "6.8"
title: "Linguaggio di programmazione"
source_url: https://www.kernel.org/doc/html/v6.8/translations/it_IT/process/programming-language.html
fetched_at: 2026-08-21T03:42:05+00:00
---
Italian

- [English](../../../process/programming-language.md)
- [Chinese (Simplified)](../../zh_CN/process/programming-language.md)
- [Chinese (Traditional)](../../zh_TW/process/programming-language.md)
- [Spanish](../../sp_SP/process/programming-language.md)

> **Warning:**
>
> In caso di dubbi sulla correttezza del contenuto di questa traduzione,
> l'unico riferimento valido è la documentazione ufficiale in inglese.
> Per maggiori informazioni consultate le [avvertenze](../index.md#it-disclaimer).

Original
:   [Documentation/process/programming-language.rst](../../../process/programming-language.md#programming-language)

Translator
:   Federico Vaga <[federico.vaga@vaga.pv.it](mailto:federico.vaga%40vaga.pv.it)>

# Linguaggio di programmazione

Il kernel è scritto nel linguaggio di programmazione C [[it-c-language]](programming-language.md#it-c-language).
Più precisamente, il kernel viene compilato con `gcc` [[it-gcc]](programming-language.md#it-gcc) usando
l'opzione `-std=gnu11` [[it-gcc-c-dialect-options]](programming-language.md#it-gcc-c-dialect-options): il dialetto GNU
dello standard ISO C11.
Linux supporta anche `clang` [[it-clang]](programming-language.md#it-clang), leggete la documentazione
[Building Linux with Clang/LLVM](../../../kbuild/llvm.md#kbuild-llvm).

Questo dialetto contiene diverse estensioni al linguaggio [[it-gnu-extensions]](programming-language.md#it-gnu-extensions),
e molte di queste vengono usate sistematicamente dal kernel.

## Attributi

Una delle estensioni più comuni e usate nel kernel sono gli attributi
[[it-gcc-attribute-syntax]](programming-language.md#it-gcc-attribute-syntax). Gli attributi permettono di aggiungere una semantica,
definita dell'implementazione, alle entità del linguaggio (come le variabili,
le funzioni o i tipi) senza dover fare importanti modifiche sintattiche al
linguaggio stesso (come l'aggiunta di nuove parole chiave) [[it-n2049]](programming-language.md#it-n2049).

In alcuni casi, gli attributi sono opzionali (ovvero un compilatore che non
dovesse supportarli dovrebbe produrre comunque codice corretto, anche se
più lento o che non esegue controlli aggiuntivi durante la compilazione).

Il kernel definisce alcune pseudo parole chiave (per esempio `__pure`)
in alternativa alla sintassi GNU per gli attributi (per esempio
`__attribute__((__pure__))`) allo scopo di mostrare quali funzionalità si
possono usare e/o per accorciare il codice.

Per maggiori informazioni consultate il file d'intestazione
`include/linux/compiler_attributes.h`.

## Rust

Il kernel supporta sperimentalmente il linguaggio di programmazione Rust
[[it-rust-language]](programming-language.md#it-rust-language) abilitando l'opzione di configurazione `CONFIG_RUST`. Il
codice verrà compilato usando `rustc` [[it-rustc]](programming-language.md#it-rustc) con l'opzione
`--edition=2021` [[it-rust-editions]](programming-language.md#it-rust-editions). Le edizioni Rust sono un modo per
introdurre piccole modifiche senza compatibilità all'indietro._

In aggiunta, nel kernel vengono utilizzate alcune funzionalità considerate
instabili [[it-rust-unstable-features]](programming-language.md#it-rust-unstable-features). Queste funzionalità potrebbero cambiare
in futuro, dunque è un'obiettivo importante è quello di far uso solo di
funzionalità stabili.

Per maggiori informazioni fate riferimento a [Rust](../../../rust/index.md) .

[it-c-language](programming-language.md#id1)
:   <http://www.open-std.org/jtc1/sc22/wg14/www/standards>

[it-gcc](programming-language.md#id2)
:   <https://gcc.gnu.org>

[it-clang](programming-language.md#id4)
:   <https://clang.llvm.org>

[it-gcc-c-dialect-options](programming-language.md#id3)
:   <https://gcc.gnu.org/onlinedocs/gcc/C-Dialect-Options.html>

[it-gnu-extensions](programming-language.md#id5)
:   <https://gcc.gnu.org/onlinedocs/gcc/C-Extensions.html>

[it-gcc-attribute-syntax](programming-language.md#id6)
:   <https://gcc.gnu.org/onlinedocs/gcc/Attribute-Syntax.html>

[it-n2049](programming-language.md#id7)
:   <http://www.open-std.org/jtc1/sc22/wg14/www/docs/n2049.pdf>

[it-rust-language](programming-language.md#id8)
:   <https://www.rust-lang.org>

[it-rustc](programming-language.md#id9)
:   <https://doc.rust-lang.org/rustc/>

[it-rust-editions](programming-language.md#id10)
:   <https://doc.rust-lang.org/edition-guide/editions/>

[it-rust-unstable-features](programming-language.md#id11)
:   <https://github.com/Rust-for-Linux/linux/issues/2>
