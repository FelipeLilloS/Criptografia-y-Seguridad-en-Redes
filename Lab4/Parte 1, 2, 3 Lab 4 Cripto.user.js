// ==UserScript==
// @name     	Parte 1, 2, 3  Lab 4 Cripto
// @namespace	http://tampermonkey.net/
// @version  	0.1
// @description try to take over the world!.
// @author   	Felipe Lillo
// @match    	https://cripto.tiiny.site/
// @icon        https://www.google.com/s2/favicons?sz=64&domain=tiiny.site
// @require     https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.2.0/crypto-js.min.js#sha512-a+SUDuwNzXDvz4XrIcXHuCf089/iJAoN4lmrXJg18XnduKK6YlDHNRalv4yd1N40OKI80tFidF+rqTFKGPoWFQ==
// @require     https://code.jquery.com/jquery-3.6.0.min.js
// @grant    	none
// ==/UserScript==

(function() {
	'use strict';

    var mensajesBody = [];
    var idsDiv = [];

    function extraerPasswordDeP() {

    	var selector = 'p';
    	var elementosP = document.querySelectorAll(selector);                  	            // Busca y obtiene si existe el selector

    	if (elementosP.length > 0) {
        	var primerP = elementosP[0];                                       	            // Toma el primer elemento <p>
        	var textoP = primerP.textContent.trim();                           	            // Obtener el texto del elemento <p>

        	var simbolosMayusculas = textoP.split('').filter(function(caracter) {
                return caracter === caracter.toUpperCase() && caracter.match(/[A-Z]/);      // Almacenar key en una variable
        	}).join('');

        	console.log('La llave es:', simbolosMayusculas);
            return simbolosMayusculas;
    	} else {
        	console.log('No existen elementos <p>.');
            return 0;
    	}

	}


	function obtenerIDsYContarDivs() {

    	var selectorDiv = 'div';
    	var elementosDiv = document.querySelectorAll(selectorDiv);                          // Toma el los campos div.

    	elementosDiv.forEach(function(div) {
        	if (div.id) {
            	idsDiv.push(div.id);                                                        // Añade la informacion contenida en el atributo "i" en un arreglo.
        	}
    	});

    	var cantidadDivs = elementosDiv.length;

    	console.log('Los mensajes cifrados son:', cantidadDivs);

    	return {
        	idsDiv: idsDiv,
        	cantidadDivs: cantidadDivs
    	};
	}


    function descifrarMensajes(texto) {

        /* Importar y agregar libreria CryptoJS */
        var scriptElement = document.createElement('script');
        scriptElement.src = 'https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.2.0/crypto-js.min.js';

        /* Seccion SRI */
        scriptElement.integrity = 'sha256-dppVXeVTurw1ozOPNE3XqhYmDJPOosfbKQcHyQSE58w==';
        scriptElement.crossOrigin = 'anonymous';
        scriptElement.type = 'text/javascript';

        document.body.appendChild(scriptElement);

        var llave = CryptoJS.enc.Utf8.parse(texto);

        var tripleDESConfig = { mode: CryptoJS.mode.ECB };

        var divElements = document.getElementsByTagName("div");

        for (var i = 0; i < divElements.length; i++) {
            var divId = divElements[i].id;

            var descifrado = CryptoJS.TripleDES.decrypt(divId, llave, tripleDESConfig).toString(CryptoJS.enc.Utf8);
            mensajesBody.push(descifrado);

            var mensaje = divId + ' ' + descifrado;
            console.log(mensaje);
        }

    }


    function agregarMensajes() {

        for(var i = 0;i < mensajesBody.length;i++) {
            var addDiv = document.createElement('p');

            addDiv.textContent = mensajesBody[i];
            document.body.appendChild(addDiv);
        }

    }

    function probarConOtraInfo() {

        var elementosP = document.querySelectorAll('p');

        elementosP.forEach(function(p) { // Elimina los campos <p>
            p.remove();
        });

    	var elementosDiv = document.querySelectorAll('div');

    	elementosDiv.forEach(function(div) { // Elimina los campos <div>
            div.remove();
    	});


        var nuevoT = document.createElement('p');

        nuevoT.textContent =
            'Claramente llevo más de 3 intentos en lo que es la realización de esta parte de la experiencia.' +
            'Inesperadamente, sigo sin lograr con un texto que me sirva para la actividad.' +
            'Espero que logre de alguna manera encontrar lo correcto.' +
            'Lo que creo que va a pasar es que probablemente destine un tiempo para jugar porque es merecido descanso.' +
            'Obviamente, como alumno totalmente responsable, se destina tiempo para descansar, y jugar porque la vida es una sola y hay que aprovecharla.' +
            'Si, tengo bastante fe de que este texto servirá, confío plenamente.'

        var textoFull = nuevoT.textContent.repeat(4);
        nuevoT.textContent = textoFull;

        document.body.appendChild(nuevoT);


        var mCifrados = ['sWguGV3Gk0E=','agEXea1zV/Q=','6Z2CYg6ES/o='];

        console.log(mCifrados.length);

        for (var i = 0; i < mCifrados.length; i++) {
            var nuevoDiv = document.createElement('div');
            nuevoDiv.id = mCifrados[i];
            nuevoDiv.className = 'm' + i.toString();
            document.body.appendChild(nuevoDiv);
        }

    }

    var textoP = extraerPasswordDeP();

    obtenerIDsYContarDivs();

    descifrarMensajes(textoP);

    agregarMensajes();

    // -----------------------//
    // Como recomendacion, lo ideal es comentar lo de arriba (que son las que se usan para el caso inicial), y luego descomentar las que vienen abajo de este comentario.

    // probarConOtraInfo();

    // svar textoP2 = extraerPasswordDeP();
    // obtenerIDsYContarDivs();
    // descifrarMensajes(textoP2);
    // agregarMensajes();


})();