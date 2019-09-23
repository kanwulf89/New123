<template lang="html">
  <div class="container login" id="content">
      
      <div class="row p-4">
        <div class="col-md-8  col-lg-4 mx-auto">
          <div class="card shadow-lg bg-white">
            <div class="card-header">
              <h2>Login</h2>
            </div>
            <div class="card-body">
              <form v-on:submit.prevent="login">
                <div class="input-group form-group">
                  
                  <input v-model="valida.cedula" type="text" class="form-control" id="" placeholder="cedula">
                </div>
                <div class="form-group">
                  <input v-model="valida.contra" type="password" name="pass" value="" class="form-control" placeholder="Password">
                </div>
                <div class="form-group">
                  <button class="btn btn-success btn-block">Entrar</button>
                </div>
               
              </form>
              <form>
                <div class="form-group">
                   <div class="form-group">
                </div>
                <div class="form-group">
                </div>
                  </div>
                </form>
            </div>
          </div>
        </div>

      </div>
    </div>
</template>

<script>
import sawl from 'sweetalert'
import { mapGetters, mapMutations} from 'vuex'
import axios from "axios";

export default {
  data(){
    return {

      valida: {
        cedula: null,
        contra: null

      },
      err: false
    }
  },
  methods: {

     
    ...mapMutations([
      'setFieldProfilename',
      'setProfileCedula',
      'setValida',
      'setUsername',
      "setCarrito",
      "setCount",
      "BorraElementoCarrito",
      "setCantidadBorrada",
      "setSaldoresta",
      "setPedido",
      "setUsername",
      "setFactura",
      "setSaldo",
      "setFUllsaldo"
    ]),
    ...mapGetters([
      'getValida',
      'profile'
    ]),
     
    login(){

      /*
      const envia = {cedula:"123", contra:"123"}
      const data = Object.assign(envia)
      var request = require("request");

    var options = { method: 'GET',
    url: 'http://localhost:8000/busca',
    headers: 
    { 
     
     'Content-Type': 'application/x-www-form-urlencoded' },
     
  form: {dat}};

request(options, function (error, response, body) {
  if (error) throw new Error(error);
  console.log(response);
  console.log(body);
  console.log(body);
});*/


      if(this.valida.cedula != null && this.valida.contra != null){
      this.$store.dispatch('api_login', this.valida)
        .then(res => {
          let dat = res.data[0]
          alert(dat)
           this.setUsername(dat)//Guarda usuario en varianle username
            if(this.valida.cedula == dat.cedula && dat!=null && dat !=""){//valida si la cedula que retorna es la misma
              
               sawl('Bienvenido a NEUROMARKET','','success')
              this.setFieldProfilename(dat.nombre)
             
               this.setProfileCedula(dat.cedula)
               this.$router.push({path: '/'});
              
              

            }else{
                   sawl('Debe registrarse primero para poder acceder','','error')
            }
          
          //console.log(this.$store.getters.token);
        })
        .catch(err => {
          console.log(this.err);
          this.err = true;
       

        });
    }else{sawl('ERROR campos vacios','','error')
}
    }
  
 
}
,created(){
  this.setFUllsaldo(0);
    //Aca borrar producto, carrito de compras y detalles
    for(let i=0; i<this.getCarrito.length; i++ ){
       this.BorraElementoCarrito(i)// aca lo borra
    }
    for(let i=0; i<this.getCantidadSeleccionada.length;i++){
      this.BorraCantidades(i)
    }
}
}
</script>

<style lang="css">
@import 'https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.5.2/animate.min.css';
  .login{
    margin-top: 100px;
  }
</style>