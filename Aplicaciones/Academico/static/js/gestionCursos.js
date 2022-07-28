(function () {
    const botonEliminar = document.querySelectorAll('.eliminacion');

    botonEliminar.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const confirmacion = confirm('¿Estás seguro de que quieres eliminar el curso?');
            if (!confirmacion) {
                e.preventDefault();
            }
        });
    });
}
)();