==========
I Permessi
==========

Al capitolo precedente è stata data la definizione di ruolo e si è visto come questo sia associato
direttamente con i **permessi**, anzi come il ruolo non sia altro che un raggruppamento di
permessi.

Se un utente con ruolo di *Editor* può fare alcune delle cose possibili anche al *Revisore*
(accedere alla vista dei contenuti di una cartella, modificare un documento, ...) è dovuto al fatto
che condividono uno o più permessi.

I permessi sono il vero cuore della sicurezza di Zope, e quindi di Plone poiché controllano una
singola azione o un singolo comportamento del sistema.

Sappiate però che agiscono a basso livello; fin'ora ci siamo abituati a lavorare sull'interfaccia
di Plone, per poi muoverci brevemente a livelli più bassi (in ZMI) e vedere poco codice.
I permessi invece *non sono visibili o gestiti a livello Plone*, per questo motivo non sono nemmeno
tradotti.

Visto che i permessi sono utilizzati in tantissimi contesti e controllano numerose funzionalità del
CMS, non sarebbe utile scendere in un eccessivo dettaglio.
Sappiate ad esempio che la singola chiamata ad un metodo di una classe Python potrebbe essere
protetta da un permesso, il che significa che quando quel metodo viene chiamato per reagire ad
un'azione di un utente, viene verificato se l'utente possiede il permesso.
In caso contrario viene lanciata un'eccezione speciale: **Unauthorized** (**Non autorizzato**) che
di solito genera la classica pagina di permessi insufficienti di Plone.

.. figure:: _static/unauthorized-error.png
   :alt: Non autorizzato

   *La classica pagina di errore di Plone per permessi insufficienti*

La gestione dei permessi
========================

La gestione dei permessi avviene da ZMI, dalla radice del sito, dalla stessa pagina da cui abbiamo
creato in precedenza un nuovo ruolo: il link **Security**.

.. figure:: _static/zmi-manage-security-link.png
   :alt: Link alla manage access in ZMI

   *Link per andare alla gestione della sicurezza del sito Plone, da ZMI*

Un accesso diretto alla pagina (che permette anche di non aprirla nel solito frame HTML usato dalla
ZMI) è richiamare manualmente ``/manage_access`` sul contesto del sito Plone.

Ad esempio, se state provando un sito locale, dovrete probabilmente digitare:

    http://localhost:8080/book/manage_access

Quello che vi troverete davanti è una griglia la cui logica è riassunta nello schema seguente.

.. figure:: _static/zmi-security-grid-for-dummies.png
   :alt: Struttura generale della gestioned della sicurezza

   *Schema generale della gestione della sicurezza del sito*

In **riga** avrete disponibili i permessi, e come potete vedere in un sito Plone possono essere
molti.

In **colonna** ci sono i ruoli, tutti i ruoli definiti, che siano Zope, Plone o applicativi
(anche il nostro *Super Revisore* si trova qui).

Preso come riferimento un qualunque permesso e un qualunque ruolo, trovate all'incrocio della riga
e della colonna una casella checkbox.
Se il checkbox è *selezionato* quel ruolo ha il relativo permesso nel contesto (il sito Plone).
Se il checkbox è *deselezionato* quel ruolo non ha il permesso.

Capire "Acquire permission settings?"
-------------------------------------

Avrete notato la presenta di una serie di checkbox in prima colonna con intestazione "**Acquire
permission settings?**".

Il loro significato è estremamente importante e diventerà vitale per la realizzazione di buoni
workflow.

