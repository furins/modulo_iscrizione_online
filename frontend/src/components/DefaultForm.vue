<template>
  <q-card class="main-form shadow-12">
    <q-card-section class="q-py-none q-px-lg">
      <div class="text-h6 q-my-lg text-primary text-center">Modulo di iscrizione all'evento</div>
      <div class="text-h4 q-my-lg text-primary text-center">{{eventData.titolo}}</div>
      <div class="q-my-lg row q-col-gutter-md">
        <p class="col-12 col-sm-9">{{eventData.descrizione}}</p>
        <p class="col-12 col-sm-3 text-center">
          <q-btn
            rounded
            outline
            color="primary"
            :label="eventData.testo_link"
            v-if="eventData.link && eventData.link !== ''"
            size="md"
            type="a"
            :href="eventData.link"
          />
        </p>
      </div>
      <q-separator class="q-my-md" />
      <q-form @submit="onSubmit" class="q-my-lg">
        <div class="row q-col-gutter-md">
          <q-input
            class="col-12 col-sm-6"
            autocomplete="fname"
            v-model="nome"
            label="Nome *"
            hint="Inserisci il tuo nome"
            lazy-rules
            :rules="[ val => val && val.length > 0 || 'Per favore inserisci il tuo nome']"
          />
          <q-input
            v-model="cognome"
            name="cognome"
            autocomplete="lname"
            class="col-12 col-sm-6"
            label="Cognome *"
            hint="Inserisci il tuo cognome"
            lazy-rules
            :rules="[ val => val && val.length > 0 || 'Per favore inserisci il tuo cognome']"
          />
          <q-input
            class="col-12 col-sm-6"
            v-model="email"
            autocomplete="email"
            label="Email *"
            hint="Inserisci la tua email"
            type="email"
            lazy-rules
            :rules="[ val => val && val.length > 9 && val.includes('@') && val.includes('.') || 'Per favore inserisci un\'email valida']"
          />
        </div>
        <q-list class="row">
          <q-item tag="label" v-ripple class="col-12 q-mt-lg">
            <q-item-section avatar top>
              <q-checkbox v-model="desidera_crediti" />
            </q-item-section>
            <q-item-section>
              <q-item-label>Richiesta crediti</q-item-label>
              <q-item-label caption>Desidero siano riconosciuti crediti dal mio Ordine professionale</q-item-label>
            </q-item-section>
          </q-item>
        </q-list>
        <div v-if="desidera_crediti === true" class="row q-mt-sm q-mb-lg q-col-gutter-md">
          <q-input
            class="col-12 col-sm-6"
            v-model="codice_fiscale"
            autocomplete="codice_fiscale"
            label="Codice Fiscale *"
            hint="Inserisci il tuo codice fiscale"
            lazy-rules
            :rules="[ val => val && val.length > 8 || 'Per favore inserisci il tuo codice fiscale']"
          />
          <q-select
            class="col-12 col-sm-6"
            v-model="ordine_di_appartenenza"
            :options="ordini_professionali"
            label="Ordine professionale *"
            hint="Inserisci l'Ordine professionale di appartenenza"
          />
          <q-select
            class="col-12 col-sm-4"
            autocomplete="region"
            v-model="regione"
            :options="regioni"
            label="Regione *"
            hint="Inserisci la Regione che ospita la sede dell'Ordine di appartenenza"
          />
          <q-input
            class="col-12 col-sm-3"
            v-model="provincia"
            autocomplete="province"
            label="Provincia"
            hint="Inserisci la provincia che ospita la sede dell'Ordine di appartenenza"
            lazy-rules
            :rules="[ val => val && val.length == 2 || 'Per favore inserisci la sigla della provincia (2 caratteri)']"
          />
          <q-input
            class="col-12 col-sm-3"
            v-model="matricola_ordine"
            autocomplete="matricola_ordine"
            label="Num. iscrizione all'ordine *"
            hint="Inserisci la matricola di iscrizione all'ordine"
            lazy-rules
            :rules="[ val => val && val.length > 0 || 'Per favore inserisci la tua matricola di iscrizione all\'ordine']"
          />
        </div>
        <q-list class="row">
          <q-item tag="label" v-ripple class="col-12">
            <q-item-section avatar top>
              <q-checkbox v-model="iscrizione_newsletter" />
            </q-item-section>
            <q-item-section>
              <q-item-label>Iscrizione alla newsletter</q-item-label>
              <q-item-label caption>
                Desidero iscrivermi alla newsletter dell'evento.
                <br />La newsletter vi manterrà aggiornati sulle attività pre- e post-evento
              </q-item-label>
            </q-item-section>
          </q-item>
          <q-item tag="label" v-ripple class="col-12">
            <q-item-section avatar top>
              <q-checkbox v-model="accettazione_privacy" />
            </q-item-section>
            <q-item-section>
              <q-item-label>Autorizzo il trattamento dei dati *</q-item-label>
              <q-item-label
                caption
              >Autorizzo il trattamento dei dati per l'espletamento delle attività di iscrizione e partecipazione al convegno</q-item-label>
            </q-item-section>
          </q-item>
        </q-list>
        <q-separator class="q-my-md" />

        <div class="text-right">
          <q-btn
            label="Torna indietro"
            color="primary"
            flat
            class="q-ml-sm"
            @click="$router.push('/')"
          />
          <q-btn
            label="Completa registrazione"
            type="submit"
            color="primary"
            :loading="loading"
            :disabled="loading"
          />
        </div>
      </q-form>
    </q-card-section>
  </q-card>
