<template>
    <main>
      <main-navigation />

      <v-main>
        <v-slide-y-transition mode="out-in">
          <slot/>
        </v-slide-y-transition>
        <version />
      </v-main>
    </main>
</template>

<script>

export default {
  name: 'LayoutDefault'
};
</script>
