<template>
  <div>
    <b-container class="bv-example-row">
      <br />
      <h1>NEUROMAKER TIENDA DE TIENDAS</h1>
      <br />
      <br />
      <br />
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
                <b-card slot="img" alt="image slot" img-blank img-alt="Card image" style="max-width:250px max-height:250px">
                  <img id="foto1" v-bind:src="item.file" >
                </b-card>
              </b-carousel-slide>
            </b-carousel>
          </div>
        </b-col>
        <b-col sm="4">
          <b-container class="bv-example-row">
            <b-row>
              <b-col>
                <h1>
                  <b-card-text>{{this.getDetails.productos.nombre_producto}}</b-card-text>
                </h1>
              </b-col>
              <b-row></b-row>
            </b-row>
            <b-row>
              <b-col>
                <h1>
                  <b-card-text>${{getDetails.productos.precio_unidad}}</b-card-text>
                </h1>
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
                <b-card-text>Quien lo Vende: {{getDetails.vendedor.nombre}}</b-card-text>
                <br />
              </b-col>
              <b-col>
                  <b-card-text>
                              Cantidad
                              <input
                                type="number"
                                min="0"
                                step="1"
                                id="n1"
                                v-bind:max="this.getDetails.productos.cantidad_producto"
                                v-model="Productos.cantidad_producto"
                              />
                            </b-card-text>
              </b-col>
            </b-row>
            <b-row>
              <b-col lg="12" class="pb-2">
                <b-button block variant="success" @click=" getProductosDetalles">Add a Carrito<i class="fas fa-cart-plus"></i></b-button>
              </b-col>
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
                    <input id="radio1" type="radio" name="estrellas" value="5" />
                    <!--
                    -->
                    <label for="radio1">★</label>
                    <!--
                    -->
                    <input id="radio2" type="radio" name="estrellas" value="4" />
                    <!--
                    -->
                    <label for="radio2">★</label>
                    <!--
                    -->
                    <input id="radio3" type="radio" name="estrellas" value="3" />
                    <!--
                    -->
                    <label for="radio3">★</label>
                    <!--
                    -->
                    <input id="radio4" type="radio" name="estrellas" value="2" />
                    <!--
                    -->
                    <label for="radio4">★</label>
                    <!--
                    -->
                    <input id="radio5" type="radio" name="estrellas" value="1" />
                    <!--
                    -->
                    <label for="radio5">★</label>
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
import { mapGetters, mapMutations } from "vuex";
import Cartas from "@/components/Cartas.vue";
import JQuery from "jquery";
let $ = JQuery;
import sawl from "sweetalert";

export default {
  data() {
    return {
      slide: 0,
      sliding: null,
      Productos:{
        id_producto:null,
        cantidad_producto:null,
      },
      cantidadActual:0,
      cantidadBorrada_idproducto:{
        id_delPoroducto:null,
        cantidad_borrada:null,
      }
    };
  },
  methods: {
    ...mapMutations(["setCarrito", "setCarritox","setCantidadBorrada","setSaldo","setCantidades"]),
    getProfiele() {
      this.profile.frist;
    },
    creaSaldoFactura(precio){
      this.setSaldo(precio)
    }
    ,retornaCantidad() {
      alert(this.getDetails.cantidad_producto)
      return this.getDetails.cantidad_producto;
    },
    
    getProductosDetalles() {
      let stock = 0;
      //validar si el producto tiene stock
      this.$store.dispatch('valida_stock',this.getDetails.productos.id_producto)
      .then(res=>{
        let data = res.data;
       
        if(res.data.cantidad_producto>0 && this.Productos.cantidad_producto<=res.data.cantidad_producto){
                 //Valido con un for si el producto que voy a agregar ya se encuentra en el carrito
      let productoRepetido = 0;
      if (this.getCarrito.length == 0) {//aca entra si el carrito tiene tamaño 0
        this.Productos.id_producto = this.getDetails.productos.id_producto
          this.setCantidadBorrada(this.Productos.cantidad_producto)
           this.setSaldo(this.getDetails.productos.precio_unidad*this.Productos.cantidad_producto)
         this.cantidadBorrada_idproducto.id_delPoroducto = this.getDetails.productos.id_producto;
        this.cantidadBorrada_idproducto.cantidad_borrada = this.Productos.cantidad_producto;
        alert(this.cantidadBorrada_idproducto.id_delPoroducto +  this.cantidadBorrada_idproducto.cantidad_borrada)
        this.setCantidades(this.cantidadBorrada_idproducto)
        alert(this.getCantidadSeleccionada.length)
        this.$store.dispatch('Resta_STock',this.Productos)//COnsulta
        .then(res=>{
          alert("success")
        }).catch(err=>{
          console.log(err)
        })//final consulta
       
        
        this.setCarrito(this.getDetails);
      } else {
        for (let i = 0; i < this.getCarrito.length; i++) {
          if (
            this.getDetails.productos.id_producto ==
            this.getCarrito[i].productos.id_producto
          ) {
            productoRepetido = 1;

          } else {productoRepetido = 2;
          }
        } //
      }
  

      if (productoRepetido == 1) {
        sawl("Ya tiene ese producto seleciconado en el carrito", "", "error");
      } else if(productoRepetido==2) {
        //Todo lo que hara add to carrito
        //1.peticion que descuenta en stock la cantidad del producto que desea comprar falso esto va en carrito
        this.Productos.id_producto = this.getDetails.productos.id_producto
        this.Productos.cantidad_producto = this.Productos.cantidad_producto
       
       
        this.$store.dispatch('Resta_STock',this.Productos)
        .then(res=>{
          alert("success")
        }).catch(err=>{
          console.log(err)
        })
        //crear arreglo que almacene id del producto y la cantidad seleccionada
        //despues para eliminar producto se busca el id y el valor borrado
        alert(this.getDetails.productos.precio_unidad*this.Productos.cantidad_producto)
        this.setSaldo(this.getDetails.productos.precio_unidad*this.Productos.cantidad_producto)
        this.setCarrito(this.getDetails);
        //cuando adihera a carrito debo guardar la id del producto y la cantidad en un json y esto en un arreglo
        this.cantidadBorrada_idproducto.id_delPoroducto = this.getDetails.productos.id_producto;
        this.cantidadBorrada_idproducto.cantidad_borrada = this.Productos.cantidad_producto;
        alert(this.cantidadBorrada_idproducto.id_delPoroducto +  this.cantidadBorrada_idproducto.cantidad_borrada )
        this.setCantidades(this.cantidadBorrada_idproducto)

        productoRepetido = 0;
      }
        }else{alert('stock vacio o selecciono una cantidad que no existe')}
      }).catch(err=>{
        comsole.log(err)
      })

     
    
    },
    onSlideStart(slide) {
      this.sliding = true;
    },
    onSlideEnd(slide) {
      this.sliding = false;
    }
  },
  computed: {
    ...mapGetters([
      "getDetails",
      "getPath",
      "getProducts",
      "profile",
      "getCount",
      "getCarrito",
      "getCantidadSeleccionada"
    ]),
    productos() {
      return this.getDetails.productos.files;
    }
  },
  name: "Detalles",
  components: {
    Cartas
  },
  created: {}
};
</script>
<style>
.photos {
  width: 500px;
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
.card-body img{
  display:block;
  width: auto!important;
  max-width:1024px;
  max-height:480px;
  height: auto!important;
  margin: auto;
  
  
}
</style>
