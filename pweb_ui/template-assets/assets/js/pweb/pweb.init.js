jQuery(document).ready(function () {
    jQuery('.delete-confirmation').confirm({
        title: 'Confirmation!',
        content: 'Are you sure want to delete?'
    });

    jQuery('.cancel-confirmation').confirm({
        title: 'Confirmation!',
        content: 'Are you sure want to cancel?'
    });

    let dateFormat = "dd/MM/yyyy"
    if (PWeb.dateFormat) {
        dateFormat = PWeb.dateFormat
    }

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
            format: dateFormat,
        }
    });

    let dateTimeFormat = "dd/MM/yyyy HH:mm"
    if (PWeb.dateTimeFormat) {
        dateTimeFormat = PWeb.dateTimeFormat
    }
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
            format: dateTimeFormat,
        }
    });

    jQuery('.searchable-select').select2({
        theme: "bootstrap-5",
    });
});