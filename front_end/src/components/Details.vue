<template>

<div>

  <b-container class="bv-example-row">
    <br>
    <h1>NEUROMAKER TIENDA DE TIENDAS</h1><br><br><br>
  <b-row>
    <b-col sm="8">
     <div class="slider-size">
    <b-carousel
      id="carousel-1"
      v-model="slide"
      :interval="4000"
      controls
      indicators
      background="#ababab"
      img-width="1024"
      img-height="480"
      style="text-shadow: 1px 1px 2px #333;"
      @sliding-start="onSlideStart"
      @sliding-end="onSlideEnd"
    >
      <!-- Text slides with image -->
      <b-carousel-slide v-for="item in productos" :key="item.id">
        <b-card
          slot="img"
          width="1024"
          height="480"
          v-bind:img-src="item.file"
          alt="image slot"
          img-blank 
          img-alt="Card image"  style="height: 100%; width:100%" 
        ></b-card>
      </b-carousel-slide>

    </b-carousel>

  </div>
    </b-col>
    <b-col sm="4">
   
      <b-container class="bv-example-row">
  <b-row>
    <b-col>
     <h1> <b-card-text>{{this.getDetails.productos.nombre_producto}}</b-card-text></h1>
    </b-col>
    <b-row></b-row>
  </b-row>
  <b-row>
    <b-col>
 <h1><b-card-text>${{getDetails.productos.precio_unidad}}</b-card-text></h1>
    </b-col>
  </b-row>
  <b-row>
  <b-col>
  <b-card-text>Cantidad disponible: {{getDetails.productos.cantidad_producto}}</b-card-text>
  </b-col>
  </b-row>
  <b-row>
    <b-col>
       <b-card-text>Descripcion:</b-card-text>
    </b-col>
  </b-row>
  <b-row>
    <b-col>
       <b-card-text>{{getDetails.productos.descripcion}}</b-card-text>
    </b-col>
  </b-row>
  <b-row>
    <b-col>
       <b-card-text>Quien lo Vende: {{getDetails.vendedor.nombre}}</b-card-text><br>
    </b-col>
  </b-row>
  <b-row>
  <b-col lg="12" class="pb-2"><b-button block variant="success" @click=" getProductosDetalles">Comprar</b-button></b-col>
</b-row>
<b-row>
  <b-col>
      <b-button variant="link">Detalles del Vendedor</b-button>
  </b-col>
</b-row>

  <b-row>
    <b-col>
     <form>
  <p class="clasificacion">
    <input id="radio1" type="radio" name="estrellas" value="5"><!--
    --><label for="radio1">★</label><!--
    --><input id="radio2" type="radio" name="estrellas" value="4"><!--
    --><label for="radio2">★</label><!--
    --><input id="radio3" type="radio" name="estrellas" value="3"><!--
    --><label for="radio3">★</label><!--
    --><input id="radio4" type="radio" name="estrellas" value="2"><!--
    --><label for="radio4">★</label><!--
    --><input id="radio5" type="radio" name="estrellas" value="1"><!--
    --><label for="radio5">★</label>
  </p>
</form>
    </b-col>
  </b-row>
</b-container>

    </b-col>
  </b-row>
  </b-container>


 
</div>
  


</template>
<script>
import { mapGetters, mapMutations} from 'vuex'
import Cartas from '@/components/Cartas.vue'
export default {
  data() {
      return {
        slide: 0,
        sliding: null
      }
    },
    methods:{
      ...mapMutations([
       'setCarrito',
       'setCarritox',
      ]),
      getProfiele(){
        this.profile.frist
      },
      getProductosDetalles(){
        alert('DETALLES'+this.getCarrito);
        this.setCarrito(this.getDetails);
        
        alert('Lo que tiene carrito'+this.getCarrito[0].productos.nombre_producto)



      },
       onSlideStart(slide) {
        this.sliding = true
      },
      onSlideEnd(slide) {
        this.sliding = false
      }
    },
    computed:{
        ...mapGetters([
            'getDetails',
            'getPath',
            'getProducts',
            'profile',
            'getCount',
            'getCarrito'
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
.photos{
    width:500px; 
     height: 400px;
}
#form {
  width: 250px;
  margin: 0 auto;
  height: 50px;
}

#form p {
  text-align: center;
}

#form label {
  font-size: 20px;
}

input[type="radio"] {
  display: none;
}

label {
  color: grey;
}

.clasificacion {
  direction: rtl;
  unicode-bidi: bidi-override;
}

label:hover,
label:hover ~ label {
  color: orange;
}

input[type="radio"]:checked ~ label {
  color: orange;
}

</style>
