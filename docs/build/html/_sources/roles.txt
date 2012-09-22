=======
I Ruoli
=======

La miglior definizione di "ruolo Plone" che posso trovare è questa:

    I ruoli sono un accorpamento di **permessi**. I ruoli sono i **poteri** di un utente.

Non c'è altro da dire dal punto di vista "tecnico": quando assegnate un ruolo ad un utente, state
fornendo in realtà una serie di permessi (il vero motore della sicurezza di Zope).
Come già detto in precedenza infatti non potete in nessun modo assegnare permessi agli utenti o
ai gruppi, ma potete solo assegnare ruoli.

Questa è una delle prime caratteristiche che fanno assaporare la potenza del sistema sottostante.
Prendiamo ad esempio in ruolo del **Lettore** (che verrà introdotto meglio in seguito).
cosa significhi essere un "lettore" non è qualcosa scritto nella roccia; siti diversi (e senza
dover per forza sviluppare del codice) possono differire dalla sua definizione, aumentando o
limitando i poteri (permessi) del ruolo.

I ruoli predefiniti
===================

Plone (e il framework Zope sottostante) forniscono una serie di ruoli predefiniti il cui
funzionamento è bene approfondire e comprendere.
Il motivo principale è che, sebbene sia possibile creare nuovi ruoli, l'eventualità di doverlo fare
è meno frequente di quanto si pensi (anche se non impossibile).

I ruoli forniti di Zope
-----------------------

.. figure:: _static/zmi-security-zope-roles.png
   :alt: I ruoli di Zope

   *I quattro ruoli Zope, visti da ZMI*

I ruoli forniti da Zope sono quattro e non sono modificabili od eliminabili. Sulla loro presenza
si basa il funzionamento della sicurezza dell'application server, e quindi di Plone.

Anonimo (Anonymous)
~~~~~~~~~~~~~~~~~~~

**Anonimo** (**Anonymous**) è il ruolo assegnato agli utenti anonimi.
E' un ruolo speciale ed ha un comportamento diverso da tutti gli altri ruoli.
Non è infatti possibile definire un permesso accessibile dal ruolo Anonymous ma non da altri ruoli:
un potere dato ad un anonimo è di certo fornito anche a *qualunque* utente del sito.

Questo può sembrare scontato dal punto di vista logico, ma per gli altri ruoli può non essere così:
con altri ruoli sarebbe possibile disegnare una policy di sicurezza che assegni un permesso ad un
ruolo "poco importante" e non darlo ad un ruolo importante (un esempio: dare il permesso di vedere
un contenuto ad un *Collaboratore* del sito ma non al *Manager*. Possibile, anche se totalmente
illogico e sconsigliato).

Il ruolo di Anonimo è per sua natura associato con il tipo di utente anonimo. Nel disegnare workflow
per i vostri contenuti questo ruolo assume parecchia importanza: un errore nell'assegnare un
permesso di troppo a questo utente e la sicurezza del vostro siti potrebbe risentirne.

Autenticato (Authenticated)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Autenticato** (**Authenticated**) è il ruolo automaticamente assegnato ai visitatori del sito
che hanno eseguito un qualunque tipo di autenticazione, anche tramite `autenticazione basic`__ via
ZMI.

__ http://en.wikipedia.org/wiki/Basic_access_authentication

Un utente con ruolo *Autenticato* è quindi un utente a livello Zope.

Questo ruolo non è solitamente molto utilizzato nei workflow di Plone, preferendovi, per
correttezza, il ruolo di *Collaboratore*.

Manager
~~~~~~~

L'Alpha e l'Omega dei ruoli. Chi ha ruolo **Manager** ha solitamente potere assoluto nel sito Plone
ed entra senza restrizioni in ZMI.

E' un ruolo ovviamente pericoloso e non va mai assegnato a sproposito. Come regola generale, se il
vostro utente *non ha* bisogno di accedere alla ZMI, *Manager* non è il ruolo migliore da
assegnargli, ma va preferito il ruolo di *Amministratore del Sito*.

E' lecito avere installazioni di Plone dove esiste un solo utente con questo ruolo: **admin**,
l'utente predefinito a livello Zope che è di solito il creatore dei siti Plone.

Owner
~~~~~

Il concetto di **Possessore** (**Owner**), per quanto orribilmente tradotto in italiano, nasce a
livello Zope.
Un primo esempio: l'utente *admin*, introdotto poco fa, ha di solito il ruolo di *Owner*
sull'"oggetto sito Plone".

E' un ruolo che va ben compreso e di solito deve essere assegnato ad un solo utente, per quanto è
possibile fornirlo a più persone (ciò oggi è fortunatamente più difficile da farsi da interfaccia
Plone, mentre in versioni precedenti del CMS era purtroppo un modo di operare molto comune).



