from django.conf.urls import url
from register import views
# SET THE NAMESPACE!
app_name = 'register'

urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    # url(r'^book/$',views.book,name='book'),

]
