<template>
  <div id="app" style="height: 100%">

    <!--<img src="./assets/backup.jpg" width="100%" >-->
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}

</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  /*margin-top: 60px;*/
  left: 0;
    top: 0;
    width: 98vw;
    height: 100vh;
    margin: 0;
    position: absolute;

}

</style>
