module.exports = {
  root: true,
  env: {
    node: true
  },
  extends: [
    'plugin:vue/essential',
    '@vue/airbnb'
  ],
  rules: {
    'no-console': process.env.NODE_ENV === 'production' ? 'error' : 'off',
    'no-debugger': process.env.NODE_ENV === 'production' ? 'error' : 'off',
    quotes: [
      'error',
      'single'
    ],
    'comma-dangle': [
      'error',
      'never'
    ],
    'func-names': 'off',
    'no-param-reassign': 'off',
    'no-new': 'off',
    'no-shadow': 'off',
    'prefer-destructuring': 'off',
    'no-prototype-builtins': 'off'
  },
  parserOptions: {
    parser: 'babel-eslint'
  }
};
