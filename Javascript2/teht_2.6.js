'use strict';

/*
Palauttaa satunnaisen kokonaisluvun väliltä 1...6.
*/
function heita_noppaa()
{
    let luku = Math.floor(Math.random() * 6) + 1;
    return luku;
}

let luku;
do {
    luku = heita_noppaa();
     document.getElementById('luvut').innerHTML += `<li>${luku}</li>`;

}
while (luku !== 6);