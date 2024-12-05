// current year

let currentDate = new Date();
let currentYear = currentDate.getFullYear();

const currentYearElement = document.getElementById('currentYear');

currentYearElement.textContent = currentYear;

setTimeout(
    () => {
        $(".messages").fadeOut("slow");
    }, 60000
)

$(document).ready(function () {
    //console.log("It's working")
    $('.like-form').submit(function (e) {
        e.preventDefault();

        const eventId = $('.like-btn').val();
        const token = $('input[name=csrfmiddlewaretoken]').val();
        const url = $(this).attr('action');

        $.ajax({
            method: "POST",
            url: url,
            header: { 'X-CSRFToken': token },
            data: {
                'eventId': eventId
            },
            success: function (response) {
                //console.log(response);
                if (response.liked === true) {
                    $('#like-icon').removeClass('bi-hand-thumbs-up');
                    $('#like-icon').addClass('bi-hand-thumbs-up-fill');
                } else {
                    $('#like-icon').removeClass('bi-hand-thumbs-up-fill');
                    $('#like-icon').addClass('bi-hand-thumbs-up');
                }

                $('#like-count').text(response.likes_count);
            },
            error: function (response) {
                console.log('failed ', response)
            }
        })

    })

    $('.dislike-form').submit(function (e) {
        e.preventDefault();

        const eventId = $('.dislike-btn').val();
        const token = $('input[name=csrfmiddlewaretoken]').val();
        const url = $(this).attr('action');

        $.ajax({
            method: "POST",
            url: url,
            header: { 'X-CSRFToken': token },
            data: {
                'eventId': eventId
            },
            success: function (response) {
                //console.log(response);
                if (response.disliked === true) {
                    $('#dislike-icon').removeClass('bi-hand-thumbs-down');
                    $('#dislike-icon').addClass('bi-hand-thumbs-down-fill');
                } else {
                    $('#dislike-icon').removeClass('bi-hand-thumbs-down-fill');
                    $('#dislike-icon').addClass('bi-hand-thumbs-down');
                }

                $('#dislike-count').text(response.dislikes_count);
            },
            error: function (response) {
                console.log('failed ', response)
            }
        })

    })
})