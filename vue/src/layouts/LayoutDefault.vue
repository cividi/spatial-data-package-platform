<template>
    <main>
      <main-navigation />

      <v-content>
        <slot/>
      </v-content>
    </main>
</template>

<script>

export default {
  name: 'LayoutDefault'
};
</script>
