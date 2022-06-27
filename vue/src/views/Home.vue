<!-- eslint-disable -->
<i18n>
{
  "de": {
    "img.1.alt":
      "dføur",
    "h2.2": "Beispiele",
    "networkerror": "Die Projekterfassung ist zur Zeit nicht verfügbar."
  },
  "fr": {
    "img.1.alt":
      "Le dføur",
    "h2.2": "Examples",
   "networkerror": "La recherche n'est pas disponible actuellement."
  },
  "en": {
    "img.1.alt":
      "dføur",
    "h2.2": "Examples",
    "networkerror": "The data is currently not available, please try again soon."
  },
  "it": {
    "img.1.alt":
      "dføur",
    "h2.2": "Esempi",
    "networkerror": "I dati non sono attualmente disponibili, riprovare al più presto."
  }
}
</i18n>
<!-- eslint-enable -->

<template>
<div>
  <v-container my-12>
    <v-col sm="12" lg="8">
      <div
        id="project"
        v-html="homepageSnippet">
      </div>
    </v-col>
  </v-container>

  <div id="teaser">
    <h1 id="abriss-atlas-schweiz">Abriss-Atlas Schweiz</h1>
    <p>In der Schweiz werden über 500kg pro Sekunde abgerissen. Woher kommt diese Masse?
      Was für Gebäude werden abgerissen?
      Diesen Fragen möchte der Abriss-Atlas Schweiz nachgehen.</p>
    <h2 id="testphase">Testphase</h2>
    <p>Diese Website ist im Aufbau. Wir arbeiten partizipatorisch und verbessern im Prozess.
      Die Einträge im Atlas bilden unter Anderem die Grundlage für die Ausstellung
      “Die Schweiz: Ein Abriss” im Herbst 2022 im Schweizerischen Architekturmuseum S AM.
      Um möglichst lange über die Mauern des Museums zu wirken, wird diese Website und ihre
      Einträge so früh wie möglich der Öffentlichkeit zugänglich gemacht.</p>
    <h2 id="wer-kann-gebäude-registrieren">Wer kann Gebäude registrieren?</h2>
    <p>Jede und jeder kann über das Formular einfach Gebäude erfassen, Kommentare und
      Geschichten zu den Häusern schreiben.</p>
    <h2 id="wie-finde-ich-heraus-wo-gebäude-abgerissen-werden">Wie finde ich heraus, wo
      Gebäude abgerissen werden?</h2>
    <p>Geh mit wachen Augen durch dein Quartier und melde, wenn du einen Abbruch entdeckst! </p>
    <p>Wenn du gezielter vorgehen willst, sind geplante Abbrüche in Bauanzeigen oder Publikationen
      online in den Amtsblättern der Gemeinden zu finden. Je nach Gemeinde sind die Begriffe
      etwas anders, bekannte Suchmaschinen sind hier eine Hilfe.
      Einige Beispiele:</p>
    <ul>
      <li>
        <a href="https://www.bern.ch/themen/planen-und-bauen/baupublikationen">
          Stadt Bern
        </a>
      </li>
      <li><a href="https://info.engadin.online/stmoritz">St. Moritz</a></li>
      <li><a href="https://www.koeniz.ch/aktuell/amtliche-publikationen.page/8">Köniz</a></li>
    </ul>
    <h2 id="fehlermeldungen">Fehlermeldungen</h2>
    <p>Hast Du einen Fehler entdeckt:</p>
    <ul>
      <li>Fehler in der Programmierung, Homepage o.ä.: bitte inkl. Link &amp; Screenshot melden an:
        <a href="mailto:support@dfour.io">support@dfour.io</a>
      </li>
      <li>Fehler in den Daten oder Rückmeldungen zum Projekt:
        <a href="mailto:atlas@countdown2030.ch">atlas@countdown2030.ch</a>
      </li>
    </ul>
    <h2 id="impressum">Impressum</h2>
    <h3 id="lancierung">Lancierung</h3>
    <ul>
      <li><a href="https://www.countdown2030.ch">Countdown 2030</a>, Verein für zukunftsfähige Baukultur</li>
      <li>Grafik: <a href="https://www.nerak.ch">Karen Trachsel</a></li>
      <li>Programmierung: <a href="https://dfour.space">dfour</a></li>
    </ul>
    <h3 id="partner">Partner</h3>
    <ul>
      <li><a href="https://www.sam-basel.org">S AM Schweizerisches Architekturmuseum</a></li>
      <li><a href="https://www.ita.arch.ethz.ch">Professur für Konstruktionserbe und Denkmalpflege, ETH Zürich, Prof.
          Silke Langenberg</a></li>
      <li><a href="https://www.heimatschutz.ch">Schweizer Heimatschutz</a></li>
    </ul>
    <h3 id="medienpartner">Medienpartner</h3>
    <ul>
      <li><a href="https://www.hochparterre.ch">Hochparterre</a></li>
      <li><a href="https://www.espazium.ch">espazium</a></li>
      <li><a href="https://www.espazium.ch/de/tec21">Tec21</a></li>
      <li><a href="https://www.espazium.ch/it/archi">Archi</a></li>
      <li><a href="https://www.espazium.ch/fr/revue-traces">Tracé</a></li>
      <li><a href="https://bajour.ch/">Bajour</a></li>
      <li><a href="https://tsri.ch/">Tsüri</a></li>
    </ul>
  </div>

  <v-snackbar color="primary" v-model="snackbar" :timeout="9000">
    {{ $t('networkerror') }}
    <v-btn icon @click="snackbar=false" >
      <v-icon>mdi-close-circle-outline</v-icon>
    </v-btn>
  </v-snackbar>
