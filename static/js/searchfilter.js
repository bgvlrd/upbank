$(document).ready(function(){

    $("#nameFilter").on("keyup", function() {
        filterTable()
    });

    $("#amountFilter").on("change", function() {
        filterTable()
    });

    $("#tagFilter").on("change", function() {
        filterTable()
    });

    $("#reset_btn").click( function() {
        $("#nameFilter").val("")
        $("#tagFilter").val("")
        $("#amountFilter").val("")
        $("#tableSearch tr").show()
    })

});

function filterTable() {
    // filter by name
    if ($("#nameFilter").val() != null){
        var value = $("#nameFilter").val().toLowerCase();
        $("#tableSearch tr").filter(function() {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
        });
    }

    // filter by amount
    if ($("#amountFilter").val() != null){
        var amountFilter = $("#amountFilter").val().toLowerCase();
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
          var amount = this.textContent.replace('$', '');
          if (amount >= amount1 && amount <= amount2) {
            $(this).closest('tr').show();
          } else {
            $(this).closest('tr').hide();
          }
        })
    }

    // filter by tag 
    if ($("#tagFilter").val() != null){
        var tag = $("#tagFilter").val().toLowerCase();
        $("#tableSearch tr:visible").filter(function() {
            $(this).toggle($(this).text().toLowerCase().indexOf(tag) > -1)
        });
    }

}