jQuery(document).ready(function () {
    jQuery('.delete-confirmation').confirm({
        title: 'Confirmation!',
        content: 'Are you sure want to delete?'
    });

    jQuery('.cancel-confirmation').confirm({
        title: 'Confirmation!',
        content: 'Are you sure want to cancel?'
    });

    jQuery('.add-datepicker').tempusDominus({
        allowInputToggle: true,
        display: {
            components: {
                clock: false,
                hours: false,
                minutes: false,
                seconds: false,
            },
        },
        localization: {
            format: 'dd/MM/yyyy',
        }
    });

    jQuery('.add-date-time-picker').tempusDominus({
        allowInputToggle: true,
        display: {
            components: {
                clock: true,
                hours: true,
                minutes: true,
                seconds: true,
            },
        },
        localization: {
            format: 'dd/MM/yyyy HH:mm',
        }
    });

    jQuery('.searchable-select').select2({
        theme: "bootstrap-5",
    });
});