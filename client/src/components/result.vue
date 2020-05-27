<template>
    <v-content>
        <v-container grid-list-md></v-container>
        <v-card class="elevation-12" v-bind:class="{
            inputcard: true}"
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