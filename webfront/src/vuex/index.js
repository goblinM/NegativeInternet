import Vue from 'vue'
import Vuex from 'Vuex'

Vue.use(Vuex)


export default new Vuex.Store({
  state: {
    // location:'http://172.23.202.192:8000',
    location:"http://192.168.0.107:8000",
    // location:'http://192.168.2.19:10000',
    // location:'http://218.77.58.168:10000',
    //location:'http://218.77.58.168:9099',
    status:false,
  },
  mutations: {
    add(state, command) {
      state.activeName = command;
    },
    propagandaCtrl(state, val) {
      //console.log(val)
      state.status = val;
    },
    firstrouterCtrl(state, val) {
      state.firstrouter = val;
    },
    secondrouterCtrl(state, val) {
      state.secondrouter = val;
    },
    thirdrouterCtrl(state, val) {
      state.thirdrouter = val;
    },
  }
})
