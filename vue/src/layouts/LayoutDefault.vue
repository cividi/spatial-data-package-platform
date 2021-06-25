<template>
    <main>
      <main-navigation />

      <v-content>
        <v-slide-y-transition mode="out-in">
          <slot/>
        </v-slide-y-transition>
      </v-content>

      <version />
    </main>
</template>

<script>

export default {
  name: 'LayoutDefault'
};
</script>
