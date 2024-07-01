$(document).ready(function() {
    $(".card-category-n1").hide()
    $(".card-category-n2-in").hide()
    $(".card-category-n2-out").hide()
    $(".card-category-n3-in").hide()
    $(".card-category-n3-out").hide()
});

$(document).on('click', '.js-mostra-itens', function() {
    var registry_id = $(this).data("registry-id")
    $.ajax({
        type: "GET",
        url: "view_registry_itens",
        data : {
            registry_id: registry_id
        },
        success: function(data) {
            $('.card-registry-itens').html(data["html_registry_itens"]);
            $('.card-registry-itens').show();
        },
    });   
});
