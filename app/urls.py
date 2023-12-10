from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.IndexPage, name="index"),
    path("signup/", views.SignupPage, name="signup"),
    path("register/", views.RegisterUser, name="register"),
    path("otppage/", views.OTPPAGE, name="otppage"),
    path("otp", views.OtpVerify, name="otp"),
    path("loginpage/", views.LoginPage, name="loginpage"),
    path("loginuser", views.LoginUser, name="loginuser"),
    path("profile/<int:pk>", views.ProfilePage, name="profile"),
    path("updateprofile/<int:pk>", views.UpdateProfile, name="updateprofile"),
    path("joblist/", views.CandidateJobListPage, name="joblist"),

    # ------------------- Company ---------------------

    path("company/", views.CompanyIndex, name="companyindex"),
    path("companyprofile/<int:pk>", views.CompanyProfile, name="companyprofile"),
    path("updatecompanyprofile/<int:pk>", views.CompanyProfileUpdate, name="updatecompanyprofile"),
    path("jobpostpage/", views.JobPostPage, name="jobpostpage"),
    path("jobpost/", views.JobPost, name="jobpost"),
    path("joblistpage/", views.JobListPage, name='joblistpage'),
    path("companylogout/", views.CompanyLogout, name='companylogout'),
]
