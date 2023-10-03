from django.shortcuts import render, HttpResponse, redirect
from app1.models import user_data, complaint as c, schemes as sc, notice as nt, appointment as ap
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
import random
from datetime import timedelta

def index(request):
    return render(request, 'index.html')

def login(request):
    # forgot password
    if request.method == 'POST' and 'reset' in request.POST:
        email = request.POST.get('Email')
        if user_data.objects.filter(email = email).exists() == True:
            fill_mail = render_to_string('resetpass.html', {email:email})
            send_email = EmailMessage(
                'Forgot Password! Gram Management System',
                f'http://127.0.0.1:8000/reset/{email}/',
                # fill_mail,
                settings.EMAIL_HOST_USER,
                [email],
            )
            send_email.fail_silently = False
            send_email.send()
            return redirect('/')
        else:
            return render(request, 'login.html', {'noexist' : 1})
    # login code
    if request.method == 'POST':
        email = request.POST.get('Email')
        password = request.POST.get('Password')
        check = user_data.objects.filter(email = email, password= password).exists()
        if check == True:
            id = user_data.objects.get(email = email)
            request.session['u_id'] = id.id
            return redirect('/profile')
        else:
            return render(request, 'login.html', {'noexist' : 2})
    return render(request, 'login.html')

def reset(request , email):
    if request.method == 'POST':
        password = request.POST.get('newpass')
        user_data.objects.filter(email=email).update(password=password)
        return redirect('/login')
    return render(request, 'resetnew.html')

def generateOPT(email):
    digits = "0123456789"
    otp = ""
    for i in range(4):
        otp += random.choice(digits)
    # mail sending
    fill_mail = render_to_string('register/mail.html', {'o':otp})
    send_email = EmailMessage(
        'Welcome to Gram Management System',
        fill_mail,
        settings.EMAIL_HOST_USER,
        [email],
    )
    send_email.fail_silently = False
    send_email.send()
    print(otp)
    return otp

def verifyemail(request):
    if request.method == 'POST':
        email = request.POST.get('Email')
        # get OTP
        if user_data.objects.filter(email = email).exists() == True:
            print("arre email paylut aasa part part ghalu naka !!!!!!!!!!!!!!!!!!! ")
            # add the message to display that the email is already present in the models
            return render(request, 'register/verifyemail.html', { 'jsmess' : 1 })
        request.session['email'] = email
        request.session['otp'] = generateOPT(email)
        # request.session.set_expiry(timedelta(minutes=5))
        return redirect('/otp')
    return render(request, 'register/verifyemail.html')

def otp_verify(request):
    if request.method == 'POST' and 'otpbox' in request.POST:
        optin = request.POST.get('otpenter')
        print('Entered : ',optin,' generated : ',request.session['otp'])
        if optin == request.session['otp']:
            print("otp verified !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            del request.session['otp']
            return redirect('/register')
        else:
            print("invalid password ?????????????????????????????????")
            # return redirect('/otp')
            return render(request, 'register/otp_verify.html', { 'otpver': 1 })
    if request.method == 'POST' and 'reset' in request.POST:
        print('resending otp !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        request.session['otp'] = generateOPT(request.session['email'])
        return redirect('/otp')
    return render(request, 'register/otp_verify.html')

def register(request):
    if request.method == 'POST':
        name = request.POST.get('Name')
        email = request.session['email']
        address = request.POST.get('address')
        password = request.POST.get('Password')
        adhar = request.POST.get('aadhaar')
        image = request.FILES['photo']
        send = user_data(name=name, email=email, address=address, password=password, image=image, adhar=adhar)
        send.save()
        del request.session['email']
        return redirect('/')
    return render(request, 'register/Register.html')

def profile(request):
    user_id = user_data.objects.get(id = request.session['u_id'])
    return render(request, 'user/profile.html', {'data' : user_id})

# compaint
def complaint(request):
    pass_d = c.objects.filter(user = request.session['u_id'])
    return render(request, 'user/complaint.html', {'data' : pass_d})

def complaintfrom(request):
    if request.method == 'POST':
        add = request.POST.get('address')
        sub = request.POST.get('subject')
        mesg = request.POST.get('mesg')
        image = request.FILES['photo']
        fk = user_data.objects.get(id = request.session['u_id'])
        c(user = fk, address = add, subject = sub, message = mesg, image=image).save()
        return redirect('/complaint')
    return render(request, 'user/complaintfrom.html')

def schemes(request):
    p_data = sc.objects.all()
    return render(request, 'user/schemes.html', {'data' : p_data})

def notice(request):
    p_data = nt.objects.all()
    return render(request, 'user/notice.html', {'data' : p_data})

def bugets(request):
    return render(request, 'user/bugets.html')

def appointment(request):
    p_data = ap.objects.filter(fk = request.session['u_id'])
    return render(request, 'user/appointment.html', {'data' : p_data})

def appointmentfrom(request):
    if request.method == 'POST':
        fk_id = user_data.objects.get(id = request.session['u_id'])
        name = fk_id.name
        print('------------------------------->',fk_id," : ",name)
        sub = request.POST.get('subject')
        appoi = request.POST.get('Appointment')
        # image = request.FILES['photo']
        ap(fk = fk_id, name = name, subject = sub, purpose = appoi).save()
        return redirect('/appointment')
    return render(request, 'user/appointmentfrom.html')

def logout(request):
    print("your session in logout is : ",request.session['u_id'])
    del request.session['u_id']
    return redirect('/')