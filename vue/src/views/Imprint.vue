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
            Diese Webseite und ihr Inhalt wird durch cividi GmbH gestellt.
            Der Schutz Ihrer persönlichen Daten ist uns wichtig und wir behandeln
            personenbezogenen Daten vertraulich und entsprechend der gesetzlichen
            Datenschutzvorschriften sowie dieser Datenschutzerklärung.
            Die Nutzung unserer Webseite verlangt generell keine Angabe persönlicher Daten.
            Personenbezogene Daten wie Namen oder E-Mail-Adressen werden nur auf freiwilliger
            Basis gesammelt, so zum Beispiel bei dem Ausfüllen unserer Formularen oder bei der
            Anmeldung für unseren Newsletter.
            Bei der Nutzung unserer Webseite werden aber automatisch Informationen allgemeiner
            Natur erfasst.
            Diese Informationen werden im Server-Logfile erfasst und beinhalten die Art des
            Webbrowsers, das verwendete Betriebssystem, den Domainnamen Ihres
            Internet-Service-Providers, Ihre IP-Adresse und ähnliches.
            Eure Daten werden dabei jedoch nicht verwendet,
            um Rückschlüsse auf Ihre Person zu ziehen.
            Informationen dieser Art werden lediglich statistisch ausgewertet,
            um unseren Web-Auftritt analysieren und optimieren zu können.
            Die Daten werden gelöscht, sobald diese für den Zweck der Erhebung nicht mehr
            erforderlich sind.
            Dies ist für die Daten, die der Bereitstellung der Webseite dienen,
            grundsätzlich der Fall, wenn die jeweilige Sitzung beendet ist.
          </p>

          <h3>
            Formulare und Newsletterdaten
          </h3>
          <p>
            Wenn Sie unser Formular ausfüllen, werden Ihre Daten sprich
            E-Mail Adresse, Organisation, Ort, Name, Zweck eurem Besuch sowie Zeitpunkt
            der Anmeldung bei Typeform und Mailchimp gespeichert.
            Diese Daten nutzen wir einzig für den von euch angeforderten Newsletter-Versand
            und um Ihre Anfragen direkt beantworten zu können.
            Sie können sich mittels Abmelde-Link im Newsletter jederzeit wieder
            vom Newsletter abmelden.
            Die Newsletter-Anmeldung erfolgt via Double-Opt-In, sprich Sie erhalten nach Ausfüllen
            des Anmeldeformulars zwecks Verifizierung eine Bestätigungs-E-Mail.
            Erst danach werden Sie in die Newsletter-Datenbank übernommen.
          </p>

          <h3>
            MailChimp
          </h3>
          <p>
            Unsere Newsletter werden mit „MailChimp” versendet
            (Newsletterversandplattform von der Rocket Science Group,
            LLC, 675 Ponce De Leon Ave NE, Suite 5000, Atlanta, GA 30308, USA).
            Die gesammelten E-Mail-Adressen werden entsprechend auf den MailChimp-Servern
            gespeichert.
            MailChimp verwendet diese Informationen für von uns ausgelöste Newsletter-Versände
            und -Auswertungen. MailChimp nutzt die Daten für Optimierung des eigenen Services,
            jedoch nicht um Newsletter-Empfänger selber anzuschreiben oder deren Daten
            an Dritte weiterzugeben.
            Die Datenschutzbestimmungen von MailChimp könnt ihr
            <a href="https://mailchimp.com/legal/" target="_blank">hier</a> nachlesen.
          </p>

          <h3>
            Typeform
          </h3>
          <p>
            Unsere Formulare werden mit Typeform (C/ Bac de Roda 163, Local 1, Barcelona,
            Catalunya 08018, ES) entwickelt.
            Diese Daten nutzen wir einzig für die Weiterentwicklung und Personalisierung
            unsere Dienstleistungen und Produkten anhand von den von Ihnen angegeben Daten.
            Die gesammelten E-Mail-Adressen und Antworten werden entsprechend auf den
            Typeform-Servern gespeichert. Typeform verwendet diese Informationen
            für die Sammlung der Antworten in von uns ausgelösten Formulare und ihre
            Auswertungen. Typeform nutzt die Daten für Optimierung des eigenen Services,
            jedoch nicht um Formular-Ausfüller selber anzuschreiben oder deren
            Daten an Dritte weiterzugeben.
            Die Datenschutzbestimmungen von Typeform könnt ihr
            <a href="https://admin.typeform.com/to/L9Crcj" target="_blank">hier</a> nachlesen.
          </p>

          <h3>
            TLS-Verschlüsselung
          </h3>
          <p>
            Um die Sicherheit eurer Daten bei der Übertragung zu schützen,
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
            Für datenschutzrelevante Anliegen könnt ihr euch wenden an:<br>
            Viktoria Molnar<br>
            Flüelastrasse 10<br>
            8048 Zürich<br>
            <a href="mailto:legal@cividi.ch">legal@cividi.ch</a>
          </p>
          <p>
            Zürich, 09.11.2020
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
