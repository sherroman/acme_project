from django.urls import include, path

from . import views

app_name = 'birthday'

urlpatterns = [
    path('', include('pages.urls')),
    path('list/', views.BirthdayListView.as_view(), name='list'),
    path('<int:pk>/', views.BirthdayDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', views.BirthdayUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/',
         views.BirthdayDeleteView.as_view(), name='delete'),
    path('create/', views.BirthdayCreateView.as_view(), name='create'),
]
