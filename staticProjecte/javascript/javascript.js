/**
 * @author Rodrigo Saulis
 */


function getData(){
	var data = new Date();
	var hora;
	var dia;
	hora = data.getHours() + ":" + data.getMinutes() + ":" + data.getSeconds();
	dia = data.getDate() + "/" + (data.getMonth() + 1) + "/" + data.getFullYear();
	document.getElementById("dia").innerHTML = '<span class="glyphicon glyphicon-calendar"></span> ' + dia;
	document.getElementById("hora").innerHTML = '<span class="glyphicon glyphicon-time"></span> ' + hora;
}

setInterval(getData, 1000);
