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
        <v-card-title>Reset Password</v-card-title>
        <v-spacer />
        <v-btn
          class="primary"
          @click="backToLogin"
        >
          Log In
        </v-btn>
      </v-toolbar>
      <v-form
        ref="submit"
        @submit.prevent="resetPass"
      >
        <v-alert
          v-if="submitted"
          type="info"
          class="emailform"
          :email="email"
        >
          An email with password reset instructions was sent to {{ email }}
        </v-alert>
        <v-text-field
          v-model="email"
          style="padding: 15px"
          :error-messages="emailErrors"
          label="E-mail"
          required
          @input="$v.email.$touch()"
          @blur="$v.email.$touch()"
        />
        <div class="text-right">
          <v-btn
            class="primary submit"
            @click="resetPass"
          >
            Reset
          </v-btn>
        </div>
      </v-form>
    </v-card>
  </v-content>
</template>

<script>
import { validationMixin } from 'vuelidate';
import { required, email } from 'vuelidate/lib/validators';

export default {
  name: 'RequestPassword',
  mixins: [validationMixin],
  validations: {
    email: { required, email },
  },
  data() {
    return {
      email: '',
      submitted: false,
    };
  },
  computed: {
    emailErrors() {
      const errors = [];
      if (!this.$v.email.$dirty) return errors;
      return errors;
    },
  },
  methods: {
    backToLogin() {
      this.$router.push('/');
    },
    async resetPass() {
      if (this.emailErrors.length > 0 || this.email.length === 0) {
        return;
      }
      this.submitted = true;
      this.$v.$touch();
      /* Deal with this.email */
      /* await this.girderRest.post something or anything to send the email */
      /* with link in email call a await this.girderRest.put("user/password") */
    },
  },
};
</script>

<style scoped>
    .submit {
        bottom: 20px;
        right: 15px;
    }
</style>
