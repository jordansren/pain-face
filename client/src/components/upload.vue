<template>
    <v-content>
        <v-card class="elevation-12" v-bind:class="{
            inputcard:true}"
            style="max-width: 600px;">

            <!-- Tool Bar -->
            <v-toolbar color="primary" dark flat>
            <v-toolbar-title>Accepted File Types: jpg, png, jpeg, mp4</v-toolbar-title>
            <v-spacer></v-spacer>
            <dropdown :user="user" @logout="logOut"></dropdown>
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
import dropdown from './dropdown.vue';

export default {
    name: 'upload',
    inject: ['girderRest'],
    data() {
        return {
            dest: { name: this.girderRest.user.name },
            accepted: "image/jpeg|image/jpg|image/png|video/mp4",
            userRandomId: null,
        }
    },
    components: {
        GirderUpload,
        dropdown,
    },
    async mounted () {
        const res = await this.girderRest.post("folder", stringify({
            parentType: "user",
            parentId: this.girderRest.user._id,
            name: 'Mouse Data ' + new Date().toISOString()
        }))
        this.dest = res.data;
    },
    props: {
        user: String,
    },
    methods: {
        async onUpload() {
            const res = await this.girderRest.post("mouse_pain_face/" + this.dest._id);
            this.$emit("uploaded", res.data);
        },
        logOut() {
            this.$emit('logout');
        }
    }
}
</script>