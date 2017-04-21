(function ($) {
    $(document).ready(function () {
        $('.js-accordionButton').on('click', function () {
            $(this).toggleClass('active');
            $(this).siblings('.js-accordionContent').toggleClass('show');
        });
    });
})(jQuery);