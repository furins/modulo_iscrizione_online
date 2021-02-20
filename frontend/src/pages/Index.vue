<template>
  <q-page class="flex flex-center background-cirf">
    <q-card class="elenco-eventi shadow-12">
      <div class="text-center">
        <img alt="CIRF logo" src="~assets/cirf.svg" />
      </div>
      <q-card-section>
        <q-separator />
        <q-card-section class="q-pt-none" v-if="eventi.length > 0">
          <div class="text-h6 q-my-lg text-primary">Iscrizione eventi</div>
          <q-list bordered separator class="lista">
            <q-item
              clickable
              v-ripple
              v-for="evento in eventi"
              :key="evento.slug"
              @click="$router.push('/'+evento.slug+'/')"
            >
              <q-item-section>
                {{evento.titolo}}
                <q-item-label caption>{{evento.descrizione}}</q-item-label>
              </q-item-section>

              <q-item-section side>
                <q-icon name="keyboard_arrow_right" color="dark" />
              </q-item-section>
            </q-item>
          </q-list>
        </q-card-section>
        <q-card-section v-else>
          <div class="text-h6 q-mt-lg text-primary text-center">Nessun evento programmato</div>
          <div
            class="q-pt-md q-pb-md text-center"
          >Per conoscere gli eventi organizzati dal Centro Italiano per la Riqualificazione Fluviale</div>
          <div class="text-center">
            <q-btn
              unelevated
              rounded
              color="negative"
              label="Iscriviti alla newsletter"
              class="q-ma-md bottone"
              size="md"
            />
            <q-btn
              unelevated
              rounded
              color="primary"
              label="Seguici su facebook"
              class="q-ma-md bottone"
              size="md"
              href="https://www.facebook.com/CIRF.org/"
              type="a"
            />
          </div>
        </q-card-section>
      </q-card-section>
    </q-card>
  </q-page>
</template>
<style lang="scss">
.background-cirf {
  background-color: $primary;
}
@media (min-width: $breakpoint-sm-min) {
  .elenco-eventi {
    img {
      width: 50%;
    }
    width: 100%;
    max-width: 50vw;
  }
}

.lista {
  background-color: $secondary;
}
.bottone {
  min-width: 33%;
}
</style>
<script>
import axios from "axios";

export default {
  name: "PaginaIniziale",
  components: {},
  data() {
    return {
      eventi: []
    };
  },
  mounted() {
    axios
      .get(process.env.API_SERVER_URL + "/api/list/")
      .then(response => (this.eventi = response.data.eventi));
  }
};
</script>
