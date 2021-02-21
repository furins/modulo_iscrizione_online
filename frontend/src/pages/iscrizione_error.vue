<template>
  <q-page class="flex flex-center background-cirf">
    <transition appear enter-active-class="animated fadeIn">
      <q-card class="elenco-eventi shadow-12 animazione-lenta">
        <div class="text-center">
          <img alt="CIRF logo" src="~assets/cirf.svg" />
        </div>

        <q-separator />
        <q-card-section>
          <div class="text-h6 q-my-lg text-negative text-center">ERRORE DI VALIDAZIONE!</div>
          <p>Sembra che qualcosa sia andato storto. Vi preghiamo di contattare la segreteria CIRF per confermare la vostra iscrizione.</p>
          <div class="text-center">
            <q-btn
              unelevated
              rounded
              color="negative"
              label="Contatti CIRF"
              class="q-ma-md bottone"
              size="md"
              href="https://www.cirf.org/contatti/"
              type="a"
            />
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
