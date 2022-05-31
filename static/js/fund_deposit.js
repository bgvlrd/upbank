	
$('.holder').val(full_name);
$('.acctnumber').val(account_number);

$("#submit-button").click(function(){

	if ($('#amt').val() != '' && $('#amt').val() > 0){
		$(".error").addClass("d-none");
		$(".fill").addClass("d-none");
		$(".review").removeClass("d-none");
		var amt = $("#amt").val();

		$("#amt-review").text("PHP " + amt.toString());
	} else {
		$(".error").removeClass("d-none");
	}		
});


$("#fill-button").click(function(){
	if ($('#amt').val() != '' && $('#amt').val() > 0 && $("#loan-number :selected").val() > 0){
		$(".error").addClass("d-none");
		$(".fill").addClass("d-none");
		$(".review").removeClass("d-none");

		var loan = $("#loan-number :selected").text();
		console.log("LOAN:" + loan);
        var amt = $("#amt").val();

        $("#loan-number-review").text(loan.toString());
		$("#amt-review").text("PHP " + amt.toString());
	} else {
		$(".error").removeClass("d-none");
	}
});

$("#otc-fill-button").click(function(){
	if ($("#loan-number :selected").val() > 0){
		$(".error").addClass("d-none");
		$(".fill").addClass("d-none");
		$(".review").removeClass("d-none");

		var loan = $("#loan-number :selected").text();

        $("#loan-number-review").text(loan.toString());

        $.ajax({
            type: 'POST',
            url: otc_url,
            data: {
                loan_account_no: $("#loan-number :selected").text()
            },
            success:function(data){
                $(".review").addClass("d-none");
                $(".review").removeClass("d-none");
                $("#amt-review").text("PHP " + data["to_pay"]);
                $("#monthly-amortization-review").text("PHP " + data["monthly_amortization"]);
                $("#months-missed-review").text(data["months_missed"]);
            },
            error: function() {
                swal("Something's wrong.", "There is an error with the server. Try again later.", "error");
            }
        });

	} else {
		$(".error").removeClass("d-none");
	}
});

$("#back-button").click(function(){
	$(".review").addClass("d-none");
	$(".fill").removeClass("d-none");
});


$("#submit-final").click(function(e){
	e.preventDefault();

	$.ajax({
		type: 'POST',
		url: deposit_url,
		data: {
			amt: $("#amt").val()
		},
		success:function(data){
			$(".review").addClass("d-none");
			$(".success-submit").removeClass("d-none");
			$("#date-success").text(data["date"]);
			$("#time-success").text(data["time"]);
			$("#holder-success").text(data["full_name"]);
			$("#acctnumber-success").text(data["account_number"]);
			$("#amt-success").text("PHP " + data["amt_deposited"]);
			$("#balance-success").text("PHP " + data["balance"]);
		},
		error: function() {
			swal("Something's wrong.", "There is an error with the server. Try again later.", "error");
		}
	});
});

$("#otc-submit-final").click(function(e){
	e.preventDefault();

	$.ajax({
		type: 'POST',
		url: otc_url,
		data: {
			amt: $("#amt").val(),
			loan_account_no: $("#loan-number :selected").text()
		},
		success:function(data){
			$(".review").addClass("d-none");
			$(".success-submit").removeClass("d-none");
		},
		error: function() {
			swal("Something's wrong.", "There is an error with the server. Try again later.", "error");
		}
	});
});
