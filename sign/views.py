from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from sign.models import Event, Guest
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    return render(request, 'index.html')


# 登录动作
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)  # 登录
            request.session['user'] = username  # 将session信息记录到浏览器
            response = HttpResponseRedirect('/event_manage/')
            return response
        else:
            return render(request, 'index.html', {'error': 'user or password error!'})

            # if username == 'admin' and password == 'admin123':
            #     response = HttpResponseRedirect('/event_manage')
            #     # 将session信息记录到浏览器
            #     request.session['user'] = username
            #     return response
            # else:
            #     return render(request, 'index.html', {
            #         'Error': 'username or password error'
            #     })
            # else:
            #     return render(request, 'index.html', {
            #         'Error': 'username or password error'
            #     })


# 发布会管理
# @login_required()
def event_manage(request):
    event_list = Event.objects.all()  # 查询所有发布会对象数据,通过 render()函数附加在event_manage.html页面返回给客户端浏览器。
    username = request.session.get('user', '')

    paginatorEvent = Paginator(event_list, 5)
    page = request.GET.get('page')
    try:
        contacts = paginatorEvent.page(page)
    except PageNotAnInteger:
        # 如果页数不是整型, 取第一页.
        contacts = paginatorEvent.page(1)
    except EmptyPage:
        # 如果页数超出查询范围，取最后一页
        contacts = paginatorEvent.page(paginatorEvent.num_pages)

    return render(request, 'event_manage.html', {'user': username,
                                                 'events': contacts})


# 发布会名称搜索
# @login_required
def search_name(request):
    username = request.session.get('user', '')
    search_name = request.GET.get("name", "")
    events = Event.objects.filter(name__contains=search_name)
    if len(events) == 0:
        return render(request, "event_manage.html", {"user": username,
                                                     "hint": "根据输入的 `发布会名称` 查询结果为空！"})
    return render(request, "event_manage.html", {"user": username, "events": events})


# 嘉宾管理
# @login_required
def guest_manage(request):
    username = request.session.get('user', '')
    guests = Guest.objects.all()

    paginatorGuest = Paginator(guests, 5)
    page = request.GET.get('page')
    try:
        contacts = paginatorGuest.page(page)
    except PageNotAnInteger:
        # 如果页数不是整型, 取第一页.
        contacts = paginatorGuest.page(1)
    except EmptyPage:
        # 如果页数超出查询范围，取最后一页
        contacts = paginatorGuest.page(paginatorGuest.num_pages)
    return render(request, "guest_manage.html", {"user": username, "guests": contacts})


# 嘉宾手机号的查询
# @login_required
def search_phone(request):
    username = request.session.get('user', '')
    search_phone = request.GET.get("phone", "")
    guests = Guest.objects.filter(phone__contains=search_phone)

    if len(guests) == 0:
        return render(request, "guest_manage.html", {"user": username,
                                                     "hint": "根据输入的 `手机号码` 查询结果为空！"})

    # paginator = Paginator(guests, 5)  # 少于5条数据不够分页会产生警告
    # page = request.GET.get('page')
    # try:
    #     contacts = paginator.page(page)
    # except PageNotAnInteger:
    #     # If page is not an integer, deliver first page.
    #     contacts = paginator.page(1)
    # except EmptyPage:
    #     # If page is out of range (e.g. 9999), deliver last page of results.
    #     contacts = paginator.page(paginator.num_pages)

    return render(request, "guest_manage.html", {"user": username,
                                                 # "guests": contacts,
                                                 "phone": search_phone})


# 签到页面
@login_required
def sign_index(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'sign_index.html', {'event': event})


# 退出登录
@login_required
def logout(request):
    auth.logout(request)  # 退出登录
    response = HttpResponseRedirect('/index/')
    return response
