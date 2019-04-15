$(function() {

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
            }
        }
    }
    return cookieValue;
}
    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    function sameOrigin(url) {
        var host = document.location.host;
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        return (url === origin || url.slice(0, origin.length + 1) === origin + '/') ||
            (url === sr_origin || url.slice(0, sr_origin.length + 1) === sr_origin + '/') ||
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    $('#fav_form').on('submit', function(event){
        event.preventDefault();
        displayFavicon();
    });

    function successfulDisplay(json) {
        if (json.fav_image !== '') {
            $('#search_result').replaceWith("<img id=search_result " + "src=" + json.fav_image + " alt" + " style = width:30px; height:30px;>");
        } else {
            $('#search_result').replaceWith("<h4 id=search_result> Could not find Favicon. Maybe try a different URL?</h4>")
        }
    }

    function displayFavicon() {
        $.ajax({
            type: "POST",
            data: {fav_url: $('#fav-url').val(), checked: $('#get_fresh').is(':checked')},

            success: function(json) {
                $('#fav-url').val('');
                console.log(json);
                successfulDisplay(json)
            },

            error: function(xhr) {
                console.log(xhr.status);
                $('#search_result').replaceWith("<h4 id=search_result> There seems to be an issue (error code: " + xhr.status + ") </h4>")
            }
        });
    }
});