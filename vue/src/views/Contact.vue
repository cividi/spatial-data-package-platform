<!-- eslint-disable -->
<i18n>
{
  "de": {
    "h1.1": "Kontakt",
    "p.1":
      "Direkt mit dem Gemeindescan-Team in Kontakt treten:",
    "a.mail":
      "kontakt@gemeindescan.ch",
    "p.2":
      "Die Gemeindescan-Plattform ist Open Source und Open Development. Zum Gemeindescan beitragen: [Projekt auf Bitbucket](https://bitbucket.org/cividi/gemeindescan-webui)",
    "p.3":
      "cividi - digitale Werkzeuge für die analoge Stadt.",
    "p.4.small":
      "Das Pionierprojekt wird ermöglicht durch [Engagement Migros](https://www.engagement-migros.ch/de), dem Förderfonds der Migros-Gruppe.",
    "img.em":
      "@/assets/images/EngagementM_d_rgb.jpg"
  },
  "fr": {
    "h1.1": "Contact",
    "p.1":
      "Prenez contact directement avec l'équipe du Gemeindescan.",
    "a.mail":
      "contact@gemeindescan.ch",
    "p.2":
      "La plate-forme du Gemeindescan est un logiciel Open Source & Development. Contribuer au Gemeindescan:  [Project sur Bitbucket](https://bitbucket.org/cividi/gemeindescan-webui)",
    "p.3":
      "cividi - Des outils numériques pour la ville analogique",
    "p.4.small":
      "Ce projet innovateur est rendu possible grâce à [l'engagement de Migros](https://www.engagement-migros.ch/fr), le fonds de développement du groupe Migros.",
    "img.em":
      "@/assets/images/EngagementM_f_rgb.jpg"
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
          <p>
            {{ $t('p.1') }}
            <br>
            <a href="mailto:kontakt@gemeindescan.ch">{{ $t('a.mail') }}</a><br>
            <a href="tel:+41 43 543 44 45">+41 43 543 44 45</a><br>
            Flüelastrasse 10<br>
            8048 Zürich
          </p>
          <p>
            {{ $t('p.2') }}
          </p>
          <p>
            {{ $t('p.3') }}
          </p>

          <a href="https://www.cividi.ch" target="_blank" style="padding-right:40px">
            <img src="@/assets/images/logo-cividi.svg" width="250px">
          </a>

          <p><small>{{ $t('p.4.small') }}</small>
          </p>

          <a href="https://www.engagement-migros.ch/" target="_blank"><img :src="$t('img.em')" width="220px"></a>

        </v-flex>
    </v-layout>
  </v-container>
</template>
