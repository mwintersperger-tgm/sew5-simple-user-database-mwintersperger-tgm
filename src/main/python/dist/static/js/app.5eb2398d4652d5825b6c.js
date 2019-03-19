webpackJsonp([1],{"1/oy":function(e,t){},GfHa:function(e,t){},Id91:function(e,t){},Jmt5:function(e,t){},NHnr:function(e,t,r){"use strict";Object.defineProperty(t,"__esModule",{value:!0});r("Jmt5");var s=r("e6fC"),o=r("7+uW"),a={render:function(){var e=this.$createElement,t=this._self._c||e;return t("div",{attrs:{id:"app"}},[t("router-view")],1)},staticRenderFns:[]};var i=r("VU/8")({name:"App"},a,!1,function(e){r("c4Nv")},null,null).exports,n=r("/ocq"),l=r("mtWM"),d=r.n(l),m={name:"Ping",data:function(){return{msg:""}},methods:{getMessage:function(){var e=this;d.a.get("http://localhost:5000/ping").then(function(t){e.msg=t.data}).catch(function(e){console.error(e)})}},created:function(){this.getMessage()}},u={render:function(){var e=this.$createElement,t=this._self._c||e;return t("div",{staticClass:"container"},[t("button",{staticClass:"btn btn-primary",attrs:{type:"button"}},[this._v(this._s(this.msg))])])},staticRenderFns:[]},p=r("VU/8")(m,u,!1,null,null,null).exports,c={render:function(){var e=this.$createElement,t=this._self._c||e;return t("div",[t("b-alert",{attrs:{variant:"success",show:""}},[this._v(this._s(this.message))]),this._v(" "),t("br")],1)},staticRenderFns:[]},h={data:function(){return{users:[],addUserForm:{username:"",email:"",password:"",photo:""},editForm:{id:"",username:"",email:"",password:"",photo:""},loginUserForm:{lEmail:"",lPassword:""},message:"",showMessage:!1}},components:{alert:r("VU/8")({props:["message"]},c,!1,null,null,null).exports},methods:{getUsers:function(){var e=this;d.a.get("http://localhost:5000/users").then(function(t){e.users=t.data.users}).catch(function(e){console.error(e)})},addUser:function(e){var t=this;d.a.post("http://localhost:5000/users",e).then(function(e){t.getUsers(),t.message=e.data.message,t.showMessage=!0}).catch(function(e){console.log(e),t.getUsers()})},updateUser:function(e,t){var r=this,s="http://localhost:5000/users/"+t;d.a.put(s,e).then(function(e){r.getUsers(),r.message=e.data.message,r.showMessage=!0}).catch(function(e){console.error(e),r.getUser()})},editUser:function(e){this.editForm=e},removeUser:function(e){var t=this,r="http://localhost:5000/users/"+e;d.a.delete(r,{}).then(function(){t.getUsers(),t.message="User removed!",t.showMessage=!0}).catch(function(e){console.error(e),t.getUsers()})},onDeleteUser:function(e){this.removeUser(e.id)},loginUser:function(e){var t=this;d.a.post("http://localhost:5000/login",e).then(function(e){t.getUsers(),t.message=e.data.message,t.showMessage=!0}).catch(function(e){console.log(e),t.getUsers()})},initForm:function(){this.addUserForm.username="",this.addUserForm.email="",this.addUserForm.password="",this.addUserForm.photo="",this.editForm.id="",this.editForm.username="",this.editForm.email="",this.editForm.password="",this.editForm.photo=""},onSubmitUpdate:function(e){e.preventDefault(),this.$refs.editUserModal.hide();var t={username:this.editForm.username,email:this.editForm.email,password:this.editForm.password,photo:this.editForm.photo};this.updateUser(t,this.editForm.id)},onResetUpdate:function(e){e.preventDefault(),this.$refs.editUserModal.hide(),this.initForm(),this.getUsers()},onSubmitLogin:function(e){e.preventDefault(),this.$refs.loginUserModal.hide();var t={lEmail:this.loginUserForm.lEmail,lPassword:this.loginUserForm.lPassword};this.loginUser(t),this.initForm()},onResetLogin:function(e){e.preventDefault(),this.$refs.loginUserModal.hide(),this.initForm()},onSubmit:function(e){e.preventDefault(),this.$refs.addUserModal.hide();var t={lEmail:this.loginUserForm.lEmail,lPassword:this.loginUserForm.lPassword,username:this.addUserForm.username,email:this.addUserForm.email,password:this.addUserForm.password,photo:this.addUserForm.photo};this.addUser(t),this.initForm()},onReset:function(e){e.preventDefault(),this.$refs.addUserModal.hide(),this.initForm()}},created:function(){this.getUsers()}},f={render:function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("div",{staticClass:"container"},[r("div",{staticClass:"row"},[r("div",{staticClass:"col-sm-10"},[r("p",{staticClass:"right"},[r("button",{directives:[{name:"b-modal",rawName:"v-b-modal.login-user-modal",modifiers:{"login-user-modal":!0}}],staticClass:"btn btn-success btn-sm",attrs:{type:"button"}},[e._v("\n      Login\n      ")])]),e._v(" "),r("h1",[e._v("Users")]),e._v(" "),r("hr"),r("br"),r("br"),e._v(" "),e.showMessage?r("alert",{attrs:{message:e.message}}):e._e(),e._v(" "),r("button",{directives:[{name:"b-modal",rawName:"v-b-modal.user-modal",modifiers:{"user-modal":!0}}],staticClass:"btn btn-success btn-sm",attrs:{type:"button"}},[e._v("Add User")]),e._v(" "),r("br"),r("br"),e._v(" "),r("table",{staticClass:"table table-hover"},[e._m(0),e._v(" "),r("tbody",e._l(e.users,function(t,s){return r("tr",{key:s},[r("td",[e._v(e._s(t.username))]),e._v(" "),r("td",[e._v(e._s(t.email))]),e._v(" "),r("td",[e._v(e._s(t.photo))]),e._v(" "),r("td",[r("button",{directives:[{name:"b-modal",rawName:"v-b-modal.user-update-modal",modifiers:{"user-update-modal":!0}}],staticClass:"btn btn-warning btn-sm",attrs:{type:"button"},on:{click:function(r){e.editUser(t)}}},[e._v("\n                  Update\n              ")]),e._v(" "),r("button",{staticClass:"btn btn-danger btn-sm",attrs:{type:"button"},on:{click:function(r){e.onDeleteUser(t)}}},[e._v("\n                  Delete\n              ")])])])}))])],1)]),e._v(" "),r("b-modal",{ref:"loginUserModal",attrs:{id:"login-user-modal",title:"Login","hide-footer":""}},[r("b-form",{staticClass:"w-100",on:{submit:e.onSubmitLogin,reset:e.onResetLogin}},[r("b-form-group",{attrs:{id:"form-email-login-group",label:"Email:","label-for":"form-email-login-input"}},[r("b-form-input",{attrs:{id:"form-email-login-input",type:"text",required:"",placeholder:"Enter Email"},model:{value:e.loginUserForm.lEmail,callback:function(t){e.$set(e.loginUserForm,"lEmail",t)},expression:"loginUserForm.lEmail"}})],1),e._v(" "),r("b-form-group",{attrs:{id:"form-password-login-group",label:"Password:","label-for":"form-password-login-input"}},[r("b-form-input",{attrs:{id:"form-password-input",type:"text",required:"",placeholder:"Enter password"},model:{value:e.loginUserForm.lPassword,callback:function(t){e.$set(e.loginUserForm,"lPassword",t)},expression:"loginUserForm.lPassword"}})],1),e._v(" "),r("b-button",{attrs:{type:"submit",variant:"primary"}},[e._v("Submit")]),e._v(" "),r("b-button",{attrs:{type:"reset",variant:"danger"}},[e._v("Reset")])],1)],1),e._v(" "),r("b-modal",{ref:"addUserModal",attrs:{id:"user-modal",title:"Add a new user","hide-footer":""}},[r("b-form",{staticClass:"w-100",on:{submit:e.onSubmit,reset:e.onReset}},[r("b-form-group",{attrs:{id:"form-username-group",label:"Username:","label-for":"form-username-input"}},[r("b-form-input",{attrs:{id:"form-username-input",type:"text",required:"",placeholder:"Enter Username"},model:{value:e.addUserForm.username,callback:function(t){e.$set(e.addUserForm,"username",t)},expression:"addUserForm.username"}})],1),e._v(" "),r("b-form-group",{attrs:{id:"form-email-group",label:"Email:","label-for":"form-email-input"}},[r("b-form-input",{attrs:{id:"form-email-input",type:"text",required:"",placeholder:"Enter email"},model:{value:e.addUserForm.email,callback:function(t){e.$set(e.addUserForm,"email",t)},expression:"addUserForm.email"}})],1),e._v(" "),r("b-form-group",{attrs:{id:"form-password-group",label:"Password:","label-for":"form-password-input"}},[r("b-form-input",{attrs:{id:"form-password-input",type:"text",required:"",placeholder:"Enter password"},model:{value:e.addUserForm.password,callback:function(t){e.$set(e.addUserForm,"password",t)},expression:"addUserForm.password"}})],1),e._v(" "),r("b-form-group",{attrs:{id:"form-photo-group",label:"Photo:","label-for":"form-photo-input"}},[r("b-form-input",{attrs:{id:"form-photo-input",type:"text",required:"",placeholder:"Enter photo"},model:{value:e.addUserForm.photo,callback:function(t){e.$set(e.addUserForm,"photo",t)},expression:"addUserForm.photo"}})],1),e._v(" "),r("b-button",{attrs:{type:"submit",variant:"primary"}},[e._v("Submit")]),e._v(" "),r("b-button",{attrs:{type:"reset",variant:"danger"}},[e._v("Reset")])],1)],1),e._v(" "),r("b-modal",{ref:"editUserModal",attrs:{id:"user-update-modal",title:"Update","hide-footer":""}},[r("b-form",{staticClass:"w-100",on:{submit:e.onSubmitUpdate,reset:e.onResetUpdate}},[r("b-form-group",{attrs:{id:"form-username-edit-group",label:"Username:","label-for":"form-username-edit-input"}},[r("b-form-input",{attrs:{id:"form-username-edit-input",type:"text",required:"",placeholder:"Enter username"},model:{value:e.editForm.username,callback:function(t){e.$set(e.editForm,"username",t)},expression:"editForm.username"}})],1),e._v(" "),r("b-form-group",{attrs:{id:"form-email-edit-group",label:"Email:","label-for":"form-email-edit-input"}},[r("b-form-input",{attrs:{id:"form-email-edit-input",type:"text",required:"",placeholder:"Enter email"},model:{value:e.editForm.email,callback:function(t){e.$set(e.editForm,"email",t)},expression:"editForm.email"}})],1),e._v(" "),r("b-form-group",{attrs:{id:"form-password-edit-group",label:"Password:","label-for":"form-password-edit-input"}},[r("b-form-input",{attrs:{id:"form-password-edit-input",type:"text",required:"",placeholder:"Enter Password"},model:{value:e.editForm.password,callback:function(t){e.$set(e.editForm,"password",t)},expression:"editForm.password"}})],1),e._v(" "),r("b-form-group",{attrs:{id:"form-photo-edit-group",label:"Photo:","label-for":"form-photo-edit-input"}},[r("b-form-input",{attrs:{id:"form-photo-edit-input",type:"text",required:"",placeholder:"Enter photo"},model:{value:e.editForm.photo,callback:function(t){e.$set(e.editForm,"photo",t)},expression:"editForm.photo"}})],1),e._v(" "),r("b-button",{attrs:{type:"submit",variant:"primary"}},[e._v("Update")]),e._v(" "),r("b-button",{attrs:{type:"reset",variant:"danger"}},[e._v("Cancel")])],1)],1)],1)},staticRenderFns:[function(){var e=this.$createElement,t=this._self._c||e;return t("thead",[t("tr",[t("th",{attrs:{scope:"col"}},[this._v("Username")]),this._v(" "),t("th",{attrs:{scope:"col"}},[this._v("Email")]),this._v(" "),t("th",{attrs:{scope:"col"}},[this._v("Photo")]),this._v(" "),t("th")])])}]},b=r("VU/8")(h,f,!1,null,null,null).exports;o.a.use(n.a);var v=new n.a({routes:[{path:"/ping",name:"Ping",component:p},{path:"/",name:"Users",component:b}],mode:"history"});o.a.config.productionTip=!1,o.a.use(s.a),new o.a({el:"#app",router:v,components:{App:i},template:"<App/>"})},c4Nv:function(e,t){},zj2Q:function(e,t){}},["NHnr"]);
//# sourceMappingURL=app.5eb2398d4652d5825b6c.js.map