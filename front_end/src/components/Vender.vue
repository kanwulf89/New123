<template>
     <div class="container">
       <form v-on:submit.prevent="register2">
           <fieldset>
               <legend>Especifique lo que desea vender</legend>
               <table style="margin: 0 auto;">
                 <tr>
                   <td><label> Código:</label></td>
                   <td><input required type="number" v-model="dat.id_producto" ></td>
                    

                 </tr>
                 <tr>
                   <td><label>Nombre:</label></td>
                   <td><input required  type="text" v-model="dat.nombre_producto" placeholder="Nombre Claro del Producto"></td>
                 
                 </tr>
                 <tr>
                   <td><label>Cantidad del Producto:</label></td>
                   <td><input  required  placeholder="Cantidad" type="number" v-model="dat.cantidad_producto"></td>
                 </tr>
                 <tr>
                   <td><label >Precio:</label></td>
                   <td><input  required  placeholder="$Valor$" type="number" v-model="dat.precio_unidad"></td>
                 </tr>
                 <tr>
                   <td><label>Categoría: </label></td>
                   <td>
                      <b-form-select v-model="dat.categoria_id" :options="this.categorias"   class="nav-item">
                        <!-- This slot appears above the options from 'options' prop -->
                        <template slot="first">
                          <option :value="null" disabled>Seleccione...</option>
                        </template>
                      </b-form-select>
                   </td>
                 </tr>
               </table>  
               <h1 class="left-text" style="">Neuromarker</h1>  
             
               <label>Descripcion</label>
               <b-form-textarea
      id="textarea"
      placeholder="Caracteristicas del articulo..."
      rows="3"
      max-rows="3"
      v-model="dat.descripcion"
    ></b-form-textarea>
    
    <b-container class="bv-example-row">
    <b-row>
    <b-col> <b-form-file
      id="file-small" 
      size="sm"
      v-model="Foto.file"
      :state="Boolean(Foto.file)"
      placeholder="Eliga una foto aqui 1..."
      drop-placeholder="Drop file here..."
    ></b-form-file>
        <div class="mt-3">Selected file: {{ Foto.file ? Foto.images.file : '' }}</div></b-col>
    <b-col> <b-form-file
      id="file-small" 
      size="sm"
      v-model="atrapa.file"
      :state="Boolean(atrapa.file)"
      placeholder="Eliga una foto aqui..."
      drop-placeholder="Drop file here..."
    ></b-form-file>
        <div class="mt-3">Selected file: {{ atrapa.file ? atrapa.file.name : '' }}</div></b-col>
    <b-col> <b-form-file
      id="file-small" 
      size="sm"
      v-model="atrapa1.file"
      :state="Boolean(atrapa1.file)"
      placeholder="Eliga una foto aqui..."
      drop-placeholder="Drop file here..."
    ></b-form-file>
        <div class="mt-3">Selected file: {{ atrapa1.file ? atrapa1.file.name : '' }}</div></b-col>
  </b-row>
</b-container>
           </fieldset>
                 <button class="btn btn-primary">Crear o Registrar Producto</button>

       </form>
    </div>
</template>
<script>
import { mapGetters, mapMutations} from 'vuex'
import sawl from 'sweetalert'
import axios from 'axios'


export default {
 
 
    data() {
      return {
          dat:{
              
              id_producto:null,
              nombre_producto:null,
              cantidad_producto:null,
              precio_unidad:null,
              descripcion:null,
              categoria_id:null,
              
              
              
           
           
     
      },
      oferta:{
        vendedor:null,
        productos:null,
       

      },
      Foto:{
          file:null,
          p:null

      },
      atrapa:{
        file:null,
        p:null,
      },
      atrapa1:{
        file:null,
        p:null
      },
       categorias:[],
      selected:null,}
    },computed:{
    ...mapGetters([
         'profile',
         'getProducts',
         'getCategorias'
       ]),traeCategorias(){
         return this.getCategorias
       }
  },
     methods:{
       ...mapMutations([
         'setCategorias'
       ]),
        getCategoriaz(){
        const path =  'http://localhost:8000/api/v1.0/categoria/'
        axios.get(path).then((response)=>{
          
            for (var i = response.data.length - 1; i >= 0; i--) {
              var categoria = { value: response.data[i].id_categoria, text: response.data[i].nombre_categoria };
              this.categorias.push(categoria);
            }
           
           
        }).catch((err)=>{
            console.log(err)
            
        })
    },
       
      register2(){
        
       if(this.Foto.file!=null || this.atrapa.file!=null || this.atrapa1.file!=null){
      //Peticion que guarda datos de la entidad producto
      //validar que se ingrese al menos 1 foto, validar que no se manden promesas con vacios

        this.$store.dispatch('api_productos',this.dat)
        .then(res => {
          this.registraOferta()
        if(this.Foto.file!=null && this.atrapa.file==null && this.atrapa1.file==null){this.registraFotos()}
        else if(this.Foto.file==null && this.atrapa.file!=null && this.atrapa1.file==null){this.registraFotos1()}
        else if(this.Foto.file==null && this.atrapa.file==null && this.atrapa1.file!=null){this.registraFotos2()}
        else if(this.Foto.file!=null && this.atrapa.file!=null && this.atrapa1.file==null){this.registraFotos()
        this.registraFotos1()}
        else if(this.Foto.file!=null && this.atrapa.file==null && this.atrapa1.file!=null){this.registraFotos()
         this.registraFotos2()}
         else if(this.Foto.file==null && this.atrapa.file!=null && this.atrapa1.file!=null){ this.registraFotos1()
         this.registraFotos2()}
         else if(this.Foto.file!=null && this.atrapa.file!=null && this.atrapa1.file!=null){this.registraFotos()
          this.registraFotos1()
            this.registraFotos2()}
          this.dat = "";
        }).catch(err => {
          alert(err)
        })
          

      }else{alert('Seleccione una foto al menos')}
   
         },
         registraOferta(){//peticion que guarda en la tabla Oferta que tien
          this.oferta.productos = this.dat.id_producto
          this.oferta.vendedor = this.profile.cedula
          this.$store.dispatch('api_oferta',this.oferta)
          .then(response => {
           
          })

         },
         registraFotos(){
           let data = new FormData()
           data.append('file',this.Foto.file)
           data.append('p',this.dat.id_producto)
           
           this.$store.dispatch('api_fotos',data)
           .then(res =>{
            alert(res)
           })
         },
         registraFotos1(){
           let data = new FormData()
           data.append('file',this.atrapa.file)
           data.append('p',this.dat.id_producto)
           this.$store.dispatch('api_fotos',data)
           .then(response =>{
             console.log('funciono1')
           })
         }, registraFotos2(){
           let data = new FormData()
           data.append('file',this.atrapa1.file)
           data.append('p',this.dat.id_producto)
           this.$store.dispatch('api_fotos',data)
           .then(response =>{
             console.log('funciono2')
           })
         },
  },
   created(){
    this.getCategoriaz()
  },
  }
 

</script>
<style>

</style>
