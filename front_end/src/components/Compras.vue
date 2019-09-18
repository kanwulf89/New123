<template>
  <div>
      <h1>Mis Compras</h1>
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
                          <img v-bind:src="i.producto1.files[0].file" img-alt="Card image" />
                        </b-card>
                      </b-col>
                      <b-col md="6">
                        <b-card-text>
                          <form>
                            <b-card-text><h1>{{i.producto1.nombre_producto}}</h1></b-card-text>
                            <b-card-text>{{i.producto1.descripcion}}</b-card-text>
                            <b-card-text>Fecha compra:{{i.facturax.created_at}}</b-card-text>
                            <b-card-text>Vendedor:{{i.vendedor1.nombre}}</b-card-text>
                            <b-card-text>Precio Unidad:{{i.producto1.precio_unidad}}</b-card-text>
                           
                          </form>
                          <br />
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
      }
    },
    computed:{
        ...mapGetters([
            'getUsername'
        ])
    },
    created(){
        this.cargaProductosComprados()
    },
    methods:{
      cargaProductosComprados(){
          this.valida.cedula = this.getUsername.cedula
          let data = new FormData();
          data.append('cedula',this.valida.cedula)
        this.$store.dispatch('BuscaProductos',this.valida)
        .then(res=>{
          
          for(let i=0; i<res.data.length; i++){
            this.Productos.push(res.data[i])
          }
        })


      }
    }
  }
</script>