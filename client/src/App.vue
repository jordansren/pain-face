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
            <!-- Always present -->
            <v-card class="elevation-12" style="width:500px">
              <h1 class="display-2" style="text-align: center;">AMGS Upload Tool </h1>
              <v-img class="mainImage center" src="./assets/Mouse.jpeg" alt="Mouse"></v-img>
            </v-card>
            <GirderAuth register style="width: 500px" v-if="stage == 1" />
            <upload v-if="stage == 2" :user="currentUserLogin" @uploaded="uploaded"></upload>
            <result v-if="stage == 3" @newUpload="newUpload"></result>
          </v-col>
        </v-row>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
  import { Authentication as GirderAuth } from '@girder/components/src/components';
  import upload from './components/upload.vue';
  import result from './components/result.vue';

  export default {
    inject: ['girderRest'],
    components: {
      GirderAuth,
      upload,
      result,
    },
    data() {
      return {
        imageUploaded: false,
        finishedProcessing: false,
        responseData: null
      }
    },
    computed: {
      stage() {
        console.log(this.girderRest);
        if (this.isLoggedOut) { return 1; } 
        else if (!this.imageUploaded && !this.finishedProcessing) { return 2; } 
        else { return 3; }
      }, 
      currentUserLogin() {
        return this.girderRest.user ? this.girderRest.user.login : 'anonymous';
      },
      isLoggedOut() {
        return this.girderRest.user == null;  
      }
    },
    methods: {
      newUpload() {
        this.imageUploaded = false;
        this.finishedProcessing = false;
      },
      uploaded(val) {
        this.imageUploaded = true;
        this.responseData = val;
      },
    },
  }
</script>
<style scoped src="@/assets/styles.css">
</style>
