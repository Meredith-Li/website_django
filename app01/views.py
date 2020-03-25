from django.shortcuts import render,HttpResponse,redirect
from pymongo import MongoClient
from django.views.generic import View
def home(req):
    return render(req, 'home_test.html')
def introduction(req):
    return render(req, 'introduction.html')
def coding(req):
    return render(req,'coding.html')
def cgss(req):
    return render(req,'cgss.html')
def ele(req):
    return render(req,'ele.html')
def under_construction(req):
    return render(req,"under_construction.html")
def login(req):
    message = ''
    if req.method == "POST":
        email1 = req.POST.get('email1',None)
        pwd1 = req.POST.get('pwd1',None)
        __db_server, __db_port = '127.0.0.1', 27017
        client = MongoClient(__db_server, __db_port)
        db = client['userinfo']
        user = db.trial1.find_one({'_id': email1})
        if user is not None:
            pwd = user['密码']
            print(user)
            print(user["密码"],type(pwd))
            print(pwd1,type(pwd1))
            if pwd1 == pwd:
                message = "zzcg"
                return render(req, 'home_test.html', {'msg': message})
            else:
                message = '用户名或密码错误'
        else:
            message = '请先注册'
            return render(req, 'login.html', {'msg': message})
        client.close()
        return render(req,'login.html',{'msg':message})
    else:
        return render(req,'login.html')




"""
def register(request):
    if request.method == "POST":
        email = request.POST.get('email')
        username1 = request.POST.get('username1')
        username2 = request.POST.get('username2')
        pwd = request.POST.get('pwd')
        pwd2 = request.POST.get('pwd2')
        sex = request.POST.get('sex')
        organization = request.POST.get('organization')
        research = request.POST.get('research')
        title = request.POST.get('title')
        age = request.POST.get('age')
        qq = request.POST.get('qq')
        wechat = request.POST.get('wechat')
        blog = request.POST.get('blog')
        __db_server, __db_port = '127.0.0.1', 27017
        client = MongoClient(__db_server, __db_port)
        db = client['userinfo']
        result = db.userinfo.find_one({'_id': email})
        if result is None:
            db.trial1.insert_one(
                {'_id': email,
                 '姓': username1,
                 '名': username2,
                 '密码': pwd,
                 '密码2': pwd2,
                 '性别': sex,
                 '工作/学习单位': organization,
                 '专业/研究方向': research,
                 '职称': title,
                 '年龄': age,
                 'qq': qq,
                 'wechat': wechat,
                 '个人主页': blog,
                 }
            )
        else:
            db.trial1.update_one(
                {"_id": email},
                {'$set':
                     {'姓': username1,
                      '名': username2,
                      '密码': pwd,
                      '密码2': pwd2,
                      '性别': sex,
                      '工作/学习单位': organization,
                      '专业/研究方向': research,
                      '职称': title,
                      '年龄': age,
                      'qq': qq,
                      'wechat': wechat,
                      '个人主页': blog, }
                 }
                , upsert=None)

        if len(str(email)) == 0:
            db.trial1.delete_one({'_id': email})
            client.close()
            return HttpResponse('提交失败')
        elif pwd != pwd2:
            db.trial1.delete_one({'_id': email})
            client.close()
            return HttpResponse('两次密码不一致')
        else:
            return render(request, 'home_test.html')



    else:
        return render(request, 'register.html')
"""



def test_register(request):
    if request.method == "POST":
        email = request.POST.get('email')
        email2 = request.POST.get('email2')
        username1 = request.POST.get('username1')
        username2 = request.POST.get('username2')
        pwd = request.POST.get('pwd')
        pwd2 = request.POST.get('pwd2')
        sex = request.POST.get('sex')
        organization = request.POST.get('organization')
        research = request.POST.get('research')
        title = request.POST.get('title')
        age = request.POST.get('age')
        qq = request.POST.get('qq')
        wechat = request.POST.get('wechat')
        blog = request.POST.get('blog')
        if email != email2:
            return HttpResponse('两次注册邮箱不一致')
        elif len(str(email)) == 0:
            return HttpResponse('提交失败')
        elif pwd != pwd2:
            return HttpResponse('两次密码不一致')

        else:
            __db_server, __db_port = '127.0.0.1', 27017
            client = MongoClient(__db_server, __db_port)
            db = client['userinfo']
            try:
                user = db.userinfo.find_one({'_id': email})
                if user is None:
                    db.trial1.insert_one(
                        {'_id': email,
                         '姓': username1,
                         '名': username2,
                         '密码': pwd,
                         '密码2': pwd2,
                         '性别': sex,
                         '工作/学习单位': organization,
                         '专业/研究方向': research,
                         '职称': title,
                         '年龄': age,
                         'qq': qq,
                         'wechat': wechat,
                         '个人主页': blog,
                         }
                    )
                    send_register_email(email, 'register')
                    client.close()
                    return HttpResponse('邮箱验证已发送')
                else:
                    db.trial1.update_one(
                        {"_id": email},
                        {'$set':
                             {'姓': username1,
                              '名': username2,
                              '密码': pwd,
                              '密码2': pwd2,
                              '性别': sex,
                              '工作/学习单位': organization,
                              '专业/研究方向': research,
                              '职称': title,
                              '年龄': age,
                              'qq': qq,
                              'wechat': wechat,
                              '个人主页': blog, }
                         }
                        , upsert=None)
                    send_register_email(email, 'register')
                    client.close()
                    return HttpResponse('邮箱验证已发送')


            except KeyError:
                message = "该邮箱已注册"
                client.close()
                return render(request, 'login.html', {'msg': message})
    else:
        return render(request,'register.html')



from random import Random
from derek.settings import EMAIL_FROM#导入smtp
from django.core.mail import send_mail #导入发送邮件


def generate_random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars)-1
    random = Random()
    for i in range(randomlength):
        str+=chars[random.randint(0,length)]
    return str

def send_register_email(email, send_type="register"):
    random_str = generate_random_str(16)  # 取随机数
    __db_server, __db_port = '127.0.0.1', 27017
    client = MongoClient(__db_server, __db_port)
    db = client['email_code']
    db.code1.insert_one({'_id': email, 'email_code': random_str, 'status': 'false'})

    print(random_str)

    if send_type == "register":
        email_title = "注册激活链接"
        email_body = "请点击下面的链接激活你的账号：http://cssci.wh.sdu.edu.cn/active/{0}/{1}".format(random_str,email)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass

# 用于实现用户激活操作的函数
class ActiveUserView(View):
    def get(self, request, email,active_code):
        # 用于查询邮箱验证码是否存在
        __db_server, __db_port = '127.0.0.1', 27017
        client = MongoClient(__db_server, __db_port)
        db = client['email_code']
        try:

            active = db.code1.find_one({'_id': email, 'email_code': active_code})

            if active:
                db.code1.update_one(
                    {"_id": email},
                    {'$set':
                         {'status': 'true'}
                     }
                    , upsert=False)
                return render(request, "home_test.html")

        except KeyError:
            message = "您的激活链接无效"
            return render(request, 'test_register.html', {'msg': message})
        client.close()








