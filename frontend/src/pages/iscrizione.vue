<template>
  <q-page padding>
    {{ $route.params.evento }}
    <q-btn label="torna indietro" @click="$router.push('/')" />
  </q-page>
</template>

<script>
export default {
  // name: 'PageName',
};
</script>
