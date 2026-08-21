---
collection: kernel
version: "6.8"
title: "Programming Language"
source_url: https://www.kernel.org/doc/html/v6.8/process/programming-language.html
fetched_at: 2026-08-21T03:29:31+00:00
---
English

- [Chinese (Simplified)](../translations/zh_CN/process/programming-language.md)
- [Chinese (Traditional)](../translations/zh_TW/process/programming-language.md)
- [Italian](../translations/it_IT/process/programming-language.md)
- [Spanish](../translations/sp_SP/process/programming-language.md)

# Programming Language

The kernel is written in the C programming language [[c-language]](programming-language.md#c-language).
More precisely, the kernel is typically compiled with `gcc` [[gcc]](programming-language.md#gcc)
under `-std=gnu11` [[gcc-c-dialect-options]](programming-language.md#gcc-c-dialect-options): the GNU dialect of ISO C11.
`clang` [[clang]](programming-language.md#clang) is also supported, see docs on
[Building Linux with Clang/LLVM](../kbuild/llvm.md#kbuild-llvm).

This dialect contains many extensions to the language [[gnu-extensions]](programming-language.md#gnu-extensions),
and many of them are used within the kernel as a matter of course.

## Attributes

One of the common extensions used throughout the kernel are attributes
[[gcc-attribute-syntax]](programming-language.md#gcc-attribute-syntax). Attributes allow to introduce
implementation-defined semantics to language entities (like variables,
functions or types) without having to make significant syntactic changes
to the language (e.g. adding a new keyword) [[n2049]](programming-language.md#n2049).

In some cases, attributes are optional (i.e. a compiler not supporting them
should still produce proper code, even if it is slower or does not perform
as many compile-time checks/diagnostics).

The kernel defines pseudo-keywords (e.g. `__pure`) instead of using
directly the GNU attribute syntax (e.g. `__attribute__((__pure__))`)
in order to feature detect which ones can be used and/or to shorten the code.

Please refer to `include/linux/compiler_attributes.h` for more information.

## Rust

The kernel has experimental support for the Rust programming language
[[rust-language]](programming-language.md#rust-language) under `CONFIG_RUST`. It is compiled with `rustc` [[rustc]](programming-language.md#rustc)
under `--edition=2021` [[rust-editions]](programming-language.md#rust-editions). Editions are a way to introduce
small changes to the language that are not backwards compatible.

On top of that, some unstable features [[rust-unstable-features]](programming-language.md#rust-unstable-features) are used in
the kernel. Unstable features may change in the future, thus it is an important
goal to reach a point where only stable features are used.

Please refer to [Rust](../rust/index.md) for more information.

[c-language](programming-language.md#id2)
:   <http://www.open-std.org/jtc1/sc22/wg14/www/standards>

[gcc](programming-language.md#id3)
:   <https://gcc.gnu.org>

[clang](programming-language.md#id5)
:   <https://clang.llvm.org>

[gcc-c-dialect-options](programming-language.md#id4)
:   <https://gcc.gnu.org/onlinedocs/gcc/C-Dialect-Options.html>

[gnu-extensions](programming-language.md#id6)
:   <https://gcc.gnu.org/onlinedocs/gcc/C-Extensions.html>

[gcc-attribute-syntax](programming-language.md#id7)
:   <https://gcc.gnu.org/onlinedocs/gcc/Attribute-Syntax.html>

[n2049](programming-language.md#id8)
:   <http://www.open-std.org/jtc1/sc22/wg14/www/docs/n2049.pdf>

[rust-language](programming-language.md#id9)
:   <https://www.rust-lang.org>

[rustc](programming-language.md#id10)
:   <https://doc.rust-lang.org/rustc/>

[rust-editions](programming-language.md#id11)
:   <https://doc.rust-lang.org/edition-guide/editions/>

[rust-unstable-features](programming-language.md#id12)
:   <https://github.com/Rust-for-Linux/linux/issues/2>
