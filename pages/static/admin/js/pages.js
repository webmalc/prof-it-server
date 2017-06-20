/*jslint browser: true*/
/*global $, admin*/
$(document).ready(function () {
    "use strict";
    admin.aceEditor($("#id_content, #id_content_ru"));

    $('a[href="#tab_id_content_en"]').click(function(){
        if (!$('#id_content_divid_content_en').length) {
            admin.aceEditor($("#id_content_en"));
        }
    });
});
