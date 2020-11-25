<!-- eslint-disable -->
<i18n>
{
  "de": {
    "h1.1": "Entdecke das Lebensraum-Potential deiner Gemeinde.",
    "p.1":
      "Der Gemeindescan ermöglicht Gemeindeverwaltungen auf einfache und kosteneffiziente Weise ein Bild von Nutzungen und Nutzern in Ihrer Gemeinde zu erhalten. Flächennutzung, Verkehr oder Struktur werden an einer Stelle evidenzbasiert zusammengeführt.",
    "p.2":
      "Die Darstellungen dienen der Vorbereitung von Planungsaufgaben, der Kommunikation mit Politik, Bürgern oder Entwicklern und Investoren.",
    "img.1.alt":
      "Gemeindescan Schweiz",
    "h2.2": "Beispiele",
    "p.3": "«Als Gemeindepräsident ist es mir wichtig, der Bevölkerung und dem Gemeinderat die Komplexität des Ortsplanungsprozesses und der Standortentwicklung verständlich und einfach zu übermitteln. Mit Hilfe von Daten und Visualisierungen über den Gemeindescan fällt es mir leichter, Lösungen und wichtige Entscheide zu fällen!»",
    "p.4": "Gemeindepräsident Wittenbach",
    "networkerror": "Die Gemeindesuche ist zur Zeit nicht verfügbar."
  },
  "fr": {
    "h1.1": "Découvrez le potentiel en terme d'habitat de votre communauté.",
    "p.1":
      "Le Gemeindescan permet aux autorités locales de se faire une idée des utilisations et des utilisateurs de votre communauté de manière simple et économique. L'utilisation des sols, du trafic ou des structures est rassemblée sur un seul support basé sur des faits.",
    "p.2":
      "Les représentations servent à la préparation des tâches de planification, à la communication avec les politiciens, les citoyens ou les promoteurs et les investisseurs.",
    "img.1.alt":
      "Le Gemeindescan Suisse",
    "h2.2": "Examples",
    "p.3": "«En tant que maire, il est important pour moi de communiquer la complexité du processus de planification locale et du développement urbain à la population et au conseil municipal de manière simple et compréhensible. Avec l'aide des données et des visualisations via les analyses de la communauté, il m'est plus facile de trouver des solutions et de prendre des décisions importantes!»",
    "p.4": "Le maire de la municipalité Wittenbach",
    "networkerror": "La recherche de communauté n'est pas disponible actuellement."
  }
}
</i18n>
<!-- eslint-enable -->

<template>
<div>
  <v-container my-12 >
      <!-- <div class="gmdscn">
          <img :alt="$t('img.1.alt')" class="" width="100%"
            src="@/assets/images/gmdscn-ch-map.svg"/>
          <search :autofocus=true />
      </div> -->
      <v-row justify="center" >
        <v-col class="introtxt text-center pt-12">

          <a href="https://hack.opendata.ch/event/35#top" target="_blank">
            <v-img
              src="https://bucketeer-036aa605-c047-4623-8610-f1764b90cf98.s3.amazonaws.com/public/L7KGJ1NROQP4M3UNH5183L99.png"
              height=100
              contain=false
              >
            </v-img>
          </a>

          <h1>Shape My City Luzern Sandbox</h1>

          <p>
            Willkommen bei der öffentliche Sandbox für den<br>
            OpenData Hackathon <a href="https://opendata.ch/projects/hslu_shape-my-city-2020/"
            target="_blank">Shape My City Luzern</a>.
            </p>
            <p>
            <small>
            Diese Sandbox steht allen Teilnehmern zur freien Verfügung, um<br>kartenbasierte
            Analysen zu publizieren.<br>Die API ist auf <a href="https://sandbox.gemeindescan.ch/graphql" target="_blank">
            sandbox.gemeindescan.ch/graphql</a> erreichbar.</small>
          <p>
            Sandbox Login<br>
            Benutzername: luzern, Passwort: shapemycity
          </p>

           <v-btn
            color="primary"
            elevation="2"
            large
            target="_blank"
            href="https://hackmd.io/@n0rdlicht/Bk9gEqdYP"
          >Anleitung</v-btn>

          <p>
            <small>
              <a href="https://sandbox.gemeindescan.ch/de/RHAX8/QYRB6S/" target="_blank">Direktlink Sandbox (kein Upload)</a>
            </small>
          </p>

          <br>
          <br>

          <v-btn
            color="primary"
            elevation="2"
            large
            target="_blank"
            href="https://sandbox.gemeindescan.ch/BTJHR3/"
          >Beispielanalysen Lenzburg</v-btn>

          <p>
            <small>
              <a target="_blank" href="https://github.com/cividi/scl-lenzburg">Lenzburg Daten auf GitHub</a>
            </small>
          </p>
          <!-- <h1>{{ $t('h1.1') }}</h1>
          <p>{{ $t('p.1') }}</p>
          <p>{{ $t('p.2') }}</p> -->
        </v-col>
      </v-row>
  </v-container>

  <v-container v-if="!networkError" class="center" fluid mb-12>
      <v-row justify="center" >
        <v-col class="introtxt text-center">
          <h2>{{ $t('h2.2') }}</h2>
        </v-col>
      </v-row>

      <v-row justify="center">
        <v-col cols="sm" sm="12" md="4" lg="3"
        v-for="snapshot in snapshotsExamples" :key="snapshot.id">
          <div>

          <v-btn icon :to="'/' + $i18n.locale +'/'+ snapshot.pk + '/'" height="300">
            <v-hover v-slot:default="{ hover }">
              <v-avatar tile size="300">
                <v-img :src="djangobaseurl + '/media/' + snapshot.thumbnail"></v-img>
                <v-fade-transition>
                  <v-overlay v-if="hover" color="primary" opacity="0.6" absolute
                    style="text-transform: none; white-space: normal; hyphens: auto;">
                    <h5 style="font-weight: bold; line-height: 1.2em; padding:0.3em;">
                      {{snapshot.title}}
                    </h5>
                    <span style="">{{snapshot.topic}}<br>-<br>{{snapshot.municipality.name}}</span>
                  </v-overlay>
                </v-fade-transition>
              </v-avatar>
            </v-hover>
          </v-btn>
          </div>
        </v-col>
      </v-row>
  </v-container>

  <v-snackbar color="primary" v-model="snackbar" :timeout="9000">
    {{ $t('networkerror') }}
    <v-btn icon @click="snackbar=false" >
      <v-icon>mdi-close-circle-outline</v-icon>
    </v-btn>
  </v-snackbar>
</div>

</template>

<style>
.gmdscn {
  position: relative;
  max-width: 720px;
  margin: 0 auto;
}

.gmdscn .gemeindesuche.v-select {
  position: absolute;
  top: calc(50% - 30px);
  left: 50%;
  transform: translateX(-50%);
}

.introtxt {
  max-width: 660px;
}

.quotetxt {
  font-style: italic;
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
      snackbar: false
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
    await this.getSnapshotsExamples();
  },
  methods: {
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
