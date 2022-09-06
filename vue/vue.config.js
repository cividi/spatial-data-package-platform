const { execSync } = require('child_process');
const fs = require('fs');

const gitCommand = 'git rev-parse --short HEAD';

process.env.VUE_APP_GIT_VERSION = 'NaN.NaN.NaN\tNaN';

try {
  process.env.VUE_APP_GIT_VERSION = `${fs.readFileSync('VERSION', 'utf8')}\t${execSync(gitCommand).toString().trim()}`;
} catch (err) {
  // pass
}


module.exports = {
  devServer: {
    compress: true,
    inline: true,
    port: '8080',
    public: 'www',
    // https: true,
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
  }

  // pluginOptions: {
  // prerenderSpa: {
  // registry: undefined,
  // renderRoutes: [
  //   '/de/',
  //   '/fr/',
  //   '/en/',
  //   '/it/'
  // ],
  // useRenderEvent: true,
  // headless: true,
  // onlyProduction: true
  // customRendererConfig: {
  //   executablePath: '/usr/bin/chromium-browser',
  //   args: [
  //     '--no-sandbox',
  //     '--disable-dev-shm-usage'
  //   ]
  // }
  // }
  // }
};
