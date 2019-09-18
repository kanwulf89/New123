<template>
  <div>
      <h1>Mis Datos</h1>
      <b-container class="bv-example-row">
  <b-row>
    <b-col cols="12">
        <form>
            <fieldset>
          <table class="col-lg-12" >
 
 
        
         
          <tr>
            <th>Nombre:</th>
            <th>{{getUsername.nombre}}</th><th><button class="btn btn-success">Editar</button></th>
          </tr>
          <tr>
            <th>Apellido:</th>
            <th>{{getUsername.lastname}}</th><th><button class="btn btn-success">Editar</button></th>
          </tr>
          <tr>
            <th>Cedula:</th>
            <th>{{getUsername.cedula}}</th><th><button class="btn btn-success">Editar</button></th>
          </tr>
          <tr>
            <th>Email:</th>
            <th>{{getUsername.email}}</th><th><button class="btn btn-success">Editar</button></th><br><br>
          </tr>
           <tr>
            <th>Phone:</th>
            <th>{{getUsername.phone}} </th><th><button class="btn btn-success">Editar</button></th><br><br>
          </tr>
           <tr>
            <th>Numero tarjeta Credito:</th>
            <th>{{getUsername.phone}}</th><th><button class="btn btn-success">Editar</button></th><br><br>
          </tr>
        
                  <h1 class="center-text"></h1>

</table>

</fieldset>
        </form>
    </b-col>
  

  </b-row>
</b-container>
  
          
  </div>
</template>

<script>
import {mapGetters} from 'vuex';
  export default {
    data() {
      return {
        items: [
          { age: 40, first_name: 'Dickerson', last_name: 'Macdonald' },
          { age: 21, first_name: 'Larsen', last_name: 'Shaw' },
          { age: 89, first_name: 'Geneva', last_name: 'Wilson' },
          { age: 38, first_name: 'Jami', last_name: 'Carney' }
        ]
      }
    },
    computed:{
        ...mapGetters([
            'getUsername'
        ])
    }
  }
</script>