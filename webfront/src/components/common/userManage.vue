<template>
  <el-container>
    <el-main>
      <div class="head-title" style="    float: right;margin-right: 135px;margin-bottom: 20px;">
        <!--用户管理-->
        <el-button type="primary" size="small" icon="el-icon-circle-plus"  @click="dialogFormVisible = true">新增用户</el-button>
      </div>
      <div class="table-box">
        <el-table :data="userData">
          <el-table-column
            prop="username"
            label="账号"
            align="center"
            width="200"
          >

          </el-table-column>
          <el-table-column
            prop="email"
            label="邮件"
            align="center"
            width="300"
          >
          </el-table-column>
          <el-table-column
            label="手机号"
            align="center"
            width="200"
            prop="user_phone"
          >
          </el-table-column>
          <el-table-column
            prop="user_type"
            label="用户类型"
            align="center"
            width="200"
          >
            <template slot-scope="scope">
              {{scope.row.user_type|filterType}}
            </template>
          </el-table-column>
          <el-table-column
            prop="opera"
            label="操作"
            align="center"
            width="300"
          >
            <template slot-scope="scope">
              <el-button type="primary" size="small" icon="el-icon-edit" @click="openupdate(scope.row.id)"><span
                style="padding: 15px auto">修改</span></el-button>
              <el-button type="primary" icon="el-icon-remove" size="small" @click="opendelete(scope.row.id)">
                <span>删除</span></el-button>
              <!--<el-button class="btn-primary" icon="el-icon-plus"><span style="padding: 15px auto">禁用</span></el-button>-->
            </template>
          </el-table-column>
        </el-table>
      </div>
      <!---------------------新增添加用户弹框--------------------->
      <el-dialog title="添加用户" :visible.sync="dialogFormVisible" >
        <el-form :model="userform" style="width: 500px">
          <el-form-item label="账户" :label-width="formLabelWidth">
            <el-input v-model="userform.username" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="密码" :label-width="formLabelWidth">
            <el-input v-model="userform.password" autocomplete="off" type="password"></el-input>
          </el-form-item>
          <el-form-item label="邮件" :label-width="formLabelWidth">
            <el-input v-model="userform.email" autocomplete="off" ></el-input>
          </el-form-item>
          <el-form-item label="手机号码" :label-width="formLabelWidth">
            <el-input v-model="userform.phone" autocomplete="off" ></el-input>
          </el-form-item>
          <el-form-item label="用户类型" :label-width="formLabelWidth">
          <el-select v-model="userform.user_type" placeholder="请选择用户类型" style="width: 380px;">
            <el-option label="超级管理员" value="1"></el-option>
            <el-option label="普通用户" value="0"></el-option>
          </el-select>
      </el-form-item>
        </el-form>
         <div slot="footer" class="dialog-footer">
    <el-button @click="dialogFormVisible = false">取 消</el-button>
    <el-button type="primary" @click="addUser()">确 定</el-button>
  </div>
      </el-dialog>
      <!---------------------新增修改用户弹框--------------------->
      <el-dialog title="修改用户" :visible.sync="dialogUpdateFormVisible" >
        <el-form :model="updateform" style="width: 500px">
          <el-form-item label="账户" :label-width="formLabelWidth">
            <el-input v-model="updateform.username" autocomplete="off" disabled></el-input>
          </el-form-item>
          <el-form-item label="密码" :label-width="formLabelWidth">
            <el-input v-model="updateform.password" autocomplete="off" type="password"></el-input>
          </el-form-item>
          <el-form-item label="邮件" :label-width="formLabelWidth">
            <el-input v-model="updateform.email" autocomplete="off" ></el-input>
          </el-form-item>
          <el-form-item label="手机号码" :label-width="formLabelWidth">
            <el-input v-model="updateform.phone" autocomplete="off" ></el-input>
          </el-form-item>
          <el-form-item label="用户类型" :label-width="formLabelWidth">
          <el-select v-model="userform.user_type" placeholder="请选择用户类型" style="width: 380px;">
            <el-option label="超级管理员" value="1"></el-option>
            <el-option label="普通用户" value="0"></el-option>
          </el-select>
      </el-form-item>
        </el-form>
         <div slot="footer" class="dialog-footer">
    <el-button @click="dialogUpdateFormVisible = false">取 消</el-button>
    <el-button type="primary" @click="updateUser()">修 改</el-button>
  </div>
      </el-dialog>
    </el-main>
  </el-container>
