from django.shortcuts import render,get_object_or_404
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
def viewtintuc(request, tintuc_id):
    listloai=Theloai.objects.all()
    listtt=get_object_or_404(Tintuc,pk=tintuc_id)
    return render(request,"polls/tintuc.html",{"listloai":listloai,"tintuc":listtt})
def viewkey(request):
    #listloai=Theloai.objects.all()
    #listtintuc=Tintuc.objects.all()
    keytem=request.POST.get("keyget",'')
    # for i in listtintuc:
    #     if i.tieu_de.find(key)==-1:
    #         listtintuc.remove(i)
    # context={"listloai":listloai,"listtintuc":listtintuc}
    return HttpResponse(keytem)
    # return render(request,"polls/index.html",context)