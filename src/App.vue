<template>
  <v-app id="app">
    <!-- Title -->
    <v-container>
      <v-layout row wrap>
        <v-flex xs6 md3>
          <h1 class="display-2">aMGS <br> Upload Tool </h1>
        </v-flex>
        <v-flex xs6 md9>
          <v-img class="mainImage center" src="./assets/Mouse.jpeg" alt="Mouse"></v-img>
        </v-flex>
      </v-layout>
      <v-divider></v-divider>
      <!-- Main Content and Uploader -->
      <v-layout row wrap>
        <!-- Drag and drop area -->
        <v-layout column>
          <v-flex xs6 md3 class="area">
            <label>
              <h3>Click or Drag to choose file</h3>
            </label>
            <v-img class="icon center" src="./assets/upload.png" alt="upload"></v-img>
            <input id="upload" type="file" accept="image/jpeg,image/png" @change="onImageChosen">
          </v-flex>
        </v-layout>
        <!-- Preview and upload -->
        <v-layout column>
          <v-flex xs6 md9>
            <p v-if="wrongImageType">
              Oops! You did not input an image of type png, jpeg, or jpg. <br> Current file to upload: {{ images[0].name }}
            </p>
            <v-btn class="primary" @click="onImageUpload" v-if="!uploadingImage">
              <p v-if="numberOfImages > 1">Upload Images</p>
              <p v-else>Upload Image</p>
            </v-btn>
          </v-flex>
          <v-flex xs6 md9>
            <div class="image-preview" v-if="imageData.length > 0">
              <div v-for="img in imageData" :key="img">
                <img class="preview imageStack" :src="img">
              </div>
            </div>
          </v-flex>
          <div class="clear" v-if="uploadingImage">
            <h3 v-if="numberOfImages > 1">Processing {{ images[0].name }}...</h3>
            <h3 v-else>Processing {{ images[0].name }}...</h3>
            <div class="loader"></div>
          </div>
        </v-layout>
      </v-layout>
    </v-container>
  
    <!-- Video Upload -->
    <!-- <form>
      <h3 >Videos</h3>
      <input type="file" accept="video/*" @change="onVideoChosen" v-if="!uploadingVideo"><br>
      <p v-if="wrongVideoType">
        Oops! You did not input an image of type png, jpeg, or jpg. <br> Current file to upload: {{ videos[0].name }}
      </p>
      <video style="width:300px" :src="blobURL" v-if="numberOfVideos > 0"></video>
      <button class="clear" @click="onVideoUpload" v-if="!uploadingVideo">
        <p v-if="numberOfVideos > 1">Upload Videos</p>
        <p v-else>Upload Video</p>
      </button>
      <div class="clear" v-if="uploadingVideo">
        <h3 v-if="numberOfVideos > 1">Processing {{ videos[0].name }}...</h3>
        <h3 v-else>Processing {{ videos[0].name }}...</h3>
        <div class="loader"></div>
      </div>
    </form> -->
  </v-app>
</template>

<script>
  export default {
    data() {
      return {
        images: [],
        videos: [],
        imageData: [],
        uploadingImage: false,
        uploadingVideo: false,
        outputImage: null,
        outputVideo: null,
        wrongImageType: false,
        wrongVideoType: false,
        blobURL: null
      }
    },
    computed: {
      numberOfImages() {
        return this.images.length;
      },
      numberOfVideos() {
        return this.videos.length;
      }
    },
    methods: {
      onImageChosen(event) {
        /* Loop over files, check for only images */
        Array
          .from(Array(event.target.files.length).keys())
          .map(x => {
            let tag = event.target.files[x].name.split(".")[1];
            if (tag == "png" || tag == "jpeg" || tag == "jpg") {
              /* Since we are only doing single files for now, this if statement
                  will ensure only one file is stored at a time */
              if (this.images.length == 1) {
                this.images = [];
                this.imageData = [];
                this.wrongImageType = false;
              }
              this.showImage(event, x)
              this.images.push(event.target.files[x]);
            } else {
              this.wrongImageType = true;
            }
          });
      },
      onVideoChosen(event) {
        /* Loop over files, check for only videos */
        Array
          .from(Array(event.target.files.length).keys())
          .map(x => {
            let tag = event.target.files[x].name.split(".")[1];
            if (tag == "mp4") {
              /* Since we are only doing single files for now, this if statement
                  will ensure only one file is stored at a time */
              if (this.videos.length == 1) {
                this.videos = [];
                this.videoData = [];
                this.wrongVideoType = false;
              } 
              this.showVideo(event);
              this.videos.push(event.target.files[x]);
            } else {
              this.wrongVideoType = true;
            }
          });
      },
      async onImageUpload() {
        this.uploadingImage = true;
        const axios = require('axios');
        const path = 'http://localhost:8080/'; /* Not sure what to put here */
        this.outputImage = await axios.get(path);
        /* this.uploadingImage = false; */
      },
      async onVideoUpload() {
        this.uploadingVideo = true;
        const axios = require('axios');
        const path = 'http://localhost:8080/'; /* Not sure what to put here */
        this.outputVideo = await axios.get(path);
        /* this.uploadingVideo = false; */
      },
      showImage(event, i) {
        var input = event.target;
        if (input.files && input.files[i]) {
          var reader = new FileReader();
          reader.onload = (e) => {
              this.imageData.push(e.target.result);
          }
          reader.readAsDataURL(input.files[i]);
        }
      },
      showVideo(event) {
        let file = event.target.files[0];
        this.blobURL = URL.createObjectURL(file);
      },
      reset(fileType) {
        if (fileType == "image") {
          this.images = [];
        } 
        if (fileType == "video") {
          this.videos = []; 
        }
      }
    }
  }
</script>

<style>
  .split {
    height: 100%;
    width: 50%;
    position: fixed;
    z-index: 1;
    top: 200;
    overflow-x: hidden;
    padding-top: 20px;
    background-color: rgb(149, 214, 240);
  } 

  .left {
    left: 0;
    top: 200;
    }

  .right {
    right: 0;
    top: 200;
  }
    body{
      background-color: rgb(149, 214, 240);
    }

  .loader {
    border: 16px solid #f3f3f3; /* Light grey */
    border-top: 16px solid #3498db; /* Blue */
    border-radius: 50%;
    width: 120px;
    height: 120px;
    animation: spin 2s linear infinite;
  }

  @keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
  }

  img.preview {
    width: 300px;
    background-color: white;
    border: 1px solid #DDD;
    padding: 5px;
  }

  .mainImage {
    border: 1px solid rgb(119, 43, 43);
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
    display: block;
    margin-left: auto;
    margin-right: auto;
  }

  .area {
    width: 20%;
    height: 20%;
    position: absolute;
    border: 4px dashed #000;
    background-image: url("http://kmtlondon.com/img/upload.png");
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
    width: 400%;
    height: 100%;
    margin-left: -300%;
    border: none;
    cursor: pointer;
  }

  .area input:focus {
      outline: none;
  }

  .icon {
    top: 20px;
    width: 40px;
    height: 40px;
  }
</style>
