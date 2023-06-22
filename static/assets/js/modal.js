const modal = document.querySelector('[data-modal]')


if(modal){
    modal.showModal()

    modal.addEventListener('click', (evento) => {
        if(evento.target === modal)
            modal.close()
    })
}