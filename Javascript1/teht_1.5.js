'use strict';

// Luetaan syöte.
let v = parseInt(prompt("Anna vuosiluku"));

// Etsitään html-dokumentista kohta vastaukselle.
let vastaus = document.querySelector('#vastaus');

// Tutkitaan, onko karkausvuosi.
if ((v % 4 === 0 && v % 100 !== 0) || (v % 400 === 0))
{
    vastaus.innerHTML = "On karkausvuosi";
}
else
{
    vastaus.innerHTML = "Ei ole karkausvuosi";
}