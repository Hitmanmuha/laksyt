'use strict';

const nimi =prompt('Anna nimesi');

const vastaus = document.querySelector('#vastaus');

vastaus.innerHTML = `Hello, ${nimi}!`;