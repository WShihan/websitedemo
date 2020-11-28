from django.shortcuts import render
import logging
# Create your views here.
import sqlite3
import sentMail ,E_Meil
import hashlib
from . import models
import time ,random
from django.http import HttpResponse ,JsonResponse
from django.template.response import TemplateResponse

# 首页函数
def index(request):
    week=('星期日' ,'星期一','星期二','星期三','星期四','星期五','星期六')
    day = int(time.strftime('%w'))
    tt = time.localtime()
    tlt = str(tt[0]) +'-' + str(tt[1]) +'-' + str(tt[2]) + '   ' + week[day]
    # 获取访问人数
    info = models.ViewNum.objects.get(name='home')
    num = str(info.num)
    info.num += 1
    info.save()

    return TemplateResponse(request , 'page.html' ,{'weather':'多云转晴' ,'date': tlt,'Email':'6996669999@qq.com' , 'num':num})

def img(request):
    html='这是我的第一个Django网页<br/><img src="/static/mn.jpg" alt="beauty">'
    return HttpResponse(html)

def contact(request):
    r = HttpResponse('联系我们\n' , content_type='text/txt;charset=utf-8')
    r['Content-Disposition']='attachment; filename="contact.txt"'
    r.write('QQ:3558034053 \n  WeChat:WannaBeRealMan_233 \n Phone:xxxxxxxxxxxx')
    return r

def about(request):
   r = HttpResponse(content_type="application/json;charset=utf-8")
   r.write('这是一个小破站，希望你可以喜欢它')
   return r
def showImage(request):
    return TemplateResponse(request ,'draw.html')

def book(request):
    info = models.ViewNum.objects.get(name='book')
    viewer = info.num
    info.num += 1
    info.save()
    return TemplateResponse(request , 'books.html',{'viewer':viewer ,'fresh':'2020-6-15'})
# 以下为返回图片的视图函数
def img1(request):
    source = '/static/images/og/m1.png'
    return HttpResponse(request , 'showImage.html' ,{'source':source})
# 代取快递视图函数
def getData(request):
    if request.method == "GET":
        name = request.GET.get('name')
        phone = request.GET.get('phone')
        pack_size = request.GET.get('cb')
        address = request.GET.get('add')
        code = request.GET.get('code')
        note = request.GET.get('note')
        date = time.asctime()
        msg = "姓名:---" + name + ",电话:---" + phone + ",取件码:---" + code + ",大小:---" + pack_size +  ",寝室号:---" + address + ",备注:---" + note

        info = models.Customer.objects.all()
        for f in info:
            if code == f.code:
                return HttpResponse("姓名:" + f.name + "----取件码:" + f.code)
        s = E_Meil.SentEmail('1718258151@qq.com', msg, '快递代取通知')
        id = len(info)
        update = models.Customer(id = id + 1,name = name ,phone = phone ,code = code ,pack_size = pack_size ,address = address , date = date ,note = note)
        update.save()
        return HttpResponse("Yes")


def pack(request):
    if request.method == "GET":
        name = request.GET.get('name')
        phone = request.GET.get('phone')
        pack_size = request.GET.get('cb')
        address = request.GET.get('add')
        code = request.GET.get('code')
        note = request.GET.get('note')
        date = time.asctime()
        msg = "姓名:---" + name + ",电话:" + phone + ",取件码:" + code + ",大小:" + pack_size +  ",寝室号:" + address + ",备注:" + note

        info = models.Customer.objects.all()
        for f in info:
            if code == f.code:
                return HttpResponse("姓名:" + f.name + "----取件码:" + f.code)
        s = E_Meil.SentEmail('1718258151@qq.com', msg, '快递代取通知')
        e2 = E_Meil.SentEmail('2513272383@qq.com', msg, '外卖代取通知')
        id = len(info)
        update = models.Customer(name = name ,phone = phone ,code = code ,pack_size = pack_size ,address = address , date = date ,note = note)
        update.save()
        return HttpResponse("Yes")

