---
collection: kernel
version: "6.8"
title: "Guida all'hacking del kernel"
source_url: https://www.kernel.org/doc/html/v6.8/translations/it_IT/kernel-hacking/index.html
fetched_at: 2026-08-21T03:33:48+00:00
---
Italian

- [English](../../../kernel-hacking/index.md)
- [Chinese (Simplified)](../../zh_CN/kernel-hacking/index.md)

> **Warning:**
>
> In caso di dubbi sulla correttezza del contenuto di questa traduzione,
> l'unico riferimento valido è la documentazione ufficiale in inglese.
> Per maggiori informazioni consultate le [avvertenze](../index.md#it-disclaimer).

Original
:   [Documentation/kernel-hacking/index.rst](../../../kernel-hacking/index.md#kernel-hacking)

Translator
:   Federico Vaga <[federico.vaga@vaga.pv.it](mailto:federico.vaga%40vaga.pv.it)>

# Guida all'hacking del kernel

- [L'inaffidabile guida all'hacking del kernel Linux](hacking.md)
  - [Introduzione](hacking.md#introduzione)
  - [Gli attori](hacking.md#gli-attori)
  - [Alcune regole basilari](hacking.md#alcune-regole-basilari)
  - [ioctl: non scrivere nuove chiamate di sistema](hacking.md#ioctl-non-scrivere-nuove-chiamate-di-sistema)
  - [La ricetta per uno stallo](hacking.md#la-ricetta-per-uno-stallo)
  - [Alcune delle procedure più comuni](hacking.md#alcune-delle-procedure-piu-comuni)
  - [Code d'attesa `include/linux/wait.h`](hacking.md#code-d-attesa-include-linux-wait-h)
  - [Operazioni atomiche](hacking.md#operazioni-atomiche)
  - [Simboli](hacking.md#simboli)
  - [Procedure e convenzioni](hacking.md#procedure-e-convenzioni)
  - [Mettere le vostre cose nel kernel](hacking.md#mettere-le-vostre-cose-nel-kernel)
  - [Trucchetti del kernel](hacking.md#trucchetti-del-kernel)
  - [Ringraziamenti](hacking.md#ringraziamenti)
- [L'inaffidabile guida alla sincronizzazione](locking.md)
  - [Introduzione](locking.md#introduzione)
  - [Il problema con la concorrenza](locking.md#il-problema-con-la-concorrenza)
  - [Sincronizzazione nel kernel Linux](locking.md#sincronizzazione-nel-kernel-linux)
  - [Contesto di interruzione hardware](locking.md#contesto-di-interruzione-hardware)
  - [Bigino della sincronizzazione](locking.md#bigino-della-sincronizzazione)
  - [Le funzioni *trylock*](locking.md#le-funzioni-trylock)
  - [Esempi più comuni](locking.md#esempi-piu-comuni)
  - [Problemi comuni](locking.md#problemi-comuni)
  - [Velocità della sincronizzazione](locking.md#velocita-della-sincronizzazione)
  - [Quali funzioni possono essere chiamate in modo sicuro dalle interruzioni?](locking.md#quali-funzioni-possono-essere-chiamate-in-modo-sicuro-dalle-interruzioni)
  - [Riferimento per l'API dei Mutex](locking.md#riferimento-per-l-api-dei-mutex)
  - [Riferimento per l'API dei Futex](locking.md#riferimento-per-l-api-dei-futex)
  - [Approfondimenti](locking.md#approfondimenti)
  - [Ringraziamenti](locking.md#ringraziamenti)
  - [Glossario](locking.md#glossario)
