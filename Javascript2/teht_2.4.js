'use strict';

const luvut = [];

let luku = parseInt(prompt('Anna luku (0 lopettaa)'));

while (luku !== 0)
{
    luvut.push(luku);
    luku = parseInt(prompt('Anna luku (0 lopettaa)'));

}

luvut.sort((a, b) => b - a);

console.log(luvut);