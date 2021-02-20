<template>
  <q-layout view="lHh Lpr lFf">
    <q-page-container>
      <router-view />
    </q-page-container>
    <q-footer>
      <q-toolbar>
        <q-toolbar-title
          class="text-right text-secondary text-subtitle1"
        >rev. {{$application_built.version}}</q-toolbar-title>
      </q-toolbar>
    </q-footer>
  </q-layout>
</template>

<script>
export default {
  name: "MainLayout",
  data() {
    return {
      loading: true,
      eventi: []
    };
  }
};
</script>
