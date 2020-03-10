<template>
  <v-container my-6>
      <v-layout
        wrap
      >
        <v-flex>
          <v-row justify="center">
              <v-col sm="12" md="8" lg="6">
                <div style="padding-top:20px;">
                  <iframe width="100%" height="704" :src="dataurl" frameborder="0">
                  </iframe>
                </div>
              </v-col>
          </v-row>
        </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
    };
  },

  computed: {
    dataurl() {
      if (this.$store.state.bfsnumber && this.$store.state.bfsname && this.$route.params.lang) {
        return `//cividi.typeform.com/to/vjVoPr?bfs_gmdno=${this.$store.state.bfsnumber}&bfs_gmdname=${this.$store.state.bfsname}&gmdscn_lang=${this.$route.params.lang}`;
      }
      return `//cividi.typeform.com/to/vjVoPr?gmdscn_lang=${this.$route.params.lang}`;
    }
  }
};
</script>
