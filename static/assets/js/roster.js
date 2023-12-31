"use strict";

        $(document).ready(function() {
            var array = {{ array|tojson }};
            var trima = [];
            for (i = 0; i < array.length; i++) {
                trima.push(array[i].substring(10, ""));
            }
            $('#datepicker').datepicker({
                beforeShowDay: function(date) {
                    var string = jQuery.datepicker.formatDate('yy-mm-dd', date);
                    return [trima.indexOf(string) == -1];
                }
            });
        });

        $(document).ready(function() {
            $('.my-container').scrollbar();
        });
        
