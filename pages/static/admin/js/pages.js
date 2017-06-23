/*jslint browser: true*/
/*global $, admin*/
$(document).ready(function () {
    "use strict";
    admin.aceEditor($("#id_content, #id_content_ru"));
    admin.aceEditorOnClick('a[href="#tab_id_content_en"]', 'id_content');
});
