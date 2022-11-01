from django.urls import path


from . import views



urlpatterns = [
    path('', views.getEndpoints,name="home"),
    path('payment', views.createPayment,name="payment"),
    path('getpay', views.getPayments,name="getpay"),

] 