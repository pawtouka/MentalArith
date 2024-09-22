// Функция для изменения опций выпадающего списка "maximum" в зависимости от выбранного значения "topic"
function updateMaximumOptions() {
    var topic = document.getElementById("topic").value;
    var maximumSelect = document.getElementById("maximum");
    maximumSelect.innerHTML = "";  // Очистить текущие опции

    var options = [];
    if (topic === "просто") {
        options = [2, 3, 4, 5, 6, 7, 8, 9];
    } else if (topic === "брат") {
        options = [1, 2, 3, 4];
    }

    // Добавление новых опций в выпадающий список
    options.forEach(function(option) {
        var opt = document.createElement('option');
        opt.value = option;
        opt.innerHTML = option;
        maximumSelect.appendChild(opt);
    });
}

// Функция для отображения текущего значения ползунка "actions"
function updateActionValue() {
    var actionValue = document.getElementById("actions").value;
    document.getElementById("actionValue").innerText = actionValue;
}

// Инициализация значений при загрузке страницы
window.onload = function() {
    updateMaximumOptions();  // Устанавливаем опции для "maximum" по умолчанию
};