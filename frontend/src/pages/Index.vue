<template>
  <q-page class="flex flex-center background-cirf">
    <transition appear enter-active-class="animated fadeIn">
      <q-card class="elenco-eventi shadow-12 animazione-lenta">
        <div class="text-center">
          <img alt="CIRF logo" src="~assets/cirf.svg" />
        </div>
        <q-card-section>
          <q-separator />
          <div v-if="loading===true" class="text-center">
            <q-card-section class="q-py-lg">
              <q-spinner color="primary" size="3em" :thickness="2" />
            </q-card-section>
          </div>
          <div v-else>
            <q-card-section class="q-pt-none" v-if="eventi.length > 0">
              <div class="text-h6 q-my-lg text-primary">Prossimi eventi</div>
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
                  href="https://www.cirf.org/it/contatti-cirf/"
                  class="q-ma-md bottone"
                  size="md"
                  type="a"
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
              <div class="q-py-none text-right muted">rev. {{$application_built.version}}</div>
            </q-card-section>
          </div>
        </q-card-section>
      </q-card>
    </transition>
  </q-page>
</template>
<style lang="scss">
.background-cirf {
  background: $primary;
}
.elenco-eventi {
  width: 90%;
  max-width: 90vw;
}
@media (min-width: $breakpoint-sm-min) {
  .animazione-lenta {
    animation-duration: 2s;
  }
  .background-cirf {
    background: #4c3a1a url("~assets/img/ray-hennessy-oEcQFq0NKjo-unsplash.jpg");
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
  }
  .elenco-eventi {
    img {
      width: 50%;
    }
    width: 100%;
    max-width: 50vw;
  }
}
.muted {
  color: #eee;
}
.lista {
  background-color: $secondary;
}
.bottone {
  min-width: 33%;
}
</style>
<script>
export default {
  name: "PaginaIniziale",
  components: {},
  data() {
    return {
      loading: true,
      eventi: []
    };
  },
  mounted() {
    this.$axios
      .get(process.env.API_SERVER_URL + "/api/list/")
      .then(response => {
        this.eventi = response.data.eventi;
        this.loading = false;
      })
      .catch(e => {
        console.error(e);
        this.loading = false;
      });
  }
};
</script>
