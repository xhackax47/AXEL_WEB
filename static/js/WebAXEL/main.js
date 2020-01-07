// Confirmation suppression

$(document).on('click', '.confirm-delete', function () {
    $("#confirmDeleteDocumentModal").attr("caller-id", $(this).attr("id"));
});

$(document).on('click', '#confirmDeleteDocumentButtonModal', function () {
    var caller = $("#confirmDeleteDocumentButtonModal").closest(".modal").attr("caller-id");
    window.location = $("#".concat(caller)).attr("href");
});

