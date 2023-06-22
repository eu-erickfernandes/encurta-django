const menu = document.querySelector('[data-menu]')
const menuBotao = document.querySelector('[data-menu-botao]')

menuBotao.addEventListener('click', () => {
    menu.classList.toggle('oculto')
})

window.addEventListener('click', (evento) => {
    if(!evento.target.matches('[data-menu]') && !evento.target.matches('[data-menu-botao]'))
        menu.classList.add('oculto')
})