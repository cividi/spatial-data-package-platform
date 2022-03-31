<template>
  <v-container my-6 class="content">
      <v-layout
        wrap
      >
        <v-flex>
          <h1>
            Impressum
          </h1>
          <p>
            cividi GmbH<br>
            Flüelastrasse 10<br>
            8048 Zürich<br>
            <a href="mailto:legal@cividi.ch" target="_blank">legal@cividi.ch</a>
          </p>

          <h2>
            Datenschutzerklärung
          </h2>
          <p>
            parti.dfour.io (nachfolgend Plattform) und
            ihr Inhalt wird durch cividi GmbH gestellt. Der Schutz Ihrer persönlichen
            Daten ist uns wichtig und wir behandeln personenbezogenen Daten vertraulich
            und entsprechend der gesetzlichen Datenschutzvorschriften sowie dieser
            Datenschutzerklärung. Die Plattform verlangt von den Besuchern generell keine
            Angabe persönlicher Daten. Personenbezogene Daten wie E-Mail-Adressen werden als
            Teil des Beteiligungprozesses lediglich zur Vorbeugung von Missbrauch bis
            Abschluss des Prozesses benötigt und werden nicht veröffentlicht oder an Dritte,
            die nicht in dieser Datenschutzerklärung genannt werden weitergegeben. Die
            erhobenen E-Mail Adressen werden nach Abschluss der öffentlichen Beteiligung
            gelöscht. Bei Nutzung und besonders Einreichung eines Kommentars wird diese
            Datenschutzerklärung anerkannt.
          </p>
          <p>
            Bei der Nutzung unserer Webseite und Beteiligungsplattform werden automatisch
            Informationen allgemeiner Natur erfasst. Diese Informationen werden im
            Server-Logfile erfasst und beinhalten die Art des Webbrowsers, das verwendete
            Betriebssystem, den Domainnamen Ihres Internet-Service-Providers, Ihre IP-Adresse
            und ähnliches. Ihre Daten werden dabei jedoch nicht verwendet, um Rückschlüsse
            auf Ihre Person zu ziehen. Informationen dieser Art werden lediglich statistisch
            ausgewertet, um unseren Web-Auftritt analysieren und optimieren zu können. Die Daten
            werden gelöscht, sobald diese für den Zweck der Erhebung nicht mehr erforderlich
            sind. Dies ist für die Daten, die der Bereitstellung der Webseite dienen,
            grundsätzlich der Fall, wenn die jeweilige Sitzung beendet ist.
          </p>
          <h3>
            Server- und Datenmanagement
          </h3>
          <p>
            Die Plattform greift auf Produkte und Dienstleistungen von Drittanbietern zurück,
            was der Nutzer mit seinem Besuch und seiner Teilnahme anerkennt. Zur Nutzung der
            Platfform werden nicht technisch notwendigen Cookies (z.B. zum Schutz vor Cross Site
            Request Forgery Angriffen) eingesetzt. Mehr Information über die aktuell angewandte
            Datenschutzkonzepte der verwendeten Anbieter finden Sie unter:
          </p>
          <ul>
            <li>Analytics: <a href="https://usefathom.com/privacy">
              usefathom.com/privacy</a></li>
            <li>Hosting (Standort: Frankfurt):
              <a href="https://www.linode.com/legal-privacy/">
                linode.com/legal-privacy/</a></li>
            <li>Daten (Standort: Frankfurt):
              <a href="https://www.elephantsql.com/legal/privacy_policy.html">
                elephantsql.com/legal/privacy_policy.html</a></li>
            <li>Logs:
              <a href="https://www.datadoghq.com/legal/privacy/">
                datadoghq.com/legal/privacy/</a></li>
            <li>Email Versand:
              <a href="https://www.mailgun.com/privacy-policy/">
                mailgun.com/privacy-policy/</a></li>
          </ul>
          <p></p>
          <h3>
            TLS-Verschlüsselung
          </h3>
          <p>
            Um die Sicherheit der Daten bei der Übertragung zu schützen,
            verwenden wir dem aktuellen Stand der Technik entsprechende Verschlüsselungsverfahren
            (z.B. TLS) über HTTPS.
          </p>

          <h3>
            Sonstiges
          </h3>
          <p>
            Wir können diese Datenschutzerklärung jederzeit ohne Vorankündigung anpassen.
            Es gilt die jeweils aktuelle, auf dieser Website publizierte Fassung.
          </p>
          <p>
            Für datenschutzrelevante Anliegen:<br>
            Viktoria Molnar<br>
            Flüelastrasse 10<br>
            8048 Zürich<br>
            <a href="mailto:legal@cividi.ch">legal@cividi.ch</a>
          </p>
          <p>
            Zürich, 31.03.2022
          </p>
          <h2>Lizenz</h2>
          <p>
            Mehr über die Lizenz und die Lizenzen der verwendeten Softwarepakete
            finden Sie auf
            <router-link
              :to="'/' + $i18n.locale + '/notices/'">dieser Seite</router-link>.
          </p>
        </v-flex>
    </v-layout>
  </v-container>
</template>
