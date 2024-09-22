// Находим все кнопки и текущий элемент для отображения значения
const buttons = document.querySelectorAll('.toggle-button');
const currentValueDisplay = document.getElementById('currentValue');
let currentValue = 1;

// Добавляем обработчик событий на каждую кнопку
buttons.forEach(button => {
    button.addEventListener('click', function() {
        // Убираем активный класс у всех кнопок
        buttons.forEach(btn => btn.classList.remove('active'));

        // Добавляем активный класс для нажатой кнопки
        this.classList.add('active');

        // Обновляем текущее значение
        currentValue = this.getAttribute('data-value');
        currentValueDisplay.innerText = currentValue;
    });
});
