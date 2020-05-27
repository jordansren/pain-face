<template>
    <v-content>
        <v-container grid-list-md></v-container>
        <v-card class="elevation-12" v-bind:class="{
            inputcard: displayInputCard == 2, 
            smallinputcard: displayInputCard == 3,
            loadingCard: displayInputCard == 1}"
            style="max-width: 500px;">

            <!-- Tool Bar -->
            <v-toolbar color="primary" dark flat>
            <v-toolbar-title>Finished</v-toolbar-title>
            <v-spacer></v-spacer>
            <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn rounded class="info" @click="newFile">
                Upload Another File
                </v-btn>
            </v-card-actions> 
            </v-toolbar>
            <div>
                Your result is: 
            </div>
<!--             <div v-if="fileType=='image'">
                <img class="preview" :src="imageData">
            </div>
            <video class="preview" :src="blobURL" v-if="fileType=='video'"></video>
            <h1 v-if="fileType == 'image'" :img="outputImage" style="text-align: center;">
                Mouse Face Pain Score: <br> {{ img }}
            </h1>
            <h1 v-if="fileType == 'video'" :vid="outputVideo" style="text-align: center">
                Mouse Face Pain Score: <br> {{ vid }}
            </h1> -->
        </v-card>
    </v-content>
</template>

<script>
export default {
    name: 'result',
    methods: {
        newFile() {
            this.$emit('newUpload', true);
        }
    }
}
</script>