<template>
  <v-content>
    <v-card
      class="elevation-12"
      :class="{
        inputcard: true}"
    >
      <!-- Tool Bar -->
      <v-toolbar
        color="primary"
        dark
        flat
      >
        <v-btn
          class="primary"
          @click="newFile"
        >
          Upload
        </v-btn>
        <v-spacer />
        <dropdown :user="user" />
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
  name: 'Result',
  inject: ['girderRest'],
  components: {
    dropdown,
  },
  props: {
    data: {
      type: Object,
      default: () => {},
    },
  },
  data() {
    return {
      user: this.girderRest.user.login,
    };
  },
  mounted() {
    if (this.girderRest.user === null) {
      this.$router.push('/');
    }
  },
  methods: {
    newFile() {
      this.$router.push('/upload');
    },
  },
};
</script>
