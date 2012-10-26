===========================
Plone: worfklow e sicurezza
===========================

Un libro (in lingua italiana) riguardo il `CMS Plone`__ e nello specifico la gestione della
sicurezza e dei workflow.

__ http://plone.org/

La documentazione è generate usando `Sphinx`__.

__ http://sphinx.pocoo.org/

Come generare la documentazione
===============================

Lanciare inizializzare e lanciare buildout::

    % python2.7 bootstrap.py
    % ./bin/buildout

Successivamente si consiglia di lavorare nella directory ``docs``::

    % cd docs

Per generare la documentazione HTML::

    % make html
    
Per generare il libro in PDF::

    % make latexpdf

Versione HTML online
====================

La versione aggiornata e online del libro è ospitata all'indirizzo
http://plone-worfklow-e-sicurezza.readthedocs.org
