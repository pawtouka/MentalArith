import random

from flask import Blueprint, render_template, request, redirect, abort, flash, url_for, session
from flask_login import login_required, current_user

from ..extensions import db

flast = Blueprint('flast', __name__)

# Глобальные переменные для хранения диапазона
lower_bound = 1
upper_bound = 100


@flast.route('/flas', methods=['GET'])
@login_required
def flas():
    return render_template('flast/flas.html')



@flast.route('/flas/task1', methods=['GET', 'POST'])
@login_required
def task1():
    random_number = session.get('random_number', None)

    if random_number is None:
        # Генерация случайного числа в диапазоне 1-9
        random_number = random.randint(1, 9)
        session['random_number'] = random_number

    # Преобразуем число в строку и разбиваем на отдельные цифры
    number_str = str(random_number)
    number_images = [f'{digit}.png' for digit in number_str]

    if request.method == 'POST':
        action = request.form.get('action')

        if action == 'check':
            user_input = request.form.get('user_input')
            if user_input == number_str:
                flash('Вы правильно ввели число!', 'success')
                random_number = random.randint(1, 9)
                session['random_number'] = random_number
                return redirect(url_for('flast.task1'))
            else:
                flash('Неправильный ответ, попробуйте снова.', 'danger')

        elif action == 'next':
            random_number = random.randint(1, 9)
            session['random_number'] = random_number
            return redirect(url_for('flast.task1'))

    return render_template('flast/task1.html', number_images=number_images)

@flast.route('/flas/task2', methods=['GET', 'POST'])
@login_required
def task2():
    random_number = session.get('random_number', None)

    if random_number is None:
        random_number = random.randint(10, 99)
        session['random_number'] = random_number

    number_str = str(random_number)
    number_images = [f'{digit}.png' for digit in number_str]

    if request.method == 'POST':
        action = request.form.get('action')

        if action == 'check':
            user_input = request.form.get('user_input')
            if user_input == number_str:
                flash('Вы правильно ввели число!', 'success')
                random_number = random.randint(10, 99)
                session['random_number'] = random_number
                return redirect(url_for('flast.task2'))
            else:
                flash('Неправильный ответ, попробуйте снова.', 'danger')

        elif action == 'next':
            random_number = random.randint(10, 99)
            session['random_number'] = random_number
            return redirect(url_for('flast.task2'))

    return render_template('flast/task2.html', number_images=number_images)

@flast.route('/flas/task3', methods=['GET', 'POST'])
@login_required
def task3():
    random_number = session.get('random_number', None)

    if random_number is None:
        random_number = random.randint(100, 999)
        session['random_number'] = random_number

    number_str = str(random_number)
    number_images = [f'{digit}.png' for digit in number_str]

    if request.method == 'POST':
        action = request.form.get('action')

        if action == 'check':
            user_input = request.form.get('user_input')
            if user_input == number_str:
                flash('Вы правильно ввели число!', 'success')
                random_number = random.randint(100, 999)
                session['random_number'] = random_number
                return redirect(url_for('flast.task3'))
            else:
                flash('Неправильный ответ, попробуйте снова.', 'danger')

        elif action == 'next':
            random_number = random.randint(100, 999)
            session['random_number'] = random_number
            return redirect(url_for('flast.task3'))

    return render_template('flast/task3.html', number_images=number_images)

