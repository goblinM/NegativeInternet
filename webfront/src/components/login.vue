<template>
  <!--<div class="top">正真科技&nbsp;·&nbsp;用数据改变未来</div>-->
  <div class="content">

    <div class="login">
      <div class="title">舆情系统&nbsp;·&nbsp;登录</div>
      <div class="line">
        <img class="smallImg" src="../assets/icon-4.png"/>
        <input placeholder="请输入账号" type="text" v-model="usernameModel"/>
      </div>
      <div class="line">
        <img class="smallImg" src="../assets/icon-5.png"/>
        <input placeholder="请输入密码" type="password" v-model="passwordModel"/>
      </div>
      <button type="button" class="logBut" @click="UserLogin">登&nbsp;&nbsp;录</button>
    </div>
  </div>
</template>
import {Loading} from 'element-ui'
<script>
  export default {
    name: "login",
    data() {
      return {
        usernameModel: "",
        passwordModel: "",

      }
    },
    computed: {
      //判断是否是手机
      rightPhoneNumber: function () {
        return /^1\d{10}$/gi.test(this.phoneNumber)
      }
    },
    methods: {

      UserLogin() {
        console.log("login...");
        this.$http.interceptors.request.eject(this.$store.state.$responseInterceptor); //取消拦截器
        this.$http.interceptors.response.eject(this.$store.state.$responseInterceptor); //取消拦截器
        if (this.usernameModel === "") {
          this.$message.error({message: '请输入账号！', duration: 700});
          return false;
        } else if (this.passwordModel === "") {
          this.$message.error({message: '请输入密码！', duration: 700});
          return false;
        }
        else {
          this.loading = true;
          let data = {
            "username": this.usernameModel,
            "password": this.passwordModel,
            //"csrfmiddlewaretoken": this.getCookie("csrftoken")
          };
          this.$http({
            url: this.$store.state.location + "/api/user/login/",
            method: "POST",
            data: this.$Qs.stringify(data),
            headers: {
              'content-type': 'application/x-www-form-urlencoded'
            },
          }).then((response) => {
            let result = response.data;
            console.log(result);
            if (result === "failed") {
              this.$message.error({
                message: "登录失败，请检查账户或密码"
              })
            }
            else {
              sessionStorage.setItem("name", result["username"]);
              sessionStorage.setItem("user_id", result["id"]);
              sessionStorage.setItem("user_type",result["user_type"])
              this.$router.push({name:"HomePage"});//跳转到index页面
            }
            //取消拦截器
            //this.$http.interceptors.request.handlers = [];
          }).catch(error => {
            console.log(error)
          })
        }
      },
    }
  }
</script>

<style scoped>
  .content {
    background: url("../assets/bg3.jpg");
    text-align: center;
    background-size: 100% 100%;
    height: 100%;
    overflow: hidden;
    background-repeat: no-repeat;
    background-position: center;
    background-attachment: fixed;
  }

  .top {
    background: #ffffff2e;
    width: 100%;
    position: absolute;
    bottom: 0;
    line-height: 60px;
    left: 0px;
    right: 0px;
    color: #fff;
    text-align: center;
    font-size: 16px;
    font-weight: 600;
  }

  .login {
    background: #dddbdbd6;
    width: 40%;
    text-align: center;
    padding: 70px 2%;
    border-radius: 2px;
    position: absolute;
    top: 16%;
    left: 27.5%;
  }

  .title {
    font-weight: 600;
    font-size: 22px;
    color: #333;
    margin-bottom: 40px;
  }

  .line {
    border-bottom: 1px solid #ffff;
    margin: 22px 1%;
    width: 96%;
  }

  .line input {
    border: none;
    padding: 0px 1%;
    margin: 1%;
    background: #ffffff14;
    width: 84%;
    font-size: 16px;
    line-height: 30px;
    outline: none;
  }

  .line .smallImg {
    width: 26px;
    float: left;
    vertical-align: middle;
    margin-top: 1px;
  }

  .logBut {
    background: #7bb5ee;
    padding: 10px 80px;
    border: none;
    color: #fff;
    margin-top: 40px;
    font-size: 16px;
    cursor: pointer;
  }
</style>
