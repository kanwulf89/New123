
<template>
    <div class="container">
      
        <h1>Profile del Usuario registrado En construccion</h1>
        <h1> {{profile.first_name}}</h1>
        <form v-on:submit.prevent="deleteUser">
        <button>Logout</button>
        
        </form>

    </div>
</template>

<script>
import { mapGetters, mapMutations, mapState} from 'vuex'
import sawl from 'sweetalert'

export default {
    computed:{
        ...mapGetters([
            'profile'
        ]),
    },
    methods:{
        ...mapMutations([
            'setFieldProfilename'
        ]),
        deleteUser: function(){
            this.setFieldProfilename("");
            sawl('Usted cerro su sesion','','success')
             this.$router.push({path: '/'});
        }
    }
}
</script>
<style>

</style>