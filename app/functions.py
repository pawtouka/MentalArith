import os
import secrets
from PIL import Image
from random import randint, choice, random

from flask import current_app


def save_picture(picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.config['SERVER_PATH'], picture_fn)
    output_size = (125, 125)
    i = Image.open(picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn

def check_ava(avatar_filename):
    a = avatar_filename.find('.')
    sec = avatar_filename[a:]
    if sec == '.jpeg' or sec == '.png' or sec == '.jpg':
        return 1
    else:
        return 0

def split_by_digits(number):
    return [int(digit) for digit in str(number)]

def randnum(a,b,c,d):
    d1 = randint(a,b)
    d2 = randint(c,d)
    if random == 1:
        k = d1
    else:
        k = d2
    return k

def con(a, b, maximum):
    return [i for i in range(-maximum, maximum + 1) if i in a or i in b]

def under_zero(a):
    return [i for i in a if i <= 0]
# Функции для фильтрации значений

def above_zero(a):
    return [i for i in a if i >= 0]

def create_ranges_def(queue_val):
    start1 = min(5, 9 - queue_val)
    start2 = min(-5, -queue_val)
    fin1 = max(5, 9 - queue_val)
    fin2 = max(-5, -queue_val)
    l1 = range(-queue_val, 4 - queue_val + 1)
    l2 = range(start1, fin1 + 1)
    l3 = range(5 - queue_val, 9 - queue_val + 1)
    l4 = range(start2, fin2 + 1)
    return l1, l2, l3, l4

def create_ranges_bro(queue_val):
    l1 = range(-queue_val, 9 - queue_val)
    l2 = []
    return l1, l2

def gen_q(maximum):
    a = randint(1, maximum)
    queue = [a]
    action = [a]
    return queue, action

def con_bro1(a, b, mode):
    return [i for i in range(-10, mode + 1) if i in a or i in b]

def con_bro2(a, b, mode):
    return [i for i in range(-mode, 10) if i in a or i in b]

def create_ranges_bro(queue_val):
    l1 = range(5 - queue_val, 5 + 1)
    l2 = range(-queue_val, 0 + 1)
    l3 = range(0, 9 - queue_val + 1)
    l4 = range(-4, 4 - queue_val + 1)
    return l1, l2, l3, l4

def generate_queue_def(act, maximum, dignits):
    random_hex = secrets.token_hex(8)
    maximum = min(9, maximum)
    dignits = min(3, dignits)
    act = min(20, act)
    queue, action = gen_q(maximum)
    queue2, action2 = gen_q(maximum)
    queue3, action3 = gen_q(maximum)

    for i in range(act - 1):
        # Генерация диапазонов для первой, второй и третьей очереди
        l1, l2, l3, l4 = create_ranges_def(queue[i])
        k1, k2, k3, k4 = create_ranges_def(queue2[i])
        m1, m2, m3, m4 = create_ranges_def(queue3[i])

        # Объединение диапазонов
        l5 = con(l1, l2, maximum)
        l6 = con(l3, l4, maximum)
        k5 = con(k1, k2, maximum)
        k6 = con(k3, k4, maximum)
        m5 = con(m1, m2, maximum)
        m6 = con(m3, m4, maximum)

        k7 = above_zero(k5) or [0]
        k8 = above_zero(k6) or [0]
        k9 = under_zero(k5) or [0]
        k10 = under_zero(k6) or [0]
        m7 = above_zero(m5) or [0]
        m8 = above_zero(m6) or [0]
        m9 = under_zero(m5) or [0]
        m10 = under_zero(m6) or [0]

        # Выбор b для queue[i]
        if 5 > queue[i] > 0:
            b = choice(l5)
        elif queue[i] >= 5:
            b = choice(l6)
        else:
            b = randint(1, maximum)

        if b == 0 and queue[i] == 9:
            b = -1
        elif b == 0 and queue[i] < 9:
            b = 1

        # Выбор b2 для queue2[i]
        if b > 0 and 5 > queue2[i] > 0:
            b2 = choice(k7)
        elif b > 0 and queue2[i] >= 5:
            b2 = choice(k8)
        elif b > 0 and queue2[i] == 0:
            b2 = randint(1, maximum)
        elif b < 0 and 5 > queue2[i] > 0:
            b2 = choice(k9)
        elif b < 0 and queue2[i] >= 5:
            b2 = choice(k10)
        elif b < 0 and queue2[i] == 0:
            b2 = randint(1, maximum)

        # Выбор b3 для queue3[i]
        if b > 0 and 5 > queue3[i] > 0:
            b3 = choice(m7)
        elif b > 0 and queue3[i] >= 5:
            b3 = choice(m8)
        elif b > 0 and queue3[i] == 0:
            b3 = randint(1, maximum)
        elif b < 0 and 5 > queue3[i] > 0:
            b3 = choice(m9)
        elif b < 0 and queue3[i] >= 5:
            b3 = choice(m10)
        elif b < 0 and queue3[i] == 0:
            b3 = randint(1, maximum)

        # Обновление очередей
        queue.append(queue[i] + b)
        queue2.append(queue2[i] + b2)
        queue3.append(queue3[i] + b3)

        action.append(b)
        action2.append(b2)
        action3.append(b3)

    if dignits == 1:
        res = queue[-1]
        c = [action[i] for i in range(act)]
    elif dignits == 2:
        res = queue[-1] + queue2[-1] * 10
        c = [action[i] + action2[i] * 10 for i in range(act)]
    elif dignits == 3:
        res = queue[-1] + queue2[-1] * 10 + queue3[-1] * 100
        c = [action[i] + action2[i] * 10 + action3[i] * 100 for i in range(act)]

    for i in range(len(c)):
        if c[i]>0:
            c[i] = '+' + str(c[i])
        else:
            c[i] = str(c[i])

    return c, res, random_hex

def generate_queue_bro(act, maximum, dignits, mode):
    random_hex = secrets.token_hex(8)
    maximum = min(9, maximum)
    dignits = min(3, dignits)
    act = min(20, act)
    queue, action = gen_q(maximum)
    queue2, action2 = gen_q(maximum)
    queue3, action3 = gen_q(maximum)

    for i in range(act - 1):
        # Генерация диапазонов для первой, второй и третьей очереди
        l1, l2, l3, l4 = create_ranges_bro(queue[i])
        k1, k2, k3, k4 = create_ranges_bro(queue2[i])
        m1, m2, m3, m4 = create_ranges_bro(queue3[i])

        # Объединение диапазонов
        l5 = con_bro1(l1, l2, mode)
        l6 = con_bro2(l3, l4, mode)
        k5 = con_bro1(k1, k2, mode)
        k6 = con_bro2(k3, k4, mode)
        m5 = con_bro1(m1, m2, mode)
        m6 = con_bro2(m3, m4, mode)

        k7 = above_zero(k5) or [0]
        k8 = above_zero(k6) or [0]
        k9 = under_zero(k5) or [0]
        k10 = under_zero(k6) or [0]
        m7 = above_zero(m5) or [0]
        m8 = above_zero(m6) or [0]
        m9 = under_zero(m5) or [0]
        m10 = under_zero(m6) or [0]

        # Выбор b для queue[i]
        if 5 > queue[i] > 0:
            b = choice(l5)
        elif 9 > queue[i] >= 5:
            b = choice(l6)
        elif queue[i] == 9:
            b = randint(-9, 1)
        else:
            b = randint(1, maximum)

        if b == 0 and queue[i] == 9:
            b = -1
        elif b == 0 and queue[i] < 9:
            b = 1

        # Выбор b2 для queue2[i]
        if b > 0 and 5 > queue2[i] > 0:
            b2 = choice(k7)
        elif b > 0 and queue2[i] >= 5:
            b2 = choice(k8)
        elif b > 0 and queue2[i] == 0:
            b2 = randint(1, maximum)
        elif b < 0 and 5 > queue2[i] > 0:
            b2 = choice(k9)
        elif b < 0 and queue2[i] >= 5:
            b2 = choice(k10)
        elif b < 0 and queue2[i] == 0:
            b2 = randint(1, maximum)

        # Выбор b3 для queue3[i]
        if b > 0 and 5 > queue3[i] > 0:
            b3 = choice(m7)
        elif b > 0 and queue3[i] >= 5:
            b3 = choice(m8)
        elif b > 0 and queue3[i] == 0:
            b3 = randint(1, maximum)
        elif b < 0 and 5 > queue3[i] > 0:
            b3 = choice(m9)
        elif b < 0 and queue3[i] >= 5:
            b3 = choice(m10)
        elif b < 0 and queue3[i] == 0:
            b3 = randint(1, maximum)

        # Обновление очередей
        queue.append(queue[i] + b)
        queue2.append(queue2[i] + b2)
        queue3.append(queue3[i] + b3)

        action.append(b)
        action2.append(b2)
        action3.append(b3)

    if dignits == 1:
        res = queue[-1]
        c = [action[i] for i in range(act)]
    elif dignits == 2:
        res = queue[-1] + queue2[-1] * 10
        c = [action[i] + action2[i] * 10 for i in range(act)]
    elif dignits == 3:
        res = queue[-1] + queue2[-1] * 10 + queue3[-1] * 100
        c = [action[i] + action2[i] * 10 + action3[i] * 100 for i in range(act)]

    for i in range(len(c)):
        if c[i]>0:
            c[i] = '+' + str(c[i])
        else:
            c[i] = str(c[i])

    return c, res, random_hex