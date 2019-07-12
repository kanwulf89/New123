<template >
    <div class="container">
        <div class="row">
            <div class="col text-left">
                <h2>Listado productos</h2>
                <div class="col-md-12">
                <b-table striped hover :items="productos" :fields="fields">
                    </b-table>
                </div>
                </div>
                </div>
                </div>
</template>

<script >
import axios from "axios";
export default{
data (){
    return{
        fields: [
            {key: 'nombre_producto', label:'Nombre'},
            {key: 'id_productos', label: 'Id_productos'},
            {key: 'cantidad_producto', label:'Cantidad'},
        ],
        productos :[]
    }
},
methods : {
        getProductos(){
            const path =  'http://localhost:8000/api/v1.0/producto/'
            axios.get(path).then((response)=>{
                this.productos = response.data
            }).catch((err)=>{
                console.log(err)
                
            })
        }
    }, created(){
        this.getProductos()
    }
}
</script>

<style>



</style>