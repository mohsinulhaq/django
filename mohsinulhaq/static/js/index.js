$(function () {
    $('.form').submit(function (e) {
        e.preventDefault();
        var searchBox = $('.search-box').val().trim();
        $('.loading').show();
        $.getJSON('https://api.github.com/users/' + searchBox, function (data) {
            $('.image').attr({
                src: data.avatar_url,
                height: '150px',
                width: '150px'
            });
            $('.name').text(data.name);
            $('.profile').attr('href', data.html_url).text('Click here');
            $('.id').text(data.id);
            $('.followers').text(data.followers);
            $('.repos').text(data.public_repos);
            $('.loading').hide();
            $('.result').modal('show');
        });
    });
});
