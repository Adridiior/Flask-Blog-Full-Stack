function confirmDelete(message) {
    return confirm(message);
}

$(document).ready(function() {
    // Scroll to top button
    var scrollToTopBtn = $('.scroll-to-top');
    $(window).scroll(function() {
        if ($(window).scrollTop() > 300) {
            scrollToTopBtn.fadeIn();
        } else {
            scrollToTopBtn.fadeOut();
        }
    });

    scrollToTopBtn.click(function(e) {
        e.preventDefault();
        $('html, body').animate({scrollTop: 0}, '300');
    });
});
