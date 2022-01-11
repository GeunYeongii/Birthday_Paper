import Vue from 'vue';
import Vuetify from 'vuetify/lib/framework';

Vue.use(Vuetify);

export default new Vuetify({
  theme: {
    themes: {
      light: {
        primary: '#26A3A3',
        secondary: '#474775',
        accent: '#8c9eff',
        error: '#FF7199',
      },
      options: {
        customProperties: true,
      },
    },
  },
});
