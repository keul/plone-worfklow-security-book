==========
Gli Utenti
==========

Per quanto poco ci possa essere da dire sugli utenti, qualcosa vale la pena venga definito.

Un **utente** è un visitatore del sito che ha eseguito l'**autenticazione**, che possiede quindi un
account per accedere al sito.

In alcuni siti, dove è abilitata l'autoregistrazione degli utenti, chiunque può diventare utente
del sito.

Ogni utente del sito ha (di solito) il **ruolo Collaboratore** (**Member**).

Ci possono essere eccezioni?
Sì.
Altre basi dati di utenti che non siano quella predefinita di Plone (queste fonti si ottengono
tramite **plugin PAS**) forniscono di solito questo ruolo, ma nessuno vieta di configurare a dovere
il plugin per fornire anche altri ruoli, o nessun ruolo.

Come si danno poteri agli utenti?
=================================

    Gli utenti acquisiscono diversi poteri perché vengono loro assegnati **ruoli** oppure perché,
    facendo parte di **gruppi**, acquisicono ruoli dati al gruppo.
    
    Gli utenti non possono avere direttamente **permessi**.

Che poteri predefiniti ha un utente?
====================================

Ci si potrebbe aspettare che il possedere un account in un sito Plone fornisca qualche tipo di
potere, ma questo *non è scontato*.

L'utente autenticato ha di certo (a meno di personalizzazioni poco comuni) una differenza
nell'interfaccia grafica del sito: compare il suo nome e l'accesso alle proprie preferenze
personali.

.. figure:: _static/loggedin-user.png
   :alt: Strumenti personali

   *Il menù degli strumenti personali, espanso*

Per il resto (e nella versione attuale di Plone questo è vero di partenza) un utente del sito non
ha di partenza nessun altro potere.

L'utente inizia ad acquisire poteri nel momento in cui gli vengono assegnati dei ruoli
(direttamente, o tramite un gruppo).

Le cartelle personali
---------------------

In alcuni siti l'amministratore potrebbe aver abilitato l'uso delle **cartelle personali** degli
utenti, una speciale posizione del sito da considerarsi come la "casa" dell'utente (un po' come
la directory "home" comune in tutti i sistemi operativi odierni).

.. figure:: _static/user-home-link.png
   :alt: Link alla cartella personale

   *Il link per raggiungere la propria cartella personale*

Questa impostazione ad oggi è disattivata nelle impostazioni predefinite ma può ancora essere
attivata dalle *impostazioni di sicurezza* del sito.

.. figure:: _static/user-home-enabling.png
   :alt: Impostazioni di sicurezza

   *Come abilitate le cartelle personali degli utenti*

Che cosa può fare un utente comune nella propria cartella personale? Come ripeterò molto spesso
nel resto del libro: dipende.
L'unica cosa che succede sempre è che l'utente ha il ruolo di  **Possessore** (**Owner**) della
cartella e quindi acquisisce tutti i poteri del ruolo quando lavora in quella sezione.

In una installazione base questo significa che l'utente è in grado di creare qualunque contenuto
egli voglia all'interno della propria cartella e, con i workflow che oggi sono predefiniti in
Plone, pubblicare i contenuti.

C'è sono vari motivi per cui questa sezione è ora disabilitata di base:

* si evita l'inutile creazione di cartelle (nei siti dove queste non sono in realtà mai usate)
* si evita che l'utente "salti" il workflow del sito e il sistema di revisione.

Il secondo punto è il più importante.
Nella mia esperienza (soprattutto con le vecchie versioni di Plone, precedenti alla 3, dove
questa impostazione era di base abilitata e ci si dimenticata di disattivarla) questa impostazione
provocava vari problemi.

Quando si disegna un sito con un workflow per ospitare una redazione molto complessa, si passa
diverso tempo ad ideare una struttura del sito più o meno complessa, dove utenti e gruppi abbiano
compiti ben definiti.
Ad esempio: l'ipotetico "Ufficio 5" può avere una sua cartella e si vuole che gli utenti
scrivano lì dentro i contenuti relativi all'ufficio.

Molto spesso gli utenti trovano la strada più semplice: si accorgono di avere una cartella
personale dove possono scrivere i propri documenti... e lì scrivono.
Al termine del lavoro di solito viene chiesto agli amministratori di spostare i contenuti altrove.
In questo modo non c'è bisogno di imparare come funziona il workflow del sito o dove si trova la
propria area di lavoro.

Quanto usare le cartelle personali
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

La cartella personale è una bella funzionalità che va valutata e che può tornare utile, ma di
solito va presa in considerazione assieme ad una modifica dei workflow e della sicurezza del sito.

Se il vostro sito vuole creare una community dove però ogni utente deve avere il proprio spazio,
la cartella personale può essere una strada molto comoda.

L'utente anonimo
================

Anche *il visitatore anonimo è un utente* e possiede un ruolo speciale: **Anonimo**
(**Anonymous**).
L'unica differenza con un utente autenticato è che non ha link agli strumenti personali o un'area
dove salvare le proprie preferenze, e che non identifica un singolo visitatore ma una intera
schiera di visitatori.

Sia che stiate realizzando una sito pubblico o una intranet, *questo utente va previsto*.

In un **sito pubblico** l'utente anonimo è quello che genera la maggior parte del traffico (i **bot
e crawler** dei motori di ricerca sono utenti anonimi). Va capito cosa e cosa non possono vedere, e
la sicurezza del sito deve essere calibrata su questa idea.

Per **una intranet** le cose possono sembrare più semplici, e in certi contesti lo sono, ma non
ignorate il problema.
Ho visto casi dove il fatto che una intranet non sia accessibile al pubblico lasciava intendere
di essere al sicuro, per poi accorgersi che una qualunque persona in grado di collegare il proprio
computer alla rete dell'azienda o dell'ente potesse poi accedere a documenti importanti.

In altri casi ho visto come l'obbligo di autenticazione di una intranet venisse ottenuto
limitandosi a rendere privata la home page del sito.
Ci si accorgeva poi col tempo che un utente fosse in grado di saltare la home page e accedere
direttamente ad altre pagine (ad esempio: la pagina di ricerca di Plone) e fosse quindi in grado
di vedere documenti che si credevano segreti.

.. note::

   Il "*workflow intranet*" fornito da Plone **può non essere ottimale** per i vostri scopi! 

In questi casi la ricerca di Plone può darvi da subito un'idea della situazione ed aiuta molto
a trovare potenziali problemi ma può non bastare poiché esistono tipi di contenuto che sono
configurati per non essere "ricercabili".
La loro visibilità va comunque verificata

