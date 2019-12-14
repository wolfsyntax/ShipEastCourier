$(document).ready(function(){
	
	feather.replace();
	
	$('.toast').toast('show');
	
	//$('#carousel-promo').carousel();
	
	$("#register_btn").attr('disabled','');
	/*$("#register_btn").on('click', function(){
		alert('Hey! Stop clicking me');
	});*/

	$("#is_agree").change(function(){//alert("Changin");
	    
	    if(this.checked){
	      $("#register_btn").removeAttr("disabled");
	    }else{
	      $("#register_btn").attr("disabled","disabled");
	    }

  	});

  	$('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
        $(this).toggleClass('active');
    });

	$('#upModal').modal();
});