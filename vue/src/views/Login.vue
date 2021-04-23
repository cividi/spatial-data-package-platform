<!-- eslint-disable -->
<i18n>
{
  "de": {
    "form.email": "E-Mail Adresse",
    "form.password": "Passwort",
    "form.submit": "Anmelden",
    "error.nonexistent": "Der User existiert nicht.<br>Bitte einen gültigen User eingeben.",
    "error.noemail": "Bitte eine E-Mail eingeben.",
    "error.invalidemail": "Bitte eine gültige E-Mail eingeben.",
    "error.nopassword": "Bitte ein Passwort eingeben."
  },
  "fr": {
    "form.email": "E-Mail",
    "form.password": "Mot de passe",
    "form.submit": "S'inscrire",
    "error.nonexistent": "L'utilisateur n'existe pas.<br>Veuillez entrer un utilisateur valide.",
    "error.noemail": "Veuillez saisir un e-mail.",
    "error.invalidemail": "Veuillez entrer une adresse électronique valide.",
    "error.nopassword": "Veuillez entrer un mot de passe."
  },
  "en": {
    "form.email": "E-Mail",
    "form.password": "Password",
    "form.submit": "Login",
    "error.nonexistent": "This user doesn't exist.<br>Please enter a valid username.",
    "error.noemail": "Please enter an email address.",
    "error.invalidemail": "Please enter a valid email address.",
    "error.nopassword": "Please enter a password."
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
          <v-dialog v-model="noUserDialog" persistent max-width="290">
            <v-card>
              <v-card-title class="headline red--text">Error</v-card-title>
              <v-card-text>
                <span v-html="$t('error.nonexistent')"></span>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn
                  depressed large color="primary"
                  @click="noUserDialog = false">OK
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
          <v-card outlined width="400" class="mx-auto">
            <v-card-title class="headline">
              Login
            </v-card-title>
            <v-card-text>
              <v-form v-model="valid" ref="form">
                <v-text-field
                  outlined
                  :label="$t('form.email')"
                  v-model="email"
                  required
                  :rules="emailRules"
                />
                <v-text-field
                  outlined
                  v-model="password"
                  :label="$t('form.password')"
                  :type="showPassword ? 'text' : 'password'"
                  :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
                  @click:append="showPassword = !showPassword"
                  min="8"
                  :rules="passwordRules"
                  required
                />
              </v-form>
            </v-card-text>
            <v-card-actions class="px-4 pb-4">
              <v-spacer></v-spacer>
              <v-btn
                depressed large color="primary"
                @click="submitLogin">
                {{ $t('form.submit') }}
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      noUserDialog: false,
      valid: false,
      showPassword: false,
      password: '',
      passwordRules: [
        v => !!v || this.$i18n.t('error.nopassword')
      ],
      email: '',
      emailRules: [
        v => !!v || this.$i18n.t('error.noemail'),
        v => /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(v) || this.$i18n.t('error.invalidemail')
      ]
    };
  },

  methods: {
    submitLogin() {
      if (this.$refs.form.validate()) {
        this.noUserDialog = true;
      }
    }
  }
};
</script>
