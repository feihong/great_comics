$(document).ready(function() {
    var renderContent = function(items) {
        $.each(items, function(i, item) {
            var $body = $(document.body);

            $body.append('<h2>' + item.head + '</h2>');
            $body.append('<img src="images/' + item.image + '">');
            $body.append('<p><a href="' + item.link + '">' + item.title + '</a></p>');
        });
    };

    var addNavigation = function() {
        // Add navigational elements:
        $('h2').each(function() {
            $(this).prev().after('<a class="next" href="#">&crarr;</a>');
        });
        $(document.body).click(function(evt) {
            var target = evt.target;
            if (target.tagName === 'A' && target.className === 'next') {
                evt.preventDefault();

                var y = $(target).next('h2').offset().top;

                window.scrollTo(0, y);
            }
        });
    };

    var setH2Margins = function() {
        var height = $(window).height();
        $('h2').css('margin-top', height+10);
    };

    // Load and render content
    $.ajax({
        url: 'great_comics.json',
        async: false,
        mimeType: 'application/json',
        success: renderContent
    });

    // Check to see if this is going to be a slideshow:
    var url = window.location.href;
    if (url.match(/#slideshow$/)) {
        setH2Margins();
        $(window).bind('resize'. setH2Margins);

        addNavigation();
    }
});
