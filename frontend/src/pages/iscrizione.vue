<template>
  <q-page class="flex flex-center background-cirf">
    <div v-if="loading===true" class="text-center">
      <q-card-section class="q-py-lg">
        <q-spinner color="white" size="3em" :thickness="5" />
      </q-card-section>
    </div>
    <DefaultForm
      :eventData="eventData"
      :slug="$route.params.evento"
      v-if="eventData.modello_form_evento === 'default' || eventData.modello_form_evento === ''"
    />
    <DefaultFormConAttivita
      :eventData="eventData"
      :slug="$route.params.evento"
      v-else-if="eventData.modello_form_evento === 'con_attivita'"
    />
  </q-page>
</template>

<style lang="scss">
.background-cirf {
  background: $primary;
}
@media (min-width: $breakpoint-sm-min) {
  .background-cirf {
    background: #4c3a1a url("~assets/img/ray-hennessy-oEcQFq0NKjo-unsplash.jpg");
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
  }
}
</style>

<script>
import DefaultForm from "../components/DefaultForm.vue";
import DefaultFormConAttivita from "../components/DefaultFormConAttivita.vue";

export default {
  name: "Iscrizione",
  components: {
    DefaultForm,
    DefaultFormConAttivita
  },
  data() {
    return {
      loading: true,
      eventData: ""
    };
  },
  mounted() {
    this.$axios
      .get(
        process.env.API_SERVER_URL +
          "/api/events/" +
          this.$route.params.evento +
          "/"
      )
      .then(response => {
        this.eventData = response.data.evento;
        console.log(this.eventData);
        this.loading = false;
      })
      .catch(e => {
        console.error(e);
        this.loading = false;
      });
  }
};
</script>
