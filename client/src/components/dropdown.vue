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
          @click="handler(item)"
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
    inject: ['girderRest'],
    data() {
        return {
            items: [{ title: 'Logout' },]
        }
    },
    methods: {
        handler(item) {
            if (item.title == "Logout") {
              this.girderRest.user = null;
              this.$router.push('/');
            }
        }
    }
}
</script>
