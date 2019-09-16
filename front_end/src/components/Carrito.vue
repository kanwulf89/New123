<template>

      <b-container fluid class="bv-example-row">
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

            <b-container fluid class="bv-example-row">
              <h1>Factura</h1>
              <b-row v-for="item in this.Productos" :key="item.id">
                <b-col md="12">
                  <b-card-text><strong>{{item.productos.nombre_producto}}</strong></b-card-text>
                  <b-card-text>Vendedor: {{item.vendedor.nombre}}</b-card-text>
                  <b-card-text>Precio: {{item.productos.precio_unidad}}</b-card-text>
                  <b-card-text>Cantidad: {{cantidadProducto(item)}}</b-card-text>
                </b-col>
              </b-row>
              <b-container></b-container>
              <b-card-text>Saldo Total: {{getSaldo}}</b-card-text>
              <template v-if="verificaSaldo">
                <button class="btn btn-success">COMPRAR</button>
              </template>
            </b-container>

            <!-- Finaliza Columna factura -->
          </b-col>
        </b-row>
      </b-container>
  
</template>

<script>
import { mapGetters, mapMutations } from "vuex";
import JQuery from "jquery";
let $ = JQuery;

export default {
  data() {
    return {
      Productoscantidad: {
        id_producto: 0,
        cantidad_producto: 0
      },
      Productos: []
    };
  },
  methods: {
    ...mapMutations([
      "setDetalle",
      "setCount",
      "BorraElementoCarrito",
      "setCantidadBorrada",
      "setSaldoresta"
    ]),
    restauraCantidad(i) {
      //Si la persona elimina el elemento del carrito se restaura el valor de la cantidad
      this.Productoscantidad.id_producto = i;
      this.Productoscantidad.cantidad_producto = this.getCantidadBorrada;
      this.$store
        .dispatch("restauraCantidad", this.Productoscantidad)
        .then(res => {
          alert("restauro");
        });
    },
    Getid(i) {
      this.setDetalle("");
      this.setDetalle(i);
      this.$router.push({ path: "/Details" });
    },
    retauraCantidadProducto(id_producto) {
      this.$store.dispatch("restauraCantidadProducto");
    },
    borraTodo() {
      this.setCarritox("");
    },
    saluda(j) {
      let test = 0;
      let cantidades_borradas_de_cada_producto = 0;
      alert(
        "cantidades" +
          this.getCantidadSeleccionada.length +
          "carrito" +
          this.Productos.length
      );

      for (let i = 0; i < this.Productos.length; i++) {
        alert(
          "idP" +
            this.Productos[i].productos.id_producto +
            "idCanti" +
            this.getCantidadSeleccionada[i].id_delPoroducto
        );

        if (
          //compara si el elemento seleccionado en la funcion saluda que borra aun elemento esta en
          // donde se almacena los productos del carrito, se hace porque carrito e sun arreglo de productos
          this.Productos[i].productos.id_producto == j.productos.id_producto
        ) {
          for (let i = 0; i < this.getCantidadSeleccionada.length; i++) {
            if (
              j.productos.id_producto ==
              this.getCantidadSeleccionada[i].id_delPoroducto
            ) {
             
              this.cantidades_borradas_de_cada_producto = this.getCantidadSeleccionada[
                i
              ].cantidad_borrada;
            }
          }

          //Va a la base de datos a restaurar el valor cantidad del producto borrado del carrito de compras
          this.restauraCantidad(j.productos.id_producto);
          this.setSaldoresta(
            j.productos.precio_unidad *
              this.cantidades_borradas_de_cada_producto
          ); //Resta el saldo total pero no cantidad
          this.Productos.splice(i, 1);
          this.BorraElementoCarrito(i);
          //debo hacer que el for me recorra el arreglo de id y cantidad borrada para que me borre del saldo
          //total no solo el valor del producto si no la cantidad que se escogio del producto
          test = 1;
        } else {
          test = 0;
        }
      }
    },
    cantidadProducto(j){//funcion que retorna la cantidad que la persona selecciono
      let posicionArreglo = 0;//variable para gaudar cantidad
      for(let i=0; i<this.getCantidadSeleccionada.length;i++){
        if(this.getCantidadSeleccionada[i].id_delPoroducto == j.productos.id_producto){//seleccionar la posicion donde esta la cantidad deseada
          posicionArreglo = i;// guardo la posicion del arreglo
        }
      }
      return this.getCantidadSeleccionada[posicionArreglo].cantidad_borrada;//imprimo la cantidad
    }
  },

  created() {
    for (let i = 0; i < this.getCarrito.length; i++) {
      this.Productos.push(this.getCarrito[i]);
    }
  },
  computed: {
    ...mapGetters([
      "getProducts",
      "getCount",
      "getInfo",
      "getCarrito",
      "getCantidadBorrada",
      "getSaldo",
      "getCantidadSeleccionada"
    ]),
    trae() {
      return this.getInfo;
    },
    trae2() {
      return this.getCount;
    },
    traeCarrito() {
      return this.getCarrito;
    },
    verificaSaldo() {
      if (this.getSaldo > 0) {
        return true;
      } else {
        return false;
      }
    }
  }
};
</script>
<style >
</style>
