<template>
  <div>
    <div class="container">
      <form>
        <fieldset>
          <legend class="center-text">{{getInfo[0].productos.categoria_id.nombre_categoria}}</legend>

          <b-card-group deck>
            <b-container class="bv-example-row">
              <b-row>
                <b-col></b-col>
                <b-col md="10" v-for="(i,index) in trae" v-bind:index="index" :key="i.id">
                  <b-card
                    v-bind:img-src="i.productos.files[0].file"
                    img-alt="Card image"
                    style="max-height: 20rem;"
                    img-left
                    class="mb-30"
                  >
                    <b-card-text>
                      <form v-on:submit.prevent="Getid(i)">
                        <b-card-title>{{i.productos.nombre_producto}}</b-card-title>Some quick text to build on the card and make up the bulk of the card's content.
                        <b-card-text>Cantidad Actual: {{i.productos.cantidad_producto}}</b-card-text>
                        <b-card-text>Compralo Ahora!</b-card-text>
                        <button class="btn btn-success">Detalles</button>
                        <button class="btn btn-danger">Comprar</button>
                      </form>
                    </b-card-text>
                  </b-card>
                </b-col>
              </b-row>
            </b-container>
          </b-card-group>
        </fieldset>
      </form>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapMutations } from "vuex";
export default {
  methods: {
    ...mapMutations(["setDetalle", "setCount"]),
    Getid(i) {
      this.setDetalle("");
      this.setDetalle(i);
      this.$router.push({ path: "/Details" });
    }
  },
  computed: {
    ...mapGetters(["getProducts", "getCount", "getInfo"]),
    trae() {
      return this.getInfo;
      alert("prueba1" + this.getInfo);
    },
    trae2() {
      return this.getCount;
    }
  }
};
</script>
<style >
</style>
