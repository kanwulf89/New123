<template>
  <div>
    <div class="container">
      <b-container class="bv-example-row">
        <b-row>
          <b-col md="8">
            <!-- inicia datos de carrito -->
            <form>
              <fieldset>
                <b-card-group deck>
                  <b-container class="bv-example-row">
                    <b-row v-for="(i,index) in  this.Productos" v-bind:index="index" :key="i.id">
                      <b-col md="8">
                        <b-card id="foto1" img-left class="mb-3">
                          <img v-bind:src="i.productos.files[0].file" img-alt="Card image" />
                        </b-card>
                      </b-col>
                      <b-col md="4">
                        <b-card-text>
                          <form>
                            <b-card-text>{{i.productos.nombre_producto}}</b-card-text>Some quick text to build on the card and make up the bulk of the card's content.
                            
                            <b-card-text>Compralo Ahora!</b-card-text>
                            <button class="btn btn-success" @click="Getid(i)">Detalles</button>
                            <button class="btn btn-danger" @click="saluda(i)">Eliminar</button>
                          </form>
                          <br />
                        </b-card-text>
                      </b-col>
                    </b-row>
                  </b-container>
                </b-card-group>
              </fieldset>
            </form>
            <!-- Finaliza datos de carrito -->
          </b-col>
          <b-col md="4">
            <!-- Columna Factura -->

            <b-container class="bv-example-row">
              <h1>Factura</h1>
              <b-row v-for="item in this.Productos" :key="item.id">
                <b-col md="12">
                  <b-card-text>{{item.productos.nombre_producto}}</b-card-text>
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
import { mapGetters, mapMutations } from "vuex";
import JQuery from "jquery";
let $ = JQuery;

export default {
  data() {
    return {
      Productoscantidad:{
        id_producto:0,
        cantidad_producto:0,
      },
      Productos:[]
    };
  },
  methods: {
    ...mapMutations(["setDetalle", "setCount", "BorraElementoCarrito",'setCantidadBorrada']),
   restauraCantidad(i){
     //Si la persona elimina el elemento del carrito se restaura el valor de la cantidad
     this.Productoscantidad.id_producto = i;
     this.Productoscantidad.cantidad_producto = this.getCantidadBorrada;
     this.$store.dispatch('restauraCantidad',this.Productoscantidad)
     .then(res=>{
        alert("restauro")
     })
   },
    Getid(i) {
      this.setDetalle("");
      this.setDetalle(i);
      this.$router.push({ path: "/Details" });
    },
    retauraCantidadProducto(id_producto){
      this.$store.dispatch('restauraCantidadProducto')
    },
    borraTodo() {
      this.setCarritox("");
    },
    saluda(j) {
      for (let i = 0; i < this.Productos.length; i++) {
       
        if (
          //compara si el elemento seleccionado en la funcion saluda que borra aun elemento esta en
          // donde se almacena los productos del carrito, se hace porque carrito e sun arreglo de productos
          this.Productos[i].productos.id_producto == j.productos.id_producto
        ) {
          //Va a la base de datos a restaurar el valor cantidad del producto borrado del carrito de compras
          this.restauraCantidad(j.productos.id_producto)
          this.Productos.splice(i, 1);
          this.BorraElementoCarrito(i);
        }
      }
     
    }
  },

  created() {
    for (let i = 0; i < this.getCarrito.length; i++) {
      this.Productos.push(this.getCarrito[i]);
    }
  },
  computed: {
    ...mapGetters(["getProducts", "getCount", "getInfo", "getCarrito", "getCantidadBorrada"]),
    trae() {
      return this.getInfo;
      alert("prueba1" + this.getInfo);
    },
    trae2() {
      return this.getCount;
    },
    traeCarrito() {
      return this.getCarrito;
    }
  }
};
</script>
<style >
</style>
