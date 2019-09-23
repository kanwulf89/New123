<template>
<div>
  <div class="container" >
    <form>
      <fieldset>
        <legend class="center-text"></legend>
          <div class="container center-text">
  <b-alert show variant="primary"><strong>Ropa</strong></b-alert>
          </div>

    <b-card-group deck>
       <b-card   v-for="(i,index) in trae" v-bind:index="index"  v-if="index < 4" :key="i.id" text-variant="black" class="text-center mb-2"
      
   
    img-alt="Image"
    img-top
    tag="article"
    style="max-width: 20rem;">
    <form v-on:submit.prevent="Getid(i)">
      
        <b-card-title>{{i.productos.nombre_producto}}</b-card-title>
        <div>
        <b-card-img  thumbnail fluid v-bind:src="i.productos.files[0].file"  ></b-card-img>
        </div>  
                <b-card-text>${{i.productos.precio_unidad}}</b-card-text>

       <b-card-text>Compralo Ahora!</b-card-text>
        <button class="btn btn-success" >Detalles</button>
    </form>
      </b-card>
    </b-card-group>
      </fieldset>
    </form>
   <b-alert show variant="primary"><strong>VideoJuegos</strong></b-alert>
    <b-card-group deck >
       <b-card   v-for="(j,index) in trae2" v-bind:index="index" v-if="index < 4" :key="j.id" bg-variant="" text-variant="black" class="text-center mb-2"
      
   
    img-alt="Image"
    img-top
    tag="article"
    style="max-width: 25rem;">
    <form v-on:submit.prevent="Getid(j)">
        <b-card-title>{{j.productos.nombre_producto}}</b-card-title>
        <b-card-img thumbnail fluid  v-bind:src="j.productos.files[0].file" fluid alt="Fluid image"></b-card-img>
        <b-card-text>${{j.productos.precio_unidad}}</b-card-text>
        <b-card-text>Compralo Ahora!</b-card-text>
        <button class="btn btn-success">Detalles</button>
    </form>
      </b-card>
    </b-card-group>
    <b-alert show variant="primary"><strong>Celulares</strong></b-alert>
    <b-card-group deck >
       <b-card   v-for="(j,index) in trae3" v-bind:index="index" v-if="index < 4" :key="j.id" bg-variant="" text-variant="black" class="text-center mb-2"
      
   
    img-alt="Image"
    img-top
    tag="article"
    style="max-width: 25rem;">
    <form v-on:submit.prevent="Getid(j)">
        <b-card-title>{{j.productos.nombre_producto}}</b-card-title>
        <b-card-img thumbnail fluid  v-bind:src="j.productos.files[0].file"  alt="Fluid image"></b-card-img>
                <b-card-text>${{j.productos.precio_unidad}}</b-card-text>

        <b-card-text>Compralo Ahora!</b-card-text>
        <button class="btn btn-success">Detalles</button>
    </form>
      </b-card>
    </b-card-group>
     <b-alert show variant="primary"><strong>Televisores</strong></b-alert>
    <b-card-group deck >
       <b-card   v-for="(j,index) in trae4" v-bind:index="index" v-if="index < 4" :key="j.id" bg-variant="" text-variant="black" class="text-center mb-2"
      
   
    img-alt="Image"
    img-top
    tag="article"
    style="max-width: 25rem;">
    <form v-on:submit.prevent="Getid(j)">
        <b-card-title>{{j.productos.nombre_producto}}</b-card-title>

        <b-card-img thumbnail fluid  v-bind:src="j.productos.files[0].file" fluid alt="Fluid image"></b-card-img>
                        <b-card-text>${{j.productos.precio_unidad}}</b-card-text>

        <b-card-text>Compralo Ahora!</b-card-text>
        <button class="btn btn-success">Detalles</button>
    </form>
      </b-card>
    </b-card-group>
    
  </div>
  
</div>
</template>
<script>
let data = [1,2,3,4]
import { mapGetters, mapMutations} from 'vuex'
export default {
  methods:{
    ...mapMutations([
      'setDetalle',
      'setCount'
    ]),
      Getid(i){
        this.setDetalle(i)
        this.$router.push({path:'/Details'})
      }
     
    },
computed:{
  ...mapGetters([
    'getProducts',
    'getCount',
    'getPhones',
    'getTelevisores',
    
  ]),trae(){
      return this.getProducts
      alert('prueba1'+this.getProducts)
    },
    trae2(){
      return this.getCount
    },
    trae3(){
      return this.getPhones
    },
    trae4(){
      return this.getTelevisores;
    }
    
      
     
    }
   
}
</script>
<style >

</style>
