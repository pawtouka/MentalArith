// Получаем элементы
    var modal = document.getElementById("helpModal");
    var btn = document.getElementById("helpButton");
    var span = document.getElementsByClassName("close")[0];

    // Открытие модального окна при нажатии на кнопку "Помощь"
    btn.onclick = function() {
        modal.style.display = "block";
        document.body.classList.add("modal-open"); // Блокировка прокрутки страницы
    }

    // Закрытие модального окна при нажатии на крестик
    span.onclick = function() {
        modal.style.display = "none";
        document.body.classList.remove("modal-open"); // Разблокировка прокрутки
    }

    // Закрытие модального окна при нажатии на любое место вне окна
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
            document.body.classList.remove("modal-open"); // Разблокировка прокрутки
        }
    }

    // Логика для кнопки "Повторить"
    document.getElementById('retryButton')?.addEventListener('click', () => {
        location.href = "{{ url_for('post.show_queue', random_hex=post.random_hex) }}";
    });