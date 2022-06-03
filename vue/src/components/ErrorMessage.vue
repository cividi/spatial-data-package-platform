<!-- eslint-disable -->
<i18n>
{
  "de": {
    "title": "Fehler",
    "text": "Da ist was schiefgegangen...",
    "netwokerror.title": "Verbindungsfehler",
    "netwokerror.text": "Daten konnten nicht geladen werden.",
    "button.ok": "OK",
    "button.retry": "Seite neu laden",
    "button.back": "Zur Startseite",
    "button.contact": "Problem melden"
  },
  "fr": {
    "title": "Erreur",
    "text": "Quelque chose a mal tourné...",
    "netwokerror.title": "Erreur de connexion",
    "netwokerror.text": "Les données n'ont pas pu être chargées.",
    "button.ok": "OK",
    "button.retry": "Recharger la page",
    "button.back": "Vers la page d'accueil",
    "button.contact": "Signaler un problème"
  },
  "en": {
    "title": "Error",
    "text": "Something went wrong...",
    "netwokerror.title": "Connection error",
    "netwokerror.text": "Data could not be loaded.",
    "button.ok": "OK",
    "button.retry": "Reload page",
    "button.back": "Back to the start page",
    "button.contact": "Report problem"
  },
  "it": {
    "title": "Errore",
    "text": "Qualcosa è andato storto...",
    "netwokerror.title": "Errore di connessione",
    "netwokerror.text": "Non è stato possibile caricare i dati.",
    "button.ok": "OK",
    "button.retry": "Ricarica la pagina",
    "button.back": "Torna alla pagina iniziale",
    "button.contact": "Segnala il problema"
  }
}
</i18n>
<!-- eslint-enable -->

<template>
<v-dialog persistent v-model="settings.open" class="errormessage" width="600">
 <v-card>
        <v-card-title>{{titleString}}</v-card-title>
        <v-card-text>{{textString}}</v-card-text>
        <v-card-actions class="pb-4 pr-4">
          <v-row>
            <v-col>
              <v-btn depressed color="gray" @click="composeEmail">{{$t('button.contact')}}</v-btn>
            </v-col>
            <v-col>
              <v-btn depressed color="primary" class="ml-4" :to="'/' + $i18n.locale + '/'">
                {{$t('button.back')}}
              </v-btn>
            </v-col>
          </v-row>
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
    },
    composeEmail() {
      window.location.href = `mailto:support@dfour.space?subject=${this.titleString}&body=`;
    }
  }
};
</script>
