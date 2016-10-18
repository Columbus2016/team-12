"""sqladmin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from data import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # ex: /polls/
    # url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
#    url(r'^(?P<question_id>[0-9]+)/results/$', view=views.results, kwargs=1),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    #url(r'^admin', '')

    url(r'^results/(?P<question_id>[0-9]+)/$', views.results),

    url(r'staticTest/$', views.staticTest),


#(r'^about', 'django.views.generic.simple.direct_to_template', {'template': 'path/to/about_us.html'}),



 #   url(r'^')

]
