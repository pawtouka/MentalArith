from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user

from ..functions import save_picture, check_ava
from ..forms import RegistrationForm, LoginForm
from ..extensions import db, bcrypt
from ..models.user import User

user = Blueprint('user', __name__)


@user.route('/user/register', methods=['POST', 'GET'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        # Получаем статус из скрытого поля формы
        status = request.form.get('status', 'student')  # По умолчанию 'student'

        existing_user = User.query.filter_by(login=form.login.data).first()
        if existing_user:
            flash(f"Логин {form.login.data} уже занят. Пожалуйста, выберите другой логин.", "danger")
            return redirect(url_for('user.register'))

        # Хешируем пароль
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

        # Сохраняем аватар и проверяем его формат
        avatar_filename = save_picture(form.avatar.data)
        if check_ava(avatar_filename) == 0:
            flash(
                "Выбран неверный формат аватара. Доступные форматы PNG, JPEG, JPG. Пожалуйста, выберите другой аватар.",
                "danger")
            return redirect(url_for('user.register'))

        # Создаем нового пользователя
        user = User(name=form.name.data, login=form.login.data, avatar=avatar_filename, password=hashed_password,
                    status=status)

        try:
            db.session.add(user)
            db.session.commit()
            flash(f"Поздравляем, {form.login.data}! Вы успешно зарегистрированы.", "success")
            return redirect(url_for('user.login'))
        except Exception as e:
            print(str(e))
            flash("При регистрации произошла ошибка. Пожалуйста, попробуйте еще раз.", "danger")
            return redirect(url_for('user.register'))

    # Если форма не прошла валидацию
    for field, errors in form.errors.items():
        for error in errors:
            flash(f"Ошибка в поле {getattr(form, field).label.text}: {error}", "danger")

    return render_template('user/register.html', form=form)


@user.route('/user/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(login=form.login.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            flash(f"Поздравляем, {form.login.data}! Вы успешно авторизованы", "success")
            return redirect(next_page) if next_page else redirect(url_for('post.all'))
        else:
            flash(f"Ошибка входа. Пожалуйста проверьте логин и пароль!", "danger")
    return render_template('user/login.html', form=form)

@user.route('/user/logout')
def logout():
    logout_user()
    return redirect('/')