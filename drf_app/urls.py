from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import RegisterAPI, EmployeeListCreate, EmployeeRUD, Logout

app_name = 'drf_app'
# router = DefaultRouter()
#
# router.register('reg/', RegisterAPI, basename='user')
# router.register('td_model_api/', EmployeeViewSet, basename='employee')
# router.register('std_model_api/<int:pk>/', EmployeeViewSet, basename='employee')
#
# urlpatterns = router.urls
urlpatterns = [
    path('', RegisterAPI.as_view(), name='register'),
    # path('std_model_api/', EmployeeViewSet, name='employee'),
    # path('std_model_api/<int:pk>/', EmployeeViewSet, name='employee'),
    # path('emp_list/', EmployeeList.as_view(), name='student'),
    # path('emp_create/', EmployeeCreate.as_view(), name='student'),
    # path('emp_retrieve/<int:pk>/', EmployeeRetrieve.as_view(), name='student'),
    # path('emp_update/<int:pk>/', EmployeeUpdate.as_view(), name='student'),
    # path('emp_delete/<int:pk>/', EmployeeDestroy.as_view(), name='student'),
    path('emp/', EmployeeListCreate.as_view(), name='employee'),
    path('emp/<int:pk>/', EmployeeRUD.as_view(), name='employee'),
    path('logout/', Logout.as_view(), name='logout'),
    #
]
