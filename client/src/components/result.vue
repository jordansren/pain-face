<template>
    <v-content>
        <v-card class="elevation-12" v-bind:class="{
            inputcard: true}"
            >

            <!-- Tool Bar -->
            <v-toolbar color="primary" dark flat>
            <v-btn class="primary" @click="newFile">
                Upload
            </v-btn>
            <v-spacer></v-spacer>
            <dropdown :user="user" @logout="logOut"></dropdown>
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
    inject: ['girderRest'],
    data() {
        return {
            user: this.girderRest.user.login,
        }
    },
    components: {
        dropdown,
    },
    props: ['data'],
    mounted() {
        if (this.girderRest.user == null) {
            this.$router.push('/');
        }
    },
    methods: {
        newFile() {
            this.$router.push('/upload');
        },
        logOut() {
            this.girderRest.user = null;
            this.$router.push('/');
        }
    }
}
</script>
