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
            <v-card class="elevation-12" style="width:500px">
              <h1 class="display-2" style="text-align: center;">AMGS Upload Tool </h1>
              <v-img class="mainImage center" src="./assets/Mouse.jpeg" alt="Mouse"></v-img>
            </v-card>
            <v-container grid-list-md></v-container>
            <v-card class="elevation-12" v-bind:class="{
              inputcard: displayInputCard == 2, 
              smallinputcard: displayInputCard == 3,
              loadingCard: displayInputCard == 1}"
              style="max-width: 500px;">

              <!-- Tool Bar -->
              <v-toolbar color="primary" dark flat>
                <v-toolbar-title>Accepted File Types: <br> jpg, png, jpeg, mp4</v-toolbar-title>
                <v-spacer></v-spacer>
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn rounded class="info" @click="onUpload" v-if="stage == 1">
                    Upload File
                  </v-btn>
                  <v-btn rounded class="info" @click="reset" v-if="stage == 3">
                    Upload Another File
                  </v-btn>
                </v-card-actions> 
              </v-toolbar>

              <!-- Image Upload -->
              <div v-if="stage == 1">
                <div v-bind:class="{ area: true, withpreview: displayInputCard == 2}">
                  <input id="upload" type="file" accept="image/jpeg,image/png,image/jpg,video/mp4" @change="onFileChosen">
                  <v-img class="icon center" src="./assets/upload.png" alt="upload"></v-img>
                  <p style="position:relative; top:-140px; z-index: 2;">Click or Drag to Choose Files</p>
                </div>
                <div>
                  <p style="text-align: center" v-if="wrongFileType">
                    Oops! You did not input an file of type png, jpeg, jpg, or mp4. <br> Current file to upload: {{ file.name }}
                  </p>
                  <p style="text-align: center" v-else-if="fileType != null">
                    Preview:
                  </p>
                  <img :class="{preview: !wrongFileType, previewerror: wrongFileType}" :src="imageData" v-if="fileType=='image'">
                  <video :class="preview" :src="blobURL" v-if="fileType=='video'"></video>
                </div>
              </div>

              <!-- Uploading Image -->
              <div class="clear center" v-else-if="stage == 2">
                <h3 style="text-align:center">Processing {{ file.name }}...</h3>
                <v-progress-linear
                  indeterminate
                  color="green"
                ></v-progress-linear>
              </div>

              <!-- Return Processed Data -->
              <div v-if="stage == 3">
                <div v-if="fileType=='image'">
                  <img class="preview" :src="imageData">
                </div>
                <video class="preview" :src="blobURL" v-if="fileType=='video'"></video>
                <h1 v-if="fileType == 'image'" :img="outputImage" style="text-align: center;">
                  Mouse Face Pain Score: <br> {{ img }}
                </h1>
                <h1 v-if="fileType == 'video'" :vid="outputVideo" style="text-align: center">
                  Mouse Face Pain Score: <br> {{ vid }}
                </h1>
              </div>

            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
  export default {
    data() {
      return {
        file: null,
        imageData: "",
        blobURL: "",
        fileType: null,
        uploadingFile: false,
        finishedUpload: false,
        outputImage: null,
        outputVideo: null,
        wrongFileType: false
      }
    },
    computed: {
      stage() {
        if (!this.uploadingFile && !this.finishedUpload) {
          return 1;
        } else if (this.uploadingFile && !this.finishedUpload) {
          return 2;
        } else {
          return 3;
        }
      },
      displayInputCard() {
        if (this.uploadingFile && !this.finishedUpload) {
          return 1;
        }
        if (this.fileType!=null || this.wrongFileType) {
          return 2;
        } else {
          return 3;
        }
      } 
    },
    methods: {
      onFileChosen(event) {
        /* Loop over files, check for correct file types*/
        let tag = event.target.files[0].name.split(".")[1];
        if (tag == "png" || tag == "jpeg" || tag == "jpg") {
          /* Since we are only doing single files for now, this if statement
              will ensure only one file is stored at a time */
          if (this.file != null) {
            this.file = null;
            this.imageData = null;
          }
          this.showImage(event, 0)
          this.wrongFileType = false;
          this.fileType = "image";
          this.file = event.target.files[0];
        } else if (tag == "mp4") {
          if (this.file != null) {
            this.file = null;
            this.blobURL = null;
          }
          this.wrongFileType = false;
          this.showVideo(event);
          this.fileType = "video";
          this.file = event.target.files[0];
        } else {
          this.wrongFileType = true;  
        }
      },
      async onUpload() {
        if (this.file == null) {
          return;
        }
        this.uploadingFile = true;
/*         let tag = this.file.name.split(".")[1];
        const axios = require('axios');
        if (tag == "mp4") {
          const path = 'http://localhost:8080/vidUpload';
          this.outputImage = await axios.get(path);
        } else {
          const path = 'http://localhost:8080/imgUpload';
          this.outputVideo = await axios.get(path);
        } */
        this.finishedUpload = true;
        this.uploadingFile = false;
      },
      showImage(event) {
        var input = event.target;
        if (input.files && input.files[0]) {
          var reader = new FileReader();
          reader.onload = (e) => {
              this.imageData = e.target.result;
          }
          reader.readAsDataURL(input.files[0]);
        }
      },
      showVideo(event) {
        let file = event.target.files[0];
        this.blobURL = URL.createObjectURL(file);
      },
      reset() {
        this.file = null;
        this.imageData = null;
        this.blobURL = null;
        this.fileType = null;
        this.finishedUpload = false;
        this.uploadingFile = false;
        this.outputImage = null;
        this.outputVideo = null;
        this.wrongFileType = false;
      }
    }
  }
</script>

<style>
  .area {
    width: 500px;
    height: 200px;
    position: absolute;
    border: 4px dashed #000;
    background-position: center;
    background-repeat: no-repeat;
    background-size: 64px 64px;
    -webkit-box-sizing: border-box;
    -moz-box-sizing: border-box;
    box-sizing: border-box;
    filter: alpha(opacity=50);
    -khtml-opacity: 0.5;
    -moz-opacity: 0.5;
    opacity: 0.5;
    text-align: center;
    background-color: white;
  }

  .area:hover,
  .area.dragging,
  .area.uploading {
      filter: alpha(opacity=100);
      -khtml-opacity: 1;
      -moz-opacity: 1;
      opacity: 1;
  }

  .area input {
    width: 500px;  
    height: 200px;
    border: none;
    cursor: pointer;
    opacity: 0;
    z-index: 3;
  }

  .area input:focus {
      outline: none;
  }

  body{
    background-color: rgb(149, 214, 240);
  }

  .clear {
    clear: both;
  }

  .center {
    display: block;
    margin-left: auto;
    margin-right: auto;
  }

  .icon {
    top: -145px;
    width: 60px;
    height: 60px;
    z-index: 2;
  }

  .inputcard {
    width: 500px;
    height: 500px;
  }

  .loadingcard {
    width: 500px;
    height: 50px;
  }

  .mainImage {
    padding: 5px;
    width: 150px;
    height: 150px;
  }

  .preview {
    padding: 2px;
    display: block;
    margin-left: auto;
    margin-right: auto; 
    max-height: 190px;
    max-width: 400px; 
  }

  .previewerror {
    padding: 2px;
    display: block;
    margin-left: auto;
    margin-right: auto; 
    max-height: 150px;
    max-width: 400px;
  }

  .smallinputcard {
    width: 500px;
    height: 264px;
  }

  .withpreview {
    top: 300px;
  }

</style>
