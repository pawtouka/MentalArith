from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import ValidationError, StringField, PasswordField, FileField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, EqualTo, Length

from .functions import check_ava, save_picture
from .models.user import User


class RegistrationForm(FlaskForm):
    name = StringField('ФИО', validators=[DataRequired(), Length(min=2, max=100)])
    login = StringField('Логин', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Пароль', validators=[DataRequired()])
    confirm_password = PasswordField('Подтвердите пароль', validators=[DataRequired(), EqualTo('password')])
    avatar = FileField('Загрузите своё фото', validators=[FileAllowed(['jpg', 'jpeg', 'png'])])
    submit = SubmitField('Зарегистрироваться')

    def validate_login(self, login):
        user = User.query.filter_by(login=login.data).first()
        if user:
            raise ValidationError('Данное имя пользователя уже занято. Пожалуйста, выберите другое...')



class LoginForm(FlaskForm):
    """Form to log in users"""
    login = StringField('Логин', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')

class TeacherForm(FlaskForm):
    teacher = SelectField('teacher', choices=[], render_kw={'class':'form-control'})