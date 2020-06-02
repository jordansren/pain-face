<template>
  <v-app id="app">
    <v-content>
      <v-container
        class="fill-height"
        fluid
      >
        <v-row
          align="center"
          justify="center"
        >
          <v-col
            cols="12"
            sm="8"
            md="4"
          >
            <v-card class="elevation-12">
              <h1
                class="display-2"
                style="text-align: center;"
              >
                Pain Face
              </h1>
              <v-img
                class="mainImage center"
                src="./assets/pain-face.svg"
                alt="Mouse"
              />
            </v-card>
            <v-container grid-list-md />
            <router-view />
          </v-col>
        </v-row>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
export default {

};
</script>
<style scoped>
  .center {
    display: block;
    margin-left: auto;
    margin-right: auto;
  }

  .mainImage {
    padding: 5px;
    width: 150px;
    height: 150px;
  }
</style>
