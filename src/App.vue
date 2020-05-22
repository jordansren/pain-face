<template>
  <div id="app">
    <!-- Title -->
    <div>
      <h1 style="text-align:center">aMGS Image and Video Upload Tool</h1>
      <img class="center mainImage" src="./assets/Mouse.jpeg">
    </div>

    <!-- Image Upload -->
    <form class="split left center">
      <h3 style="text-align:center">Images</h3>
      <input class="center" type="file" accept="image/jpeg,image/png" @change="onImageChosen" v-if="!uploadingImage"><br>
      <p style="text-align:center" v-if="wrongImageType">
        Oops! You did not input an image of type png, jpeg, or jpg. <br> Current file to upload: {{ images[0].name }}
      </p>
      <div class="image-preview" v-if="imageData.length > 0">
        <div v-for="img in imageData" :key="img">
          <img class="center preview imageStack" :src="img">
        </div>
      </div>
      <button class="center clear" @click="onImageUpload" v-if="!uploadingImage"> 
        <p v-if="numberOfImages > 1">Upload Images</p>
        <p v-else>Upload Image</p>
      </button>
      <div class="center clear" v-if="uploadingImage">
        <h3 style="text-align:center" v-if="numberOfImages > 1">Processing {{ images[0].name }}...</h3>
        <h3 style="text-align:center" v-else>Processing {{ images[0].name }}...</h3>
        <div class="center loader"></div>
      </div>
    </form>

    <!-- Video Upload -->
    <form class="split right center">
      <h3 style="text-align:center">Videos</h3>
      <input class="center" type="file" accept="video/*" @change="onVideoChosen" v-if="!uploadingVideo"><br>
      <p style="text-align:center" v-if="wrongVideoType">
        Oops! You did not input an image of type png, jpeg, or jpg. <br> Current file to upload: {{ videos[0].name }}
      </p>
      <video style="width:300px" :src="blobURL" class="center" v-if="numberOfVideos > 0"></video>
      <button class="center clear" @click="onVideoUpload" v-if="!uploadingVideo">
        <p v-if="numberOfVideos > 1">Upload Videos</p>
        <p v-else>Upload Video</p>
      </button>
      <div class="center clear" v-if="uploadingVideo">
        <h3 style="text-align:center" v-if="numberOfVideo > 1">Processing {{ videos[0].name }}...</h3>
        <h3 style="text-align:center" v-else>Processing {{ videos[0].name }}...</h3>
        <div class="center loader"></div>
      </div>
    </form>
  </div>
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
        this.uploadingImage = false;
      },
      async onVideoUpload() {
        this.uploadingVideo = true;
        const axios = require('axios');
        const path = 'http://localhost:8080/'; /* Not sure what to put here */
        this.outputVideo = await axios.get(path);
        this.uploadingVideo = false;
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
    overflow-x: hidden;
    padding-top: 20px;
    background-color: rgb(149, 214, 240);
  } 

  /* Control the left side */
  .left {
    left: 0;
    top: 200;
    }


  /* Control the right side */
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
</style>