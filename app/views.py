from django.shortcuts import render, redirect
from .models import *
from random import randint


# Create your views here.
def IndexPage(request):
    return render(request, "app/index.html")


def SignupPage(request):
    return render(request, "app/signup.html")


def RegisterUser(request):
    # Candidate Registration
    if request.POST["role"] == "Candidate":
        role = request.POST["role"]
        fname = request.POST["firstname"]
        lname = request.POST["lastname"]
        email = request.POST["email"]
        password = request.POST["password"]
        cpassword = request.POST["cpassword"]

        # checking user email id is same as in database
        user = UserMaster.objects.filter(email=email)

        if user:
            message = "User already Exists"
            return render(request, "app/signup.html", {"msg": message})
        else:
            if password == cpassword:
                otp = randint(100000, 999999)
                newuser = UserMaster.objects.create(
                    role=role, otp=otp, email=email, password=password
                )
                newcand = Candidate.objects.create(
                    user_id=newuser, firstname=fname, lastname=lname
                )
                return render(request, "app/otpverify.html", {"email": email})
    else:        
        if request.POST["role"] == "Company":
            # Company registration
            role = request.POST["role"]
            fname = request.POST["firstname"]
            lname = request.POST["lastname"]
            email = request.POST["email"]
            password = request.POST["password"]
            cpassword = request.POST["cpassword"]

            # checking user email id is same as in database
            user = UserMaster.objects.filter(email=email)

            if user:
                message = "User already Exists"
                return render(request, "app/signup.html", {"msg": message})
            else:
                if password == cpassword:
                    otp = randint(100000, 999999)
                    newuser = UserMaster.objects.create( role=role, otp=otp, email=email, password=password )
                    newcompany = Company.objects.create(user_id=newuser, firstname=fname, lastname=lname)
                    return render(request, "app/otpverify.html", {"email": email})


def OTPPAGE(request):
    return render(request, "app/otpverify.html")


def OtpVerify(request):
    email = request.POST["email"]
    otp = int(request.POST["otp"])
    user = UserMaster.objects.get(email=email)

    if user:
        if user.otp == otp:
            message = "Otp verify Successfully"
            return render(request, "app/login.html")
        else:
            message = "OTP is incorrect"
            return render(request, "app/otpverify.html", {"msg": message})
    else:
        return render(request, "app/signup.html", {"msg": message})


def LoginPage(request):
    return render(request, "app/login.html")


def LoginUser(request):
    if request.POST["role"] == "Candidate":
        email = request.POST["email"]
        password = request.POST["password"]
        user = UserMaster.objects.get(email=email)

        if user:
            if user.password == password and user.role == "Candidate":
                can = Candidate.objects.get(user_id=user)
                request.session["id"] = user.id
                request.session["role"] = user.role
                request.session["firstname"] = can.firstname
                request.session["lastname"] = can.lastname
                request.session["email"] = user.email
                request.session["password"] = user.password
                return redirect("index")
            else:
                message = "Password does not match"
                return render(request, "app/login.html", {"msg": message})
        else:
            message = "User does not exist"
            return render(request, "app/login.html", {"msg": message})
        
    else:
        if request.POST["role"] == "Company":
            email = request.POST["email"]
            password = request.POST["password"]
            user = UserMaster.objects.get(email=email)

            if user:
                if user.password == password and user.role == "Company":
                    company = Company.objects.get(user_id=user)
                    request.session["id"] = user.id
                    request.session["role"] = user.role
                    request.session["firstname"] = company.firstname
                    request.session["lastname"] = company.lastname
                    request.session["email"] = user.email
                    request.session["password"] = user.password
                    return redirect("companyindex")
                else:
                    message = "Password does not match"
                    return render(request, "app/login.html", {"msg": message})
            else:
                message = "User does not exist"
                return render(request, "app/login.html", {"msg": message})


def ProfilePage(request, pk):
    user = UserMaster.objects.get(pk=pk)
    if user.role == "Candidate":
        can = Candidate.objects.get(user_id=user)
        return render(request, "app/profile.html", {"user": user, "can": can})


def UpdateProfile(request, pk):
    user = UserMaster.objects.get(pk=pk)
    if user.role == "Candidate":
        can = Candidate.objects.get(user_id=user)
        print(can)
        can.contact = request.POST["contact"]
        can.country = request.POST["country"]
        can.state = request.POST["country"]
        can.city = request.POST["city"]
        can.address = request.POST["address"]
        can.dob = request.POST["dob"]
        can.gender = request.POST["gender"]
        can.highestedu = request.POST["highestedu"]
        can.experience = request.POST["experience"]
        can.min_salary = request.POST["min_salary"]
        can.max_salary = request.POST["max_salary"]
        can.website = request.POST["website"]
        can.shift = request.POST["shift"]
        can.website = request.POST["website"]
        can.jobdescription = request.POST["jobdescription"]
        can.profile_pic = request.FILES["profile_pic"]
        can.save()
        url = f"/profile/{pk}"  # formating url
        return redirect(url)


# ------------------- Company ---------------------


def CompanyIndex(request):
    return render(request, "app/company/index.html")


def CompanyProfile(request, pk):
    user = UserMaster.objects.get(pk=pk)
    if user.role == "Company":
        comp = Company.objects.get(user_id=user)
        return render(
            request, "app/company/profile.html", {"user": user, "comp": comp}
        )


def CompanyProfileUpdate(request, pk):
    user = UserMaster.objects.get(pk=pk)
    if user.role == "Company":
        comp = Company.objects.get(user_id=user)
        comp.firstname = request.POST["firstname"]
        comp.lastname = request.POST["lastname"]
        comp.company_name = request.POST["company_name"]
        comp.state = request.POST["state"]
        comp.city = request.POST["city"]
        comp.contact = request.POST["contact"]
        comp.website = request.POST["website"]
        comp.address = request.POST["address"]
        comp.logo_pic = request.FILES["logo_pic"]
        comp.save()
        url = f"/companyprofile/{pk}"  # formating url
        return redirect(url)
    return render(request, "app/company/index.html")

def JobPostPage(request):
    return render(request, 'app/company/jobpost.html')

def JobPost(request):
    user = UserMaster.objects.get(id=request.session["id"])
    if user.role == "Company":
        comp = Company.objects.get(user_id=user)
        jobname = request.POST['jobname']
        companyname = request.POST['company_name']
        companyaddress = request.POST['companyaddress']
        jobdescription = request.POST['jobdescription']
        qualification = request.POST['qualification']
        responsibilities = request.POST['responsibilities']
        location = request.POST['location']
        companywebsite = request.POST['website']
        companyemail = request.POST['companyemail']
        companycontact = request.POST['companycontact']
        salarypackage = request.POST['salarypackage']
        experience =    request.POST['experience']
        newjob = JobDetails.objects.create(company_id=comp, jobname=jobname, companyname=companyname, companyaddress=companyaddress, jobdescription=jobdescription, qualification=qualification, responsibilities=responsibilities, location=location, companywebsite=companywebsite,companyemail=companyemail, companycontact=companycontact, salarypackage=salarypackage, experience=experience)

        message= "Job Post Successfully"
        return render(request, 'app/company/jobpost.html', {'msg':message})

def JobListPage(request):
    all_job = JobDetails.objects.all()
    return render(request, 'app/company/jobpostlist.html', {'alljob':all_job})
    
def CandidateJobListPage(request):
    all_job = JobDetails.objects.all()
    return render(request, 'app/job-list.html', {'alljob':all_job})

def CompanyLogout(request):
    del request.session['email']
    del request.session['password']
    return redirect('index')