</template>

<script>
  export default {
    name: "userManage",
    data() {
      return {
        userData: [],
        dialogFormVisible: false,
        dialogUpdateFormVisible:false,
        userform:{
          username:"",
          user_type:"",
          password:"",
          email:"",
          phone:"",
        },
        updateform:{
          username:"",
          user_type:"",
          password:"",
          email:"",
          phone:"",
        },
        formLabelWidth: '120px'
      }
    },
    mounted() {
    },
    created() {
      this.GetUser();
    },
    methods: {
      // 打开修改用户

      openupdate(uid){
         let data = {"user_id":uid};
         this.$http({
          method: "POST",
          url: this.$store.state.location + "/api/user/get_user_infor/",
          data: this.$Qs.stringify(data)
        }).then(response => {
          let data = response.data;
          this.updateform.username = data[0].username;
          // this.updateform.password = data[0].password;
          this.updateform.email = data[0].email;
          this.updateform.phone = data[0].user_phone;
          this.updateform.user_type = data[0].user_type;
          this.dialogUpdateFormVisible = true;
          console.log(data);
        }).catch(error => {
          console.log(error)
        })
      },
      updateUser(){
        this.dialogUpdateFormVisible = false;
        let data = {
          "username":this.updateform.username,
          "user_type":this.updateform.user_type,
          "email":this.updateform.email,
          "phone":this.updateform.phone,
          "password":this.updateform.password,
          "csrfmiddlewaretoken":this.getCookie('csrftoken')
        };
        this.$http({
          url:this.$store.state.location+"/api/user/update_user/",
          method:"POST",
          data:this.$Qs.stringify(data)
        }).then(response=>{
           let data = response.data;
           if(data === "ok"){
             this.$message({
               type:"info",
               message:"修改成功"
             });
             this.GetUser();
           }else{
             this.$message({
               type:"error",
               message:"修改失败"
             })
           }
        }).catch(error=>{
          console.log(error)
        })
      },
      // 增加用户
      addUser(){
        this.dialogFormVisible = false;
        let data = {
          "username":this.userform.username,
          "user_type":this.userform.user_type,
          "email":this.userform.email,
          "phone":this.userform.phone,
          "password":this.userform.password,
          "csrfmiddlewaretoken":this.getCookie('csrftoken')
        };
        if(this.userform.user_type===""||this.userform.username === "" || this.userform.password===""||this.userform.email === "" || this.userform.phone===""){
          this.$message({
            type: 'info',
            message: '请输入完整信息'
          });
        }
        else{
          this.$http({
          url:this.$store.state.location+"/api/user/add_user/",
          method:"POST",
          data:this.$Qs.stringify(data)
        }).then(response=>{
          let data = response.data;
          if(data === "ok"){
            this.$message({
              type:"success",
              message:"添加成功"
            });
            this.GetUser();
          }else {
            this.$message({
              type: "error",
              message: "添加失败,该用户已经存在"
            })
          }
        }).catch(error=>{
          console.log(error)
        })
        }

      },
      // 打开删除用户提示
      opendelete(uid) {
         this.$confirm('此操作将永久删除该用户, 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          this.deleteUser(uid);
        }).catch(() => {
          this.$message({
            type: 'info',
            message: '已取消删除'
          });
        });
      },
      // 删除用户请求
      deleteUser(uid){
        this.$http({
          url:this.$store.state.location +"/api/user/delete_user/",
          method:"POST",
          data:this.$Qs.stringify({"user_id":uid})
        }).then(response =>{
          let data = response.data;
          if(data === "ok"){
            this.$message({
              type:"success",
              message:"删除成功"
            });
            this.GetUser();
          }else{
            this.$message({
              type:"error",
              message:"删除失败"
            })
          }
        })
      },
      // 获取用户信息
      GetUser() {
        this.$http({
          method: "POST",
          url: this.$store.state.location + "/api/user/get_user_infor/",
          data: {}
        }).then(response => {
          let data = response.data;
          this.userData = data;
          console.log(data);
        }).catch(error => {
          console.log(error)
        })
      }
    }

  }
</script>

<style scoped>
  .table-box {
    width: 1200px;
    margin: 20px auto;
  }
</style>
