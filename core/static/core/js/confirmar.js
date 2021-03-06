function confirmarEliminacion(id) {
    Swal.fire({
        title: '¿Estás seguro?',
        text: "No podrás deshacer esta acción!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Sí, Eliminar!',
        cancelButtonText: 'Cancelar'
    }).then((result) => {
        if (result.isConfirmed) {
            //redirigimos al usuario a la ruta de eliminar
            window.location.href = "/eliminar-anime/"+id+"/";
        }
    })
}