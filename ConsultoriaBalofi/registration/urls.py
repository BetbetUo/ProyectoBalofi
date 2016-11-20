from django.conf.urls import url
from registration import views

app_name = "registration"
urlpatterns = [
	# sessions
	url(r'^$', views.LoginView.as_view(), name='login'),
	url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
	# register
	url(r'^register/$', views.RegisterView.as_view(), name='register'),
	url(r'^register/success/$',views.RegisterSuccessView.as_view(), name='register-success'),
]
