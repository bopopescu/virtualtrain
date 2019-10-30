function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
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
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});


$('#send').click(function() {

    

    let form = new FormData()
    var button = $(this)
    form.append('post', button.data('id'))
    form.append('username', $('#user').val())
    form.append('content',$('#cont').val())
    $.ajax({
        type: "POST",
        url:'',
        processData: false,
        contentType: false,
        data: form,
        success: function(data) {

            console.log(data)

            $('.comments').prepend(data.map(function (item) {

                console.log(item)

                return `


                <h1>${item.username}</h1>
                <h1>${item.content}</h1>
                <hr>


                                        `


            }))

            
        },
        error: function(xhr, errmsg, err) {

                console.log(xhr, errmsg, err);

            } // end error: function
    });




})
