from datetime import date
from master_app.models import user_master
from django.shortcuts import  render,redirect
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def login_page(request):
    return render(request,'login_page.html')
    # return HttpResponse("testing with login ")
@csrf_exempt
def login_check(request):
    if request.method=="POST":
        userid = request.POST.get('userid')
        password = request.POST.get('password')
        check_user = user_master.objects.filter(userid=userid,password=password,crnt_sts=1).count()
        if check_user == 1 :
            userid=request.session['user_id']= userid
            user = user_master.objects.get(userid=userid,password=password,crnt_sts=1)
            print(user.first_name)
            context={ 'username':user.first_name , }
            return render(request,'index.html',context)
        else :
            return redirect('login_page')
    else :
        return redirect('login_page')
def logout(request):
    try:
        del request.session["user_id"]
        return redirect('login_page')
    except KeyError:
        pass
    return redirect('login_page')
def create_page(request):
    return render(request,'register.html')
# from django.http import HttpResponse
@csrf_exempt
def create_account(request):
    if request.method=="POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        mail_id = request.POST.get('mail_id')
        phno = request.POST.get('phno')
        password = request.POST.get('password')
        # confirmpassword = request.POST.get('confirmpassword')
        crnt_sts = 1
        new_user = user_master(first_name=first_name,last_name=last_name,mail_id=mail_id,phno=phno,crnt_sts=crnt_sts,password=password,createdby=0)
        new_user.save()
        contex = { 'message' : 'Successfully Saved your Details and New account created'}
        return render(request,'login_page.html',contex)
        # print(password)
        # print(confirmpassword)
        # if password == confirmpassword : 
        #     print('test passed')           
            
        # else :
        #     print('test failed')
        #     contex = { 'message' : 'Password and confirm password not matched.'}
        #     return render(request,'register.html',contex)

    else :
        return redirect('create_page')



        

        # print('ok creating ')
        # return HttpResponse('fistname'+str(first_name))