$(document).ready(function() {
    $('[name="genres"]').select2({
        placeholder: 'Search Genre (Optional)',
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
});


