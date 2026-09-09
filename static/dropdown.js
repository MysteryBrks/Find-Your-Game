$(document).ready(function() {
    $('[name="genres"]').select2({
        placeholder: 'Search Genres',
        allowClear: true
    });
    $('[name="tags"]').select2({
        placeholder: 'Search Tags',
        allowClear: true
    });
});


