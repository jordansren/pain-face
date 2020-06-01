<template>
    <v-content>
        <GirderAuth :register="true" @forgotpassword="forgotPassword"
             /> <!-- :oauth="true" -->
    </v-content>
</template>

<script>
  import { Authentication as GirderAuth } from '@girder/components/src/components';

  export default {
    inject: ['girderRest'],
    components: {
      GirderAuth,
    },
    computed: {
      currentUserLogin() {
        return this.girderRest.user ? this.girderRest.user.login : 'anonymous';
      },
      loggedIn() {
          return this.girderRest.user == null;
      }
    },
    watch: {
        loggedIn() {
            if (!(this.girderRest.user == null)) {
                this.$router.push({
                    name: 'Upload',
                });
            } 
        }
    },
    methods: {
      forgotPassword() {
        this.$router.push('/password-reset');
        this.hasPassword = false;
      }
    },
  }
</script>

