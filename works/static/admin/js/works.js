/*jslint browser: true*/
/*global $, admin*/
$(document).ready(function () {
    "use strict";
    admin.aceEditor($("#id_description_ru, #id_description"));
    admin.aceEditorOnClick('a[href="#tab_id_description_en"]', 'id_description');
    admin.aceEditor($("#id_content_ru, #id_content"));
    admin.aceEditorOnClick('a[href="#tab_id_content_en"]', 'id_content');
});
