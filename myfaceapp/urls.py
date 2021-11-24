from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name="index"),
    path("signup/",views.signup,name="signup"),
    path('profile/',views.profile,name="profile"),
    path("upload-profile/",views.profile_upload,name="uploadprofile"),
    # path("profile-upload/",views.profile_upload,name="profie-upload"),
    path("logout/",views.logout1,name="logout"),
    path("login1/",views.login1,name="login1"),
    # path("login/",views.login1,name="login"),
    # path("upload-post",views.uploadpost,name="upload-post"),
    path("upload-post",views.uploadpost,name="upload-post"),
    path("search/",views.search,name="search"),
    path("follow-user",views.follow_user,name="follow")
]