</div>

</template>

<style>
#teaser {
  display: none;
}
#project h1,
#project h2,
#project h3,
#project h4 {
  text-transform: uppercase;
  /* border-bottom: 6px solid black; */
  padding-bottom: 0;
  line-height: 1.2em;
  margin-bottom: 0.1em;
  margin-top: 1.5em;
  width: fit-content;
}
#project h2 {
  font-weight: bolder;
}
#project a {
  /* border-bottom: 6px solid black; */
  font-weight: bold;
}
#project ul {
  padding-bottom: 1em;
}
#project ul li {
  margin-bottom: 0.3em;
}
</style>

<script>
import gql from 'graphql-tag';

export default {
  name: 'Home',

  data() {
    return {
      djangobaseurl: process.env.VUE_APP_DJANGOBASEURL,
      snapshotsExamples: [],
      networkError: false,
      snackbar: false,
      searchEnabled: true,
      exampleGalleryEnabled: true,
      homepageSnippet: ''
    };
  },

  created() {
    this.$store.commit('setBfsnumber', '');
    this.$store.commit('setBfsname', '');
  },

  async mounted() {
    const sessionid = this.$cookies.get('sessionid', '');
    if (sessionid) {
      this.$store.commit('setIsLoggedIn');
      const workspaceid = this.$cookies.get('workspaceid', '');
      if (workspaceid) {
        const hashed = workspaceid.replace(/^"|"$/g, '').split('/');
        const wshash = hashed[0];
        const hash = hashed[1];
        this.$router.push({ name: 'workspaceRedirect', params: { wshash, hash } });
      }
    } else {
      this.$store.commit('setIsLoggedOut');
    }
    await this.getConfig();
    await this.getSnapshotsExamples();
  },

  methods: {
    async getConfig() {
      const language = this.$i18n.locale;
      const configResult = await this.$apollo.query({
        query: gql`query getconfig($language: String) {
          config(language: $language) {
            searchEnabled,
            exampleGalleryEnabled,
            homepageSnippet
          }
        }`,
        variables: {
          language
        },
        fetchPolicy: 'no-cache' // fixes empty homepage, apollo bug?
      }).catch(() => {
        this.snackbar = true;
        this.networkError = true;
      });
      if (configResult) {
        const config = configResult.data.config;
        if (config) {
          this.searchEnabled = config.searchEnabled;
          this.exampleGalleryEnabled = config.exampleGalleryEnabled;
          this.homepageSnippet = this.md(config.homepageSnippet);
        }
      }
    },

    async getSnapshotsExamples() {
      const result = await this.$apollo.query({
        query: gql`{
          snapshots(isShowcase: true) {
            edges {
              node {
                id
                pk
                title
                topic
                thumbnail
                municipality {
                  name
                }
              }
            }
          }
        }`
      }).catch(() => {
        this.snackbar = true;
        this.networkError = true;
      });
      if (result) {
        const snapshots = result.data.snapshots.edges.map(snapshot => snapshot.node);
        // fake random, for more randomness, use https://www.npmjs.com/package/lodash.shuffle package
        this.snapshotsExamples = snapshots.sort(() => (Math.random() > 0.5 ? -1 : 1)).slice(0, 3);
        this.snackbar = false;
        this.networkError = false;
      }
    }
  }
};
</script>
