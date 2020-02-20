<!-- eslint-disable -->
<i18n>
{
  "de": {
    "h1.1": "Hintergrund",
    "p.1":
      "Der Gemeindescan ermöglicht Gemeindeverwaltungen auf einfache und kosteneffiziente Weise ein Bild von Nutzungen und Nutzern in Ihrer Gemeinde zu erhalten. Flächenverbräuche,Verkehr und strukturelle Indikatoren werden an einer Stelle evidenzbasiert zusammengeführt. Die Darstellungen dienen der Vorbereitung von Planungsaufgaben, der Kommunikation mit Politik, Bürgern oder Entwicklern und Investoren.",
    "p.2":
      "Der Gemeindescan ist eine <a href=\"https://cividi.ch\" target=\"_blank\">cividi</a> Anwendung, die in Zusammenarbeit mit <a href=\"https://taywa.ch\" target=\"_blank\">Taywa</a> entwickelt wird."
  },
  "fr": {
    "h1.1": "Contexte",
    "p.1":
      "Le Gemeindescan permet aux autorités locales d'obtenir une image des utilisations et des utilisateurs dans leur communauté d'une manière simple et économique. L'utilisation des sols, du trafic et des indicateurs structurels est combinée sur un seul support basé sur des faits. Les représentations servent à la préparation des tâches de planification, à la communication avec les politiciens, les citoyens ou les promoteurs et les investisseurs.",
    "p.2":
      "Le Gemeindescan est une application <a href=\"https://cividi.ch/societe/\" target=\"_blank\">cividi</a> développée en coopération avec <a href=\"https://taywa.ch\" target=\"_blank\">Taywa</a>."
  }
}
</i18n>
<!-- eslint-enable -->

<template>
  <v-container my-6 class="content">
      <v-layout
        wrap
      >
        <v-flex>
          <h1>{{ $t('h1.1') }}</h1>
          <p>{{ $t('p.1') }}</p>
          <p v-html="$t('p.2')"></p>
        </v-flex>
    </v-layout>
  </v-container>
</template>
