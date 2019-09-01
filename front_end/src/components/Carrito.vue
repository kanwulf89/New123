<template>
    <div>
  <div class="container" >

  <b-container class="bv-example-row">
  <b-row>
    <b-col>
      <!-- inicia datos de carrito -->
 <form>
      <fieldset>
    <b-card-group deck  >

      <b-container class="bv-example-row">
  <b-row>
   
    <b-col md="10" v-for="(i,index) in  this.Productos" v-bind:index="index" :key="i.id" > 
      <b-card v-bind:img-src="i.productos.files[0].file" img-alt="Card image" style="max-height: 20rem;" img-left class="mb-30">
      <b-card-text>
         <form >
        <b-card-title>{{i.productos.nombre_producto}}</b-card-title>
        Some quick  text to build on the card and make up the bulk of the card's content.
      <b-card-text>Cantidad Actual: {{i.productos.cantidad_producto}}</b-card-text>
       <b-card-text>Compralo Ahora!</b-card-text>
        <button class="btn btn-success" @click="Getid(i)">Detalles</button>
         <button class="btn btn-danger" @click="saluda(i)">Eliminar</button>
       
  </form><br>
       

</b-card-text>
    </b-card>
    </b-col>
  </b-row>
    </b-container>
    </b-card-group>
      </fieldset>
    </form>
      <!-- Finaliza datos de carrito -->
    </b-col>
    <b-col >
      <!-- Columna Factura -->

      <b-container class="bv-example-row">
        <h1>Factura</h1>
  <b-row v-for="item in this.Productos" :key="item.id">
    <b-col>
      <b-card-text>{{item.productos.nombre_producto}} </b-card-text>
      <b-card-text>{{item.productos.precio_unidad}}</b-card-text>
    </b-col>
  </b-row>
      </b-container>

      <!-- Finaliza Columna factura -->
    </b-col>
  </b-row>
  </b-container>

  
   
  </div>
    </div>
</template>

<script>
import { mapGetters, mapMutations} from 'vuex'
export default {

  data(){
    return{
      Productos:[],
      
    }
  },
methods:{
    ...mapMutations([
      'setDetalle',
      'setCount',
      'BorraElementoCarrito',
      
    ]),
      Getid(i){
        alert(i.productos.id_producto)
          this.setDetalle("")
        this.setDetalle(i)
        this.$router.push({path:'/Details'})
      },
      borraTodo(){
        this.setCarritox("");
      },saluda(j){
         
         for(let i=0; i < this.Productos.length; i++){
          alert("hola")
           if(this.Productos[i].productos.id_producto == j.productos.id_producto){
             this.Productos.splice(i,1);
             this.BorraElementoCarrito(i)
           }
         }
        for(let i=0; i < this.Productos.length; i++){
          alert(this.Productos[i].productos.nombre_producto)
        }



      }}
     
    ,created(){
      
          for(let i = 0; i < this.getCarrito.length; i++){            
            this.Productos.push(this.getCarrito[i])
          }

      
    },
computed:{
  ...mapGetters([
    'getProducts',
    'getCount',
    'getInfo',
    'getCarrito'

    
  ]),trae(){
      return this.getInfo
      alert('prueba1'+this.getInfo)
    },
    trae2(){
      return this.getCount
    },
    traeCarrito(){
        return this.getCarrito;
    }
    
      
     
    }
   
}
</script>
<style >

</style>
