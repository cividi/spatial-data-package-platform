<template>
    <main>
      <main-navigation />

      <v-main class="pa-0">
        <slot/>
      </v-main>
    </main>
</template>

<script>
export default {
  name: 'LayoutSnapshot'
};
</script>
