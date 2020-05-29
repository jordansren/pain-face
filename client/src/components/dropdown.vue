<template>
  <div class="text-center">
    <v-menu offset-y>
      <template v-slot:activator="{ on }">
        <v-btn
          color="primary"
          dark  :user="user"
          v-on="on"
        >
          {{ user }}
        </v-btn>
      </template>
      <v-list>
        <v-list-item
          v-for="(item, index) in items"
          :key="index"
          @click="logout"
        >
          <v-list-item-title>{{ item.title }}</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>
  </div>
</template>

<script>
export default {
    props: {
        user: String
    },
    data() {
        return {
            items: [{ title: 'logout' },]
        }
    },
    methods: {
        logout() {
            this.$emit('logout');
        },
        handler(item) {
            if (item.title == "logout") {
                this.logout;
            }
        }
    }
}
</script>