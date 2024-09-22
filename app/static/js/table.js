function updateMaxValueOptions() {
    const mode = document.getElementById('mode').value;
    const maxValueWrapper = document.getElementById('maxValueWrapper');
    const maxValueSelect = document.getElementById('maxValue');

    // Очистка предыдущих опций
    while (maxValueSelect.firstChild) {
        maxValueSelect.removeChild(maxValueSelect.firstChild);
    }

    // Добавление новых опций в зависимости от выбранного режима
    if (mode === 'брат') {
        for (let i = 1; i <= 4; i++) {
            const option = document.createElement('option');
            option.value = i;
            option.textContent = i;
            maxValueSelect.appendChild(option);
        }
    } else if (mode === 'просто') {
        for (let i = 1; i <= 9; i++) {
            const option = document.createElement('option');
            option.value = i;
            option.textContent = i;
            maxValueSelect.appendChild(option);
        }
    }

    // Отображение или скрытие блока с выбором максимального значения
    maxValueWrapper.style.display = mode ? 'block' : 'none';
}
