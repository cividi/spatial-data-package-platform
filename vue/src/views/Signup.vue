<template>
  <v-container>
      <v-layout
        wrap
      >
        <v-flex>
          <h1>Account erstellen</h1>
          <v-row justify="center">
              <v-col sm="12" md="8" lg="6">
              <div class="typeform-widget" :data-url="dataurl"
                data-transparency="50" style="width: 100%; height:500px"></div>
                <div style="font-family: Sans-Serif;font-size: 12px;
                  color: #999;opacity: 0.5; padding-top: 5px;">
                <!-- eslint-disable-next-line max-len -->
                <a href="https://admin.typeform.com/signup?utm_campaign=vjVoPr&amp;.utm_source=typeform.com-01DH3Y9W4K4NQZANA3FZ4EVVMZ-essentials&amp;.utm_medium=typeform&amp;.utm_content=typeform-embedded-poweredbytypeform&amp;.utm_term=EN"
                  style="color: #999" target="_blank"></a>
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
      if (this.$route.params.gemeinde) {
        return `https://cividi.typeform.com/to/vjVoPr?gemeinde=${this.$route.params.gemeinde}`;
      }
      return 'https://cividi.typeform.com/to/vjVoPr';
    }
  },

  props: {
    gemeinde: String
  },

  mounted() {
    // eslint-disable-next-line
    (function() { var qs,js,q,s,d=document, gi=d.getElementById, ce=d.createElement, gt=d.getElementsByTagName, id="typef_orm", b="https://embed.typeform.com/"; if(!gi.call(d,id)) { js=ce.call(d,"script"); js.id=id; js.src=b+"embed.js"; q=gt.call(d,"script")[0]; q.parentNode.insertBefore(js,q) } })()
  }
};
</script>
