<template>
  <v-content>
    <v-card class="elevation-12">
      <!-- Tool Bar -->
      <v-toolbar
        color="primary"
        dark
        flat
      >
        <v-toolbar-title class="text-wrap">
          File Types: jpg, png, jpeg, mp4
        </v-toolbar-title>
        <v-spacer />
        <dropdown :user="user" />
      </v-toolbar>
      <GirderUpload
        :dest="dest"
        :post-upload="onUpload"
        :multiple="false"
        :accept="accepted"
        :pre-upload="createFolder"
      />
    </v-card>
  </v-content>
</template>

<script>
import { Upload as GirderUpload } from '@girder/components/src/components';
import { stringify } from 'qs';
import dropdown from './dropdown.vue';

export default {
  name: 'Upload',
  inject: ['girderRest'],
  components: {
    GirderUpload,
    dropdown,
  },
  data() {
    return {
      dest: {
        name: this.girderRest.user.login,
        _id: null,
        _modelType: null,
      },
      accepted: 'image/jpeg,image/jpg,image/png,video/mp4',
      user: this.girderRest.user.login,
    };
  },
  computed: {
    loggedIn() {
      return !(this.girderRest.user === null);
    },
  },
  methods: {
    async onUpload() {
      const res = await this.girderRest.post(`mouse_pain_face/${this.dest.dest._id}`);
      this.$router.push({
        name: 'Result',
        params: {
          data: res.data,
        },
      });
    },
    async createFolder() {
      if (this.girderRest.user === null) {
        this.$router.push('/');
      }
      const res = await this.girderRest.post('folder', stringify({
        parentType: 'user',
        parentId: this.girderRest.user._id,
        name: `Mouse Data ${new Date().toISOString()}`,
      }));
      this.dest = { dest: res.data };
      return this.dest;
    },
  },
};
</script>
