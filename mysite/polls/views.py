from django.shortcuts import render
from django.http import HttpResponse
from .models import Theloai
from .models import Tintuc
# Create your views here.
# def index(request):
#     myname="donle"
#     taisan1=["xe","dola","tien"]
#     context={"name":myname,"taisan":taisan1}
#     return render(request,"polls/index.html",context)
def viewlistloai(request):
    listloai=Theloai.objects.all()
    listtintuc=Tintuc.objects.all()
    context={"listloai":listloai,"listtintuc":listtintuc}
    return render(request,"polls/index.html",context)
def viewlisttintuc(request, loai_id):
    listtt=Theloai.objects.get(pk=loai_id)
    return render(request,"polls/loaitintuc.html",{"tintuc":listtt})