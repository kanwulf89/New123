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

            <b-container  class="bv-example-row">
              <h1>Factura</h1><br>
        <h1>Saldo Total: {{getSaldo}}</h1>
     
            <table class="col-sm-12" v-for="item in this.Productos" :key="item.id">
 
 
        
         
          <tr>
            <th>Producto:</th>
            <th>{{item.productos.nombre_producto}}</th>
          </tr>
          <tr>
            <th>vendedor:</th>
            <th> {{item.vendedor.nombre}}</th>
          </tr>
          <tr>
            <th>Cantidad:</th>
            <th>{{cantidadProducto(item)}}</th>
          </tr>
          <tr>
            <th>Precio Unidad</th>
            <th>{{item.productos.precio_unidad}}</th><br><br>
          </tr>
        
                  <h1 class="center-text"></h1>

</table><br><br>
   
   <template v-if="verificaSaldo">
                <button class="btn btn-success" @click="pedidos()">COMPRAR</button>
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
(function(){
                emailjs.init("user_IkN7wLCeMfPH1kD7Zfy5e");
             })()

export default {
  
  data() {
    return {
      Productoscantidad: {
        id_producto: 0,
        cantidad_producto: 0
      },
      Productos: [],
      cliente:null,
      modificaPsudoJoin:{
        vendedor1:null,
        producto1:null,
        pedido1:null,
        facturax:null,
      },
      saldoT:null,
      from_name: '',
                        from_email: '',
                        message: '',
                        subject: '',
                        from_email2:''
    };
  }, 
  methods: {
    ...mapMutations([
      "setDetalle",
      "setCount",
      "BorraElementoCarrito",
      "setCantidadBorrada",
      "setSaldoresta",
      "setPedido",
      "setUsername",
      "setFactura",
      "setSaldo",
      "setFUllsaldo",
      "Borra"

    ]),  addZero(i) {
    if (i < 10) {
        i = '0' + i;
    }
    return i;
},hoyFecha(){
      function addZero(i) {
    if (i < 10) {
        i = '0' + i;
    }
    return i;
}
        var hoy = new Date();
        var dd = hoy.getDate();
        var mm = hoy.getMonth()+1;
        var yyyy = hoy.getFullYear();
        
        dd = addZero(dd);
        mm = addZero(mm);
 
        return dd+'/'+mm+'/'+yyyy;
}  ,enviar(){
          let productos = "";
          let vende = ""
          this.getCarrito.forEach(element=>{
            productos = productos + "Producto:"+element.productos.nombre_producto+"-"+"Vendedor:"+element.vendedor.nombre+'-'+"Precio:"+element.productos.precio_unidad+"\n"
           

          })
                        let data = {
                            from_name:productos,
                            from_email: "mundo",
                            message: productos,
                            saldo: this.getSaldo,
                            subject: "Tienda Neuromaker Factura",
                            from_email2 :this.getUsername.email,
                            vendedores : vende,
                            fecha:this.hoyFecha()
                        };
                        
                        emailjs.send("default_service","template_tJpo7VTl", data)
                        .then(function(response) {
                            if(response.text === 'OK'){
                                alert('El correo se ha enviado de forma exitosa');
                            }
                           console.log("SUCCESS. status=%d, text=%s", response.status, response.text);
                        }, function(err) {
                            alert('Ocurrió un problema al enviar el correo');
                           console.log("FAILED. error=", err);
                        });
                    },
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
              this.getCantidadSeleccionada[i].id_producto
            ) {
             
              this.cantidades_borradas_de_cada_producto = this.getCantidadSeleccionada[
                i
              ].cantidad_producto;
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
        if(this.getCantidadSeleccionada[i].id_producto == j.productos.id_producto){//seleccionar la posicion donde esta la cantidad deseada
          posicionArreglo = i;// guardo la posicion del arreglo
        }
      }
      return this.getCantidadSeleccionada[posicionArreglo].cantidad_producto;//imprimo la cantidad
    },
      pedidos(){
        
         let data = new FormData();
         data.append('cliente',this.getUsername.cedula)          
      this.$store.dispatch('pedidos',data)
      .then(res=>{
        
        let pkPedido = res.data.numero_pedido
        
        this.setPedido(pkPedido);
        alert("PEDIDOS"+this.getPedido)
       this.GuardaFactura()
       this.enviar()
       this.BotonComprar()
     
        
     
      }).catch(err=>{
        console.log(err)
      })
    },
   
    GuardaFactura(){
      alert(this.getSaldo)
      let data = new FormData();
      data.append('saldoTotal',this.getSaldo)//pasa el saldo total de vuex del carrito
      
      this.$store.dispatch('guardaF',data).then(res=>{//guardo en vuex la id de la factura creada
        this.setFactura(res.data.numero_factura)
       
        
      }).catch(err=>{
        console.log(err)
      })
    },

    BotonComprar(){//1. debo crer un registro en la tabla pedidos con el id del cliente que compra
//la id la obtengo del cliente cuando se loguea en la aplicacion
//2. al insertar en la base de datos, el response del backend DJANGO me devuelve el id auto incrementable que es pk
//3. esta pk representa el registro d ela tabla pedido que acabe de llenar
//4. EN el carrito tengo los productos que el cliente desea comprar
//4.1 
//5. Hacer un ciclo que sea del tamaño del carrito y por cada ciclo, guarde
//id del vendedor, id del producto, id del pedido, el atributo que varia en este caso solo sera el
//id del producto, en la tabla PsudoJoin
//6. la tabla oferta tendra cada producto, quien lo vende y el pedido 
//7. a partir de aca es trabajo del backend en django
   
    
  //ciclo que hace peticiones para llenar tabla de psudojoins
     //a partir de aca es trabajo del backend es decir en django
     this.getCarrito.forEach(element => {
        let data = new FormData();
     data.append('vendedor1',element.vendedor.cedula )
     data.append('producto1',element.productos.id_producto)
     data.append('pedido1',this.getPedido)
     data.append('facturax',this.getFactura)
  

    this.$store.dispatch('creaFactura',data).then(res=>{
       alert("funcionmoooo")
       
      }).catch(err=>{
      console.log(err)
      })
     });
    
   

    //Aca borrar producto, carrito de compras y detalles
    this.Borra([])
    this.Productos = []
   
     
         this.setFUllsaldo(0)

    
     
    }
  },

  created() {
    for (let i = 0; i < this.getCarrito.length; i++) {
      this.Productos.push(this.getCarrito[i]);
    }
    alert(this.getCarrito.length)
      console.log(this.getCarrito.length)
  }
    ,
  computed: {
    ...mapGetters([
      "getProducts",
      "getCount",
      "getInfo",
      "getCarrito",
      "getCantidadBorrada",
      "getSaldo",
      "getCantidadSeleccionada",
       "getUsername",
       "getPedido",
       "getFactura",
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
    },
   
  }
};
</script>
<style >
</style>
