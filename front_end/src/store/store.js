import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate';
import sawl from 'sweetalert'

Vue.use(Vuex);

/* idproducto: this.$route.params.idProducto*/

export const store = new Vuex.Store({
  state: {

    profile: { first_name: null, last_name: null, phone: null, cedula: null, direccion: null, passw: null },
    username:null,
    productos: { id_producto: null, nombre_producto: null, cantidad_producto: null, precio_unidad: null, descripcion: null, categoria_id: null },
    products: [],
    detalle: null,
    count:[],
    valida1:null,
    categorias:[],
    valida:{cedula:null,contra:null},
    info:[],
    autos:[],
    phones:[],
    tv:[],
    saldoTotal:0,
    cantidadBorrada:0,
    saldoBorrado:0,
    cantidades:[],
    vistas:null,
   
  },
  getters: {
    profile: state => {
      return state.profile;
    },
    getInfo: state =>{
      return state.info
    },getUsername: state=>{
      return state.username;
    },
    getProducts: state => {
      return state.products
    },
    getDetails: state => {
      return state.detalle
    },
    getCount: state => {
      return state.count
    },
    getProducts1: state => {
      return state.products1
    },
    getCategorias: state => {
      return state.categorias
    },
    getValida: state =>{
      return state.valida.cedula
    },
    getCarrito: state =>{
      return state.autos
    },
    getPhones: state =>{
      return state.phones
    },
    getTelevisores: state =>{
      return state.tv;
    },
    getSaldo: state =>{
      return state.saldoTotal;
    },
    getCantidadBorrada: state =>{
      return state.cantidadBorrada;
    },
    getSaldoBorrado: state =>{
      return state.saldoBorrado;
    },
    getCantidadSeleccionada: state=>{
      return state.cantidades;
    },
    getVista: state =>{
      return state.vistas
    }
    
    
  
    
  }, 
  mutations: {
    setVistas: (state,field) =>{
      state.vistas = field;
    }
    ,
    setProfile: (state, pro) => {
      state.profile = pro;
    },
    setSaldoBorrado: (state, field)=>{
      state.saldoBorrado = field
    },
    setInfo: (state,field) =>{
      state.info = field
    },
    setFieldProfilename: (state, field) => {
      state.profile.first_name = field;
    },
    setProfileCedula: (state,field) =>{
      state.profile.cedula = field;
    },
    setProducts: (state, field) => {
      state.products = field;
    },
    setDetalle: (state, field) => {
      state.detalle = field;
    },
    setCount: (state,field) =>{
      state.count = field;
    },
    setProducts1: (state, field) => {
      state.products1 = field;
    },
    setId:(state,field) =>{
      state.cedula = field;
    },
    setCategorias: (state,field) =>{
      state.categorias = field;
    },
    setValida: (state,field) => {
      state.valida = field
    },
    setCarrito: (state, field) => {
      state.autos.push(field);
    },
    BorraElementoCarrito: (state,field) =>{
      state.autos.splice(field,1)
    },
    setPhone: (state,field)=>{
      state.phones = field;
    },
    setTelevisores: (state,field) =>{
      state.tv = field;
    },
    setUsername: (state,field)=>{
      state.username = field;
    },
    setSaldo: (state,field) =>{
      state.saldoTotal = parseFloat(state.saldoTotal) + parseFloat(field)
    },setFUllsaldo:(state,field)=>{
      state.saldoTotal = field;
    },
    setCantidadBorrada: (state,field) =>{//no hace falta esta variable global
      state.cantidadBorrada = field
    },setSaldoresta: (state,field) =>{
      state.saldoTotal = parseFloat(state.saldoTotal)-  parseFloat(field)
    },
    setCantidades: (state,field)=>{
      state.cantidades.push(field)
    },
    BorraCantidades: (state,field) =>{
      state.cantidades.splice(field,1)
    }
    
   
  },
  actions: {
    api_register: (context, credentials) => {
        axios.post('http://localhost:8000/api/v1.0/clientes/', credentials)
          .then(res => {
        
           alert(res.data.cedula)
          })
          .catch(err => {
           alert(err);
            
          })
     
    },
    setFieldProfile: (context) => {
      context.commit('setFieldProfile')
    },
    api_login: (context, credentials) => {

      return new Promise((resolve, reject) => {
        axios.get('http://localhost:8000/busca/'+credentials.contra+'/'+credentials.cedula+'/')
          .then(res => {
            resolve(res);
            
          }).catch(err =>{
            alert(err)
          })
      })
    },
    api_productos: (context, credentials) => {
      alert('prueba'+credentials.categoria_id)
      return new Promise((resolve, reject) =>{
     axios.post('http://localhost:8000/api/v1.0/gp/', credentials)
        .then(res => {
          sawl('Creo un producto correctamente','','success')
          resolve(res)
        }).catch(ErrorEvent => {
          sawl('Error al registrar el Producto','','error')
          alert(ErrorEvent)
        })
      })
        /*axios.post('http://localhost:8000/api/v1.0/Oferta/', credentials.id_producto)
        .then(res => {
          alert('Producto registrado Bien')
        }).catch(err=>{
          alert(err)
        })*/
    },

    api_oferta: (context, credentials) =>{
      //Peticion que llena la entidad Oferta, esta entidad tiene
      //3 llaves foreaneas, 1 id del vendedor, id del producto e id del pedido(null default)
      axios.post('http://localhost:8000/api/v1.0/Oferta/', credentials)
      .then(res =>{
          alert('Registro finalizado')
      }).catch(err =>{
        alert(err)
      })
      
    },
    api_fotos: (context, credentials) => {
      return new Promise((resolve, reject) =>{
      axios.post('http://localhost:8000/api/v1.0/guardafoto/', credentials)
      .then(res =>{
        resolve(res)
      }).catch(err =>{
        
      })
    })
    },
    api_trae: (context) =>{
      return new Promise((resolve, reject) => { 
        axios.get('http://localhost:8000/traeJuegos/')
      .then(res =>{
        resolve(res)})
        .catch(err => {
          console.log(err)
        })
      })

    },
    Pro_cate: (context, credentials) =>{
      return new Promise((resolve, reject) =>{
        axios.get('http://localhost:8000:/buscaCate/'+credentials+'/')
        .then(res =>{
          resolve(res)
        }).catch(err=>{
          console.log(err)
        })
      })
    },
    B_P: (context, credentials) =>{
      return new Promise((resolve, reject) =>{
        axios.get('http://localhost:8000/buscaProdu/'+credentials+'/')
        .then(res =>{
          resolve(res)
        }).catch(err =>{
          console.log(err)
        })
      })
    },
    api_trea_phone: (context, credentials)=>{
      return new Promise((resolve, reject)=>{
        axios.get('http://localhost:8000/traeCelulares/')
        .then(res=>{
          resolve(res)
        }).catch(err =>{
          console.log(err);
        })
      })
    },
    api_trea_tele: (context, credentials) =>{
      return new Promise((resolve)=>{
        axios.get('http://localhost:8000/traeTeles/')
        .then(res =>{
          resolve(res)
        }).catch(res=>{
          console.log(res)
        })
      })
    },
    valida_stock:(context, credentials) =>{
      return new Promise((resolve)=>{
        axios.get('http://localhost:8000/stock/'+credentials+'/')
        .then(res=>{
          resolve(res)
        }).catch(res=>{
          console.log(res);
        })
      })
    },

    Resta_STock:(context,credentials) =>{
      return new Promise((resolve)=>{
        axios.patch('http://localhost:8000/edita/'+credentials.id_producto+'/'+credentials.cantidad_producto+'/')
        .then(res=>{
          resolve(res)
        }).catch(err=>{
          console.log(err)
        })
      })
    },
    restauraCantidad:(context,credentials)=>{
      return new Promise((resolve)=>{
        axios.patch('http://localhost:8000/restaura/'+credentials.id_producto+'/'+credentials.cantidad_producto+'/')
        .then(res=>{
          resolve(res)
        }).catch(err=>{
          console.log(err)
        })
      })
    }
    
  },plugins: [createPersistedState()]
})