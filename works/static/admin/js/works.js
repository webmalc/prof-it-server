/*jslint browser: true*/
/*global $, admin*/
$(document).ready(function () {
    "use strict";
    admin.aceEditor($("#id_description_ru, #id_description"));
    admin.aceEditorOnClick('a[href="#tab_id_description_en"]', 'id_description');
});
