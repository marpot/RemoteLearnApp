"""RemoteLearnApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import include
from RemoteLearnApp import urls


urlpatterns = [
    url(r'^admin/', admin.site.urls),    	
   # url(r'^$', views.index, name='site_index')
    ]


"""
To zrób,odpowiedź z neta:

  1. Bootstrap mozesz zainstalowac ale mozesz tez w pliku css uzyc CDN czyli jeden link zalatwia wszystko. Strona podczas ladowania pobiera nie jako tego bootstrapa wiec jesli chciales bootstrapa tylko do strony to wywal to i uzyj CDN w pliku css.
2. Nie znajduje u Ciebie katalogu templates gdzie przechowujesz pliki html i do tego w settingsach musisz miec podana sciezke do obslugi tego
3. We views.py musisz jakos miec uwzgledniony ten template i do tego urls.py do zrobienia zeby django wiedzialo jak obslugiwac urly tworzone przez Ciebie
4. Katalog static brak gdzie przechowujesz pliki statyczne w tym plik css"""