"""Users URLs."""

# Django
from django.urls import path

# View
from users import views


urlpatterns = [

    # Management
    path(
        route='login/',
        view=views.LoginView.as_view(),
        name='login'
    ),
    path(
        route='logout/',
        view=views.LogoutView.as_view(),
        name='logout'
    ),
    path(
        route='signup/',
        view=views.SignupView.as_view(),
        name='signup'
    ),
    path(
        route='me/profile/',
        view=views.UpdateProfileView.as_view(),
        name='update'
    ),
    
    # Posts
    path(
        route='profile/<str:username>/',
        view=views.UserDetailView.as_view(), #Para que meusytre el detalle del usuario. Ver views.py de Users.
        name='detail'                        #TemplateView.as_view(template_name='users/detail.html') CODIGO ANTIGUO.                                   
    ),                                       #Este acepta el <str:usermane> cualquier dato, no precisamente el username real.


]
