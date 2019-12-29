from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Theloai
from .models import Tintuc
from xml.etree import ElementTree as etree
from bs4 import BeautifulSoup
import requests
# Create your views here.
# def index(request):
#     myname="donle"
#     taisan1=["xe","dola","tien"]
#     context={"name":myname,"taisan":taisan1}
#     return render(request,"polls/index.html",context)
def viewlistloai(request):
    listloai=Theloai.objects.all()
    listtintuc=Tintuc.objects.all()
    class hot:  
        def __init__(self, tieu_de, description, ngaytao, hinh, link):  
            self.tieu_de = tieu_de  
            self.description = description 
            self.ngaytao = ngaytao
            self.hinh = hinh
            self.link = link
    listhot = []  

    data = requests.get(url = "https://video.thanhnien.vn/rss/thoi-su.rss").text
    RSS = etree.fromstring(data)
    item = RSS.findall('channel/item')

    for entry in item:
        listhot.append( hot(entry.findtext('title'), entry.findtext('description'), entry.findtext('pubDate'), entry.findtext('description').split('"')[7], entry.findtext('link'))) 

    context={"listloai":listloai,"listtintuc":listtintuc, "listhot": listhot}
    return render(request,"polls/index.html",context)
def viewlisttintuc(request, loai_id):
    listtt=Theloai.objects.get(pk=loai_id)
    listloai=Theloai.objects.all()
    return render(request,"polls/loaitintuc.html",{"tintuc":listtt,"listloai":listloai})
def viewtintuc(request, tintuc_id):
    listloai=Theloai.objects.all()
    listtt=get_object_or_404(Tintuc,pk=tintuc_id)
    return render(request,"polls/tintuc.html",{"listloai":listloai,"tintuc":listtt})
def viewkey(request):
    listloai=Theloai.objects.all()
    listtintuc=Tintuc.objects.all()
    class listtt:  
        def __init__(self,id, tieu_de, ngaytao, hinh):  
            self.id=id
            self.tieu_de = tieu_de  
            self.ngaytao = ngaytao
            self.hinh = hinh
    listttt = []  
    keytem=request.GET.get("keyget")
    for i in listtintuc:
        #print(i.tieu_de)
        if i.tieu_de.find(keytem)!=-1:
            listttt.append(listtt(i.id,i.tieu_de,i.ngaytao,i.hinh))
            #listfindtemp=listfindtemp.append(i) 
            print(i.tieu_de)
    context={"listloai":listloai,"tintuc":listttt}
    #return HttpResponse(keytem)
    return render(request,"polls/loaitintuc.html",context)