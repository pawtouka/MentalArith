from flask import Blueprint, render_template, request, redirect, abort, flash, url_for
from flask_login import login_required, current_user

from ..forms import TeacherForm
from ..models.user import User
from ..extensions import db
from ..models.post import Post

post = Blueprint('post', __name__)

@post.route('/')
def all():
    return render_template('post/head.html')

@post.route('/post')
def posters():
    form = TeacherForm()
    form.teacher.choices = [t.name for t in User.query.filter_by(status='teacher')]

    if request.method == "POST":
        teacher = request.form.get('teacher')
        teacher_id = User.query.filter_by(name=teacher).first().id
        posts = Post.query.filter_by(teacher=teacher_id).order_by(Post.date.desc()).all()
    else:
        posts = Post.query.order_by(Post.date.desc()).limit(20).all()
    return render_template('post/all.html', posts=posts, user=User, form=form)


@post.route('/post/create', methods=['POST', 'GET'])
@login_required
def create():
    if request.method == 'POST':
        topic = request.form.get('topic')
        maximum = request.form.get('maximum')
        actions = request.form.get('actions')
        dignits = request.form.get('dignits')

        post = Post(teacher=current_user.id, topic=topic, maximum=maximum, actions=actions, dignits=dignits)

        try:
            db.session.add(post)
            db.session.commit()
            return redirect('/post')
        except Exception as e:
            print(str(e))
    else:
        pass
    return render_template('post/create.html')

# @post.route('/post/<int:id>/update', methods=['POST', 'GET'])
# @login_required
# def update(id):
#     post = Post.query.get(id)
#     if request.method == 'POST':
#         post.teacher = request.form['teacher']
#         post.subject = request.form['subject']
#         post.student = request.form['student']
#
#         try:
#             db.session.commit()
#             return redirect('/')
#         except Exception as e:
#             print(str(e))
#     else:
#         return render_template('post/update.html', post=post)

@post.route('/post/<int:id>/delete', methods=['POST', 'GET'])
@login_required
def delete(id):
    post = Post.query.get(id)

    if post.author.id == current_user.id:
        try:
            db.session.delete(post)
            db.session.commit()
            return redirect('/post')
        except Exception as e:
            print(str(e))
            return (str(e))
    else:
        abort(403)



@post.route('/post/<string:random_hex>/show_queue', methods=['GET'])
@login_required
def show_queue(random_hex):
    post = Post.query.filter_by(random_hex=random_hex).first_or_404()
    return render_template('post/show_queue.html', post=post)


@post.route('/post/<string:random_hex>/submit_answer', methods=['GET', 'POST'])
@login_required
def submit_answer(random_hex):
    # Находим пост по уникальному идентификатору random_hex
    post = Post.query.filter_by(random_hex=random_hex).first_or_404()

    if request.method == 'POST':
        # Получаем ответ пользователя
        user_response = request.form.get('response')

        # Проверяем правильность ответа
        if user_response == post.res:
            flash('Да! Молодец! Правильный ответ!', 'success')
            return redirect(url_for('post.posters'))  # Перенаправляем на главную страницу
        else:
            flash('Ошибка! Попробуйте снова.', 'danger')
            return render_template('post/submit_answer.html', post=post, show_retry=True)

    return render_template('post/submit_answer.html', post=post)

@post.route('/random_hex_input', methods=['GET', 'POST'])
def handle_random_hex():
    if request.method == 'POST':
        random_hex = request.form.get('random_hex')

        if not random_hex:
            flash('Please enter a random hex.')
            return render_template('post/random_hex_input.html')

        # Поиск записи в базе данных
        post = Post.query.filter_by(random_hex=random_hex).first()

        if post:
            return redirect(url_for('post.show_queue', random_hex=random_hex))
        else:
            flash('Invalid random hex. Please try again.')
            return render_template('post/random_hex_input.html')

    return render_template('post/random_hex_input.html')