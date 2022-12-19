<template>
  <v-app>
    <v-app-bar app>
      <v-toolbar-title>YATMoS</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn text to="/">Dashboard</v-btn>
      <v-btn text to="/projects">Projects</v-btn>
      <v-btn text to="/runs">Runs</v-btn>
    </v-app-bar>

    <v-main>
      <v-container fluid>
        <router-view/>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: "App",

  components: {},

  data: () => ({
    //
  }),
};
</script>
