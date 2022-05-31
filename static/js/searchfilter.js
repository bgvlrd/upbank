$(document).ready(function(){

    $("#nameFilter").on("keyup", function() {
        var value = $(this).val().toLowerCase();
        $("#tableSearch tr").filter(function() {
            $(this).toggle($(this).find("td:eq(1)").text().toLowerCase().indexOf(value) > -1)
        });
    });

    $("#amountFilter").on("change", function() {
        var amountFilter = $(this).val().toLowerCase();
        var amount1, amount2
        if (amountFilter == '≤ 1,000,000') {
            amount1 = 0
            amount2 = 1000000
        }else if (amountFilter == '1,000,000 to 5,000,000') {
            amount1 = 1000000
            amount2 = 5000000
        }else if (amountFilter == '≥ 5,000,000') {
            amount1 = 5000000
            amount2 = Number.MAX_SAFE_INTEGER
        }

        $("#tableSearch tr td:nth-child(3):visible").each( function() {
          var value = this.textContent.replace('$', '');
          console.log("amount1: " + amount1)
          console.log("amount2: " + amount2)
          console.log("row value: " + value)
          if (value >= amount1 && value <= amount2) {
            $(this).closest('tr').show();
          } else {
            $(this).closest('tr').hide();
          }
        })
   
    });

    // $("#tagFilter").on("change", function() {
    //     var value = $(this).val().toLowerCase();
    //     $("#tableSearch tr").filter(function() {
    //         $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
    //     });
    // });

    $("#tagFilter").on("change", function() {
        var value = $(this).val().toLowerCase();
        $("#tableSearch tr").filter(function() {
            $(this).toggle($(this).find("td:eq(4)").text().toLowerCase().indexOf(value) > -1)
        });
    });

});

