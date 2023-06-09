$(function() {
    // Получаем объект карусели
    var carousel = $('#product-carousel');

    // Отключаем автоматическое переключение карусели
    carousel.carousel({
        pause: false
    });

    // Обработчик для кнопки "назад"
    carousel.find('.carousel-control-prev').click(function() {
        carousel.carousel('prev');
    });

    // Обработчик для кнопки "вперед"
    carousel.find('.carousel-control-next').click(function() {
        carousel.carousel('next');
    });
});
