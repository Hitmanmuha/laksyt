'use strict';


const nimet = [];

for (let i = 0; i < 6; i++)
{
    const nimi = prompt( `Anna koiran ${i + 1} nimi`);
    nimet.push(nimi);

}

nimet.sort();
nimet.reverse();

const lista = document.querySelector('#lista');
for (let i = 0; i < nimet.length; i++)
{
    lista.innerHTML += `<li>${nimet[i]}</li>`;


}