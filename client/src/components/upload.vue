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
            :accept="accepted"
            ></GirderUpload>
        </v-card>
    </v-content>
</template>

<script>
import { Upload as GirderUpload } from '@girder/components/src/components';
import { stringify } from 'qs';

export default {
    name: 'upload',
    inject: ['girderRest'],
    data() {
        return {
            dest: null,
            accepted: "image/jpeg|image/jpg|image/png|video/mp4",
            userRandomId: null,
        }
    },
    components: {
        GirderUpload,
    },
    props: {
        user: String,
    },
    async mounted () {
        const res = await this.girderRest.post("folder", stringify({
                parentType: "user",
                parentId: this.girderRest.user._id,
                name: 'Mouse Data ' + new Date().toISOString()
        }))
        this.dest = res.data;
    },
    methods: {
        async onUpload() {
            const res = await this.girderRest.post("mouse_pain_face/thing")
            console.log(res.data);
            this.$emit("uploaded", res.data);
        },
    }
}
</script>