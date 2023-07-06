from django.shortcuts import render , redirect
from .models import  head  , book    , bookr  , bookre 
from datetime import datetime , timedelta
from .forms import bookf
from django.core.mail import send_mail
from django.conf import settings
import csv
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
# Create your views here.




def index(request):
    form = request.session['e']
    return render(request , 'app/index.html' , {'form':form})


def login(request):
    if(request.method  == "POST" ):
        e = request.POST['e']
        p = request.POST['p']
        a = head.objects.filter(e = e , p = p).first()
        request.session['e'] = e 
        
        if(a is not None):
            
            return redirect(index)
        else:
            return render(request , 'app/login.html' , {'key':'not found'})



    return render(request , 'app/login.html' , {})


def library(request):
    form = book.objects.all()
    if(request.method  == "POST" ):
        e = request.POST['s']
        em = request.POST['e']
        print(e)

    return render (request , 'app/library.html' ,{'form':form})



def bookadd(request , id ):

    if(request.method  == "POST" ):
        e = request.POST['s'] 
        em = request.POST['e']  
        current_date = datetime.now().date()

        # Add 14 days to the current date
        new_date = current_date + timedelta(days=14)

        s = book.objects.get(pk = id)
        from_email = 'your_email@example.com'
        
        recipient_list = [em]
        current_date = datetime.now().date()
        subject = s.bi
        # Add 14 days to the current date
        new_date = current_date + timedelta(days=14)        
        message = f'book id -> {subject} must be returned before -> {new_date} '
        send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list, fail_silently=False)
        bookr(bi = s.bi , bn = s.bn , an = s.an  , e = em ,si = e , se = new_date).save()
        s.delete()
    
    return redirect(library)

def takenbook(request):
    form = bookr.objects.all()
    if(request.method  == "POST" ):
        e = request.POST['s']
        print(e)

    return render (request , 'app/takenbook.html' ,{'form':form})



def booktakenn(request , id ):

    if(request.method  == "POST" ):
        e = request.POST['s']  

        s = bookr.objects.get(pk = id)  
        if (s.st == 't'):
            bookre(bi = s.bi , bn = s.bn , an = s.an , sn =s.sname).save()
            s.delete()
        else:
            book(bi = s.bi , bn = s.bn , an = s.an  , sn = e).save()
            
            s.delete()
    
    return redirect(takenbook)

def reserve(request):
    form = bookr.objects.filter(st='f')
    if(request.method  == "POST" ):
        e = request.POST['s']
        em = request.POST['e']
        print(e)

    return render (request , 'app/reserve.html' ,{'form':form})



def reserved(request , id ):

    if(request.method  == "POST" ):
        e = request.POST['s'] 
        em = request.POST['e'] 
        current_date = datetime.now().date()

        # Add 14 days to the current date
        new_date = current_date + timedelta(days=14)

        s = bookr.objects.get(pk = id)
        bookr(bi = s.bi , bn = s.bn , an = s.an  , e = em ,si = e , se = new_date , st ='t').save()
        
    
    
    return redirect(reserve)




def res(request):
    form = bookre.objects.all()
    return render (request , 'app/res.html',{'form':form})



def ress(request , id ):

    if(request.method  == "POST" ):
        e = request.POST['s'] 
        em = request.POST['e']  
        current_date = datetime.now().date()

        # Add 14 days to the current date
        new_date = current_date + timedelta(days=14)

        s = bookre.objects.get(pk = id)
        bookr(bi = s.bi , bn = s.bn , an = s.an  , e = em ,si = e , se = new_date).save()
        s.delete()
    
    return redirect(res)


def info(request):
    return render (request ,  'app/info.html' , {})


def vam(request):
    return render(request , 'app/vam.html',{})



def booka(request):
    if(request.method == "POST" ):
        form = bookf(request.POST)
        if (form.is_valid()):

            bi=form.cleaned_data['bi']
            bn=form.cleaned_data['bn']
            an=form.cleaned_data['an']
            sn=form.cleaned_data['sn']
            
            book(bi = bi , bn = bn , an = an , sn = sn).save()
            form = bookf()
            
    form = bookf()         
    return render (request , 'app/booka.html' , {'form':form})

def csvv(request):
    
    # Query your model data
    queryset = book.objects.all()

    # Set response headers for CSV
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="mydata.csv"'

    # Create CSV writer object
    writer = csv.writer(response)

    # Write headers to CSV
    writer.writerow(['book_id','book_name','author_name','seller_name'])

    # Write data to CSV
    for obj in queryset:
        writer.writerow([obj.bi,obj.bn,obj.an,obj.sn])

    return response


def csvvv(request):
    
    # Query your model data
    queryset = bookr.objects.all()

    # Set response headers for CSV
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="mydata.csv"'

    # Create CSV writer object
    writer = csv.writer(response)

    # Write headers to CSV
    writer.writerow(['book_id','book_name','author_name','student_id','date','s_no'])

    # Write data to CSV
    for obj in queryset:
        writer.writerow([obj.bi,obj.bn,obj.an,obj.si,obj.se,obj.sname])

    return response
