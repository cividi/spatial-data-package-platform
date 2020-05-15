<!-- eslint-disable -->
<i18n>
{
  "de": {
    "title": "Fehler",
    "text": "Da ist was schiefgegangen...",
    "netwokerror.title": "Verbindungsfehler",
    "netwokerror.text": "Benötigte Daten konnten nicht geladen werden.",
    "button.ok": "OK",
    "button.retry": "Seite neu laden",
    "button.back": "Zur Startseite"
  },
  "fr": {
    "title": "Fehler",
    "text": "Da ist was schiefgegangen...",
    "netwokerror.title": "Verbindungsfehler",
    "netwokerror.text": "Benötigte Daten konnten nicht geladen werden.",
    "button.ok": "OK",
    "button.retry": "Nochmals versuchen",
    "button.back": "Zur Startseite"
  }
}
</i18n>
<!-- eslint-enable -->

<template>
<v-dialog persistent v-model="settings.open" class="errormessage" width="400">
 <v-card>
        <v-card-title>{{titleString}}</v-card-title>
        <v-card-text>{{textString}}</v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn text @click="forceReload">{{$t('button.retry')}}</v-btn>
          <v-btn color="primary" text :to="'/' + $i18n.locale + '/'">{{$t('button.back')}}</v-btn>
        </v-card-actions>
      </v-card>
</v-dialog>
</template>

<style scoped>
.errormessage {
  z-index: 666;
}
</style>

<script>
export default {
  name: 'ErrorMessage',
  data() {
    return {
    };
  },
  props: {
    settings: Object
  },

  computed: {
    titleString() {
      if (this.settings.title) {
        return this.settings.title;
      } if (this.settings.type) {
        return this.$t(`${this.settings.type}.title`);
      }
      return this.$t('title');
    },
    textString() {
      if (this.settings.text) {
        return this.settings.text;
      } if (this.settings.type) {
        return this.$t(`${this.settings.type}.text`);
      }
      return this.$t('text');
    }
  },
  methods: {
    forceReload() {
      window.location.reload();
    }
  }
};
</script>
