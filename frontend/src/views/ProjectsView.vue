<template>
  <div class="projects">
    <v-card
      v-bind:key="project.title"
      v-for="project in projects"
      elevation="2"
      style="margin-bottom: 15px"
    >
      <v-card-title>
        {{ project.title }}
      </v-card-title>
      <v-card-subtitle>
        {{ project.desc }}
      </v-card-subtitle>
    </v-card>

    <v-dialog v-model="dialog" width="500">
      <template v-slot:activator="{ on, attrs }">
        <v-btn color="primary" absolute bottom right v-bind="attrs" v-on="on"
          ><v-icon>mdi-plus</v-icon></v-btn
        >
      </template>

      <v-card>
        <v-card-title class="text-h5 grey lighten-2">
          New Project
        </v-card-title>

        <v-card-text>
          <v-form ref="form" lazy-validation>
            <v-text-field
              v-model="name"
              label="Project name"
              required
            ></v-text-field>

            <v-text-field
              v-model="desc"
              label="Project Description"
            ></v-text-field>
          </v-form>
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary" text @click="createProject(name, desc)"> CREATE </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "ProjectsView",
  methods: {
    createProject: function (title, desc) {
      console.log(title, desc);
      this.dialog = false;
    },
  },
  data() {
    return {
      name: '',
      desc: null,
      dialog: false,
      projects: [],
    };
  },
  mounted() {
    axios
      .get("http://127.0.0.1:8000/projects/")
      .then((response) => (this.projects = response.data));
  },
};
</script>
