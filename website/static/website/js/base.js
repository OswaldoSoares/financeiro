function openMyModal(event) {
    var modal = initModalDialog(event, '#MyModal');
    var url = $(event.target).data('action');
    var id_selected = $(event.target).data('id-selected');
    $.ajax({
        type: "GET",
        url: url,
        data : {
            id_selected: id_selected
        }
    }).done(function(data) {
        $('.box-loader').hide()
        modal.find('.modal-body').html(data.html_modal);
        modal.modal('show');
        formAjaxSubmit(modal, url, null, null);
    })
}
