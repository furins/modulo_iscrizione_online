# BUGFIX

- [ ] CORS/CRSF per axios
- [ ] nell'amministrazione le inline mostrano intestazioni che non servono, ma non riesco a nasconderle con il css
- [ ] lo slug deve essere generato automaticamente quando l'evento è creato. In tutti gli altri casi solo se non è già definito

# NEW FEATURES

- [ ] alla conferma dell'iscrizione, far puntare a un indirizzo arbitrario (configurabile per evento, di default manda alla home del sito)
- [ ] gestire le configurazioni per ciascun sito
- [ ] i link esterni dovrebbero aprirsi in finestre diverse
- [ ] consentire di far puntare al sito con dei CNAME (con tutte le implicazioni del caso, in particolare CORS)
- [ ] excel dati iscrizioni seminari
- [ ] interfaccia di admin personalizzata, in quasar

# TOOLS

- [ ] il build necessita che sia attivo il database di sviluppo per predisporre i makemigrations. Idealmente dovrebbe partire da un database vuoto, caricare tutte le migrazioni precedenti e poi effettuare un makemigrations ma non sono sicuro funzioni correttamente
- [ ] il build, in caso di successo, dovrebbe
- [ ] generare i changelog automaticamente (https://www.mokkapps.de/blog/how-to-automatically-generate-a-helpful-changelog-from-your-git-commit-messages/)
- [ ] configurare i build con un file YAML (per evitare env.dev e env.prod)
- [ ] verificare che questi strumenti di build non diventino alla fine un vero e proprio CI
