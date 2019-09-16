<template>
  <div class="block1">
    <div>
      <!-- Single button triggers two "<b-collapse>" components -->
      <b-button
        v-b-toggle.collapse-a.collapse-b.collapse-c.collapse-d.collapse-e
        style="background-color:green; width:200px"
      >Mi cuenta</b-button>

      <!-- Elements to collapse -->
      <b-collapse id="collapse-a" class="mt-2">
        <b-card>Bienvenido</b-card>
      </b-collapse>
      <b-collapse id="collapse-b" class="mt-2">
        <b-card>
          <button
            lass="mt-2"
            class="btn btn-danger"
            @click="vistaFactura()"
            style="background-color:green; width:150px"
          >Facturas</button>
        </b-card>
      </b-collapse>
      <b-collapse id="collapse-c" class="mt-2">
        <b-card>
          <button
            lass="mt-2"
            class="btn btn-danger"
            style="background-color:green; width:150px"
          >Compras</button>
        </b-card>
      </b-collapse>
      <b-collapse id="collapse-d" class="mt-2">
        <b-card>
          <button
            lass="mt-2"
            class="btn btn-danger"
            style="background-color:green; width:150px"
            @click="vistaVentas()"
          >Ventas</button>
        </b-card>
      </b-collapse>
      <b-collapse id="collapse-e" class="mt-2">
        <b-card>
          <button
            lass="mt-2"
            class="btn btn-danger"
            style="background-color:green; width:150px"
          >Articulos</button>
        </b-card>
      </b-collapse>
    </div>
  </div>
</template>

<script>
import Ventas from "@/components/Ventas.vue";

import { mapGetters, mapMutations } from "vuex";

export default {
  methods: {
    ...mapMutations(["setVistas"]),
    vistaVentas() {
      this.setVistas("Ventas");
    },
    vistaFactura() {
      this.setVistas("Facturas");
    }
  }
};
</script>

<style scoped>
.block1 {
  color: black;
  width: 200px;
  border: 1px solid green;
}

.block2 {
  color: blue;
  width: 70px;
  border: 2px solid black;
  position: relative;
}
</style>