from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from registraciy.form import SignUpform


# Create your views here.

def index(request):
    if request.user.username: # если пользователь есть в табличке то присваеваем его в переменную
        user_f_name = request.user.first_name # присваение имени пользователя в переменную
        user_l_name = request.user.last_name # присвоение фамилии пользователя в переменную
    else: # иначе (если нет пользователя в таблице)
        user_f_name = 'Гость'
        user_l_name = ''
    data = {'user_f_name': user_f_name,
            'user_l_name': user_l_name}  # словарь для непосредственного вывода информации на страницу для пользователя

    return render(request, 'index.html', context=data)  # возврат запроса на на какую страницу и какую информацию вывести

def registr(req): # функция сбора информации от пользователя и дальнейшее его регистрация в таблице
    print(1)
    if req.POST:
        print(2)
        anketa = SignUpform(req.POST)
        if anketa.is_valid():
            print(3)
            anketa.save()
            k1 = anketa.cleaned_data.get('username')
            k2 = anketa.cleaned_data.get('password1')
            k3 = anketa.cleaned_data.get('first_name')
            k4 = anketa.cleaned_data.get('last_name')
            k5 = anketa.cleaned_data.get('email')
            user = authenticate(username=k1, password=k2) # сохраняет нового пользоватлея
            man = User.objects.get(username=k1)             # найдем нового юзера
            #заполним поля в таблице
            man.first_name = k3
            man.last_name = k4
            man.email = k5
            man.save()
            login(req, user)
            # group = Group.objects.get(id=1) # находим бесплатную подписку
            # group.user_set.add(man) # записываем нового пользователя в подписку, связываем две таблицы
            return redirect('home') # входит на сайт
    else:
        anketa = SignUpform()
    data = {'regform': anketa}
    return render(req,'registration/registration.html',context=data)
