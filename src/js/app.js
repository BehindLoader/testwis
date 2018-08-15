define([
    'text!template/main.html',
    'marionette',
], function(html, Mn) {
    'use strict';
    
    var View = Mn.View.extend({
        template: $(html).filter('#main-app-template')[0].outerHTML,
        el: '#app',
        rate: void(0),
        ui: {
            'in': '.in',
            'ok': '.ok',
            'result': '.result',
            'out': '.out',
            'nowRate': '.nowRate',
            'error': '.error',
        },
        events: {
            'change @ui.in': 'convert',
            'click @ui.ok': 'convert',
        },

        /** Конвертирует валлюту */
        convert: function() {
            var this_ = this;
            if (!$.isNumeric(this.ui.in.val())) {
                this_.getAlert();
                return;
            }
            if (!this.rate) {
                this.getRate();
            } else {
                if (this.ui.out.css('opacity') == 0) {
                    this.ui.out.animate({ opacity: 1 }, 500);
                }
                var value = this.ui.in.val();
                this.ui.nowRate.val(this.rate);
                this.ui.result.val(value * this.rate);
            }
        },

        /** Получает текущее значение курса валют */
        getRate: function() {
            var url = window.location.origin + '/api/rate?value=USD'
            var this_ = this;
            $.ajax({
                url: url,
                success: function(response) {
                    this_.rate = response.result.value;
                    this_.convert();
                },
            })
        },

        /** Показ окна ошибки */
        getAlert: function() {
            var this_ = this;
            this.ui.error.css({ display: 'block' });
            this.ui.error.animate({ opacity: 1 }, 500);
            setTimeout(function(){
                this_.ui.error.animate({ opacity: 0 }, 500);
                setTimeout(function() {
                    this_.ui.error.css({ display: 'none' });
                }, 1000);
            }, 1000);
        },
    });

    return View;
});