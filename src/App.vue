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
            <v-card class="elevation-12 inputcard">
              <v-toolbar
                color="primary"
                dark
                flat
              >
                <v-toolbar-title>Accepted File Types: <br> jpg, png, jpeg, mp4</v-toolbar-title>
                <v-spacer></v-spacer>
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn rounded class="info" style="text-align: center" @click="onUpload" v-if="stage == 1">
                    <p style="top:20px">Upload File</p>
                  </v-btn>
                </v-card-actions> 
              </v-toolbar>
              <div v-if="stage == 1">
                <div class="area">
                  <v-img class="icon center" src="./assets/upload.png" alt="upload"></v-img>
                  <input id="upload" type="file" accept="image/jpeg,image/png,image/jpg,video/mp4" @change="onFileChosen">
                </div>
                <div>
                  <div class="preview" v-if="fileType=='image'">
                    <img class="preview imageStack" :src="imageData">
                  </div>
                  <video class="preview imageStack" :src="blobURL" v-if="fileType=='video'"></video>
                  <p style="text-align: center" v-if="wrongFileType">
                    Oops! You did not input an file of type png, jpeg, jpg, or mp4. <br> Current file to upload: {{ file.name }}
                  </p>
                </div>
              </div>
              <div v-else>
                <div class="clear center" v-if="stage == 2">
                  <h3 style="text-align:center">Processing {{ file.name }}...</h3>
                  <v-progress-linear
                    indeterminate
                    color="green"
                  ></v-progress-linear>
                </div>
              </div>
              <div v-if="stage == 3">
                <div v-if="fileType=='image'">
                  <img class="imageStack processedpreview center" :src="imageData">
                </div>
                <video class="imageStack processedpreview center" :src="blobURL" v-if="fileType=='video'"></video>
                <h1 v-if="fileType == 'image'" :img="outputImage">
                  Here is the data you want {{ img }}
                </h1>
                <h1 v-if="fileType == 'video'" :vid="outputVideo">
                  Here is the data you want {{ vid }}
                </h1>
                <v-btn rounded class="info center" @click="reset">
                  <p style="top:20px">Upload Another File</p>
                </v-btn>
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
        imageData: null,
        blobURL: null,
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
        if (!this.uploadingfile && !this.finishedUpload) {
          return 1;
        } else if (this.uploadingFile && !this.finishedUpload) {
          return 2;
        } else {
          return 3;
        }
      }
    },
    methods: {
      onFileChosen(event) {
        /* Loop over files, check for correct file types*/
        Array
          .from(Array(event.target.files.length).keys())
          .map(x => {
            let tag = event.target.files[x].name.split(".")[1];
            if (tag == "png" || tag == "jpeg" || tag == "jpg") {
              /* Since we are only doing single files for now, this if statement
                  will ensure only one file is stored at a time */
              if (this.file != null) {
                this.file = null;
                this.imageData = null;
              }
              this.showImage(event, x)
              this.wrongFileType = false;
              this.fileType = "image";
              this.file = event.target.files[x];
            } else if (tag == "mp4") {
              if (this.file != null) {
                this.file = null;
                this.blobURL = null;
              }
              this.wrongFileType = false;
              this.showVideo(event);
              this.fileType = "video";
              this.file = event.target.files[x];
            } else {
              this.wrongFileType = true;
            }
          });
      },
      async onUpload() {
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
  body{
    background-color: rgb(149, 214, 240);
  }


  img.preview {
    max-width: 400px;
    max-height: 200px;
    background-color: white;
    border: 1px solid #DDD;
    padding: 5px;
  }

  .mainImage {
    padding: 5px;
    width: 150px;
    height: 150px;
  }

  .imageStack {
    padding: 5px;
    display: block; 
    position: relative;
  }

  .clear {
    clear: both;
  }

  .center {
    display: inline-block;
    margin-left: auto;
    margin-right: auto;
  }

  .area {
    width: 100%;
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
    background-color: aqua;
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
    z-index: 1;
  }

  .area input:focus {
      outline: none;
  }

  .inputcard {
    width: 500px;
    height: 500px;
  }

  .preview {
    top: 200px;
    max-height: 200px;
    max-width: 400px; 
  }

  .processedpreview {
    max-height: 300px;
    max-width: 480px; 
  }

  .icon {
    top: 60px;
    width: 60px;
    height: 60px;
    z-index: 2;
  }
</style>
