<template>

<div class="col-xs-6 col-xs-offset-3 tamano" >
<div>

  <b-container class="bv-example-row">
  <b-row>
    <b-col>
      <div class="container3-fixed">
  <b-carousel 
    id="carousel-fade"
    style="text-shadow: 3px 0px 2px #000"
    fade
    indicators
    img-width="800"
    img-height="480"
  >
    <b-carousel-slide v-for="items in productos" :key="items.id"
      v-bind:img-src="items.file" fluid alt="Responsive image" 
    ></b-carousel-slide>
   
  </b-carousel>
  <br>
 
  
</div>
    </b-col>
    <b-col>
       <b-card no-body class="overflow-hidden" style="max-width: 999px;">
    <b-row no-gutters>
      <b-col md="2">

     </b-col>
      <b-col md="6">
        <b-card-body v-bind:title="this.getDetails.productos.nombre_producto">
          
        <h1>  <b-card-text>${{getDetails.productos.precio_unidad}}</b-card-text></h1>
          <b-card-text></b-card-text>
         <strong> <b-card-text>Vendedor {{getDetails.vendedor.nombre}}</b-card-text></strong>
          <b-card-text> {{getDetails.productos.descripcion}}</b-card-text>

         
          <buttom class="btn btn-danger">Comprar</buttom>
          <!--        <b-card-img v-bind:src="getDetails.productos.files[0].file" class="rounded-0"></b-card-img>
          -->
       
        </b-card-body>
      </b-col>
    </b-row>
  </b-card>
    </b-col>
  </b-row>
   </b-container>
 
</div>
  
</div>

</template>
<script>
import { mapGetters, mapMutations} from 'vuex'
import Cartas from '@/components/Cartas.vue'
export default {
    methods:{
      getProfiele(){
        this.profile.frist
      }
    },
    computed:{
        ...mapGetters([
            'getDetails',
            'getPath',
            'getProducts',
            'profile',
            'getCount'
        ]),
        productos(){
      return this.getDetails.productos.files
      
    },
    },
    name: 'Detalles',
    components: {
        Cartas
    },
    created:{
    
    }
}
</script>
<style>

</style>