</template>

<style lang="scss">
.main-form {
  width: 90%;
  max-width: 90vw;
}
@media (min-width: $breakpoint-sm-min) {
  .main-form {
    img {
      width: 50%;
    }
    width: 100%;
    max-width: 50vw;
  }
}
.bottone {
  min-width: 33%;
}
</style>

<script>
import * as Sentry from "@sentry/vue";

// attenzione devono coincidere con  quanto indicato in /backend/iscrizioni/models.py
let regioni = [
  "Abruzzo",
  "Basilicata",
  "Calabria",
  "Campania",
  "Emilia-Romagna",
  "Friuli-Venezia Giulia",
  "Lazio",
  "Liguria",
  "Lombardia",
  "Marche",
  "Molise",
  "Piemonte",
  "Puglia",
  "Sardegna",
  "Sicilia",
  "Toscana",
  "Trentino-Alto Adige",
  "Umbria",
  "Valle d'Aosta",
  "Veneto"
];

let ordini_professionali = [
  "Consiglio nazionale ingegneri",
  "Consiglio nazionale architetti, pianificatori, paesaggisti e conservatori",
  "Consiglio nazionale dei chimici",
  "Consiglio nazionale dei geologi",
  "Ordine nazionale dei biologi",
  "Ordine nazionale dei dottori agronomi e dottori forestali"
];

export default {
  name: "DefaultForm",
  props: ["eventData", "slug"],
  data() {
    return {
      nome: "",
      cognome: "",
      email: "",
      iscrizione_newsletter: false,
      accettazione_privacy: false,
      desidera_crediti: false,
      codice_fiscale: "",
      matricola_ordine: "",
      regione: "",
      provincia: "",
      ordine_di_appartenenza: "",
      regioni: regioni,
      ordini_professionali: ordini_professionali,
      loading: false
    };
  },
  methods: {
    onSubmit() {
      if (this.accettazione_privacy !== true) {
        this.$q.notify({
          type: "negative",
          position: "top",
          message:
            "È necessario accettare l'autorizzazione al trattamento dei dati"
        });
      } else {
        try {
          this.loading = true;
          // acquisisco il token
          let token = "";
          // TODO si può annidare meglio vedi https://fractalideas.com/blog/making-react-and-django-play-well-together-single-page-app-model/
          this.$axios
            .get(process.env.API_SERVER_URL + "/csrf/")
            .then(response => {
              // attendere esito dell'invio e mostrare messaggio
              token = response.data.csrfToken;
              console.log(token);
              this.$axios
                .post(
                  process.env.API_SERVER_URL +
                    "/api/events/" +
                    this.$route.params.evento +
                    "/subscribe/",
                  {
                    nome: this.nome,
                    cognome: this.cognome,
                    email: this.email,
                    iscrizione_newsletter: this.iscrizione_newsletter,
                    accettazione_privacy: this.accettazione_privacy,
                    desidera_crediti: this.desidera_crediti,
                    codice_fiscale: this.codice_fiscale,
                    matricola_ordine: this.matricola_ordine,
                    regione: this.regione,
                    provincia: this.provincia,
                    ordine_di_appartenenza: this.ordine_di_appartenenza,
                    csrfmiddlewaretoken: token
                  },
                  { headers: { "X-CSRFToken": token } }
                )
                .then(response => {
                  var eventData = response.data;
                  console.log(eventData);
                  this.loading = false;
                  this.$q.notify({
                    type: "positive",
                    position: "top",
                    message: "Registrazione avvenuta con successo"
                  });
                  this.$router.push("/");
                })
                .catch(error => {
                  this.loading = false;
                  Sentry.captureException(error);

                  let caption = "";

                  if (error.response) {
                    if (error.response.status == 500) {
                      caption =
                        "C'è un errore sul server, abbiamo avvisato il nostro staff. Siete pregati di riprovare più tardi";
                    } else {
                      caption =
                        error.response.data.error +
                        "  (" +
                        error.response.status +
                        ")";
                    }
                  } else if (error.request) {
                    caption = "nessuna risposta ricevuta dal server";
                  } else {
                    caption = error.message;
                  }

                  this.$q.notify({
                    type: "negative",
                    position: "top",
                    timeout: 0,
                    actions: [{ label: "CHIUDI", color: "white" }],
                    caption: caption,
                    message: "Si è verificato un errore"
                  });
                });
            });
        } catch (err) {
          console.log(err);
          Sentry.captureException(err);
          this.loading = false;
        }
      }
    },

    onReset() {
      this.name = null;
      this.age = null;
      this.accept = false;
    }
  }
};
</script>
