from django.shortcuts import render, redirect
from .models import profile
import os


def login(r):
    if r.method == 'POST':
        name = r.POST['name']
        email = r.POST['email']
        img = r.FILES['fileupload']
        user = profile.objects.create(name=name, email=email, proPic=img)
        user.save()

    return render(r, 'login.html', locals())


def Prof(r):
    pro = profile.objects.all()
    search = r.GET.get('search')
    if search:
        pro = profile.objects.filter(name__icontains=search)
    else:
        pro = profile.objects.all()

    return render(r, 'newProf.html', locals())


def update(r, id):
    pro = profile.objects.get(id=id)

    if r.method == 'POST':
        name = r.POST['name']
        email = r.POST['email']
        img = r.FILES.get('fileupload')

        if len(r.FILES)!=0:
            if len(pro.proPic)>0:
                os.remove(pro.proPic.path)
            pro.proPic = img
        pro.name = name
        pro.email = email
        pro.save()
        return redirect('Prof')

    return render(r, 'Update.html', locals())


def delete(r, id):
    p = profile.objects.get(id=id)
    p.delete()
    return redirect("Prof")
