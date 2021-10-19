<!-- eslint-disable -->
<i18n>
{
  "de": {
    "h1.1": "Kontakt",
    "p.1":
      "Direkt mit dem dføur-Team in Kontakt treten:<br><a href=\"mailto:support@dfour.space\">support@dfour.space</a><br><a href=\"tel:+41 43 543 44 45\">+41 43 543 44 45</a><br>Flüelastrasse 10<br>8048 Zürich",
    "p.2":
      "Die dføur-Plattform ist Open Source und Open Development. Zum dføur beitragen: <a href=\"https://github.org/cividi/spatial-data-package-platform\" target=\"_blank\">Projekt auf GitHub</a>",
    "p.3":
      "cividi - digitale Werkzeuge für die analoge Stadt.",
    "p.4":
      "<small>Das Pionierprojekt wird ermöglicht durch <a href=\"https://www.engagement-migros.ch/de\" target=\"_blank\">Engagement Migros</a>,<br>dem Förderfonds der Migros-Gruppe.</small>",
    "p.5": 
      "dføur ist eine <a href=\"https://cividi.ch\" target=\"_blank\">cividi</a> Anwendung, die in Zusammenarbeit mit <a href=\"https://taywa.ch\" target=\"_blank\">Taywa</a> entwickelt wird.",
    "cividi.link":
      "https://cividi.ch",
    "em.link":
      "https://www.engagement-migros.ch/de"
  },
  "fr": {
    "h1.1": "Contact",
    "p.1":
      "Prenez contact directement avec l'équipe du dføur.<br><a href=\"mailto:support@dfour.space\">support@dfour.space</a><br><a href=\"tel:+41 43 543 44 45\">+41 43 543 44 45</a><br>Flüelastrasse 10<br>8048 Zürich",
    "p.2":
      "La plate-forme du dføur est un logiciel Open Source & Development. Contribuer au dføur:  <a href=\"https://github.com/cividi/spatial-data-package-platform\" target=\"_blank\">Projet sur GitHub</a>",
    "p.3":
      "cividi - Des outils numériques pour la ville analogique",
    "p.4":
      "<small>Ce projet innovateur est rendu possible grâce à <a href=\"https://www.engagement-migros.ch/fr\" target=\"_blank\">l'engagement de Migros</a>,<br>le fonds de développement du groupe Migros.</small>",
    "p.5":
      "Le dføur est une application <a href=\"https://cividi.ch/societe/\" target=\"_blank\">cividi</a> développée en coopération avec <a href=\"https://taywa.ch\" target=\"_blank\">Taywa</a>.",
    "cividi.link":
      "https://cividi.ch/societe",
    "em.link":
      "https://www.engagement-migros.ch/fr"
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
          <h1>
            {{ $t('h1.1')}}
          </h1>
          <p v-html="$t('p.5')">
          </p>
          <p v-html="$t('p.1')">
          </p>
          <p v-html="$t('p.2')">
          </p>
          <p>
            {{ $t('p.3') }}
          </p>

          <a :href="$t('cividi.link')" target="_blank" style="padding-right:40px">
            <img src="@/assets/images/logo-cividi.svg" width="250px">
          </a>

          <p v-html="$t('p.4')">
          </p>

          <a :href="$t('em.link')" target="_blank">
            <img v-if="$i18n.locale === 'fr'"
              src="@/assets/images/EngagementM_f_rgb.jpg" width="220px">
            <img v-else
              src="@/assets/images/EngagementM_d_rgb.jpg" width="220px">
          </a>

        </v-flex>
    </v-layout>
  </v-container>
</template>
