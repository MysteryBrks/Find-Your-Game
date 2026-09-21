$(document).ready(function() {
    $('[name="genres"]').select2({
        placeholder: 'Search Genres (Optional)',
        allowClear: true
    });
    $('[name="tags"]').select2({
        placeholder: 'Search Tags (min: 1)',
        allowClear: true
    });
    $('[name="excludeds"]').select2({
        placeholder: 'Exclude Tags (Optional)',
        allowClear: true
    });

    // Limits checkbox to only one option
    $('input[type="checkbox"]').on('change', function() {
        $('input[name="' + this.name + '"]').not(this).prop('checked', false);
    });
});


