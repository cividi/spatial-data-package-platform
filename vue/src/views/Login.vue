<template>
  <v-container my-6>
      <v-layout
        wrap
      >
        <v-flex>
          <v-dialog v-model="noUserDialog" persistent max-width="290">
            <v-card>
              <v-card-title class="headline red--text">Error</v-card-title>
              <v-card-text>
                Der User existiert nicht.<br>
                Bitte einen gültigen User eingeben.
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
                  label="E-Mail Adresse"
                  v-model="email"
                  required
                  :rules="emailRules"
                />
                <v-text-field
                  outlined
                  v-model="password"
                  label="Passwort"
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
                Anmelden
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
        v => !!v || 'Bitte ein Passwort eingeben'
      ],
      email: '',
      emailRules: [
        v => !!v || 'Bitte eine E-Mail eingeben',
        v => /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(v) || 'Bitte eine gültige E-Mail eingeben'
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
