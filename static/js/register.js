// if checkbox is changed, show div

$(function () {
    $("#relative_working").click(function () {
        if ($(this).is(":checked")) {
            $("#relative-name-div").show();
        } else {
            $("#relative-name-div").hide();
        }
    });
});