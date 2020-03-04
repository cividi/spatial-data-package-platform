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
      "Gemeindescan Schweiz"
  },
  "fr": {
    "h1.1": "Découvrez le potentiel en terme d'habitat de votre communauté.",
    "p.1":
      "Le Gemeindescan permet aux autorités locales de se faire une idée des utilisations et des utilisateurs de votre communauté de manière simple et économique. L'utilisation des sols, du trafic ou des structures est rassemblée sur un seul support basé sur des faits.",
    "p.2":
      "Les représentations servent à la préparation des tâches de planification, à la communication avec les politiciens, les citoyens ou les promoteurs et les investisseurs.",
    "img.1.alt":
      "Le Gemeindescan Suisse"
  }
}
</i18n>
<!-- eslint-enable -->

<template>
  <!-- eslint-disable max-len -->
  <v-container my-12>
      <div class="gmdscn">
          <img :alt="$t('img.1.alt')" class="" width="100%"
            src="@/assets/images/gmdscn-ch-map.svg"/>
          <search/>
      </div>
      <v-row justify="center">
        <v-col class="introtxt text-center py-12">
          <h1>{{ $t('h1.1') }}</h1>
          <p>{{ $t('p.1') }}</p>
          <p>{{ $t('p.2') }}</p>
        </v-col>
      </v-row>
  </v-container>
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
</style>

<script>
export default {
  name: 'Home',
  data() {
    return {};
  }
};
</script>
