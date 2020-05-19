<template>
  <div id="app">
    <div>
      <h1 style="text-align:center">aMGS Image and Video Upload Tool</h1>
      <img class="center" src="./assets/Mouse.jpeg">
    </div>
    <form class="split left center">
      <h3>Images:</h3>
      <input type="file" accept="image/*" @change="onImageChosen" multiple><br>
      <button @click="onImageUpload">
        <p v-if="isMultipleImages">Upload Images</p>
        <p v-else>Upload Image</p>
      </button>
    </form>
    <form class="split right center">
      <h3>Videos:</h3>
      <input type="file" accept="video/*" @change="onVideoChosen" multiple><br>
      <button @click="onVideoUpload">
        <p v-if="isMultipleVideos">Upload Videos</p>
        <p v-else>Upload Video</p>
      </button>
    </form>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        images: [],
        videos: []
      }
    },
    computed: {
      isMultipleImages() {
        console.log(this.images.length);
        return this.images.length > 1;
      },
      isMultipleVideos() {
        console.log(this.videos.length);
        return this.videos.length > 1;
      }
    },
    methods: {
      onImageChosen(event) {
        Array
          .from(Array(event.target.files.length).keys())
          .map(x => {
            this.images.push(event.target.files[x]);
          });
      },
      onVideoChosen(event) {
        Array
          .from(Array(event.target.files.length).keys())
          .map(x => {
            this.videos.push(event.target.files[x]);
          });
      },
      onImageUpload() {
        /* Something here to upload all images in this.files */
        /*  const fd = new formData() 
            this.images.forEach(x -> {
              fd.append("image", x, x.name)
            })
            axios???.post(fd); (Confused here, .then???)
            this.reset();
                 */
      },
      onVideoUpload() {
        /* Something here to upload all images in this.files */
        /*  const fd = new formData() 
            this.videos.forEach(x -> {
              fd.append("image", x, x.name)
            })
            axios???.post(fd); (Confused here, .then???)
            this.reset();
                 */
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
  /*
  form{
    margin-top: -100px;
    margin-left: -250px;
    width: 500px;
    height: 200px;
    border: 4px dashed #fff;
  }
  form p{
    line-height: 170px;
    color: #ffffff;
    font-family: Arial;
  }
  form input{
    margin: 0;
    padding: 0;
    width: 100%;
    height: 100%;
    outline: none;
    opacity: 0;
  }
  form button{
    margin: 0;
    color: #fff;
    background: #16a085;
    border: none;
    width: 508px;
    height: 35px;
    margin-top: -20px;
    margin-left: -4px;
    border-radius: 4px;
    border-bottom: 4px solid #117A60;
    transition: all .2s ease;
    outline: none;
  }
  form button:hover{
    background: #149174;
    color: #0C5645;
  }
  form button:active{
    border:0;
  } */
  .center {
    display: block;
    margin-left: auto;
    margin-right: auto;
  }
</style>