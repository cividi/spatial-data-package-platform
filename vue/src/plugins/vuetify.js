import Vue from 'vue';
// import VueI18n from 'vue-i18n';
import Vuetify from 'vuetify/lib';

Vue.use(Vuetify);

// const messages = {
//   en: {
//     $vuetify: {
//     }
//   },
//   de: {
//     $vuetify: {
//     }
//   },
//   fr: {
//     $vuetify: {
//     }
//   }
// };

// Create VueI18n instance with options
// const i18n = new VueI18n({
//   locale: 'de',
//   messages
// });

export default new Vuetify({
  // lang: {
  //   t: (key, ...params) => i18n.t(key, params)
  // },
  theme: {
    themes: {
      light: {
        primary: '#000000',
        secondary: '#61BEBF'
        // accent: '#8c9eff',
        // error: '#b71c1c'
      }
    }
  }
});
