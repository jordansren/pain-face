<template>
    <v-content>
        <v-card class="elevation-12" v-bind:class="{
            inputcard: true}"
            style="max-width: 600px;">

            <!-- Tool Bar -->
            <v-toolbar color="primary" dark flat>
            <v-card-actions></v-card-actions>
            <v-spacer>
                <v-btn rounded class="info" @click="newFile">
                    Upload Another File
                    </v-btn>
            </v-spacer>
            <v-card-actions>
                <v-spacer></v-spacer>
                <dropdown :user="user" @logout="logOut"></dropdown>
            </v-card-actions> 
            </v-toolbar>
            <div>
                Your result is: {{ data }}
            </div>
        </v-card>
    </v-content>
</template>

<script>
import dropdown from './dropdown.vue';

export default {
    name: 'result',
    components: {
        dropdown,
    },
    props: ['data', 'user'],
    methods: {
        newFile() {
            this.$emit('newUpload', true);
        },
        logOut() {
            this.$emit("logout"); 
        }
    }
}
</script>