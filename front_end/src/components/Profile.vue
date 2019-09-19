<template>
  <b-container fluid class="bv-example-row">
    <b-row>
      <b-col sm="0">
        <!--collapse-->
        <div>
          <!-- Single button triggers two "<b-collapse>" components -->
          <b-button
            class="btn btn-info"
            v-b-toggle.collapse-a.collapse-b.collapse-c.collapse-d.collapse-e
            style=" width:200px"
          >Mi cuenta</b-button>

          <!-- Elements to collapse -->
          <b-collapse id="collapse-a" class="mt-2">
            <b-card>Bienvenido<br>{{getUsername.email}}</b-card>
           
          </b-collapse>
          <b-collapse id="collapse-b" class="mt-2">
            <b-card>
              <!--
              <button
                lass="mt-2"
                class="btn btn-info"
                @click="llamaVistaFactura()"
                style="width:150px"
              >Facturas</button>-->
            </b-card>
          </b-collapse>
          <b-collapse id="collapse-c" class="mt-2">
            <b-card>
              <button
                lass="mt-2"
                class="btn btn-info"
                style="width:150px"
                @click="llamaVistaCompras()"
              >Compras</button>
            </b-card>
          </b-collapse>
          <b-collapse id="collapse-d" class="mt-2">
            <b-card>
              <button
                lass="mt-2"
                class="btn btn-info"
                style="width:150px"
                @click="llamaVistasUsuario()"
              >Ventas</button>
            </b-card>
          </b-collapse>
          <b-collapse id="collapse-e" class="mt-2">
            <b-card>
              <button
                lass="mt-2"
                class="btn btn-info"
                style="width:150px"
                @click="llamaVistaArticulos()"
              >Articulos</button>
            </b-card>
          </b-collapse>
          <b-collapse id="collapse-e" class="mt-2">
            <b-card>
              <button
                lass="mt-2"
                class="btn btn-info"
                style="width:150px"
                @click="llamaVistaDatos()"
              >Mis datos</button>
            </b-card>
          </b-collapse>
        </div>
        <!-- collapse -->
      </b-col>
      <b-col sm="8" v-if="comparavistas">
        <Ventas></Ventas>
      </b-col>
      <b-col sm="8" v-if="comparavavistas2">
        <Facturas></Facturas>
      </b-col>
      <b-col sm="8" v-if="comparavistas3">
        <Compras></Compras>
      </b-col>
      <b-col sm="8" v-if="comparavistas4">
        <Articulos></Articulos>
      </b-col>
      <b-col sm="8" v-if="comparavistas5">
        <Datos></Datos>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import Perfil from "@/components/Perfil.vue";
import Ventas from "@/components/Ventas.vue";
import Facturas from "@/components/Facturas.vue";
import Articulos from "@/components/Articulos.vue";
import Compras from "@/components/Compras.vue";
import Datos from '@/components/Datos.vue';

import { mapGetters, mapMutations } from "vuex";
export default {
  methods: {
    ...mapMutations(["setVistas"]),
    llamaVistasUsuario() {
      this.setVistas("Ventas");
    },
    llamaVistaFactura() {
      this.setVistas("Facturas");
    },
    llamaVistaCompras() {
      this.setVistas("Compras");
    },
    llamaVistaArticulos() {
      this.setVistas("Articulos");
    },
    llamaVistaDatos(){
      this.setVistas("Datos")
    }
  },
  computed: {
    ...mapGetters(["getVista","getUsername"]),
    comparavavistas2() {
      if (this.getVista == "Facturas") {
        return true;
      }
    },
    comparavistas() {
      if (this.getVista == "Ventas") {
        return true;
        console.log("funcione1");
      }
    },
    comparavistas3() {
      if (this.getVista == "Compras") {
        return true;
      }
    },
    comparavistas4() {
      if (this.getVista == "Articulos") {
        return true;
      }
    },
    comparavistas5(){
      if(this.getVista == "Datos"){
        return true
      }
    }
  },
  components: {
    Perfil,
    Ventas,
    Facturas,
    Articulos,
    Compras,
    Datos,
  }
};
</script>

<style >
</style>