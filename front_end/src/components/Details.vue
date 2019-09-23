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
              <b-col lg="12" class="pb-2" >
                <template v-if="ExisteUsuario()">
                <b-button block variant="success" @click=" getProductosDetalles">Add a Carrito<i class="fas fa-cart-plus"></i></b-button>
                </template>
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
        id_producto:null,
        cantidad_producto:null,
      },
      count: 0
    };
  },
  methods: {
    ...mapMutations(["setCarrito", "setCarritox","setCantidadBorrada","setSaldo","setCantidades","setContador"]),
    getProfiele() {
      this.profile.frist;
    },
    creaSaldoFactura(precio){
      this.setSaldo(precio)
    },
    ExisteUsuario(){
      if(this.getUsername != ""){
        return true
      }else{return false}
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
//valido si la cantidad traida de la base de datos es >0, si la cantidad ingresada es >0 y 
//si la cantidad ingresada es <= a la cantidad traida de la base de datos

        if(res.data.cantidad_producto>0 && this.Productos.cantidad_producto<=res.data.cantidad_producto && this.Productos.cantidad_producto>0){
      let productoRepetido = 0;
      if (this.getCarrito.length == 0) {//aca entra si el carrito tiene tamaño 0
        this.Productos.id_producto = this.getDetails.productos.id_producto //atrapa la id del producto seleccionado en
        //una variable creada en vue en data return de tipo json para manadarla por axios
          this.setCantidadBorrada(this.Productos.cantidad_producto)//guarda en variable de vuex la cantidad borrada
           this.setSaldo(this.getDetails.productos.precio_unidad*this.Productos.cantidad_producto)//guarda en vuex
           //el valor del producto traido de la base de datos de la peticion de arriba
         this.cantidadBorrada_idproducto.id_producto = this.getDetails.productos.id_producto;//guarda en la variable tipo 
         //object json la id del producto que va a alamcenar en el carrito para usarla despues
        this.cantidadBorrada_idproducto.cantidad_producto = this.Productos.cantidad_producto;//guarda la cantidad que selecciono
        //del producto que se desea comprar para usarla despues
        this.setCantidades(this.cantidadBorrada_idproducto)//guarda en vuex un arreglo de objetos con id del producto
        // y la cantidad que desea comprar de ese producto

        this.$store.dispatch('Resta_STock',this.Productos)//Consulta para descontar cantidad seleccionada del producto que
        //agrego al carrito de compras
        .then(res=>{
          alert("success")//respuesta de la peticion
        }).catch(err=>{
          console.log(err)
        })//final consulta
      this.setCarrito(this.getDetails);//En esta condicion cumplida se agrega el producto al carrito
       this.popToast()

      } else {//Valido con un for si el producto que voy a agregar ya se encuentra en el carrito
        for (let i = 0; i < this.getCarrito.length; i++) {
          if (//getDetails carrito contiene el objeto producto que se atrapa al ingresar a los detalles con el boton detalles
            this.getDetails.productos.id_producto ==
            this.getCarrito[i].productos.id_producto
            //busca el producto que esta en getDetails y lo busca en el arreglo de productos(objetos) de carrito
          ) {
            productoRepetido = 1;// si lo encuentra la variable producto repetido se hace = 1

          } else {productoRepetido = 2;// si no lo encuentra la viariable producto repetido = 2;
          }
        } //
      }
  

      if (productoRepetido == 1) {//valida si esta repetido
        sawl("Ya tiene ese producto seleciconado en el carrito", "", "error");
      } else if(productoRepetido==2) {//valida si no esta repetido
        //Todo lo que hara add to carrito
        this.Productos.id_producto = this.getDetails.productos.id_producto//atrapa la id del producto
        this.Productos.cantidad_producto = this.Productos.cantidad_producto// atrapa la cantidad que selecciono
       
       
        this.$store.dispatch('Resta_STock',this.Productos)//peticion que modifica cantidad del producto
        .then(res=>{
          alert("success")
        }).catch(err=>{
          console.log(err)
        })
        //crear arreglo que almacene id del producto y la cantidad seleccionada
        //despues para eliminar producto se busca el id y el valor borrado

        //guarda el valor del producto multiplicado por la cantidad que selecciono, esto se suma al saldoTotal
        this.setSaldo(this.getDetails.productos.precio_unidad*this.Productos.cantidad_producto)
        this.setCarrito(this.getDetails);//IMPORTANTE: ACA SE LLENA EL ARREGLO CARRITO CUANDO PRESIONA ADD CARRITO
        //cuando adihera a carrito debo guardar la id del producto y la cantidad en un json y esto en un arreglo
        this.cantidadBorrada_idproducto.id_producto = this.getDetails.productos.id_producto;//Id del producto
        this.cantidadBorrada_idproducto.cantidad_producto = this.Productos.cantidad_producto;//cantidad que eligio del producto
        this.setCantidades(this.cantidadBorrada_idproducto)//guarda id del producto y la cantidad que selecciono para comprar
        this.popToast()//muestra mensaje de un elemento seleccionado

        productoRepetido = 0;//Reinicio la variable del producto repetido 
      }
        }else{alert('stock vacio o selecciono una cantidad que no existe')}//aca entra si 1. ya selecciono el producto 
        //2.No selecciono una cantidad, 3.selecciono una cantidad no valida.
      }).catch(err=>{
        console.log(err)
      })

     
    
    },
    onSlideStart(slide) {//metodo que causa error que no afecta nada
      this.sliding = true;
    },
    onSlideEnd(slide) {//metodo que causa error que no afecta nada
      this.sliding = false;
    },
    popToast() {//Toasts
        // Use a shorter name for this.$createElement
        const h = this.$createElement
        // Increment the toast count
        this.count = this.count + 1
        this.setContador(this.count)
        // Create the message
        const vNodesMsg = h(
          'p',
          { class: ['text-center', 'mb-0'] },
          [
            h('b-spinner', { props: { type: 'grow', small: true } }),
            ' Agrego ',
            h('strong', {}, 'Producto'),
            ` #${this.getCarrito.length} ${this.getDetails.productos.nombre_producto}`,
            h('b-spinner', { props: { type: 'grow', small: true } })
          ]
        )
        // Create the title
        const vNodesTitle = h(
          'div',
          { class: ['d-flex', 'flex-grow-1', 'align-items-baseline', 'mr-2'] },
          [
            h('strong', { class: 'mr-2' }, 'Carrito de Compras'),
            h('small', { class: 'ml-auto text-italics' }, '1 minutes ago')
          ]
        )
        // Pass the VNodes as an array for message and title
        this.$bvToast.toast([vNodesMsg], {
          title: [vNodesTitle],
          solid: true,
          variant: 'info'
        })
      },
  },
  computed: {
    ...mapGetters([
      "getDetails",
      "getPath",
      "getProducts",
      "profile",
      "getCount",
      "getCarrito",
      "getCantidadSeleccionada",
      'getUsername',
      'getContador'
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

</style>
