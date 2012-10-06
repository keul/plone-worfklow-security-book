============
Introduzione
============

Lo scopo del libro
==================

Questo documento si prefigge lo scopo di fornire una guida completa al comprendere le funzionalità,
la configurazione e la gestione dei **workflow** e della **sicurezza** nel CMS `Plone`__.

__ http://plone.org/

Il sistema di workflow disponibile in Plone e tutto quello che concerne la sicurezza dei documenti
nel CMS sono una tra le sue maggiori attrattive e una tra le caratteristiche più potenti, ma molto
spesso incomprese.

Non sono un grande fan della documentazione, poiché questa tende a diventare obsoleta molto
velocemente, ma questa parte della tecnologia Plone è la stessa da quando ho iniziato a lavorarvi
(o poco è cambiato) e non credo ci saranno grosse novità nel prossimo futuro.
Questo a mio parere giustifica lo sforzo.

Per chi è questo libro
======================

Un programmatore Plone, ma molto spesso più semplicemente un amministratore del sito, *avrebbero*
il potere di fare grandi cose e plasmare il funzionamento del sito al proprio volere, ma la
documentazione è sparsa ed a volte assente.

Questo libro è pensato per entrambi questi tipi di utente:

* ad uno **sviluppatore Plone** verrà mostrato che cosa è possibile fare senza ricorrere allo
  sviluppo e i limiti oltre i quali lo sviluppo può intervenire (e in che modo).
  
  Questo vuole evitare situazioni in cui lo sviluppatore non esperto di Plone *non sa* di una
  determinata funzionalità, e quindi la reinventa in modo non corretto.
* ad un **amministratore** verrà mostrato tutto quello che è possibile fare senza ricorrere allo
  sviluppo, semplicemente usando prodotti già presenti o aggiuntivi, o configurado a dovere il
  sistema.
  
  Questo secondo scopo vuole far comprendere agli amministratori quante cose è possibile fare senza
  bisogno di richiedere sviluppo dall'esterno.

Per chi *non* è questo libro
============================

Sebbene io sia uno sviluppatore Plone, questo libro non insegnerà a sviluppare: verranno toccati
i minimi argomenti necessari per arrivare allo scopo.
Quando l'argomento analizzato inizierà ad addentrarsi nei meandri della programmazione verranno
date le minime informazioni necessarie, fornendo poi riferimenti esterni, nel caso il lettore
volesse approfondire oltre.

Qualche riga di codice potrebbe anche essere spiegata, ma sarà sempre ridotta all'osso e mai ben
approfondita.

Che cosa verrà approfondito in questo libro
===========================================

Verranno mostrare tutte le funzionalità riguardanti la sicurezza di Plone, partendo dalla
**gestione degli utenti** e **dei gruppi**, per arrivare all'analisi dei **ruoli** che Plone
fornisce di base e ad una spiegazione di come questi vanno intesi ed interpretati.

Verranno poi introdotti i **permessi** e il loro ruolo nella sicurezza, portando infine l'utente
al cuore della sicurezza dei contenuti in Plone: il **workflow**.
Verranno mostrati i workflow predefiniti del CMS, i loro limiti e difetti e il come superarli.

Infine verrà insegnato come creare nuovi workflow, come disegnarli e fargli fare cose non sempre
semplici.

Cosa *non* verrà affrontato
===========================

Questo libro vuole essere *diretto*, evitando tutti quegli argomenti che non ritengo importanti.
Non verranno spiegati i "dogmi", non verranno date inutili definizioni di qualcosa che (mi aspetto)
sia già conosciuto dal lettore.

Il linguaggio sarà esso stesso *diretto*.

Come è strutturato questo libro
===============================

Il libro parte dalla "superficie", mostrando Plone come si presenta una volta installato e
spiegandone il funzionamento (e la *configurazione*) di base.
Da qui si prenderà lo spunto per le prime riflessioni e domande su cosa è possibile
personalizzare, il che ci porterà a scavare sotto la superficie e sarà trampolino di lancio
per personalizzare lo strumento e spingersi quindi verso i confini con la programmazione.

Sebbene il focus centrale degli argomenti è il CMS Plone, gran parte degli argomenti mostrati
sono applicabili alle tecnologie sottostanti (`Zope`__, `CMF`__, ...), ma per semplicità di lettura
queste differenze di tecnologia *non* saranno evidenziate nel libro.

__ http://zope.org/
__ http://pypi.python.org/pypi/Products.CMFCore

Riferimenti alle versioni utilizzati
====================================

Quanto mostrato è applicabile alla versione 4 di Plone (specificatamente: `Plone 4.2.x`__), ma sono
quasi certo che se la vostra versione di Plone è maggiore, una grossa percentuale di quanto qui
riportato sarà comunque estremamente utile.

__ http://plone.org/products/plone/releases/4.2

