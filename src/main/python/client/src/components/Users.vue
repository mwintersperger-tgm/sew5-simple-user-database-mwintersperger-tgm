<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Users</h1>
        <hr><br><br>
        <alert :message="message" v-if="showMessage"></alert>
        <button type="button" class="btn btn-success btn-sm" v-b-modal.user-modal>Add User</button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Username</th>
              <th scope="col">Email</th>
              <th scope="col">Photo</th>
              <th></th>
            </tr>
          </thead>
         <tbody>
            <tr v-for="(user, index) in users" :key="index">
              <td>{{ user.username }}</td>
              <td>{{ user.email }}</td>
              <td>{{ user.photo }}</td>
              <td>
                <button
                        type="button"
                        class="btn btn-warning btn-sm"
                        v-b-modal.user-update-modal
                        @click="editUser(user)">
                    Update
                </button>
                <button
                        type="button"
                        class="btn btn-danger btn-sm"
                        @click="onDeleteUser(user)">
                    Delete
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <b-modal ref="addUserModal"
             id="user-modal"
             title="Add a new user"
             hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
      <b-form-group id="form-username-group"
                    label="Username:"
                    label-for="form-username-input">
        <b-form-input id="form-username-input"
                      type="text"
                      v-model="addUserForm.username"
                      required
                      placeholder="Enter Username">
        </b-form-input>
      </b-form-group>
      <b-form-group id="form-email-group"
                    label="Email:"
                    label-for="form-email-input">
        <b-form-input id="form-email-input"
                      type="text"
                      v-model="addUserForm.email"
                      required
                      placeholder="Enter email">
        </b-form-input>
      </b-form-group>
      <b-form-group id="form-password-group"
                    label="Password:"
                    label-for="form-password-input">
        <b-form-input id="form-password-input"
                      type="text"
                      v-model="addUserForm.password"
                      required
                      placeholder="Enter password">
        </b-form-input>
      </b-form-group>
      <b-form-group id="form-photo-group"
                    label="Photo:"
                    label-for="form-photo-input">
        <b-form-input id="form-photo-input"
                      type="text"
                      v-model="addUserForm.photo"
                      required
                      placeholder="Enter photo">
          </b-form-input>
        </b-form-group>
        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
    </b-modal>

    <b-modal ref="editUserModal"
             id="user-update-modal"
             title="Update"
             hide-footer>
      <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
      <b-form-group id="form-username-edit-group"
                    label="Username:"
                    label-for="form-username-edit-input">
        <b-form-input id="form-username-edit-input"
                      type="text"
                      v-model="editForm.username"
                      required
                      placeholder="Enter username">
        </b-form-input>
        </b-form-group>
        <b-form-group id="form-email-edit-group"
                      label="Email:"
                      label-for="form-email-edit-input">
          <b-form-input id="form-email-edit-input"
                        type="text"
                        v-model="editForm.email"
                        required
                        placeholder="Enter email">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-password-edit-group"
                      label="Password:"
                      label-for="form-password-edit-input">
          <b-form-input id="form-password-edit-input"
                        type="text"
                        v-model="editForm.password"
                        required
                        placeholder="Enter Password">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-photo-edit-group"
                      label="Photo:"
                      label-for="form-photo-edit-input">
          <b-form-input id="form-photo-edit-input"
                        type="text"
                        v-model="editForm.photo"
                        required
                        placeholder="Enter photo">
          </b-form-input>
        </b-form-group>
        <b-button type="submit" variant="primary">Update</b-button>
        <b-button type="reset" variant="danger">Cancel</b-button>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert';

export default {
  data() {
    return {
      users: [],
      addUserForm: {
        username: '',
        email: '',
        password: '',
        photo: '',
      },
      editForm: {
        id: '',
        username: '',
        email: '',
        password: '',
        photo: '',
      },
      message: '',
      showMessage: false,
    };
  },
  components: {
    alert: Alert,
  },
  methods: {
    getUsers() {
      const path = 'http://localhost:5000/users';
      axios.get(path)
        .then((res) => {
          this.users = res.data.users;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addUser(payload) {
      const path = 'http://localhost:5000/users';
      axios.post(path, payload)
        .then((res) => {
          this.getUsers();
          this.message = res.data.message;
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getUsers();
        });
    },
    updateUser(payload, userID) {
      const path = `http://localhost:5000/users/${userID}`;
      axios.put(path, payload)
        .then((res) => {
          this.getUsers();
          this.message = res.data.message;
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getUser();
        });
    },
    editUser(user) {
      this.editForm = user;
    },
    removeUser(userID) {
      const path = `http://localhost:5000/users/${userID}`;
      axios.delete(path, {})
        .then(() => {
          this.getUsers();
          this.message = 'User removed!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
          this.getUsers();
        });
    },
    onDeleteUser(user) {
      this.removeUser(user.id);
    },
    initForm() {
      this.addUserForm.username = '';
      this.addUserForm.email = '';
      this.addUserForm.password = '';
      this.addUserForm.photo = '';
      this.editForm.id = '';
      this.editForm.username = '';
      this.editForm.email = '';
      this.editForm.password = '';
      this.editForm.photo = '';
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editUserModal.hide();
      const payload = {
        username: this.editForm.username,
        email: this.editForm.email,
        password: this.editForm.password,
        photo: this.editForm.photo,
      };
      this.updateUser(payload, this.editForm.id);
    },
    onResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.editUserModal.hide();
      this.initForm();
      this.getUsers(); // why?
    },
    onSubmitLogin(evt) {
      evt.preventDefault();
      this.$refs.loginUserModal.hide();
      const payload = {
        lEmail: this.loginUserForm.lEmail,
        lPassword: this.loginUserForm.lPassword,
      };
      this.loginUser(payload);
      this.initForm();
    },
    onResetLogin(evt) {
      evt.preventDefault();
      this.$refs.loginUserModal.hide();
      this.initForm();
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addUserModal.hide();
      const payload = {
        username: this.addUserForm.username,
        email: this.addUserForm.email,
        password: this.addUserForm.password,
        photo: this.addUserForm.photo,
      };
      this.addUser(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addUserModal.hide();
      this.initForm();
    },
  },
  created() {
    this.getUsers();
  },
};
</script>
