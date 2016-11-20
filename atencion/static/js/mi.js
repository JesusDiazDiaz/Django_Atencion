$(document).ready(function(){
    $('[data-toggle="tooltip"]').tooltip();

	
});

$('#fechaf').pickdate({
	format: 'yyyy-mm-dd'
});

$('#fechai').pickdate({
	format: 'yyyy-mm-dd',
	today: ''
});

$('#id_fecha_nacimiento').pickdate({
	format: 'yyyy-mm-dd',
	today: ''
});

$('#id_fecha_inicial').pickdate({
	format: 'yyyy-mm-dd',
	today: ''
});

$('#id_fecha_final').pickdate({
	format: 'yyyy-mm-dd'
});