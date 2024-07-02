$(document).ready(function(){
    $('#datepicker').datepicker({
        format: "mm/yyyy",
        startView: "months",
        minViewMode: "months",
        autoclose: true,
        language: 'pt-BR',
        inline: true
    }).on('changeDate', function(e) {
        var selectedDate = e.format('mm/yyyy');
        document.getElementById("menu-transactions").href = '/transactions/?date=' + selectedDate
    })
})

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

function initModalDialog(event, modal_element) {
    var modal = $(modal_element);
    var target = $(event.target);
    var title = target.data('title') || '';
    var subtitle = target.data('subtitle') || '';
    var dialog_class = (target.data('dialog-class') || '') + ' modal-dialog';
    var icon_class = (target.data('icon') || 'fa-laptop') + ' fa modal-icon';
    var button_save_label = target.data('button-save-label') || 'Save changes';
    modal.find('.modal-dialog').attr('class', dialog_class);
    modal.find('.modal-title').text(title);
    modal.find('.modal-subtitle').text(subtitle);
    modal.find('.modal-header .title-wrapper i').attr('class', icon_class);
    modal.find('.modal-footer .btn-save').text(button_save_label);
    modal.find('.modal-body').html('');
    modal.data('target', target);
    return modal;
}

function formAjaxSubmit(modal, action, cbAfterLoad, cbAfterSuccess) {
    var form = modal.find('.modal-body form');
    var header = $(modal).find('.modal-header');
    var btn_save = modal.find('.modal-footer .btn-save');
    if (btn_save) {
        modal.find('.modal-body form .form-submit-row').hide();
        btn_save.off().on('click', function() {
            modal.find('.modal-body form').submit();
        });
    }
    if (cbAfterLoad) { cbAfterLoad(modal); }
    modal.find('form input:visible').first().focus();
    $(form).on('submit', function(event) {
        event.preventDefault();
        header.addClass('loading');
        var url = $(this).attr('action') || action;
        var formData = new FormData($('.rows').get(0));  
        $.ajax({
            type: $(this).attr('method'),
            url: url,
            formData: formData,
            data: $(this).serialize(),
            beforeSend: function() {
                $(".box-loader").show()
                $(".card-registries-unpaid").hide()
            },
            success: function(xhr) {
                $(modal).find('.modal-body').html(xhr['html_form']);
                if ($(xhr['html_form']).find('.errorlist').length > 0) {
                    formAjaxSubmit(modal, url, cbAfterLoad, cbAfterSuccess);
                } else {
                    $(modal).modal('hide');
                    if (xhr["html_registries_unpaid"]) {
                        $(".card-registries-unpaid").html(xhr["html_registries_unpaid"])
                        $(".card-registries-unpaid").show()
                    }
                    if (xhr["html_registry_itens"]) {
                        $(".card-registries-unpaid").show()
                        $(".card-registry-itens").html(xhr["html_registry_itens"])
                        $(".card-registry-itens").show()
                    }
                    if (cbAfterSuccess) { 
                        cbAfterSuccess(modal);
                    }
                }
                $('.box-loader').hide()
            },
            complete: function() {
                header.removeClass('loading');
            }
        });
    });
}
