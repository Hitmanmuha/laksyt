'use strict';

const maara = parseInt(prompt('Kuinka monta osallistujaa?'));
const nimet = [];

for (let i = 0; i < maara; i++)
{
    const nimi = prompt( `Anna osallistujan ${i + 1} nimi`);
    nimet.push(nimi);

}

nimet.sort();

const lista = document.querySelector('#lista');
for (let i = 0; i < nimet.length; i++)
{
    lista.innerHTML += `<li>${nimet[i]}</li>`;


}