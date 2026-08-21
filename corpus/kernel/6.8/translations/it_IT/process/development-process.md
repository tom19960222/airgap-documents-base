---
collection: kernel
version: "6.8"
title: "Una guida al processo di sviluppo del Kernel"
source_url: https://www.kernel.org/doc/html/v6.8/translations/it_IT/process/development-process.html
fetched_at: 2026-08-21T03:29:14+00:00
---
Italian

- [English](../../../process/development-process.md)
- [Chinese (Simplified)](../../zh_CN/process/development-process.md)
- [Chinese (Traditional)](../../zh_TW/process/development-process.md)

> **Warning:**
>
> In caso di dubbi sulla correttezza del contenuto di questa traduzione,
> l'unico riferimento valido è la documentazione ufficiale in inglese.
> Per maggiori informazioni consultate le [avvertenze](../index.md#it-disclaimer).

Original
:   [Documentation/process/development-process.rst](../../../process/development-process.md#development-process-main)

Translator
:   Alessia Mantegazza <[amantegazza@vaga.pv.it](mailto:amantegazza%40vaga.pv.it)>

# Una guida al processo di sviluppo del Kernel

Lo scopo di questo documento è quello di aiutare gli sviluppatori (ed i loro
supervisori) a lavorare con la communità di sviluppo con il minimo sforzo. È
un tentativo di documentare il funzionamento di questa communità in modo che
sia accessibile anche a coloro che non hanno famigliarità con lo sviluppo del
Kernel Linux (o, anzi, con lo sviluppo di software libero in generale). Benchè
qui sia presente del materiale tecnico, questa è una discussione rivolta in
particolare al procedimento, e quindi per essere compreso non richiede una
conoscenza approfondità sullo sviluppo del kernel.

Contenuti

- [1. Introduzione](1.Intro.md)
  - [1.1. Riepilogo generale](1.Intro.md#riepilogo-generale)
  - [1.2. Di cosa parla questo documento](1.Intro.md#di-cosa-parla-questo-documento)
  - [1.3. Crediti](1.Intro.md#crediti)
  - [1.4. L'importanza d'avere il codice nei sorgenti principali](1.Intro.md#l-importanza-d-avere-il-codice-nei-sorgenti-principali)
  - [1.5. Licenza](1.Intro.md#licenza)
- [2. Come funziona il processo di sviluppo](2.Process.md)
  - [2.1. Il quadro d'insieme](2.Process.md#il-quadro-d-insieme)
  - [2.2. Il ciclo di vita di una patch](2.Process.md#il-ciclo-di-vita-di-una-patch)
  - [2.3. Come le modifiche finiscono nel Kernel](2.Process.md#come-le-modifiche-finiscono-nel-kernel)
  - [2.4. Sorgenti -next](2.Process.md#sorgenti-next)
  - [2.5. Sorgenti in preparazione](2.Process.md#sorgenti-in-preparazione)
  - [2.6. Strumenti](2.Process.md#strumenti)
  - [2.7. Liste di discussione](2.Process.md#liste-di-discussione)
  - [2.8. Iniziare con lo sviluppo del Kernel](2.Process.md#iniziare-con-lo-sviluppo-del-kernel)
- [3. I primi passi della pianificazione](3.Early-stage.md)
  - [3.1. Specificare il problema](3.Early-stage.md#specificare-il-problema)
  - [3.2. Prime discussioni](3.Early-stage.md#prime-discussioni)
  - [3.3. Con chi parlare?](3.Early-stage.md#con-chi-parlare)
  - [3.4. Quando pubblicare](3.Early-stage.md#quando-pubblicare)
  - [3.5. Ottenere riscontri ufficiali](3.Early-stage.md#ottenere-riscontri-ufficiali)
- [4. Scrivere codice corretto](4.Coding.md)
  - [4.1. Trappole](4.Coding.md#trappole)
  - [4.2. Strumenti di verifica del codice](4.Coding.md#strumenti-di-verifica-del-codice)
  - [4.3. Documentazione](4.Coding.md#documentazione)
  - [4.4. Cambiamenti interni dell'API](4.Coding.md#cambiamenti-interni-dell-api)
- [5. Pubblicare modifiche](5.Posting.md)
  - [5.1. Quando pubblicarle](5.Posting.md#quando-pubblicarle)
  - [5.2. Prima di creare patch](5.Posting.md#prima-di-creare-patch)
  - [5.3. Preparazione di una patch](5.Posting.md#preparazione-di-una-patch)
  - [5.4. Formattazione delle patch e i changelog](5.Posting.md#formattazione-delle-patch-e-i-changelog)
  - [5.5. Inviare la modifica](5.Posting.md#inviare-la-modifica)
- [6. Completamento](6.Followthrough.md)
  - [6.1. Lavorare con i revisori](6.Followthrough.md#lavorare-con-i-revisori)
  - [6.2. Cosa accade poi](6.Followthrough.md#cosa-accade-poi)
  - [6.3. Altre cose che posso accadere](6.Followthrough.md#altre-cose-che-posso-accadere)
- [7. Argomenti avanzati](7.AdvancedTopics.md)
  - [7.1. Gestire le modifiche con git](7.AdvancedTopics.md#gestire-le-modifiche-con-git)
  - [7.2. Revisionare le patch](7.AdvancedTopics.md#revisionare-le-patch)
- [8. Per maggiori informazioni](8.Conclusion.md)
- [9. Conclusioni](8.Conclusion.md#conclusioni)
