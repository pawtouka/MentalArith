import random

from flask import Blueprint, render_template, request, redirect, abort, flash, url_for, session
from flask_login import login_required, current_user

from ..extensions import db

flast = Blueprint('flast', __name__)

# Глобальные переменные для хранения диапазона
lower_bound = 1
upper_bound = 100


@flast.route('/flas', methods=['GET', 'POST'])
@login_required
def flas():
    if request.method == 'POST':
        range_value = request.form.get('range')

        range_value = request.form.get('range')

        if range_value == '1':
            # Перенаправление на task1
            random_number = random.randint(1, 9)
            return redirect(url_for('flast.task1', number=random_number))
        elif range_value == '2':
            # Перенаправление на task2
            random_number = random.randint(10, 99)
            return redirect(url_for('flast.task2', number=random_number))
        elif range_value == '3':
            # Перенаправление на task3
            random_number = random.randint(100, 999)
            return redirect(url_for('flast.task3', number=random_number))

    return render_template('flast/flas.html')


@flast.route('/flas/task1', methods=['GET', 'POST'])
@login_required
def task1():
    # Получаем сгенерированное число из сессии
    random_number = session.get('random_number', None)

    if random_number is None:
        return redirect(url_for('flast.flas'))

    # Преобразуем число в строку и разбиваем на отдельные цифры
    number_str = str(random_number)
    number_images = [f'{digit}.png' for digit in number_str]  # Преобразуем цифры в названия файлов

    if request.method == 'POST':
        action = request.form.get('action')

        if action == 'check':  # Если нажата кнопка "Проверить"
            user_input = request.form.get('user_input')
            if user_input == number_str:
                flash('Вы правильно ввели число!', 'success')
                # Генерация нового числа при правильном ответе
                lower_bound, upper_bound = 1, 9  # Замените на логику по выбору диапазона
                random_number = random.randint(lower_bound, upper_bound)
                session['random_number'] = random_number
                return redirect(url_for('flast.task1'))  # Перезагружаем страницу с новым числом
            else:
                flash('Неправильный ответ, попробуйте снова.', 'danger')

        elif action == 'next':  # Если нажата кнопка "Далее"
            # Генерация нового числа без проверки ответа
            lower_bound, upper_bound = 1, 9  # Замените на логику по выбору диапазона
            random_number = random.randint(lower_bound, upper_bound)
            session['random_number'] = random_number
            return redirect(url_for('flast.task1'))  # Перезагружаем страницу с новым числом

    return render_template('flast/task1.html', number_images=number_images)

@flast.route('/flas/task3', methods=['GET', 'POST'])
@login_required
def task3():
    # Получаем сгенерированное число из сессии
    random_number = session.get('random_number', None)

    if random_number is None:
        return redirect(url_for('flast.flas'))

    # Преобразуем число в строку и разбиваем на отдельные цифры
    number_str = str(random_number)
    number_images = [f'{digit}.png' for digit in number_str]  # Преобразуем цифры в названия файлов

    if request.method == 'POST':
        action = request.form.get('action')

        if action == 'check':  # Если нажата кнопка "Проверить"
            user_input = request.form.get('user_input')
            if user_input == number_str:
                flash('Вы правильно ввели число!', 'success')
                # Генерация нового числа при правильном ответе
                lower_bound, upper_bound = 100, 999  # Замените на логику по выбору диапазона
                random_number = random.randint(lower_bound, upper_bound)
                session['random_number'] = random_number
                return redirect(url_for('flast.task3'))  # Перезагружаем страницу с новым числом
            else:
                flash('Неправильный ответ, попробуйте снова.', 'danger')

        elif action == 'next':  # Если нажата кнопка "Далее"
            # Генерация нового числа без проверки ответа
            lower_bound, upper_bound = 100, 999  # Замените на логику по выбору диапазона
            random_number = random.randint(lower_bound, upper_bound)
            session['random_number'] = random_number
            return redirect(url_for('flast.task3'))  # Перезагружаем страницу с новым числом

    return render_template('flast/task3.html', number_images=number_images)

@flast.route('/flas/task2', methods=['GET', 'POST'])
@login_required
def task2():
    # Получаем сгенерированное число из сессии
    random_number = session.get('random_number', None)

    if random_number is None:
        return redirect(url_for('flast.flas'))

    # Преобразуем число в строку и разбиваем на отдельные цифры
    number_str = str(random_number)
    number_images = [f'{digit}.png' for digit in number_str]  # Преобразуем цифры в названия файлов

    if request.method == 'POST':
        action = request.form.get('action')

        if action == 'check':  # Если нажата кнопка "Проверить"
            user_input = request.form.get('user_input')
            if user_input == number_str:
                flash('Вы правильно ввели число!', 'success')
                # Генерация нового числа при правильном ответе
                lower_bound, upper_bound = 10, 99  # Замените на логику по выбору диапазона
                random_number = random.randint(lower_bound, upper_bound)
                session['random_number'] = random_number
                return redirect(url_for('flast.task2'))  # Перезагружаем страницу с новым числом
            else:
                flash('Неправильный ответ, попробуйте снова.', 'danger')

        elif action == 'next':  # Если нажата кнопка "Далее"
            # Генерация нового числа без проверки ответа
            lower_bound, upper_bound = 10, 99  # Замените на логику по выбору диапазона
            random_number = random.randint(lower_bound, upper_bound)
            session['random_number'] = random_number
            return redirect(url_for('flast.task2'))  # Перезагружаем страницу с новым числом

    return render_template('flast/task2.html', number_images=number_images)
