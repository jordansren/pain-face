<template>
    <v-content>
        <v-card class="elevation-12"
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
            :accept="accepted" :preUpload=createFolder
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
            dest: { name: this.girderRest.user.login,
                    _id: null,
                    _modelType: null,
            },
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
            return this.dest;
        },
    methods: {
        async onUpload() {
            const res = await this.girderRest.post("mouse_pain_face/" + this.dest._id);
            this.$emit("uploaded", res.data);
        },
    }
}
</script>
