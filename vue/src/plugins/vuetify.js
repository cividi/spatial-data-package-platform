import Vue from 'vue';
import Vuetify from 'vuetify/lib';
import de from 'vuetify/es5/locale/de';

Vue.use(Vuetify);

export default new Vuetify({
  lang: {
    locales: { de },
    current: 'de'
  },
  theme: {
    themes: {
      light: {
        primary: '#543076',
        secondary: '#61BEBF'
        // accent: '#8c9eff',
        // error: '#b71c1c'
      }
    }
  }
});
