'use strict';

const maara = parseInt(prompt(`Kuinka monta noppaa heitetään?`));

let summa = 0;

for (let i = 0; i < maara; ++i)
{

    const luku = Math.floor(Math.random() * 6) + 1;
    summa = summa + luku;
}
document.querySelector('#vastaus').innerHTML = `Summa on ${summa}`;