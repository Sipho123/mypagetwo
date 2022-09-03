from django.urls import path
from xml.etree.ElementInclude import include
from django.views import View

from .views import(        
StoreView,
AllProductsView,
ProductDetailView,
AddToCartView,
MyCartView,
ManageCartView,
EmptyCartView,
CheckoutView,
CustomerRegistrationView,
CustomerLogoutView,
CustomerLoginView,
CustomerProfileView,
CustomerOrderDetailView,
AdminLoginView,
AdminHomeView,
AdminOrderDetailView,
AdminOrderListView,
AdminOrderStatusChangeView,
SearchView,
AdminProductListView,
AdminProductCreateView,
ForgotPasswordView,
PasswordResetView,
AdminLogoutView
)

app_name = 'our_store'
urlpatterns = [
        path('store/', StoreView.as_view(), name='store'),
        path('all-products/', AllProductsView.as_view(), name='allproducts'),
        path('product/<slug:slug>/', ProductDetailView.as_view(), name='productdetail'),
        path('add-to-cart-<int:pro_id>/', AddToCartView.as_view(), name='addtocart'),
        path('my-cart/', MyCartView.as_view(), name='mycart'),
        path('manage-cart/<int:cp_id>/', ManageCartView.as_view(), name='managecart'),
        path('empty-cart/', EmptyCartView.as_view(), name='emptycart'),
        path('checkout/', CheckoutView.as_view(), name='checkout'),
        
        path('register/', CustomerRegistrationView.as_view(), name='customerregistration'),
        path('logout/', CustomerLogoutView.as_view(), name='customerlogout'),
        path('login/', CustomerLoginView.as_view(), name='customerlogin'),
        path('forgot-password/', ForgotPasswordView.as_view(), name='forgotpassword'),
        path('password-reset/<email>/<token>/', PasswordResetView.as_view(), name='passwordreset'),
        
        path('profile/', CustomerProfileView.as_view(), name='customerprofile'),
        path('profile/order-<int:pk>/', CustomerOrderDetailView.as_view(), name='customerorderdetail'),
        
        path('search/', SearchView.as_view(), name='search'),

        # Admin Side pages

        path('admin-login/', AdminLoginView.as_view(), name='adminlogin'),
        path('admin-home/', AdminHomeView.as_view(), name='adminhome'),
        path('admin-order/<int:pk>/', AdminOrderDetailView.as_view(), name='adminorderdetail'),
        path('admin-logout/', AdminLogoutView.as_view(), name='adminlogout'),


        path('admin-all-orders/', AdminOrderListView.as_view(), name='adminorderlist'),
        path('admin-order-<int:pk>-change/', AdminOrderStatusChangeView.as_view(), name='adminorderstatuschange'),

        path('admin-product/list/', AdminProductListView.as_view(), name='adminproductlist'),
        path('admin-product/add/', AdminProductCreateView.as_view(), name='adminproductcreate'),



]

