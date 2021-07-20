<!-- eslint-disable -->
<i18n>
{
  "de": {
    "title": "Verwendete Pakete und deren Lizenzen",
    "pythontitle": "Python Pakete",
    "jstitle": "JavaScript Pakete"
  },
  "fr": {
    "title": "Paquets utilisés et leurs licences",
    "pythontitle": "Paquets Python",
    "jstitle": "Paquets JavaScript"
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
          <h1>{{ $t('title') }}</h1>
          <h3>{{ $t('pythontitle') }}</h3>
          <table>
          <thead>
          <tr>
          <th>Name</th>
          <th>Version</th>
          <th>License</th>
          </tr>
          </thead>
          <tbody>
          <tr>
          <td>Rx</td>
          <td>1.6.1</td>
          <td>Apache Software License</td>
          </tr>
          <tr>
          <td>requests</td>
          <td>2.25.1</td>
          <td>Apache Software License</td>
          </tr>
          <tr>
          <td>yapf</td>
          <td>0.30.0</td>
          <td>Apache Software License</td>
          </tr>
          <tr>
          <td>packaging</td>
          <td>20.9</td>
          <td>Apache Software License; BSD License</td>
          </tr>
          <tr>
          <td>uvloop</td>
          <td>0.14.0</td>
          <td>Apache Software License; MIT License</td>
          </tr>
          <tr>
          <td>text-unidecode</td>
          <td>1.3</td>
          <td>
            Artistic License; GNU General Public License (GPL);
            GNU General Public License v2 or later (GPLv2+)
          </td>
          </tr>
          <tr>
          <td>Django</td>
          <td>3.1.12</td>
          <td>BSD License</td>
          </tr>
          <tr>
          <td>PTable</td>
          <td>0.9.2</td>
          <td>BSD License</td>
          </tr>
          <tr>
          <td>Pygments</td>
          <td>2.7.4</td>
          <td>BSD License</td>
          </tr>
          <tr>
          <td>aniso8601</td>
          <td>7.0.0</td>
          <td>BSD License</td>
          </tr>
          <tr>
          <td>asgiref</td>
          <td>3.4.1</td>
          <td>BSD License</td>
          </tr>
          <tr>
          <td>click</td>
          <td>8.0.1</td>
          <td>BSD License</td>
          </tr>
          <tr>
          <td>django-filter</td>
          <td>2.4.0</td>
          <td>BSD License</td>
          </tr>
          <tr>
          <td>django-json-widget</td>
          <td>1.1.1</td>
          <td>BSD License</td>
          </tr>
          <tr>
          <td>django-sortedm2m</td>
          <td>3.0.2</td>
          <td>BSD License</td>
          </tr>
          <tr>
          <td>django-sortedm2m-filter-horizontal-widget</td>
          <td>1.3.2</td>
          <td>BSD License</td>
          </tr>
          <tr>
          <td>djangorestframework</td>
          <td>3.12.2</td>
          <td>BSD License</td>
          </tr>
          <tr>
          <td>idna</td>
          <td>2.10</td>
          <td>BSD License</td>
          </tr>
          <tr>
          <td>lazy-object-proxy</td>
          <td>1.4.3</td>
          <td>BSD License</td>
          </tr>
          <tr>
          <td>olefile</td>
          <td>0.46</td>
          <td>BSD License</td>
          </tr>
          <tr>
          <td>pytest-django</td>
          <td>4.1.0</td>
          <td>BSD License</td>
          </tr>
          <tr>
          <td>sorl-thumbnail</td>
          <td>12.7.0</td>
          <td>BSD License</td>
          </tr>
          <tr>
          <td>sqlparse</td>
          <td>0.4.1</td>
          <td>BSD License</td>
          </tr>
          <tr>
          <td>uvicorn</td>
          <td>0.14.0</td>
          <td>BSD License</td>
          </tr>
          <tr>
          <td>websockets</td>
          <td>9.1</td>
          <td>BSD License</td>
          </tr>
          <tr>
          <td>wrapt</td>
          <td>1.12.1</td>
          <td>BSD License</td>
          </tr>
          <tr>
          <td>django-solo</td>
          <td>1.1.5</td>
          <td>Creative Commons Attribution 3.0 Unported</td>
          </tr>
          <tr>
          <td>pylint</td>
          <td>2.6.0</td>
          <td>GNU General Public License (GPL)</td>
          </tr>
          <tr>
          <td>astroid</td>
          <td>2.6.2</td>
          <td>GNU Lesser General Public License v2 (LGPLv2)</td>
          </tr>
          <tr>
          <td>chardet</td>
          <td>4.0.0</td>
          <td>GNU Library or Lesser General Public License (LGPL)</td>
          </tr>
          <tr>
          <td>psycopg2</td>
          <td>2.8.6</td>
          <td>GNU Library or Lesser General Public License (LGPL)</td>
          </tr>
          <tr>
          <td>pylint-django</td>
          <td>2.3.0</td>
          <td>GPLv2</td>
          </tr>
          <tr>
          <td>pylint-plugin-utils</td>
          <td>0.6</td>
          <td>GPLv2</td>
          </tr>
          <tr>
          <td>Pillow</td>
          <td>8.3.1</td>
          <td>Historical Permission Notice and Disclaimer (HPND)</td>
          </tr>
          <tr>
          <td>graphene</td>
          <td>2.1.8</td>
          <td>MIT</td>
          </tr>
          <tr>
          <td>graphene-django</td>
          <td>2.14.0</td>
          <td>MIT</td>
          </tr>
          <tr>
          <td>APScheduler</td>
          <td>3.6.3</td>
          <td>MIT License</td>
          </tr>
          <tr>
          <td>appdirs</td>
          <td>1.4.4</td>
          <td>MIT License</td>
          </tr>
          <tr>
          <td>attrs</td>
          <td>20.3.0</td>
          <td>MIT License</td>
          </tr>
          <tr>
          <td>beautifulsoup4</td>
          <td>4.9.3</td>
          <td>MIT License</td>
          </tr>
          <tr>
          <td>blessings</td>
          <td>1.7</td>
          <td>MIT License</td>
          </tr>
          <tr>
          <td>curtsies</td>
          <td>0.3.4</td>
          <td>MIT License</td>
          </tr>
          <tr>
          <td>django-apscheduler</td>
          <td>0.5.1</td>
          <td>MIT License</td>
          </tr>
          <tr>
          <td>django-cors-headers</td>
          <td>3.7.0</td>
          <td>MIT License</td>
          </tr>
          <tr>
          <td>future</td>
          <td>0.18.2</td>
          <td>MIT License</td>
          </tr>
          <tr>
          <td>graphql-core</td>
          <td>2.3.2</td>
          <td>MIT License</td>
          </tr>
          <tr>
          <td>graphql-relay</td>
          <td>2.0.1</td>
          <td>MIT License</td>
          </tr>
          <tr>
          <td>greenlet</td>
          <td>0.4.17</td>
          <td>MIT License</td>
          </tr>
          <tr>
          <td>gunicorn</td>
          <td>20.1.0</td>
          <td>MIT License</td>
          </tr>
          <tr>
          <td>h11</td>
          <td>0.12.0</td>
          <td>MIT License</td>
          </tr>
          <tr>
          <td>httptools</td>
          <td>0.1.1</td>
          <td>MIT License</td>
          </tr>
          <tr>
          <td>iniconfig</td>
          <td>1.1.1</td>
          <td>MIT License</td>
          </tr>
          <tr>
          <td>isort</td>
          <td>5.6.4</td>
          <td>MIT License</td>
          </tr>
          <tr>
          <td>jsonslicer</td>
          <td>0.1.6</td>
          <td>MIT License</td>
          </tr>
          <tr>
          <td>mccabe</td>
          <td>0.6.1</td>
          <td>MIT License</td>
          </tr>
          <tr>
          <td>more-itertools</td>
          <td>8.6.0</td>
          <td>MIT License</td>
          </tr>
          <tr>
          <td>ordered-set</td>
          <td>4.0.1</td>
          <td>MIT License</td>
          </tr>
          <tr>
          <td>pip</td>
          <td>21.1.3</td>
          <td>MIT License</td>
          </tr>
          <tr>
          <td>pip-licenses</td>
          <td>3.5.1</td>
          <td>MIT License</td>
          </tr>
          <tr>
          <td>pluggy</td>
          <td>0.13.1</td>
          <td>MIT License</td>
          </tr>
          <tr>
          <td>promise</td>
          <td>2.3</td>
          <td>MIT License</td>
          </tr>
          <tr>
          <td>py</td>
          <td>1.10.0</td>
          <td>MIT License</td>
          </tr>
          <tr>
          <td>pyparsing</td>
          <td>2.4.7</td>
          <td>MIT License</td>
          </tr>
          <tr>
          <td>pytest</td>
          <td>6.2.1</td>
          <td>MIT License</td>
          </tr>
          <tr>
          <td>pytz</td>
          <td>2021.1</td>
          <td>MIT License</td>
          </tr>
          <tr>
          <td>setuptools</td>
          <td>51.3.3</td>
          <td>MIT License</td>
          </tr>
          <tr>
          <td>singledispatch</td>
          <td>3.6.2</td>
          <td>MIT License</td>
          </tr>
          <tr>
          <td>six</td>
          <td>1.15.0</td>
          <td>MIT License</td>
          </tr>
          <tr>
          <td>soupsieve</td>
          <td>2.2.1</td>
          <td>MIT License</td>
          </tr>
          <tr>
          <td>toml</td>
          <td>0.10.2</td>
          <td>MIT License</td>
          </tr>
          <tr>
          <td>tzlocal</td>
          <td>2.1</td>
          <td>MIT License</td>
          </tr>
          <tr>
          <td>urllib3</td>
          <td>1.26.5</td>
          <td>MIT License</td>
          </tr>
          <tr>
          <td>wcwidth</td>
          <td>0.2.5</td>
          <td>MIT License</td>
          </tr>
          <tr>
          <td>wheel</td>
          <td>0.36.2</td>
          <td>MIT License</td>
          </tr>
          <tr>
          <td>bpython</td>
          <td>0.20.1</td>
          <td>MIT/X</td>
          </tr>
          <tr>
          <td>certifi</td>
          <td>2021.5.30</td>
          <td>Mozilla Public License 2.0 (MPL 2.0)</td>
          </tr>
          </tbody>
          </table>
          <p><br><br><br></p>
          <h3>{{ $t('jstitle') }}</h3>
          <table>
          <thead>
          <tr>
          <th>Name</th>
          <th>Version</th>
          <th>License</th>
          <th>URL</th>
          <th>VendorUrl</th>
          <th>VendorName</th>
          </tr>
          </thead>
          <tbody>
          <tr>
          <td>@babel/code-frame</td>
          <td>7.12.13</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-code-frame">https://babel.dev/docs/en/next/babel-code-frame</a></td>
          <td>Sebastian McKenzie</td>
          </tr>
          <tr>
          <td>@babel/compat-data</td>
          <td>7.13.8</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/team">https://babel.dev/team</a></td>
          <td>The Babel Team</td>
          </tr>
          <tr>
          <td>@babel/core</td>
          <td>7.13.8</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-core">https://babel.dev/docs/en/next/babel-core</a></td>
          <td>Sebastian McKenzie</td>
          </tr>
          <tr>
          <td>@babel/generator</td>
          <td>7.13.9</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-generator">https://babel.dev/docs/en/next/babel-generator</a></td>
          <td>Sebastian McKenzie</td>
          </tr>
          <tr>
          <td>@babel/helper-annotate-as-pure</td>
          <td>7.12.13</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-helper-annotate-as-pure">https://babel.dev/docs/en/next/babel-helper-annotate-as-pure</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@babel/helper-builder-binary-assignment-operator-visitor</td>
          <td>7.12.13</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-helper-builder-binary-assignment-operator-visitor">https://babel.dev/docs/en/next/babel-helper-builder-binary-assignment-operator-visitor</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@babel/helper-compilation-targets</td>
          <td>7.13.8</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/team">https://babel.dev/team</a></td>
          <td>The Babel Team</td>
          </tr>
          <tr>
          <td>@babel/helper-create-class-features-plugin</td>
          <td>7.13.8</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/team">https://babel.dev/team</a></td>
          <td>The Babel Team</td>
          </tr>
          <tr>
          <td>@babel/helper-create-regexp-features-plugin</td>
          <td>7.12.17</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/team">https://babel.dev/team</a></td>
          <td>The Babel Team</td>
          </tr>
          <tr>
          <td>@babel/helper-define-polyfill-provider</td>
          <td>0.1.5</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel-polyfills.git">https://github.com/babel/babel-polyfills.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@babel/helper-explode-assignable-expression</td>
          <td>7.13.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-helper-explode-assignable-expression">https://babel.dev/docs/en/next/babel-helper-explode-assignable-expression</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@babel/helper-function-name</td>
          <td>7.12.13</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-helper-function-name">https://babel.dev/docs/en/next/babel-helper-function-name</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@babel/helper-get-function-arity</td>
          <td>7.12.13</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-helper-get-function-arity">https://babel.dev/docs/en/next/babel-helper-get-function-arity</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@babel/helper-hoist-variables</td>
          <td>7.13.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-helper-hoist-variables">https://babel.dev/docs/en/next/babel-helper-hoist-variables</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@babel/helper-member-expression-to-functions</td>
          <td>7.13.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-helper-member-expression-to-functions">https://babel.dev/docs/en/next/babel-helper-member-expression-to-functions</a></td>
          <td>Justin Ridgewell</td>
          </tr>
          <tr>
          <td>@babel/helper-module-imports</td>
          <td>7.12.13</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-helper-module-imports">https://babel.dev/docs/en/next/babel-helper-module-imports</a></td>
          <td>Logan Smyth</td>
          </tr>
          <tr>
          <td>@babel/helper-module-transforms</td>
          <td>7.13.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-helper-module-transforms">https://babel.dev/docs/en/next/babel-helper-module-transforms</a></td>
          <td>Logan Smyth</td>
          </tr>
          <tr>
          <td>@babel/helper-optimise-call-expression</td>
          <td>7.12.13</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-helper-optimise-call-expression">https://babel.dev/docs/en/next/babel-helper-optimise-call-expression</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@babel/helper-plugin-utils</td>
          <td>7.13.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-helper-plugin-utils">https://babel.dev/docs/en/next/babel-helper-plugin-utils</a></td>
          <td>Logan Smyth</td>
          </tr>
          <tr>
          <td>@babel/helper-remap-async-to-generator</td>
          <td>7.13.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-helper-remap-async-to-generator">https://babel.dev/docs/en/next/babel-helper-remap-async-to-generator</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@babel/helper-replace-supers</td>
          <td>7.13.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-helper-replace-supers">https://babel.dev/docs/en/next/babel-helper-replace-supers</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@babel/helper-simple-access</td>
          <td>7.12.13</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-helper-simple-access">https://babel.dev/docs/en/next/babel-helper-simple-access</a></td>
          <td>Logan Smyth</td>
          </tr>
          <tr>
          <td>@babel/helper-skip-transparent-expression-wrappers</td>
          <td>7.12.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@babel/helper-split-export-declaration</td>
          <td>7.12.13</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-helper-split-export-declaration">https://babel.dev/docs/en/next/babel-helper-split-export-declaration</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@babel/helper-validator-identifier</td>
          <td>7.12.11</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@babel/helper-validator-option</td>
          <td>7.12.17</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@babel/helper-wrap-function</td>
          <td>7.13.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-helper-wrap-function">https://babel.dev/docs/en/next/babel-helper-wrap-function</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@babel/helpers</td>
          <td>7.13.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-helpers">https://babel.dev/docs/en/next/babel-helpers</a></td>
          <td>Sebastian McKenzie</td>
          </tr>
          <tr>
          <td>@babel/highlight</td>
          <td>7.13.8</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-highlight">https://babel.dev/docs/en/next/babel-highlight</a></td>
          <td>suchipi</td>
          </tr>
          <tr>
          <td>@babel/parser</td>
          <td>7.13.9</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-parser">https://babel.dev/docs/en/next/babel-parser</a></td>
          <td>Sebastian McKenzie</td>
          </tr>
          <tr>
          <td>@babel/plugin-proposal-async-generator-functions</td>
          <td>7.13.8</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-plugin-proposal-async-generator-functions">https://babel.dev/docs/en/next/babel-plugin-proposal-async-generator-functions</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@babel/plugin-proposal-class-properties</td>
          <td>7.13.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-plugin-proposal-class-properties">https://babel.dev/docs/en/next/babel-plugin-proposal-class-properties</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@babel/plugin-proposal-decorators</td>
          <td>7.13.5</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-plugin-proposal-decorators">https://babel.dev/docs/en/next/babel-plugin-proposal-decorators</a></td>
          <td>Logan Smyth</td>
          </tr>
          <tr>
          <td>@babel/plugin-proposal-dynamic-import</td>
          <td>7.13.8</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@babel/plugin-proposal-export-namespace-from</td>
          <td>7.12.13</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-plugin-proposal-export-namespace-from">https://babel.dev/docs/en/next/babel-plugin-proposal-export-namespace-from</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@babel/plugin-proposal-json-strings</td>
          <td>7.13.8</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-plugin-proposal-json-strings">https://babel.dev/docs/en/next/babel-plugin-proposal-json-strings</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@babel/plugin-proposal-logical-assignment-operators</td>
          <td>7.13.8</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-plugin-proposal-logical-assignment-operators">https://babel.dev/docs/en/next/babel-plugin-proposal-logical-assignment-operators</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@babel/plugin-proposal-nullish-coalescing-operator</td>
          <td>7.13.8</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-plugin-proposal-nullish-coalescing-operator">https://babel.dev/docs/en/next/babel-plugin-proposal-nullish-coalescing-operator</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@babel/plugin-proposal-numeric-separator</td>
          <td>7.12.13</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-plugin-proposal-numeric-separator">https://babel.dev/docs/en/next/babel-plugin-proposal-numeric-separator</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@babel/plugin-proposal-object-rest-spread</td>
          <td>7.13.8</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-plugin-proposal-object-rest-spread">https://babel.dev/docs/en/next/babel-plugin-proposal-object-rest-spread</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@babel/plugin-proposal-optional-catch-binding</td>
          <td>7.13.8</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-plugin-proposal-optional-catch-binding">https://babel.dev/docs/en/next/babel-plugin-proposal-optional-catch-binding</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@babel/plugin-proposal-optional-chaining</td>
          <td>7.13.8</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-plugin-proposal-optional-chaining">https://babel.dev/docs/en/next/babel-plugin-proposal-optional-chaining</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@babel/plugin-proposal-private-methods</td>
          <td>7.13.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-plugin-proposal-private-methods">https://babel.dev/docs/en/next/babel-plugin-proposal-private-methods</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@babel/plugin-proposal-unicode-property-regex</td>
          <td>7.12.13</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-plugin-proposal-unicode-property-regex">https://babel.dev/docs/en/next/babel-plugin-proposal-unicode-property-regex</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@babel/plugin-syntax-async-generators</td>
          <td>7.8.4</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel/tree/master/packages/babel-plugin-syntax-async-generators">https://github.com/babel/babel/tree/master/packages/babel-plugin-syntax-async-generators</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@babel/plugin-syntax-class-properties</td>
          <td>7.12.13</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-plugin-syntax-class-properties">https://babel.dev/docs/en/next/babel-plugin-syntax-class-properties</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@babel/plugin-syntax-decorators</td>
          <td>7.12.13</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-plugin-syntax-decorators">https://babel.dev/docs/en/next/babel-plugin-syntax-decorators</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@babel/plugin-syntax-dynamic-import</td>
          <td>7.8.3</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel/tree/master/packages/babel-plugin-syntax-dynamic-import">https://github.com/babel/babel/tree/master/packages/babel-plugin-syntax-dynamic-import</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@babel/plugin-syntax-export-namespace-from</td>
          <td>7.8.3</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel/tree/master/packages/babel-plugin-syntax-export-namespace-from">https://github.com/babel/babel/tree/master/packages/babel-plugin-syntax-export-namespace-from</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@babel/plugin-syntax-json-strings</td>
          <td>7.8.3</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel/tree/master/packages/babel-plugin-syntax-json-strings">https://github.com/babel/babel/tree/master/packages/babel-plugin-syntax-json-strings</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@babel/plugin-syntax-jsx</td>
          <td>7.12.13</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-plugin-syntax-jsx">https://babel.dev/docs/en/next/babel-plugin-syntax-jsx</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@babel/plugin-syntax-logical-assignment-operators</td>
          <td>7.10.4</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@babel/plugin-syntax-nullish-coalescing-operator</td>
          <td>7.8.3</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel/tree/master/packages/babel-plugin-syntax-nullish-coalescing-operator">https://github.com/babel/babel/tree/master/packages/babel-plugin-syntax-nullish-coalescing-operator</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@babel/plugin-syntax-numeric-separator</td>
          <td>7.10.4</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@babel/plugin-syntax-object-rest-spread</td>
          <td>7.8.3</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel/tree/master/packages/babel-plugin-syntax-object-rest-spread">https://github.com/babel/babel/tree/master/packages/babel-plugin-syntax-object-rest-spread</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@babel/plugin-syntax-optional-catch-binding</td>
          <td>7.8.3</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel/tree/master/packages/babel-plugin-syntax-optional-catch-binding">https://github.com/babel/babel/tree/master/packages/babel-plugin-syntax-optional-catch-binding</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@babel/plugin-syntax-optional-chaining</td>
          <td>7.8.3</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel/tree/master/packages/babel-plugin-syntax-optional-chaining">https://github.com/babel/babel/tree/master/packages/babel-plugin-syntax-optional-chaining</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@babel/plugin-syntax-top-level-await</td>
          <td>7.12.13</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-plugin-syntax-top-level-await">https://babel.dev/docs/en/next/babel-plugin-syntax-top-level-await</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@babel/plugin-transform-arrow-functions</td>
          <td>7.13.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-plugin-transform-arrow-functions">https://babel.dev/docs/en/next/babel-plugin-transform-arrow-functions</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@babel/plugin-transform-async-to-generator</td>
          <td>7.13.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-plugin-transform-async-to-generator">https://babel.dev/docs/en/next/babel-plugin-transform-async-to-generator</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@babel/plugin-transform-block-scoped-functions</td>
          <td>7.12.13</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-plugin-transform-block-scoped-functions">https://babel.dev/docs/en/next/babel-plugin-transform-block-scoped-functions</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@babel/plugin-transform-block-scoping</td>
          <td>7.12.13</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-plugin-transform-block-scoping">https://babel.dev/docs/en/next/babel-plugin-transform-block-scoping</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@babel/plugin-transform-classes</td>
          <td>7.13.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-plugin-transform-classes">https://babel.dev/docs/en/next/babel-plugin-transform-classes</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@babel/plugin-transform-computed-properties</td>
          <td>7.13.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-plugin-transform-computed-properties">https://babel.dev/docs/en/next/babel-plugin-transform-computed-properties</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@babel/plugin-transform-destructuring</td>
          <td>7.13.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-plugin-transform-destructuring">https://babel.dev/docs/en/next/babel-plugin-transform-destructuring</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@babel/plugin-transform-dotall-regex</td>
          <td>7.12.13</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-plugin-transform-dotall-regex">https://babel.dev/docs/en/next/babel-plugin-transform-dotall-regex</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@babel/plugin-transform-duplicate-keys</td>
          <td>7.12.13</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-plugin-transform-duplicate-keys">https://babel.dev/docs/en/next/babel-plugin-transform-duplicate-keys</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@babel/plugin-transform-exponentiation-operator</td>
          <td>7.12.13</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-plugin-transform-exponentiation-operator">https://babel.dev/docs/en/next/babel-plugin-transform-exponentiation-operator</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@babel/plugin-transform-for-of</td>
          <td>7.13.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-plugin-transform-for-of">https://babel.dev/docs/en/next/babel-plugin-transform-for-of</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@babel/plugin-transform-function-name</td>
          <td>7.12.13</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-plugin-transform-function-name">https://babel.dev/docs/en/next/babel-plugin-transform-function-name</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@babel/plugin-transform-literals</td>
          <td>7.12.13</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-plugin-transform-literals">https://babel.dev/docs/en/next/babel-plugin-transform-literals</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@babel/plugin-transform-member-expression-literals</td>
          <td>7.12.13</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-plugin-transform-member-expression-literals">https://babel.dev/docs/en/next/babel-plugin-transform-member-expression-literals</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@babel/plugin-transform-modules-amd</td>
          <td>7.13.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-plugin-transform-modules-amd">https://babel.dev/docs/en/next/babel-plugin-transform-modules-amd</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@babel/plugin-transform-modules-commonjs</td>
          <td>7.13.8</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-plugin-transform-modules-commonjs">https://babel.dev/docs/en/next/babel-plugin-transform-modules-commonjs</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@babel/plugin-transform-modules-systemjs</td>
          <td>7.13.8</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-plugin-transform-modules-systemjs">https://babel.dev/docs/en/next/babel-plugin-transform-modules-systemjs</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@babel/plugin-transform-modules-umd</td>
          <td>7.13.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-plugin-transform-modules-umd">https://babel.dev/docs/en/next/babel-plugin-transform-modules-umd</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@babel/plugin-transform-named-capturing-groups-regex</td>
          <td>7.12.13</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-plugin-transform-named-capturing-groups-regex">https://babel.dev/docs/en/next/babel-plugin-transform-named-capturing-groups-regex</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@babel/plugin-transform-new-target</td>
          <td>7.12.13</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-plugin-transform-new-target">https://babel.dev/docs/en/next/babel-plugin-transform-new-target</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@babel/plugin-transform-object-super</td>
          <td>7.12.13</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-plugin-transform-object-super">https://babel.dev/docs/en/next/babel-plugin-transform-object-super</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@babel/plugin-transform-parameters</td>
          <td>7.13.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-plugin-transform-parameters">https://babel.dev/docs/en/next/babel-plugin-transform-parameters</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@babel/plugin-transform-property-literals</td>
          <td>7.12.13</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-plugin-transform-property-literals">https://babel.dev/docs/en/next/babel-plugin-transform-property-literals</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@babel/plugin-transform-regenerator</td>
          <td>7.12.13</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-plugin-transform-regenerator">https://babel.dev/docs/en/next/babel-plugin-transform-regenerator</a></td>
          <td>Ben Newman</td>
          </tr>
          <tr>
          <td>@babel/plugin-transform-reserved-words</td>
          <td>7.12.13</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-plugin-transform-reserved-words">https://babel.dev/docs/en/next/babel-plugin-transform-reserved-words</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@babel/plugin-transform-runtime</td>
          <td>7.13.9</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-plugin-transform-runtime">https://babel.dev/docs/en/next/babel-plugin-transform-runtime</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@babel/plugin-transform-shorthand-properties</td>
          <td>7.12.13</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-plugin-transform-shorthand-properties">https://babel.dev/docs/en/next/babel-plugin-transform-shorthand-properties</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@babel/plugin-transform-spread</td>
          <td>7.13.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-plugin-transform-spread">https://babel.dev/docs/en/next/babel-plugin-transform-spread</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@babel/plugin-transform-sticky-regex</td>
          <td>7.12.13</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-plugin-transform-sticky-regex">https://babel.dev/docs/en/next/babel-plugin-transform-sticky-regex</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@babel/plugin-transform-template-literals</td>
          <td>7.13.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-plugin-transform-template-literals">https://babel.dev/docs/en/next/babel-plugin-transform-template-literals</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@babel/plugin-transform-typeof-symbol</td>
          <td>7.12.13</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-plugin-transform-typeof-symbol">https://babel.dev/docs/en/next/babel-plugin-transform-typeof-symbol</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@babel/plugin-transform-unicode-escapes</td>
          <td>7.12.13</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-plugin-transform-unicode-escapes">https://babel.dev/docs/en/next/babel-plugin-transform-unicode-escapes</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@babel/plugin-transform-unicode-regex</td>
          <td>7.12.13</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-plugin-transform-unicode-regex">https://babel.dev/docs/en/next/babel-plugin-transform-unicode-regex</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@babel/preset-env</td>
          <td>7.13.9</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-preset-env">https://babel.dev/docs/en/next/babel-preset-env</a></td>
          <td>Henry Zhu</td>
          </tr>
          <tr>
          <td>@babel/preset-modules</td>
          <td>0.1.4</td>
          <td>MIT</td>
          <td>Unknown</td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@babel/runtime</td>
          <td>7.13.9</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-runtime">https://babel.dev/docs/en/next/babel-runtime</a></td>
          <td>Sebastian McKenzie</td>
          </tr>
          <tr>
          <td>@babel/template</td>
          <td>7.12.13</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-template">https://babel.dev/docs/en/next/babel-template</a></td>
          <td>Sebastian McKenzie</td>
          </tr>
          <tr>
          <td>@babel/traverse</td>
          <td>7.13.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-traverse">https://babel.dev/docs/en/next/babel-traverse</a></td>
          <td>Sebastian McKenzie</td>
          </tr>
          <tr>
          <td>@babel/types</td>
          <td>7.13.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel.git">https://github.com/babel/babel.git</a></td>
          <td><a href="https://babel.dev/docs/en/next/babel-types">https://babel.dev/docs/en/next/babel-types</a></td>
          <td>Sebastian McKenzie</td>
          </tr>
          <tr>
          <td>@intervolga/optimize-cssnano-plugin</td>
          <td>1.0.6</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/intervolga/optimize-cssnano-plugin">https://github.com/intervolga/optimize-cssnano-plugin</a></td>
          <td><a href="https://github.com/intervolga/optimize-cssnano-plugin#readme">https://github.com/intervolga/optimize-cssnano-plugin#readme</a></td>
          <td>Shkarupa Alex</td>
          </tr>
          <tr>
          <td>@intlify/vue-i18n-loader</td>
          <td>0.6.1</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/intlify/vue-i18n-loader.git">https://github.com/intlify/vue-i18n-loader.git</a></td>
          <td><a href="https://github.com/intlify/vue-i18n-loader#readme">https://github.com/intlify/vue-i18n-loader#readme</a></td>
          <td>kazuya kawaguchi</td>
          </tr>
          <tr>
          <td>@mrmlnc/readdir-enhanced</td>
          <td>2.2.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/bigstickcarpet/readdir-enhanced.git">https://github.com/bigstickcarpet/readdir-enhanced.git</a></td>
          <td><a href="https://github.com/bigstickcarpet/readdir-enhanced">https://github.com/bigstickcarpet/readdir-enhanced</a></td>
          <td>James Messinger</td>
          </tr>
          <tr>
          <td>@nodelib/fs.scandir</td>
          <td>2.1.4</td>
          <td>MIT</td>
          <td><a href="https://github.com/nodelib/nodelib/tree/master/packages/fs/fs.scandir">https://github.com/nodelib/nodelib/tree/master/packages/fs/fs.scandir</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@nodelib/fs.stat</td>
          <td>1.1.3</td>
          <td>MIT</td>
          <td><a href="https://github.com/nodelib/nodelib/tree/master/packages/fs/fs.stat">https://github.com/nodelib/nodelib/tree/master/packages/fs/fs.stat</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@nodelib/fs.stat</td>
          <td>2.0.4</td>
          <td>MIT</td>
          <td><a href="https://github.com/nodelib/nodelib/tree/master/packages/fs/fs.stat">https://github.com/nodelib/nodelib/tree/master/packages/fs/fs.stat</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@nodelib/fs.walk</td>
          <td>1.2.6</td>
          <td>MIT</td>
          <td><a href="https://github.com/nodelib/nodelib/tree/master/packages/fs/fs.walk">https://github.com/nodelib/nodelib/tree/master/packages/fs/fs.walk</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@prerenderer/prerenderer</td>
          <td>0.7.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/Tribex/prerenderer.git">https://github.com/Tribex/prerenderer.git</a></td>
          <td><a href="https://joshderf.com/">https://joshderf.com/</a></td>
          <td>Joshua Bemenderfer</td>
          </tr>
          <tr>
          <td>@prerenderer/renderer-puppeteer</td>
          <td>0.2.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/Tribex/prerenderer.git">https://github.com/Tribex/prerenderer.git</a></td>
          <td><a href="https://joshderf.com/">https://joshderf.com/</a></td>
          <td>Joshua Bemenderfer</td>
          </tr>
          <tr>
          <td>@sindresorhus/is</td>
          <td>0.14.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/is.git">https://github.com/sindresorhus/is.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>@soda/friendly-errors-webpack-plugin</td>
          <td>1.8.0</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/sodatea/friendly-errors-webpack-plugin.git">https://github.com/sodatea/friendly-errors-webpack-plugin.git</a></td>
          <td>Unknown</td>
          <td>Geoffroy Warin</td>
          </tr>
          <tr>
          <td>@soda/get-current-script</td>
          <td>1.0.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/sodatea/get-current-script.git">https://github.com/sodatea/get-current-script.git</a></td>
          <td>Unknown</td>
          <td>Haoqun Jiang</td>
          </tr>
          <tr>
          <td>@szmarczak/http-timer</td>
          <td>1.1.2</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/szmarczak/http-timer.git">https://github.com/szmarczak/http-timer.git</a></td>
          <td><a href="https://github.com/szmarczak/http-timer#readme">https://github.com/szmarczak/http-timer#readme</a></td>
          <td>Szymon Marczak</td>
          </tr>
          <tr>
          <td>@types/anymatch</td>
          <td>1.3.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/DefinitelyTyped/DefinitelyTyped.git">https://github.com/DefinitelyTyped/DefinitelyTyped.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@types/body-parser</td>
          <td>1.19.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/DefinitelyTyped/DefinitelyTyped.git">https://github.com/DefinitelyTyped/DefinitelyTyped.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@types/connect</td>
          <td>3.4.34</td>
          <td>MIT</td>
          <td><a href="https://github.com/DefinitelyTyped/DefinitelyTyped.git">https://github.com/DefinitelyTyped/DefinitelyTyped.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@types/connect-history-api-fallback</td>
          <td>1.3.3</td>
          <td>MIT</td>
          <td><a href="https://github.com/DefinitelyTyped/DefinitelyTyped.git">https://github.com/DefinitelyTyped/DefinitelyTyped.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@types/express</td>
          <td>4.17.11</td>
          <td>MIT</td>
          <td><a href="https://github.com/DefinitelyTyped/DefinitelyTyped.git">https://github.com/DefinitelyTyped/DefinitelyTyped.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@types/express-serve-static-core</td>
          <td>4.17.18</td>
          <td>MIT</td>
          <td><a href="https://github.com/DefinitelyTyped/DefinitelyTyped.git">https://github.com/DefinitelyTyped/DefinitelyTyped.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@types/glob</td>
          <td>7.1.3</td>
          <td>MIT</td>
          <td><a href="https://github.com/DefinitelyTyped/DefinitelyTyped.git">https://github.com/DefinitelyTyped/DefinitelyTyped.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@types/http-proxy</td>
          <td>1.17.5</td>
          <td>MIT</td>
          <td><a href="https://github.com/DefinitelyTyped/DefinitelyTyped.git">https://github.com/DefinitelyTyped/DefinitelyTyped.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@types/http-proxy-middleware</td>
          <td>0.19.3</td>
          <td>MIT</td>
          <td><a href="https://github.com/DefinitelyTyped/DefinitelyTyped.git">https://github.com/DefinitelyTyped/DefinitelyTyped.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@types/json-schema</td>
          <td>7.0.7</td>
          <td>MIT</td>
          <td><a href="https://github.com/DefinitelyTyped/DefinitelyTyped.git">https://github.com/DefinitelyTyped/DefinitelyTyped.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@types/json5</td>
          <td>0.0.29</td>
          <td>MIT</td>
          <td><a href="https://www.github.com/DefinitelyTyped/DefinitelyTyped.git">https://www.github.com/DefinitelyTyped/DefinitelyTyped.git</a></td>
          <td>Unknown</td>
          <td>Jason Swearingen</td>
          </tr>
          <tr>
          <td>@types/mime</td>
          <td>1.3.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/DefinitelyTyped/DefinitelyTyped.git">https://github.com/DefinitelyTyped/DefinitelyTyped.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@types/minimatch</td>
          <td>3.0.3</td>
          <td>MIT</td>
          <td><a href="https://www.github.com/DefinitelyTyped/DefinitelyTyped.git">https://www.github.com/DefinitelyTyped/DefinitelyTyped.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@types/minimist</td>
          <td>1.2.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/DefinitelyTyped/DefinitelyTyped.git">https://github.com/DefinitelyTyped/DefinitelyTyped.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@types/node</td>
          <td>14.14.31</td>
          <td>MIT</td>
          <td><a href="https://github.com/DefinitelyTyped/DefinitelyTyped.git">https://github.com/DefinitelyTyped/DefinitelyTyped.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@types/normalize-package-data</td>
          <td>2.4.0</td>
          <td>MIT</td>
          <td><a href="https://www.github.com/DefinitelyTyped/DefinitelyTyped.git">https://www.github.com/DefinitelyTyped/DefinitelyTyped.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@types/q</td>
          <td>1.5.4</td>
          <td>MIT</td>
          <td><a href="https://github.com/DefinitelyTyped/DefinitelyTyped.git">https://github.com/DefinitelyTyped/DefinitelyTyped.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@types/qs</td>
          <td>6.9.5</td>
          <td>MIT</td>
          <td><a href="https://github.com/DefinitelyTyped/DefinitelyTyped.git">https://github.com/DefinitelyTyped/DefinitelyTyped.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@types/range-parser</td>
          <td>1.2.3</td>
          <td>MIT</td>
          <td><a href="https://github.com/DefinitelyTyped/DefinitelyTyped.git">https://github.com/DefinitelyTyped/DefinitelyTyped.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@types/serve-static</td>
          <td>1.13.9</td>
          <td>MIT</td>
          <td><a href="https://github.com/DefinitelyTyped/DefinitelyTyped.git">https://github.com/DefinitelyTyped/DefinitelyTyped.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@types/source-list-map</td>
          <td>0.1.2</td>
          <td>MIT</td>
          <td><a href="https://www.github.com/DefinitelyTyped/DefinitelyTyped.git">https://www.github.com/DefinitelyTyped/DefinitelyTyped.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@types/tapable</td>
          <td>1.0.6</td>
          <td>MIT</td>
          <td><a href="https://github.com/DefinitelyTyped/DefinitelyTyped.git">https://github.com/DefinitelyTyped/DefinitelyTyped.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@types/uglify-js</td>
          <td>3.12.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/DefinitelyTyped/DefinitelyTyped.git">https://github.com/DefinitelyTyped/DefinitelyTyped.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@types/webpack</td>
          <td>4.41.26</td>
          <td>MIT</td>
          <td><a href="https://github.com/DefinitelyTyped/DefinitelyTyped.git">https://github.com/DefinitelyTyped/DefinitelyTyped.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@types/webpack-dev-server</td>
          <td>3.11.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/DefinitelyTyped/DefinitelyTyped.git">https://github.com/DefinitelyTyped/DefinitelyTyped.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@types/webpack-sources</td>
          <td>2.1.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/DefinitelyTyped/DefinitelyTyped.git">https://github.com/DefinitelyTyped/DefinitelyTyped.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@types/zen-observable</td>
          <td>0.8.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/DefinitelyTyped/DefinitelyTyped.git">https://github.com/DefinitelyTyped/DefinitelyTyped.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@vue/babel-helper-vue-jsx-merge-props</td>
          <td>1.2.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/vuejs/jsx/tree/master/packages/babel-helper-vue-jsx-merge-props">https://github.com/vuejs/jsx/tree/master/packages/babel-helper-vue-jsx-merge-props</a></td>
          <td>Unknown</td>
          <td>Evan You</td>
          </tr>
          <tr>
          <td>@vue/babel-helper-vue-transform-on</td>
          <td>1.0.2</td>
          <td>MIT</td>
          <td>Unknown</td>
          <td>Unknown</td>
          <td>Amour1688</td>
          </tr>
          <tr>
          <td>@vue/babel-plugin-jsx</td>
          <td>1.0.3</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/vuejs/jsx-next.git">https://github.com/vuejs/jsx-next.git</a></td>
          <td><a href="https://github.com/vuejs/jsx-next/tree/dev/packages/babel-plugin-jsx#readme">https://github.com/vuejs/jsx-next/tree/dev/packages/babel-plugin-jsx#readme</a></td>
          <td>Amour1688</td>
          </tr>
          <tr>
          <td>@vue/babel-plugin-transform-vue-jsx</td>
          <td>1.2.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/vuejs/jsx/tree/master/packages/babel-plugin-transform-vue-jsx">https://github.com/vuejs/jsx/tree/master/packages/babel-plugin-transform-vue-jsx</a></td>
          <td>Unknown</td>
          <td>Evan You</td>
          </tr>
          <tr>
          <td>@vue/babel-preset-app</td>
          <td>4.5.11</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/vuejs/vue-cli.git">https://github.com/vuejs/vue-cli.git</a></td>
          <td><a href="https://github.com/vuejs/vue-cli/tree/dev/packages/@vue/babel-preset-app#readme">https://github.com/vuejs/vue-cli/tree/dev/packages/@vue/babel-preset-app#readme</a></td>
          <td>Evan You</td>
          </tr>
          <tr>
          <td>@vue/babel-preset-jsx</td>
          <td>1.2.4</td>
          <td>MIT</td>
          <td><a href="https://github.com/vuejs/jsx/tree/master/packages/babel-preset-jsx">https://github.com/vuejs/jsx/tree/master/packages/babel-preset-jsx</a></td>
          <td>Unknown</td>
          <td>Nick Messing</td>
          </tr>
          <tr>
          <td>@vue/babel-sugar-composition-api-inject-h</td>
          <td>1.2.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/vuejs/jsx/tree/master/packages/babel-sugar-composition-api-inject-h">https://github.com/vuejs/jsx/tree/master/packages/babel-sugar-composition-api-inject-h</a></td>
          <td>Unknown</td>
          <td>luwanquan</td>
          </tr>
          <tr>
          <td>@vue/babel-sugar-composition-api-render-instance</td>
          <td>1.2.4</td>
          <td>MIT</td>
          <td><a href="https://github.com/vuejs/jsx/tree/master/packages/babel-sugar-composition-api-render-instance">https://github.com/vuejs/jsx/tree/master/packages/babel-sugar-composition-api-render-instance</a></td>
          <td>Unknown</td>
          <td>luwanquan</td>
          </tr>
          <tr>
          <td>@vue/babel-sugar-functional-vue</td>
          <td>1.2.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/vuejs/jsx/tree/master/packages/babel-sugar-functional-vue">https://github.com/vuejs/jsx/tree/master/packages/babel-sugar-functional-vue</a></td>
          <td>Unknown</td>
          <td>Nick Messing</td>
          </tr>
          <tr>
          <td>@vue/babel-sugar-inject-h</td>
          <td>1.2.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/vuejs/jsx/tree/master/packages/babel-sugar-inject-h">https://github.com/vuejs/jsx/tree/master/packages/babel-sugar-inject-h</a></td>
          <td>Unknown</td>
          <td>Nick Messing</td>
          </tr>
          <tr>
          <td>@vue/babel-sugar-v-model</td>
          <td>1.2.3</td>
          <td>MIT</td>
          <td><a href="https://github.com/vuejs/jsx/tree/master/packages/babel-sugar-v-model">https://github.com/vuejs/jsx/tree/master/packages/babel-sugar-v-model</a></td>
          <td>Unknown</td>
          <td>Nick Messing</td>
          </tr>
          <tr>
          <td>@vue/babel-sugar-v-on</td>
          <td>1.2.3</td>
          <td>MIT</td>
          <td><a href="https://github.com/vuejs/jsx/tree/master/packages/babel-sugar-v-on">https://github.com/vuejs/jsx/tree/master/packages/babel-sugar-v-on</a></td>
          <td>Unknown</td>
          <td>Nick Messing</td>
          </tr>
          <tr>
          <td>@vue/cli-overlay</td>
          <td>4.5.11</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/vuejs/vue-cli.git">https://github.com/vuejs/vue-cli.git</a></td>
          <td><a href="https://github.com/vuejs/vue-cli/tree/dev/packages/@vue/cli-overlay#readme">https://github.com/vuejs/vue-cli/tree/dev/packages/@vue/cli-overlay#readme</a></td>
          <td>Evan You</td>
          </tr>
          <tr>
          <td>@vue/cli-plugin-babel</td>
          <td>4.5.11</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/vuejs/vue-cli.git">https://github.com/vuejs/vue-cli.git</a></td>
          <td><a href="https://github.com/vuejs/vue-cli/tree/dev/packages/@vue/cli-plugin-babel#readme">https://github.com/vuejs/vue-cli/tree/dev/packages/@vue/cli-plugin-babel#readme</a></td>
          <td>Evan You</td>
          </tr>
          <tr>
          <td>@vue/cli-plugin-eslint</td>
          <td>4.5.11</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/vuejs/vue-cli.git">https://github.com/vuejs/vue-cli.git</a></td>
          <td><a href="https://github.com/vuejs/vue-cli/tree/dev/packages/@vue/cli-plugin-eslint#readme">https://github.com/vuejs/vue-cli/tree/dev/packages/@vue/cli-plugin-eslint#readme</a></td>
          <td>Evan You</td>
          </tr>
          <tr>
          <td>@vue/cli-plugin-router</td>
          <td>4.5.11</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/vuejs/vue-cli.git">https://github.com/vuejs/vue-cli.git</a></td>
          <td><a href="https://github.com/vuejs/vue-cli/tree/dev/packages/@vue/cli-plugin-router#readme">https://github.com/vuejs/vue-cli/tree/dev/packages/@vue/cli-plugin-router#readme</a></td>
          <td>Evan You</td>
          </tr>
          <tr>
          <td>@vue/cli-plugin-vuex</td>
          <td>4.5.11</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/vuejs/vue-cli.git">https://github.com/vuejs/vue-cli.git</a></td>
          <td><a href="https://github.com/vuejs/vue-cli/tree/dev/packages/@vue/cli-plugin-vuex#readme">https://github.com/vuejs/vue-cli/tree/dev/packages/@vue/cli-plugin-vuex#readme</a></td>
          <td>Evan You</td>
          </tr>
          <tr>
          <td>@vue/cli-service</td>
          <td>4.5.11</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/vuejs/vue-cli.git">https://github.com/vuejs/vue-cli.git</a></td>
          <td><a href="https://cli.vuejs.org/">https://cli.vuejs.org/</a></td>
          <td>Evan You</td>
          </tr>
          <tr>
          <td>@vue/cli-shared-utils</td>
          <td>4.5.11</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/vuejs/vue-cli.git">https://github.com/vuejs/vue-cli.git</a></td>
          <td><a href="https://github.com/vuejs/vue-cli/tree/dev/packages/@vue/cli-shared-utils#readme">https://github.com/vuejs/vue-cli/tree/dev/packages/@vue/cli-shared-utils#readme</a></td>
          <td>Evan You</td>
          </tr>
          <tr>
          <td>@vue/component-compiler-utils</td>
          <td>3.2.0</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/vuejs/component-compiler-utils.git">https://github.com/vuejs/component-compiler-utils.git</a></td>
          <td><a href="https://github.com/vuejs/component-compiler-utils#readme">https://github.com/vuejs/component-compiler-utils#readme</a></td>
          <td>Evan You</td>
          </tr>
          <tr>
          <td>@vue/component-compiler-utils</td>
          <td>2.6.0</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/vuejs/component-compiler-utils.git">https://github.com/vuejs/component-compiler-utils.git</a></td>
          <td><a href="https://github.com/vuejs/component-compiler-utils#readme">https://github.com/vuejs/component-compiler-utils#readme</a></td>
          <td>Evan You</td>
          </tr>
          <tr>
          <td>@vue/composition-api</td>
          <td>1.0.0-rc.2</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/vuejs/composition-api.git">https://github.com/vuejs/composition-api.git</a></td>
          <td><a href="https://github.com/vuejs/composition-api#readme">https://github.com/vuejs/composition-api#readme</a></td>
          <td>liximomo</td>
          </tr>
          <tr>
          <td>@vue/eslint-config-airbnb</td>
          <td>4.0.1</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/vuejs/vue-cli.git">https://github.com/vuejs/vue-cli.git</a></td>
          <td><a href="https://github.com/vuejs/vue-cli/tree/dev/packages/@vue/eslint-config-airbnb#readme">https://github.com/vuejs/vue-cli/tree/dev/packages/@vue/eslint-config-airbnb#readme</a></td>
          <td>Evan You</td>
          </tr>
          <tr>
          <td>@vue/test-utils</td>
          <td>1.1.3</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/vuejs/vue-test-utils.git">https://github.com/vuejs/vue-test-utils.git</a></td>
          <td><a href="https://github.com/vuejs/vue-test-utils#readme">https://github.com/vuejs/vue-test-utils#readme</a></td>
          <td>vuejs</td>
          </tr>
          <tr>
          <td>@vue/web-component-wrapper</td>
          <td>1.3.0</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/vuejs/web-component-wrapper.git">https://github.com/vuejs/web-component-wrapper.git</a></td>
          <td><a href="https://github.com/vuejs/web-component-wrapper#readme">https://github.com/vuejs/web-component-wrapper#readme</a></td>
          <td>Evan You</td>
          </tr>
          <tr>
          <td>@webassemblyjs/ast</td>
          <td>1.9.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/xtuc/webassemblyjs.git">https://github.com/xtuc/webassemblyjs.git</a></td>
          <td>Unknown</td>
          <td>Sven Sauleau</td>
          </tr>
          <tr>
          <td>@webassemblyjs/floating-point-hex-parser</td>
          <td>1.9.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/xtuc/webassemblyjs.git">https://github.com/xtuc/webassemblyjs.git</a></td>
          <td>Unknown</td>
          <td>Mauro Bringolf</td>
          </tr>
          <tr>
          <td>@webassemblyjs/helper-api-error</td>
          <td>1.9.0</td>
          <td>MIT</td>
          <td>Unknown</td>
          <td>Unknown</td>
          <td>Sven Sauleau</td>
          </tr>
          <tr>
          <td>@webassemblyjs/helper-buffer</td>
          <td>1.9.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/xtuc/webassemblyjs.git">https://github.com/xtuc/webassemblyjs.git</a></td>
          <td>Unknown</td>
          <td>Sven Sauleau</td>
          </tr>
          <tr>
          <td>@webassemblyjs/helper-code-frame</td>
          <td>1.9.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/xtuc/webassemblyjs.git">https://github.com/xtuc/webassemblyjs.git</a></td>
          <td>Unknown</td>
          <td>Sven Sauleau</td>
          </tr>
          <tr>
          <td>@webassemblyjs/helper-module-context</td>
          <td>1.9.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/xtuc/webassemblyjs.git">https://github.com/xtuc/webassemblyjs.git</a></td>
          <td>Unknown</td>
          <td>Sven Sauleau</td>
          </tr>
          <tr>
          <td>@webassemblyjs/helper-wasm-bytecode</td>
          <td>1.9.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/xtuc/webassemblyjs.git">https://github.com/xtuc/webassemblyjs.git</a></td>
          <td>Unknown</td>
          <td>Sven Sauleau</td>
          </tr>
          <tr>
          <td>@webassemblyjs/helper-wasm-section</td>
          <td>1.9.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/xtuc/webassemblyjs.git">https://github.com/xtuc/webassemblyjs.git</a></td>
          <td>Unknown</td>
          <td>Sven Sauleau</td>
          </tr>
          <tr>
          <td>@webassemblyjs/ieee754</td>
          <td>1.9.0</td>
          <td>MIT</td>
          <td>Unknown</td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@webassemblyjs/leb128</td>
          <td>1.9.0</td>
          <td>MIT</td>
          <td>Unknown</td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@webassemblyjs/utf8</td>
          <td>1.9.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/xtuc/webassemblyjs.git">https://github.com/xtuc/webassemblyjs.git</a></td>
          <td>Unknown</td>
          <td>Sven Sauleau</td>
          </tr>
          <tr>
          <td>@webassemblyjs/wasm-edit</td>
          <td>1.9.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/xtuc/webassemblyjs.git">https://github.com/xtuc/webassemblyjs.git</a></td>
          <td>Unknown</td>
          <td>Sven Sauleau</td>
          </tr>
          <tr>
          <td>@webassemblyjs/wasm-gen</td>
          <td>1.9.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/xtuc/webassemblyjs.git">https://github.com/xtuc/webassemblyjs.git</a></td>
          <td>Unknown</td>
          <td>Sven Sauleau</td>
          </tr>
          <tr>
          <td>@webassemblyjs/wasm-opt</td>
          <td>1.9.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/xtuc/webassemblyjs.git">https://github.com/xtuc/webassemblyjs.git</a></td>
          <td>Unknown</td>
          <td>Sven Sauleau</td>
          </tr>
          <tr>
          <td>@webassemblyjs/wasm-parser</td>
          <td>1.9.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/xtuc/webassemblyjs.git">https://github.com/xtuc/webassemblyjs.git</a></td>
          <td>Unknown</td>
          <td>Sven Sauleau</td>
          </tr>
          <tr>
          <td>@webassemblyjs/wast-parser</td>
          <td>1.9.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/xtuc/webassemblyjs.git">https://github.com/xtuc/webassemblyjs.git</a></td>
          <td>Unknown</td>
          <td>Sven Sauleau</td>
          </tr>
          <tr>
          <td>@webassemblyjs/wast-printer</td>
          <td>1.9.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/xtuc/webassemblyjs.git">https://github.com/xtuc/webassemblyjs.git</a></td>
          <td>Unknown</td>
          <td>Sven Sauleau</td>
          </tr>
          <tr>
          <td>@wry/context</td>
          <td>0.4.4</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/benjamn/wryware.git">https://github.com/benjamn/wryware.git</a></td>
          <td><a href="https://github.com/benjamn/wryware">https://github.com/benjamn/wryware</a></td>
          <td>Ben Newman</td>
          </tr>
          <tr>
          <td>@wry/equality</td>
          <td>0.1.11</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/benjamn/wryware.git">https://github.com/benjamn/wryware.git</a></td>
          <td><a href="https://github.com/benjamn/wryware">https://github.com/benjamn/wryware</a></td>
          <td>Ben Newman</td>
          </tr>
          <tr>
          <td>accepts</td>
          <td>1.3.7</td>
          <td>MIT</td>
          <td><a href="https://github.com/jshttp/accepts.git">https://github.com/jshttp/accepts.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>acorn</td>
          <td>6.4.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/acornjs/acorn.git">https://github.com/acornjs/acorn.git</a></td>
          <td><a href="https://github.com/acornjs/acorn">https://github.com/acornjs/acorn</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>acorn</td>
          <td>7.4.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/acornjs/acorn.git">https://github.com/acornjs/acorn.git</a></td>
          <td><a href="https://github.com/acornjs/acorn">https://github.com/acornjs/acorn</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>acorn</td>
          <td>8.0.5</td>
          <td>MIT</td>
          <td><a href="https://github.com/acornjs/acorn.git">https://github.com/acornjs/acorn.git</a></td>
          <td><a href="https://github.com/acornjs/acorn">https://github.com/acornjs/acorn</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>acorn-globals</td>
          <td>6.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/ForbesLindesay/acorn-globals.git">https://github.com/ForbesLindesay/acorn-globals.git</a></td>
          <td>Unknown</td>
          <td>ForbesLindesay</td>
          </tr>
          <tr>
          <td>acorn-jsx</td>
          <td>5.3.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/acornjs/acorn-jsx">https://github.com/acornjs/acorn-jsx</a></td>
          <td><a href="https://github.com/acornjs/acorn-jsx">https://github.com/acornjs/acorn-jsx</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>acorn-walk</td>
          <td>7.2.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/acornjs/acorn.git">https://github.com/acornjs/acorn.git</a></td>
          <td><a href="https://github.com/acornjs/acorn">https://github.com/acornjs/acorn</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>acorn-walk</td>
          <td>8.0.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/acornjs/acorn.git">https://github.com/acornjs/acorn.git</a></td>
          <td><a href="https://github.com/acornjs/acorn">https://github.com/acornjs/acorn</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>address</td>
          <td>1.1.2</td>
          <td>MIT</td>
          <td>git://github.com/node-modules/address.git</td>
          <td>Unknown</td>
          <td>fengmk2</td>
          </tr>
          <tr>
          <td>agent-base</td>
          <td>4.3.0</td>
          <td>MIT</td>
          <td>git://github.com/TooTallNate/node-agent-base.git</td>
          <td><a href="http://n8.io/">http://n8.io/</a></td>
          <td>Nathan Rajlich</td>
          </tr>
          <tr>
          <td>aggregate-error</td>
          <td>3.1.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/aggregate-error.git">https://github.com/sindresorhus/aggregate-error.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>ajv</td>
          <td>6.12.6</td>
          <td>MIT</td>
          <td><a href="https://github.com/ajv-validator/ajv.git">https://github.com/ajv-validator/ajv.git</a></td>
          <td><a href="https://github.com/ajv-validator/ajv">https://github.com/ajv-validator/ajv</a></td>
          <td>Evgeny Poberezkin</td>
          </tr>
          <tr>
          <td>ajv-errors</td>
          <td>1.0.1</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/epoberezkin/ajv-errors.git">https://github.com/epoberezkin/ajv-errors.git</a></td>
          <td><a href="https://github.com/epoberezkin/ajv-errors#readme">https://github.com/epoberezkin/ajv-errors#readme</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>ajv-keywords</td>
          <td>3.5.2</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/epoberezkin/ajv-keywords.git">https://github.com/epoberezkin/ajv-keywords.git</a></td>
          <td><a href="https://github.com/epoberezkin/ajv-keywords#readme">https://github.com/epoberezkin/ajv-keywords#readme</a></td>
          <td>Evgeny Poberezkin</td>
          </tr>
          <tr>
          <td>alphanum-sort</td>
          <td>1.0.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/TrySound/alphanum-sort.git">https://github.com/TrySound/alphanum-sort.git</a></td>
          <td><a href="https://github.com/TrySound/alphanum-sort">https://github.com/TrySound/alphanum-sort</a></td>
          <td>Bogdan Chadkin</td>
          </tr>
          <tr>
          <td>ansi-colors</td>
          <td>3.2.4</td>
          <td>MIT</td>
          <td><a href="https://github.com/doowb/ansi-colors.git">https://github.com/doowb/ansi-colors.git</a></td>
          <td><a href="https://github.com/doowb/ansi-colors">https://github.com/doowb/ansi-colors</a></td>
          <td>Brian Woodward</td>
          </tr>
          <tr>
          <td>ansi-escapes</td>
          <td>4.3.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/ansi-escapes.git">https://github.com/sindresorhus/ansi-escapes.git</a></td>
          <td><a href="https://sindresorhus.com">https://sindresorhus.com</a></td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>ansi-escapes</td>
          <td>3.2.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/ansi-escapes.git">https://github.com/sindresorhus/ansi-escapes.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>ansi-regex</td>
          <td>5.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/chalk/ansi-regex.git">https://github.com/chalk/ansi-regex.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>ansi-regex</td>
          <td>4.1.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/chalk/ansi-regex.git">https://github.com/chalk/ansi-regex.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>ansi-regex</td>
          <td>2.1.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/chalk/ansi-regex.git">https://github.com/chalk/ansi-regex.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>ansi-regex</td>
          <td>3.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/chalk/ansi-regex.git">https://github.com/chalk/ansi-regex.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>ansi-styles</td>
          <td>3.2.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/chalk/ansi-styles.git">https://github.com/chalk/ansi-styles.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>ansi-styles</td>
          <td>4.3.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/chalk/ansi-styles.git">https://github.com/chalk/ansi-styles.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>ansi-styles</td>
          <td>5.1.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/chalk/ansi-styles.git">https://github.com/chalk/ansi-styles.git</a></td>
          <td><a href="https://sindresorhus.com">https://sindresorhus.com</a></td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>ansi-styles</td>
          <td>2.2.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/chalk/ansi-styles.git">https://github.com/chalk/ansi-styles.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>any-promise</td>
          <td>1.3.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/kevinbeaty/any-promise">https://github.com/kevinbeaty/any-promise</a></td>
          <td><a href="http://github.com/kevinbeaty/any-promise">http://github.com/kevinbeaty/any-promise</a></td>
          <td>Kevin Beaty</td>
          </tr>
          <tr>
          <td>apollo-cache</td>
          <td>1.3.5</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/apollographql/apollo-client.git">https://github.com/apollographql/apollo-client.git</a></td>
          <td><a href="https://github.com/apollographql/apollo-client#readme">https://github.com/apollographql/apollo-client#readme</a></td>
          <td>James Baxley</td>
          </tr>
          <tr>
          <td>apollo-cache-inmemory</td>
          <td>1.6.6</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/apollographql/apollo-client.git">https://github.com/apollographql/apollo-client.git</a></td>
          <td><a href="https://github.com/apollographql/apollo-client#readme">https://github.com/apollographql/apollo-client#readme</a></td>
          <td>James Baxley</td>
          </tr>
          <tr>
          <td>apollo-client</td>
          <td>2.6.10</td>
          <td>MIT</td>
          <td><a href="https://github.com/apollographql/apollo-client.git">https://github.com/apollographql/apollo-client.git</a></td>
          <td>Unknown</td>
          <td>Sashko Stubailo</td>
          </tr>
          <tr>
          <td>apollo-link</td>
          <td>1.2.14</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/apollographql/apollo-link.git">https://github.com/apollographql/apollo-link.git</a></td>
          <td><a href="https://github.com/apollographql/apollo-link#readme">https://github.com/apollographql/apollo-link#readme</a></td>
          <td>Evans Hauser</td>
          </tr>
          <tr>
          <td>apollo-link-http</td>
          <td>1.5.17</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/apollographql/apollo-link.git">https://github.com/apollographql/apollo-link.git</a></td>
          <td><a href="https://github.com/apollographql/apollo-link#readme">https://github.com/apollographql/apollo-link#readme</a></td>
          <td>Evans Hauser</td>
          </tr>
          <tr>
          <td>apollo-link-http-common</td>
          <td>0.2.16</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/apollographql/apollo-link.git">https://github.com/apollographql/apollo-link.git</a></td>
          <td><a href="https://github.com/apollographql/apollo-link#readme">https://github.com/apollographql/apollo-link#readme</a></td>
          <td>Evans Hauser</td>
          </tr>
          <tr>
          <td>apollo-utilities</td>
          <td>1.3.4</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/apollographql/apollo-client.git">https://github.com/apollographql/apollo-client.git</a></td>
          <td><a href="https://github.com/apollographql/apollo-client#readme">https://github.com/apollographql/apollo-client#readme</a></td>
          <td>James Baxley</td>
          </tr>
          <tr>
          <td>arch</td>
          <td>2.2.0</td>
          <td>MIT</td>
          <td>git://github.com/feross/arch.git</td>
          <td><a href="https://github.com/feross/arch">https://github.com/feross/arch</a></td>
          <td>Feross Aboukhadijeh</td>
          </tr>
          <tr>
          <td>argparse</td>
          <td>1.0.10</td>
          <td>MIT</td>
          <td><a href="https://github.com/nodeca/argparse.git">https://github.com/nodeca/argparse.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>arr-diff</td>
          <td>4.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/arr-diff.git">https://github.com/jonschlinkert/arr-diff.git</a></td>
          <td><a href="https://github.com/jonschlinkert/arr-diff">https://github.com/jonschlinkert/arr-diff</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>arr-flatten</td>
          <td>1.1.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/arr-flatten.git">https://github.com/jonschlinkert/arr-flatten.git</a></td>
          <td><a href="https://github.com/jonschlinkert/arr-flatten">https://github.com/jonschlinkert/arr-flatten</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>arr-union</td>
          <td>3.1.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/arr-union.git">https://github.com/jonschlinkert/arr-union.git</a></td>
          <td><a href="https://github.com/jonschlinkert/arr-union">https://github.com/jonschlinkert/arr-union</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>array-find</td>
          <td>1.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/stefanduberg/array-find.git">https://github.com/stefanduberg/array-find.git</a></td>
          <td><a href="https://github.com/stefanduberg/array-find">https://github.com/stefanduberg/array-find</a></td>
          <td>Stefan Duberg</td>
          </tr>
          <tr>
          <td>array-find-index</td>
          <td>1.0.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/array-find-index.git">https://github.com/sindresorhus/array-find-index.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>array-flatten</td>
          <td>1.1.1</td>
          <td>MIT</td>
          <td>git://github.com/blakeembrey/array-flatten.git</td>
          <td><a href="https://github.com/blakeembrey/array-flatten">https://github.com/blakeembrey/array-flatten</a></td>
          <td>Blake Embrey</td>
          </tr>
          <tr>
          <td>array-flatten</td>
          <td>2.1.2</td>
          <td>MIT</td>
          <td>git://github.com/blakeembrey/array-flatten.git</td>
          <td><a href="https://github.com/blakeembrey/array-flatten">https://github.com/blakeembrey/array-flatten</a></td>
          <td>Blake Embrey</td>
          </tr>
          <tr>
          <td>array-includes</td>
          <td>3.1.3</td>
          <td>MIT</td>
          <td>git://github.com/es-shims/array-includes.git</td>
          <td><a href="http://ljharb.codes">http://ljharb.codes</a></td>
          <td>Jordan Harband</td>
          </tr>
          <tr>
          <td>array-union</td>
          <td>1.0.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/array-union.git">https://github.com/sindresorhus/array-union.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>array-union</td>
          <td>2.1.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/array-union.git">https://github.com/sindresorhus/array-union.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>array-uniq</td>
          <td>1.0.3</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/array-uniq.git">https://github.com/sindresorhus/array-uniq.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>array-unique</td>
          <td>0.3.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/array-unique.git">https://github.com/jonschlinkert/array-unique.git</a></td>
          <td><a href="https://github.com/jonschlinkert/array-unique">https://github.com/jonschlinkert/array-unique</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>array.prototype.flat</td>
          <td>1.2.4</td>
          <td>MIT</td>
          <td>git://github.com/es-shims/Array.prototype.flat.git</td>
          <td><a href="http://ljharb.codes">http://ljharb.codes</a></td>
          <td>Jordan Harband</td>
          </tr>
          <tr>
          <td>arrgv</td>
          <td>1.0.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/astur/arrgv.git">https://github.com/astur/arrgv.git</a></td>
          <td><a href="http://kozlov.am/">http://kozlov.am/</a></td>
          <td>astur</td>
          </tr>
          <tr>
          <td>arrify</td>
          <td>2.0.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/arrify.git">https://github.com/sindresorhus/arrify.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>arrify</td>
          <td>1.0.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/arrify.git">https://github.com/sindresorhus/arrify.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>asn1</td>
          <td>0.2.4</td>
          <td>MIT</td>
          <td>git://github.com/joyent/node-asn1.git</td>
          <td>joyent.com</td>
          <td>Joyent</td>
          </tr>
          <tr>
          <td>asn1.js</td>
          <td>5.4.1</td>
          <td>MIT</td>
          <td>git@github.com:indutny/asn1.js</td>
          <td><a href="https://github.com/indutny/asn1.js">https://github.com/indutny/asn1.js</a></td>
          <td>Fedor Indutny</td>
          </tr>
          <tr>
          <td>assert</td>
          <td>1.5.0</td>
          <td>MIT</td>
          <td>git://github.com/browserify/commonjs-assert.git</td>
          <td><a href="https://github.com/browserify/commonjs-assert">https://github.com/browserify/commonjs-assert</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>assert-plus</td>
          <td>1.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/mcavage/node-assert-plus.git">https://github.com/mcavage/node-assert-plus.git</a></td>
          <td>Unknown</td>
          <td>Mark Cavage</td>
          </tr>
          <tr>
          <td>assign-symbols</td>
          <td>1.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/assign-symbols.git">https://github.com/jonschlinkert/assign-symbols.git</a></td>
          <td><a href="https://github.com/jonschlinkert/assign-symbols">https://github.com/jonschlinkert/assign-symbols</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>astral-regex</td>
          <td>2.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/kevva/astral-regex.git">https://github.com/kevva/astral-regex.git</a></td>
          <td>github.com/kevva</td>
          <td>Kevin Mårtensson</td>
          </tr>
          <tr>
          <td>astral-regex</td>
          <td>1.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/kevva/astral-regex.git">https://github.com/kevva/astral-regex.git</a></td>
          <td>github.com/kevva</td>
          <td>Kevin Mårtensson</td>
          </tr>
          <tr>
          <td>async</td>
          <td>2.6.3</td>
          <td>MIT</td>
          <td><a href="https://github.com/caolan/async.git">https://github.com/caolan/async.git</a></td>
          <td><a href="https://caolan.github.io/async/">https://caolan.github.io/async/</a></td>
          <td>Caolan McMahon</td>
          </tr>
          <tr>
          <td>async-each</td>
          <td>1.0.3</td>
          <td>MIT</td>
          <td>git://github.com/paulmillr/async-each.git</td>
          <td><a href="https://github.com/paulmillr/async-each/">https://github.com/paulmillr/async-each/</a></td>
          <td>Paul Miller</td>
          </tr>
          <tr>
          <td>async-limiter</td>
          <td>1.0.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/strml/async-limiter.git">https://github.com/strml/async-limiter.git</a></td>
          <td>Unknown</td>
          <td>Samuel Reed</td>
          </tr>
          <tr>
          <td>asynckit</td>
          <td>0.4.0</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/alexindigo/asynckit.git">https://github.com/alexindigo/asynckit.git</a></td>
          <td><a href="https://github.com/alexindigo/asynckit#readme">https://github.com/alexindigo/asynckit#readme</a></td>
          <td>Alex Indigo</td>
          </tr>
          <tr>
          <td>autoprefixer</td>
          <td>9.8.6</td>
          <td>MIT</td>
          <td><a href="https://github.com/postcss/autoprefixer.git">https://github.com/postcss/autoprefixer.git</a></td>
          <td>Unknown</td>
          <td>Andrey Sitnik</td>
          </tr>
          <tr>
          <td>ava</td>
          <td>3.15.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/avajs/ava.git">https://github.com/avajs/ava.git</a></td>
          <td><a href="https://avajs.dev/">https://avajs.dev/</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>aws4</td>
          <td>1.11.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/mhart/aws4.git">https://github.com/mhart/aws4.git</a></td>
          <td><a href="https://github.com/mhart">https://github.com/mhart</a></td>
          <td>Michael Hart</td>
          </tr>
          <tr>
          <td>axios</td>
          <td>0.21.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/axios/axios.git">https://github.com/axios/axios.git</a></td>
          <td><a href="https://github.com/axios/axios">https://github.com/axios/axios</a></td>
          <td>Matt Zabriskie</td>
          </tr>
          <tr>
          <td>babel-eslint</td>
          <td>10.1.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel-eslint.git">https://github.com/babel/babel-eslint.git</a></td>
          <td><a href="https://github.com/babel/babel-eslint">https://github.com/babel/babel-eslint</a></td>
          <td>Sebastian McKenzie</td>
          </tr>
          <tr>
          <td>babel-loader</td>
          <td>8.2.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel-loader.git">https://github.com/babel/babel-loader.git</a></td>
          <td><a href="https://github.com/babel/babel-loader">https://github.com/babel/babel-loader</a></td>
          <td>Luis Couto</td>
          </tr>
          <tr>
          <td>babel-plugin-dynamic-import-node</td>
          <td>2.3.3</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/airbnb/babel-plugin-dynamic-import-node.git">https://github.com/airbnb/babel-plugin-dynamic-import-node.git</a></td>
          <td><a href="https://github.com/airbnb/babel-plugin-dynamic-import-node#readme">https://github.com/airbnb/babel-plugin-dynamic-import-node#readme</a></td>
          <td>Jordan Gensler</td>
          </tr>
          <tr>
          <td>babel-plugin-polyfill-corejs2</td>
          <td>0.1.10</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel-polyfills.git">https://github.com/babel/babel-polyfills.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>babel-plugin-polyfill-corejs3</td>
          <td>0.1.7</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel-polyfills.git">https://github.com/babel/babel-polyfills.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>babel-plugin-polyfill-regenerator</td>
          <td>0.1.6</td>
          <td>MIT</td>
          <td><a href="https://github.com/babel/babel-polyfills.git">https://github.com/babel/babel-polyfills.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>balanced-match</td>
          <td>1.0.0</td>
          <td>MIT</td>
          <td>git://github.com/juliangruber/balanced-match.git</td>
          <td><a href="https://github.com/juliangruber/balanced-match">https://github.com/juliangruber/balanced-match</a></td>
          <td>Julian Gruber</td>
          </tr>
          <tr>
          <td>base</td>
          <td>0.11.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/node-base/base.git">https://github.com/node-base/base.git</a></td>
          <td><a href="https://github.com/node-base/base">https://github.com/node-base/base</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>base64-js</td>
          <td>1.5.1</td>
          <td>MIT</td>
          <td>git://github.com/beatgammit/base64-js.git</td>
          <td><a href="https://github.com/beatgammit/base64-js">https://github.com/beatgammit/base64-js</a></td>
          <td>T. Jameson Little</td>
          </tr>
          <tr>
          <td>batch</td>
          <td>0.6.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/visionmedia/batch.git">https://github.com/visionmedia/batch.git</a></td>
          <td>Unknown</td>
          <td>TJ Holowaychuk</td>
          </tr>
          <tr>
          <td>bfj</td>
          <td>6.1.2</td>
          <td>MIT</td>
          <td><a href="https://gitlab.com/philbooth/bfj.git">https://gitlab.com/philbooth/bfj.git</a></td>
          <td><a href="https://gitlab.com/philbooth/bfj">https://gitlab.com/philbooth/bfj</a></td>
          <td>Phil Booth</td>
          </tr>
          <tr>
          <td>big.js</td>
          <td>5.2.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/MikeMcl/big.js.git">https://github.com/MikeMcl/big.js.git</a></td>
          <td>Unknown</td>
          <td>Michael Mclaughlin</td>
          </tr>
          <tr>
          <td>big.js</td>
          <td>3.2.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/MikeMcl/big.js.git">https://github.com/MikeMcl/big.js.git</a></td>
          <td>Unknown</td>
          <td>Michael Mclaughlin</td>
          </tr>
          <tr>
          <td>binary-extensions</td>
          <td>2.2.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/binary-extensions.git">https://github.com/sindresorhus/binary-extensions.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>binary-extensions</td>
          <td>1.13.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/binary-extensions.git">https://github.com/sindresorhus/binary-extensions.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>bindings</td>
          <td>1.5.0</td>
          <td>MIT</td>
          <td>git://github.com/TooTallNate/node-bindings.git</td>
          <td><a href="https://github.com/TooTallNate/node-bindings">https://github.com/TooTallNate/node-bindings</a></td>
          <td>Nathan Rajlich</td>
          </tr>
          <tr>
          <td>bl</td>
          <td>4.1.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/rvagg/bl.git">https://github.com/rvagg/bl.git</a></td>
          <td><a href="https://github.com/rvagg/bl">https://github.com/rvagg/bl</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>bluebird</td>
          <td>3.7.2</td>
          <td>MIT</td>
          <td>git://github.com/petkaantonov/bluebird.git</td>
          <td><a href="https://github.com/petkaantonov/bluebird">https://github.com/petkaantonov/bluebird</a></td>
          <td>Petka Antonov</td>
          </tr>
          <tr>
          <td>blueimp-md5</td>
          <td>2.18.0</td>
          <td>MIT</td>
          <td>git://github.com/blueimp/JavaScript-MD5.git</td>
          <td><a href="https://github.com/blueimp/JavaScript-MD5">https://github.com/blueimp/JavaScript-MD5</a></td>
          <td>Sebastian Tschan</td>
          </tr>
          <tr>
          <td>bn.js</td>
          <td>4.12.0</td>
          <td>MIT</td>
          <td>git@github.com:indutny/bn.js</td>
          <td><a href="https://github.com/indutny/bn.js">https://github.com/indutny/bn.js</a></td>
          <td>Fedor Indutny</td>
          </tr>
          <tr>
          <td>bn.js</td>
          <td>5.2.0</td>
          <td>MIT</td>
          <td>git@github.com:indutny/bn.js</td>
          <td><a href="https://github.com/indutny/bn.js">https://github.com/indutny/bn.js</a></td>
          <td>Fedor Indutny</td>
          </tr>
          <tr>
          <td>body-parser</td>
          <td>1.19.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/expressjs/body-parser.git">https://github.com/expressjs/body-parser.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>bonjour</td>
          <td>3.5.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/watson/bonjour.git">https://github.com/watson/bonjour.git</a></td>
          <td><a href="https://github.com/watson/bonjour">https://github.com/watson/bonjour</a></td>
          <td>Thomas Watson Steen</td>
          </tr>
          <tr>
          <td>boxen</td>
          <td>5.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/boxen.git">https://github.com/sindresorhus/boxen.git</a></td>
          <td><a href="https://sindresorhus.com">https://sindresorhus.com</a></td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>brace-expansion</td>
          <td>1.1.11</td>
          <td>MIT</td>
          <td>git://github.com/juliangruber/brace-expansion.git</td>
          <td><a href="https://github.com/juliangruber/brace-expansion">https://github.com/juliangruber/brace-expansion</a></td>
          <td>Julian Gruber</td>
          </tr>
          <tr>
          <td>braces</td>
          <td>2.3.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/micromatch/braces.git">https://github.com/micromatch/braces.git</a></td>
          <td><a href="https://github.com/micromatch/braces">https://github.com/micromatch/braces</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>braces</td>
          <td>3.0.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/micromatch/braces.git">https://github.com/micromatch/braces.git</a></td>
          <td><a href="https://github.com/micromatch/braces">https://github.com/micromatch/braces</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>brorand</td>
          <td>1.1.0</td>
          <td>MIT</td>
          <td>git@github.com:indutny/brorand</td>
          <td><a href="https://github.com/indutny/brorand">https://github.com/indutny/brorand</a></td>
          <td>Fedor Indutny</td>
          </tr>
          <tr>
          <td>browserify-aes</td>
          <td>1.2.0</td>
          <td>MIT</td>
          <td>git://github.com/crypto-browserify/browserify-aes.git</td>
          <td><a href="https://github.com/crypto-browserify/browserify-aes">https://github.com/crypto-browserify/browserify-aes</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>browserify-cipher</td>
          <td>1.0.1</td>
          <td>MIT</td>
          <td>git@github.com:crypto-browserify/browserify-cipher.git</td>
          <td>Unknown</td>
          <td>Calvin Metcalf</td>
          </tr>
          <tr>
          <td>browserify-des</td>
          <td>1.0.2</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/crypto-browserify/browserify-des.git">https://github.com/crypto-browserify/browserify-des.git</a></td>
          <td><a href="https://github.com/crypto-browserify/browserify-des#readme">https://github.com/crypto-browserify/browserify-des#readme</a></td>
          <td>Calvin Metcalf</td>
          </tr>
          <tr>
          <td>browserify-rsa</td>
          <td>4.1.0</td>
          <td>MIT</td>
          <td><a href="https://github.com:crypto-browserify/browserify-rsa.git">https://github.com:crypto-browserify/browserify-rsa.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>browserify-zlib</td>
          <td>0.2.0</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/devongovett/browserify-zlib.git">https://github.com/devongovett/browserify-zlib.git</a></td>
          <td><a href="https://github.com/devongovett/browserify-zlib">https://github.com/devongovett/browserify-zlib</a></td>
          <td>Devon Govett</td>
          </tr>
          <tr>
          <td>browserslist</td>
          <td>4.16.6</td>
          <td>MIT</td>
          <td><a href="https://github.com/browserslist/browserslist.git">https://github.com/browserslist/browserslist.git</a></td>
          <td>Unknown</td>
          <td>Andrey Sitnik</td>
          </tr>
          <tr>
          <td>buffer</td>
          <td>4.9.2</td>
          <td>MIT</td>
          <td>git://github.com/feross/buffer.git</td>
          <td><a href="https://github.com/feross/buffer">https://github.com/feross/buffer</a></td>
          <td>Feross Aboukhadijeh</td>
          </tr>
          <tr>
          <td>buffer</td>
          <td>5.7.1</td>
          <td>MIT</td>
          <td>git://github.com/feross/buffer.git</td>
          <td><a href="https://github.com/feross/buffer">https://github.com/feross/buffer</a></td>
          <td>Feross Aboukhadijeh</td>
          </tr>
          <tr>
          <td>buffer-crc32</td>
          <td>0.2.13</td>
          <td>MIT</td>
          <td>git://github.com/brianloveswords/buffer-crc32.git</td>
          <td><a href="https://github.com/brianloveswords/buffer-crc32">https://github.com/brianloveswords/buffer-crc32</a></td>
          <td>Brian J. Brennan</td>
          </tr>
          <tr>
          <td>buffer-from</td>
          <td>1.1.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/LinusU/buffer-from.git">https://github.com/LinusU/buffer-from.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>buffer-indexof</td>
          <td>1.1.1</td>
          <td>MIT</td>
          <td>git://github.com/soldair/node-buffer-indexof.git</td>
          <td>Unknown</td>
          <td>Ryan Day</td>
          </tr>
          <tr>
          <td>buffer-json</td>
          <td>2.0.0</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/jprichardson/buffer-json.git">https://github.com/jprichardson/buffer-json.git</a></td>
          <td><a href="https://github.com/jprichardson/buffer-json#readme">https://github.com/jprichardson/buffer-json#readme</a></td>
          <td>JP Richardson</td>
          </tr>
          <tr>
          <td>buffer-xor</td>
          <td>1.0.3</td>
          <td>MIT</td>
          <td><a href="https://github.com/crypto-browserify/buffer-xor.git">https://github.com/crypto-browserify/buffer-xor.git</a></td>
          <td><a href="https://github.com/crypto-browserify/buffer-xor">https://github.com/crypto-browserify/buffer-xor</a></td>
          <td>Daniel Cousens</td>
          </tr>
          <tr>
          <td>builtin-status-codes</td>
          <td>3.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/bendrucker/builtin-status-codes.git">https://github.com/bendrucker/builtin-status-codes.git</a></td>
          <td>bendrucker.me</td>
          <td>Ben Drucker</td>
          </tr>
          <tr>
          <td>bytes</td>
          <td>3.1.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/visionmedia/bytes.js.git">https://github.com/visionmedia/bytes.js.git</a></td>
          <td><a href="http://tjholowaychuk.com">http://tjholowaychuk.com</a></td>
          <td>TJ Holowaychuk</td>
          </tr>
          <tr>
          <td>bytes</td>
          <td>3.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/visionmedia/bytes.js.git">https://github.com/visionmedia/bytes.js.git</a></td>
          <td><a href="http://tjholowaychuk.com">http://tjholowaychuk.com</a></td>
          <td>TJ Holowaychuk</td>
          </tr>
          <tr>
          <td>cache-base</td>
          <td>1.0.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/cache-base.git">https://github.com/jonschlinkert/cache-base.git</a></td>
          <td><a href="https://github.com/jonschlinkert/cache-base">https://github.com/jonschlinkert/cache-base</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>cache-loader</td>
          <td>4.1.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/webpack-contrib/cache-loader.git">https://github.com/webpack-contrib/cache-loader.git</a></td>
          <td><a href="https://github.com/webpack-contrib/cache-loader">https://github.com/webpack-contrib/cache-loader</a></td>
          <td>Tobias Koppers @sokra</td>
          </tr>
          <tr>
          <td>cacheable-request</td>
          <td>6.1.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/lukechilds/cacheable-request.git">https://github.com/lukechilds/cacheable-request.git</a></td>
          <td><a href="http://lukechilds.co.uk">http://lukechilds.co.uk</a></td>
          <td>Luke Childs</td>
          </tr>
          <tr>
          <td>call-bind</td>
          <td>1.0.2</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/ljharb/call-bind.git">https://github.com/ljharb/call-bind.git</a></td>
          <td><a href="https://github.com/ljharb/call-bind#readme">https://github.com/ljharb/call-bind#readme</a></td>
          <td>Jordan Harband</td>
          </tr>
          <tr>
          <td>call-me-maybe</td>
          <td>1.0.1</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/limulus/call-me-maybe.git">https://github.com/limulus/call-me-maybe.git</a></td>
          <td><a href="https://github.com/limulus/call-me-maybe#readme">https://github.com/limulus/call-me-maybe#readme</a></td>
          <td>Eric McCarthy</td>
          </tr>
          <tr>
          <td>caller-callsite</td>
          <td>2.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/caller-callsite.git">https://github.com/sindresorhus/caller-callsite.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>caller-path</td>
          <td>2.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/caller-path.git">https://github.com/sindresorhus/caller-path.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>callsites</td>
          <td>2.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/callsites.git">https://github.com/sindresorhus/callsites.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>callsites</td>
          <td>3.1.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/callsites.git">https://github.com/sindresorhus/callsites.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>camel-case</td>
          <td>3.0.0</td>
          <td>MIT</td>
          <td>git://github.com/blakeembrey/camel-case.git</td>
          <td><a href="https://github.com/blakeembrey/camel-case">https://github.com/blakeembrey/camel-case</a></td>
          <td>Blake Embrey</td>
          </tr>
          <tr>
          <td>camelcase</td>
          <td>6.2.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/camelcase.git">https://github.com/sindresorhus/camelcase.git</a></td>
          <td><a href="https://sindresorhus.com">https://sindresorhus.com</a></td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>camelcase</td>
          <td>5.3.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/camelcase.git">https://github.com/sindresorhus/camelcase.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>caniuse-api</td>
          <td>3.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/nyalab/caniuse-api.git">https://github.com/nyalab/caniuse-api.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>case-sensitive-paths-webpack-plugin</td>
          <td>2.4.0</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/Urthen/case-sensitive-paths-webpack-plugin.git">https://github.com/Urthen/case-sensitive-paths-webpack-plugin.git</a></td>
          <td><a href="https://github.com/Urthen/case-sensitive-paths-webpack-plugin#readme">https://github.com/Urthen/case-sensitive-paths-webpack-plugin#readme</a></td>
          <td>Michael Pratt</td>
          </tr>
          <tr>
          <td>chalk</td>
          <td>2.4.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/chalk/chalk.git">https://github.com/chalk/chalk.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>chalk</td>
          <td>4.1.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/chalk/chalk.git">https://github.com/chalk/chalk.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>chalk</td>
          <td>1.1.3</td>
          <td>MIT</td>
          <td><a href="https://github.com/chalk/chalk.git">https://github.com/chalk/chalk.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>chardet</td>
          <td>0.7.0</td>
          <td>MIT</td>
          <td>git@github.com:runk/node-chardet.git</td>
          <td><a href="https://github.com/runk/node-chardet">https://github.com/runk/node-chardet</a></td>
          <td>Dmitry Shirokov</td>
          </tr>
          <tr>
          <td>check-types</td>
          <td>8.0.3</td>
          <td>MIT</td>
          <td><a href="https://gitlab.com/philbooth/check-types.js.git">https://gitlab.com/philbooth/check-types.js.git</a></td>
          <td><a href="https://gitlab.com/philbooth/check-types.js">https://gitlab.com/philbooth/check-types.js</a></td>
          <td>Phil Booth</td>
          </tr>
          <tr>
          <td>chokidar</td>
          <td>3.5.1</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/paulmillr/chokidar.git">https://github.com/paulmillr/chokidar.git</a></td>
          <td><a href="https://github.com/paulmillr/chokidar">https://github.com/paulmillr/chokidar</a></td>
          <td>Paul Miller</td>
          </tr>
          <tr>
          <td>chokidar</td>
          <td>2.1.8</td>
          <td>MIT</td>
          <td><a href="https://github.com/paulmillr/chokidar.git">https://github.com/paulmillr/chokidar.git</a></td>
          <td><a href="https://github.com/paulmillr/chokidar">https://github.com/paulmillr/chokidar</a></td>
          <td>Paul Miller</td>
          </tr>
          <tr>
          <td>chrome-trace-event</td>
          <td>1.0.2</td>
          <td>MIT</td>
          <td>github.com:samccone/chrome-trace-event</td>
          <td>Unknown</td>
          <td>Trent Mick, Sam Saccone</td>
          </tr>
          <tr>
          <td>chunkd</td>
          <td>2.0.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/jamiebuilds/chunkd.git">https://github.com/jamiebuilds/chunkd.git</a></td>
          <td>Unknown</td>
          <td>Jamie Kyle</td>
          </tr>
          <tr>
          <td>ci-info</td>
          <td>1.6.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/watson/ci-info.git">https://github.com/watson/ci-info.git</a></td>
          <td><a href="https://github.com/watson/ci-info">https://github.com/watson/ci-info</a></td>
          <td>Thomas Watson Steen</td>
          </tr>
          <tr>
          <td>ci-info</td>
          <td>2.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/watson/ci-info.git">https://github.com/watson/ci-info.git</a></td>
          <td><a href="https://github.com/watson/ci-info">https://github.com/watson/ci-info</a></td>
          <td>Thomas Watson Steen</td>
          </tr>
          <tr>
          <td>ci-parallel-vars</td>
          <td>1.0.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/jamiebuilds/ci-parallel-vars">https://github.com/jamiebuilds/ci-parallel-vars</a></td>
          <td>Unknown</td>
          <td>Jamie Kyle</td>
          </tr>
          <tr>
          <td>cipher-base</td>
          <td>1.0.4</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/crypto-browserify/cipher-base.git">https://github.com/crypto-browserify/cipher-base.git</a></td>
          <td><a href="https://github.com/crypto-browserify/cipher-base#readme">https://github.com/crypto-browserify/cipher-base#readme</a></td>
          <td>Calvin Metcalf</td>
          </tr>
          <tr>
          <td>class-utils</td>
          <td>0.3.6</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/class-utils.git">https://github.com/jonschlinkert/class-utils.git</a></td>
          <td><a href="https://github.com/jonschlinkert/class-utils">https://github.com/jonschlinkert/class-utils</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>clean-css</td>
          <td>4.2.3</td>
          <td>MIT</td>
          <td><a href="https://github.com/jakubpawlowicz/clean-css.git">https://github.com/jakubpawlowicz/clean-css.git</a></td>
          <td><a href="https://github.com/jakubpawlowicz/clean-css">https://github.com/jakubpawlowicz/clean-css</a></td>
          <td>Jakub Pawlowicz</td>
          </tr>
          <tr>
          <td>clean-stack</td>
          <td>2.2.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/clean-stack.git">https://github.com/sindresorhus/clean-stack.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>clean-yaml-object</td>
          <td>0.1.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/tapjs/clean-yaml-object.git">https://github.com/tapjs/clean-yaml-object.git</a></td>
          <td>github.com/jamestalmage</td>
          <td>James Talmage</td>
          </tr>
          <tr>
          <td>cli-boxes</td>
          <td>2.2.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/cli-boxes.git">https://github.com/sindresorhus/cli-boxes.git</a></td>
          <td><a href="https://sindresorhus.com">https://sindresorhus.com</a></td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>cli-cursor</td>
          <td>2.1.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/cli-cursor.git">https://github.com/sindresorhus/cli-cursor.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>cli-cursor</td>
          <td>3.1.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/cli-cursor.git">https://github.com/sindresorhus/cli-cursor.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>cli-spinners</td>
          <td>2.5.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/cli-spinners.git">https://github.com/sindresorhus/cli-spinners.git</a></td>
          <td><a href="https://sindresorhus.com">https://sindresorhus.com</a></td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>cli-truncate</td>
          <td>2.1.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/cli-truncate.git">https://github.com/sindresorhus/cli-truncate.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>clipboardy</td>
          <td>2.3.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/clipboardy.git">https://github.com/sindresorhus/clipboardy.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>clone</td>
          <td>1.0.4</td>
          <td>MIT</td>
          <td>git://github.com/pvorb/node-clone.git</td>
          <td><a href="http://paul.vorba.ch/">http://paul.vorba.ch/</a></td>
          <td>Paul Vorbach</td>
          </tr>
          <tr>
          <td>clone-deep</td>
          <td>4.0.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/clone-deep.git">https://github.com/jonschlinkert/clone-deep.git</a></td>
          <td><a href="https://github.com/jonschlinkert/clone-deep">https://github.com/jonschlinkert/clone-deep</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>clone-response</td>
          <td>1.0.2</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/lukechilds/clone-response.git">https://github.com/lukechilds/clone-response.git</a></td>
          <td><a href="https://github.com/lukechilds/clone-response">https://github.com/lukechilds/clone-response</a></td>
          <td>Luke Childs</td>
          </tr>
          <tr>
          <td>coa</td>
          <td>2.0.2</td>
          <td>MIT</td>
          <td>git://github.com/veged/coa.git</td>
          <td><a href="http://github.com/veged/coa">http://github.com/veged/coa</a></td>
          <td>Sergey Berezhnoy</td>
          </tr>
          <tr>
          <td>code-excerpt</td>
          <td>3.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/vadimdemedes/code-excerpt.git">https://github.com/vadimdemedes/code-excerpt.git</a></td>
          <td>github.com/vadimdemedes</td>
          <td>vdemedes</td>
          </tr>
          <tr>
          <td>collection-visit</td>
          <td>1.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/collection-visit.git">https://github.com/jonschlinkert/collection-visit.git</a></td>
          <td><a href="https://github.com/jonschlinkert/collection-visit">https://github.com/jonschlinkert/collection-visit</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>color</td>
          <td>3.1.3</td>
          <td>MIT</td>
          <td><a href="https://github.com/Qix-/color.git">https://github.com/Qix-/color.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>color-convert</td>
          <td>1.9.3</td>
          <td>MIT</td>
          <td><a href="https://github.com/Qix-/color-convert.git">https://github.com/Qix-/color-convert.git</a></td>
          <td>Unknown</td>
          <td>Heather Arthur</td>
          </tr>
          <tr>
          <td>color-convert</td>
          <td>2.0.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/Qix-/color-convert.git">https://github.com/Qix-/color-convert.git</a></td>
          <td>Unknown</td>
          <td>Heather Arthur</td>
          </tr>
          <tr>
          <td>color-name</td>
          <td>1.1.3</td>
          <td>MIT</td>
          <td>git@github.com:dfcreative/color-name.git</td>
          <td><a href="https://github.com/dfcreative/color-name">https://github.com/dfcreative/color-name</a></td>
          <td>DY</td>
          </tr>
          <tr>
          <td>color-name</td>
          <td>1.1.4</td>
          <td>MIT</td>
          <td>git@github.com:colorjs/color-name.git</td>
          <td><a href="https://github.com/colorjs/color-name">https://github.com/colorjs/color-name</a></td>
          <td>DY</td>
          </tr>
          <tr>
          <td>color-string</td>
          <td>1.5.5</td>
          <td>MIT</td>
          <td><a href="https://github.com/Qix-/color-string.git">https://github.com/Qix-/color-string.git</a></td>
          <td>Unknown</td>
          <td>Heather Arthur</td>
          </tr>
          <tr>
          <td>color-string</td>
          <td>1.5.4</td>
          <td>MIT</td>
          <td><a href="https://github.com/Qix-/color-string.git">https://github.com/Qix-/color-string.git</a></td>
          <td>Unknown</td>
          <td>Heather Arthur</td>
          </tr>
          <tr>
          <td>colorette</td>
          <td>1.2.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/jorgebucaran/colorette.git">https://github.com/jorgebucaran/colorette.git</a></td>
          <td>Unknown</td>
          <td>Jorge Bucaran</td>
          </tr>
          <tr>
          <td>combined-stream</td>
          <td>1.0.8</td>
          <td>MIT</td>
          <td>git://github.com/felixge/node-combined-stream.git</td>
          <td><a href="https://github.com/felixge/node-combined-stream">https://github.com/felixge/node-combined-stream</a></td>
          <td>Felix Geisendörfer</td>
          </tr>
          <tr>
          <td>commander</td>
          <td>2.20.3</td>
          <td>MIT</td>
          <td><a href="https://github.com/tj/commander.js.git">https://github.com/tj/commander.js.git</a></td>
          <td>Unknown</td>
          <td>TJ Holowaychuk</td>
          </tr>
          <tr>
          <td>commander</td>
          <td>2.17.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/tj/commander.js.git">https://github.com/tj/commander.js.git</a></td>
          <td>Unknown</td>
          <td>TJ Holowaychuk</td>
          </tr>
          <tr>
          <td>commander</td>
          <td>2.19.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/tj/commander.js.git">https://github.com/tj/commander.js.git</a></td>
          <td>Unknown</td>
          <td>TJ Holowaychuk</td>
          </tr>
          <tr>
          <td>commondir</td>
          <td>1.0.1</td>
          <td>MIT</td>
          <td><a href="http://github.com/substack/node-commondir.git">http://github.com/substack/node-commondir.git</a></td>
          <td><a href="http://substack.net">http://substack.net</a></td>
          <td>James Halliday</td>
          </tr>
          <tr>
          <td>component-emitter</td>
          <td>1.3.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/component/emitter.git">https://github.com/component/emitter.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>compressible</td>
          <td>2.0.18</td>
          <td>MIT</td>
          <td><a href="https://github.com/jshttp/compressible.git">https://github.com/jshttp/compressible.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>compression</td>
          <td>1.7.4</td>
          <td>MIT</td>
          <td><a href="https://github.com/expressjs/compression.git">https://github.com/expressjs/compression.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>concat-map</td>
          <td>0.0.1</td>
          <td>MIT</td>
          <td>git://github.com/substack/node-concat-map.git</td>
          <td><a href="http://substack.net">http://substack.net</a></td>
          <td>James Halliday</td>
          </tr>
          <tr>
          <td>concat-stream</td>
          <td>1.6.2</td>
          <td>MIT</td>
          <td><a href="http://github.com/maxogden/concat-stream.git">http://github.com/maxogden/concat-stream.git</a></td>
          <td>Unknown</td>
          <td>Max Ogden</td>
          </tr>
          <tr>
          <td>condense-newlines</td>
          <td>0.2.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/condense-newlines.git">https://github.com/jonschlinkert/condense-newlines.git</a></td>
          <td><a href="https://github.com/jonschlinkert/condense-newlines">https://github.com/jonschlinkert/condense-newlines</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>config-chain</td>
          <td>1.1.12</td>
          <td>MIT</td>
          <td><a href="https://github.com/dominictarr/config-chain.git">https://github.com/dominictarr/config-chain.git</a></td>
          <td><a href="http://github.com/dominictarr/config-chain">http://github.com/dominictarr/config-chain</a></td>
          <td>Dominic Tarr</td>
          </tr>
          <tr>
          <td>confusing-browser-globals</td>
          <td>1.0.10</td>
          <td>MIT</td>
          <td><a href="https://github.com/facebook/create-react-app.git">https://github.com/facebook/create-react-app.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>connect-history-api-fallback</td>
          <td>1.6.0</td>
          <td>MIT</td>
          <td><a href="http://github.com/bripkens/connect-history-api-fallback.git">http://github.com/bripkens/connect-history-api-fallback.git</a></td>
          <td><a href="http://bripkens.de">http://bripkens.de</a></td>
          <td>Ben Ripkens</td>
          </tr>
          <tr>
          <td>console-browserify</td>
          <td>1.2.0</td>
          <td>MIT</td>
          <td>git://github.com/browserify/console-browserify.git</td>
          <td><a href="https://github.com/browserify/console-browserify">https://github.com/browserify/console-browserify</a></td>
          <td>Raynos</td>
          </tr>
          <tr>
          <td>consolidate</td>
          <td>0.15.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/tj/consolidate.js.git">https://github.com/tj/consolidate.js.git</a></td>
          <td><a href="https://github.com/tj/consolidate.js">https://github.com/tj/consolidate.js</a></td>
          <td>TJ Holowaychuk</td>
          </tr>
          <tr>
          <td>constants-browserify</td>
          <td>1.0.0</td>
          <td>MIT</td>
          <td>git://github.com/juliangruber/constants-browserify.git</td>
          <td><a href="https://github.com/juliangruber/constants-browserify">https://github.com/juliangruber/constants-browserify</a></td>
          <td>Julian Gruber</td>
          </tr>
          <tr>
          <td>contains-path</td>
          <td>0.1.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/contains-path.git">https://github.com/jonschlinkert/contains-path.git</a></td>
          <td><a href="https://github.com/jonschlinkert/contains-path">https://github.com/jonschlinkert/contains-path</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>content-disposition</td>
          <td>0.5.3</td>
          <td>MIT</td>
          <td><a href="https://github.com/jshttp/content-disposition.git">https://github.com/jshttp/content-disposition.git</a></td>
          <td>Unknown</td>
          <td>Douglas Christopher Wilson</td>
          </tr>
          <tr>
          <td>content-type</td>
          <td>1.0.4</td>
          <td>MIT</td>
          <td><a href="https://github.com/jshttp/content-type.git">https://github.com/jshttp/content-type.git</a></td>
          <td>Unknown</td>
          <td>Douglas Christopher Wilson</td>
          </tr>
          <tr>
          <td>convert-source-map</td>
          <td>1.7.0</td>
          <td>MIT</td>
          <td>git://github.com/thlorenz/convert-source-map.git</td>
          <td><a href="https://github.com/thlorenz/convert-source-map">https://github.com/thlorenz/convert-source-map</a></td>
          <td>Thorsten Lorenz</td>
          </tr>
          <tr>
          <td>convert-to-spaces</td>
          <td>1.0.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/vadimdemedes/convert-to-spaces.git">https://github.com/vadimdemedes/convert-to-spaces.git</a></td>
          <td>Unknown</td>
          <td>Vadim Demedes</td>
          </tr>
          <tr>
          <td>cookie</td>
          <td>0.4.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/jshttp/cookie.git">https://github.com/jshttp/cookie.git</a></td>
          <td>Unknown</td>
          <td>Roman Shtylman</td>
          </tr>
          <tr>
          <td>cookie-signature</td>
          <td>1.0.6</td>
          <td>MIT</td>
          <td><a href="https://github.com/visionmedia/node-cookie-signature.git">https://github.com/visionmedia/node-cookie-signature.git</a></td>
          <td>Unknown</td>
          <td>TJ Holowaychuk</td>
          </tr>
          <tr>
          <td>copy-descriptor</td>
          <td>0.1.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/copy-descriptor.git">https://github.com/jonschlinkert/copy-descriptor.git</a></td>
          <td><a href="https://github.com/jonschlinkert/copy-descriptor">https://github.com/jonschlinkert/copy-descriptor</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>copy-webpack-plugin</td>
          <td>5.1.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/webpack-contrib/copy-webpack-plugin.git">https://github.com/webpack-contrib/copy-webpack-plugin.git</a></td>
          <td><a href="https://github.com/webpack-contrib/copy-webpack-plugin">https://github.com/webpack-contrib/copy-webpack-plugin</a></td>
          <td>Len Boyette</td>
          </tr>
          <tr>
          <td>core-js</td>
          <td>3.9.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/zloirock/core-js.git">https://github.com/zloirock/core-js.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>core-js-compat</td>
          <td>3.9.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/zloirock/core-js.git">https://github.com/zloirock/core-js.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>core-util-is</td>
          <td>1.0.2</td>
          <td>MIT</td>
          <td>git://github.com/isaacs/core-util-is</td>
          <td><a href="http://blog.izs.me/">http://blog.izs.me/</a></td>
          <td>Isaac Z. Schlueter</td>
          </tr>
          <tr>
          <td>cors</td>
          <td>2.8.5</td>
          <td>MIT</td>
          <td><a href="https://github.com/expressjs/cors.git">https://github.com/expressjs/cors.git</a></td>
          <td><a href="https://github.com/troygoode/">https://github.com/troygoode/</a></td>
          <td>Troy Goode</td>
          </tr>
          <tr>
          <td>cosmiconfig</td>
          <td>5.2.1</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/davidtheclark/cosmiconfig.git">https://github.com/davidtheclark/cosmiconfig.git</a></td>
          <td><a href="https://github.com/davidtheclark/cosmiconfig#readme">https://github.com/davidtheclark/cosmiconfig#readme</a></td>
          <td>David Clark</td>
          </tr>
          <tr>
          <td>create-ecdh</td>
          <td>4.0.4</td>
          <td>MIT</td>
          <td><a href="https://github.com/crypto-browserify/createECDH.git">https://github.com/crypto-browserify/createECDH.git</a></td>
          <td><a href="https://github.com/crypto-browserify/createECDH">https://github.com/crypto-browserify/createECDH</a></td>
          <td>Calvin Metcalf</td>
          </tr>
          <tr>
          <td>create-hash</td>
          <td>1.2.0</td>
          <td>MIT</td>
          <td>git@github.com:crypto-browserify/createHash.git</td>
          <td><a href="https://github.com/crypto-browserify/createHash">https://github.com/crypto-browserify/createHash</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>create-hmac</td>
          <td>1.1.7</td>
          <td>MIT</td>
          <td><a href="https://github.com/crypto-browserify/createHmac.git">https://github.com/crypto-browserify/createHmac.git</a></td>
          <td><a href="https://github.com/crypto-browserify/createHmac">https://github.com/crypto-browserify/createHmac</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>cross-spawn</td>
          <td>6.0.5</td>
          <td>MIT</td>
          <td>git@github.com:moxystudio/node-cross-spawn.git</td>
          <td><a href="https://github.com/moxystudio/node-cross-spawn">https://github.com/moxystudio/node-cross-spawn</a></td>
          <td>André Cruz</td>
          </tr>
          <tr>
          <td>cross-spawn</td>
          <td>5.1.0</td>
          <td>MIT</td>
          <td>git://github.com/IndigoUnited/node-cross-spawn.git</td>
          <td><a href="http://indigounited.com">http://indigounited.com</a></td>
          <td>IndigoUnited</td>
          </tr>
          <tr>
          <td>cross-spawn</td>
          <td>7.0.3</td>
          <td>MIT</td>
          <td>git@github.com:moxystudio/node-cross-spawn.git</td>
          <td><a href="https://github.com/moxystudio/node-cross-spawn">https://github.com/moxystudio/node-cross-spawn</a></td>
          <td>André Cruz</td>
          </tr>
          <tr>
          <td>crypto-browserify</td>
          <td>3.12.0</td>
          <td>MIT</td>
          <td>git://github.com/crypto-browserify/crypto-browserify.git</td>
          <td><a href="https://github.com/crypto-browserify/crypto-browserify">https://github.com/crypto-browserify/crypto-browserify</a></td>
          <td>Dominic Tarr</td>
          </tr>
          <tr>
          <td>crypto-random-string</td>
          <td>2.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/crypto-random-string.git">https://github.com/sindresorhus/crypto-random-string.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>css-color-names</td>
          <td>0.0.4</td>
          <td>MIT</td>
          <td>git://github.com/bahamas10/css-color-names.git</td>
          <td><a href="http://www.daveeddy.com">http://www.daveeddy.com</a></td>
          <td>Dave Eddy</td>
          </tr>
          <tr>
          <td>css-declaration-sorter</td>
          <td>4.0.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/Siilwyn/css-declaration-sorter.git">https://github.com/Siilwyn/css-declaration-sorter.git</a></td>
          <td><a href="https://selwyn.cc/">https://selwyn.cc/</a></td>
          <td>Selwyn</td>
          </tr>
          <tr>
          <td>css-loader</td>
          <td>3.6.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/webpack-contrib/css-loader.git">https://github.com/webpack-contrib/css-loader.git</a></td>
          <td><a href="https://github.com/webpack-contrib/css-loader">https://github.com/webpack-contrib/css-loader</a></td>
          <td>Tobias Koppers @sokra</td>
          </tr>
          <tr>
          <td>css-select-base-adapter</td>
          <td>0.1.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/nrkn/css-select-base-adapter.git">https://github.com/nrkn/css-select-base-adapter.git</a></td>
          <td><a href="https://github.com/nrkn/css-select-base-adapter#readme">https://github.com/nrkn/css-select-base-adapter#readme</a></td>
          <td>Nik Coughlin</td>
          </tr>
          <tr>
          <td>css-selector-tokenizer</td>
          <td>0.7.3</td>
          <td>MIT</td>
          <td><a href="https://github.com/css-modules/css-selector-tokenizer.git">https://github.com/css-modules/css-selector-tokenizer.git</a></td>
          <td><a href="https://github.com/css-modules/css-selector-tokenizer">https://github.com/css-modules/css-selector-tokenizer</a></td>
          <td>Tobias Koppers @sokra</td>
          </tr>
          <tr>
          <td>css-tree</td>
          <td>1.0.0-alpha.37</td>
          <td>MIT</td>
          <td><a href="https://github.com/csstree/csstree.git">https://github.com/csstree/csstree.git</a></td>
          <td><a href="https://github.com/lahmatiy">https://github.com/lahmatiy</a></td>
          <td>Roman Dvornov</td>
          </tr>
          <tr>
          <td>css-tree</td>
          <td>1.1.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/csstree/csstree.git">https://github.com/csstree/csstree.git</a></td>
          <td><a href="https://github.com/lahmatiy">https://github.com/lahmatiy</a></td>
          <td>Roman Dvornov</td>
          </tr>
          <tr>
          <td>cssesc</td>
          <td>3.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/mathiasbynens/cssesc.git">https://github.com/mathiasbynens/cssesc.git</a></td>
          <td><a href="https://mths.be/cssesc">https://mths.be/cssesc</a></td>
          <td>Mathias Bynens</td>
          </tr>
          <tr>
          <td>cssesc</td>
          <td>2.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/mathiasbynens/cssesc.git">https://github.com/mathiasbynens/cssesc.git</a></td>
          <td><a href="https://mths.be/cssesc">https://mths.be/cssesc</a></td>
          <td>Mathias Bynens</td>
          </tr>
          <tr>
          <td>cssnano</td>
          <td>4.1.10</td>
          <td>MIT</td>
          <td><a href="https://github.com/cssnano/cssnano.git">https://github.com/cssnano/cssnano.git</a></td>
          <td><a href="https://github.com/cssnano/cssnano">https://github.com/cssnano/cssnano</a></td>
          <td>Ben Briggs</td>
          </tr>
          <tr>
          <td>cssnano-preset-default</td>
          <td>4.0.7</td>
          <td>MIT</td>
          <td><a href="https://github.com/cssnano/cssnano.git">https://github.com/cssnano/cssnano.git</a></td>
          <td><a href="https://github.com/cssnano/cssnano">https://github.com/cssnano/cssnano</a></td>
          <td>Ben Briggs</td>
          </tr>
          <tr>
          <td>cssnano-util-get-arguments</td>
          <td>4.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/cssnano/cssnano.git">https://github.com/cssnano/cssnano.git</a></td>
          <td><a href="https://github.com/cssnano/cssnano">https://github.com/cssnano/cssnano</a></td>
          <td>Ben Briggs</td>
          </tr>
          <tr>
          <td>cssnano-util-get-match</td>
          <td>4.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/cssnano/cssnano.git">https://github.com/cssnano/cssnano.git</a></td>
          <td><a href="https://github.com/cssnano/cssnano">https://github.com/cssnano/cssnano</a></td>
          <td>Ben Briggs</td>
          </tr>
          <tr>
          <td>cssnano-util-raw-cache</td>
          <td>4.0.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/cssnano/cssnano.git">https://github.com/cssnano/cssnano.git</a></td>
          <td><a href="https://github.com/cssnano/cssnano">https://github.com/cssnano/cssnano</a></td>
          <td>Ben Briggs</td>
          </tr>
          <tr>
          <td>cssnano-util-same-parent</td>
          <td>4.0.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/cssnano/cssnano.git">https://github.com/cssnano/cssnano.git</a></td>
          <td><a href="https://github.com/cssnano/cssnano">https://github.com/cssnano/cssnano</a></td>
          <td>Ben Briggs</td>
          </tr>
          <tr>
          <td>csso</td>
          <td>4.2.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/css/csso.git">https://github.com/css/csso.git</a></td>
          <td><a href="https://github.com/css/csso">https://github.com/css/csso</a></td>
          <td>Sergey Kryzhanovsky</td>
          </tr>
          <tr>
          <td>cssom</td>
          <td>0.4.4</td>
          <td>MIT</td>
          <td><a href="https://github.com/NV/CSSOM.git">https://github.com/NV/CSSOM.git</a></td>
          <td>Unknown</td>
          <td>Nikita Vasilyev</td>
          </tr>
          <tr>
          <td>cssom</td>
          <td>0.3.8</td>
          <td>MIT</td>
          <td><a href="https://github.com/NV/CSSOM.git">https://github.com/NV/CSSOM.git</a></td>
          <td>Unknown</td>
          <td>Nikita Vasilyev</td>
          </tr>
          <tr>
          <td>cssstyle</td>
          <td>2.3.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/jsdom/cssstyle.git">https://github.com/jsdom/cssstyle.git</a></td>
          <td><a href="https://github.com/jsdom/cssstyle">https://github.com/jsdom/cssstyle</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>currently-unhandled</td>
          <td>0.4.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/jamestalmage/currently-unhandled.git">https://github.com/jamestalmage/currently-unhandled.git</a></td>
          <td>github.com/jamestalmage</td>
          <td>James Talmage</td>
          </tr>
          <tr>
          <td>cyclist</td>
          <td>1.0.1</td>
          <td>MIT</td>
          <td>git://github.com/mafintosh/cyclist</td>
          <td><a href="https://github.com/mafintosh/cyclist">https://github.com/mafintosh/cyclist</a></td>
          <td>Mathias Buus Madsen</td>
          </tr>
          <tr>
          <td>dashdash</td>
          <td>1.14.1</td>
          <td>MIT</td>
          <td>git://github.com/trentm/node-dashdash.git</td>
          <td><a href="http://trentm.com">http://trentm.com</a></td>
          <td>Trent Mick</td>
          </tr>
          <tr>
          <td>data-urls</td>
          <td>2.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/jsdom/data-urls.git">https://github.com/jsdom/data-urls.git</a></td>
          <td><a href="https://domenic.me/">https://domenic.me/</a></td>
          <td>Domenic Denicola</td>
          </tr>
          <tr>
          <td>date-time</td>
          <td>3.1.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/date-time.git">https://github.com/sindresorhus/date-time.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>de-indent</td>
          <td>1.0.2</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/yyx990803/de-indent.git">https://github.com/yyx990803/de-indent.git</a></td>
          <td><a href="https://github.com/yyx990803/de-indent#readme">https://github.com/yyx990803/de-indent#readme</a></td>
          <td>Evan You</td>
          </tr>
          <tr>
          <td>debug</td>
          <td>2.6.9</td>
          <td>MIT</td>
          <td>git://github.com/visionmedia/debug.git</td>
          <td>Unknown</td>
          <td>TJ Holowaychuk</td>
          </tr>
          <tr>
          <td>debug</td>
          <td>4.3.1</td>
          <td>MIT</td>
          <td>git://github.com/visionmedia/debug.git</td>
          <td>Unknown</td>
          <td>TJ Holowaychuk</td>
          </tr>
          <tr>
          <td>debug</td>
          <td>3.2.7</td>
          <td>MIT</td>
          <td>git://github.com/visionmedia/debug.git</td>
          <td>Unknown</td>
          <td>TJ Holowaychuk</td>
          </tr>
          <tr>
          <td>decache</td>
          <td>4.6.0</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/dwyl/decache.git">https://github.com/dwyl/decache.git</a></td>
          <td><a href="https://github.com/dwyl/decache#readme">https://github.com/dwyl/decache#readme</a></td>
          <td><a href="https://github.com/dwyl/decache/graphs/contributors">https://github.com/dwyl/decache/graphs/contributors</a></td>
          </tr>
          <tr>
          <td>decamelize</td>
          <td>1.2.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/decamelize.git">https://github.com/sindresorhus/decamelize.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>decimal.js</td>
          <td>10.2.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/MikeMcl/decimal.js.git">https://github.com/MikeMcl/decimal.js.git</a></td>
          <td>Unknown</td>
          <td>Michael Mclaughlin</td>
          </tr>
          <tr>
          <td>decode-uri-component</td>
          <td>0.2.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/SamVerschueren/decode-uri-component.git">https://github.com/SamVerschueren/decode-uri-component.git</a></td>
          <td>github.com/SamVerschueren</td>
          <td>Sam Verschueren</td>
          </tr>
          <tr>
          <td>decompress-response</td>
          <td>3.3.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/decompress-response.git">https://github.com/sindresorhus/decompress-response.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>deep-equal</td>
          <td>1.1.1</td>
          <td>MIT</td>
          <td><a href="http://github.com/substack/node-deep-equal.git">http://github.com/substack/node-deep-equal.git</a></td>
          <td><a href="http://substack.net">http://substack.net</a></td>
          <td>James Halliday</td>
          </tr>
          <tr>
          <td>deep-extend</td>
          <td>0.6.0</td>
          <td>MIT</td>
          <td>git://github.com/unclechu/node-deep-extend.git</td>
          <td><a href="https://github.com/unclechu/node-deep-extend">https://github.com/unclechu/node-deep-extend</a></td>
          <td>Viacheslav Lotsmanov</td>
          </tr>
          <tr>
          <td>deep-is</td>
          <td>0.1.3</td>
          <td>MIT</td>
          <td><a href="http://github.com/thlorenz/deep-is.git">http://github.com/thlorenz/deep-is.git</a></td>
          <td><a href="http://thlorenz.com">http://thlorenz.com</a></td>
          <td>Thorsten Lorenz</td>
          </tr>
          <tr>
          <td>deepmerge</td>
          <td>1.5.2</td>
          <td>MIT</td>
          <td>git://github.com/KyleAMathews/deepmerge.git</td>
          <td><a href="https://github.com/KyleAMathews/deepmerge">https://github.com/KyleAMathews/deepmerge</a></td>
          <td>Nick Fisher</td>
          </tr>
          <tr>
          <td>defaults</td>
          <td>1.0.3</td>
          <td>MIT</td>
          <td>git://github.com/tmpvar/defaults.git</td>
          <td>Unknown</td>
          <td>Elijah Insua</td>
          </tr>
          <tr>
          <td>defer-to-connect</td>
          <td>1.1.3</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/szmarczak/defer-to-connect.git">https://github.com/szmarczak/defer-to-connect.git</a></td>
          <td><a href="https://github.com/szmarczak/defer-to-connect#readme">https://github.com/szmarczak/defer-to-connect#readme</a></td>
          <td>Szymon Marczak</td>
          </tr>
          <tr>
          <td>define-properties</td>
          <td>1.1.3</td>
          <td>MIT</td>
          <td>git://github.com/ljharb/define-properties.git</td>
          <td>Unknown</td>
          <td>Jordan Harband</td>
          </tr>
          <tr>
          <td>define-property</td>
          <td>2.0.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/define-property.git">https://github.com/jonschlinkert/define-property.git</a></td>
          <td><a href="https://github.com/jonschlinkert/define-property">https://github.com/jonschlinkert/define-property</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>define-property</td>
          <td>1.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/define-property.git">https://github.com/jonschlinkert/define-property.git</a></td>
          <td><a href="https://github.com/jonschlinkert/define-property">https://github.com/jonschlinkert/define-property</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>define-property</td>
          <td>0.2.5</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/define-property.git">https://github.com/jonschlinkert/define-property.git</a></td>
          <td><a href="https://github.com/jonschlinkert/define-property">https://github.com/jonschlinkert/define-property</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>del</td>
          <td>4.1.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/del.git">https://github.com/sindresorhus/del.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>del</td>
          <td>6.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/del.git">https://github.com/sindresorhus/del.git</a></td>
          <td><a href="https://sindresorhus.com">https://sindresorhus.com</a></td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>delayed-stream</td>
          <td>1.0.0</td>
          <td>MIT</td>
          <td>git://github.com/felixge/node-delayed-stream.git</td>
          <td><a href="https://github.com/felixge/node-delayed-stream">https://github.com/felixge/node-delayed-stream</a></td>
          <td>Felix Geisendörfer</td>
          </tr>
          <tr>
          <td>depd</td>
          <td>1.1.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/dougwilson/nodejs-depd.git">https://github.com/dougwilson/nodejs-depd.git</a></td>
          <td>Unknown</td>
          <td>Douglas Christopher Wilson</td>
          </tr>
          <tr>
          <td>des.js</td>
          <td>1.0.1</td>
          <td>MIT</td>
          <td>git+ssh://git@github.com/indutny/des.js.git</td>
          <td><a href="https://github.com/indutny/des.js#readme">https://github.com/indutny/des.js#readme</a></td>
          <td>Fedor Indutny</td>
          </tr>
          <tr>
          <td>destroy</td>
          <td>1.0.4</td>
          <td>MIT</td>
          <td><a href="https://github.com/stream-utils/destroy.git">https://github.com/stream-utils/destroy.git</a></td>
          <td><a href="http://jongleberry.com">http://jongleberry.com</a></td>
          <td>Jonathan Ong</td>
          </tr>
          <tr>
          <td>diffie-hellman</td>
          <td>5.0.3</td>
          <td>MIT</td>
          <td><a href="https://github.com/crypto-browserify/diffie-hellman.git">https://github.com/crypto-browserify/diffie-hellman.git</a></td>
          <td><a href="https://github.com/crypto-browserify/diffie-hellman">https://github.com/crypto-browserify/diffie-hellman</a></td>
          <td>Calvin Metcalf</td>
          </tr>
          <tr>
          <td>dir-glob</td>
          <td>2.2.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/kevva/dir-glob.git">https://github.com/kevva/dir-glob.git</a></td>
          <td>github.com/kevva</td>
          <td>Kevin Mårtensson</td>
          </tr>
          <tr>
          <td>dir-glob</td>
          <td>3.0.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/kevva/dir-glob.git">https://github.com/kevva/dir-glob.git</a></td>
          <td>github.com/kevva</td>
          <td>Kevin Mårtensson</td>
          </tr>
          <tr>
          <td>dns-equal</td>
          <td>1.0.0</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/watson/dns-equal.git">https://github.com/watson/dns-equal.git</a></td>
          <td><a href="https://github.com/watson/dns-equal#readme">https://github.com/watson/dns-equal#readme</a></td>
          <td>Thomas Watson Steen</td>
          </tr>
          <tr>
          <td>dns-packet</td>
          <td>1.3.4</td>
          <td>MIT</td>
          <td><a href="https://github.com/mafintosh/dns-packet">https://github.com/mafintosh/dns-packet</a></td>
          <td><a href="https://github.com/mafintosh/dns-packet">https://github.com/mafintosh/dns-packet</a></td>
          <td>Mathias Buus</td>
          </tr>
          <tr>
          <td>dns-txt</td>
          <td>2.0.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/watson/dns-txt.git">https://github.com/watson/dns-txt.git</a></td>
          <td><a href="https://github.com/watson/dns-txt">https://github.com/watson/dns-txt</a></td>
          <td>Thomas Watson Steen</td>
          </tr>
          <tr>
          <td>dom-converter</td>
          <td>0.2.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/AriaMinaei/dom-converter">https://github.com/AriaMinaei/dom-converter</a></td>
          <td>Unknown</td>
          <td>Aria Minaei</td>
          </tr>
          <tr>
          <td>dom-event-types</td>
          <td>1.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/eddyerburgh/dom-event-types">https://github.com/eddyerburgh/dom-event-types</a></td>
          <td>Unknown</td>
          <td>Edd Yerburgh</td>
          </tr>
          <tr>
          <td>dom-serializer</td>
          <td>0.2.2</td>
          <td>MIT</td>
          <td>git://github.com/cheeriojs/dom-renderer.git</td>
          <td>Unknown</td>
          <td>Felix Boehm</td>
          </tr>
          <tr>
          <td>domain-browser</td>
          <td>1.2.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/bevry/domain-browser.git">https://github.com/bevry/domain-browser.git</a></td>
          <td><a href="https://github.com/bevry/domain-browser">https://github.com/bevry/domain-browser</a></td>
          <td>2013+ Bevry Pty Ltd</td>
          </tr>
          <tr>
          <td>domexception</td>
          <td>2.0.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/jsdom/domexception.git">https://github.com/jsdom/domexception.git</a></td>
          <td><a href="https://domenic.me/">https://domenic.me/</a></td>
          <td>Domenic Denicola</td>
          </tr>
          <tr>
          <td>dot-prop</td>
          <td>5.3.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/dot-prop.git">https://github.com/sindresorhus/dot-prop.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>duplexer</td>
          <td>0.1.2</td>
          <td>MIT</td>
          <td>git://github.com/Raynos/duplexer.git</td>
          <td><a href="https://github.com/Raynos/duplexer">https://github.com/Raynos/duplexer</a></td>
          <td>Raynos</td>
          </tr>
          <tr>
          <td>duplexify</td>
          <td>3.7.1</td>
          <td>MIT</td>
          <td>git://github.com/mafintosh/duplexify</td>
          <td><a href="https://github.com/mafintosh/duplexify">https://github.com/mafintosh/duplexify</a></td>
          <td>Mathias Buus</td>
          </tr>
          <tr>
          <td>easy-stack</td>
          <td>1.0.1</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/RIAEvangelist/easy-stack.git">https://github.com/RIAEvangelist/easy-stack.git</a></td>
          <td><a href="https://github.com/RIAEvangelist/easy-stack#readme">https://github.com/RIAEvangelist/easy-stack#readme</a></td>
          <td>Brandon Nozaki Miller</td>
          </tr>
          <tr>
          <td>ecc-jsbn</td>
          <td>0.1.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/quartzjer/ecc-jsbn.git">https://github.com/quartzjer/ecc-jsbn.git</a></td>
          <td><a href="https://github.com/quartzjer/ecc-jsbn">https://github.com/quartzjer/ecc-jsbn</a></td>
          <td>Jeremie Miller</td>
          </tr>
          <tr>
          <td>editorconfig</td>
          <td>0.15.3</td>
          <td>MIT</td>
          <td>git://github.com/editorconfig/editorconfig-core-js.git</td>
          <td>Unknown</td>
          <td>EditorConfig Team</td>
          </tr>
          <tr>
          <td>ee-first</td>
          <td>1.1.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonathanong/ee-first.git">https://github.com/jonathanong/ee-first.git</a></td>
          <td><a href="http://jongleberry.com">http://jongleberry.com</a></td>
          <td>Jonathan Ong</td>
          </tr>
          <tr>
          <td>elliptic</td>
          <td>6.5.4</td>
          <td>MIT</td>
          <td>git@github.com:indutny/elliptic</td>
          <td><a href="https://github.com/indutny/elliptic">https://github.com/indutny/elliptic</a></td>
          <td>Fedor Indutny</td>
          </tr>
          <tr>
          <td>emittery</td>
          <td>0.8.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/emittery.git">https://github.com/sindresorhus/emittery.git</a></td>
          <td><a href="https://sindresorhus.com">https://sindresorhus.com</a></td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>emoji-regex</td>
          <td>8.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/mathiasbynens/emoji-regex.git">https://github.com/mathiasbynens/emoji-regex.git</a></td>
          <td><a href="https://mths.be/emoji-regex">https://mths.be/emoji-regex</a></td>
          <td>Mathias Bynens</td>
          </tr>
          <tr>
          <td>emoji-regex</td>
          <td>7.0.3</td>
          <td>MIT</td>
          <td><a href="https://github.com/mathiasbynens/emoji-regex.git">https://github.com/mathiasbynens/emoji-regex.git</a></td>
          <td><a href="https://mths.be/emoji-regex">https://mths.be/emoji-regex</a></td>
          <td>Mathias Bynens</td>
          </tr>
          <tr>
          <td>emojis-list</td>
          <td>3.0.0</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/kikobeats/emojis-list.git">https://github.com/kikobeats/emojis-list.git</a></td>
          <td><a href="https://nidecoc.io/Kikobeats/emojis-list">https://nidecoc.io/Kikobeats/emojis-list</a></td>
          <td>Kiko Beats</td>
          </tr>
          <tr>
          <td>emojis-list</td>
          <td>2.1.0</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/kikobeats/emojis-list.git">https://github.com/kikobeats/emojis-list.git</a></td>
          <td><a href="https://github.com/Kikobeats/emojis-list">https://github.com/Kikobeats/emojis-list</a></td>
          <td>Kiko Beats</td>
          </tr>
          <tr>
          <td>encodeurl</td>
          <td>1.0.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/pillarjs/encodeurl.git">https://github.com/pillarjs/encodeurl.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>end-of-stream</td>
          <td>1.4.4</td>
          <td>MIT</td>
          <td>git://github.com/mafintosh/end-of-stream.git</td>
          <td><a href="https://github.com/mafintosh/end-of-stream">https://github.com/mafintosh/end-of-stream</a></td>
          <td>Mathias Buus</td>
          </tr>
          <tr>
          <td>enhanced-resolve</td>
          <td>4.5.0</td>
          <td>MIT</td>
          <td>git://github.com/webpack/enhanced-resolve.git</td>
          <td><a href="http://github.com/webpack/enhanced-resolve">http://github.com/webpack/enhanced-resolve</a></td>
          <td>Tobias Koppers @sokra</td>
          </tr>
          <tr>
          <td>enhanced-resolve</td>
          <td>0.9.1</td>
          <td>MIT</td>
          <td>git://github.com/webpack/enhanced-resolve.git</td>
          <td><a href="http://github.com/webpack/enhanced-resolve">http://github.com/webpack/enhanced-resolve</a></td>
          <td>Tobias Koppers @sokra</td>
          </tr>
          <tr>
          <td>equal-length</td>
          <td>1.0.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/vadimdemedes/equal-length.git">https://github.com/vadimdemedes/equal-length.git</a></td>
          <td>github.com/vadimdemedes</td>
          <td>vdemedes</td>
          </tr>
          <tr>
          <td>errno</td>
          <td>0.1.8</td>
          <td>MIT</td>
          <td><a href="https://github.com/rvagg/node-errno.git">https://github.com/rvagg/node-errno.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>error-ex</td>
          <td>1.3.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/qix-/node-error-ex.git">https://github.com/qix-/node-error-ex.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>error-stack-parser</td>
          <td>2.0.6</td>
          <td>MIT</td>
          <td>git://github.com/stacktracejs/error-stack-parser.git</td>
          <td><a href="https://www.stacktracejs.com/">https://www.stacktracejs.com/</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>es-abstract</td>
          <td>1.18.0-next.3</td>
          <td>MIT</td>
          <td>git://github.com/ljharb/es-abstract.git</td>
          <td><a href="http://ljharb.codes">http://ljharb.codes</a></td>
          <td>Jordan Harband</td>
          </tr>
          <tr>
          <td>es-abstract</td>
          <td>1.17.7</td>
          <td>MIT</td>
          <td>git://github.com/ljharb/es-abstract.git</td>
          <td><a href="http://ljharb.codes">http://ljharb.codes</a></td>
          <td>Jordan Harband</td>
          </tr>
          <tr>
          <td>es-to-primitive</td>
          <td>1.2.1</td>
          <td>MIT</td>
          <td>git://github.com/ljharb/es-to-primitive.git</td>
          <td>Unknown</td>
          <td>Jordan Harband</td>
          </tr>
          <tr>
          <td>es6-promise</td>
          <td>4.2.8</td>
          <td>MIT</td>
          <td>git://github.com/stefanpenner/es6-promise.git</td>
          <td><a href="https://github.com/stefanpenner/es6-promise">https://github.com/stefanpenner/es6-promise</a></td>
          <td>Yehuda Katz, Tom Dale, Stefan Penner and contributors</td>
          </tr>
          <tr>
          <td>es6-promisify</td>
          <td>5.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/digitaldesignlabs/es6-promisify.git">https://github.com/digitaldesignlabs/es6-promisify.git</a></td>
          <td>Unknown</td>
          <td>Mike Hall</td>
          </tr>
          <tr>
          <td>escalade</td>
          <td>3.1.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/lukeed/escalade.git">https://github.com/lukeed/escalade.git</a></td>
          <td><a href="https://lukeed.com">https://lukeed.com</a></td>
          <td>Luke Edwards</td>
          </tr>
          <tr>
          <td>escape-goat</td>
          <td>2.1.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/escape-goat.git">https://github.com/sindresorhus/escape-goat.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>escape-html</td>
          <td>1.0.3</td>
          <td>MIT</td>
          <td><a href="https://github.com/component/escape-html.git">https://github.com/component/escape-html.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>escape-string-regexp</td>
          <td>1.0.5</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/escape-string-regexp.git">https://github.com/sindresorhus/escape-string-regexp.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>escape-string-regexp</td>
          <td>4.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/escape-string-regexp.git">https://github.com/sindresorhus/escape-string-regexp.git</a></td>
          <td><a href="https://sindresorhus.com">https://sindresorhus.com</a></td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>escape-string-regexp</td>
          <td>2.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/escape-string-regexp.git">https://github.com/sindresorhus/escape-string-regexp.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>eslint</td>
          <td>5.16.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/eslint/eslint.git">https://github.com/eslint/eslint.git</a></td>
          <td><a href="https://eslint.org/">https://eslint.org/</a></td>
          <td>Nicholas C. Zakas</td>
          </tr>
          <tr>
          <td>eslint-config-airbnb-base</td>
          <td>13.2.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/airbnb/javascript">https://github.com/airbnb/javascript</a></td>
          <td><a href="https://github.com/airbnb/javascript">https://github.com/airbnb/javascript</a></td>
          <td>Jake Teton-Landis</td>
          </tr>
          <tr>
          <td>eslint-import-resolver-node</td>
          <td>0.3.4</td>
          <td>MIT</td>
          <td><a href="https://github.com/benmosher/eslint-plugin-import">https://github.com/benmosher/eslint-plugin-import</a></td>
          <td><a href="https://github.com/benmosher/eslint-plugin-import">https://github.com/benmosher/eslint-plugin-import</a></td>
          <td>Ben Mosher</td>
          </tr>
          <tr>
          <td>eslint-import-resolver-webpack</td>
          <td>0.11.1</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/benmosher/eslint-plugin-import.git">https://github.com/benmosher/eslint-plugin-import.git</a></td>
          <td><a href="https://github.com/benmosher/eslint-plugin-import/tree/master/resolvers/webpack">https://github.com/benmosher/eslint-plugin-import/tree/master/resolvers/webpack</a></td>
          <td>Ben Mosher</td>
          </tr>
          <tr>
          <td>eslint-loader</td>
          <td>2.2.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/webpack-contrib/eslint-loader.git">https://github.com/webpack-contrib/eslint-loader.git</a></td>
          <td>Unknown</td>
          <td>Maxime Thirouin</td>
          </tr>
          <tr>
          <td>eslint-module-utils</td>
          <td>2.6.0</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/benmosher/eslint-plugin-import.git">https://github.com/benmosher/eslint-plugin-import.git</a></td>
          <td><a href="https://github.com/benmosher/eslint-plugin-import#readme">https://github.com/benmosher/eslint-plugin-import#readme</a></td>
          <td>Ben Mosher</td>
          </tr>
          <tr>
          <td>eslint-plugin-import</td>
          <td>2.22.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/benmosher/eslint-plugin-import">https://github.com/benmosher/eslint-plugin-import</a></td>
          <td><a href="https://github.com/benmosher/eslint-plugin-import">https://github.com/benmosher/eslint-plugin-import</a></td>
          <td>Ben Mosher</td>
          </tr>
          <tr>
          <td>eslint-plugin-vue</td>
          <td>5.2.3</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/vuejs/eslint-plugin-vue.git">https://github.com/vuejs/eslint-plugin-vue.git</a></td>
          <td><a href="https://eslint.vuejs.org/">https://eslint.vuejs.org/</a></td>
          <td>Toru Nagashima</td>
          </tr>
          <tr>
          <td>eslint-utils</td>
          <td>1.4.3</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/mysticatea/eslint-utils.git">https://github.com/mysticatea/eslint-utils.git</a></td>
          <td><a href="https://github.com/mysticatea/eslint-utils#readme">https://github.com/mysticatea/eslint-utils#readme</a></td>
          <td>Toru Nagashima</td>
          </tr>
          <tr>
          <td>esm</td>
          <td>3.2.25</td>
          <td>MIT</td>
          <td><a href="https://github.com/standard-things/esm.git">https://github.com/standard-things/esm.git</a></td>
          <td>Unknown</td>
          <td>John-David Dalton</td>
          </tr>
          <tr>
          <td>etag</td>
          <td>1.8.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/jshttp/etag.git">https://github.com/jshttp/etag.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>eventemitter3</td>
          <td>4.0.7</td>
          <td>MIT</td>
          <td>git://github.com/primus/eventemitter3.git</td>
          <td>Unknown</td>
          <td>Arnout Kazemier</td>
          </tr>
          <tr>
          <td>events</td>
          <td>3.3.0</td>
          <td>MIT</td>
          <td>git://github.com/Gozala/events.git</td>
          <td><a href="http://jeditoolkit.com">http://jeditoolkit.com</a></td>
          <td>Irakli Gozalishvili</td>
          </tr>
          <tr>
          <td>eventsource</td>
          <td>1.0.7</td>
          <td>MIT</td>
          <td>git://github.com/EventSource/eventsource.git</td>
          <td><a href="http://github.com/EventSource/eventsource">http://github.com/EventSource/eventsource</a></td>
          <td>Aslak Hellesøy</td>
          </tr>
          <tr>
          <td>evp_bytestokey</td>
          <td>1.0.3</td>
          <td>MIT</td>
          <td><a href="https://github.com/crypto-browserify/EVP_BytesToKey.git">https://github.com/crypto-browserify/EVP_BytesToKey.git</a></td>
          <td><a href="https://github.com/crypto-browserify/EVP_BytesToKey">https://github.com/crypto-browserify/EVP_BytesToKey</a></td>
          <td>Calvin Metcalf</td>
          </tr>
          <tr>
          <td>execa</td>
          <td>1.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/execa.git">https://github.com/sindresorhus/execa.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>execa</td>
          <td>0.8.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/execa.git">https://github.com/sindresorhus/execa.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>execa</td>
          <td>3.4.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/execa.git">https://github.com/sindresorhus/execa.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>expand-brackets</td>
          <td>2.1.4</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/expand-brackets.git">https://github.com/jonschlinkert/expand-brackets.git</a></td>
          <td><a href="https://github.com/jonschlinkert/expand-brackets">https://github.com/jonschlinkert/expand-brackets</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>express</td>
          <td>4.17.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/expressjs/express.git">https://github.com/expressjs/express.git</a></td>
          <td><a href="http://expressjs.com/">http://expressjs.com/</a></td>
          <td>TJ Holowaychuk</td>
          </tr>
          <tr>
          <td>extend</td>
          <td>3.0.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/justmoon/node-extend.git">https://github.com/justmoon/node-extend.git</a></td>
          <td><a href="http://www.justmoon.net">http://www.justmoon.net</a></td>
          <td>Stefan Thomas</td>
          </tr>
          <tr>
          <td>extend-shallow</td>
          <td>2.0.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/extend-shallow.git">https://github.com/jonschlinkert/extend-shallow.git</a></td>
          <td><a href="https://github.com/jonschlinkert/extend-shallow">https://github.com/jonschlinkert/extend-shallow</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>extend-shallow</td>
          <td>3.0.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/extend-shallow.git">https://github.com/jonschlinkert/extend-shallow.git</a></td>
          <td><a href="https://github.com/jonschlinkert/extend-shallow">https://github.com/jonschlinkert/extend-shallow</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>external-editor</td>
          <td>3.1.0</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/mrkmg/node-external-editor.git">https://github.com/mrkmg/node-external-editor.git</a></td>
          <td><a href="https://github.com/mrkmg/node-external-editor#readme">https://github.com/mrkmg/node-external-editor#readme</a></td>
          <td>Kevin Gravier</td>
          </tr>
          <tr>
          <td>extglob</td>
          <td>2.0.4</td>
          <td>MIT</td>
          <td><a href="https://github.com/micromatch/extglob.git">https://github.com/micromatch/extglob.git</a></td>
          <td><a href="https://github.com/micromatch/extglob">https://github.com/micromatch/extglob</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>extsprintf</td>
          <td>1.3.0</td>
          <td>MIT</td>
          <td>git://github.com/davepacheco/node-extsprintf.git</td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>fast-deep-equal</td>
          <td>3.1.3</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/epoberezkin/fast-deep-equal.git">https://github.com/epoberezkin/fast-deep-equal.git</a></td>
          <td><a href="https://github.com/epoberezkin/fast-deep-equal#readme">https://github.com/epoberezkin/fast-deep-equal#readme</a></td>
          <td>Evgeny Poberezkin</td>
          </tr>
          <tr>
          <td>fast-glob</td>
          <td>2.2.7</td>
          <td>MIT</td>
          <td><a href="https://github.com/mrmlnc/fast-glob.git">https://github.com/mrmlnc/fast-glob.git</a></td>
          <td>canonium.com</td>
          <td>Denis Malinochkin</td>
          </tr>
          <tr>
          <td>fast-glob</td>
          <td>3.2.5</td>
          <td>MIT</td>
          <td><a href="https://github.com/mrmlnc/fast-glob.git">https://github.com/mrmlnc/fast-glob.git</a></td>
          <td><a href="https://mrmlnc.com">https://mrmlnc.com</a></td>
          <td>Denis Malinochkin</td>
          </tr>
          <tr>
          <td>fast-json-stable-stringify</td>
          <td>2.1.0</td>
          <td>MIT</td>
          <td>git://github.com/epoberezkin/fast-json-stable-stringify.git</td>
          <td><a href="https://github.com/epoberezkin/fast-json-stable-stringify">https://github.com/epoberezkin/fast-json-stable-stringify</a></td>
          <td>James Halliday</td>
          </tr>
          <tr>
          <td>fast-levenshtein</td>
          <td>2.0.6</td>
          <td>MIT</td>
          <td><a href="https://github.com/hiddentao/fast-levenshtein.git">https://github.com/hiddentao/fast-levenshtein.git</a></td>
          <td><a href="http://www.hiddentao.com/">http://www.hiddentao.com/</a></td>
          <td>Ramesh Nair</td>
          </tr>
          <tr>
          <td>fast-xml-parser</td>
          <td>3.19.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/NaturalIntelligence/fast-xml-parser">https://github.com/NaturalIntelligence/fast-xml-parser</a></td>
          <td><a href="https://amitkumargupta.work/">https://amitkumargupta.work/</a></td>
          <td>Amit Gupta</td>
          </tr>
          <tr>
          <td>fastparse</td>
          <td>1.1.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/webpack/fastparse.git">https://github.com/webpack/fastparse.git</a></td>
          <td><a href="https://github.com/webpack/fastparse">https://github.com/webpack/fastparse</a></td>
          <td>Tobias Koppers @sokra</td>
          </tr>
          <tr>
          <td>fd-slicer</td>
          <td>1.1.0</td>
          <td>MIT</td>
          <td>git://github.com/andrewrk/node-fd-slicer.git</td>
          <td>Unknown</td>
          <td>Andrew Kelley</td>
          </tr>
          <tr>
          <td>figures</td>
          <td>3.2.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/figures.git">https://github.com/sindresorhus/figures.git</a></td>
          <td><a href="https://sindresorhus.com">https://sindresorhus.com</a></td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>figures</td>
          <td>2.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/figures.git">https://github.com/sindresorhus/figures.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>file-entry-cache</td>
          <td>5.0.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/royriojas/file-entry-cache.git">https://github.com/royriojas/file-entry-cache.git</a></td>
          <td><a href="http://royriojas.com">http://royriojas.com</a></td>
          <td>Roy Riojas</td>
          </tr>
          <tr>
          <td>file-loader</td>
          <td>4.3.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/webpack-contrib/file-loader.git">https://github.com/webpack-contrib/file-loader.git</a></td>
          <td><a href="https://github.com/webpack-contrib/file-loader">https://github.com/webpack-contrib/file-loader</a></td>
          <td>Tobias Koppers @sokra</td>
          </tr>
          <tr>
          <td>file-loader</td>
          <td>6.2.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/webpack-contrib/file-loader.git">https://github.com/webpack-contrib/file-loader.git</a></td>
          <td><a href="https://github.com/webpack-contrib/file-loader">https://github.com/webpack-contrib/file-loader</a></td>
          <td>Tobias Koppers @sokra</td>
          </tr>
          <tr>
          <td>file-uri-to-path</td>
          <td>1.0.0</td>
          <td>MIT</td>
          <td>git://github.com/TooTallNate/file-uri-to-path.git</td>
          <td><a href="https://github.com/TooTallNate/file-uri-to-path">https://github.com/TooTallNate/file-uri-to-path</a></td>
          <td>Nathan Rajlich</td>
          </tr>
          <tr>
          <td>fill-range</td>
          <td>4.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/fill-range.git">https://github.com/jonschlinkert/fill-range.git</a></td>
          <td><a href="https://github.com/jonschlinkert/fill-range">https://github.com/jonschlinkert/fill-range</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>fill-range</td>
          <td>7.0.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/fill-range.git">https://github.com/jonschlinkert/fill-range.git</a></td>
          <td><a href="https://github.com/jonschlinkert/fill-range">https://github.com/jonschlinkert/fill-range</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>finalhandler</td>
          <td>1.1.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/pillarjs/finalhandler.git">https://github.com/pillarjs/finalhandler.git</a></td>
          <td>Unknown</td>
          <td>Douglas Christopher Wilson</td>
          </tr>
          <tr>
          <td>find-cache-dir</td>
          <td>3.3.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/avajs/find-cache-dir.git">https://github.com/avajs/find-cache-dir.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>find-cache-dir</td>
          <td>2.1.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/avajs/find-cache-dir.git">https://github.com/avajs/find-cache-dir.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>find-cache-dir</td>
          <td>0.1.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/jamestalmage/find-cache-dir.git">https://github.com/jamestalmage/find-cache-dir.git</a></td>
          <td>github.com/jamestalmage</td>
          <td>James Talmage</td>
          </tr>
          <tr>
          <td>find-root</td>
          <td>1.1.0</td>
          <td>MIT</td>
          <td>git@github.com:js-n/find-root.git</td>
          <td>Unknown</td>
          <td>jsdnxx</td>
          </tr>
          <tr>
          <td>find-up</td>
          <td>4.1.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/find-up.git">https://github.com/sindresorhus/find-up.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>find-up</td>
          <td>3.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/find-up.git">https://github.com/sindresorhus/find-up.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>find-up</td>
          <td>1.1.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/find-up.git">https://github.com/sindresorhus/find-up.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>find-up</td>
          <td>2.1.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/find-up.git">https://github.com/sindresorhus/find-up.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>flat-cache</td>
          <td>2.0.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/royriojas/flat-cache.git">https://github.com/royriojas/flat-cache.git</a></td>
          <td><a href="http://royriojas.com">http://royriojas.com</a></td>
          <td>Roy Riojas</td>
          </tr>
          <tr>
          <td>flush-write-stream</td>
          <td>1.1.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/mafintosh/flush-write-stream.git">https://github.com/mafintosh/flush-write-stream.git</a></td>
          <td><a href="https://github.com/mafintosh/flush-write-stream">https://github.com/mafintosh/flush-write-stream</a></td>
          <td>Mathias Buus</td>
          </tr>
          <tr>
          <td>follow-redirects</td>
          <td>1.13.3</td>
          <td>MIT</td>
          <td>git@github.com:follow-redirects/follow-redirects.git</td>
          <td><a href="https://github.com/follow-redirects/follow-redirects">https://github.com/follow-redirects/follow-redirects</a></td>
          <td>Ruben Verborgh</td>
          </tr>
          <tr>
          <td>for-in</td>
          <td>1.0.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/for-in.git">https://github.com/jonschlinkert/for-in.git</a></td>
          <td><a href="https://github.com/jonschlinkert/for-in">https://github.com/jonschlinkert/for-in</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>form-data</td>
          <td>2.3.3</td>
          <td>MIT</td>
          <td>git://github.com/form-data/form-data.git</td>
          <td><a href="http://debuggable.com/">http://debuggable.com/</a></td>
          <td>Felix Geisendörfer</td>
          </tr>
          <tr>
          <td>forwarded</td>
          <td>0.1.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/jshttp/forwarded.git">https://github.com/jshttp/forwarded.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>fragment-cache</td>
          <td>0.2.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/fragment-cache.git">https://github.com/jonschlinkert/fragment-cache.git</a></td>
          <td><a href="https://github.com/jonschlinkert/fragment-cache">https://github.com/jonschlinkert/fragment-cache</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>fresh</td>
          <td>0.5.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/jshttp/fresh.git">https://github.com/jshttp/fresh.git</a></td>
          <td><a href="http://tjholowaychuk.com">http://tjholowaychuk.com</a></td>
          <td>TJ Holowaychuk</td>
          </tr>
          <tr>
          <td>from2</td>
          <td>2.3.0</td>
          <td>MIT</td>
          <td>git://github.com/hughsk/from2</td>
          <td><a href="https://github.com/hughsk/from2">https://github.com/hughsk/from2</a></td>
          <td>Hugh Kennedy</td>
          </tr>
          <tr>
          <td>fs-extra</td>
          <td>7.0.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/jprichardson/node-fs-extra">https://github.com/jprichardson/node-fs-extra</a></td>
          <td><a href="https://github.com/jprichardson/node-fs-extra">https://github.com/jprichardson/node-fs-extra</a></td>
          <td>JP Richardson</td>
          </tr>
          <tr>
          <td>function-bind</td>
          <td>1.1.1</td>
          <td>MIT</td>
          <td>git://github.com/Raynos/function-bind.git</td>
          <td><a href="https://github.com/Raynos/function-bind">https://github.com/Raynos/function-bind</a></td>
          <td>Raynos</td>
          </tr>
          <tr>
          <td>functional-red-black-tree</td>
          <td>1.0.1</td>
          <td>MIT</td>
          <td>git://github.com/mikolalysenko/functional-red-black-tree.git</td>
          <td>Unknown</td>
          <td>Mikola Lysenko</td>
          </tr>
          <tr>
          <td>generic-names</td>
          <td>1.0.3</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/css-modules/generic-names.git">https://github.com/css-modules/generic-names.git</a></td>
          <td><a href="https://github.com/css-modules/generic-names#readme">https://github.com/css-modules/generic-names#readme</a></td>
          <td>Alexey Litvinov</td>
          </tr>
          <tr>
          <td>generic-pool</td>
          <td>3.7.2</td>
          <td>MIT</td>
          <td><a href="http://github.com/coopernurse/node-pool.git">http://github.com/coopernurse/node-pool.git</a></td>
          <td>Unknown</td>
          <td>James Cooper</td>
          </tr>
          <tr>
          <td>gensync</td>
          <td>1.0.0-beta.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/loganfsmyth/gensync.git">https://github.com/loganfsmyth/gensync.git</a></td>
          <td><a href="https://github.com/loganfsmyth/gensync">https://github.com/loganfsmyth/gensync</a></td>
          <td>Logan Smyth</td>
          </tr>
          <tr>
          <td>get-intrinsic</td>
          <td>1.1.1</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/ljharb/get-intrinsic.git">https://github.com/ljharb/get-intrinsic.git</a></td>
          <td><a href="https://github.com/ljharb/get-intrinsic#readme">https://github.com/ljharb/get-intrinsic#readme</a></td>
          <td>Jordan Harband</td>
          </tr>
          <tr>
          <td>get-stream</td>
          <td>4.1.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/get-stream.git">https://github.com/sindresorhus/get-stream.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>get-stream</td>
          <td>3.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/get-stream.git">https://github.com/sindresorhus/get-stream.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>get-stream</td>
          <td>5.2.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/get-stream.git">https://github.com/sindresorhus/get-stream.git</a></td>
          <td><a href="https://sindresorhus.com">https://sindresorhus.com</a></td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>get-value</td>
          <td>2.0.6</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/get-value.git">https://github.com/jonschlinkert/get-value.git</a></td>
          <td><a href="https://github.com/jonschlinkert/get-value">https://github.com/jonschlinkert/get-value</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>getpass</td>
          <td>0.1.7</td>
          <td>MIT</td>
          <td><a href="https://github.com/arekinath/node-getpass.git">https://github.com/arekinath/node-getpass.git</a></td>
          <td>Unknown</td>
          <td>Alex Wilson</td>
          </tr>
          <tr>
          <td>global-dirs</td>
          <td>3.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/global-dirs.git">https://github.com/sindresorhus/global-dirs.git</a></td>
          <td><a href="https://sindresorhus.com">https://sindresorhus.com</a></td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>globals</td>
          <td>11.12.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/globals.git">https://github.com/sindresorhus/globals.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>globby</td>
          <td>9.2.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/globby.git">https://github.com/sindresorhus/globby.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>globby</td>
          <td>7.1.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/globby.git">https://github.com/sindresorhus/globby.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>globby</td>
          <td>6.1.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/globby.git">https://github.com/sindresorhus/globby.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>globby</td>
          <td>11.0.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/globby.git">https://github.com/sindresorhus/globby.git</a></td>
          <td><a href="https://sindresorhus.com">https://sindresorhus.com</a></td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>got</td>
          <td>9.6.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/got.git">https://github.com/sindresorhus/got.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>graphql</td>
          <td>14.7.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/graphql/graphql-js.git">https://github.com/graphql/graphql-js.git</a></td>
          <td><a href="https://github.com/graphql/graphql-js">https://github.com/graphql/graphql-js</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>graphql-tag</td>
          <td>2.11.0</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/apollographql/graphql-tag.git">https://github.com/apollographql/graphql-tag.git</a></td>
          <td><a href="https://github.com/apollographql/graphql-tag#readme">https://github.com/apollographql/graphql-tag#readme</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>gzip-size</td>
          <td>5.1.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/gzip-size.git">https://github.com/sindresorhus/gzip-size.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>handle-thing</td>
          <td>2.0.1</td>
          <td>MIT</td>
          <td>git+ssh://git@github.com/indutny/handle-thing.git</td>
          <td><a href="https://github.com/spdy-http2/handle-thing#readme">https://github.com/spdy-http2/handle-thing#readme</a></td>
          <td>Fedor Indutny</td>
          </tr>
          <tr>
          <td>har-validator</td>
          <td>5.1.5</td>
          <td>MIT</td>
          <td><a href="https://github.com/ahmadnassri/node-har-validator.git">https://github.com/ahmadnassri/node-har-validator.git</a></td>
          <td><a href="https://github.com/ahmadnassri/node-har-validator">https://github.com/ahmadnassri/node-har-validator</a></td>
          <td>Ahmad Nassri</td>
          </tr>
          <tr>
          <td>has</td>
          <td>1.0.3</td>
          <td>MIT</td>
          <td>git://github.com/tarruda/has.git</td>
          <td><a href="https://github.com/tarruda/has">https://github.com/tarruda/has</a></td>
          <td>Thiago de Arruda</td>
          </tr>
          <tr>
          <td>has-ansi</td>
          <td>2.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/has-ansi.git">https://github.com/sindresorhus/has-ansi.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>has-bigints</td>
          <td>1.0.1</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/ljharb/has-bigints.git">https://github.com/ljharb/has-bigints.git</a></td>
          <td><a href="https://github.com/ljharb/has-bigints#readme">https://github.com/ljharb/has-bigints#readme</a></td>
          <td>Jordan Harband</td>
          </tr>
          <tr>
          <td>has-flag</td>
          <td>3.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/has-flag.git">https://github.com/sindresorhus/has-flag.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>has-flag</td>
          <td>4.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/has-flag.git">https://github.com/sindresorhus/has-flag.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>has-flag</td>
          <td>1.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/has-flag.git">https://github.com/sindresorhus/has-flag.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>has-symbols</td>
          <td>1.0.2</td>
          <td>MIT</td>
          <td>git://github.com/inspect-js/has-symbols.git</td>
          <td><a href="http://ljharb.codes">http://ljharb.codes</a></td>
          <td>Jordan Harband</td>
          </tr>
          <tr>
          <td>has-value</td>
          <td>1.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/has-value.git">https://github.com/jonschlinkert/has-value.git</a></td>
          <td><a href="https://github.com/jonschlinkert/has-value">https://github.com/jonschlinkert/has-value</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>has-value</td>
          <td>0.3.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/has-value.git">https://github.com/jonschlinkert/has-value.git</a></td>
          <td><a href="https://github.com/jonschlinkert/has-value">https://github.com/jonschlinkert/has-value</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>has-values</td>
          <td>1.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/has-values.git">https://github.com/jonschlinkert/has-values.git</a></td>
          <td><a href="https://github.com/jonschlinkert/has-values">https://github.com/jonschlinkert/has-values</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>has-values</td>
          <td>0.1.4</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/has-values.git">https://github.com/jonschlinkert/has-values.git</a></td>
          <td><a href="https://github.com/jonschlinkert/has-values">https://github.com/jonschlinkert/has-values</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>has-yarn</td>
          <td>2.1.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/has-yarn.git">https://github.com/sindresorhus/has-yarn.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>hash-base</td>
          <td>3.1.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/crypto-browserify/hash-base.git">https://github.com/crypto-browserify/hash-base.git</a></td>
          <td><a href="https://github.com/crypto-browserify/hash-base">https://github.com/crypto-browserify/hash-base</a></td>
          <td>Kirill Fomichev</td>
          </tr>
          <tr>
          <td>hash-sum</td>
          <td>2.0.0</td>
          <td>MIT</td>
          <td>git://github.com/bevacqua/hash-sum.git</td>
          <td><a href="https://github.com/bevacqua/hash-sum">https://github.com/bevacqua/hash-sum</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>hash-sum</td>
          <td>1.0.2</td>
          <td>MIT</td>
          <td>git://github.com/bevacqua/hash-sum.git</td>
          <td><a href="https://github.com/bevacqua/hash-sum">https://github.com/bevacqua/hash-sum</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>hash.js</td>
          <td>1.1.7</td>
          <td>MIT</td>
          <td>git@github.com:indutny/hash.js</td>
          <td><a href="https://github.com/indutny/hash.js">https://github.com/indutny/hash.js</a></td>
          <td>Fedor Indutny</td>
          </tr>
          <tr>
          <td>he</td>
          <td>1.2.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/mathiasbynens/he.git">https://github.com/mathiasbynens/he.git</a></td>
          <td><a href="https://mths.be/he">https://mths.be/he</a></td>
          <td>Mathias Bynens</td>
          </tr>
          <tr>
          <td>hex-color-regex</td>
          <td>1.1.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/regexps/hex-color-regex.git">https://github.com/regexps/hex-color-regex.git</a></td>
          <td><a href="http://www.tunnckocore.tk">http://www.tunnckocore.tk</a></td>
          <td>Charlike Mike Reagent</td>
          </tr>
          <tr>
          <td>hmac-drbg</td>
          <td>1.0.1</td>
          <td>MIT</td>
          <td>git+ssh://git@github.com/indutny/hmac-drbg.git</td>
          <td><a href="https://github.com/indutny/hmac-drbg#readme">https://github.com/indutny/hmac-drbg#readme</a></td>
          <td>Fedor Indutny</td>
          </tr>
          <tr>
          <td>hoopy</td>
          <td>0.1.4</td>
          <td>MIT</td>
          <td>git+<a href="https://gitlab.com/philbooth/hoopy.git">https://gitlab.com/philbooth/hoopy.git</a></td>
          <td><a href="https://gitlab.com/philbooth/hoopy#readme">https://gitlab.com/philbooth/hoopy#readme</a></td>
          <td>Phil Booth</td>
          </tr>
          <tr>
          <td>hpack.js</td>
          <td>2.1.6</td>
          <td>MIT</td>
          <td>git+ssh://git@github.com/indutny/hpack.js.git</td>
          <td><a href="https://github.com/indutny/hpack.js#readme">https://github.com/indutny/hpack.js#readme</a></td>
          <td>Fedor Indutny</td>
          </tr>
          <tr>
          <td>hsl-regex</td>
          <td>1.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/regexps/hsl-regex.git">https://github.com/regexps/hsl-regex.git</a></td>
          <td><a href="https://github.com/regexps/hsl-regex">https://github.com/regexps/hsl-regex</a></td>
          <td>John Otander</td>
          </tr>
          <tr>
          <td>hsla-regex</td>
          <td>1.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/regexps/hsla-regex.git">https://github.com/regexps/hsla-regex.git</a></td>
          <td><a href="https://github.com/regexps/hsla-regex">https://github.com/regexps/hsla-regex</a></td>
          <td>John Otander</td>
          </tr>
          <tr>
          <td>html-comment-regex</td>
          <td>1.1.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/stevemao/html-comment-regex.git">https://github.com/stevemao/html-comment-regex.git</a></td>
          <td><a href="https://github.com/stevemao/html-comment-regex">https://github.com/stevemao/html-comment-regex</a></td>
          <td>Steve Mao</td>
          </tr>
          <tr>
          <td>html-encoding-sniffer</td>
          <td>2.0.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/jsdom/html-encoding-sniffer.git">https://github.com/jsdom/html-encoding-sniffer.git</a></td>
          <td><a href="https://domenic.me/">https://domenic.me/</a></td>
          <td>Domenic Denicola</td>
          </tr>
          <tr>
          <td>html-entities</td>
          <td>1.4.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/mdevils/node-html-entities.git">https://github.com/mdevils/node-html-entities.git</a></td>
          <td>Unknown</td>
          <td>Marat Dulin</td>
          </tr>
          <tr>
          <td>html-minifier</td>
          <td>3.5.21</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/kangax/html-minifier.git">https://github.com/kangax/html-minifier.git</a></td>
          <td><a href="https://kangax.github.io/html-minifier/">https://kangax.github.io/html-minifier/</a></td>
          <td>Juriy \kangax\  Zaytsev</td>
          </tr>
          <tr>
          <td>html-tags</td>
          <td>3.1.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/html-tags.git">https://github.com/sindresorhus/html-tags.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>html-tags</td>
          <td>2.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/html-tags.git">https://github.com/sindresorhus/html-tags.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>html-webpack-plugin</td>
          <td>3.2.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/jantimon/html-webpack-plugin.git">https://github.com/jantimon/html-webpack-plugin.git</a></td>
          <td><a href="https://github.com/jantimon/html-webpack-plugin">https://github.com/jantimon/html-webpack-plugin</a></td>
          <td>Charles Blaxland</td>
          </tr>
          <tr>
          <td>htmlparser2</td>
          <td>3.10.1</td>
          <td>MIT</td>
          <td>git://github.com/fb55/htmlparser2.git</td>
          <td>Unknown</td>
          <td>Felix Boehm</td>
          </tr>
          <tr>
          <td>http-deceiver</td>
          <td>1.2.7</td>
          <td>MIT</td>
          <td>git+ssh://git@github.com/indutny/http-deceiver.git</td>
          <td><a href="https://github.com/indutny/http-deceiver#readme">https://github.com/indutny/http-deceiver#readme</a></td>
          <td>Fedor Indutny</td>
          </tr>
          <tr>
          <td>http-errors</td>
          <td>1.7.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/jshttp/http-errors.git">https://github.com/jshttp/http-errors.git</a></td>
          <td><a href="http://jongleberry.com">http://jongleberry.com</a></td>
          <td>Jonathan Ong</td>
          </tr>
          <tr>
          <td>http-errors</td>
          <td>1.6.3</td>
          <td>MIT</td>
          <td><a href="https://github.com/jshttp/http-errors.git">https://github.com/jshttp/http-errors.git</a></td>
          <td><a href="http://jongleberry.com">http://jongleberry.com</a></td>
          <td>Jonathan Ong</td>
          </tr>
          <tr>
          <td>http-parser-js</td>
          <td>0.5.3</td>
          <td>MIT</td>
          <td>git://github.com/creationix/http-parser-js.git</td>
          <td><a href="https://github.com/creationix">https://github.com/creationix</a></td>
          <td>Tim Caswell</td>
          </tr>
          <tr>
          <td>http-proxy</td>
          <td>1.18.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/http-party/node-http-proxy.git">https://github.com/http-party/node-http-proxy.git</a></td>
          <td>Unknown</td>
          <td>Charlie Robbins</td>
          </tr>
          <tr>
          <td>http-proxy-middleware</td>
          <td>0.19.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/chimurai/http-proxy-middleware.git">https://github.com/chimurai/http-proxy-middleware.git</a></td>
          <td><a href="https://github.com/chimurai/http-proxy-middleware">https://github.com/chimurai/http-proxy-middleware</a></td>
          <td>Steven Chim</td>
          </tr>
          <tr>
          <td>http-proxy-middleware</td>
          <td>0.18.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/chimurai/http-proxy-middleware.git">https://github.com/chimurai/http-proxy-middleware.git</a></td>
          <td><a href="https://github.com/chimurai/http-proxy-middleware">https://github.com/chimurai/http-proxy-middleware</a></td>
          <td>Steven Chim</td>
          </tr>
          <tr>
          <td>http-signature</td>
          <td>1.2.0</td>
          <td>MIT</td>
          <td>git://github.com/joyent/node-http-signature.git</td>
          <td><a href="https://github.com/joyent/node-http-signature/">https://github.com/joyent/node-http-signature/</a></td>
          <td>Joyent, Inc</td>
          </tr>
          <tr>
          <td>https-browserify</td>
          <td>1.0.0</td>
          <td>MIT</td>
          <td>git://github.com/substack/https-browserify.git</td>
          <td><a href="https://github.com/substack/https-browserify">https://github.com/substack/https-browserify</a></td>
          <td>James Halliday</td>
          </tr>
          <tr>
          <td>https-proxy-agent</td>
          <td>2.2.4</td>
          <td>MIT</td>
          <td>git://github.com/TooTallNate/node-https-proxy-agent.git</td>
          <td><a href="http://n8.io/">http://n8.io/</a></td>
          <td>Nathan Rajlich</td>
          </tr>
          <tr>
          <td>iconv-lite</td>
          <td>0.4.24</td>
          <td>MIT</td>
          <td>git://github.com/ashtuchkin/iconv-lite.git</td>
          <td><a href="https://github.com/ashtuchkin/iconv-lite">https://github.com/ashtuchkin/iconv-lite</a></td>
          <td>Alexander Shtuchkin</td>
          </tr>
          <tr>
          <td>iferr</td>
          <td>0.1.5</td>
          <td>MIT</td>
          <td><a href="https://github.com/shesek/iferr">https://github.com/shesek/iferr</a></td>
          <td><a href="https://github.com/shesek/iferr">https://github.com/shesek/iferr</a></td>
          <td>Nadav Ivgi</td>
          </tr>
          <tr>
          <td>ignore</td>
          <td>4.0.6</td>
          <td>MIT</td>
          <td>git@github.com:kaelzhang/node-ignore.git</td>
          <td>Unknown</td>
          <td>kael</td>
          </tr>
          <tr>
          <td>ignore</td>
          <td>3.3.10</td>
          <td>MIT</td>
          <td>git@github.com:kaelzhang/node-ignore.git</td>
          <td>Unknown</td>
          <td>kael</td>
          </tr>
          <tr>
          <td>ignore</td>
          <td>5.1.8</td>
          <td>MIT</td>
          <td>git@github.com:kaelzhang/node-ignore.git</td>
          <td>Unknown</td>
          <td>kael</td>
          </tr>
          <tr>
          <td>import-cwd</td>
          <td>2.1.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/import-cwd.git">https://github.com/sindresorhus/import-cwd.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>import-fresh</td>
          <td>2.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/import-fresh.git">https://github.com/sindresorhus/import-fresh.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>import-fresh</td>
          <td>3.3.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/import-fresh.git">https://github.com/sindresorhus/import-fresh.git</a></td>
          <td><a href="https://sindresorhus.com">https://sindresorhus.com</a></td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>import-from</td>
          <td>2.1.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/import-from.git">https://github.com/sindresorhus/import-from.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>import-lazy</td>
          <td>2.1.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/import-lazy.git">https://github.com/sindresorhus/import-lazy.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>import-local</td>
          <td>2.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/import-local.git">https://github.com/sindresorhus/import-local.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>import-local</td>
          <td>3.0.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/import-local.git">https://github.com/sindresorhus/import-local.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>imurmurhash</td>
          <td>0.1.4</td>
          <td>MIT</td>
          <td><a href="https://github.com/jensyt/imurmurhash-js">https://github.com/jensyt/imurmurhash-js</a></td>
          <td><a href="https://github.com/jensyt/imurmurhash-js">https://github.com/jensyt/imurmurhash-js</a></td>
          <td>Jens Taylor</td>
          </tr>
          <tr>
          <td>indent-string</td>
          <td>4.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/indent-string.git">https://github.com/sindresorhus/indent-string.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>indexes-of</td>
          <td>1.0.1</td>
          <td>MIT</td>
          <td>git://github.com/dominictarr/indexes-of.git</td>
          <td><a href="https://github.com/dominictarr/indexes-of">https://github.com/dominictarr/indexes-of</a></td>
          <td>Dominic Tarr</td>
          </tr>
          <tr>
          <td>inquirer</td>
          <td>7.3.3</td>
          <td>MIT</td>
          <td><a href="https://github.com/SBoudrias/Inquirer.js.git">https://github.com/SBoudrias/Inquirer.js.git</a></td>
          <td>Unknown</td>
          <td>Simon Boudrias</td>
          </tr>
          <tr>
          <td>inquirer</td>
          <td>6.5.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/SBoudrias/Inquirer.js.git">https://github.com/SBoudrias/Inquirer.js.git</a></td>
          <td>Unknown</td>
          <td>Simon Boudrias</td>
          </tr>
          <tr>
          <td>internal-ip</td>
          <td>4.3.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/internal-ip.git">https://github.com/sindresorhus/internal-ip.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>interpret</td>
          <td>1.4.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/gulpjs/interpret.git">https://github.com/gulpjs/interpret.git</a></td>
          <td><a href="http://gulpjs.com/">http://gulpjs.com/</a></td>
          <td>Gulp Team</td>
          </tr>
          <tr>
          <td>ip</td>
          <td>1.1.5</td>
          <td>MIT</td>
          <td><a href="http://github.com/indutny/node-ip.git">http://github.com/indutny/node-ip.git</a></td>
          <td><a href="https://github.com/indutny/node-ip">https://github.com/indutny/node-ip</a></td>
          <td>Fedor Indutny</td>
          </tr>
          <tr>
          <td>ip-regex</td>
          <td>2.1.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/ip-regex.git">https://github.com/sindresorhus/ip-regex.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>ipaddr.js</td>
          <td>1.9.1</td>
          <td>MIT</td>
          <td>git://github.com/whitequark/ipaddr.js</td>
          <td>Unknown</td>
          <td>whitequark</td>
          </tr>
          <tr>
          <td>irregular-plurals</td>
          <td>3.2.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/irregular-plurals.git">https://github.com/sindresorhus/irregular-plurals.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>is-absolute-url</td>
          <td>3.0.3</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/is-absolute-url.git">https://github.com/sindresorhus/is-absolute-url.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>is-absolute-url</td>
          <td>2.1.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/is-absolute-url.git">https://github.com/sindresorhus/is-absolute-url.git</a></td>
          <td><a href="http://sindresorhus.com">http://sindresorhus.com</a></td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>is-accessor-descriptor</td>
          <td>1.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/is-accessor-descriptor.git">https://github.com/jonschlinkert/is-accessor-descriptor.git</a></td>
          <td><a href="https://github.com/jonschlinkert/is-accessor-descriptor">https://github.com/jonschlinkert/is-accessor-descriptor</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>is-accessor-descriptor</td>
          <td>0.1.6</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/is-accessor-descriptor.git">https://github.com/jonschlinkert/is-accessor-descriptor.git</a></td>
          <td><a href="https://github.com/jonschlinkert/is-accessor-descriptor">https://github.com/jonschlinkert/is-accessor-descriptor</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>is-arguments</td>
          <td>1.1.0</td>
          <td>MIT</td>
          <td>git://github.com/inspect-js/is-arguments.git</td>
          <td><a href="https://github.com/inspect-js/is-arguments">https://github.com/inspect-js/is-arguments</a></td>
          <td>Jordan Harband</td>
          </tr>
          <tr>
          <td>is-arrayish</td>
          <td>0.3.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/qix-/node-is-arrayish.git">https://github.com/qix-/node-is-arrayish.git</a></td>
          <td><a href="http://github.com/qix-">http://github.com/qix-</a></td>
          <td>Qix</td>
          </tr>
          <tr>
          <td>is-arrayish</td>
          <td>0.2.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/qix-/node-is-arrayish.git">https://github.com/qix-/node-is-arrayish.git</a></td>
          <td><a href="http://github.com/qix-">http://github.com/qix-</a></td>
          <td>Qix</td>
          </tr>
          <tr>
          <td>is-bigint</td>
          <td>1.0.1</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/ljharb/is-bigint.git">https://github.com/ljharb/is-bigint.git</a></td>
          <td><a href="https://github.com/ljharb/is-bigint#readme">https://github.com/ljharb/is-bigint#readme</a></td>
          <td>Jordan Harband</td>
          </tr>
          <tr>
          <td>is-binary-path</td>
          <td>2.1.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/is-binary-path.git">https://github.com/sindresorhus/is-binary-path.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>is-binary-path</td>
          <td>1.0.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/is-binary-path.git">https://github.com/sindresorhus/is-binary-path.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>is-boolean-object</td>
          <td>1.1.0</td>
          <td>MIT</td>
          <td>git://github.com/ljharb/is-boolean-object.git</td>
          <td>Unknown</td>
          <td>Jordan Harband</td>
          </tr>
          <tr>
          <td>is-buffer</td>
          <td>1.1.6</td>
          <td>MIT</td>
          <td>git://github.com/feross/is-buffer.git</td>
          <td><a href="http://feross.org/">http://feross.org/</a></td>
          <td>Feross Aboukhadijeh</td>
          </tr>
          <tr>
          <td>is-callable</td>
          <td>1.2.3</td>
          <td>MIT</td>
          <td>git://github.com/ljharb/is-callable.git</td>
          <td><a href="http://ljharb.codes">http://ljharb.codes</a></td>
          <td>Jordan Harband</td>
          </tr>
          <tr>
          <td>is-ci</td>
          <td>1.2.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/watson/is-ci.git">https://github.com/watson/is-ci.git</a></td>
          <td><a href="https://github.com/watson/is-ci">https://github.com/watson/is-ci</a></td>
          <td>Thomas Watson Steen</td>
          </tr>
          <tr>
          <td>is-ci</td>
          <td>2.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/watson/is-ci.git">https://github.com/watson/is-ci.git</a></td>
          <td><a href="https://github.com/watson/is-ci">https://github.com/watson/is-ci</a></td>
          <td>Thomas Watson Steen</td>
          </tr>
          <tr>
          <td>is-color-stop</td>
          <td>1.1.0</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/pigcan/is-color-stop.git">https://github.com/pigcan/is-color-stop.git</a></td>
          <td><a href="https://github.com/pigcan/is-color-stop#readme">https://github.com/pigcan/is-color-stop#readme</a></td>
          <td>pigcan</td>
          </tr>
          <tr>
          <td>is-core-module</td>
          <td>2.2.0</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/inspect-js/is-core-module.git">https://github.com/inspect-js/is-core-module.git</a></td>
          <td><a href="https://github.com/inspect-js/is-core-module">https://github.com/inspect-js/is-core-module</a></td>
          <td>Jordan Harband</td>
          </tr>
          <tr>
          <td>is-data-descriptor</td>
          <td>1.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/is-data-descriptor.git">https://github.com/jonschlinkert/is-data-descriptor.git</a></td>
          <td><a href="https://github.com/jonschlinkert/is-data-descriptor">https://github.com/jonschlinkert/is-data-descriptor</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>is-data-descriptor</td>
          <td>0.1.4</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/is-data-descriptor.git">https://github.com/jonschlinkert/is-data-descriptor.git</a></td>
          <td><a href="https://github.com/jonschlinkert/is-data-descriptor">https://github.com/jonschlinkert/is-data-descriptor</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>is-date-object</td>
          <td>1.0.2</td>
          <td>MIT</td>
          <td>git://github.com/ljharb/is-date-object.git</td>
          <td>Unknown</td>
          <td>Jordan Harband</td>
          </tr>
          <tr>
          <td>is-descriptor</td>
          <td>1.0.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/is-descriptor.git">https://github.com/jonschlinkert/is-descriptor.git</a></td>
          <td><a href="https://github.com/jonschlinkert/is-descriptor">https://github.com/jonschlinkert/is-descriptor</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>is-descriptor</td>
          <td>0.1.6</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/is-descriptor.git">https://github.com/jonschlinkert/is-descriptor.git</a></td>
          <td><a href="https://github.com/jonschlinkert/is-descriptor">https://github.com/jonschlinkert/is-descriptor</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>is-directory</td>
          <td>0.3.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/is-directory.git">https://github.com/jonschlinkert/is-directory.git</a></td>
          <td><a href="https://github.com/jonschlinkert/is-directory">https://github.com/jonschlinkert/is-directory</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>is-docker</td>
          <td>2.1.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/is-docker.git">https://github.com/sindresorhus/is-docker.git</a></td>
          <td><a href="https://sindresorhus.com">https://sindresorhus.com</a></td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>is-error</td>
          <td>2.2.2</td>
          <td>MIT</td>
          <td>git://github.com/mk-pmb/is-error-js.git</td>
          <td><a href="https://github.com/mk-pmb/is-error-js">https://github.com/mk-pmb/is-error-js</a></td>
          <td>Raynos</td>
          </tr>
          <tr>
          <td>is-extendable</td>
          <td>0.1.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/is-extendable.git">https://github.com/jonschlinkert/is-extendable.git</a></td>
          <td><a href="https://github.com/jonschlinkert/is-extendable">https://github.com/jonschlinkert/is-extendable</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>is-extendable</td>
          <td>1.0.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/is-extendable.git">https://github.com/jonschlinkert/is-extendable.git</a></td>
          <td><a href="https://github.com/jonschlinkert/is-extendable">https://github.com/jonschlinkert/is-extendable</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>is-extglob</td>
          <td>2.1.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/is-extglob.git">https://github.com/jonschlinkert/is-extglob.git</a></td>
          <td><a href="https://github.com/jonschlinkert/is-extglob">https://github.com/jonschlinkert/is-extglob</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>is-fullwidth-code-point</td>
          <td>3.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/is-fullwidth-code-point.git">https://github.com/sindresorhus/is-fullwidth-code-point.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>is-fullwidth-code-point</td>
          <td>2.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/is-fullwidth-code-point.git">https://github.com/sindresorhus/is-fullwidth-code-point.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>is-glob</td>
          <td>4.0.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/micromatch/is-glob.git">https://github.com/micromatch/is-glob.git</a></td>
          <td><a href="https://github.com/micromatch/is-glob">https://github.com/micromatch/is-glob</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>is-glob</td>
          <td>3.1.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/is-glob.git">https://github.com/jonschlinkert/is-glob.git</a></td>
          <td><a href="https://github.com/jonschlinkert/is-glob">https://github.com/jonschlinkert/is-glob</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>is-installed-globally</td>
          <td>0.4.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/is-installed-globally.git">https://github.com/sindresorhus/is-installed-globally.git</a></td>
          <td><a href="https://sindresorhus.com">https://sindresorhus.com</a></td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>is-interactive</td>
          <td>1.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/is-interactive.git">https://github.com/sindresorhus/is-interactive.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>is-negative-zero</td>
          <td>2.0.1</td>
          <td>MIT</td>
          <td>git://github.com/inspect-js/is-negative-zero.git</td>
          <td><a href="https://github.com/inspect-js/is-negative-zero">https://github.com/inspect-js/is-negative-zero</a></td>
          <td>Jordan Harband</td>
          </tr>
          <tr>
          <td>is-npm</td>
          <td>5.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/is-npm.git">https://github.com/sindresorhus/is-npm.git</a></td>
          <td><a href="https://sindresorhus.com">https://sindresorhus.com</a></td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>is-number</td>
          <td>3.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/is-number.git">https://github.com/jonschlinkert/is-number.git</a></td>
          <td><a href="https://github.com/jonschlinkert/is-number">https://github.com/jonschlinkert/is-number</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>is-number</td>
          <td>7.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/is-number.git">https://github.com/jonschlinkert/is-number.git</a></td>
          <td><a href="https://github.com/jonschlinkert/is-number">https://github.com/jonschlinkert/is-number</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>is-number-object</td>
          <td>1.0.4</td>
          <td>MIT</td>
          <td>git://github.com/inspect-js/is-number-object.git</td>
          <td>Unknown</td>
          <td>Jordan Harband</td>
          </tr>
          <tr>
          <td>is-obj</td>
          <td>2.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/is-obj.git">https://github.com/sindresorhus/is-obj.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>is-path-cwd</td>
          <td>2.2.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/is-path-cwd.git">https://github.com/sindresorhus/is-path-cwd.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>is-path-in-cwd</td>
          <td>2.1.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/is-path-in-cwd.git">https://github.com/sindresorhus/is-path-in-cwd.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>is-path-inside</td>
          <td>2.1.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/is-path-inside.git">https://github.com/sindresorhus/is-path-inside.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>is-path-inside</td>
          <td>3.0.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/is-path-inside.git">https://github.com/sindresorhus/is-path-inside.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>is-plain-obj</td>
          <td>1.1.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/is-plain-obj.git">https://github.com/sindresorhus/is-plain-obj.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>is-plain-object</td>
          <td>2.0.4</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/is-plain-object.git">https://github.com/jonschlinkert/is-plain-object.git</a></td>
          <td><a href="https://github.com/jonschlinkert/is-plain-object">https://github.com/jonschlinkert/is-plain-object</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>is-plain-object</td>
          <td>5.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/is-plain-object.git">https://github.com/jonschlinkert/is-plain-object.git</a></td>
          <td><a href="https://github.com/jonschlinkert/is-plain-object">https://github.com/jonschlinkert/is-plain-object</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>is-potential-custom-element-name</td>
          <td>1.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/mathiasbynens/is-potential-custom-element-name.git">https://github.com/mathiasbynens/is-potential-custom-element-name.git</a></td>
          <td><a href="https://github.com/mathiasbynens/is-potential-custom-element-name">https://github.com/mathiasbynens/is-potential-custom-element-name</a></td>
          <td>Mathias Bynens</td>
          </tr>
          <tr>
          <td>is-promise</td>
          <td>4.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/then/is-promise.git">https://github.com/then/is-promise.git</a></td>
          <td>Unknown</td>
          <td>ForbesLindesay</td>
          </tr>
          <tr>
          <td>is-regex</td>
          <td>1.1.2</td>
          <td>MIT</td>
          <td>git://github.com/inspect-js/is-regex.git</td>
          <td><a href="https://github.com/inspect-js/is-regex">https://github.com/inspect-js/is-regex</a></td>
          <td>Jordan Harband</td>
          </tr>
          <tr>
          <td>is-stream</td>
          <td>1.1.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/is-stream.git">https://github.com/sindresorhus/is-stream.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>is-stream</td>
          <td>2.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/is-stream.git">https://github.com/sindresorhus/is-stream.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>is-string</td>
          <td>1.0.5</td>
          <td>MIT</td>
          <td>git://github.com/ljharb/is-string.git</td>
          <td>Unknown</td>
          <td>Jordan Harband</td>
          </tr>
          <tr>
          <td>is-svg</td>
          <td>4.3.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/is-svg.git">https://github.com/sindresorhus/is-svg.git</a></td>
          <td><a href="https://sindresorhus.com">https://sindresorhus.com</a></td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>is-svg</td>
          <td>3.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/is-svg.git">https://github.com/sindresorhus/is-svg.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>is-symbol</td>
          <td>1.0.3</td>
          <td>MIT</td>
          <td>git://github.com/inspect-js/is-symbol.git</td>
          <td>Unknown</td>
          <td>Jordan Harband</td>
          </tr>
          <tr>
          <td>is-typedarray</td>
          <td>1.0.0</td>
          <td>MIT</td>
          <td>git://github.com/hughsk/is-typedarray.git</td>
          <td><a href="https://github.com/hughsk/is-typedarray">https://github.com/hughsk/is-typedarray</a></td>
          <td>Hugh Kennedy</td>
          </tr>
          <tr>
          <td>is-whitespace</td>
          <td>0.3.0</td>
          <td>MIT</td>
          <td>git://github.com/jonschlinkert/is-whitespace.git</td>
          <td><a href="https://github.com/jonschlinkert/is-whitespace">https://github.com/jonschlinkert/is-whitespace</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>is-windows</td>
          <td>1.0.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/is-windows.git">https://github.com/jonschlinkert/is-windows.git</a></td>
          <td><a href="https://github.com/jonschlinkert/is-windows">https://github.com/jonschlinkert/is-windows</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>is-wsl</td>
          <td>1.1.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/is-wsl.git">https://github.com/sindresorhus/is-wsl.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>is-wsl</td>
          <td>2.2.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/is-wsl.git">https://github.com/sindresorhus/is-wsl.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>is-yarn-global</td>
          <td>0.3.0</td>
          <td>MIT</td>
          <td>git@github.com:LitoMore/is-yarn-global.git</td>
          <td>litomore@gmail.com</td>
          <td>LitoMore</td>
          </tr>
          <tr>
          <td>isarray</td>
          <td>1.0.0</td>
          <td>MIT</td>
          <td>git://github.com/juliangruber/isarray.git</td>
          <td><a href="https://github.com/juliangruber/isarray">https://github.com/juliangruber/isarray</a></td>
          <td>Julian Gruber</td>
          </tr>
          <tr>
          <td>isobject</td>
          <td>3.0.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/isobject.git">https://github.com/jonschlinkert/isobject.git</a></td>
          <td><a href="https://github.com/jonschlinkert/isobject">https://github.com/jonschlinkert/isobject</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>isobject</td>
          <td>2.1.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/isobject.git">https://github.com/jonschlinkert/isobject.git</a></td>
          <td><a href="https://github.com/jonschlinkert/isobject">https://github.com/jonschlinkert/isobject</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>isstream</td>
          <td>0.1.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/rvagg/isstream.git">https://github.com/rvagg/isstream.git</a></td>
          <td><a href="https://github.com/rvagg/isstream">https://github.com/rvagg/isstream</a></td>
          <td>Rod Vagg</td>
          </tr>
          <tr>
          <td>iterall</td>
          <td>1.3.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/leebyron/iterall.git">https://github.com/leebyron/iterall.git</a></td>
          <td><a href="https://github.com/leebyron/iterall">https://github.com/leebyron/iterall</a></td>
          <td>Lee Byron</td>
          </tr>
          <tr>
          <td>javascript-stringify</td>
          <td>2.0.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/blakeembrey/javascript-stringify.git">https://github.com/blakeembrey/javascript-stringify.git</a></td>
          <td><a href="https://github.com/blakeembrey/javascript-stringify">https://github.com/blakeembrey/javascript-stringify</a></td>
          <td>Blake Embrey</td>
          </tr>
          <tr>
          <td>jest-worker</td>
          <td>25.5.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/facebook/jest.git">https://github.com/facebook/jest.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>js-beautify</td>
          <td>1.13.5</td>
          <td>MIT</td>
          <td>git://github.com/beautify-web/js-beautify.git</td>
          <td><a href="https://beautifier.io/">https://beautifier.io/</a></td>
          <td>Einar Lielmanis</td>
          </tr>
          <tr>
          <td>js-message</td>
          <td>1.0.7</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/RIAEvangelist/js-message.git">https://github.com/RIAEvangelist/js-message.git</a></td>
          <td><a href="https://github.com/RIAEvangelist/js-message#readme">https://github.com/RIAEvangelist/js-message#readme</a></td>
          <td>Brandon Nozaki Miller</td>
          </tr>
          <tr>
          <td>js-queue</td>
          <td>2.0.2</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/RIAEvangelist/js-queue.git">https://github.com/RIAEvangelist/js-queue.git</a></td>
          <td><a href="https://github.com/RIAEvangelist/js-queue#readme">https://github.com/RIAEvangelist/js-queue#readme</a></td>
          <td>Brandon Nozaki Miller</td>
          </tr>
          <tr>
          <td>js-string-escape</td>
          <td>1.0.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/joliss/js-string-escape">https://github.com/joliss/js-string-escape</a></td>
          <td>Unknown</td>
          <td>Jo Liss</td>
          </tr>
          <tr>
          <td>js-tokens</td>
          <td>4.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/lydell/js-tokens.git">https://github.com/lydell/js-tokens.git</a></td>
          <td>Unknown</td>
          <td>Simon Lydell</td>
          </tr>
          <tr>
          <td>js-yaml</td>
          <td>3.14.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/nodeca/js-yaml.git">https://github.com/nodeca/js-yaml.git</a></td>
          <td><a href="https://github.com/nodeca/js-yaml">https://github.com/nodeca/js-yaml</a></td>
          <td>Vladimir Zapparov</td>
          </tr>
          <tr>
          <td>jsbn</td>
          <td>0.1.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/andyperlitch/jsbn.git">https://github.com/andyperlitch/jsbn.git</a></td>
          <td>Unknown</td>
          <td>Tom Wu</td>
          </tr>
          <tr>
          <td>jsdom</td>
          <td>16.4.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/jsdom/jsdom.git">https://github.com/jsdom/jsdom.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>jsdom-global</td>
          <td>3.0.2</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/rstacruz/jsdom-global.git">https://github.com/rstacruz/jsdom-global.git</a></td>
          <td><a href="https://github.com/rstacruz/jsdom-global#readme">https://github.com/rstacruz/jsdom-global#readme</a></td>
          <td>Rico Sta. Cruz</td>
          </tr>
          <tr>
          <td>jsesc</td>
          <td>2.5.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/mathiasbynens/jsesc.git">https://github.com/mathiasbynens/jsesc.git</a></td>
          <td><a href="https://mths.be/jsesc">https://mths.be/jsesc</a></td>
          <td>Mathias Bynens</td>
          </tr>
          <tr>
          <td>jsesc</td>
          <td>0.5.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/mathiasbynens/jsesc.git">https://github.com/mathiasbynens/jsesc.git</a></td>
          <td><a href="http://mths.be/jsesc">http://mths.be/jsesc</a></td>
          <td>Mathias Bynens</td>
          </tr>
          <tr>
          <td>json-buffer</td>
          <td>3.0.0</td>
          <td>MIT</td>
          <td>git://github.com/dominictarr/json-buffer.git</td>
          <td><a href="https://github.com/dominictarr/json-buffer">https://github.com/dominictarr/json-buffer</a></td>
          <td>Dominic Tarr</td>
          </tr>
          <tr>
          <td>json-parse-better-errors</td>
          <td>1.0.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/zkat/json-parse-better-errors">https://github.com/zkat/json-parse-better-errors</a></td>
          <td>Unknown</td>
          <td>Kat Marchán</td>
          </tr>
          <tr>
          <td>json-parse-even-better-errors</td>
          <td>2.3.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/npm/json-parse-even-better-errors">https://github.com/npm/json-parse-even-better-errors</a></td>
          <td>Unknown</td>
          <td>Kat Marchán</td>
          </tr>
          <tr>
          <td>json-schema-traverse</td>
          <td>0.4.1</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/epoberezkin/json-schema-traverse.git">https://github.com/epoberezkin/json-schema-traverse.git</a></td>
          <td><a href="https://github.com/epoberezkin/json-schema-traverse#readme">https://github.com/epoberezkin/json-schema-traverse#readme</a></td>
          <td>Evgeny Poberezkin</td>
          </tr>
          <tr>
          <td>json-stable-stringify-without-jsonify</td>
          <td>1.0.1</td>
          <td>MIT</td>
          <td>git://github.com/samn/json-stable-stringify.git</td>
          <td><a href="https://github.com/samn/json-stable-stringify">https://github.com/samn/json-stable-stringify</a></td>
          <td>James Halliday</td>
          </tr>
          <tr>
          <td>json3</td>
          <td>3.3.3</td>
          <td>MIT</td>
          <td>git://github.com/bestiejs/json3.git</td>
          <td><a href="https://bestiejs.github.io/json3">https://bestiejs.github.io/json3</a></td>
          <td>Kit Cambridge</td>
          </tr>
          <tr>
          <td>json5</td>
          <td>2.2.0</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/json5/json5.git">https://github.com/json5/json5.git</a></td>
          <td><a href="http://json5.org/">http://json5.org/</a></td>
          <td>Aseem Kishore</td>
          </tr>
          <tr>
          <td>json5</td>
          <td>1.0.1</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/json5/json5.git">https://github.com/json5/json5.git</a></td>
          <td><a href="http://json5.org/">http://json5.org/</a></td>
          <td>Aseem Kishore</td>
          </tr>
          <tr>
          <td>json5</td>
          <td>0.5.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/aseemk/json5.git">https://github.com/aseemk/json5.git</a></td>
          <td><a href="http://json5.org/">http://json5.org/</a></td>
          <td>Aseem Kishore</td>
          </tr>
          <tr>
          <td>jsonfile</td>
          <td>4.0.0</td>
          <td>MIT</td>
          <td>git@github.com:jprichardson/node-jsonfile.git</td>
          <td>Unknown</td>
          <td>JP Richardson</td>
          </tr>
          <tr>
          <td>jsprim</td>
          <td>1.4.1</td>
          <td>MIT</td>
          <td>git://github.com/joyent/node-jsprim.git</td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>keyv</td>
          <td>3.1.0</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/lukechilds/keyv.git">https://github.com/lukechilds/keyv.git</a></td>
          <td><a href="https://github.com/lukechilds/keyv">https://github.com/lukechilds/keyv</a></td>
          <td>Luke Childs</td>
          </tr>
          <tr>
          <td>kind-of</td>
          <td>3.2.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/kind-of.git">https://github.com/jonschlinkert/kind-of.git</a></td>
          <td><a href="https://github.com/jonschlinkert/kind-of">https://github.com/jonschlinkert/kind-of</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>kind-of</td>
          <td>6.0.3</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/kind-of.git">https://github.com/jonschlinkert/kind-of.git</a></td>
          <td><a href="https://github.com/jonschlinkert/kind-of">https://github.com/jonschlinkert/kind-of</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>kind-of</td>
          <td>5.1.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/kind-of.git">https://github.com/jonschlinkert/kind-of.git</a></td>
          <td><a href="https://github.com/jonschlinkert/kind-of">https://github.com/jonschlinkert/kind-of</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>kind-of</td>
          <td>4.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/kind-of.git">https://github.com/jonschlinkert/kind-of.git</a></td>
          <td><a href="https://github.com/jonschlinkert/kind-of">https://github.com/jonschlinkert/kind-of</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>latest-version</td>
          <td>5.1.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/latest-version.git">https://github.com/sindresorhus/latest-version.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>launch-editor</td>
          <td>2.2.1</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/yyx990803/launch-editor.git">https://github.com/yyx990803/launch-editor.git</a></td>
          <td><a href="https://github.com/yyx990803/launch-editor#readme">https://github.com/yyx990803/launch-editor#readme</a></td>
          <td>Evan You</td>
          </tr>
          <tr>
          <td>launch-editor-middleware</td>
          <td>2.2.1</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/yyx990803/launch-editor.git">https://github.com/yyx990803/launch-editor.git</a></td>
          <td><a href="https://github.com/yyx990803/launch-editor#readme">https://github.com/yyx990803/launch-editor#readme</a></td>
          <td>Evan You</td>
          </tr>
          <tr>
          <td>levn</td>
          <td>0.3.0</td>
          <td>MIT</td>
          <td>git://github.com/gkz/levn.git</td>
          <td><a href="https://github.com/gkz/levn">https://github.com/gkz/levn</a></td>
          <td>George Zahariev</td>
          </tr>
          <tr>
          <td>lines-and-columns</td>
          <td>1.1.6</td>
          <td>MIT</td>
          <td><a href="https://github.com/eventualbuddha/lines-and-columns.git">https://github.com/eventualbuddha/lines-and-columns.git</a></td>
          <td><a href="https://github.com/eventualbuddha/lines-and-columns#readme">https://github.com/eventualbuddha/lines-and-columns#readme</a></td>
          <td>Brian Donovan</td>
          </tr>
          <tr>
          <td>load-json-file</td>
          <td>2.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/load-json-file.git">https://github.com/sindresorhus/load-json-file.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>load-json-file</td>
          <td>5.3.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/load-json-file.git">https://github.com/sindresorhus/load-json-file.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>loader-fs-cache</td>
          <td>1.0.3</td>
          <td>MIT</td>
          <td><a href="https://github.com/viankakrisna/loader-fs-cache.git">https://github.com/viankakrisna/loader-fs-cache.git</a></td>
          <td>Unknown</td>
          <td>Ade Viankakrisna Fadlil</td>
          </tr>
          <tr>
          <td>loader-runner</td>
          <td>2.4.0</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/webpack/loader-runner.git">https://github.com/webpack/loader-runner.git</a></td>
          <td><a href="https://github.com/webpack/loader-runner#readme">https://github.com/webpack/loader-runner#readme</a></td>
          <td>Tobias Koppers @sokra</td>
          </tr>
          <tr>
          <td>loader-utils</td>
          <td>1.4.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/webpack/loader-utils.git">https://github.com/webpack/loader-utils.git</a></td>
          <td>Unknown</td>
          <td>Tobias Koppers @sokra</td>
          </tr>
          <tr>
          <td>loader-utils</td>
          <td>0.2.17</td>
          <td>MIT</td>
          <td><a href="https://github.com/webpack/loader-utils.git">https://github.com/webpack/loader-utils.git</a></td>
          <td>Unknown</td>
          <td>Tobias Koppers @sokra</td>
          </tr>
          <tr>
          <td>loader-utils</td>
          <td>2.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/webpack/loader-utils.git">https://github.com/webpack/loader-utils.git</a></td>
          <td>Unknown</td>
          <td>Tobias Koppers @sokra</td>
          </tr>
          <tr>
          <td>locate-path</td>
          <td>5.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/locate-path.git">https://github.com/sindresorhus/locate-path.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>locate-path</td>
          <td>3.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/locate-path.git">https://github.com/sindresorhus/locate-path.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>locate-path</td>
          <td>2.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/locate-path.git">https://github.com/sindresorhus/locate-path.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>lodash</td>
          <td>4.17.21</td>
          <td>MIT</td>
          <td><a href="https://github.com/lodash/lodash.git">https://github.com/lodash/lodash.git</a></td>
          <td><a href="https://lodash.com/">https://lodash.com/</a></td>
          <td>John-David Dalton</td>
          </tr>
          <tr>
          <td>lodash.debounce</td>
          <td>4.0.8</td>
          <td>MIT</td>
          <td><a href="https://github.com/lodash/lodash.git">https://github.com/lodash/lodash.git</a></td>
          <td><a href="https://lodash.com/">https://lodash.com/</a></td>
          <td>John-David Dalton</td>
          </tr>
          <tr>
          <td>lodash.defaultsdeep</td>
          <td>4.6.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/lodash/lodash.git">https://github.com/lodash/lodash.git</a></td>
          <td><a href="https://lodash.com/">https://lodash.com/</a></td>
          <td>John-David Dalton</td>
          </tr>
          <tr>
          <td>lodash.kebabcase</td>
          <td>4.1.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/lodash/lodash.git">https://github.com/lodash/lodash.git</a></td>
          <td><a href="https://lodash.com/">https://lodash.com/</a></td>
          <td>John-David Dalton</td>
          </tr>
          <tr>
          <td>lodash.mapvalues</td>
          <td>4.6.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/lodash/lodash.git">https://github.com/lodash/lodash.git</a></td>
          <td><a href="https://lodash.com/">https://lodash.com/</a></td>
          <td>John-David Dalton</td>
          </tr>
          <tr>
          <td>lodash.memoize</td>
          <td>4.1.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/lodash/lodash.git">https://github.com/lodash/lodash.git</a></td>
          <td><a href="https://lodash.com/">https://lodash.com/</a></td>
          <td>John-David Dalton</td>
          </tr>
          <tr>
          <td>lodash.sortby</td>
          <td>4.7.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/lodash/lodash.git">https://github.com/lodash/lodash.git</a></td>
          <td><a href="https://lodash.com/">https://lodash.com/</a></td>
          <td>John-David Dalton</td>
          </tr>
          <tr>
          <td>lodash.transform</td>
          <td>4.6.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/lodash/lodash.git">https://github.com/lodash/lodash.git</a></td>
          <td><a href="https://lodash.com/">https://lodash.com/</a></td>
          <td>John-David Dalton</td>
          </tr>
          <tr>
          <td>lodash.uniq</td>
          <td>4.5.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/lodash/lodash.git">https://github.com/lodash/lodash.git</a></td>
          <td><a href="https://lodash.com/">https://lodash.com/</a></td>
          <td>John-David Dalton</td>
          </tr>
          <tr>
          <td>log-symbols</td>
          <td>2.2.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/log-symbols.git">https://github.com/sindresorhus/log-symbols.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>log-symbols</td>
          <td>4.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/log-symbols.git">https://github.com/sindresorhus/log-symbols.git</a></td>
          <td><a href="https://sindresorhus.com">https://sindresorhus.com</a></td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>loglevel</td>
          <td>1.7.1</td>
          <td>MIT</td>
          <td>git://github.com/pimterry/loglevel.git</td>
          <td><a href="https://github.com/pimterry/loglevel">https://github.com/pimterry/loglevel</a></td>
          <td>Tim Perry</td>
          </tr>
          <tr>
          <td>lower-case</td>
          <td>1.1.4</td>
          <td>MIT</td>
          <td>git://github.com/blakeembrey/lower-case.git</td>
          <td><a href="https://github.com/blakeembrey/lower-case">https://github.com/blakeembrey/lower-case</a></td>
          <td>Blake Embrey</td>
          </tr>
          <tr>
          <td>lowercase-keys</td>
          <td>1.0.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/lowercase-keys.git">https://github.com/sindresorhus/lowercase-keys.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>lowercase-keys</td>
          <td>2.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/lowercase-keys.git">https://github.com/sindresorhus/lowercase-keys.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>make-dir</td>
          <td>3.1.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/make-dir.git">https://github.com/sindresorhus/make-dir.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>make-dir</td>
          <td>2.1.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/make-dir.git">https://github.com/sindresorhus/make-dir.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>map-age-cleaner</td>
          <td>0.1.3</td>
          <td>MIT</td>
          <td><a href="https://github.com/SamVerschueren/map-age-cleaner.git">https://github.com/SamVerschueren/map-age-cleaner.git</a></td>
          <td>github.com/SamVerschueren</td>
          <td>Sam Verschueren</td>
          </tr>
          <tr>
          <td>map-cache</td>
          <td>0.2.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/map-cache.git">https://github.com/jonschlinkert/map-cache.git</a></td>
          <td><a href="https://github.com/jonschlinkert/map-cache">https://github.com/jonschlinkert/map-cache</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>map-visit</td>
          <td>1.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/map-visit.git">https://github.com/jonschlinkert/map-visit.git</a></td>
          <td><a href="https://github.com/jonschlinkert/map-visit">https://github.com/jonschlinkert/map-visit</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>matcher</td>
          <td>3.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/matcher.git">https://github.com/sindresorhus/matcher.git</a></td>
          <td><a href="https://sindresorhus.com">https://sindresorhus.com</a></td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>md5-hex</td>
          <td>3.0.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/md5-hex.git">https://github.com/sindresorhus/md5-hex.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>md5.js</td>
          <td>1.3.5</td>
          <td>MIT</td>
          <td><a href="https://github.com/crypto-browserify/md5.js.git">https://github.com/crypto-browserify/md5.js.git</a></td>
          <td><a href="https://github.com/crypto-browserify/md5.js">https://github.com/crypto-browserify/md5.js</a></td>
          <td>Kirill Fomichev</td>
          </tr>
          <tr>
          <td>media-typer</td>
          <td>0.3.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/jshttp/media-typer.git">https://github.com/jshttp/media-typer.git</a></td>
          <td>Unknown</td>
          <td>Douglas Christopher Wilson</td>
          </tr>
          <tr>
          <td>mem</td>
          <td>8.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/mem.git">https://github.com/sindresorhus/mem.git</a></td>
          <td><a href="https://sindresorhus.com">https://sindresorhus.com</a></td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>memory-fs</td>
          <td>0.4.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/webpack/memory-fs.git">https://github.com/webpack/memory-fs.git</a></td>
          <td><a href="https://github.com/webpack/memory-fs">https://github.com/webpack/memory-fs</a></td>
          <td>Tobias Koppers @sokra</td>
          </tr>
          <tr>
          <td>memory-fs</td>
          <td>0.5.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/webpack/memory-fs.git">https://github.com/webpack/memory-fs.git</a></td>
          <td><a href="https://github.com/webpack/memory-fs">https://github.com/webpack/memory-fs</a></td>
          <td>Tobias Koppers @sokra</td>
          </tr>
          <tr>
          <td>memory-fs</td>
          <td>0.2.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/webpack/memory-fs.git">https://github.com/webpack/memory-fs.git</a></td>
          <td><a href="https://github.com/webpack/memory-fs">https://github.com/webpack/memory-fs</a></td>
          <td>Tobias Koppers @sokra</td>
          </tr>
          <tr>
          <td>merge-descriptors</td>
          <td>1.0.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/component/merge-descriptors.git">https://github.com/component/merge-descriptors.git</a></td>
          <td><a href="http://jongleberry.com">http://jongleberry.com</a></td>
          <td>Jonathan Ong</td>
          </tr>
          <tr>
          <td>merge-source-map</td>
          <td>1.1.0</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/keik/merge-source-map.git">https://github.com/keik/merge-source-map.git</a></td>
          <td>Unknown</td>
          <td>keik</td>
          </tr>
          <tr>
          <td>merge-stream</td>
          <td>2.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/grncdr/merge-stream.git">https://github.com/grncdr/merge-stream.git</a></td>
          <td>Unknown</td>
          <td>Stephen Sugden</td>
          </tr>
          <tr>
          <td>merge2</td>
          <td>1.4.1</td>
          <td>MIT</td>
          <td>git@github.com:teambition/merge2.git</td>
          <td><a href="https://github.com/teambition/merge2">https://github.com/teambition/merge2</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>methods</td>
          <td>1.1.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/jshttp/methods.git">https://github.com/jshttp/methods.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>micromatch</td>
          <td>3.1.10</td>
          <td>MIT</td>
          <td><a href="https://github.com/micromatch/micromatch.git">https://github.com/micromatch/micromatch.git</a></td>
          <td><a href="https://github.com/micromatch/micromatch">https://github.com/micromatch/micromatch</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>micromatch</td>
          <td>4.0.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/micromatch/micromatch.git">https://github.com/micromatch/micromatch.git</a></td>
          <td><a href="https://github.com/micromatch/micromatch">https://github.com/micromatch/micromatch</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>miller-rabin</td>
          <td>4.0.1</td>
          <td>MIT</td>
          <td>git@github.com:indutny/miller-rabin</td>
          <td><a href="https://github.com/indutny/miller-rabin">https://github.com/indutny/miller-rabin</a></td>
          <td>Fedor Indutny</td>
          </tr>
          <tr>
          <td>mime</td>
          <td>1.6.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/broofa/node-mime">https://github.com/broofa/node-mime</a></td>
          <td><a href="http://github.com/broofa">http://github.com/broofa</a></td>
          <td>Robert Kieffer</td>
          </tr>
          <tr>
          <td>mime</td>
          <td>2.5.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/broofa/mime">https://github.com/broofa/mime</a></td>
          <td><a href="http://github.com/broofa">http://github.com/broofa</a></td>
          <td>Robert Kieffer</td>
          </tr>
          <tr>
          <td>mime-db</td>
          <td>1.46.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/jshttp/mime-db.git">https://github.com/jshttp/mime-db.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>mime-types</td>
          <td>2.1.29</td>
          <td>MIT</td>
          <td><a href="https://github.com/jshttp/mime-types.git">https://github.com/jshttp/mime-types.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>mimic-fn</td>
          <td>1.2.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/mimic-fn.git">https://github.com/sindresorhus/mimic-fn.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>mimic-fn</td>
          <td>2.1.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/mimic-fn.git">https://github.com/sindresorhus/mimic-fn.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>mimic-fn</td>
          <td>3.1.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/mimic-fn.git">https://github.com/sindresorhus/mimic-fn.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>mimic-response</td>
          <td>1.0.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/mimic-response.git">https://github.com/sindresorhus/mimic-response.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>mini-css-extract-plugin</td>
          <td>0.9.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/webpack-contrib/mini-css-extract-plugin.git">https://github.com/webpack-contrib/mini-css-extract-plugin.git</a></td>
          <td><a href="https://github.com/webpack-contrib/mini-css-extract-plugin">https://github.com/webpack-contrib/mini-css-extract-plugin</a></td>
          <td>Tobias Koppers @sokra</td>
          </tr>
          <tr>
          <td>minimalistic-crypto-utils</td>
          <td>1.0.1</td>
          <td>MIT</td>
          <td>git+ssh://git@github.com/indutny/minimalistic-crypto-utils.git</td>
          <td><a href="https://github.com/indutny/minimalistic-crypto-utils#readme">https://github.com/indutny/minimalistic-crypto-utils#readme</a></td>
          <td>Fedor Indutny</td>
          </tr>
          <tr>
          <td>minimist</td>
          <td>1.2.5</td>
          <td>MIT</td>
          <td>git://github.com/substack/minimist.git</td>
          <td><a href="https://github.com/substack/minimist">https://github.com/substack/minimist</a></td>
          <td>James Halliday</td>
          </tr>
          <tr>
          <td>mixin-deep</td>
          <td>1.3.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/mixin-deep.git">https://github.com/jonschlinkert/mixin-deep.git</a></td>
          <td><a href="https://github.com/jonschlinkert/mixin-deep">https://github.com/jonschlinkert/mixin-deep</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>mkdirp</td>
          <td>1.0.4</td>
          <td>MIT</td>
          <td><a href="https://github.com/isaacs/node-mkdirp.git">https://github.com/isaacs/node-mkdirp.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>mkdirp</td>
          <td>0.5.5</td>
          <td>MIT</td>
          <td><a href="https://github.com/substack/node-mkdirp.git">https://github.com/substack/node-mkdirp.git</a></td>
          <td><a href="http://substack.net">http://substack.net</a></td>
          <td>James Halliday</td>
          </tr>
          <tr>
          <td>ms</td>
          <td>2.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/zeit/ms.git">https://github.com/zeit/ms.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>ms</td>
          <td>2.1.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/zeit/ms.git">https://github.com/zeit/ms.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>ms</td>
          <td>2.1.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/zeit/ms.git">https://github.com/zeit/ms.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>ms</td>
          <td>2.1.3</td>
          <td>MIT</td>
          <td><a href="https://github.com/vercel/ms.git">https://github.com/vercel/ms.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>multicast-dns</td>
          <td>6.2.3</td>
          <td>MIT</td>
          <td><a href="https://github.com/mafintosh/multicast-dns.git">https://github.com/mafintosh/multicast-dns.git</a></td>
          <td><a href="https://github.com/mafintosh/multicast-dns">https://github.com/mafintosh/multicast-dns</a></td>
          <td>Mathias Buus</td>
          </tr>
          <tr>
          <td>multicast-dns-service-types</td>
          <td>1.1.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/mafintosh/multicast-dns-service-types.git">https://github.com/mafintosh/multicast-dns-service-types.git</a></td>
          <td><a href="https://github.com/mafintosh/multicast-dns-service-types">https://github.com/mafintosh/multicast-dns-service-types</a></td>
          <td>Mathias Buus</td>
          </tr>
          <tr>
          <td>mustache</td>
          <td>3.0.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/janl/mustache.js.git">https://github.com/janl/mustache.js.git</a></td>
          <td><a href="https://github.com/janl/mustache.js">https://github.com/janl/mustache.js</a></td>
          <td>mustache.js Authors</td>
          </tr>
          <tr>
          <td>mz</td>
          <td>2.7.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/normalize/mz.git">https://github.com/normalize/mz.git</a></td>
          <td><a href="http://jongleberry.com">http://jongleberry.com</a></td>
          <td>Jonathan Ong</td>
          </tr>
          <tr>
          <td>nan</td>
          <td>2.14.2</td>
          <td>MIT</td>
          <td>git://github.com/nodejs/nan.git</td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>nanomatch</td>
          <td>1.2.13</td>
          <td>MIT</td>
          <td><a href="https://github.com/micromatch/nanomatch.git">https://github.com/micromatch/nanomatch.git</a></td>
          <td><a href="https://github.com/micromatch/nanomatch">https://github.com/micromatch/nanomatch</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>natural-compare</td>
          <td>1.4.0</td>
          <td>MIT</td>
          <td>git://github.com/litejs/natural-compare-lite.git</td>
          <td><a href="https://github.com/litejs/natural-compare-lite">https://github.com/litejs/natural-compare-lite</a></td>
          <td>Lauri Rooden</td>
          </tr>
          <tr>
          <td>negotiator</td>
          <td>0.6.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/jshttp/negotiator.git">https://github.com/jshttp/negotiator.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>neo-async</td>
          <td>2.6.2</td>
          <td>MIT</td>
          <td>git@github.com:suguru03/neo-async.git</td>
          <td><a href="https://github.com/suguru03/neo-async">https://github.com/suguru03/neo-async</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>nice-try</td>
          <td>1.0.5</td>
          <td>MIT</td>
          <td><a href="https://github.com/electerious/nice-try.git">https://github.com/electerious/nice-try.git</a></td>
          <td><a href="https://github.com/electerious/nice-try">https://github.com/electerious/nice-try</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>no-case</td>
          <td>2.3.2</td>
          <td>MIT</td>
          <td>git://github.com/blakeembrey/no-case.git</td>
          <td><a href="https://github.com/blakeembrey/no-case">https://github.com/blakeembrey/no-case</a></td>
          <td>Blake Embrey</td>
          </tr>
          <tr>
          <td>node-ipc</td>
          <td>9.1.4</td>
          <td>MIT</td>
          <td><a href="https://github.com/RIAEvangelist/node-ipc.git">https://github.com/RIAEvangelist/node-ipc.git</a></td>
          <td><a href="http://riaevangelist.github.io/node-ipc/">http://riaevangelist.github.io/node-ipc/</a></td>
          <td>Brandon Nozaki Miller</td>
          </tr>
          <tr>
          <td>node-libs-browser</td>
          <td>2.2.1</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/webpack/node-libs-browser.git">https://github.com/webpack/node-libs-browser.git</a></td>
          <td><a href="http://github.com/webpack/node-libs-browser">http://github.com/webpack/node-libs-browser</a></td>
          <td>Tobias Koppers @sokra</td>
          </tr>
          <tr>
          <td>node-releases</td>
          <td>1.1.72</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/chicoxyzzy/node-releases.git">https://github.com/chicoxyzzy/node-releases.git</a></td>
          <td>Unknown</td>
          <td>Sergey Rubanov</td>
          </tr>
          <tr>
          <td>normalize-path</td>
          <td>3.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/normalize-path.git">https://github.com/jonschlinkert/normalize-path.git</a></td>
          <td><a href="https://github.com/jonschlinkert/normalize-path">https://github.com/jonschlinkert/normalize-path</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>normalize-path</td>
          <td>2.1.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/normalize-path.git">https://github.com/jonschlinkert/normalize-path.git</a></td>
          <td><a href="https://github.com/jonschlinkert/normalize-path">https://github.com/jonschlinkert/normalize-path</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>normalize-path</td>
          <td>1.0.0</td>
          <td>MIT</td>
          <td>git://github.com/jonschlinkert/normalize-path.git</td>
          <td><a href="https://github.com/jonschlinkert/normalize-path">https://github.com/jonschlinkert/normalize-path</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>normalize-range</td>
          <td>0.1.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/jamestalmage/normalize-range.git">https://github.com/jamestalmage/normalize-range.git</a></td>
          <td>github.com/jamestalmage</td>
          <td>James Talmage</td>
          </tr>
          <tr>
          <td>normalize-url</td>
          <td>4.5.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/normalize-url.git">https://github.com/sindresorhus/normalize-url.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>normalize-url</td>
          <td>1.9.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/normalize-url.git">https://github.com/sindresorhus/normalize-url.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>normalize-url</td>
          <td>3.3.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/normalize-url.git">https://github.com/sindresorhus/normalize-url.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>normalize-url</td>
          <td>4.5.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/normalize-url.git">https://github.com/sindresorhus/normalize-url.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>npm-run-path</td>
          <td>2.0.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/npm-run-path.git">https://github.com/sindresorhus/npm-run-path.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>npm-run-path</td>
          <td>4.0.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/npm-run-path.git">https://github.com/sindresorhus/npm-run-path.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>null-loader</td>
          <td>3.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/webpack-contrib/null-loader.git">https://github.com/webpack-contrib/null-loader.git</a></td>
          <td><a href="https://github.com/webpack-contrib/null-loader">https://github.com/webpack-contrib/null-loader</a></td>
          <td>Tobias Koppers @sokra</td>
          </tr>
          <tr>
          <td>num2fraction</td>
          <td>1.2.2</td>
          <td>MIT</td>
          <td>git@github.com:yisibl/num2fraction.git</td>
          <td><a href="http://iyunlu.com/view">http://iyunlu.com/view</a></td>
          <td>yisi</td>
          </tr>
          <tr>
          <td>nwsapi</td>
          <td>2.2.0</td>
          <td>MIT</td>
          <td>git://github.com/dperini/nwsapi.git</td>
          <td><a href="http://javascript.nwbox.com/nwsapi/">http://javascript.nwbox.com/nwsapi/</a></td>
          <td>Diego Perini</td>
          </tr>
          <tr>
          <td>object-assign</td>
          <td>4.1.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/object-assign.git">https://github.com/sindresorhus/object-assign.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>object-copy</td>
          <td>0.1.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/object-copy.git">https://github.com/jonschlinkert/object-copy.git</a></td>
          <td><a href="https://github.com/jonschlinkert/object-copy">https://github.com/jonschlinkert/object-copy</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>object-hash</td>
          <td>1.3.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/puleos/object-hash">https://github.com/puleos/object-hash</a></td>
          <td><a href="https://github.com/puleos/object-hash">https://github.com/puleos/object-hash</a></td>
          <td>Scott Puleo</td>
          </tr>
          <tr>
          <td>object-inspect</td>
          <td>1.9.0</td>
          <td>MIT</td>
          <td>git://github.com/inspect-js/object-inspect.git</td>
          <td><a href="https://github.com/inspect-js/object-inspect">https://github.com/inspect-js/object-inspect</a></td>
          <td>James Halliday</td>
          </tr>
          <tr>
          <td>object-is</td>
          <td>1.1.5</td>
          <td>MIT</td>
          <td>git://github.com/es-shims/object-is.git</td>
          <td><a href="https://github.com/es-shims/object-is">https://github.com/es-shims/object-is</a></td>
          <td>Jordan Harband</td>
          </tr>
          <tr>
          <td>object-keys</td>
          <td>1.1.1</td>
          <td>MIT</td>
          <td>git://github.com/ljharb/object-keys.git</td>
          <td><a href="http://ljharb.codes">http://ljharb.codes</a></td>
          <td>Jordan Harband</td>
          </tr>
          <tr>
          <td>object-visit</td>
          <td>1.0.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/object-visit.git">https://github.com/jonschlinkert/object-visit.git</a></td>
          <td><a href="https://github.com/jonschlinkert/object-visit">https://github.com/jonschlinkert/object-visit</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>object.assign</td>
          <td>4.1.2</td>
          <td>MIT</td>
          <td>git://github.com/ljharb/object.assign.git</td>
          <td>Unknown</td>
          <td>Jordan Harband</td>
          </tr>
          <tr>
          <td>object.entries</td>
          <td>1.1.3</td>
          <td>MIT</td>
          <td>git://github.com/es-shims/Object.entries.git</td>
          <td>Unknown</td>
          <td>Jordan Harband</td>
          </tr>
          <tr>
          <td>object.getownpropertydescriptors</td>
          <td>2.1.2</td>
          <td>MIT</td>
          <td>git://github.com/es-shims/object.getownpropertydescriptors.git</td>
          <td>Unknown</td>
          <td>Jordan Harband</td>
          </tr>
          <tr>
          <td>object.pick</td>
          <td>1.3.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/object.pick.git">https://github.com/jonschlinkert/object.pick.git</a></td>
          <td><a href="https://github.com/jonschlinkert/object.pick">https://github.com/jonschlinkert/object.pick</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>object.values</td>
          <td>1.1.3</td>
          <td>MIT</td>
          <td>git://github.com/es-shims/Object.values.git</td>
          <td>Unknown</td>
          <td>Jordan Harband</td>
          </tr>
          <tr>
          <td>obuf</td>
          <td>1.1.2</td>
          <td>MIT</td>
          <td>git@github.com:indutny/offset-buffer</td>
          <td><a href="https://github.com/indutny/offset-buffer">https://github.com/indutny/offset-buffer</a></td>
          <td>Fedor Indutny</td>
          </tr>
          <tr>
          <td>on-finished</td>
          <td>2.3.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/jshttp/on-finished.git">https://github.com/jshttp/on-finished.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>on-headers</td>
          <td>1.0.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/jshttp/on-headers.git">https://github.com/jshttp/on-headers.git</a></td>
          <td>Unknown</td>
          <td>Douglas Christopher Wilson</td>
          </tr>
          <tr>
          <td>onetime</td>
          <td>2.0.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/onetime.git">https://github.com/sindresorhus/onetime.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>onetime</td>
          <td>5.1.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/onetime.git">https://github.com/sindresorhus/onetime.git</a></td>
          <td><a href="https://sindresorhus.com">https://sindresorhus.com</a></td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>open</td>
          <td>6.4.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/open.git">https://github.com/sindresorhus/open.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>opn</td>
          <td>5.5.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/opn.git">https://github.com/sindresorhus/opn.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>optimism</td>
          <td>0.10.3</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/benjamn/optimism.git">https://github.com/benjamn/optimism.git</a></td>
          <td><a href="https://github.com/benjamn/optimism#readme">https://github.com/benjamn/optimism#readme</a></td>
          <td>Ben Newman</td>
          </tr>
          <tr>
          <td>optionator</td>
          <td>0.8.3</td>
          <td>MIT</td>
          <td>git://github.com/gkz/optionator.git</td>
          <td><a href="https://github.com/gkz/optionator">https://github.com/gkz/optionator</a></td>
          <td>George Zahariev</td>
          </tr>
          <tr>
          <td>ora</td>
          <td>3.4.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/ora.git">https://github.com/sindresorhus/ora.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>ora</td>
          <td>5.3.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/ora.git">https://github.com/sindresorhus/ora.git</a></td>
          <td><a href="https://sindresorhus.com">https://sindresorhus.com</a></td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>original</td>
          <td>1.0.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/unshiftio/original">https://github.com/unshiftio/original</a></td>
          <td>Unknown</td>
          <td>Arnout Kazemier</td>
          </tr>
          <tr>
          <td>os-browserify</td>
          <td>0.3.0</td>
          <td>MIT</td>
          <td><a href="http://github.com/CoderPuppy/os-browserify.git">http://github.com/CoderPuppy/os-browserify.git</a></td>
          <td>Unknown</td>
          <td>CoderPuppy</td>
          </tr>
          <tr>
          <td>os-tmpdir</td>
          <td>1.0.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/os-tmpdir.git">https://github.com/sindresorhus/os-tmpdir.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>p-cancelable</td>
          <td>1.1.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/p-cancelable.git">https://github.com/sindresorhus/p-cancelable.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>p-defer</td>
          <td>1.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/p-defer.git">https://github.com/sindresorhus/p-defer.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>p-event</td>
          <td>4.2.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/p-event.git">https://github.com/sindresorhus/p-event.git</a></td>
          <td><a href="https://sindresorhus.com">https://sindresorhus.com</a></td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>p-finally</td>
          <td>1.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/p-finally.git">https://github.com/sindresorhus/p-finally.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>p-finally</td>
          <td>2.0.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/p-finally.git">https://github.com/sindresorhus/p-finally.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>p-limit</td>
          <td>2.3.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/p-limit.git">https://github.com/sindresorhus/p-limit.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>p-limit</td>
          <td>1.3.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/p-limit.git">https://github.com/sindresorhus/p-limit.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>p-locate</td>
          <td>4.1.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/p-locate.git">https://github.com/sindresorhus/p-locate.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>p-locate</td>
          <td>3.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/p-locate.git">https://github.com/sindresorhus/p-locate.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>p-locate</td>
          <td>2.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/p-locate.git">https://github.com/sindresorhus/p-locate.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>p-map</td>
          <td>3.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/p-map.git">https://github.com/sindresorhus/p-map.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>p-map</td>
          <td>2.1.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/p-map.git">https://github.com/sindresorhus/p-map.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>p-map</td>
          <td>4.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/p-map.git">https://github.com/sindresorhus/p-map.git</a></td>
          <td><a href="https://sindresorhus.com">https://sindresorhus.com</a></td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>p-retry</td>
          <td>3.0.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/p-retry.git">https://github.com/sindresorhus/p-retry.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>p-timeout</td>
          <td>3.2.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/p-timeout.git">https://github.com/sindresorhus/p-timeout.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>p-try</td>
          <td>2.2.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/p-try.git">https://github.com/sindresorhus/p-try.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>p-try</td>
          <td>1.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/p-try.git">https://github.com/sindresorhus/p-try.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>package-json</td>
          <td>6.5.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/package-json.git">https://github.com/sindresorhus/package-json.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>parallel-transform</td>
          <td>1.2.0</td>
          <td>MIT</td>
          <td>git://github.com/mafintosh/parallel-transform</td>
          <td>Unknown</td>
          <td>Mathias Buus Madsen</td>
          </tr>
          <tr>
          <td>param-case</td>
          <td>2.1.1</td>
          <td>MIT</td>
          <td>git://github.com/blakeembrey/param-case.git</td>
          <td><a href="https://github.com/blakeembrey/param-case">https://github.com/blakeembrey/param-case</a></td>
          <td>Blake Embrey</td>
          </tr>
          <tr>
          <td>parent-module</td>
          <td>1.0.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/parent-module.git">https://github.com/sindresorhus/parent-module.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>parse-json</td>
          <td>5.2.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/parse-json.git">https://github.com/sindresorhus/parse-json.git</a></td>
          <td><a href="https://sindresorhus.com">https://sindresorhus.com</a></td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>parse-json</td>
          <td>4.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/parse-json.git">https://github.com/sindresorhus/parse-json.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>parse-json</td>
          <td>2.2.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/parse-json.git">https://github.com/sindresorhus/parse-json.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>parse-ms</td>
          <td>2.1.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/parse-ms.git">https://github.com/sindresorhus/parse-ms.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>parse5</td>
          <td>5.1.1</td>
          <td>MIT</td>
          <td>git://github.com/inikulin/parse5.git</td>
          <td><a href="https://github.com/inikulin/parse5">https://github.com/inikulin/parse5</a></td>
          <td>Ivan Nikulin</td>
          </tr>
          <tr>
          <td>parse5</td>
          <td>6.0.1</td>
          <td>MIT</td>
          <td>git://github.com/inikulin/parse5.git</td>
          <td><a href="https://github.com/inikulin/parse5">https://github.com/inikulin/parse5</a></td>
          <td>Ivan Nikulin</td>
          </tr>
          <tr>
          <td>parse5-htmlparser2-tree-adapter</td>
          <td>6.0.1</td>
          <td>MIT</td>
          <td>git://github.com/inikulin/parse5.git</td>
          <td><a href="https://github.com/inikulin/parse5">https://github.com/inikulin/parse5</a></td>
          <td>Ivan Nikulin</td>
          </tr>
          <tr>
          <td>parseurl</td>
          <td>1.3.3</td>
          <td>MIT</td>
          <td><a href="https://github.com/pillarjs/parseurl.git">https://github.com/pillarjs/parseurl.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>pascalcase</td>
          <td>0.1.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/pascalcase.git">https://github.com/jonschlinkert/pascalcase.git</a></td>
          <td><a href="https://github.com/jonschlinkert/pascalcase">https://github.com/jonschlinkert/pascalcase</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>path-browserify</td>
          <td>0.0.1</td>
          <td>MIT</td>
          <td>git://github.com/substack/path-browserify.git</td>
          <td><a href="https://github.com/substack/path-browserify">https://github.com/substack/path-browserify</a></td>
          <td>James Halliday</td>
          </tr>
          <tr>
          <td>path-dirname</td>
          <td>1.0.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/es128/path-dirname.git">https://github.com/es128/path-dirname.git</a></td>
          <td>Unknown</td>
          <td>Elan Shanker</td>
          </tr>
          <tr>
          <td>path-exists</td>
          <td>4.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/path-exists.git">https://github.com/sindresorhus/path-exists.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>path-exists</td>
          <td>3.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/path-exists.git">https://github.com/sindresorhus/path-exists.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>path-exists</td>
          <td>2.1.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/path-exists.git">https://github.com/sindresorhus/path-exists.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>path-is-absolute</td>
          <td>1.0.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/path-is-absolute.git">https://github.com/sindresorhus/path-is-absolute.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>path-key</td>
          <td>2.0.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/path-key.git">https://github.com/sindresorhus/path-key.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>path-key</td>
          <td>3.1.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/path-key.git">https://github.com/sindresorhus/path-key.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>path-parse</td>
          <td>1.0.6</td>
          <td>MIT</td>
          <td><a href="https://github.com/jbgutierrez/path-parse.git">https://github.com/jbgutierrez/path-parse.git</a></td>
          <td><a href="https://github.com/jbgutierrez/path-parse#readme">https://github.com/jbgutierrez/path-parse#readme</a></td>
          <td>Javier Blanco</td>
          </tr>
          <tr>
          <td>path-to-regexp</td>
          <td>0.1.7</td>
          <td>MIT</td>
          <td><a href="https://github.com/component/path-to-regexp.git">https://github.com/component/path-to-regexp.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>path-type</td>
          <td>3.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/path-type.git">https://github.com/sindresorhus/path-type.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>path-type</td>
          <td>2.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/path-type.git">https://github.com/sindresorhus/path-type.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>path-type</td>
          <td>4.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/path-type.git">https://github.com/sindresorhus/path-type.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>pbkdf2</td>
          <td>3.1.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/crypto-browserify/pbkdf2.git">https://github.com/crypto-browserify/pbkdf2.git</a></td>
          <td><a href="https://github.com/crypto-browserify/pbkdf2">https://github.com/crypto-browserify/pbkdf2</a></td>
          <td>Daniel Cousens</td>
          </tr>
          <tr>
          <td>pend</td>
          <td>1.2.0</td>
          <td>MIT</td>
          <td>git://github.com/andrewrk/node-pend.git</td>
          <td>Unknown</td>
          <td>Andrew Kelley</td>
          </tr>
          <tr>
          <td>performance-now</td>
          <td>2.1.0</td>
          <td>MIT</td>
          <td>git://github.com/braveg1rl/performance-now.git</td>
          <td><a href="https://github.com/braveg1rl/performance-now">https://github.com/braveg1rl/performance-now</a></td>
          <td>Braveg1rl</td>
          </tr>
          <tr>
          <td>picomatch</td>
          <td>2.2.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/micromatch/picomatch.git">https://github.com/micromatch/picomatch.git</a></td>
          <td><a href="https://github.com/micromatch/picomatch">https://github.com/micromatch/picomatch</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>pify</td>
          <td>4.0.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/pify.git">https://github.com/sindresorhus/pify.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>pify</td>
          <td>3.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/pify.git">https://github.com/sindresorhus/pify.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>pify</td>
          <td>2.3.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/pify.git">https://github.com/sindresorhus/pify.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>pinkie</td>
          <td>2.0.4</td>
          <td>MIT</td>
          <td><a href="https://github.com/floatdrop/pinkie.git">https://github.com/floatdrop/pinkie.git</a></td>
          <td>github.com/floatdrop</td>
          <td>Vsevolod Strukchinsky</td>
          </tr>
          <tr>
          <td>pinkie-promise</td>
          <td>2.0.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/floatdrop/pinkie-promise.git">https://github.com/floatdrop/pinkie-promise.git</a></td>
          <td>github.com/floatdrop</td>
          <td>Vsevolod Strukchinsky</td>
          </tr>
          <tr>
          <td>pkg-conf</td>
          <td>3.1.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/pkg-conf.git">https://github.com/sindresorhus/pkg-conf.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>pkg-dir</td>
          <td>4.2.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/pkg-dir.git">https://github.com/sindresorhus/pkg-dir.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>pkg-dir</td>
          <td>3.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/pkg-dir.git">https://github.com/sindresorhus/pkg-dir.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>pkg-dir</td>
          <td>1.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/pkg-dir.git">https://github.com/sindresorhus/pkg-dir.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>pkg-dir</td>
          <td>2.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/pkg-dir.git">https://github.com/sindresorhus/pkg-dir.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>plur</td>
          <td>4.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/plur.git">https://github.com/sindresorhus/plur.git</a></td>
          <td><a href="https://sindresorhus.com">https://sindresorhus.com</a></td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>pnp-webpack-plugin</td>
          <td>1.6.4</td>
          <td>MIT</td>
          <td><a href="https://github.com/arcanis/pnp-webpack-plugin.git">https://github.com/arcanis/pnp-webpack-plugin.git</a></td>
          <td><a href="https://github.com/arcanis/pnp-webpack-plugin">https://github.com/arcanis/pnp-webpack-plugin</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>portfinder</td>
          <td>1.0.28</td>
          <td>MIT</td>
          <td>git@github.com:http-party/node-portfinder.git</td>
          <td>Unknown</td>
          <td>Charlie Robbins</td>
          </tr>
          <tr>
          <td>posix-character-classes</td>
          <td>0.1.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/posix-character-classes.git">https://github.com/jonschlinkert/posix-character-classes.git</a></td>
          <td><a href="https://github.com/jonschlinkert/posix-character-classes">https://github.com/jonschlinkert/posix-character-classes</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>postcss</td>
          <td>7.0.36</td>
          <td>MIT</td>
          <td><a href="https://github.com/postcss/postcss.git">https://github.com/postcss/postcss.git</a></td>
          <td><a href="https://postcss.org/">https://postcss.org/</a></td>
          <td>Andrey Sitnik</td>
          </tr>
          <tr>
          <td>postcss</td>
          <td>7.0.35</td>
          <td>MIT</td>
          <td><a href="https://github.com/postcss/postcss.git">https://github.com/postcss/postcss.git</a></td>
          <td><a href="https://postcss.org/">https://postcss.org/</a></td>
          <td>Andrey Sitnik</td>
          </tr>
          <tr>
          <td>postcss</td>
          <td>5.2.18</td>
          <td>MIT</td>
          <td><a href="https://github.com/postcss/postcss.git">https://github.com/postcss/postcss.git</a></td>
          <td><a href="http://postcss.org/">http://postcss.org/</a></td>
          <td>Andrey Sitnik</td>
          </tr>
          <tr>
          <td>postcss</td>
          <td>6.0.23</td>
          <td>MIT</td>
          <td><a href="https://github.com/postcss/postcss.git">https://github.com/postcss/postcss.git</a></td>
          <td><a href="https://postcss.org/">https://postcss.org/</a></td>
          <td>Andrey Sitnik</td>
          </tr>
          <tr>
          <td>postcss-calc</td>
          <td>7.0.5</td>
          <td>MIT</td>
          <td><a href="https://github.com/postcss/postcss-calc.git">https://github.com/postcss/postcss-calc.git</a></td>
          <td>Unknown</td>
          <td>Andy Jansson</td>
          </tr>
          <tr>
          <td>postcss-colormin</td>
          <td>4.0.3</td>
          <td>MIT</td>
          <td><a href="https://github.com/cssnano/cssnano.git">https://github.com/cssnano/cssnano.git</a></td>
          <td><a href="https://github.com/cssnano/cssnano">https://github.com/cssnano/cssnano</a></td>
          <td>Ben Briggs</td>
          </tr>
          <tr>
          <td>postcss-convert-values</td>
          <td>4.0.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/cssnano/cssnano.git">https://github.com/cssnano/cssnano.git</a></td>
          <td><a href="https://github.com/cssnano/cssnano">https://github.com/cssnano/cssnano</a></td>
          <td>Ben Briggs</td>
          </tr>
          <tr>
          <td>postcss-discard-comments</td>
          <td>4.0.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/cssnano/cssnano.git">https://github.com/cssnano/cssnano.git</a></td>
          <td><a href="https://github.com/cssnano/cssnano">https://github.com/cssnano/cssnano</a></td>
          <td>Ben Briggs</td>
          </tr>
          <tr>
          <td>postcss-discard-duplicates</td>
          <td>4.0.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/cssnano/cssnano.git">https://github.com/cssnano/cssnano.git</a></td>
          <td><a href="https://github.com/cssnano/cssnano">https://github.com/cssnano/cssnano</a></td>
          <td>Ben Briggs</td>
          </tr>
          <tr>
          <td>postcss-discard-empty</td>
          <td>4.0.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/cssnano/cssnano.git">https://github.com/cssnano/cssnano.git</a></td>
          <td><a href="https://github.com/cssnano/cssnano">https://github.com/cssnano/cssnano</a></td>
          <td>Ben Briggs</td>
          </tr>
          <tr>
          <td>postcss-discard-overridden</td>
          <td>4.0.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/cssnano/cssnano.git">https://github.com/cssnano/cssnano.git</a></td>
          <td><a href="https://github.com/cssnano/cssnano">https://github.com/cssnano/cssnano</a></td>
          <td>Justineo</td>
          </tr>
          <tr>
          <td>postcss-load-config</td>
          <td>2.1.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/postcss/postcss-load-config.git">https://github.com/postcss/postcss-load-config.git</a></td>
          <td>Unknown</td>
          <td>Michael Ciniawky</td>
          </tr>
          <tr>
          <td>postcss-loader</td>
          <td>3.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/postcss/postcss-loader.git">https://github.com/postcss/postcss-loader.git</a></td>
          <td><a href="https://github.com/postcss/postcss-loader#readme">https://github.com/postcss/postcss-loader#readme</a></td>
          <td>Andrey Sitnik</td>
          </tr>
          <tr>
          <td>postcss-merge-longhand</td>
          <td>4.0.11</td>
          <td>MIT</td>
          <td><a href="https://github.com/cssnano/cssnano.git">https://github.com/cssnano/cssnano.git</a></td>
          <td><a href="https://github.com/cssnano/cssnano">https://github.com/cssnano/cssnano</a></td>
          <td>Ben Briggs</td>
          </tr>
          <tr>
          <td>postcss-merge-rules</td>
          <td>4.0.3</td>
          <td>MIT</td>
          <td><a href="https://github.com/cssnano/cssnano.git">https://github.com/cssnano/cssnano.git</a></td>
          <td><a href="https://github.com/cssnano/cssnano">https://github.com/cssnano/cssnano</a></td>
          <td>Ben Briggs</td>
          </tr>
          <tr>
          <td>postcss-minify-font-values</td>
          <td>4.0.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/cssnano/cssnano.git">https://github.com/cssnano/cssnano.git</a></td>
          <td><a href="https://github.com/cssnano/cssnano">https://github.com/cssnano/cssnano</a></td>
          <td>Bogdan Chadkin</td>
          </tr>
          <tr>
          <td>postcss-minify-gradients</td>
          <td>4.0.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/cssnano/cssnano.git">https://github.com/cssnano/cssnano.git</a></td>
          <td><a href="https://github.com/cssnano/cssnano">https://github.com/cssnano/cssnano</a></td>
          <td>Ben Briggs</td>
          </tr>
          <tr>
          <td>postcss-minify-params</td>
          <td>4.0.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/cssnano/cssnano.git">https://github.com/cssnano/cssnano.git</a></td>
          <td><a href="https://github.com/cssnano/cssnano">https://github.com/cssnano/cssnano</a></td>
          <td>Bogdan Chadkin</td>
          </tr>
          <tr>
          <td>postcss-minify-selectors</td>
          <td>4.0.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/cssnano/cssnano.git">https://github.com/cssnano/cssnano.git</a></td>
          <td><a href="https://github.com/cssnano/cssnano">https://github.com/cssnano/cssnano</a></td>
          <td>Ben Briggs</td>
          </tr>
          <tr>
          <td>postcss-modules-local-by-default</td>
          <td>3.0.3</td>
          <td>MIT</td>
          <td><a href="https://github.com/css-modules/postcss-modules-local-by-default.git">https://github.com/css-modules/postcss-modules-local-by-default.git</a></td>
          <td>Unknown</td>
          <td>Mark Dalgleish</td>
          </tr>
          <tr>
          <td>postcss-modules-local-by-default</td>
          <td>1.2.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/css-modules/postcss-modules-local-by-default.git">https://github.com/css-modules/postcss-modules-local-by-default.git</a></td>
          <td>Unknown</td>
          <td>Mark Dalgleish</td>
          </tr>
          <tr>
          <td>postcss-modules-sync</td>
          <td>1.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/schiehll/postcss-modules-sync.git">https://github.com/schiehll/postcss-modules-sync.git</a></td>
          <td><a href="http://github.com/schiehll">http://github.com/schiehll</a></td>
          <td>schiehll</td>
          </tr>
          <tr>
          <td>postcss-normalize-charset</td>
          <td>4.0.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/cssnano/cssnano.git">https://github.com/cssnano/cssnano.git</a></td>
          <td><a href="https://github.com/cssnano/cssnano">https://github.com/cssnano/cssnano</a></td>
          <td>Bogdan Chadkin</td>
          </tr>
          <tr>
          <td>postcss-normalize-display-values</td>
          <td>4.0.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/cssnano/cssnano.git">https://github.com/cssnano/cssnano.git</a></td>
          <td><a href="https://github.com/cssnano/cssnano">https://github.com/cssnano/cssnano</a></td>
          <td>Ben Briggs</td>
          </tr>
          <tr>
          <td>postcss-normalize-positions</td>
          <td>4.0.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/cssnano/cssnano.git">https://github.com/cssnano/cssnano.git</a></td>
          <td><a href="https://github.com/cssnano/cssnano">https://github.com/cssnano/cssnano</a></td>
          <td>Ben Briggs</td>
          </tr>
          <tr>
          <td>postcss-normalize-repeat-style</td>
          <td>4.0.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/cssnano/cssnano.git">https://github.com/cssnano/cssnano.git</a></td>
          <td><a href="https://github.com/cssnano/cssnano">https://github.com/cssnano/cssnano</a></td>
          <td>Ben Briggs</td>
          </tr>
          <tr>
          <td>postcss-normalize-string</td>
          <td>4.0.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/cssnano/cssnano.git">https://github.com/cssnano/cssnano.git</a></td>
          <td><a href="https://github.com/cssnano/cssnano">https://github.com/cssnano/cssnano</a></td>
          <td>Ben Briggs</td>
          </tr>
          <tr>
          <td>postcss-normalize-timing-functions</td>
          <td>4.0.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/cssnano/cssnano.git">https://github.com/cssnano/cssnano.git</a></td>
          <td><a href="https://github.com/cssnano/cssnano">https://github.com/cssnano/cssnano</a></td>
          <td>Ben Briggs</td>
          </tr>
          <tr>
          <td>postcss-normalize-unicode</td>
          <td>4.0.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/cssnano/cssnano.git">https://github.com/cssnano/cssnano.git</a></td>
          <td><a href="https://github.com/cssnano/cssnano">https://github.com/cssnano/cssnano</a></td>
          <td>Ben Briggs</td>
          </tr>
          <tr>
          <td>postcss-normalize-url</td>
          <td>4.0.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/cssnano/cssnano.git">https://github.com/cssnano/cssnano.git</a></td>
          <td><a href="https://github.com/cssnano/cssnano">https://github.com/cssnano/cssnano</a></td>
          <td>Ben Briggs</td>
          </tr>
          <tr>
          <td>postcss-normalize-whitespace</td>
          <td>4.0.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/cssnano/cssnano.git">https://github.com/cssnano/cssnano.git</a></td>
          <td><a href="https://github.com/cssnano/cssnano">https://github.com/cssnano/cssnano</a></td>
          <td>Ben Briggs</td>
          </tr>
          <tr>
          <td>postcss-ordered-values</td>
          <td>4.1.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/cssnano/cssnano.git">https://github.com/cssnano/cssnano.git</a></td>
          <td><a href="https://github.com/cssnano/cssnano">https://github.com/cssnano/cssnano</a></td>
          <td>Ben Briggs</td>
          </tr>
          <tr>
          <td>postcss-reduce-initial</td>
          <td>4.0.3</td>
          <td>MIT</td>
          <td><a href="https://github.com/cssnano/cssnano.git">https://github.com/cssnano/cssnano.git</a></td>
          <td><a href="https://github.com/cssnano/cssnano">https://github.com/cssnano/cssnano</a></td>
          <td>Ben Briggs</td>
          </tr>
          <tr>
          <td>postcss-reduce-transforms</td>
          <td>4.0.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/cssnano/cssnano.git">https://github.com/cssnano/cssnano.git</a></td>
          <td><a href="https://github.com/cssnano/cssnano">https://github.com/cssnano/cssnano</a></td>
          <td>Ben Briggs</td>
          </tr>
          <tr>
          <td>postcss-selector-parser</td>
          <td>6.0.4</td>
          <td>MIT</td>
          <td><a href="https://github.com/postcss/postcss-selector-parser.git">https://github.com/postcss/postcss-selector-parser.git</a></td>
          <td><a href="https://github.com/postcss/postcss-selector-parser">https://github.com/postcss/postcss-selector-parser</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>postcss-selector-parser</td>
          <td>3.1.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/postcss/postcss-selector-parser.git">https://github.com/postcss/postcss-selector-parser.git</a></td>
          <td><a href="https://github.com/postcss/postcss-selector-parser">https://github.com/postcss/postcss-selector-parser</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>postcss-selector-parser</td>
          <td>5.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/postcss/postcss-selector-parser.git">https://github.com/postcss/postcss-selector-parser.git</a></td>
          <td><a href="https://github.com/postcss/postcss-selector-parser">https://github.com/postcss/postcss-selector-parser</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>postcss-svgo</td>
          <td>4.0.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/cssnano/cssnano.git">https://github.com/cssnano/cssnano.git</a></td>
          <td><a href="https://github.com/cssnano/cssnano">https://github.com/cssnano/cssnano</a></td>
          <td>Ben Briggs</td>
          </tr>
          <tr>
          <td>postcss-unique-selectors</td>
          <td>4.0.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/cssnano/cssnano.git">https://github.com/cssnano/cssnano.git</a></td>
          <td><a href="https://github.com/cssnano/cssnano">https://github.com/cssnano/cssnano</a></td>
          <td>Ben Briggs</td>
          </tr>
          <tr>
          <td>postcss-value-parser</td>
          <td>4.1.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/TrySound/postcss-value-parser.git">https://github.com/TrySound/postcss-value-parser.git</a></td>
          <td><a href="https://github.com/TrySound/postcss-value-parser">https://github.com/TrySound/postcss-value-parser</a></td>
          <td>Bogdan Chadkin</td>
          </tr>
          <tr>
          <td>postcss-value-parser</td>
          <td>3.3.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/TrySound/postcss-value-parser.git">https://github.com/TrySound/postcss-value-parser.git</a></td>
          <td><a href="https://github.com/TrySound/postcss-value-parser">https://github.com/TrySound/postcss-value-parser</a></td>
          <td>Bogdan Chadkin</td>
          </tr>
          <tr>
          <td>prelude-ls</td>
          <td>1.1.2</td>
          <td>MIT</td>
          <td>git://github.com/gkz/prelude-ls.git</td>
          <td><a href="http://preludels.com/">http://preludels.com/</a></td>
          <td>George Zahariev</td>
          </tr>
          <tr>
          <td>prepend-http</td>
          <td>1.0.4</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/prepend-http.git">https://github.com/sindresorhus/prepend-http.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>prepend-http</td>
          <td>2.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/prepend-http.git">https://github.com/sindresorhus/prepend-http.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>prerender-spa-plugin</td>
          <td>3.4.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/chrisvfritz/prerender-spa-plugin.git">https://github.com/chrisvfritz/prerender-spa-plugin.git</a></td>
          <td><a href="https://twitter.com/chrisvfritz">https://twitter.com/chrisvfritz</a></td>
          <td>Chris Fritz</td>
          </tr>
          <tr>
          <td>prettier</td>
          <td>1.19.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/prettier/prettier.git">https://github.com/prettier/prettier.git</a></td>
          <td><a href="https://prettier.io/">https://prettier.io/</a></td>
          <td>James Long</td>
          </tr>
          <tr>
          <td>prettier</td>
          <td>1.16.3</td>
          <td>MIT</td>
          <td><a href="https://github.com/prettier/prettier.git">https://github.com/prettier/prettier.git</a></td>
          <td><a href="https://prettier.io/">https://prettier.io/</a></td>
          <td>James Long</td>
          </tr>
          <tr>
          <td>pretty</td>
          <td>2.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/pretty.git">https://github.com/jonschlinkert/pretty.git</a></td>
          <td><a href="https://github.com/jonschlinkert/pretty">https://github.com/jonschlinkert/pretty</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>pretty-error</td>
          <td>2.1.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/AriaMinaei/pretty-error.git">https://github.com/AriaMinaei/pretty-error.git</a></td>
          <td>Unknown</td>
          <td>Aria Minaei</td>
          </tr>
          <tr>
          <td>pretty-ms</td>
          <td>7.0.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/pretty-ms.git">https://github.com/sindresorhus/pretty-ms.git</a></td>
          <td><a href="https://sindresorhus.com">https://sindresorhus.com</a></td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>process</td>
          <td>0.11.10</td>
          <td>MIT</td>
          <td>git://github.com/shtylman/node-process.git</td>
          <td>Unknown</td>
          <td>Roman Shtylman</td>
          </tr>
          <tr>
          <td>process-nextick-args</td>
          <td>2.0.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/calvinmetcalf/process-nextick-args.git">https://github.com/calvinmetcalf/process-nextick-args.git</a></td>
          <td><a href="https://github.com/calvinmetcalf/process-nextick-args">https://github.com/calvinmetcalf/process-nextick-args</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>progress</td>
          <td>2.0.3</td>
          <td>MIT</td>
          <td>git://github.com/visionmedia/node-progress</td>
          <td>Unknown</td>
          <td>TJ Holowaychuk</td>
          </tr>
          <tr>
          <td>proxy-addr</td>
          <td>2.0.6</td>
          <td>MIT</td>
          <td><a href="https://github.com/jshttp/proxy-addr.git">https://github.com/jshttp/proxy-addr.git</a></td>
          <td>Unknown</td>
          <td>Douglas Christopher Wilson</td>
          </tr>
          <tr>
          <td>proxy-from-env</td>
          <td>1.1.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/Rob--W/proxy-from-env.git">https://github.com/Rob--W/proxy-from-env.git</a></td>
          <td><a href="https://github.com/Rob--W/proxy-from-env#readme">https://github.com/Rob--W/proxy-from-env#readme</a></td>
          <td>Rob Wu</td>
          </tr>
          <tr>
          <td>prr</td>
          <td>1.0.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/rvagg/prr.git">https://github.com/rvagg/prr.git</a></td>
          <td><a href="https://github.com/rvagg/prr">https://github.com/rvagg/prr</a></td>
          <td>Rod Vagg</td>
          </tr>
          <tr>
          <td>psl</td>
          <td>1.8.0</td>
          <td>MIT</td>
          <td>git@github.com:lupomontero/psl.git</td>
          <td><a href="https://lupomontero.com/">https://lupomontero.com/</a></td>
          <td>Lupo Montero</td>
          </tr>
          <tr>
          <td>public-encrypt</td>
          <td>4.0.3</td>
          <td>MIT</td>
          <td><a href="https://github.com/crypto-browserify/publicEncrypt.git">https://github.com/crypto-browserify/publicEncrypt.git</a></td>
          <td><a href="https://github.com/crypto-browserify/publicEncrypt">https://github.com/crypto-browserify/publicEncrypt</a></td>
          <td>Calvin Metcalf</td>
          </tr>
          <tr>
          <td>pump</td>
          <td>3.0.0</td>
          <td>MIT</td>
          <td>git://github.com/mafintosh/pump.git</td>
          <td>Unknown</td>
          <td>Mathias Buus Madsen</td>
          </tr>
          <tr>
          <td>pump</td>
          <td>2.0.1</td>
          <td>MIT</td>
          <td>git://github.com/mafintosh/pump.git</td>
          <td>Unknown</td>
          <td>Mathias Buus Madsen</td>
          </tr>
          <tr>
          <td>pumpify</td>
          <td>1.5.1</td>
          <td>MIT</td>
          <td>git://github.com/mafintosh/pumpify</td>
          <td><a href="https://github.com/mafintosh/pumpify">https://github.com/mafintosh/pumpify</a></td>
          <td>Mathias Buus</td>
          </tr>
          <tr>
          <td>punycode</td>
          <td>1.4.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/bestiejs/punycode.js.git">https://github.com/bestiejs/punycode.js.git</a></td>
          <td><a href="https://mths.be/punycode">https://mths.be/punycode</a></td>
          <td>Mathias Bynens</td>
          </tr>
          <tr>
          <td>punycode</td>
          <td>2.1.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/bestiejs/punycode.js.git">https://github.com/bestiejs/punycode.js.git</a></td>
          <td><a href="https://mths.be/punycode">https://mths.be/punycode</a></td>
          <td>Mathias Bynens</td>
          </tr>
          <tr>
          <td>punycode</td>
          <td>1.3.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/bestiejs/punycode.js.git">https://github.com/bestiejs/punycode.js.git</a></td>
          <td><a href="https://mths.be/punycode">https://mths.be/punycode</a></td>
          <td>Mathias Bynens</td>
          </tr>
          <tr>
          <td>pupa</td>
          <td>2.1.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/pupa.git">https://github.com/sindresorhus/pupa.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>q</td>
          <td>1.5.1</td>
          <td>MIT</td>
          <td>git://github.com/kriskowal/q.git</td>
          <td><a href="https://github.com/kriskowal/q">https://github.com/kriskowal/q</a></td>
          <td>Kris Kowal</td>
          </tr>
          <tr>
          <td>query-string</td>
          <td>4.3.4</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/query-string.git">https://github.com/sindresorhus/query-string.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>querystring</td>
          <td>0.2.0</td>
          <td>MIT</td>
          <td>git://github.com/Gozala/querystring.git</td>
          <td>Unknown</td>
          <td>Irakli Gozalishvili</td>
          </tr>
          <tr>
          <td>querystring-es3</td>
          <td>0.2.1</td>
          <td>MIT</td>
          <td>git://github.com/mike-spainhower/querystring.git</td>
          <td>Unknown</td>
          <td>Irakli Gozalishvili</td>
          </tr>
          <tr>
          <td>querystringify</td>
          <td>2.2.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/unshiftio/querystringify">https://github.com/unshiftio/querystringify</a></td>
          <td><a href="https://github.com/unshiftio/querystringify">https://github.com/unshiftio/querystringify</a></td>
          <td>Arnout Kazemier</td>
          </tr>
          <tr>
          <td>queue-microtask</td>
          <td>1.2.2</td>
          <td>MIT</td>
          <td>git://github.com/feross/queue-microtask.git</td>
          <td><a href="https://github.com/feross/queue-microtask">https://github.com/feross/queue-microtask</a></td>
          <td>Feross Aboukhadijeh</td>
          </tr>
          <tr>
          <td>randombytes</td>
          <td>2.1.0</td>
          <td>MIT</td>
          <td>git@github.com:crypto-browserify/randombytes.git</td>
          <td><a href="https://github.com/crypto-browserify/randombytes">https://github.com/crypto-browserify/randombytes</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>randomfill</td>
          <td>1.0.4</td>
          <td>MIT</td>
          <td><a href="https://github.com/crypto-browserify/randomfill.git">https://github.com/crypto-browserify/randomfill.git</a></td>
          <td><a href="https://github.com/crypto-browserify/randomfill">https://github.com/crypto-browserify/randomfill</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>range-parser</td>
          <td>1.2.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/jshttp/range-parser.git">https://github.com/jshttp/range-parser.git</a></td>
          <td><a href="http://tjholowaychuk.com">http://tjholowaychuk.com</a></td>
          <td>TJ Holowaychuk</td>
          </tr>
          <tr>
          <td>raw-body</td>
          <td>2.4.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/stream-utils/raw-body.git">https://github.com/stream-utils/raw-body.git</a></td>
          <td><a href="http://jongleberry.com">http://jongleberry.com</a></td>
          <td>Jonathan Ong</td>
          </tr>
          <tr>
          <td>read-pkg</td>
          <td>5.2.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/read-pkg.git">https://github.com/sindresorhus/read-pkg.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>read-pkg</td>
          <td>2.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/read-pkg.git">https://github.com/sindresorhus/read-pkg.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>read-pkg-up</td>
          <td>2.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/read-pkg-up.git">https://github.com/sindresorhus/read-pkg-up.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>readable-stream</td>
          <td>2.3.7</td>
          <td>MIT</td>
          <td>git://github.com/nodejs/readable-stream</td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>readable-stream</td>
          <td>3.6.0</td>
          <td>MIT</td>
          <td>git://github.com/nodejs/readable-stream</td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>readdirp</td>
          <td>3.5.0</td>
          <td>MIT</td>
          <td>git://github.com/paulmillr/readdirp.git</td>
          <td><a href="https://github.com/paulmillr/readdirp">https://github.com/paulmillr/readdirp</a></td>
          <td>Thorsten Lorenz</td>
          </tr>
          <tr>
          <td>readdirp</td>
          <td>2.2.1</td>
          <td>MIT</td>
          <td>git://github.com/paulmillr/readdirp.git</td>
          <td><a href="https://github.com/paulmillr/readdirp">https://github.com/paulmillr/readdirp</a></td>
          <td>Thorsten Lorenz</td>
          </tr>
          <tr>
          <td>rechoir</td>
          <td>0.6.2</td>
          <td>MIT</td>
          <td>git://github.com/tkellen/node-rechoir.git</td>
          <td><a href="https://github.com/tkellen/node-rechoir">https://github.com/tkellen/node-rechoir</a></td>
          <td>Tyler Kellen</td>
          </tr>
          <tr>
          <td>regenerate</td>
          <td>1.4.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/mathiasbynens/regenerate.git">https://github.com/mathiasbynens/regenerate.git</a></td>
          <td><a href="https://mths.be/regenerate">https://mths.be/regenerate</a></td>
          <td>Mathias Bynens</td>
          </tr>
          <tr>
          <td>regenerate-unicode-properties</td>
          <td>8.2.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/mathiasbynens/regenerate-unicode-properties.git">https://github.com/mathiasbynens/regenerate-unicode-properties.git</a></td>
          <td><a href="https://github.com/mathiasbynens/regenerate-unicode-properties">https://github.com/mathiasbynens/regenerate-unicode-properties</a></td>
          <td>Mathias Bynens</td>
          </tr>
          <tr>
          <td>regenerator-runtime</td>
          <td>0.13.7</td>
          <td>MIT</td>
          <td><a href="https://github.com/facebook/regenerator/tree/master/packages/regenerator-runtime">https://github.com/facebook/regenerator/tree/master/packages/regenerator-runtime</a></td>
          <td>Unknown</td>
          <td>Ben Newman</td>
          </tr>
          <tr>
          <td>regenerator-transform</td>
          <td>0.14.5</td>
          <td>MIT</td>
          <td><a href="https://github.com/facebook/regenerator/tree/master/packages/regenerator-transform">https://github.com/facebook/regenerator/tree/master/packages/regenerator-transform</a></td>
          <td>Unknown</td>
          <td>Ben Newman</td>
          </tr>
          <tr>
          <td>regex-not</td>
          <td>1.0.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/regex-not.git">https://github.com/jonschlinkert/regex-not.git</a></td>
          <td><a href="https://github.com/jonschlinkert/regex-not">https://github.com/jonschlinkert/regex-not</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>regexp.prototype.flags</td>
          <td>1.3.1</td>
          <td>MIT</td>
          <td>git://github.com/es-shims/RegExp.prototype.flags.git</td>
          <td>Unknown</td>
          <td>Jordan Harband</td>
          </tr>
          <tr>
          <td>regexpp</td>
          <td>2.0.1</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/mysticatea/regexpp.git">https://github.com/mysticatea/regexpp.git</a></td>
          <td><a href="https://github.com/mysticatea/regexpp#readme">https://github.com/mysticatea/regexpp#readme</a></td>
          <td>Toru Nagashima</td>
          </tr>
          <tr>
          <td>regexpu-core</td>
          <td>4.7.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/mathiasbynens/regexpu-core.git">https://github.com/mathiasbynens/regexpu-core.git</a></td>
          <td><a href="https://mths.be/regexpu">https://mths.be/regexpu</a></td>
          <td>Mathias Bynens</td>
          </tr>
          <tr>
          <td>registry-auth-token</td>
          <td>4.2.1</td>
          <td>MIT</td>
          <td>git+ssh://git@github.com/rexxars/registry-auth-token.git</td>
          <td><a href="https://github.com/rexxars/registry-auth-token#readme">https://github.com/rexxars/registry-auth-token#readme</a></td>
          <td>Espen Hovlandsdal</td>
          </tr>
          <tr>
          <td>registry-url</td>
          <td>5.1.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/registry-url.git">https://github.com/sindresorhus/registry-url.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>regjsgen</td>
          <td>0.5.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/bnjmnt4n/regjsgen.git">https://github.com/bnjmnt4n/regjsgen.git</a></td>
          <td><a href="https://github.com/bnjmnt4n/regjsgen">https://github.com/bnjmnt4n/regjsgen</a></td>
          <td>Benjamin Tan</td>
          </tr>
          <tr>
          <td>relateurl</td>
          <td>0.2.7</td>
          <td>MIT</td>
          <td>git://github.com/stevenvachon/relateurl.git</td>
          <td><a href="https://github.com/stevenvachon/relateurl">https://github.com/stevenvachon/relateurl</a></td>
          <td>Steven Vachon</td>
          </tr>
          <tr>
          <td>renderkid</td>
          <td>2.0.5</td>
          <td>MIT</td>
          <td><a href="https://github.com/AriaMinaei/RenderKid.git">https://github.com/AriaMinaei/RenderKid.git</a></td>
          <td>Unknown</td>
          <td>Aria Minaei</td>
          </tr>
          <tr>
          <td>repeat-element</td>
          <td>1.1.3</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/repeat-element.git">https://github.com/jonschlinkert/repeat-element.git</a></td>
          <td><a href="https://github.com/jonschlinkert/repeat-element">https://github.com/jonschlinkert/repeat-element</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>repeat-string</td>
          <td>1.6.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/repeat-string.git">https://github.com/jonschlinkert/repeat-string.git</a></td>
          <td><a href="https://github.com/jonschlinkert/repeat-string">https://github.com/jonschlinkert/repeat-string</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>require-directory</td>
          <td>2.1.1</td>
          <td>MIT</td>
          <td>git://github.com/troygoode/node-require-directory.git</td>
          <td><a href="https://github.com/troygoode/node-require-directory/">https://github.com/troygoode/node-require-directory/</a></td>
          <td>Troy Goode</td>
          </tr>
          <tr>
          <td>requires-port</td>
          <td>1.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/unshiftio/requires-port">https://github.com/unshiftio/requires-port</a></td>
          <td><a href="https://github.com/unshiftio/requires-port">https://github.com/unshiftio/requires-port</a></td>
          <td>Arnout Kazemier</td>
          </tr>
          <tr>
          <td>resolve</td>
          <td>1.20.0</td>
          <td>MIT</td>
          <td>git://github.com/browserify/resolve.git</td>
          <td><a href="http://substack.net">http://substack.net</a></td>
          <td>James Halliday</td>
          </tr>
          <tr>
          <td>resolve-cwd</td>
          <td>2.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/resolve-cwd.git">https://github.com/sindresorhus/resolve-cwd.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>resolve-cwd</td>
          <td>3.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/resolve-cwd.git">https://github.com/sindresorhus/resolve-cwd.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>resolve-from</td>
          <td>3.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/resolve-from.git">https://github.com/sindresorhus/resolve-from.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>resolve-from</td>
          <td>5.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/resolve-from.git">https://github.com/sindresorhus/resolve-from.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>resolve-from</td>
          <td>4.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/resolve-from.git">https://github.com/sindresorhus/resolve-from.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>resolve-url</td>
          <td>0.2.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/lydell/resolve-url.git">https://github.com/lydell/resolve-url.git</a></td>
          <td>Unknown</td>
          <td>Simon Lydell</td>
          </tr>
          <tr>
          <td>responselike</td>
          <td>1.0.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/lukechilds/responselike.git">https://github.com/lukechilds/responselike.git</a></td>
          <td>Unknown</td>
          <td>lukechilds</td>
          </tr>
          <tr>
          <td>restore-cursor</td>
          <td>2.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/restore-cursor.git">https://github.com/sindresorhus/restore-cursor.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>restore-cursor</td>
          <td>3.1.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/restore-cursor.git">https://github.com/sindresorhus/restore-cursor.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>ret</td>
          <td>0.1.15</td>
          <td>MIT</td>
          <td>git://github.com/fent/ret.js.git</td>
          <td><a href="https://github.com/fent">https://github.com/fent</a></td>
          <td>Roly Fentanes</td>
          </tr>
          <tr>
          <td>retry</td>
          <td>0.12.0</td>
          <td>MIT</td>
          <td>git://github.com/tim-kos/node-retry.git</td>
          <td><a href="https://github.com/tim-kos/node-retry">https://github.com/tim-kos/node-retry</a></td>
          <td>Tim Koschützki</td>
          </tr>
          <tr>
          <td>reusify</td>
          <td>1.0.4</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/mcollina/reusify.git">https://github.com/mcollina/reusify.git</a></td>
          <td><a href="https://github.com/mcollina/reusify#readme">https://github.com/mcollina/reusify#readme</a></td>
          <td>Matteo Collina</td>
          </tr>
          <tr>
          <td>rgb-regex</td>
          <td>1.0.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/regexps/rgb-regex.git">https://github.com/regexps/rgb-regex.git</a></td>
          <td><a href="https://github.com/regexps/rgb-regex">https://github.com/regexps/rgb-regex</a></td>
          <td>John Otander</td>
          </tr>
          <tr>
          <td>rgba-regex</td>
          <td>1.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/johnotander/rgba-regex.git">https://github.com/johnotander/rgba-regex.git</a></td>
          <td><a href="https://github.com/johnotander/rgba-regex">https://github.com/johnotander/rgba-regex</a></td>
          <td>John Otander</td>
          </tr>
          <tr>
          <td>ripemd160</td>
          <td>2.0.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/crypto-browserify/ripemd160">https://github.com/crypto-browserify/ripemd160</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>run-async</td>
          <td>2.4.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/SBoudrias/run-async.git">https://github.com/SBoudrias/run-async.git</a></td>
          <td>Unknown</td>
          <td>Simon Boudrias</td>
          </tr>
          <tr>
          <td>run-parallel</td>
          <td>1.2.0</td>
          <td>MIT</td>
          <td>git://github.com/feross/run-parallel.git</td>
          <td><a href="https://github.com/feross/run-parallel">https://github.com/feross/run-parallel</a></td>
          <td>Feross Aboukhadijeh</td>
          </tr>
          <tr>
          <td>safe-buffer</td>
          <td>5.1.2</td>
          <td>MIT</td>
          <td>git://github.com/feross/safe-buffer.git</td>
          <td><a href="https://github.com/feross/safe-buffer">https://github.com/feross/safe-buffer</a></td>
          <td>Feross Aboukhadijeh</td>
          </tr>
          <tr>
          <td>safe-buffer</td>
          <td>5.2.1</td>
          <td>MIT</td>
          <td>git://github.com/feross/safe-buffer.git</td>
          <td><a href="https://github.com/feross/safe-buffer">https://github.com/feross/safe-buffer</a></td>
          <td>Feross Aboukhadijeh</td>
          </tr>
          <tr>
          <td>safe-regex</td>
          <td>1.1.0</td>
          <td>MIT</td>
          <td>git://github.com/substack/safe-regex.git</td>
          <td><a href="https://github.com/substack/safe-regex">https://github.com/substack/safe-regex</a></td>
          <td>James Halliday</td>
          </tr>
          <tr>
          <td>safer-buffer</td>
          <td>2.1.2</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/ChALkeR/safer-buffer.git">https://github.com/ChALkeR/safer-buffer.git</a></td>
          <td><a href="https://github.com/ChALkeR">https://github.com/ChALkeR</a></td>
          <td>Nikita Skovoroda</td>
          </tr>
          <tr>
          <td>sass</td>
          <td>1.32.8</td>
          <td>MIT</td>
          <td><a href="https://github.com/sass/dart-sass">https://github.com/sass/dart-sass</a></td>
          <td><a href="https://github.com/sass/dart-sass">https://github.com/sass/dart-sass</a></td>
          <td>Natalie Weizenbaum</td>
          </tr>
          <tr>
          <td>sass-loader</td>
          <td>8.0.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/webpack-contrib/sass-loader.git">https://github.com/webpack-contrib/sass-loader.git</a></td>
          <td><a href="https://github.com/webpack-contrib/sass-loader">https://github.com/webpack-contrib/sass-loader</a></td>
          <td>J. Tangelder</td>
          </tr>
          <tr>
          <td>schema-utils</td>
          <td>2.7.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/webpack/schema-utils.git">https://github.com/webpack/schema-utils.git</a></td>
          <td><a href="https://github.com/webpack/schema-utils">https://github.com/webpack/schema-utils</a></td>
          <td>webpack Contrib</td>
          </tr>
          <tr>
          <td>schema-utils</td>
          <td>1.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/webpack-contrib/schema-utils">https://github.com/webpack-contrib/schema-utils</a></td>
          <td><a href="https://github.com/webpack-contrib/schema-utils">https://github.com/webpack-contrib/schema-utils</a></td>
          <td>webpack Contrib</td>
          </tr>
          <tr>
          <td>schema-utils</td>
          <td>3.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/webpack/schema-utils.git">https://github.com/webpack/schema-utils.git</a></td>
          <td><a href="https://github.com/webpack/schema-utils">https://github.com/webpack/schema-utils</a></td>
          <td>webpack Contrib</td>
          </tr>
          <tr>
          <td>select-hose</td>
          <td>2.0.0</td>
          <td>MIT</td>
          <td>git+ssh://git@github.com/indutny/select-hose.git</td>
          <td><a href="https://github.com/indutny/select-hose#readme">https://github.com/indutny/select-hose#readme</a></td>
          <td>Fedor Indutny</td>
          </tr>
          <tr>
          <td>selfsigned</td>
          <td>1.10.8</td>
          <td>MIT</td>
          <td>git://github.com/jfromaniello/selfsigned.git</td>
          <td><a href="http://joseoncode.com">http://joseoncode.com</a></td>
          <td>José F. Romaniello</td>
          </tr>
          <tr>
          <td>semver-diff</td>
          <td>3.1.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/semver-diff.git">https://github.com/sindresorhus/semver-diff.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>send</td>
          <td>0.17.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/pillarjs/send.git">https://github.com/pillarjs/send.git</a></td>
          <td>Unknown</td>
          <td>TJ Holowaychuk</td>
          </tr>
          <tr>
          <td>serialize-error</td>
          <td>7.0.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/serialize-error.git">https://github.com/sindresorhus/serialize-error.git</a></td>
          <td><a href="https://sindresorhus.com">https://sindresorhus.com</a></td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>serve-index</td>
          <td>1.9.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/expressjs/serve-index.git">https://github.com/expressjs/serve-index.git</a></td>
          <td>Unknown</td>
          <td>Douglas Christopher Wilson</td>
          </tr>
          <tr>
          <td>serve-static</td>
          <td>1.14.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/expressjs/serve-static.git">https://github.com/expressjs/serve-static.git</a></td>
          <td>Unknown</td>
          <td>Douglas Christopher Wilson</td>
          </tr>
          <tr>
          <td>set-value</td>
          <td>2.0.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/set-value.git">https://github.com/jonschlinkert/set-value.git</a></td>
          <td><a href="https://github.com/jonschlinkert/set-value">https://github.com/jonschlinkert/set-value</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>setimmediate</td>
          <td>1.0.5</td>
          <td>MIT</td>
          <td><a href="https://github.com/YuzuJS/setImmediate.git">https://github.com/YuzuJS/setImmediate.git</a></td>
          <td>Unknown</td>
          <td>YuzuJS</td>
          </tr>
          <tr>
          <td>shallow-clone</td>
          <td>3.0.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/shallow-clone.git">https://github.com/jonschlinkert/shallow-clone.git</a></td>
          <td><a href="https://github.com/jonschlinkert/shallow-clone">https://github.com/jonschlinkert/shallow-clone</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>shebang-command</td>
          <td>1.2.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/kevva/shebang-command.git">https://github.com/kevva/shebang-command.git</a></td>
          <td>github.com/kevva</td>
          <td>Kevin Martensson</td>
          </tr>
          <tr>
          <td>shebang-command</td>
          <td>2.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/kevva/shebang-command.git">https://github.com/kevva/shebang-command.git</a></td>
          <td>github.com/kevva</td>
          <td>Kevin Mårtensson</td>
          </tr>
          <tr>
          <td>shebang-regex</td>
          <td>1.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/shebang-regex.git">https://github.com/sindresorhus/shebang-regex.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>shebang-regex</td>
          <td>3.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/shebang-regex.git">https://github.com/sindresorhus/shebang-regex.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>shell-quote</td>
          <td>1.7.2</td>
          <td>MIT</td>
          <td><a href="http://github.com/substack/node-shell-quote.git">http://github.com/substack/node-shell-quote.git</a></td>
          <td><a href="https://github.com/substack/node-shell-quote">https://github.com/substack/node-shell-quote</a></td>
          <td>James Halliday</td>
          </tr>
          <tr>
          <td>simple-swizzle</td>
          <td>0.2.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/qix-/node-simple-swizzle.git">https://github.com/qix-/node-simple-swizzle.git</a></td>
          <td><a href="http://github.com/qix-">http://github.com/qix-</a></td>
          <td>Qix</td>
          </tr>
          <tr>
          <td>sitemap</td>
          <td>1.13.0</td>
          <td>MIT</td>
          <td>git://github.com/ekalinin/sitemap.js.git</td>
          <td>Unknown</td>
          <td>Eugene Kalinin</td>
          </tr>
          <tr>
          <td>slash</td>
          <td>2.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/slash.git">https://github.com/sindresorhus/slash.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>slash</td>
          <td>1.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/slash.git">https://github.com/sindresorhus/slash.git</a></td>
          <td><a href="http://sindresorhus.com">http://sindresorhus.com</a></td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>slash</td>
          <td>3.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/slash.git">https://github.com/sindresorhus/slash.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>slice-ansi</td>
          <td>3.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/chalk/slice-ansi.git">https://github.com/chalk/slice-ansi.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>slice-ansi</td>
          <td>2.1.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/chalk/slice-ansi.git">https://github.com/chalk/slice-ansi.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>snapdragon</td>
          <td>0.8.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/snapdragon.git">https://github.com/jonschlinkert/snapdragon.git</a></td>
          <td><a href="https://github.com/jonschlinkert/snapdragon">https://github.com/jonschlinkert/snapdragon</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>snapdragon-node</td>
          <td>2.1.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/snapdragon-node.git">https://github.com/jonschlinkert/snapdragon-node.git</a></td>
          <td><a href="https://github.com/jonschlinkert/snapdragon-node">https://github.com/jonschlinkert/snapdragon-node</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>snapdragon-util</td>
          <td>3.0.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/snapdragon-util.git">https://github.com/jonschlinkert/snapdragon-util.git</a></td>
          <td><a href="https://github.com/jonschlinkert/snapdragon-util">https://github.com/jonschlinkert/snapdragon-util</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>sockjs</td>
          <td>0.3.21</td>
          <td>MIT</td>
          <td><a href="https://github.com/sockjs/sockjs-node.git">https://github.com/sockjs/sockjs-node.git</a></td>
          <td><a href="https://github.com/sockjs/sockjs-node">https://github.com/sockjs/sockjs-node</a></td>
          <td>Marek Majkowski</td>
          </tr>
          <tr>
          <td>sockjs-client</td>
          <td>1.5.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sockjs/sockjs-client.git">https://github.com/sockjs/sockjs-client.git</a></td>
          <td><a href="http://sockjs.org/">http://sockjs.org/</a></td>
          <td>Bryce Kahle</td>
          </tr>
          <tr>
          <td>sort-keys</td>
          <td>1.1.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/sort-keys.git">https://github.com/sindresorhus/sort-keys.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>source-list-map</td>
          <td>2.0.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/webpack/source-list-map.git">https://github.com/webpack/source-list-map.git</a></td>
          <td><a href="https://github.com/webpack/source-list-map">https://github.com/webpack/source-list-map</a></td>
          <td>Tobias Koppers @sokra</td>
          </tr>
          <tr>
          <td>source-map-resolve</td>
          <td>0.5.3</td>
          <td>MIT</td>
          <td><a href="https://github.com/lydell/source-map-resolve.git">https://github.com/lydell/source-map-resolve.git</a></td>
          <td>Unknown</td>
          <td>Simon Lydell</td>
          </tr>
          <tr>
          <td>source-map-support</td>
          <td>0.5.19</td>
          <td>MIT</td>
          <td><a href="https://github.com/evanw/node-source-map-support">https://github.com/evanw/node-source-map-support</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>source-map-url</td>
          <td>0.4.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/lydell/source-map-url.git">https://github.com/lydell/source-map-url.git</a></td>
          <td>Unknown</td>
          <td>Simon Lydell</td>
          </tr>
          <tr>
          <td>spdx-expression-parse</td>
          <td>3.0.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/jslicense/spdx-expression-parse.js.git">https://github.com/jslicense/spdx-expression-parse.js.git</a></td>
          <td><a href="https://kemitchell.com">https://kemitchell.com</a></td>
          <td>Kyle E. Mitchell</td>
          </tr>
          <tr>
          <td>spdy</td>
          <td>4.0.2</td>
          <td>MIT</td>
          <td>git://github.com/indutny/node-spdy.git</td>
          <td><a href="https://github.com/indutny/node-spdy">https://github.com/indutny/node-spdy</a></td>
          <td>Fedor Indutny</td>
          </tr>
          <tr>
          <td>spdy-transport</td>
          <td>3.0.0</td>
          <td>MIT</td>
          <td>git://github.com/spdy-http2/spdy-transport.git</td>
          <td><a href="https://github.com/spdy-http2/spdy-transport">https://github.com/spdy-http2/spdy-transport</a></td>
          <td>Fedor Indutny</td>
          </tr>
          <tr>
          <td>split-string</td>
          <td>3.1.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/split-string.git">https://github.com/jonschlinkert/split-string.git</a></td>
          <td><a href="https://github.com/jonschlinkert/split-string">https://github.com/jonschlinkert/split-string</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>sshpk</td>
          <td>1.16.1</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/joyent/node-sshpk.git">https://github.com/joyent/node-sshpk.git</a></td>
          <td><a href="https://github.com/arekinath/node-sshpk#readme">https://github.com/arekinath/node-sshpk#readme</a></td>
          <td>Joyent, Inc</td>
          </tr>
          <tr>
          <td>stable</td>
          <td>0.1.8</td>
          <td>MIT</td>
          <td><a href="https://github.com/Two-Screen/stable.git">https://github.com/Two-Screen/stable.git</a></td>
          <td>Unknown</td>
          <td>Angry Bytes</td>
          </tr>
          <tr>
          <td>stack-utils</td>
          <td>2.0.3</td>
          <td>MIT</td>
          <td><a href="https://github.com/tapjs/stack-utils.git">https://github.com/tapjs/stack-utils.git</a></td>
          <td>github.com/jamestalmage</td>
          <td>James Talmage</td>
          </tr>
          <tr>
          <td>stackframe</td>
          <td>1.2.0</td>
          <td>MIT</td>
          <td>git://github.com/stacktracejs/stackframe.git</td>
          <td><a href="https://www.stacktracejs.com/">https://www.stacktracejs.com/</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>static-extend</td>
          <td>0.1.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/static-extend.git">https://github.com/jonschlinkert/static-extend.git</a></td>
          <td><a href="https://github.com/jonschlinkert/static-extend">https://github.com/jonschlinkert/static-extend</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>statuses</td>
          <td>1.5.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/jshttp/statuses.git">https://github.com/jshttp/statuses.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>stream-browserify</td>
          <td>2.0.2</td>
          <td>MIT</td>
          <td>git://github.com/browserify/stream-browserify.git</td>
          <td><a href="https://github.com/browserify/stream-browserify">https://github.com/browserify/stream-browserify</a></td>
          <td>James Halliday</td>
          </tr>
          <tr>
          <td>stream-each</td>
          <td>1.2.3</td>
          <td>MIT</td>
          <td><a href="https://github.com/mafintosh/stream-each.git">https://github.com/mafintosh/stream-each.git</a></td>
          <td><a href="https://github.com/mafintosh/stream-each">https://github.com/mafintosh/stream-each</a></td>
          <td>Mathias Buus</td>
          </tr>
          <tr>
          <td>stream-http</td>
          <td>2.8.3</td>
          <td>MIT</td>
          <td>git://github.com/jhiesey/stream-http.git</td>
          <td><a href="https://github.com/jhiesey/stream-http#readme">https://github.com/jhiesey/stream-http#readme</a></td>
          <td>John Hiesey</td>
          </tr>
          <tr>
          <td>stream-shift</td>
          <td>1.0.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/mafintosh/stream-shift.git">https://github.com/mafintosh/stream-shift.git</a></td>
          <td><a href="https://github.com/mafintosh/stream-shift">https://github.com/mafintosh/stream-shift</a></td>
          <td>Mathias Buus</td>
          </tr>
          <tr>
          <td>strict-uri-encode</td>
          <td>1.1.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/kevva/strict-uri-encode.git">https://github.com/kevva/strict-uri-encode.git</a></td>
          <td>github.com/kevva</td>
          <td>Kevin Mårtensson</td>
          </tr>
          <tr>
          <td>string_decoder</td>
          <td>1.1.1</td>
          <td>MIT</td>
          <td>git://github.com/nodejs/string_decoder.git</td>
          <td><a href="https://github.com/nodejs/string_decoder">https://github.com/nodejs/string_decoder</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>string-width</td>
          <td>4.2.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/string-width.git">https://github.com/sindresorhus/string-width.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>string-width</td>
          <td>2.1.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/string-width.git">https://github.com/sindresorhus/string-width.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>string-width</td>
          <td>3.1.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/string-width.git">https://github.com/sindresorhus/string-width.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>string.prototype.trimend</td>
          <td>1.0.4</td>
          <td>MIT</td>
          <td>git://github.com/es-shims/String.prototype.trimEnd.git</td>
          <td>Unknown</td>
          <td>Jordan Harband</td>
          </tr>
          <tr>
          <td>string.prototype.trimstart</td>
          <td>1.0.4</td>
          <td>MIT</td>
          <td>git://github.com/es-shims/String.prototype.trimStart.git</td>
          <td>Unknown</td>
          <td>Jordan Harband</td>
          </tr>
          <tr>
          <td>strip-ansi</td>
          <td>6.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/chalk/strip-ansi.git">https://github.com/chalk/strip-ansi.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>strip-ansi</td>
          <td>5.2.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/chalk/strip-ansi.git">https://github.com/chalk/strip-ansi.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>strip-ansi</td>
          <td>3.0.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/chalk/strip-ansi.git">https://github.com/chalk/strip-ansi.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>strip-ansi</td>
          <td>4.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/chalk/strip-ansi.git">https://github.com/chalk/strip-ansi.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>strip-bom</td>
          <td>3.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/strip-bom.git">https://github.com/sindresorhus/strip-bom.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>strip-eof</td>
          <td>1.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/strip-eof.git">https://github.com/sindresorhus/strip-eof.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>strip-final-newline</td>
          <td>2.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/strip-final-newline.git">https://github.com/sindresorhus/strip-final-newline.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>strip-indent</td>
          <td>2.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/strip-indent.git">https://github.com/sindresorhus/strip-indent.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>strip-json-comments</td>
          <td>2.0.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/strip-json-comments.git">https://github.com/sindresorhus/strip-json-comments.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>stylehacks</td>
          <td>4.0.3</td>
          <td>MIT</td>
          <td><a href="https://github.com/cssnano/cssnano.git">https://github.com/cssnano/cssnano.git</a></td>
          <td><a href="https://github.com/cssnano/cssnano">https://github.com/cssnano/cssnano</a></td>
          <td>Ben Briggs</td>
          </tr>
          <tr>
          <td>supertap</td>
          <td>2.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/vadimdemedes/supertap.git">https://github.com/vadimdemedes/supertap.git</a></td>
          <td>github.com/vadimdemedes</td>
          <td>Vadim Demedes</td>
          </tr>
          <tr>
          <td>supports-color</td>
          <td>6.1.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/chalk/supports-color.git">https://github.com/chalk/supports-color.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>supports-color</td>
          <td>5.5.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/chalk/supports-color.git">https://github.com/chalk/supports-color.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>supports-color</td>
          <td>7.2.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/chalk/supports-color.git">https://github.com/chalk/supports-color.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>supports-color</td>
          <td>3.2.3</td>
          <td>MIT</td>
          <td><a href="https://github.com/chalk/supports-color.git">https://github.com/chalk/supports-color.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>supports-color</td>
          <td>2.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/chalk/supports-color.git">https://github.com/chalk/supports-color.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>svg-tags</td>
          <td>1.0.0</td>
          <td>MIT</td>
          <td>git://github.com/element-io/svg-tags.git</td>
          <td>Unknown</td>
          <td>Athan Reines</td>
          </tr>
          <tr>
          <td>svgo</td>
          <td>1.3.2</td>
          <td>MIT</td>
          <td>git://github.com/svg/svgo.git</td>
          <td><a href="https://github.com/svg/svgo">https://github.com/svg/svgo</a></td>
          <td>Kir Belevich</td>
          </tr>
          <tr>
          <td>symbol-observable</td>
          <td>1.2.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/blesh/symbol-observable.git">https://github.com/blesh/symbol-observable.git</a></td>
          <td>Unknown</td>
          <td>Ben Lesh</td>
          </tr>
          <tr>
          <td>symbol-tree</td>
          <td>3.2.4</td>
          <td>MIT</td>
          <td><a href="https://github.com/jsdom/js-symbol-tree.git">https://github.com/jsdom/js-symbol-tree.git</a></td>
          <td><a href="https://github.com/jsdom/js-symbol-tree#symbol-tree">https://github.com/jsdom/js-symbol-tree#symbol-tree</a></td>
          <td>Joris van der Wel</td>
          </tr>
          <tr>
          <td>tapable</td>
          <td>1.1.3</td>
          <td>MIT</td>
          <td><a href="http://github.com/webpack/tapable.git">http://github.com/webpack/tapable.git</a></td>
          <td><a href="https://github.com/webpack/tapable">https://github.com/webpack/tapable</a></td>
          <td>Tobias Koppers @sokra</td>
          </tr>
          <tr>
          <td>tapable</td>
          <td>0.1.10</td>
          <td>MIT</td>
          <td><a href="http://github.com/webpack/tapable.git">http://github.com/webpack/tapable.git</a></td>
          <td><a href="https://github.com/webpack/tapable">https://github.com/webpack/tapable</a></td>
          <td>Tobias Koppers @sokra</td>
          </tr>
          <tr>
          <td>temp-dir</td>
          <td>2.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/temp-dir.git">https://github.com/sindresorhus/temp-dir.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>terser-webpack-plugin</td>
          <td>1.4.5</td>
          <td>MIT</td>
          <td><a href="https://github.com/webpack-contrib/terser-webpack-plugin.git">https://github.com/webpack-contrib/terser-webpack-plugin.git</a></td>
          <td><a href="https://github.com/webpack-contrib/terser-webpack-plugin">https://github.com/webpack-contrib/terser-webpack-plugin</a></td>
          <td>webpack Contrib Team</td>
          </tr>
          <tr>
          <td>terser-webpack-plugin</td>
          <td>2.3.8</td>
          <td>MIT</td>
          <td><a href="https://github.com/webpack-contrib/terser-webpack-plugin.git">https://github.com/webpack-contrib/terser-webpack-plugin.git</a></td>
          <td><a href="https://github.com/webpack-contrib/terser-webpack-plugin">https://github.com/webpack-contrib/terser-webpack-plugin</a></td>
          <td>webpack Contrib Team</td>
          </tr>
          <tr>
          <td>text-table</td>
          <td>0.2.0</td>
          <td>MIT</td>
          <td>git://github.com/substack/text-table.git</td>
          <td><a href="https://github.com/substack/text-table">https://github.com/substack/text-table</a></td>
          <td>James Halliday</td>
          </tr>
          <tr>
          <td>thenify</td>
          <td>3.3.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/thenables/thenify.git">https://github.com/thenables/thenify.git</a></td>
          <td><a href="http://jongleberry.com">http://jongleberry.com</a></td>
          <td>Jonathan Ong</td>
          </tr>
          <tr>
          <td>thenify-all</td>
          <td>1.6.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/thenables/thenify-all.git">https://github.com/thenables/thenify-all.git</a></td>
          <td><a href="http://jongleberry.com">http://jongleberry.com</a></td>
          <td>Jonathan Ong</td>
          </tr>
          <tr>
          <td>thread-loader</td>
          <td>2.1.3</td>
          <td>MIT</td>
          <td><a href="https://github.com/webpack-contrib/thread-loader.git">https://github.com/webpack-contrib/thread-loader.git</a></td>
          <td><a href="https://github.com/webpack-contrib/thread-loader">https://github.com/webpack-contrib/thread-loader</a></td>
          <td>Tobias Koppers @sokra</td>
          </tr>
          <tr>
          <td>throttle-debounce</td>
          <td>2.3.0</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/niksy/throttle-debounce.git">https://github.com/niksy/throttle-debounce.git</a></td>
          <td><a href="https://github.com/niksy/throttle-debounce#readme">https://github.com/niksy/throttle-debounce#readme</a></td>
          <td>Ivan Nikolić</td>
          </tr>
          <tr>
          <td>through</td>
          <td>2.3.8</td>
          <td>MIT</td>
          <td><a href="https://github.com/dominictarr/through.git">https://github.com/dominictarr/through.git</a></td>
          <td><a href="https://github.com/dominictarr/through">https://github.com/dominictarr/through</a></td>
          <td>Dominic Tarr</td>
          </tr>
          <tr>
          <td>through2</td>
          <td>2.0.5</td>
          <td>MIT</td>
          <td><a href="https://github.com/rvagg/through2.git">https://github.com/rvagg/through2.git</a></td>
          <td><a href="https://github.com/rvagg">https://github.com/rvagg</a></td>
          <td>Rod Vagg</td>
          </tr>
          <tr>
          <td>thunky</td>
          <td>1.1.0</td>
          <td>MIT</td>
          <td>git://github.com/mafintosh/thunky.git</td>
          <td><a href="https://github.com/mafintosh/thunky#readme">https://github.com/mafintosh/thunky#readme</a></td>
          <td>Mathias Buus Madsen</td>
          </tr>
          <tr>
          <td>time-zone</td>
          <td>1.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/time-zone.git">https://github.com/sindresorhus/time-zone.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>timers-browserify</td>
          <td>2.0.12</td>
          <td>MIT</td>
          <td>git://github.com/jryans/timers-browserify.git</td>
          <td><a href="https://github.com/jryans/timers-browserify">https://github.com/jryans/timers-browserify</a></td>
          <td>J. Ryan Stinnett</td>
          </tr>
          <tr>
          <td>timsort</td>
          <td>0.3.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/mziccard/node-timsort.git">https://github.com/mziccard/node-timsort.git</a></td>
          <td><a href="https://github.com/mziccard/node-timsort">https://github.com/mziccard/node-timsort</a></td>
          <td>Marco Ziccardi</td>
          </tr>
          <tr>
          <td>tmp</td>
          <td>0.0.33</td>
          <td>MIT</td>
          <td><a href="https://github.com/raszi/node-tmp.git">https://github.com/raszi/node-tmp.git</a></td>
          <td><a href="http://github.com/raszi/node-tmp">http://github.com/raszi/node-tmp</a></td>
          <td>KARASZI István</td>
          </tr>
          <tr>
          <td>to-arraybuffer</td>
          <td>1.0.1</td>
          <td>MIT</td>
          <td>git://github.com/jhiesey/to-arraybuffer.git</td>
          <td><a href="https://github.com/jhiesey/to-arraybuffer#readme">https://github.com/jhiesey/to-arraybuffer#readme</a></td>
          <td>John Hiesey</td>
          </tr>
          <tr>
          <td>to-fast-properties</td>
          <td>2.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/to-fast-properties.git">https://github.com/sindresorhus/to-fast-properties.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>to-object-path</td>
          <td>0.3.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/to-object-path.git">https://github.com/jonschlinkert/to-object-path.git</a></td>
          <td><a href="https://github.com/jonschlinkert/to-object-path">https://github.com/jonschlinkert/to-object-path</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>to-readable-stream</td>
          <td>1.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/to-readable-stream.git">https://github.com/sindresorhus/to-readable-stream.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>to-regex</td>
          <td>3.0.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/to-regex.git">https://github.com/jonschlinkert/to-regex.git</a></td>
          <td><a href="https://github.com/jonschlinkert/to-regex">https://github.com/jonschlinkert/to-regex</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>to-regex-range</td>
          <td>2.1.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/micromatch/to-regex-range.git">https://github.com/micromatch/to-regex-range.git</a></td>
          <td><a href="https://github.com/micromatch/to-regex-range">https://github.com/micromatch/to-regex-range</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>to-regex-range</td>
          <td>5.0.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/micromatch/to-regex-range.git">https://github.com/micromatch/to-regex-range.git</a></td>
          <td><a href="https://github.com/micromatch/to-regex-range">https://github.com/micromatch/to-regex-range</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>toidentifier</td>
          <td>1.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/component/toidentifier.git">https://github.com/component/toidentifier.git</a></td>
          <td>Unknown</td>
          <td>Douglas Christopher Wilson</td>
          </tr>
          <tr>
          <td>toposort</td>
          <td>1.0.7</td>
          <td>MIT</td>
          <td><a href="https://github.com/marcelklehr/toposort.git">https://github.com/marcelklehr/toposort.git</a></td>
          <td>Unknown</td>
          <td>Marcel Klehr</td>
          </tr>
          <tr>
          <td>tr46</td>
          <td>2.0.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/jsdom/tr46">https://github.com/jsdom/tr46</a></td>
          <td>Unknown</td>
          <td>Sebastian Mayr</td>
          </tr>
          <tr>
          <td>trim-off-newlines</td>
          <td>1.0.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/stevemao/trim-off-newlines.git">https://github.com/stevemao/trim-off-newlines.git</a></td>
          <td>github.com/stevemao</td>
          <td>Steve Mao</td>
          </tr>
          <tr>
          <td>tryer</td>
          <td>1.0.1</td>
          <td>MIT</td>
          <td>git+<a href="https://gitlab.com/philbooth/tryer.git">https://gitlab.com/philbooth/tryer.git</a></td>
          <td><a href="https://gitlab.com/philbooth/tryer">https://gitlab.com/philbooth/tryer</a></td>
          <td>Phil Booth</td>
          </tr>
          <tr>
          <td>ts-invariant</td>
          <td>0.4.4</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/apollographql/invariant-packages.git">https://github.com/apollographql/invariant-packages.git</a></td>
          <td><a href="https://github.com/apollographql/invariant-packages">https://github.com/apollographql/invariant-packages</a></td>
          <td>Ben Newman</td>
          </tr>
          <tr>
          <td>ts-pnp</td>
          <td>1.2.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/arcanis/ts-pnp.git">https://github.com/arcanis/ts-pnp.git</a></td>
          <td><a href="https://github.com/arcanis/ts-pnp">https://github.com/arcanis/ts-pnp</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>tsconfig-paths</td>
          <td>3.9.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/dividab/tsconfig-paths">https://github.com/dividab/tsconfig-paths</a></td>
          <td>Unknown</td>
          <td>Jonas Kello</td>
          </tr>
          <tr>
          <td>tty-browserify</td>
          <td>0.0.0</td>
          <td>MIT</td>
          <td>git://github.com/substack/tty-browserify.git</td>
          <td><a href="https://github.com/substack/tty-browserify">https://github.com/substack/tty-browserify</a></td>
          <td>James Halliday</td>
          </tr>
          <tr>
          <td>type-check</td>
          <td>0.3.2</td>
          <td>MIT</td>
          <td>git://github.com/gkz/type-check.git</td>
          <td><a href="https://github.com/gkz/type-check">https://github.com/gkz/type-check</a></td>
          <td>George Zahariev</td>
          </tr>
          <tr>
          <td>type-is</td>
          <td>1.6.18</td>
          <td>MIT</td>
          <td><a href="https://github.com/jshttp/type-is.git">https://github.com/jshttp/type-is.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>typedarray</td>
          <td>0.0.6</td>
          <td>MIT</td>
          <td>git://github.com/substack/typedarray.git</td>
          <td><a href="https://github.com/substack/typedarray">https://github.com/substack/typedarray</a></td>
          <td>James Halliday</td>
          </tr>
          <tr>
          <td>typedarray-to-buffer</td>
          <td>3.1.5</td>
          <td>MIT</td>
          <td>git://github.com/feross/typedarray-to-buffer.git</td>
          <td><a href="http://feross.org/">http://feross.org/</a></td>
          <td>Feross Aboukhadijeh</td>
          </tr>
          <tr>
          <td>unbox-primitive</td>
          <td>1.0.0</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/ljharb/unbox-primitive.git">https://github.com/ljharb/unbox-primitive.git</a></td>
          <td><a href="https://github.com/ljharb/unbox-primitive#readme">https://github.com/ljharb/unbox-primitive#readme</a></td>
          <td>Jordan Harband</td>
          </tr>
          <tr>
          <td>underscore</td>
          <td>1.13.1</td>
          <td>MIT</td>
          <td>git://github.com/jashkenas/underscore.git</td>
          <td><a href="https://underscorejs.org/">https://underscorejs.org/</a></td>
          <td>Jeremy Ashkenas</td>
          </tr>
          <tr>
          <td>unicode-canonical-property-names-ecmascript</td>
          <td>1.0.4</td>
          <td>MIT</td>
          <td><a href="https://github.com/mathiasbynens/unicode-canonical-property-names-ecmascript.git">https://github.com/mathiasbynens/unicode-canonical-property-names-ecmascript.git</a></td>
          <td><a href="https://github.com/mathiasbynens/unicode-canonical-property-names-ecmascript">https://github.com/mathiasbynens/unicode-canonical-property-names-ecmascript</a></td>
          <td>Mathias Bynens</td>
          </tr>
          <tr>
          <td>unicode-match-property-ecmascript</td>
          <td>1.0.4</td>
          <td>MIT</td>
          <td><a href="https://github.com/mathiasbynens/unicode-match-property-ecmascript.git">https://github.com/mathiasbynens/unicode-match-property-ecmascript.git</a></td>
          <td><a href="https://github.com/mathiasbynens/unicode-match-property-ecmascript">https://github.com/mathiasbynens/unicode-match-property-ecmascript</a></td>
          <td>Mathias Bynens</td>
          </tr>
          <tr>
          <td>unicode-match-property-value-ecmascript</td>
          <td>1.2.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/mathiasbynens/unicode-match-property-value-ecmascript.git">https://github.com/mathiasbynens/unicode-match-property-value-ecmascript.git</a></td>
          <td><a href="https://github.com/mathiasbynens/unicode-match-property-value-ecmascript">https://github.com/mathiasbynens/unicode-match-property-value-ecmascript</a></td>
          <td>Mathias Bynens</td>
          </tr>
          <tr>
          <td>unicode-property-aliases-ecmascript</td>
          <td>1.1.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/mathiasbynens/unicode-property-aliases-ecmascript.git">https://github.com/mathiasbynens/unicode-property-aliases-ecmascript.git</a></td>
          <td><a href="https://github.com/mathiasbynens/unicode-property-aliases-ecmascript">https://github.com/mathiasbynens/unicode-property-aliases-ecmascript</a></td>
          <td>Mathias Bynens</td>
          </tr>
          <tr>
          <td>union-value</td>
          <td>1.0.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/union-value.git">https://github.com/jonschlinkert/union-value.git</a></td>
          <td><a href="https://github.com/jonschlinkert/union-value">https://github.com/jonschlinkert/union-value</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>uniq</td>
          <td>1.0.1</td>
          <td>MIT</td>
          <td>git://github.com/mikolalysenko/uniq.git</td>
          <td>Unknown</td>
          <td>Mikola Lysenko</td>
          </tr>
          <tr>
          <td>uniqs</td>
          <td>2.0.0</td>
          <td>MIT</td>
          <td>git://github.com/fgnass/uniqs.git</td>
          <td>Unknown</td>
          <td>Felix Gnass</td>
          </tr>
          <tr>
          <td>unique-string</td>
          <td>2.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/unique-string.git">https://github.com/sindresorhus/unique-string.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>universalify</td>
          <td>0.1.2</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/RyanZim/universalify.git">https://github.com/RyanZim/universalify.git</a></td>
          <td><a href="https://github.com/RyanZim/universalify#readme">https://github.com/RyanZim/universalify#readme</a></td>
          <td>Ryan Zimmerman</td>
          </tr>
          <tr>
          <td>unpipe</td>
          <td>1.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/stream-utils/unpipe.git">https://github.com/stream-utils/unpipe.git</a></td>
          <td>Unknown</td>
          <td>Douglas Christopher Wilson</td>
          </tr>
          <tr>
          <td>unquote</td>
          <td>1.1.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/lakenen/node-unquote.git">https://github.com/lakenen/node-unquote.git</a></td>
          <td><a href="https://github.com/lakenen/node-unquote">https://github.com/lakenen/node-unquote</a></td>
          <td>Cameron Lakenen</td>
          </tr>
          <tr>
          <td>unset-value</td>
          <td>1.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/unset-value.git">https://github.com/jonschlinkert/unset-value.git</a></td>
          <td><a href="https://github.com/jonschlinkert/unset-value">https://github.com/jonschlinkert/unset-value</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>upath</td>
          <td>1.2.0</td>
          <td>MIT</td>
          <td>git://github.com/anodynos/upath</td>
          <td><a href="http://github.com/anodynos/upath/">http://github.com/anodynos/upath/</a></td>
          <td>Angelos Pikoulas</td>
          </tr>
          <tr>
          <td>upper-case</td>
          <td>1.1.3</td>
          <td>MIT</td>
          <td>git://github.com/blakeembrey/upper-case.git</td>
          <td><a href="https://github.com/blakeembrey/upper-case">https://github.com/blakeembrey/upper-case</a></td>
          <td>Blake Embrey</td>
          </tr>
          <tr>
          <td>urix</td>
          <td>0.1.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/lydell/urix.git">https://github.com/lydell/urix.git</a></td>
          <td>Unknown</td>
          <td>Simon Lydell</td>
          </tr>
          <tr>
          <td>url</td>
          <td>0.11.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/defunctzombie/node-url.git">https://github.com/defunctzombie/node-url.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>url-join</td>
          <td>1.1.0</td>
          <td>MIT</td>
          <td>git://github.com/jfromaniello/url-join.git</td>
          <td><a href="http://joseoncode.com">http://joseoncode.com</a></td>
          <td>José F. Romaniello</td>
          </tr>
          <tr>
          <td>url-loader</td>
          <td>2.3.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/webpack-contrib/url-loader.git">https://github.com/webpack-contrib/url-loader.git</a></td>
          <td><a href="https://github.com/webpack-contrib/url-loader">https://github.com/webpack-contrib/url-loader</a></td>
          <td>Tobias Koppers @sokra</td>
          </tr>
          <tr>
          <td>url-parse</td>
          <td>1.5.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/unshiftio/url-parse.git">https://github.com/unshiftio/url-parse.git</a></td>
          <td>Unknown</td>
          <td>Arnout Kazemier</td>
          </tr>
          <tr>
          <td>url-parse-lax</td>
          <td>3.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/url-parse-lax.git">https://github.com/sindresorhus/url-parse-lax.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>use</td>
          <td>3.1.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/use.git">https://github.com/jonschlinkert/use.git</a></td>
          <td><a href="https://github.com/jonschlinkert/use">https://github.com/jonschlinkert/use</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>util</td>
          <td>0.11.1</td>
          <td>MIT</td>
          <td>git://github.com/defunctzombie/node-util</td>
          <td><a href="https://github.com/defunctzombie/node-util">https://github.com/defunctzombie/node-util</a></td>
          <td>Joyent</td>
          </tr>
          <tr>
          <td>util</td>
          <td>0.10.3</td>
          <td>MIT</td>
          <td>git://github.com/defunctzombie/node-util</td>
          <td><a href="https://github.com/defunctzombie/node-util">https://github.com/defunctzombie/node-util</a></td>
          <td>Joyent</td>
          </tr>
          <tr>
          <td>util-deprecate</td>
          <td>1.0.2</td>
          <td>MIT</td>
          <td>git://github.com/TooTallNate/util-deprecate.git</td>
          <td><a href="https://github.com/TooTallNate/util-deprecate">https://github.com/TooTallNate/util-deprecate</a></td>
          <td>Nathan Rajlich</td>
          </tr>
          <tr>
          <td>util.promisify</td>
          <td>1.0.0</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/ljharb/util.promisify.git">https://github.com/ljharb/util.promisify.git</a></td>
          <td><a href="https://github.com/ljharb/util.promisify#readme">https://github.com/ljharb/util.promisify#readme</a></td>
          <td>Jordan Harband</td>
          </tr>
          <tr>
          <td>util.promisify</td>
          <td>1.0.1</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/ljharb/util.promisify.git">https://github.com/ljharb/util.promisify.git</a></td>
          <td><a href="https://github.com/ljharb/util.promisify#readme">https://github.com/ljharb/util.promisify#readme</a></td>
          <td>Jordan Harband</td>
          </tr>
          <tr>
          <td>utila</td>
          <td>0.4.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/AriaMinaei/utila.git">https://github.com/AriaMinaei/utila.git</a></td>
          <td>Unknown</td>
          <td>Aria Minaei</td>
          </tr>
          <tr>
          <td>utils-merge</td>
          <td>1.0.1</td>
          <td>MIT</td>
          <td>git://github.com/jaredhanson/utils-merge.git</td>
          <td><a href="http://www.jaredhanson.net/">http://www.jaredhanson.net/</a></td>
          <td>Jared Hanson</td>
          </tr>
          <tr>
          <td>uuid</td>
          <td>3.4.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/uuidjs/uuid.git">https://github.com/uuidjs/uuid.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>vary</td>
          <td>1.1.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/jshttp/vary.git">https://github.com/jshttp/vary.git</a></td>
          <td>Unknown</td>
          <td>Douglas Christopher Wilson</td>
          </tr>
          <tr>
          <td>vendors</td>
          <td>1.0.4</td>
          <td>MIT</td>
          <td><a href="https://github.com/wooorm/vendors.git">https://github.com/wooorm/vendors.git</a></td>
          <td><a href="https://wooorm.com">https://wooorm.com</a></td>
          <td>Titus Wormer</td>
          </tr>
          <tr>
          <td>verror</td>
          <td>1.10.0</td>
          <td>MIT</td>
          <td>git://github.com/davepacheco/node-verror.git</td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>vh-check</td>
          <td>2.0.5</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/Hiswe/vh-check.git">https://github.com/Hiswe/vh-check.git</a></td>
          <td><a href="https://github.com/Hiswe/vh-check#readme">https://github.com/Hiswe/vh-check#readme</a></td>
          <td>hiswe</td>
          </tr>
          <tr>
          <td>vm-browserify</td>
          <td>1.1.2</td>
          <td>MIT</td>
          <td><a href="http://github.com/substack/vm-browserify.git">http://github.com/substack/vm-browserify.git</a></td>
          <td><a href="http://substack.net">http://substack.net</a></td>
          <td>James Halliday</td>
          </tr>
          <tr>
          <td>vue</td>
          <td>2.6.12</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/vuejs/vue.git">https://github.com/vuejs/vue.git</a></td>
          <td><a href="https://github.com/vuejs/vue#readme">https://github.com/vuejs/vue#readme</a></td>
          <td>Evan You</td>
          </tr>
          <tr>
          <td>vue-apollo</td>
          <td>3.0.7</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/Akryum/vue-apollo.git">https://github.com/Akryum/vue-apollo.git</a></td>
          <td><a href="https://github.com/Akryum/vue-apollo#readme">https://github.com/Akryum/vue-apollo#readme</a></td>
          <td>Guillaume Chau</td>
          </tr>
          <tr>
          <td>vue-cli-plugin-prerender-spa</td>
          <td>1.1.6</td>
          <td>MIT</td>
          <td><a href="https://github.com/SolarLiner/vue-cli-plugin-prerender-spa">https://github.com/SolarLiner/vue-cli-plugin-prerender-spa</a></td>
          <td>Unknown</td>
          <td>Nathan Graule</td>
          </tr>
          <tr>
          <td>vue-cli-plugin-vuetify</td>
          <td>2.2.0</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/vuetifyjs/vue-cli-plugin-vuetify.git">https://github.com/vuetifyjs/vue-cli-plugin-vuetify.git</a></td>
          <td><a href="https://github.com/vuetifyjs/vue-cli-plugin-vuetify#readme">https://github.com/vuetifyjs/vue-cli-plugin-vuetify#readme</a></td>
          <td>John Leider</td>
          </tr>
          <tr>
          <td>vue-cookies</td>
          <td>1.7.4</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/cmp-cc/vue-cookies.git">https://github.com/cmp-cc/vue-cookies.git</a></td>
          <td><a href="https://github.com/cmp-cc/vue-cookies#readme">https://github.com/cmp-cc/vue-cookies#readme</a></td>
          <td>cmp-cc</td>
          </tr>
          <tr>
          <td>vue-eslint-parser</td>
          <td>5.0.0</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/mysticatea/vue-eslint-parser.git">https://github.com/mysticatea/vue-eslint-parser.git</a></td>
          <td><a href="https://github.com/mysticatea/vue-eslint-parser#readme">https://github.com/mysticatea/vue-eslint-parser#readme</a></td>
          <td>Toru Nagashima</td>
          </tr>
          <tr>
          <td>vue-hot-reload-api</td>
          <td>2.3.4</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/vuejs/vue-hot-reload-api.git">https://github.com/vuejs/vue-hot-reload-api.git</a></td>
          <td><a href="https://github.com/vuejs/vue-hot-reload-api#readme">https://github.com/vuejs/vue-hot-reload-api#readme</a></td>
          <td>Evan You</td>
          </tr>
          <tr>
          <td>vue-i18n</td>
          <td>8.23.0</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/kazupon/vue-i18n.git">https://github.com/kazupon/vue-i18n.git</a></td>
          <td><a href="https://github.com/kazupon/vue-i18n#readme">https://github.com/kazupon/vue-i18n#readme</a></td>
          <td>kazuya kawaguchi</td>
          </tr>
          <tr>
          <td>vue-loader</td>
          <td>15.9.6</td>
          <td>MIT</td>
          <td><a href="https://github.com/vuejs/vue-loader.git">https://github.com/vuejs/vue-loader.git</a></td>
          <td><a href="https://github.com/vuejs/vue-loader">https://github.com/vuejs/vue-loader</a></td>
          <td>Evan You</td>
          </tr>
          <tr>
          <td>vue-loader-v16</td>
          <td>16.1.2</td>
          <td>MIT</td>
          <td>Unknown</td>
          <td>Unknown</td>
          <td>Evan You</td>
          </tr>
          <tr>
          <td>vue-router</td>
          <td>3.5.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/vuejs/vue-router.git">https://github.com/vuejs/vue-router.git</a></td>
          <td><a href="https://github.com/vuejs/vue-router#readme">https://github.com/vuejs/vue-router#readme</a></td>
          <td>Evan You</td>
          </tr>
          <tr>
          <td>vue-router-sitemap</td>
          <td>0.0.4</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/40818419/vue-router-sitemap.git">https://github.com/40818419/vue-router-sitemap.git</a></td>
          <td><a href="https://github.com/40818419/vue-router-sitemap#readme">https://github.com/40818419/vue-router-sitemap#readme</a></td>
          <td>Konstantin Kulinicenko</td>
          </tr>
          <tr>
          <td>vue-style-loader</td>
          <td>4.1.2</td>
          <td>MIT</td>
          <td>git@github.com:vuejs/vue-style-loader.git</td>
          <td>Unknown</td>
          <td>Evan You</td>
          </tr>
          <tr>
          <td>vue-template-compiler</td>
          <td>2.6.12</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/vuejs/vue.git">https://github.com/vuejs/vue.git</a></td>
          <td><a href="https://github.com/vuejs/vue/tree/dev/packages/vue-template-compiler#readme">https://github.com/vuejs/vue/tree/dev/packages/vue-template-compiler#readme</a></td>
          <td>Evan You</td>
          </tr>
          <tr>
          <td>vue-template-es2015-compiler</td>
          <td>1.9.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/vuejs/vue-template-es2015-compiler">https://github.com/vuejs/vue-template-es2015-compiler</a></td>
          <td>Unknown</td>
          <td>Evan You</td>
          </tr>
          <tr>
          <td>vue-test-utils</td>
          <td>1.0.0-beta.11</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/vuejs/vue-test-utils.git">https://github.com/vuejs/vue-test-utils.git</a></td>
          <td><a href="https://github.com/vuejs/vue-test-utils#readme">https://github.com/vuejs/vue-test-utils#readme</a></td>
          <td>vuejs</td>
          </tr>
          <tr>
          <td>vuetify</td>
          <td>2.4.5</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/vuetifyjs/vuetify.git">https://github.com/vuetifyjs/vuetify.git</a></td>
          <td><a href="https://vuetifyjs.com/">https://vuetifyjs.com/</a></td>
          <td>John Leider</td>
          </tr>
          <tr>
          <td>vuetify-loader</td>
          <td>1.7.2</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/vuetifyjs/vuetify-loader.git">https://github.com/vuetifyjs/vuetify-loader.git</a></td>
          <td><a href="https://github.com/vuetifyjs/vuetify-loader#readme">https://github.com/vuetifyjs/vuetify-loader#readme</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>vuex</td>
          <td>3.6.2</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/vuejs/vuex.git">https://github.com/vuejs/vuex.git</a></td>
          <td><a href="https://github.com/vuejs/vuex#readme">https://github.com/vuejs/vuex#readme</a></td>
          <td>Evan You</td>
          </tr>
          <tr>
          <td>w3c-hr-time</td>
          <td>1.0.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/jsdom/w3c-hr-time">https://github.com/jsdom/w3c-hr-time</a></td>
          <td>Unknown</td>
          <td>Timothy Gu</td>
          </tr>
          <tr>
          <td>w3c-xmlserializer</td>
          <td>2.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/jsdom/w3c-xmlserializer.git">https://github.com/jsdom/w3c-xmlserializer.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>watchpack</td>
          <td>1.7.5</td>
          <td>MIT</td>
          <td><a href="https://github.com/webpack/watchpack.git">https://github.com/webpack/watchpack.git</a></td>
          <td><a href="https://github.com/webpack/watchpack">https://github.com/webpack/watchpack</a></td>
          <td>Tobias Koppers @sokra</td>
          </tr>
          <tr>
          <td>watchpack-chokidar2</td>
          <td>2.0.1</td>
          <td>MIT</td>
          <td><a href="https://github.com/webpack/watchpack.git">https://github.com/webpack/watchpack.git</a></td>
          <td><a href="https://github.com/webpack/watchpack">https://github.com/webpack/watchpack</a></td>
          <td>Tobias Koppers @sokra</td>
          </tr>
          <tr>
          <td>wbuf</td>
          <td>1.7.3</td>
          <td>MIT</td>
          <td>git@github.com:indutny/wbuf</td>
          <td><a href="https://github.com/indutny/wbuf">https://github.com/indutny/wbuf</a></td>
          <td>Fedor Indutny</td>
          </tr>
          <tr>
          <td>wcwidth</td>
          <td>1.0.1</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/timoxley/wcwidth.git">https://github.com/timoxley/wcwidth.git</a></td>
          <td><a href="https://github.com/timoxley/wcwidth#readme">https://github.com/timoxley/wcwidth#readme</a></td>
          <td>Tim Oxley</td>
          </tr>
          <tr>
          <td>webpack</td>
          <td>4.46.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/webpack/webpack.git">https://github.com/webpack/webpack.git</a></td>
          <td><a href="https://github.com/webpack/webpack">https://github.com/webpack/webpack</a></td>
          <td>Tobias Koppers @sokra</td>
          </tr>
          <tr>
          <td>webpack-bundle-analyzer</td>
          <td>3.9.0</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/webpack-contrib/webpack-bundle-analyzer.git">https://github.com/webpack-contrib/webpack-bundle-analyzer.git</a></td>
          <td><a href="https://github.com/webpack-contrib/webpack-bundle-analyzer">https://github.com/webpack-contrib/webpack-bundle-analyzer</a></td>
          <td>Yury Grunin</td>
          </tr>
          <tr>
          <td>webpack-dev-middleware</td>
          <td>3.7.3</td>
          <td>MIT</td>
          <td><a href="https://github.com/webpack/webpack-dev-middleware.git">https://github.com/webpack/webpack-dev-middleware.git</a></td>
          <td><a href="https://github.com/webpack/webpack-dev-middleware">https://github.com/webpack/webpack-dev-middleware</a></td>
          <td>Tobias Koppers @sokra</td>
          </tr>
          <tr>
          <td>webpack-dev-server</td>
          <td>3.11.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/webpack/webpack-dev-server.git">https://github.com/webpack/webpack-dev-server.git</a></td>
          <td><a href="https://github.com/webpack/webpack-dev-server#readme">https://github.com/webpack/webpack-dev-server#readme</a></td>
          <td>Tobias Koppers @sokra</td>
          </tr>
          <tr>
          <td>webpack-log</td>
          <td>2.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/webpack-contrib/webpack-log.git">https://github.com/webpack-contrib/webpack-log.git</a></td>
          <td><a href="https://github.com/webpack-contrib/webpack-log#readme">https://github.com/webpack-contrib/webpack-log#readme</a></td>
          <td>Andrew Powell</td>
          </tr>
          <tr>
          <td>webpack-merge</td>
          <td>4.2.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/survivejs/webpack-merge.git">https://github.com/survivejs/webpack-merge.git</a></td>
          <td><a href="https://github.com/survivejs/webpack-merge">https://github.com/survivejs/webpack-merge</a></td>
          <td>Juho Vepsalainen</td>
          </tr>
          <tr>
          <td>webpack-sources</td>
          <td>1.4.3</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/webpack/webpack-sources.git">https://github.com/webpack/webpack-sources.git</a></td>
          <td><a href="https://github.com/webpack/webpack-sources#readme">https://github.com/webpack/webpack-sources#readme</a></td>
          <td>Tobias Koppers @sokra</td>
          </tr>
          <tr>
          <td>whatwg-encoding</td>
          <td>1.0.5</td>
          <td>MIT</td>
          <td><a href="https://github.com/jsdom/whatwg-encoding.git">https://github.com/jsdom/whatwg-encoding.git</a></td>
          <td><a href="https://domenic.me/">https://domenic.me/</a></td>
          <td>Domenic Denicola</td>
          </tr>
          <tr>
          <td>whatwg-fetch</td>
          <td>3.6.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/github/fetch.git">https://github.com/github/fetch.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>whatwg-mimetype</td>
          <td>2.3.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/jsdom/whatwg-mimetype.git">https://github.com/jsdom/whatwg-mimetype.git</a></td>
          <td><a href="https://domenic.me/">https://domenic.me/</a></td>
          <td>Domenic Denicola</td>
          </tr>
          <tr>
          <td>whatwg-url</td>
          <td>8.4.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/jsdom/whatwg-url.git">https://github.com/jsdom/whatwg-url.git</a></td>
          <td>Unknown</td>
          <td>Sebastian Mayr</td>
          </tr>
          <tr>
          <td>which-boxed-primitive</td>
          <td>1.0.2</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/inspect-js/which-boxed-primitive.git">https://github.com/inspect-js/which-boxed-primitive.git</a></td>
          <td><a href="https://github.com/inspect-js/which-boxed-primitive#readme">https://github.com/inspect-js/which-boxed-primitive#readme</a></td>
          <td>Jordan Harband</td>
          </tr>
          <tr>
          <td>widest-line</td>
          <td>3.1.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/widest-line.git">https://github.com/sindresorhus/widest-line.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>word-wrap</td>
          <td>1.2.3</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/word-wrap.git">https://github.com/jonschlinkert/word-wrap.git</a></td>
          <td><a href="https://github.com/jonschlinkert/word-wrap">https://github.com/jonschlinkert/word-wrap</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>worker-farm</td>
          <td>1.7.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/rvagg/node-worker-farm.git">https://github.com/rvagg/node-worker-farm.git</a></td>
          <td><a href="https://github.com/rvagg/node-worker-farm">https://github.com/rvagg/node-worker-farm</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>wrap-ansi</td>
          <td>6.2.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/chalk/wrap-ansi.git">https://github.com/chalk/wrap-ansi.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>wrap-ansi</td>
          <td>7.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/chalk/wrap-ansi.git">https://github.com/chalk/wrap-ansi.git</a></td>
          <td><a href="https://sindresorhus.com">https://sindresorhus.com</a></td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>wrap-ansi</td>
          <td>5.1.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/chalk/wrap-ansi.git">https://github.com/chalk/wrap-ansi.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>write</td>
          <td>1.0.3</td>
          <td>MIT</td>
          <td><a href="https://github.com/jonschlinkert/write.git">https://github.com/jonschlinkert/write.git</a></td>
          <td><a href="https://github.com/jonschlinkert/write">https://github.com/jonschlinkert/write</a></td>
          <td>Jon Schlinkert</td>
          </tr>
          <tr>
          <td>ws</td>
          <td>7.5.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/websockets/ws.git">https://github.com/websockets/ws.git</a></td>
          <td><a href="https://github.com/websockets/ws">https://github.com/websockets/ws</a></td>
          <td>Einar Otto Stangvik</td>
          </tr>
          <tr>
          <td>ws</td>
          <td>6.2.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/websockets/ws.git">https://github.com/websockets/ws.git</a></td>
          <td><a href="https://github.com/websockets/ws">https://github.com/websockets/ws</a></td>
          <td>Einar Otto Stangvik</td>
          </tr>
          <tr>
          <td>ws</td>
          <td>7.4.3</td>
          <td>MIT</td>
          <td><a href="https://github.com/websockets/ws.git">https://github.com/websockets/ws.git</a></td>
          <td><a href="https://github.com/websockets/ws">https://github.com/websockets/ws</a></td>
          <td>Einar Otto Stangvik</td>
          </tr>
          <tr>
          <td>xdg-basedir</td>
          <td>4.0.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/sindresorhus/xdg-basedir.git">https://github.com/sindresorhus/xdg-basedir.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>xmlchars</td>
          <td>2.2.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/lddubeau/xmlchars.git">https://github.com/lddubeau/xmlchars.git</a></td>
          <td>Unknown</td>
          <td>Louis-Dominique Dubeau</td>
          </tr>
          <tr>
          <td>xtend</td>
          <td>4.0.2</td>
          <td>MIT</td>
          <td>git://github.com/Raynos/xtend.git</td>
          <td><a href="https://github.com/Raynos/xtend">https://github.com/Raynos/xtend</a></td>
          <td>Raynos</td>
          </tr>
          <tr>
          <td>yargs</td>
          <td>16.2.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/yargs/yargs.git">https://github.com/yargs/yargs.git</a></td>
          <td><a href="https://yargs.js.org/">https://yargs.js.org/</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>yargs</td>
          <td>13.3.2</td>
          <td>MIT</td>
          <td><a href="https://github.com/yargs/yargs.git">https://github.com/yargs/yargs.git</a></td>
          <td><a href="https://yargs.js.org/">https://yargs.js.org/</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>yauzl</td>
          <td>2.10.0</td>
          <td>MIT</td>
          <td><a href="https://github.com/thejoshwolfe/yauzl.git">https://github.com/thejoshwolfe/yauzl.git</a></td>
          <td><a href="https://github.com/thejoshwolfe/yauzl">https://github.com/thejoshwolfe/yauzl</a></td>
          <td>Josh Wolfe</td>
          </tr>
          <tr>
          <td>yorkie</td>
          <td>2.0.0</td>
          <td>MIT</td>
          <td>git://github.com/yyx990803/yorkie.git</td>
          <td><a href="https://github.com/yyx990803/yorkie">https://github.com/yyx990803/yorkie</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>zen-observable</td>
          <td>0.8.15</td>
          <td>MIT</td>
          <td><a href="https://github.com/zenparsing/zen-observable.git">https://github.com/zenparsing/zen-observable.git</a></td>
          <td><a href="https://github.com/zenparsing/zen-observable">https://github.com/zenparsing/zen-observable</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>zen-observable-ts</td>
          <td>0.8.21</td>
          <td>MIT</td>
          <td>git+<a href="https://github.com/apollographql/apollo-link.git">https://github.com/apollographql/apollo-link.git</a></td>
          <td><a href="https://github.com/zenparsing/zen-observable">https://github.com/zenparsing/zen-observable</a></td>
          <td>Evans Hauser</td>
          </tr>
          <tr>
          <td>@concordance/react</td>
          <td>2.0.0</td>
          <td>ISC</td>
          <td>git+<a href="https://github.com/concordancejs/react.git">https://github.com/concordancejs/react.git</a></td>
          <td><a href="https://github.com/concordancejs/react#readme">https://github.com/concordancejs/react#readme</a></td>
          <td>Mark Wubben</td>
          </tr>
          <tr>
          <td>@webassemblyjs/helper-fsm</td>
          <td>1.9.0</td>
          <td>ISC</td>
          <td>Unknown</td>
          <td>Unknown</td>
          <td>Mauro Bringolf</td>
          </tr>
          <tr>
          <td>abbrev</td>
          <td>1.1.1</td>
          <td>ISC</td>
          <td><a href="http://github.com/isaacs/abbrev-js">http://github.com/isaacs/abbrev-js</a></td>
          <td>Unknown</td>
          <td>Isaac Z. Schlueter</td>
          </tr>
          <tr>
          <td>ansi-align</td>
          <td>3.0.0</td>
          <td>ISC</td>
          <td>git+<a href="https://github.com/nexdrew/ansi-align.git">https://github.com/nexdrew/ansi-align.git</a></td>
          <td><a href="https://github.com/nexdrew/ansi-align#readme">https://github.com/nexdrew/ansi-align#readme</a></td>
          <td>nexdrew</td>
          </tr>
          <tr>
          <td>anymatch</td>
          <td>3.1.1</td>
          <td>ISC</td>
          <td><a href="https://github.com/micromatch/anymatch">https://github.com/micromatch/anymatch</a></td>
          <td><a href="https://github.com/micromatch/anymatch">https://github.com/micromatch/anymatch</a></td>
          <td>Elan Shanker</td>
          </tr>
          <tr>
          <td>anymatch</td>
          <td>2.0.0</td>
          <td>ISC</td>
          <td><a href="https://github.com/micromatch/anymatch">https://github.com/micromatch/anymatch</a></td>
          <td><a href="https://github.com/micromatch/anymatch">https://github.com/micromatch/anymatch</a></td>
          <td>Elan Shanker</td>
          </tr>
          <tr>
          <td>aproba</td>
          <td>1.2.0</td>
          <td>ISC</td>
          <td><a href="https://github.com/iarna/aproba">https://github.com/iarna/aproba</a></td>
          <td><a href="https://github.com/iarna/aproba">https://github.com/iarna/aproba</a></td>
          <td>Rebecca Turner</td>
          </tr>
          <tr>
          <td>boolbase</td>
          <td>1.0.0</td>
          <td>ISC</td>
          <td><a href="https://github.com/fb55/boolbase">https://github.com/fb55/boolbase</a></td>
          <td><a href="https://github.com/fb55/boolbase">https://github.com/fb55/boolbase</a></td>
          <td>Felix Boehm</td>
          </tr>
          <tr>
          <td>browserify-sign</td>
          <td>4.2.1</td>
          <td>ISC</td>
          <td><a href="https://github.com/crypto-browserify/browserify-sign.git">https://github.com/crypto-browserify/browserify-sign.git</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>cacache</td>
          <td>12.0.4</td>
          <td>ISC</td>
          <td><a href="https://github.com/npm/cacache">https://github.com/npm/cacache</a></td>
          <td>Unknown</td>
          <td>Kat Marchán</td>
          </tr>
          <tr>
          <td>cacache</td>
          <td>13.0.1</td>
          <td>ISC</td>
          <td><a href="https://github.com/npm/cacache">https://github.com/npm/cacache</a></td>
          <td>Unknown</td>
          <td>Kat Marchán</td>
          </tr>
          <tr>
          <td>chownr</td>
          <td>1.1.4</td>
          <td>ISC</td>
          <td>git://github.com/isaacs/chownr.git</td>
          <td><a href="http://blog.izs.me/">http://blog.izs.me/</a></td>
          <td>Isaac Z. Schlueter</td>
          </tr>
          <tr>
          <td>cli-highlight</td>
          <td>2.1.10</td>
          <td>ISC</td>
          <td><a href="https://github.com/felixfbecker/cli-highlight.git">https://github.com/felixfbecker/cli-highlight.git</a></td>
          <td><a href="https://github.com/felixfbecker/cli-highlight#readme">https://github.com/felixfbecker/cli-highlight#readme</a></td>
          <td>Felix Becker</td>
          </tr>
          <tr>
          <td>cli-width</td>
          <td>3.0.0</td>
          <td>ISC</td>
          <td>git@github.com:knownasilya/cli-width.git</td>
          <td><a href="https://github.com/knownasilya/cli-width">https://github.com/knownasilya/cli-width</a></td>
          <td>Ilya Radchenko</td>
          </tr>
          <tr>
          <td>cli-width</td>
          <td>2.2.1</td>
          <td>ISC</td>
          <td>git@github.com:knownasilya/cli-width.git</td>
          <td><a href="https://github.com/knownasilya/cli-width">https://github.com/knownasilya/cli-width</a></td>
          <td>Ilya Radchenko</td>
          </tr>
          <tr>
          <td>cliui</td>
          <td>6.0.0</td>
          <td>ISC</td>
          <td><a href="http://github.com/yargs/cliui.git">http://github.com/yargs/cliui.git</a></td>
          <td>Unknown</td>
          <td>Ben Coe</td>
          </tr>
          <tr>
          <td>cliui</td>
          <td>7.0.4</td>
          <td>ISC</td>
          <td><a href="https://github.com/yargs/cliui.git">https://github.com/yargs/cliui.git</a></td>
          <td>Unknown</td>
          <td>Ben Coe</td>
          </tr>
          <tr>
          <td>cliui</td>
          <td>5.0.0</td>
          <td>ISC</td>
          <td><a href="http://github.com/yargs/cliui.git">http://github.com/yargs/cliui.git</a></td>
          <td>Unknown</td>
          <td>Ben Coe</td>
          </tr>
          <tr>
          <td>common-path-prefix</td>
          <td>3.0.0</td>
          <td>ISC</td>
          <td>git+<a href="https://github.com/novemberborn/common-path-prefix.git">https://github.com/novemberborn/common-path-prefix.git</a></td>
          <td><a href="https://github.com/novemberborn/common-path-prefix#readme">https://github.com/novemberborn/common-path-prefix#readme</a></td>
          <td>Mark Wubben</td>
          </tr>
          <tr>
          <td>concordance</td>
          <td>5.0.3</td>
          <td>ISC</td>
          <td>git+<a href="https://github.com/concordancejs/concordance.git">https://github.com/concordancejs/concordance.git</a></td>
          <td><a href="https://github.com/concordancejs/concordance#readme">https://github.com/concordancejs/concordance#readme</a></td>
          <td>Mark Wubben</td>
          </tr>
          <tr>
          <td>copy-concurrently</td>
          <td>1.0.5</td>
          <td>ISC</td>
          <td>git+<a href="https://github.com/npm/copy-concurrently.git">https://github.com/npm/copy-concurrently.git</a></td>
          <td><a href="https://www.npmjs.com/package/copy-concurrently">https://www.npmjs.com/package/copy-concurrently</a></td>
          <td>Rebecca Turner</td>
          </tr>
          <tr>
          <td>detect-node</td>
          <td>2.0.4</td>
          <td>ISC</td>
          <td><a href="https://github.com/iliakan/detect-node">https://github.com/iliakan/detect-node</a></td>
          <td><a href="https://github.com/iliakan/detect-node">https://github.com/iliakan/detect-node</a></td>
          <td>Ilya Kantor</td>
          </tr>
          <tr>
          <td>electron-to-chromium</td>
          <td>1.3.739</td>
          <td>ISC</td>
          <td><a href="https://github.com/kilian/electron-to-chromium/">https://github.com/kilian/electron-to-chromium/</a></td>
          <td>Unknown</td>
          <td>Kilian Valkhof</td>
          </tr>
          <tr>
          <td>fastq</td>
          <td>1.11.0</td>
          <td>ISC</td>
          <td>git+<a href="https://github.com/mcollina/fastq.git">https://github.com/mcollina/fastq.git</a></td>
          <td><a href="https://github.com/mcollina/fastq#readme">https://github.com/mcollina/fastq#readme</a></td>
          <td>Matteo Collina</td>
          </tr>
          <tr>
          <td>figgy-pudding</td>
          <td>3.5.2</td>
          <td>ISC</td>
          <td><a href="https://github.com/npm/figgy-pudding">https://github.com/npm/figgy-pudding</a></td>
          <td>Unknown</td>
          <td>Kat Marchán</td>
          </tr>
          <tr>
          <td>flatted</td>
          <td>2.0.2</td>
          <td>ISC</td>
          <td>git+<a href="https://github.com/WebReflection/flatted.git">https://github.com/WebReflection/flatted.git</a></td>
          <td><a href="https://github.com/WebReflection/flatted#readme">https://github.com/WebReflection/flatted#readme</a></td>
          <td>Andrea Giammarchi</td>
          </tr>
          <tr>
          <td>fs-minipass</td>
          <td>2.1.0</td>
          <td>ISC</td>
          <td>git+<a href="https://github.com/npm/fs-minipass.git">https://github.com/npm/fs-minipass.git</a></td>
          <td><a href="https://github.com/npm/fs-minipass#readme">https://github.com/npm/fs-minipass#readme</a></td>
          <td>Isaac Z. Schlueter</td>
          </tr>
          <tr>
          <td>fs-write-stream-atomic</td>
          <td>1.0.10</td>
          <td>ISC</td>
          <td><a href="https://github.com/npm/fs-write-stream-atomic">https://github.com/npm/fs-write-stream-atomic</a></td>
          <td><a href="https://github.com/npm/fs-write-stream-atomic">https://github.com/npm/fs-write-stream-atomic</a></td>
          <td>Isaac Z. Schlueter</td>
          </tr>
          <tr>
          <td>fs.realpath</td>
          <td>1.0.0</td>
          <td>ISC</td>
          <td>git+<a href="https://github.com/isaacs/fs.realpath.git">https://github.com/isaacs/fs.realpath.git</a></td>
          <td><a href="http://blog.izs.me/">http://blog.izs.me/</a></td>
          <td>Isaac Z. Schlueter</td>
          </tr>
          <tr>
          <td>get-caller-file</td>
          <td>2.0.5</td>
          <td>ISC</td>
          <td>git+<a href="https://github.com/stefanpenner/get-caller-file.git">https://github.com/stefanpenner/get-caller-file.git</a></td>
          <td><a href="https://github.com/stefanpenner/get-caller-file#readme">https://github.com/stefanpenner/get-caller-file#readme</a></td>
          <td>Stefan Penner</td>
          </tr>
          <tr>
          <td>glob</td>
          <td>7.1.6</td>
          <td>ISC</td>
          <td>git://github.com/isaacs/node-glob.git</td>
          <td><a href="http://blog.izs.me/">http://blog.izs.me/</a></td>
          <td>Isaac Z. Schlueter</td>
          </tr>
          <tr>
          <td>glob-parent</td>
          <td>5.1.2</td>
          <td>ISC</td>
          <td><a href="https://github.com/gulpjs/glob-parent.git">https://github.com/gulpjs/glob-parent.git</a></td>
          <td><a href="https://gulpjs.com/">https://gulpjs.com/</a></td>
          <td>Gulp Team</td>
          </tr>
          <tr>
          <td>glob-parent</td>
          <td>5.1.1</td>
          <td>ISC</td>
          <td><a href="https://github.com/gulpjs/glob-parent.git">https://github.com/gulpjs/glob-parent.git</a></td>
          <td><a href="https://gulpjs.com/">https://gulpjs.com/</a></td>
          <td>Gulp Team</td>
          </tr>
          <tr>
          <td>glob-parent</td>
          <td>3.1.0</td>
          <td>ISC</td>
          <td><a href="https://github.com/es128/glob-parent">https://github.com/es128/glob-parent</a></td>
          <td><a href="https://github.com/es128/glob-parent">https://github.com/es128/glob-parent</a></td>
          <td>Elan Shanker</td>
          </tr>
          <tr>
          <td>graceful-fs</td>
          <td>4.2.6</td>
          <td>ISC</td>
          <td><a href="https://github.com/isaacs/node-graceful-fs">https://github.com/isaacs/node-graceful-fs</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>har-schema</td>
          <td>2.0.0</td>
          <td>ISC</td>
          <td><a href="https://github.com/ahmadnassri/har-schema.git">https://github.com/ahmadnassri/har-schema.git</a></td>
          <td><a href="https://github.com/ahmadnassri/har-schema">https://github.com/ahmadnassri/har-schema</a></td>
          <td>Ahmad Nassri</td>
          </tr>
          <tr>
          <td>hosted-git-info</td>
          <td>2.8.9</td>
          <td>ISC</td>
          <td>git+<a href="https://github.com/npm/hosted-git-info.git">https://github.com/npm/hosted-git-info.git</a></td>
          <td><a href="https://github.com/npm/hosted-git-info">https://github.com/npm/hosted-git-info</a></td>
          <td>Rebecca Turner</td>
          </tr>
          <tr>
          <td>icss-replace-symbols</td>
          <td>1.1.0</td>
          <td>ISC</td>
          <td>git+<a href="https://github.com/css-modules/icss-replace-symbols.git">https://github.com/css-modules/icss-replace-symbols.git</a></td>
          <td><a href="https://github.com/css-modules/icss-replace-symbols#readme">https://github.com/css-modules/icss-replace-symbols#readme</a></td>
          <td>Glen Maddern</td>
          </tr>
          <tr>
          <td>icss-utils</td>
          <td>4.1.1</td>
          <td>ISC</td>
          <td>git+<a href="https://github.com/css-modules/icss-utils.git">https://github.com/css-modules/icss-utils.git</a></td>
          <td><a href="https://github.com/css-modules/icss-utils#readme">https://github.com/css-modules/icss-utils#readme</a></td>
          <td>Glen Maddern</td>
          </tr>
          <tr>
          <td>ignore-by-default</td>
          <td>2.0.0</td>
          <td>ISC</td>
          <td>git+<a href="https://github.com/novemberborn/ignore-by-default.git">https://github.com/novemberborn/ignore-by-default.git</a></td>
          <td><a href="https://github.com/novemberborn/ignore-by-default#readme">https://github.com/novemberborn/ignore-by-default#readme</a></td>
          <td>Mark Wubben</td>
          </tr>
          <tr>
          <td>infer-owner</td>
          <td>1.0.4</td>
          <td>ISC</td>
          <td><a href="https://github.com/npm/infer-owner">https://github.com/npm/infer-owner</a></td>
          <td><a href="https://izs.me">https://izs.me</a></td>
          <td>Isaac Z. Schlueter</td>
          </tr>
          <tr>
          <td>inflight</td>
          <td>1.0.6</td>
          <td>ISC</td>
          <td><a href="https://github.com/npm/inflight.git">https://github.com/npm/inflight.git</a></td>
          <td><a href="https://github.com/isaacs/inflight">https://github.com/isaacs/inflight</a></td>
          <td>Isaac Z. Schlueter</td>
          </tr>
          <tr>
          <td>inherits</td>
          <td>2.0.4</td>
          <td>ISC</td>
          <td>git://github.com/isaacs/inherits</td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>inherits</td>
          <td>2.0.3</td>
          <td>ISC</td>
          <td>git://github.com/isaacs/inherits</td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>inherits</td>
          <td>2.0.1</td>
          <td>ISC</td>
          <td>git://github.com/isaacs/inherits</td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>ini</td>
          <td>1.3.8</td>
          <td>ISC</td>
          <td>git://github.com/isaacs/ini.git</td>
          <td><a href="http://blog.izs.me/">http://blog.izs.me/</a></td>
          <td>Isaac Z. Schlueter</td>
          </tr>
          <tr>
          <td>ini</td>
          <td>2.0.0</td>
          <td>ISC</td>
          <td>git://github.com/isaacs/ini.git</td>
          <td><a href="http://blog.izs.me/">http://blog.izs.me/</a></td>
          <td>Isaac Z. Schlueter</td>
          </tr>
          <tr>
          <td>is-resolvable</td>
          <td>1.1.0</td>
          <td>ISC</td>
          <td><a href="https://github.com/shinnn/is-resolvable.git">https://github.com/shinnn/is-resolvable.git</a></td>
          <td><a href="https://github.com/shinnn">https://github.com/shinnn</a></td>
          <td>Shinnosuke Watanabe</td>
          </tr>
          <tr>
          <td>isexe</td>
          <td>2.0.0</td>
          <td>ISC</td>
          <td>git+<a href="https://github.com/isaacs/isexe.git">https://github.com/isaacs/isexe.git</a></td>
          <td><a href="https://github.com/isaacs/isexe#readme">https://github.com/isaacs/isexe#readme</a></td>
          <td>Isaac Z. Schlueter</td>
          </tr>
          <tr>
          <td>json-stringify-safe</td>
          <td>5.0.1</td>
          <td>ISC</td>
          <td>git://github.com/isaacs/json-stringify-safe</td>
          <td><a href="https://github.com/isaacs/json-stringify-safe">https://github.com/isaacs/json-stringify-safe</a></td>
          <td>Isaac Z. Schlueter</td>
          </tr>
          <tr>
          <td>killable</td>
          <td>1.0.1</td>
          <td>ISC</td>
          <td><a href="https://github.com/marten-de-vries/killable.git">https://github.com/marten-de-vries/killable.git</a></td>
          <td>Unknown</td>
          <td>Marten de Vries</td>
          </tr>
          <tr>
          <td>lru-cache</td>
          <td>4.1.5</td>
          <td>ISC</td>
          <td>git://github.com/isaacs/node-lru-cache.git</td>
          <td>Unknown</td>
          <td>Isaac Z. Schlueter</td>
          </tr>
          <tr>
          <td>lru-cache</td>
          <td>5.1.1</td>
          <td>ISC</td>
          <td>git://github.com/isaacs/node-lru-cache.git</td>
          <td>Unknown</td>
          <td>Isaac Z. Schlueter</td>
          </tr>
          <tr>
          <td>lru-cache</td>
          <td>6.0.0</td>
          <td>ISC</td>
          <td>git://github.com/isaacs/node-lru-cache.git</td>
          <td>Unknown</td>
          <td>Isaac Z. Schlueter</td>
          </tr>
          <tr>
          <td>minimalistic-assert</td>
          <td>1.0.1</td>
          <td>ISC</td>
          <td><a href="https://github.com/calvinmetcalf/minimalistic-assert.git">https://github.com/calvinmetcalf/minimalistic-assert.git</a></td>
          <td><a href="https://github.com/calvinmetcalf/minimalistic-assert">https://github.com/calvinmetcalf/minimalistic-assert</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>minimatch</td>
          <td>3.0.4</td>
          <td>ISC</td>
          <td>git://github.com/isaacs/minimatch.git</td>
          <td><a href="http://blog.izs.me">http://blog.izs.me</a></td>
          <td>Isaac Z. Schlueter</td>
          </tr>
          <tr>
          <td>minipass</td>
          <td>3.1.3</td>
          <td>ISC</td>
          <td>git+<a href="https://github.com/isaacs/minipass.git">https://github.com/isaacs/minipass.git</a></td>
          <td><a href="http://blog.izs.me/">http://blog.izs.me/</a></td>
          <td>Isaac Z. Schlueter</td>
          </tr>
          <tr>
          <td>minipass-collect</td>
          <td>1.0.2</td>
          <td>ISC</td>
          <td>Unknown</td>
          <td><a href="https://izs.me">https://izs.me</a></td>
          <td>Isaac Z. Schlueter</td>
          </tr>
          <tr>
          <td>minipass-flush</td>
          <td>1.0.5</td>
          <td>ISC</td>
          <td>git+<a href="https://github.com/isaacs/minipass-flush.git">https://github.com/isaacs/minipass-flush.git</a></td>
          <td><a href="https://izs.me">https://izs.me</a></td>
          <td>Isaac Z. Schlueter</td>
          </tr>
          <tr>
          <td>minipass-pipeline</td>
          <td>1.2.4</td>
          <td>ISC</td>
          <td>Unknown</td>
          <td><a href="https://izs.me">https://izs.me</a></td>
          <td>Isaac Z. Schlueter</td>
          </tr>
          <tr>
          <td>move-concurrently</td>
          <td>1.0.1</td>
          <td>ISC</td>
          <td>git+<a href="https://github.com/npm/move-concurrently.git">https://github.com/npm/move-concurrently.git</a></td>
          <td><a href="https://www.npmjs.com/package/move-concurrently">https://www.npmjs.com/package/move-concurrently</a></td>
          <td>Rebecca Turner</td>
          </tr>
          <tr>
          <td>mute-stream</td>
          <td>0.0.8</td>
          <td>ISC</td>
          <td>git://github.com/isaacs/mute-stream</td>
          <td><a href="http://blog.izs.me/">http://blog.izs.me/</a></td>
          <td>Isaac Z. Schlueter</td>
          </tr>
          <tr>
          <td>mute-stream</td>
          <td>0.0.7</td>
          <td>ISC</td>
          <td>git://github.com/isaacs/mute-stream</td>
          <td><a href="http://blog.izs.me/">http://blog.izs.me/</a></td>
          <td>Isaac Z. Schlueter</td>
          </tr>
          <tr>
          <td>nopt</td>
          <td>5.0.0</td>
          <td>ISC</td>
          <td><a href="https://github.com/npm/nopt.git">https://github.com/npm/nopt.git</a></td>
          <td><a href="http://blog.izs.me/">http://blog.izs.me/</a></td>
          <td>Isaac Z. Schlueter</td>
          </tr>
          <tr>
          <td>once</td>
          <td>1.4.0</td>
          <td>ISC</td>
          <td>git://github.com/isaacs/once</td>
          <td><a href="http://blog.izs.me/">http://blog.izs.me/</a></td>
          <td>Isaac Z. Schlueter</td>
          </tr>
          <tr>
          <td>parse-asn1</td>
          <td>5.1.6</td>
          <td>ISC</td>
          <td>git://github.com/crypto-browserify/parse-asn1.git</td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>postcss-modules-extract-imports</td>
          <td>2.0.0</td>
          <td>ISC</td>
          <td><a href="https://github.com/css-modules/postcss-modules-extract-imports.git">https://github.com/css-modules/postcss-modules-extract-imports.git</a></td>
          <td><a href="https://github.com/css-modules/postcss-modules-extract-imports">https://github.com/css-modules/postcss-modules-extract-imports</a></td>
          <td>Glen Maddern</td>
          </tr>
          <tr>
          <td>postcss-modules-scope</td>
          <td>2.2.0</td>
          <td>ISC</td>
          <td><a href="https://github.com/css-modules/postcss-modules-scope.git">https://github.com/css-modules/postcss-modules-scope.git</a></td>
          <td><a href="https://github.com/css-modules/postcss-modules-scope">https://github.com/css-modules/postcss-modules-scope</a></td>
          <td>Glen Maddern</td>
          </tr>
          <tr>
          <td>postcss-modules-scope</td>
          <td>1.1.0</td>
          <td>ISC</td>
          <td><a href="https://github.com/css-modules/postcss-modules-scope.git">https://github.com/css-modules/postcss-modules-scope.git</a></td>
          <td><a href="https://github.com/css-modules/postcss-modules-scope">https://github.com/css-modules/postcss-modules-scope</a></td>
          <td>Glen Maddern</td>
          </tr>
          <tr>
          <td>postcss-modules-values</td>
          <td>3.0.0</td>
          <td>ISC</td>
          <td>git+<a href="https://github.com/css-modules/postcss-modules-values.git">https://github.com/css-modules/postcss-modules-values.git</a></td>
          <td><a href="https://github.com/css-modules/postcss-modules-values#readme">https://github.com/css-modules/postcss-modules-values#readme</a></td>
          <td>Glen Maddern</td>
          </tr>
          <tr>
          <td>promise-inflight</td>
          <td>1.0.1</td>
          <td>ISC</td>
          <td>git+<a href="https://github.com/iarna/promise-inflight.git">https://github.com/iarna/promise-inflight.git</a></td>
          <td><a href="https://github.com/iarna/promise-inflight#readme">https://github.com/iarna/promise-inflight#readme</a></td>
          <td>Rebecca Turner</td>
          </tr>
          <tr>
          <td>promise-limit</td>
          <td>2.7.0</td>
          <td>ISC</td>
          <td>git+<a href="https://github.com/featurist/promise-limit.git">https://github.com/featurist/promise-limit.git</a></td>
          <td><a href="https://github.com/featurist/promise-limit#readme">https://github.com/featurist/promise-limit#readme</a></td>
          <td>Tim Macfarlane</td>
          </tr>
          <tr>
          <td>proto-list</td>
          <td>1.2.4</td>
          <td>ISC</td>
          <td><a href="https://github.com/isaacs/proto-list">https://github.com/isaacs/proto-list</a></td>
          <td><a href="http://blog.izs.me/">http://blog.izs.me/</a></td>
          <td>Isaac Z. Schlueter</td>
          </tr>
          <tr>
          <td>pseudomap</td>
          <td>1.0.2</td>
          <td>ISC</td>
          <td>git+<a href="https://github.com/isaacs/pseudomap.git">https://github.com/isaacs/pseudomap.git</a></td>
          <td><a href="https://github.com/isaacs/pseudomap#readme">https://github.com/isaacs/pseudomap#readme</a></td>
          <td>Isaac Z. Schlueter</td>
          </tr>
          <tr>
          <td>remove-trailing-separator</td>
          <td>1.1.0</td>
          <td>ISC</td>
          <td>git+<a href="https://github.com/darsain/remove-trailing-separator.git">https://github.com/darsain/remove-trailing-separator.git</a></td>
          <td><a href="https://github.com/darsain/remove-trailing-separator#readme">https://github.com/darsain/remove-trailing-separator#readme</a></td>
          <td>darsain</td>
          </tr>
          <tr>
          <td>request-promise-core</td>
          <td>1.1.4</td>
          <td>ISC</td>
          <td>git+<a href="https://github.com/request/promise-core.git">https://github.com/request/promise-core.git</a></td>
          <td><a href="https://github.com/request/promise-core#readme">https://github.com/request/promise-core#readme</a></td>
          <td>Nicolai Kamenzky</td>
          </tr>
          <tr>
          <td>request-promise-native</td>
          <td>1.0.9</td>
          <td>ISC</td>
          <td>git+<a href="https://github.com/request/request-promise-native.git">https://github.com/request/request-promise-native.git</a></td>
          <td><a href="https://github.com/request/request-promise-native#readme">https://github.com/request/request-promise-native#readme</a></td>
          <td>Nicolai Kamenzky</td>
          </tr>
          <tr>
          <td>require-extension-hooks</td>
          <td>0.3.3</td>
          <td>ISC</td>
          <td>git+<a href="https://github.com/jackmellis/require-extension-hooks.git">https://github.com/jackmellis/require-extension-hooks.git</a></td>
          <td><a href="https://github.com/jackmellis/require-extension-hooks#readme">https://github.com/jackmellis/require-extension-hooks#readme</a></td>
          <td>Jack Ellis</td>
          </tr>
          <tr>
          <td>require-extension-hooks-babel</td>
          <td>1.0.0</td>
          <td>ISC</td>
          <td>git+<a href="https://github.com/jackmellis/require-extension-hooks-babel.git">https://github.com/jackmellis/require-extension-hooks-babel.git</a></td>
          <td><a href="https://github.com/jackmellis/require-extension-hooks-babel#readme">https://github.com/jackmellis/require-extension-hooks-babel#readme</a></td>
          <td>Jack Ellis</td>
          </tr>
          <tr>
          <td>require-extension-hooks-vue</td>
          <td>3.0.0</td>
          <td>ISC</td>
          <td>git+<a href="https://github.com/jackmellis/require-extension-hooks-vue.git">https://github.com/jackmellis/require-extension-hooks-vue.git</a></td>
          <td><a href="https://github.com/jackmellis/require-extension-hooks-vue#readme">https://github.com/jackmellis/require-extension-hooks-vue#readme</a></td>
          <td>Jack Ellis</td>
          </tr>
          <tr>
          <td>require-main-filename</td>
          <td>2.0.0</td>
          <td>ISC</td>
          <td>git+ssh://git@github.com/yargs/require-main-filename.git</td>
          <td><a href="https://github.com/yargs/require-main-filename#readme">https://github.com/yargs/require-main-filename#readme</a></td>
          <td>Ben Coe</td>
          </tr>
          <tr>
          <td>rimraf</td>
          <td>2.7.1</td>
          <td>ISC</td>
          <td>git://github.com/isaacs/rimraf.git</td>
          <td><a href="http://blog.izs.me/">http://blog.izs.me/</a></td>
          <td>Isaac Z. Schlueter</td>
          </tr>
          <tr>
          <td>rimraf</td>
          <td>3.0.2</td>
          <td>ISC</td>
          <td>git://github.com/isaacs/rimraf.git</td>
          <td><a href="http://blog.izs.me/">http://blog.izs.me/</a></td>
          <td>Isaac Z. Schlueter</td>
          </tr>
          <tr>
          <td>rimraf</td>
          <td>2.6.3</td>
          <td>ISC</td>
          <td>git://github.com/isaacs/rimraf.git</td>
          <td><a href="http://blog.izs.me/">http://blog.izs.me/</a></td>
          <td>Isaac Z. Schlueter</td>
          </tr>
          <tr>
          <td>run-queue</td>
          <td>1.0.3</td>
          <td>ISC</td>
          <td>git+<a href="https://github.com/iarna/run-queue.git">https://github.com/iarna/run-queue.git</a></td>
          <td><a href="https://npmjs.com/package/run-queue">https://npmjs.com/package/run-queue</a></td>
          <td>Rebecca Turner</td>
          </tr>
          <tr>
          <td>sax</td>
          <td>1.2.4</td>
          <td>ISC</td>
          <td>git://github.com/isaacs/sax-js.git</td>
          <td><a href="http://blog.izs.me/">http://blog.izs.me/</a></td>
          <td>Isaac Z. Schlueter</td>
          </tr>
          <tr>
          <td>saxes</td>
          <td>5.0.1</td>
          <td>ISC</td>
          <td><a href="https://github.com/lddubeau/saxes.git">https://github.com/lddubeau/saxes.git</a></td>
          <td>Unknown</td>
          <td>Louis-Dominique Dubeau</td>
          </tr>
          <tr>
          <td>semver</td>
          <td>5.7.1</td>
          <td>ISC</td>
          <td><a href="https://github.com/npm/node-semver">https://github.com/npm/node-semver</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>semver</td>
          <td>6.3.0</td>
          <td>ISC</td>
          <td><a href="https://github.com/npm/node-semver">https://github.com/npm/node-semver</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>semver</td>
          <td>7.0.0</td>
          <td>ISC</td>
          <td><a href="https://github.com/npm/node-semver">https://github.com/npm/node-semver</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>semver</td>
          <td>7.3.4</td>
          <td>ISC</td>
          <td><a href="https://github.com/npm/node-semver">https://github.com/npm/node-semver</a></td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>set-blocking</td>
          <td>2.0.0</td>
          <td>ISC</td>
          <td>git+<a href="https://github.com/yargs/set-blocking.git">https://github.com/yargs/set-blocking.git</a></td>
          <td><a href="https://github.com/yargs/set-blocking#readme">https://github.com/yargs/set-blocking#readme</a></td>
          <td>Ben Coe</td>
          </tr>
          <tr>
          <td>setprototypeof</td>
          <td>1.1.1</td>
          <td>ISC</td>
          <td><a href="https://github.com/wesleytodd/setprototypeof.git">https://github.com/wesleytodd/setprototypeof.git</a></td>
          <td><a href="https://github.com/wesleytodd/setprototypeof">https://github.com/wesleytodd/setprototypeof</a></td>
          <td>Wes Todd</td>
          </tr>
          <tr>
          <td>setprototypeof</td>
          <td>1.1.0</td>
          <td>ISC</td>
          <td><a href="https://github.com/wesleytodd/setprototypeof.git">https://github.com/wesleytodd/setprototypeof.git</a></td>
          <td><a href="https://github.com/wesleytodd/setprototypeof">https://github.com/wesleytodd/setprototypeof</a></td>
          <td>Wes Todd</td>
          </tr>
          <tr>
          <td>sigmund</td>
          <td>1.0.1</td>
          <td>ISC</td>
          <td>git://github.com/isaacs/sigmund</td>
          <td><a href="http://blog.izs.me/">http://blog.izs.me/</a></td>
          <td>Isaac Z. Schlueter</td>
          </tr>
          <tr>
          <td>signal-exit</td>
          <td>3.0.3</td>
          <td>ISC</td>
          <td><a href="https://github.com/tapjs/signal-exit.git">https://github.com/tapjs/signal-exit.git</a></td>
          <td><a href="https://github.com/tapjs/signal-exit">https://github.com/tapjs/signal-exit</a></td>
          <td>Ben Coe</td>
          </tr>
          <tr>
          <td>ssri</td>
          <td>7.1.1</td>
          <td>ISC</td>
          <td><a href="https://github.com/npm/ssri">https://github.com/npm/ssri</a></td>
          <td>Unknown</td>
          <td>Kat Marchán</td>
          </tr>
          <tr>
          <td>ssri</td>
          <td>6.0.2</td>
          <td>ISC</td>
          <td><a href="https://github.com/zkat/ssri">https://github.com/zkat/ssri</a></td>
          <td>Unknown</td>
          <td>Kat Marchán</td>
          </tr>
          <tr>
          <td>ssri</td>
          <td>7.1.0</td>
          <td>ISC</td>
          <td><a href="https://github.com/npm/ssri">https://github.com/npm/ssri</a></td>
          <td>Unknown</td>
          <td>Kat Marchán</td>
          </tr>
          <tr>
          <td>stealthy-require</td>
          <td>1.1.1</td>
          <td>ISC</td>
          <td>git+<a href="https://github.com/analog-nico/stealthy-require.git">https://github.com/analog-nico/stealthy-require.git</a></td>
          <td><a href="https://github.com/analog-nico/stealthy-require#readme">https://github.com/analog-nico/stealthy-require#readme</a></td>
          <td>Nicolai Kamenzky</td>
          </tr>
          <tr>
          <td>unique-filename</td>
          <td>1.1.1</td>
          <td>ISC</td>
          <td><a href="https://github.com/iarna/unique-filename.git">https://github.com/iarna/unique-filename.git</a></td>
          <td><a href="https://github.com/iarna/unique-filename">https://github.com/iarna/unique-filename</a></td>
          <td>Rebecca Turner</td>
          </tr>
          <tr>
          <td>unique-slug</td>
          <td>2.0.2</td>
          <td>ISC</td>
          <td>git://github.com/iarna/unique-slug.git</td>
          <td><a href="http://re-becca.org">http://re-becca.org</a></td>
          <td>Rebecca Turner</td>
          </tr>
          <tr>
          <td>well-known-symbols</td>
          <td>2.0.0</td>
          <td>ISC</td>
          <td>git+<a href="https://github.com/novemberborn/well-known-symbols.git">https://github.com/novemberborn/well-known-symbols.git</a></td>
          <td><a href="https://github.com/novemberborn/well-known-symbols#readme">https://github.com/novemberborn/well-known-symbols#readme</a></td>
          <td>Mark Wubben</td>
          </tr>
          <tr>
          <td>which</td>
          <td>1.3.1</td>
          <td>ISC</td>
          <td>git://github.com/isaacs/node-which.git</td>
          <td><a href="http://blog.izs.me">http://blog.izs.me</a></td>
          <td>Isaac Z. Schlueter</td>
          </tr>
          <tr>
          <td>which</td>
          <td>2.0.2</td>
          <td>ISC</td>
          <td>git://github.com/isaacs/node-which.git</td>
          <td><a href="http://blog.izs.me">http://blog.izs.me</a></td>
          <td>Isaac Z. Schlueter</td>
          </tr>
          <tr>
          <td>which-module</td>
          <td>2.0.0</td>
          <td>ISC</td>
          <td>git+<a href="https://github.com/nexdrew/which-module.git">https://github.com/nexdrew/which-module.git</a></td>
          <td><a href="https://github.com/nexdrew/which-module#readme">https://github.com/nexdrew/which-module#readme</a></td>
          <td>nexdrew</td>
          </tr>
          <tr>
          <td>wrappy</td>
          <td>1.0.2</td>
          <td>ISC</td>
          <td><a href="https://github.com/npm/wrappy">https://github.com/npm/wrappy</a></td>
          <td><a href="https://github.com/npm/wrappy">https://github.com/npm/wrappy</a></td>
          <td>Isaac Z. Schlueter</td>
          </tr>
          <tr>
          <td>write-file-atomic</td>
          <td>3.0.3</td>
          <td>ISC</td>
          <td>git://github.com/npm/write-file-atomic.git</td>
          <td><a href="https://github.com/npm/write-file-atomic">https://github.com/npm/write-file-atomic</a></td>
          <td>Rebecca Turner</td>
          </tr>
          <tr>
          <td>y18n</td>
          <td>4.0.1</td>
          <td>ISC</td>
          <td>git@github.com:yargs/y18n.git</td>
          <td><a href="https://github.com/yargs/y18n">https://github.com/yargs/y18n</a></td>
          <td>Ben Coe</td>
          </tr>
          <tr>
          <td>y18n</td>
          <td>5.0.5</td>
          <td>ISC</td>
          <td><a href="https://github.com/yargs/y18n.git">https://github.com/yargs/y18n.git</a></td>
          <td><a href="https://github.com/yargs/y18n">https://github.com/yargs/y18n</a></td>
          <td>Ben Coe</td>
          </tr>
          <tr>
          <td>yallist</td>
          <td>2.1.2</td>
          <td>ISC</td>
          <td>git+<a href="https://github.com/isaacs/yallist.git">https://github.com/isaacs/yallist.git</a></td>
          <td><a href="http://blog.izs.me/">http://blog.izs.me/</a></td>
          <td>Isaac Z. Schlueter</td>
          </tr>
          <tr>
          <td>yallist</td>
          <td>4.0.0</td>
          <td>ISC</td>
          <td>git+<a href="https://github.com/isaacs/yallist.git">https://github.com/isaacs/yallist.git</a></td>
          <td><a href="http://blog.izs.me/">http://blog.izs.me/</a></td>
          <td>Isaac Z. Schlueter</td>
          </tr>
          <tr>
          <td>yallist</td>
          <td>3.1.1</td>
          <td>ISC</td>
          <td>git+<a href="https://github.com/isaacs/yallist.git">https://github.com/isaacs/yallist.git</a></td>
          <td><a href="http://blog.izs.me/">http://blog.izs.me/</a></td>
          <td>Isaac Z. Schlueter</td>
          </tr>
          <tr>
          <td>yargs-parser</td>
          <td>20.2.6</td>
          <td>ISC</td>
          <td><a href="https://github.com/yargs/yargs-parser.git">https://github.com/yargs/yargs-parser.git</a></td>
          <td>Unknown</td>
          <td>Ben Coe</td>
          </tr>
          <tr>
          <td>yargs-parser</td>
          <td>13.1.2</td>
          <td>ISC</td>
          <td>git@github.com:yargs/yargs-parser.git</td>
          <td>Unknown</td>
          <td>Ben Coe</td>
          </tr>
          <tr>
          <td>@hapi/address</td>
          <td>2.1.4</td>
          <td>BSD-3-Clause</td>
          <td>git://github.com/hapijs/address</td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@hapi/bourne</td>
          <td>1.3.2</td>
          <td>BSD-3-Clause</td>
          <td>git://github.com/hapijs/bourne</td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@hapi/hoek</td>
          <td>8.5.1</td>
          <td>BSD-3-Clause</td>
          <td>git://github.com/hapijs/hoek</td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@hapi/joi</td>
          <td>15.1.1</td>
          <td>BSD-3-Clause</td>
          <td>git://github.com/hapijs/joi</td>
          <td><a href="https://github.com/hapijs/joi">https://github.com/hapijs/joi</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@hapi/topo</td>
          <td>3.1.6</td>
          <td>BSD-3-Clause</td>
          <td>git://github.com/hapijs/topo</td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>@mapbox/sphericalmercator</td>
          <td>1.1.0</td>
          <td>BSD-3-Clause</td>
          <td>git://github.com/mapbox/node-sphericalmercator.git</td>
          <td><a href="http://mapbox.com/">http://mapbox.com/</a></td>
          <td>MapBox</td>
          </tr>
          <tr>
          <td>@xtuc/ieee754</td>
          <td>1.2.0</td>
          <td>BSD-3-Clause</td>
          <td>git://github.com/feross/ieee754.git</td>
          <td><a href="http://feross.org">http://feross.org</a></td>
          <td>Feross Aboukhadijeh</td>
          </tr>
          <tr>
          <td>abab</td>
          <td>2.0.5</td>
          <td>BSD-3-Clause</td>
          <td>git+<a href="https://github.com/jsdom/abab.git">https://github.com/jsdom/abab.git</a></td>
          <td><a href="https://github.com/jsdom/abab#readme">https://github.com/jsdom/abab#readme</a></td>
          <td>Jeff Carpenter</td>
          </tr>
          <tr>
          <td>bcrypt-pbkdf</td>
          <td>1.0.2</td>
          <td>BSD-3-Clause</td>
          <td>git://github.com/joyent/node-bcrypt-pbkdf.git</td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>duplexer3</td>
          <td>0.1.4</td>
          <td>BSD-3-Clause</td>
          <td><a href="https://github.com/floatdrop/duplexer3.git">https://github.com/floatdrop/duplexer3.git</a></td>
          <td><a href="http://www.fknsrs.biz/">http://www.fknsrs.biz/</a></td>
          <td>Conrad Pankoff</td>
          </tr>
          <tr>
          <td>esquery</td>
          <td>1.4.0</td>
          <td>BSD-3-Clause</td>
          <td><a href="https://github.com/estools/esquery.git">https://github.com/estools/esquery.git</a></td>
          <td><a href="https://github.com/estools/esquery/">https://github.com/estools/esquery/</a></td>
          <td>Joel Feenstra</td>
          </tr>
          <tr>
          <td>filesize</td>
          <td>3.6.1</td>
          <td>BSD-3-Clause</td>
          <td>git://github.com/avoidwork/filesize.js.git</td>
          <td><a href="https://filesizejs.com/">https://filesizejs.com/</a></td>
          <td>Jason Mulligan</td>
          </tr>
          <tr>
          <td>highlight.js</td>
          <td>10.4.1</td>
          <td>BSD-3-Clause</td>
          <td>git://github.com/highlightjs/highlight.js.git</td>
          <td><a href="https://highlightjs.org/">https://highlightjs.org/</a></td>
          <td>Ivan Sagalaev</td>
          </tr>
          <tr>
          <td>highlight.js</td>
          <td>10.6.0</td>
          <td>BSD-3-Clause</td>
          <td>git://github.com/highlightjs/highlight.js.git</td>
          <td><a href="https://highlightjs.org/">https://highlightjs.org/</a></td>
          <td>Ivan Sagalaev</td>
          </tr>
          <tr>
          <td>ieee754</td>
          <td>1.2.1</td>
          <td>BSD-3-Clause</td>
          <td>git://github.com/feross/ieee754.git</td>
          <td><a href="https://feross.org">https://feross.org</a></td>
          <td>Feross Aboukhadijeh</td>
          </tr>
          <tr>
          <td>js-base64</td>
          <td>2.6.4</td>
          <td>BSD-3-Clause</td>
          <td>git://github.com/dankogai/js-base64.git</td>
          <td>Unknown</td>
          <td>Dan Kogai</td>
          </tr>
          <tr>
          <td>mapbox.js</td>
          <td>3.3.1</td>
          <td>BSD-3-Clause</td>
          <td>git://github.com/mapbox/mapbox.js.git</td>
          <td><a href="http://mapbox.com/">http://mapbox.com/</a></td>
          <td>Mapbox</td>
          </tr>
          <tr>
          <td>qs</td>
          <td>6.7.0</td>
          <td>BSD-3-Clause</td>
          <td><a href="https://github.com/ljharb/qs.git">https://github.com/ljharb/qs.git</a></td>
          <td><a href="https://github.com/ljharb/qs">https://github.com/ljharb/qs</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>qs</td>
          <td>6.5.2</td>
          <td>BSD-3-Clause</td>
          <td><a href="https://github.com/ljharb/qs.git">https://github.com/ljharb/qs.git</a></td>
          <td><a href="https://github.com/ljharb/qs">https://github.com/ljharb/qs</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>serialize-javascript</td>
          <td>4.0.0</td>
          <td>BSD-3-Clause</td>
          <td>git+<a href="https://github.com/yahoo/serialize-javascript.git">https://github.com/yahoo/serialize-javascript.git</a></td>
          <td><a href="https://github.com/yahoo/serialize-javascript">https://github.com/yahoo/serialize-javascript</a></td>
          <td>Eric Ferraiuolo</td>
          </tr>
          <tr>
          <td>shelljs</td>
          <td>0.8.4</td>
          <td>BSD-3-Clause</td>
          <td>git://github.com/shelljs/shelljs.git</td>
          <td><a href="http://github.com/shelljs/shelljs">http://github.com/shelljs/shelljs</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>source-map</td>
          <td>0.6.1</td>
          <td>BSD-3-Clause</td>
          <td><a href="http://github.com/mozilla/source-map.git">http://github.com/mozilla/source-map.git</a></td>
          <td><a href="https://github.com/mozilla/source-map">https://github.com/mozilla/source-map</a></td>
          <td>Nick Fitzgerald</td>
          </tr>
          <tr>
          <td>source-map</td>
          <td>0.5.7</td>
          <td>BSD-3-Clause</td>
          <td><a href="http://github.com/mozilla/source-map.git">http://github.com/mozilla/source-map.git</a></td>
          <td><a href="https://github.com/mozilla/source-map">https://github.com/mozilla/source-map</a></td>
          <td>Nick Fitzgerald</td>
          </tr>
          <tr>
          <td>source-map</td>
          <td>0.7.3</td>
          <td>BSD-3-Clause</td>
          <td><a href="http://github.com/mozilla/source-map.git">http://github.com/mozilla/source-map.git</a></td>
          <td><a href="https://github.com/mozilla/source-map">https://github.com/mozilla/source-map</a></td>
          <td>Nick Fitzgerald</td>
          </tr>
          <tr>
          <td>sprintf-js</td>
          <td>1.0.3</td>
          <td>BSD-3-Clause</td>
          <td><a href="https://github.com/alexei/sprintf.js.git">https://github.com/alexei/sprintf.js.git</a></td>
          <td><a href="http://alexei.ro/">http://alexei.ro/</a></td>
          <td>Alexandru Marasteanu</td>
          </tr>
          <tr>
          <td>table</td>
          <td>5.4.6</td>
          <td>BSD-3-Clause</td>
          <td><a href="https://github.com/gajus/table">https://github.com/gajus/table</a></td>
          <td><a href="http://gajus.com">http://gajus.com</a></td>
          <td>Gajus Kuizinas</td>
          </tr>
          <tr>
          <td>tough-cookie</td>
          <td>2.5.0</td>
          <td>BSD-3-Clause</td>
          <td>git://github.com/salesforce/tough-cookie.git</td>
          <td><a href="https://github.com/salesforce/tough-cookie">https://github.com/salesforce/tough-cookie</a></td>
          <td>Jeremy Stashewsky</td>
          </tr>
          <tr>
          <td>tough-cookie</td>
          <td>3.0.1</td>
          <td>BSD-3-Clause</td>
          <td>git://github.com/salesforce/tough-cookie.git</td>
          <td><a href="https://github.com/salesforce/tough-cookie">https://github.com/salesforce/tough-cookie</a></td>
          <td>Jeremy Stashewsky</td>
          </tr>
          <tr>
          <td>@mapbox/corslite</td>
          <td>0.0.7</td>
          <td>BSD</td>
          <td>git://github.com/mapbox/corslite.git</td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>glob-to-regexp</td>
          <td>0.3.0</td>
          <td>BSD</td>
          <td><a href="https://github.com/fitzgen/glob-to-regexp.git">https://github.com/fitzgen/glob-to-regexp.git</a></td>
          <td>Unknown</td>
          <td>Nick Fitzgerald</td>
          </tr>
          <tr>
          <td>@mapbox/geo-viewport</td>
          <td>0.4.1</td>
          <td>BSD-2-Clause</td>
          <td>git@github.com:mapbox/geo-viewport.git</td>
          <td><a href="https://github.com/mapbox/geo-viewport">https://github.com/mapbox/geo-viewport</a></td>
          <td>Tom MacWright</td>
          </tr>
          <tr>
          <td>@mapbox/sanitize-caja</td>
          <td>0.1.4</td>
          <td>BSD-2-Clause</td>
          <td>git://github.com/mapbox/sanitize-caja.git</td>
          <td>Unknown</td>
          <td>Tom MacWright</td>
          </tr>
          <tr>
          <td>browser-process-hrtime</td>
          <td>1.0.0</td>
          <td>BSD-2-Clause</td>
          <td>git://github.com/kumavis/browser-process-hrtime.git</td>
          <td>Unknown</td>
          <td>kumavis</td>
          </tr>
          <tr>
          <td>configstore</td>
          <td>5.0.1</td>
          <td>BSD-2-Clause</td>
          <td><a href="https://github.com/yeoman/configstore.git">https://github.com/yeoman/configstore.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>css-select</td>
          <td>2.1.0</td>
          <td>BSD-2-Clause</td>
          <td>git://github.com/fb55/css-select.git</td>
          <td>Unknown</td>
          <td>Felix Boehm</td>
          </tr>
          <tr>
          <td>css-what</td>
          <td>3.4.2</td>
          <td>BSD-2-Clause</td>
          <td><a href="https://github.com/fb55/css-what">https://github.com/fb55/css-what</a></td>
          <td><a href="http://feedic.com">http://feedic.com</a></td>
          <td>Felix Böhm</td>
          </tr>
          <tr>
          <td>default-gateway</td>
          <td>5.0.5</td>
          <td>BSD-2-Clause</td>
          <td><a href="https://github.com/silverwind/default-gateway.git">https://github.com/silverwind/default-gateway.git</a></td>
          <td>Unknown</td>
          <td>silverwind</td>
          </tr>
          <tr>
          <td>default-gateway</td>
          <td>4.2.0</td>
          <td>BSD-2-Clause</td>
          <td><a href="https://github.com/silverwind/default-gateway.git">https://github.com/silverwind/default-gateway.git</a></td>
          <td>Unknown</td>
          <td>silverwind</td>
          </tr>
          <tr>
          <td>doctrine</td>
          <td>1.5.0</td>
          <td>BSD-2-Clause</td>
          <td><a href="https://github.com/eslint/doctrine.git">https://github.com/eslint/doctrine.git</a></td>
          <td><a href="https://github.com/eslint/doctrine">https://github.com/eslint/doctrine</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>domelementtype</td>
          <td>1.3.1</td>
          <td>BSD-2-Clause</td>
          <td>git://github.com/fb55/domelementtype.git</td>
          <td>Unknown</td>
          <td>Felix Boehm</td>
          </tr>
          <tr>
          <td>domelementtype</td>
          <td>2.1.0</td>
          <td>BSD-2-Clause</td>
          <td>git://github.com/fb55/domelementtype.git</td>
          <td>Unknown</td>
          <td>Felix Boehm</td>
          </tr>
          <tr>
          <td>domhandler</td>
          <td>2.4.2</td>
          <td>BSD-2-Clause</td>
          <td>git://github.com/fb55/DomHandler.git</td>
          <td>Unknown</td>
          <td>Felix Boehm</td>
          </tr>
          <tr>
          <td>domutils</td>
          <td>1.7.0</td>
          <td>BSD-2-Clause</td>
          <td>git://github.com/FB55/domutils.git</td>
          <td>Unknown</td>
          <td>Felix Boehm</td>
          </tr>
          <tr>
          <td>dotenv</td>
          <td>8.2.0</td>
          <td>BSD-2-Clause</td>
          <td>git://github.com/motdotla/dotenv.git</td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>dotenv-expand</td>
          <td>5.1.0</td>
          <td>BSD-2-Clause</td>
          <td>Unknown</td>
          <td>Unknown</td>
          <td>motdotla</td>
          </tr>
          <tr>
          <td>entities</td>
          <td>1.1.2</td>
          <td>BSD-2-Clause</td>
          <td>git://github.com/fb55/entities.git</td>
          <td>Unknown</td>
          <td>Felix Boehm</td>
          </tr>
          <tr>
          <td>entities</td>
          <td>2.2.0</td>
          <td>BSD-2-Clause</td>
          <td>git://github.com/fb55/entities.git</td>
          <td>Unknown</td>
          <td>Felix Boehm</td>
          </tr>
          <tr>
          <td>escodegen</td>
          <td>1.14.3</td>
          <td>BSD-2-Clause</td>
          <td><a href="http://github.com/estools/escodegen.git">http://github.com/estools/escodegen.git</a></td>
          <td><a href="http://github.com/estools/escodegen">http://github.com/estools/escodegen</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>eslint-scope</td>
          <td>4.0.3</td>
          <td>BSD-2-Clause</td>
          <td><a href="https://github.com/eslint/eslint-scope.git">https://github.com/eslint/eslint-scope.git</a></td>
          <td><a href="http://github.com/eslint/eslint-scope">http://github.com/eslint/eslint-scope</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>espree</td>
          <td>5.0.1</td>
          <td>BSD-2-Clause</td>
          <td><a href="https://github.com/eslint/espree.git">https://github.com/eslint/espree.git</a></td>
          <td><a href="https://github.com/eslint/espree">https://github.com/eslint/espree</a></td>
          <td>Nicholas C. Zakas</td>
          </tr>
          <tr>
          <td>espree</td>
          <td>4.1.0</td>
          <td>BSD-2-Clause</td>
          <td><a href="https://github.com/eslint/espree.git">https://github.com/eslint/espree.git</a></td>
          <td><a href="https://github.com/eslint/espree">https://github.com/eslint/espree</a></td>
          <td>Nicholas C. Zakas</td>
          </tr>
          <tr>
          <td>esprima</td>
          <td>4.0.1</td>
          <td>BSD-2-Clause</td>
          <td><a href="https://github.com/jquery/esprima.git">https://github.com/jquery/esprima.git</a></td>
          <td><a href="http://esprima.org/">http://esprima.org/</a></td>
          <td>Ariya Hidayat</td>
          </tr>
          <tr>
          <td>esrecurse</td>
          <td>4.3.0</td>
          <td>BSD-2-Clause</td>
          <td><a href="https://github.com/estools/esrecurse.git">https://github.com/estools/esrecurse.git</a></td>
          <td><a href="https://github.com/estools/esrecurse">https://github.com/estools/esrecurse</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>estraverse</td>
          <td>4.3.0</td>
          <td>BSD-2-Clause</td>
          <td><a href="http://github.com/estools/estraverse.git">http://github.com/estools/estraverse.git</a></td>
          <td><a href="https://github.com/estools/estraverse">https://github.com/estools/estraverse</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>estraverse</td>
          <td>5.2.0</td>
          <td>BSD-2-Clause</td>
          <td><a href="http://github.com/estools/estraverse.git">http://github.com/estools/estraverse.git</a></td>
          <td><a href="https://github.com/estools/estraverse">https://github.com/estools/estraverse</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>esutils</td>
          <td>2.0.3</td>
          <td>BSD-2-Clause</td>
          <td><a href="http://github.com/estools/esutils.git">http://github.com/estools/esutils.git</a></td>
          <td><a href="https://github.com/estools/esutils">https://github.com/estools/esutils</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>extract-zip</td>
          <td>1.7.0</td>
          <td>BSD-2-Clause</td>
          <td><a href="https://github.com/maxogden/extract-zip.git">https://github.com/maxogden/extract-zip.git</a></td>
          <td>Unknown</td>
          <td>max ogden</td>
          </tr>
          <tr>
          <td>http-cache-semantics</td>
          <td>4.1.0</td>
          <td>BSD-2-Clause</td>
          <td><a href="https://github.com/kornelski/http-cache-semantics.git">https://github.com/kornelski/http-cache-semantics.git</a></td>
          <td><a href="https://kornel.ski/">https://kornel.ski/</a></td>
          <td>Kornel Lesiński</td>
          </tr>
          <tr>
          <td>leaflet</td>
          <td>1.4.0</td>
          <td>BSD-2-Clause</td>
          <td>git://github.com/Leaflet/Leaflet.git</td>
          <td>Unknown</td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>mississippi</td>
          <td>3.0.0</td>
          <td>BSD-2-Clause</td>
          <td>git+<a href="https://github.com/maxogden/mississippi.git">https://github.com/maxogden/mississippi.git</a></td>
          <td><a href="https://github.com/maxogden/mississippi#readme">https://github.com/maxogden/mississippi#readme</a></td>
          <td>max ogden</td>
          </tr>
          <tr>
          <td>normalize-package-data</td>
          <td>2.5.0</td>
          <td>BSD-2-Clause</td>
          <td>git://github.com/npm/normalize-package-data.git</td>
          <td>Unknown</td>
          <td>Meryn Stol</td>
          </tr>
          <tr>
          <td>nth-check</td>
          <td>1.0.2</td>
          <td>BSD-2-Clause</td>
          <td><a href="https://github.com/fb55/nth-check">https://github.com/fb55/nth-check</a></td>
          <td><a href="https://github.com/fb55/nth-check">https://github.com/fb55/nth-check</a></td>
          <td>Felix Boehm</td>
          </tr>
          <tr>
          <td>regjsparser</td>
          <td>0.6.7</td>
          <td>BSD-2-Clause</td>
          <td>git@github.com:jviereck/regjsparser.git</td>
          <td><a href="https://github.com/jviereck/regjsparser">https://github.com/jviereck/regjsparser</a></td>
          <td>&#39;Julian Viereck&#39;</td>
          </tr>
          <tr>
          <td>terser</td>
          <td>4.8.0</td>
          <td>BSD-2-Clause</td>
          <td><a href="https://github.com/terser/terser">https://github.com/terser/terser</a></td>
          <td><a href="https://terser.org/">https://terser.org/</a></td>
          <td>Mihai Bazon</td>
          </tr>
          <tr>
          <td>uglify-js</td>
          <td>3.4.10</td>
          <td>BSD-2-Clause</td>
          <td><a href="https://github.com/mishoo/UglifyJS2.git">https://github.com/mishoo/UglifyJS2.git</a></td>
          <td><a href="http://lisperator.net/">http://lisperator.net/</a></td>
          <td>Mihai Bazon</td>
          </tr>
          <tr>
          <td>update-notifier</td>
          <td>5.1.0</td>
          <td>BSD-2-Clause</td>
          <td><a href="https://github.com/yeoman/update-notifier.git">https://github.com/yeoman/update-notifier.git</a></td>
          <td><a href="https://sindresorhus.com">https://sindresorhus.com</a></td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>uri-js</td>
          <td>4.4.1</td>
          <td>BSD-2-Clause</td>
          <td><a href="http://github.com/garycourt/uri-js">http://github.com/garycourt/uri-js</a></td>
          <td><a href="https://github.com/garycourt/uri-js">https://github.com/garycourt/uri-js</a></td>
          <td>Gary Court</td>
          </tr>
          <tr>
          <td>webidl-conversions</td>
          <td>6.1.0</td>
          <td>BSD-2-Clause</td>
          <td><a href="https://github.com/jsdom/webidl-conversions.git">https://github.com/jsdom/webidl-conversions.git</a></td>
          <td><a href="https://domenic.me/">https://domenic.me/</a></td>
          <td>Domenic Denicola</td>
          </tr>
          <tr>
          <td>webidl-conversions</td>
          <td>5.0.0</td>
          <td>BSD-2-Clause</td>
          <td><a href="https://github.com/jsdom/webidl-conversions.git">https://github.com/jsdom/webidl-conversions.git</a></td>
          <td><a href="https://domenic.me/">https://domenic.me/</a></td>
          <td>Domenic Denicola</td>
          </tr>
          <tr>
          <td>@vue/preload-webpack-plugin</td>
          <td>1.1.2</td>
          <td>Apache-2.0</td>
          <td><a href="https://github.com/vuejs/preload-webpack-plugin.git">https://github.com/vuejs/preload-webpack-plugin.git</a></td>
          <td><a href="https://github.com/vuejs/preload-webpack-plugin">https://github.com/vuejs/preload-webpack-plugin</a></td>
          <td>Addy Osmani</td>
          </tr>
          <tr>
          <td>@xtuc/long</td>
          <td>4.2.2</td>
          <td>Apache-2.0</td>
          <td><a href="https://github.com/dcodeIO/long.js.git">https://github.com/dcodeIO/long.js.git</a></td>
          <td>Unknown</td>
          <td>Daniel Wirtz</td>
          </tr>
          <tr>
          <td>ansi-html</td>
          <td>0.0.7</td>
          <td>Apache-2.0</td>
          <td>git://github.com/Tjatse/ansi-html.git</td>
          <td><a href="https://github.com/Tjatse/ansi-html">https://github.com/Tjatse/ansi-html</a></td>
          <td>Tjatse</td>
          </tr>
          <tr>
          <td>aws-sign2</td>
          <td>0.7.0</td>
          <td>Apache-2.0</td>
          <td><a href="https://github.com/mikeal/aws-sign">https://github.com/mikeal/aws-sign</a></td>
          <td><a href="http://www.futurealoof.com">http://www.futurealoof.com</a></td>
          <td>Mikeal Rogers</td>
          </tr>
          <tr>
          <td>caseless</td>
          <td>0.12.0</td>
          <td>Apache-2.0</td>
          <td><a href="https://github.com/mikeal/caseless">https://github.com/mikeal/caseless</a></td>
          <td>Unknown</td>
          <td>Mikeal Rogers</td>
          </tr>
          <tr>
          <td>doctrine</td>
          <td>3.0.0</td>
          <td>Apache-2.0</td>
          <td><a href="https://github.com/eslint/doctrine.git">https://github.com/eslint/doctrine.git</a></td>
          <td><a href="https://github.com/eslint/doctrine">https://github.com/eslint/doctrine</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>ejs</td>
          <td>2.7.4</td>
          <td>Apache-2.0</td>
          <td>git://github.com/mde/ejs.git</td>
          <td><a href="https://github.com/mde/ejs">https://github.com/mde/ejs</a></td>
          <td>Matthew Eernisse</td>
          </tr>
          <tr>
          <td>eslint-visitor-keys</td>
          <td>1.3.0</td>
          <td>Apache-2.0</td>
          <td><a href="https://github.com/eslint/eslint-visitor-keys.git">https://github.com/eslint/eslint-visitor-keys.git</a></td>
          <td><a href="https://github.com/eslint/eslint-visitor-keys#readme">https://github.com/eslint/eslint-visitor-keys#readme</a></td>
          <td>Toru Nagashima</td>
          </tr>
          <tr>
          <td>fast-diff</td>
          <td>1.2.0</td>
          <td>Apache-2.0</td>
          <td><a href="https://github.com/jhchen/fast-diff">https://github.com/jhchen/fast-diff</a></td>
          <td>Unknown</td>
          <td>Jason Chen</td>
          </tr>
          <tr>
          <td>faye-websocket</td>
          <td>0.11.3</td>
          <td>Apache-2.0</td>
          <td>git://github.com/faye/faye-websocket-node.git</td>
          <td><a href="https://github.com/faye/faye-websocket-node">https://github.com/faye/faye-websocket-node</a></td>
          <td>James Coglan</td>
          </tr>
          <tr>
          <td>forever-agent</td>
          <td>0.6.1</td>
          <td>Apache-2.0</td>
          <td><a href="https://github.com/mikeal/forever-agent">https://github.com/mikeal/forever-agent</a></td>
          <td><a href="http://www.futurealoof.com">http://www.futurealoof.com</a></td>
          <td>Mikeal Rogers</td>
          </tr>
          <tr>
          <td>human-signals</td>
          <td>1.1.1</td>
          <td>Apache-2.0</td>
          <td><a href="https://github.com/ehmicky/human-signals.git">https://github.com/ehmicky/human-signals.git</a></td>
          <td><a href="https://git.io/JeluP">https://git.io/JeluP</a></td>
          <td>ehmicky</td>
          </tr>
          <tr>
          <td>oauth-sign</td>
          <td>0.9.0</td>
          <td>Apache-2.0</td>
          <td><a href="https://github.com/mikeal/oauth-sign">https://github.com/mikeal/oauth-sign</a></td>
          <td><a href="http://www.futurealoof.com">http://www.futurealoof.com</a></td>
          <td>Mikeal Rogers</td>
          </tr>
          <tr>
          <td>puppeteer</td>
          <td>1.20.0</td>
          <td>Apache-2.0</td>
          <td><a href="https://github.com/GoogleChrome/puppeteer.git">https://github.com/GoogleChrome/puppeteer.git</a></td>
          <td>Unknown</td>
          <td>The Chromium Authors</td>
          </tr>
          <tr>
          <td>request</td>
          <td>2.88.2</td>
          <td>Apache-2.0</td>
          <td><a href="https://github.com/request/request.git">https://github.com/request/request.git</a></td>
          <td>Unknown</td>
          <td>Mikeal Rogers</td>
          </tr>
          <tr>
          <td>rxjs</td>
          <td>6.6.6</td>
          <td>Apache-2.0</td>
          <td><a href="https://github.com/reactivex/rxjs.git">https://github.com/reactivex/rxjs.git</a></td>
          <td><a href="https://github.com/ReactiveX/RxJS">https://github.com/ReactiveX/RxJS</a></td>
          <td>Ben Lesh</td>
          </tr>
          <tr>
          <td>spdx-correct</td>
          <td>3.1.1</td>
          <td>Apache-2.0</td>
          <td><a href="https://github.com/jslicense/spdx-correct.js.git">https://github.com/jslicense/spdx-correct.js.git</a></td>
          <td><a href="https://kemitchell.com">https://kemitchell.com</a></td>
          <td>Kyle E. Mitchell</td>
          </tr>
          <tr>
          <td>tunnel-agent</td>
          <td>0.6.0</td>
          <td>Apache-2.0</td>
          <td><a href="https://github.com/mikeal/tunnel-agent">https://github.com/mikeal/tunnel-agent</a></td>
          <td><a href="http://www.futurealoof.com">http://www.futurealoof.com</a></td>
          <td>Mikeal Rogers</td>
          </tr>
          <tr>
          <td>validate-npm-package-license</td>
          <td>3.0.4</td>
          <td>Apache-2.0</td>
          <td><a href="https://github.com/kemitchell/validate-npm-package-license.js.git">https://github.com/kemitchell/validate-npm-package-license.js.git</a></td>
          <td><a href="https://kemitchell.com">https://kemitchell.com</a></td>
          <td>Kyle E. Mitchell</td>
          </tr>
          <tr>
          <td>websocket-driver</td>
          <td>0.7.4</td>
          <td>Apache-2.0</td>
          <td>git://github.com/faye/websocket-driver-node.git</td>
          <td><a href="https://github.com/faye/websocket-driver-node">https://github.com/faye/websocket-driver-node</a></td>
          <td>James Coglan</td>
          </tr>
          <tr>
          <td>websocket-extensions</td>
          <td>0.1.4</td>
          <td>Apache-2.0</td>
          <td>git://github.com/faye/websocket-extensions-node.git</td>
          <td><a href="http://github.com/faye/websocket-extensions-node">http://github.com/faye/websocket-extensions-node</a></td>
          <td>James Coglan</td>
          </tr>
          <tr>
          <td>xml-name-validator</td>
          <td>3.0.0</td>
          <td>Apache-2.0</td>
          <td><a href="https://github.com/jsdom/xml-name-validator.git">https://github.com/jsdom/xml-name-validator.git</a></td>
          <td><a href="https://domenic.me/">https://domenic.me/</a></td>
          <td>Domenic Denicola</td>
          </tr>
          <tr>
          <td>atob</td>
          <td>2.1.2</td>
          <td>(MIT OR Apache-2.0)</td>
          <td>git://git.coolaj86.com/coolaj86/atob.js.git</td>
          <td><a href="https://git.coolaj86.com/coolaj86/atob.js.git">https://git.coolaj86.com/coolaj86/atob.js.git</a></td>
          <td>AJ ONeal</td>
          </tr>
          <tr>
          <td>callsite</td>
          <td>1.0.0</td>
          <td>MIT*</td>
          <td>Unknown</td>
          <td>Unknown</td>
          <td>TJ Holowaychuk</td>
          </tr>
          <tr>
          <td>caniuse-lite</td>
          <td>1.0.30001230</td>
          <td>CC-BY-4.0</td>
          <td><a href="https://github.com/browserslist/caniuse-lite.git">https://github.com/browserslist/caniuse-lite.git</a></td>
          <td><a href="http://beneb.info">http://beneb.info</a></td>
          <td>Ben Briggs</td>
          </tr>
          <tr>
          <td>event-pubsub</td>
          <td>4.3.0</td>
          <td>Unlicense</td>
          <td><a href="https://github.com/RIAEvangelist/event-pubsub.git">https://github.com/RIAEvangelist/event-pubsub.git</a></td>
          <td><a href="https://github.com/RIAEvangelist/event-pubsub">https://github.com/RIAEvangelist/event-pubsub</a></td>
          <td>Brandon Nozaki Miller</td>
          </tr>
          <tr>
          <td>tweetnacl</td>
          <td>0.14.5</td>
          <td>Unlicense</td>
          <td><a href="https://github.com/dchest/tweetnacl-js.git">https://github.com/dchest/tweetnacl-js.git</a></td>
          <td><a href="https://tweetnacl.js.org/">https://tweetnacl.js.org/</a></td>
          <td>TweetNaCl-js contributors</td>
          </tr>
          <tr>
          <td>json-schema</td>
          <td>0.2.3</td>
          <td>BSD*</td>
          <td><a href="http://github.com/kriszyp/json-schema">http://github.com/kriszyp/json-schema</a></td>
          <td>Unknown</td>
          <td>Kris Zyp</td>
          </tr>
          <tr>
          <td>mdn-data</td>
          <td>2.0.4</td>
          <td>CC0-1.0</td>
          <td><a href="https://github.com/mdn/data.git">https://github.com/mdn/data.git</a></td>
          <td><a href="https://developer.mozilla.org/">https://developer.mozilla.org/</a></td>
          <td>Mozilla Developer Network</td>
          </tr>
          <tr>
          <td>mdn-data</td>
          <td>2.0.14</td>
          <td>CC0-1.0</td>
          <td><a href="https://github.com/mdn/data.git">https://github.com/mdn/data.git</a></td>
          <td><a href="https://developer.mozilla.org/">https://developer.mozilla.org/</a></td>
          <td>Mozilla Developer Network</td>
          </tr>
          <tr>
          <td>spdx-license-ids</td>
          <td>3.0.7</td>
          <td>CC0-1.0</td>
          <td><a href="https://github.com/jslicense/spdx-license-ids.git">https://github.com/jslicense/spdx-license-ids.git</a></td>
          <td><a href="https://github.com/shinnn">https://github.com/shinnn</a></td>
          <td>Shinnosuke Watanabe</td>
          </tr>
          <tr>
          <td>string-hash</td>
          <td>1.1.3</td>
          <td>CC0-1.0</td>
          <td>git://github.com/darkskyapp/string-hash.git</td>
          <td>Unknown</td>
          <td>The Dark Sky Company</td>
          </tr>
          <tr>
          <td>node-forge</td>
          <td>0.10.0</td>
          <td>(BSD-3-Clause OR GPL-2.0)</td>
          <td><a href="https://github.com/digitalbazaar/forge">https://github.com/digitalbazaar/forge</a></td>
          <td><a href="https://github.com/digitalbazaar/forge">https://github.com/digitalbazaar/forge</a></td>
          <td>Digital Bazaar, Inc.</td>
          </tr>
          <tr>
          <td>opener</td>
          <td>1.5.2</td>
          <td>(WTFPL OR MIT)</td>
          <td><a href="https://github.com/domenic/opener.git">https://github.com/domenic/opener.git</a></td>
          <td><a href="https://domenic.me/">https://domenic.me/</a></td>
          <td>Domenic Denicola</td>
          </tr>
          <tr>
          <td>path-is-inside</td>
          <td>1.0.2</td>
          <td>(WTFPL OR MIT)</td>
          <td><a href="https://github.com/domenic/path-is-inside.git">https://github.com/domenic/path-is-inside.git</a></td>
          <td><a href="https://domenic.me">https://domenic.me</a></td>
          <td>Domenic Denicola</td>
          </tr>
          <tr>
          <td>pako</td>
          <td>1.0.11</td>
          <td>(MIT AND Zlib)</td>
          <td><a href="https://github.com/nodeca/pako.git">https://github.com/nodeca/pako.git</a></td>
          <td><a href="https://github.com/nodeca/pako">https://github.com/nodeca/pako</a></td>
          <td>Unknown</td>
          </tr>
          <tr>
          <td>rc</td>
          <td>1.2.8</td>
          <td>(BSD-2-Clause OR MIT OR Apache-2.0)</td>
          <td><a href="https://github.com/dominictarr/rc.git">https://github.com/dominictarr/rc.git</a></td>
          <td>dominictarr.com</td>
          <td>Dominic Tarr</td>
          </tr>
          <tr>
          <td>sha.js</td>
          <td>2.4.11</td>
          <td>(MIT AND BSD-3-Clause)</td>
          <td>git://github.com/crypto-browserify/sha.js.git</td>
          <td><a href="https://github.com/crypto-browserify/sha.js">https://github.com/crypto-browserify/sha.js</a></td>
          <td>Dominic Tarr</td>
          </tr>
          <tr>
          <td>spdx-exceptions</td>
          <td>2.3.0</td>
          <td>CC-BY-3.0</td>
          <td><a href="https://github.com/kemitchell/spdx-exceptions.json.git">https://github.com/kemitchell/spdx-exceptions.json.git</a></td>
          <td>Unknown</td>
          <td>The Linux Foundation</td>
          </tr>
          <tr>
          <td>tslib</td>
          <td>2.1.0</td>
          <td>0BSD</td>
          <td><a href="https://github.com/Microsoft/tslib.git">https://github.com/Microsoft/tslib.git</a></td>
          <td><a href="https://www.typescriptlang.org/">https://www.typescriptlang.org/</a></td>
          <td>Microsoft Corp.</td>
          </tr>
          <tr>
          <td>tslib</td>
          <td>1.14.1</td>
          <td>0BSD</td>
          <td><a href="https://github.com/Microsoft/tslib.git">https://github.com/Microsoft/tslib.git</a></td>
          <td><a href="https://www.typescriptlang.org/">https://www.typescriptlang.org/</a></td>
          <td>Microsoft Corp.</td>
          </tr>
          <tr>
          <td>type-fest</td>
          <td>0.6.0</td>
          <td>(MIT OR CC0-1.0)</td>
          <td><a href="https://github.com/sindresorhus/type-fest.git">https://github.com/sindresorhus/type-fest.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>type-fest</td>
          <td>0.11.0</td>
          <td>(MIT OR CC0-1.0)</td>
          <td><a href="https://github.com/sindresorhus/type-fest.git">https://github.com/sindresorhus/type-fest.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>type-fest</td>
          <td>0.3.1</td>
          <td>(MIT OR CC0-1.0)</td>
          <td><a href="https://github.com/sindresorhus/type-fest.git">https://github.com/sindresorhus/type-fest.git</a></td>
          <td>sindresorhus.com</td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>type-fest</td>
          <td>0.13.1</td>
          <td>(MIT OR CC0-1.0)</td>
          <td><a href="https://github.com/sindresorhus/type-fest.git">https://github.com/sindresorhus/type-fest.git</a></td>
          <td><a href="https://sindresorhus.com">https://sindresorhus.com</a></td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>type-fest</td>
          <td>0.20.2</td>
          <td>(MIT OR CC0-1.0)</td>
          <td><a href="https://github.com/sindresorhus/type-fest.git">https://github.com/sindresorhus/type-fest.git</a></td>
          <td><a href="https://sindresorhus.com">https://sindresorhus.com</a></td>
          <td>Sindre Sorhus</td>
          </tr>
          <tr>
          <td>webpack-chain</td>
          <td>6.5.1</td>
          <td>MPL-2.0</td>
          <td><a href="https://github.com/neutrinojs/webpack-chain.git">https://github.com/neutrinojs/webpack-chain.git</a></td>
          <td>Unknown</td>
          <td>Eli Perelman</td>
          </tr>
          </tbody>
          </table>
        </v-flex>
    </v-layout>
  </v-container>
</template>

<style scoped>
h3 {
  margin-bottom: 0.8em;
}

table {
  width: 100%;
  height: 70vh;
  overflow: scroll;
  display: block;
}
table td {
  white-space: nowrap;
}
table tr:hover {
  background: #EEE;
}
</style>
