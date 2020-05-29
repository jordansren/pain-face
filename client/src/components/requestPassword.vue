<template>
    <v-content>
        <v-card class="elevation-12" v-bind:class="{
            inputcard: true}"
            style="max-width: 600px;">

            <!-- Tool Bar -->
            <v-toolbar color="primary" dark flat>
            <v-card-actions></v-card-actions>
            <v-spacer>
                <v-card-title>Forgot Password</v-card-title>
            </v-spacer>
            <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn rounded class="info" @click="backToLogin">
                    Login
                </v-btn>
            </v-card-actions> 
            </v-toolbar>
            <v-form ref="submit" @submit.prevent="resetPass">
                <v-text-field
                v-model="email"
                style="padding: 10px"
                :error-messages="emailErrors"
                label="E-mail"
                required
                @input="$v.email.$touch()"
                @blur="$v.email.$touch()"
                ></v-text-field>
                <v-btn class="primary submit">
                    Submit
                </v-btn>
                <v-alert type="success" style="top: 5px;" 
                class="emailform" :email="email" v-if="submitted">
                    An email with password reset instructions was sent to {{ email }}
                </v-alert>
            </v-form>
        </v-card>
    </v-content>
</template>

<script>
import { validationMixin } from 'vuelidate'; 
import { required, email } from 'vuelidate/lib/validators';
export default {
    name: 'request-password',
    mixins: [validationMixin],
    validations: {
      email: { required, email },
    },
    data() {
        return {
            email: '',
            submitted: false,
        }
    },
    computed: {
        emailErrors () {
            const errors = []
            if (!this.$v.email.$dirty) return errors
            !this.$v.email.email && errors.push('Must be valid e-mail')
            !this.$v.email.required && errors.push('E-mail is required')
            return errors
        },
    },
    methods: {
        backToLogin() {
            this.$emit('relogin');
        },
        async resetPass() {
            if (this.emailErrors.length > 0 || this.email.length == 0) {
                return;
            }
            this.submitted = true;
            this.$v.$touch();
            /* Deal with this.email */
            /* await this.girderRest.post something or anything to send the email */
            /* with link in email call a await this.girderRest.put("user/password", stringify({old: oldpwd, new: newpwd})) */
        }
    }
}
</script>

<style scoped>
    .submit {
        bottom: 10px;
        left: 490px;
    }
</style>