<template>
    <v-content>
        <v-container grid-list-md></v-container>
        <v-card class="elevation-12" v-bind:class="{
            inputcard:true}"
            style="max-width: 500px;">

            <!-- Tool Bar -->
            <v-toolbar color="primary" dark flat>
            <v-toolbar-title>Accepted File Types: jpg, png, jpeg, mp4</v-toolbar-title>
            <v-spacer></v-spacer>
            <div v-if="user != ''">
                Logged in as: <br> {{ user }}
            </div>
            </v-toolbar>
            <GirderUpload :dest="dest"
            :postUpload=onUpload :multiple=false
            :accept="accepted" :preUpload=userFolder
            @click="onUpload"></GirderUpload>
        </v-card>
    </v-content>
</template>

<script>
import { Upload as GirderUpload } from '@girder/components/src/components';
export default {
    name: 'upload',
    inject: ['girderRest'],
    data() {
        return {
            dest: {name: this.user + "/private",
                    _id: "5eceadd795278a871c7532e6",
                    _modelType: "folder"
                    },
            accepted: "image/jpeg|image/jpg|image/png|video/mp4",
        }
    },
    components: {
        GirderUpload,
    },
    props: {
        user: String,
    },
    methods: {
        onUpload() {
            this.$emit("uploaded");
        },
        userFolder() {
            
        },
    }
}
</script>