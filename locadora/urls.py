from django.urls import path
from .views import ( 
    home,CarListView, CarDetailView, CarCreateView, CarUpdateView, CarDeleteView,
    UserListView, UserDetailView, UserCreateView, UserUpdateView, UserDeleteView,
    ReservationListView, ReservationDetailView, ReservationCreateView, ReservationUpdateView, ReservationDeleteView
)
urlpatterns = [
    path('', home, name='home'),
    # URLs para Carro
    path('cars/', CarListView.as_view(), name='car_list'),
    path('cars/<int:pk>/', CarDetailView.as_view(), name='car_detail'),
    path('cars/create/', CarCreateView.as_view(), name='car_create'),
    path('cars/<int:pk>/update/', CarUpdateView.as_view(), name='car_update'),
    path('cars/<int:pk>/delete/', CarDeleteView.as_view(), name='car_delete'),

    # URLs para Usuário
    path('users/', UserListView.as_view(), name='user_list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('users/create/', UserCreateView.as_view(), name='user_create'),
    path('users/<int:pk>/update/', UserUpdateView.as_view(), name='user_update'),
    path('users/<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),

    # URLs para Reserva
    path('reservations/', ReservationListView.as_view(), name='reservation_list'),
    path('reservations/<int:pk>/', ReservationDetailView.as_view(), name='reservation_detail'),
    path('reservations/create/', ReservationCreateView.as_view(), name='reservation_create'),
    path('reservations/<int:pk>/update/', ReservationUpdateView.as_view(), name='reservation_update'),
    path('reservations/<int:pk>/delete/', ReservationDeleteView.as_view(), name='reservation_delete'),
]



