PWeb.ajax = (function () {

    return {

        call: function (settings) {
            var defaults = {
                url: null,
                method: "POST",
                dataType: "json",
                afterComplete: null,
                beforeSubmit: null,
                success: null,
                beforeSend: undefined,
                complete: undefined,
                data: null,
                processData: true,
                contentType: 'application/x-www-form-urlencoded; charset=UTF-8'
            }

            if (settings) {
                jQuery.extend(defaults, settings);
            }

            jQuery.ajax({
                url: defaults.url,
                type: defaults.method,
                dataType: defaults.dataType,
                data: defaults.data,
                processData: defaults.processData,
                contentType: defaults.contentType,
                beforeSend: function () {
                    if (defaults.beforeSend !== undefined) {
                        defaults.beforeSend();
                    }
                },

                success: function (content) {
                    if (defaults.success) {
                        defaults.success(content);
                    }
                },

                complete: function () {
                    if (defaults.complete) {
                        defaults.complete();
                    }
                }
            });
        }
    }
}());