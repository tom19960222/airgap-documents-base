---
collection: kernel
version: "6.8"
title: "Lenguaje de programación"
source_url: https://www.kernel.org/doc/html/v6.8/translations/sp_SP/process/programming-language.html
fetched_at: 2026-08-21T03:37:39+00:00
---
Spanish

- [English](../../../process/programming-language.md)
- [Chinese (Simplified)](../../zh_CN/process/programming-language.md)
- [Chinese (Traditional)](../../zh_TW/process/programming-language.md)
- [Italian](../../it_IT/process/programming-language.md)

> **Warning:**
>
> Si tiene alguna duda sobre la exactitud del contenido de esta
> traducción, la única referencia válida es la documentación oficial en
> inglés.
> Además, por defecto, los enlaces a documentos redirigen a la
> documentación en inglés, incluso si existe una versión traducida.
> Consulte el índice para más información.

Original
:   [Documentation/process/programming-language.rst](../../../process/programming-language.md#programming-language)

Translator
:   Carlos Bilbao <[carlos.bilbao@amd.com](mailto:carlos.bilbao%40amd.com)>

# Lenguaje de programación

El kernel está escrito en el lenguaje de programación C [[sp-c-language]](programming-language.md#sp-c-language).
Más concretamente, el kernel normalmente se compila con `gcc` [[sp-gcc]](programming-language.md#sp-gcc)
bajo `-std=gnu11` [[sp-gcc-c-dialect-options]](programming-language.md#sp-gcc-c-dialect-options): el dialecto GNU de ISO C11.
`clang` [[sp-clang]](programming-language.md#sp-clang) también es compatible, consulte los documentos en
[Building Linux with Clang/LLVM](../../../kbuild/llvm.md#kbuild-llvm).

Este dialecto contiene muchas extensiones del lenguaje [[sp-gnu-extensions]](programming-language.md#sp-gnu-extensions),
y muchos de ellos se usan dentro del kernel de forma habitual.

Hay algo de soporte para compilar el núcleo con `icc` [[sp-icc]](programming-language.md#sp-icc) para varias
de las arquitecturas, aunque en el momento de escribir este texto, eso no
está terminado y requiere parches de terceros.

## Atributos

Una de las comunes extensiones utilizadas en todo el kernel son los atributos
[[sp-gcc-attribute-syntax]](programming-language.md#sp-gcc-attribute-syntax). Los atributos permiten introducir semántica
definida por la implementación a las entidades del lenguaje (como variables,
funciones o tipos) sin tener que hacer cambios sintácticos significativos
al idioma (por ejemplo, agregar una nueva palabra clave) [[sp-n2049]](programming-language.md#sp-n2049).

En algunos casos, los atributos son opcionales (es decir, hay compiladores
que no los admiten pero de todos modos deben producir el código adecuado,
incluso si es más lento o no realiza tantas comprobaciones/diagnósticos en
tiempo de compilación).

El kernel define pseudo-palabras clave (por ejemplo, `__pure`) en lugar
de usar directamente la sintaxis del atributo GNU (por ejemplo,
`__attribute__((__pure__))`) con el fin de detectar cuáles se pueden
utilizar y/o acortar el código.

Por favor consulte `include/linux/compiler_attributes.h` para obtener
más información.

[sp-c-language](programming-language.md#id1)
:   <http://www.open-std.org/jtc1/sc22/wg14/www/standards>

[sp-gcc](programming-language.md#id2)
:   <https://gcc.gnu.org>

[sp-clang](programming-language.md#id4)
:   <https://clang.llvm.org>

[sp-icc](programming-language.md#id6)
:   <https://software.intel.com/en-us/c-compilers>

[sp-gcc-c-dialect-options](programming-language.md#id3)
:   <https://gcc.gnu.org/onlinedocs/gcc/C-Dialect-Options.html>

[sp-gnu-extensions](programming-language.md#id5)
:   <https://gcc.gnu.org/onlinedocs/gcc/C-Extensions.html>

[sp-gcc-attribute-syntax](programming-language.md#id7)
:   <https://gcc.gnu.org/onlinedocs/gcc/Attribute-Syntax.html>

[sp-n2049](programming-language.md#id8)
:   <http://www.open-std.org/jtc1/sc22/wg14/www/docs/n2049.pdf>
