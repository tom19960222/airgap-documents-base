---
collection: kernel
version: "6.17"
title: "Guía del proceso de desarrollo del kernel"
source_url: https://www.kernel.org/doc/html/v6.17/translations/sp_SP/process/development-process.html
fetched_at: 2026-09-16T16:18:16+00:00
---
Spanish

- [English](../../../process/development-process.md)
- [Chinese (Simplified)](../../zh_CN/process/development-process.md)
- [Chinese (Traditional)](../../zh_TW/process/development-process.md)
- [Italian](../../it_IT/process/development-process.md)

> **Warning:**
>
> Si tiene alguna duda sobre la exactitud del contenido de esta
> traducción, la única referencia válida es la documentación oficial en
> inglés.
> Además, por defecto, los enlaces a documentos redirigen a la
> documentación en inglés, incluso si existe una versión traducida.
> Consulte el índice para más información.

Original:
:   [A guide to the Kernel Development Process](../../../process/development-process.md)

Translator:
:   Carlos Bilbao <[carlos.bilbao.osdev@gmail.com](mailto:carlos.bilbao.osdev%40gmail.com)> and Avadhut Naik <[avadhut.naik@amd.com](mailto:avadhut.naik%40amd.com)>

# Guía del proceso de desarrollo del kernel

El propósito de este documento es ayudar a los desarrolladores (y sus
jefes) a trabajar con la comunidad de desarrollo con el mínimo de
frustración. Es un intento de documentar cómo funciona esta comunidad
de una manera accesible, para aquellos que no están familiarizados
íntimamente con el desarrollo del kernel Linux (o, de hecho, el desarrollo
de software libre en general). Si bien hay algo de material técnico aquí,
esto es en gran medida una discusión orientada al proceso que no requiere
un conocimiento profundo de la programación del kernel para entenderla.

Contenido

- [1. Introducción](1.Intro.md)
  - [1.1. Resumen ejecutivo](1.Intro.md#resumen-ejecutivo)
  - [1.2. De qué trata este documento](1.Intro.md#de-que-trata-este-documento)
  - [1.3. Créditos](1.Intro.md#creditos)
  - [1.4. Importancia de integrar el código en el mainline](1.Intro.md#importancia-de-integrar-el-codigo-en-el-mainline)
  - [1.5. Licencias](1.Intro.md#licencias)
- [2. Cómo funciona el proceso de desarrollo](2.Process.md)
  - [2.1. El panorama general](2.Process.md#el-panorama-general)
  - [2.2. Ciclo de vida de un parche](2.Process.md#ciclo-de-vida-de-un-parche)
  - [2.3. Cómo se integran los parches en el kernel](2.Process.md#como-se-integran-los-parches-en-el-kernel)
  - [2.4. Árboles siguientes (next)](2.Process.md#arboles-siguientes-next)
  - [2.5. Árboles de staging](2.Process.md#arboles-de-staging)
  - [2.6. Herramientas](2.Process.md#herramientas)
  - [2.7. Listas de correo](2.Process.md#listas-de-correo)
  - [2.8. Comenzar con el desarrollo del kernel](2.Process.md#comenzar-con-el-desarrollo-del-kernel)
- [3. Planificación en etapa inicial](3.Early-stage.md)
  - [3.1. Especificar el problema](3.Early-stage.md#especificar-el-problema)
  - [3.2. Discusión temprana](3.Early-stage.md#discusion-temprana)
  - [3.3. ¿Con quién hablar?](3.Early-stage.md#con-quien-hablar)
  - [3.4. ¿Cuándo publicar?](3.Early-stage.md#cuando-publicar)
  - [3.5. Obtener respaldo oficial](3.Early-stage.md#obtener-respaldo-oficial)
- [4. Conseguir el código correcto](4.Coding.md)
  - [4.1. Problemas](4.Coding.md#problemas)
- [5. Publicación de parches](5.Posting.md)
  - [5.1. Cuando publicar](5.Posting.md#cuando-publicar)
  - [5.2. Antes de crear parches](5.Posting.md#antes-de-crear-parches)
  - [5.3. Preparación del parche](5.Posting.md#preparacion-del-parche)
  - [5.4. Formato de parches y registros de cambios](5.Posting.md#formato-de-parches-y-registros-de-cambios)
  - [5.5. Envió del parche](5.Posting.md#envio-del-parche)
- [6. Seguimiento](6.Followthrough.md)
  - [6.1. Trabajando con revisores](6.Followthrough.md#trabajando-con-revisores)
  - [6.2. ¿Qué pasa después?](6.Followthrough.md#que-pasa-despues)
  - [6.3. Otras cosas que pueden suceder](6.Followthrough.md#otras-cosas-que-pueden-suceder)
- [7. Temas avanzados](7.AdvancedTopics.md)
  - [7.1. Gestionar parches con git](7.AdvancedTopics.md#gestionar-parches-con-git)
  - [7.2. Revisión de parches](7.AdvancedTopics.md#revision-de-parches)
- [8. Para más información](8.Conclusion.md)
- [9. Conclusión](8.Conclusion.md#conclusion)
