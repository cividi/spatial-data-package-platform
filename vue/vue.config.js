const fs = require('fs');

process.env.VUE_APP_GIT_VERSION = 'NaN.NaN.NaN\tNaN';

try {
  if (fs.existsSync('VERSION')) {
    process.env.VUE_APP_GIT_VERSION = fs.readFileSync('VERSION', 'utf8');
  }
} catch (err) {
  //pass
}


module.exports = {
  devServer: {
    compress: true,
    inline: true,
    port: '8080',
    public: 'www',
    //https: true,
    allowedHosts: [
      'www',
      'www.local',
      'localhost',
      'vue'
    ]
  },
  transpileDependencies: [
    'vuetify'
  ],

  runtimeCompiler: true,

  chainWebpack: (config) => {
    config.module
      .rule('i18n')
      .resourceQuery(/blockType=i18n/)
      .type('javascript/auto')
      .use('i18n')
      .loader('@intlify/vue-i18n-loader');
  },

  pluginOptions: {
    prerenderSpa: {
      registry: undefined,
      renderRoutes: [
        '/de/',
        '/fr/',
        '/de/login/',
        '/de/signup/',
        '/de/about/',
        '/de/imprint/',
        '/de/contact/',
        '/fr/login/',
        '/fr/signup/',
        '/fr/about/',
        '/fr/imprint/',
        '/fr/contact/'
      ],
      useRenderEvent: true,
      headless: true,
      onlyProduction: true,
      customRendererConfig: {
        executablePath: '/usr/bin/chromium-browser',
        args: [
          '--no-sandbox',
          '--disable-dev-shm-usage'
        ]
      }
    }
  }
};