# 代取外卖视图函数
def takeOUt(request):
    if request.method == "GET":
        name = request.GET.get('name')
        phone = request.GET.get('phone')
        where= request.GET.get('where')
        note = request.GET.get('note')
        add = request.GET.get('add')
        date = time.asctime()
        msg = "姓名:" + name + ",电话:" + phone + ",地点:" + where + ",寝室:" + add + ",备注:" + note

        update = models.TakeOut(name = name , phone = phone, where = where , address = add ,note = note ,date = date)
        update.save()

        e1 = E_Meil.SentEmail('1718258151@qq.com' ,msg ,'外卖代取通知')
        e2 = E_Meil.SentEmail('2513272383@qq.com' ,msg ,'外卖代取通知')
        return HttpResponse("Yes")



# 软件安装业务视图函数
def soft(request):
    if request.method == "GET":
        name = request.GET.get('name')
        phone = request.GET.get('phone')
        soft = request.GET.get('soft')
        note = request.GET.get('note')
        date = time.asctime()
        info = models.Soft.objects.all()
        msg = "姓名:---" +name + "电话:---" + phone + "软件:---" + soft + "备注:---" + note
        id = len(info)
        update = models.Soft(id=id + 1, name=name, phone=phone, soft=soft, note=note, date=date)
        update.save()

        e1 = E_Meil.SentEmail('1718258151@qq.com' ,msg ,'软件安装通知')
        return HttpResponse("Yes")

# 返回图片二进制数据流
def returnImg(request):
    with open(r'C:\inetpub\website\myapp\static\images\montain.jpg' ,'rb') as f:
        res = f.read()
    return HttpResponse(res ,content_type='image/png')
# 返回ONE页面json数据
def returnSaying(request):
    info = models.One.objects.get(id='1')
    saying = info.saying
    return HttpResponse(saying)

def returnDay(req):
    info = models.One.objects.get(id='1')
    day = info.day
    return HttpResponse(day)
def returnDate(req):
    info = models.One.objects.get(id='1')
    date = info.date
    return HttpResponse(date)

def returnUrl(req):
    info = models.One.objects.get(id='1')
    url = info.url
    return HttpResponse(url)


def returnClaim(request):
    r ="找开发伙伴，前后端开发均可，男女不限。前端要求：*具有一定的前端语言【HTML,CSS,JavaScript】基础；后端要求：*主要具有Python编程基础，要是熟悉Pyhton Web框架Django，数据库语言SQL更好。详情请添加微信了解，WeChat ID:19184187685"
    return HttpResponse(r)
def test(req):
    if req.method == 'GET':
        return HttpResponse("Yes")

# 获取反馈信息视图函数
def getFeedBack(req):
    try:
        if req.method == 'GET':
            content = req.GET.get('feedback')
            email = req.GET.get('email')
            info = models.FeedBack.objects.all()
            date = time.asctime()
            id = len(info)
            update = models.FeedBack(content=content, email=email, date=date)
            update.save()
            e1 = E_Meil.SentEmail('1718258151@qq.com' , content + email ,'反馈通知')
            return HttpResponse("Yes")
        else:
            return HttpResponse("No")
    except Exception as e:
        print(e)
# 修改用户数据表中的信息
def updateInfo(req):
    if req.method == 'GET':
        name = req.GET.get('name')
        code = req.GET.get('code')

        info = models.Customer.objects.all()
        for f in info:
            if f.code == code and f.name == name:
                f.name = f.name + "(取消)"
                f.save()
                return HttpResponse("Yes")

        return HttpResponse("No")





def showData(req):
    data = ""
    info = models.Customer.objects.all()
    plt = "订单数据为:<br><table><tr><td>id</td><td>姓名</td><td>电话·</td><td>取件码</td><td>包裹大小</td><td>寝室</td><td>时间</td></tr>"
    for f in info:
        plt += "<td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" %(f.id ,f.name ,f.phone ,f.code ,f.pack_size ,f.address ,f.date)
    return HttpResponse(plt + "</table>")

# 校验微信小程序token
token = 'httpswwwxiemolin233'
def seeToken(req):
    global  token
    signature = req.GET.get('signature')
    timestamp = req.GET.get('timestamp')
    noce = req.GET.get('nonce')
    echostr = req.GET.get('echostr')
    token = token
    checkList = [token , timestamp ,noce]
    checkList.sort()
    s1 = hashlib.sha1()
    s1.update(''.join(checkList).encode())
    hashcode = s1.hexdigest()
    if hashcode == signature:
        return HttpResponse(echostr)
    else:
        return HttpResponse("")

def getId(req):
    if req.method == 'GET':
        code = req.GET.get('code')
        return HttpResponse(code)
