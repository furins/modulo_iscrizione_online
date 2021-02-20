# istruzioni per l'installazione

eseguire i seguenti comandi

    ./build

al termine, nella cartella dist sono presenti due sotto-cartelle

- <nome_dell_app>
- static

la prima deve essere utilizzata per distribuire l'app attraverso uwsgi o gunicorn, esponendola con l'URL radice "/"
la seconda deve essere utilizzata per distribuire tramite apache/nginx i file statici, esponendola con l'URL radice "/static"
