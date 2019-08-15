<template>
<div class="container center-text">
<div class="Detalles-relative">
<div>
    <h1>{{getDetails.nombre_producto}}</h1>
  <b-card no-body class="overflow-hidden" style="max-width: 999px;">
    <b-row no-gutters>
      <b-col md="6">
        <b-card-img v-bind:src="getDetails.productos.images" class="rounded-0"></b-card-img>
      </b-col>
      <b-col md="6">
        <b-card-body title="Horizontal Card">
          <b-card-text>
            {{getDetails.productos.descripcion}}
          </b-card-text>
          <b-card-text>Precio Unidad:</b-card-text>
          <b-card-text>{{getDetails.productos.precio_unidad}}</b-card-text>
          <b-card-text>Vendedor</b-card-text>
          <b-card-text>{{getDetails.vendedor.nombre}}</b-card-text>
          <buttom class="btn btn-success">Comprar</buttom>
          
       
        </b-card-body>
      </b-col>
    </b-row>
  </b-card>
</div>
  
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
        ])
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
