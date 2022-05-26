$(document).ready(function(){
    $("#nameFilter").on("keyup", function() {
        var value = $(this).val().toLowerCase();
        $("#tableSearch tr").filter(function() {
        $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        });
    });
});

$(document).ready(function(){
    $("#tagFilter").on("change", function() {
        var value = $(this).val().toLowerCase();
        $("#tableSearch tr").filter(function() {
        $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        });
    });
});

$(document).ready(function(){
    $("#amountFilter").on("change", function() {
        var value = $(this).val().toLowerCase();
        var loan_tag = $("#tagFilter").val();
        if (value == 'less 1,000,000') {
            var amount1 = 0
            var amount2 = 1000000
        }
        if (value == '2,000,000 to 5,000,000') {
            var amount1 = 2000000
            var amount2 = 5000000
        }
        if (value == 'more 5,000,000') {
            var amount1 = 5000000
            var amount2 = Number.MAX_SAFE_INTEGER
        }
        var table = document.getElementById("myTable")

        for (var i = 1, row; row = table.rows[i]; i++) {
           //iterate through rows (we SKIP the first row: counter starts at 1!)
              for (var j = 0, col; col = row.cells[j]; j++) {

                   if (j == 2) {    
                       var curr_loan_tag = row.cells[4].innerText 
                       if (loan_tag = "Loan Tag") {
                            if (parseInt($(col).html().replace(/,/g, '')) >= amount1 && parseInt($(col).html().replace(/,/g, '')) <= amount2) {
                                $(row).show();
                            }
                            else {
                                $(row).hide();
                            }
                           
                       } 
                       else if (parseInt($(col).html().replace(/,/g, '')) >= amount1 && parseInt($(col).html().replace(/,/g, '')) <= amount2) {
                           $(row).show();
                       } 
                       else {
                           $(row).hide();
                       }
                }
               }  
        }   
    });
});