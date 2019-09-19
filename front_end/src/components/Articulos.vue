<template>
  <div>
      <h1>Mis Articulos en venta</h1>
      <b-container class="bv-example-row">
  <b-row>
    <b-col cols="12">
        <form>
            <fieldset>
       <b-card-group deck>
                  <b-container class="bv-example-row">
                    <b-row v-for="(i,index) in  this.Productos" v-bind:index="index" :key="i.id">
                      <b-col md="6">
                        <b-card id="foto1" img-left class="mb-7">
                          <img v-bind:src="i.productos.files[0].file" img-alt="Card image" />
                        </b-card>
                      </b-col>
                      <b-col md="6">
                        <b-card-text>
                          <form>
                            <b-card-text><h1>{{i.productos.nombre_producto}}</h1></b-card-text>
                            <b-card-text>{{i.productos.descripcion}}</b-card-text>
                            <b-card-text>Precio Unidad:{{i.productos.precio_unidad}}</b-card-text>
                             <b-card-text>Cantidad Producto:{{i.productos.cantidad_producto}}</b-card-text>
                            <template v-if="stockVacio(i)">
                             <input v-model="manda.cantidad_producto" placeholder="%" >
                             <button class="btn btn-success" @click="CalculaPorcentaje(i)">Descuento</button>
                            </template>
                            <template v-else>
                              <p style="color:red;">Stock vacio</p>
                            </template>
                          </form>
                          <br/>
                        </b-card-text>
                      </b-col>
                    </b-row>
                  </b-container>
                </b-card-group>

</fieldset>
        </form>
    </b-col>
  

  </b-row>
</b-container>
  
          
  </div>
</template>

<script>
import {mapGetters} from 'vuex';
  export default {
    data() {
      return {
       Productos:[],
       valida: {
        cedula: null,
      },
       manda:{
         id_producto:null,
         cantidad_producto:null,
       }
      }
    },
    computed:{
        ...mapGetters([
            'getUsername'
        ]),
       
    },
    created(){
        this.cargaProductosComprados()
    },
    methods:{
      cargaProductosComprados(){
          this.valida.cedula = this.getUsername.cedula

          let data = new FormData();
          data.append('cedula',this.valida.cedula)
        this.$store.dispatch('BuscaProductosOfertados',this.valida)
        .then(res=>{
          
          for(let i=0; i<res.data.length; i++){
            this.Productos.push(res.data[i])
          }
        })


      },  CalculaPorcentaje(i){alert(i.productos.cantidad_producto)
        this.manda.id_producto = i.productos.id_producto
        this.$store.dispatch('EnviaDescuento',this.manda)
        .then(res=>{
        alert("funciono")
        }).catch(err=>{
          console.log(err)
        })
      },
      stockVacio(i){
        if(i.productos.cantidad_producto == 0){
          return false
        }else{return true}
      },
     
    }
  }
</script>