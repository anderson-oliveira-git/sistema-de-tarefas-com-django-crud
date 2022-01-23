const counter = document.querySelector('.counter');
const text_area = document.querySelector('#text_area');
const btn_limpar = document.querySelector('#limpar');

text_area.addEventListener('input', (event) => {
    let qtd_letras = text_area.value.toString();

    if (event.keyCode === 8) {
        counter.innerHTML = parseInt(qtd_letras.length);
    } else {
         counter.innerHTML = parseInt(qtd_letras.length);
    }
});

btn_limpar.addEventListener('click', () => {
    contador = 0;
    counter.innerHTML = contador.toString();
    text_area.value = "";
});