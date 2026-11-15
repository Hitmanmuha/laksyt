'use strict';

// Lue alku- ja loppuvuosi
let alku = parseInt(prompt("Anna alkuvuosi"));
let loppu = parseInt(prompt("Anna loppuvuosi"));

// etsitään elementti, johon vuosiluvut lisätään.
let lista = document.getElementById('lista');

// Käydään läpi jokainen vuosi v, väliltä alku....loppu.
for (let v = alku; v <= loppu; v += 1)
{
    // tutkitaan, onko vuosi v karkausvuosi
    if ((v % 4 === 0 && v % 100 !== 0) || (v % 400 === 0))
    {
        // v on karkausvuosi
        lista.innerHTML += `<li>${v}</li>`;
    }
}