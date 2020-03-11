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
    "h2.2": "Fallbeispiele",
    "p.3": "«Als Gemeindepräsident ist es mir wichtig, der Bevölkerung und dem Gemeinderat die Komplexität des Ortsplanungsprozesses und der Standortentwicklung verständlich und einfach zu übermitteln. Mit Hilfe von Daten und Visualisierungen über den Gemeindescan fällt es mir leichter, Lösungen und wichtige Entscheide zu fällen!»",
    "p.4": "Gemeindepräsident Wittenbach"
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
    "p.4": "Le maire de la municipalité Wittenbach"
  }
}
</i18n>
<!-- eslint-enable -->

<template>
<div>
  <!-- eslint-disable max-len -->
  <v-container my-12 >
      <div class="gmdscn">
          <img :alt="$t('img.1.alt')" class="" width="100%"
            src="@/assets/images/gmdscn-ch-map.svg"/>
          <search :autofocus=true />
      </div>
      <v-row justify="center" >
        <v-col class="introtxt text-center py-12">
          <h1>{{ $t('h1.1') }}</h1>
          <p>{{ $t('p.1') }}</p>
          <p>{{ $t('p.2') }}</p>
        </v-col>
      </v-row>


  </v-container>

  <v-container class="center" fluid>
      <v-row justify="center" >
        <v-col class="introtxt text-center py-12">
          <h2>{{ $t('h2.2') }}</h2>
        </v-col>
      </v-row>
      <v-row justify="center">
        <v-col cols="sm" sm="12" md="4" lg="3" >
          <div>
          <v-btn icon href="https://stage.gemeindescan.ch/de/667E75" height="300">
         <v-hover v-slot:default="{ hover }">
          <v-avatar tile size="300">
            <img src="https://cdn.vuetifyjs.com/images/cards/kitchen.png" alt="John">
            <v-fade-transition>
              <v-overlay v-if="hover" absolute style="z-index: 0">
               <span>Dietikon: Ausnützungsreserven and more things</span>
              </v-overlay>
            </v-fade-transition>
          </v-avatar>
          </v-hover>
          </v-btn>
          </div>
        </v-col>

        <v-col cols="sm" sm="12" md="4" lg="3">
          <v-btn icon href="https://stage.gemeindescan.ch/de/667E75" height="300">
         <v-hover v-slot:default="{ hover }">
          <v-avatar tile size="300">
            <img src="https://cdn.vuetifyjs.com/images/cards/kitchen.png" alt="John">
            <v-fade-transition>
              <v-overlay v-if="hover" absolute style="z-index: 0">
               <span>Use Case 1 Description</span>
              </v-overlay>
            </v-fade-transition>
          </v-avatar>
          </v-hover>
          </v-btn>
        </v-col>

        <v-col cols="sm" sm="12" md="4" lg="3">
          <v-btn icon href="https://stage.gemeindescan.ch/de/667E75" height="300">
         <v-hover v-slot:default="{ hover }">
          <v-avatar tile size="300">
            <img src="https://cdn.vuetifyjs.com/images/cards/kitchen.png" alt="John">
            <v-fade-transition>
              <v-overlay v-if="hover" absolute style="z-index: 0">
               <span>Use Case 1 Description</span>
              </v-overlay>
            </v-fade-transition>
          </v-avatar>
          </v-hover>
          </v-btn>
        </v-col>
      </v-row>

  </v-container>

  <v-container class="" justify-center my-12>
        <v-row justify="center">
        <v-col class="introtxt text-center py-12">
        <p class="quotetxt">{{ $t('p.3') }}</p>
        <br>
        <p >Oliver Gröble<br>{{ $t('p.4') }}</p>

        </v-col>
      </v-row>
  </v-container>


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
export default {
  name: 'Home',
  data() {
    return {};
  },

  created() {
    this.$store.commit('setBfsnumber', '');
    this.$store.commit('setBfsname', '');
  }
};
</script>
