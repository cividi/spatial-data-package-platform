<template>
  <div id="app">
    <header id="topbar">
      <router-link id="logo" to="/">
        <img alt="gemeindescan logo" height="50" src="@/assets/images/gemeindescan-logo.svg">
      </router-link>
      <nav id="mainnav">
        <router-link to="/about">Hintergrund</router-link>
        <router-link to="/imprint">Impressum</router-link>
        <router-link to="/contact">Kontakt</router-link>
      </nav>
      <div id="useractions" class="small">
        Login
        Kostenlos Account erstellen
      </div>
    </header>
    <main>
      <router-view/>
    </main>
  </div>
</template>

<style>
#app {
}
#topbar {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  padding: 1.2em 2.4em;
  border-bottom: 1px solid #e3e3e3;
}
#mainnav {
}

#mainnav a {
  font-weight: bold;
  color: #2c3e50;
  margin: 0 0.5em;
}

#mainnav a.router-link-exact-active {
  color: #42b983;
}
</style>
