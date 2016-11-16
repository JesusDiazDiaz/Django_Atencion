$(document).ready(function(){
    $('[data-toggle="tooltip"]').tooltip();

	
});
/*
$(document).ready(function(){
    $('$fechaf').bootstrapMaterialDatePicker({ weekStart : 0, time: false });
});

*/
$('#fechaf').pickdate({
	format: 'yyyy-mm-dd'
});

$('#fechai').pickdate({
	format: 'yyyy-mm-dd',
	today: ''
});
