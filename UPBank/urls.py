"""UPBank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from App import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing_view, name='landing_page'),
    path('dashboard/', views.dashboard_view, name="dashboard"),
    path('contact-us/', views.contact_us_view, name="contact_us"),
    path('loan-calculator/', views.loan_calculator_view, name='loan-calculator'),
    path('fund-deposit/', views.fund_deposit_view, name="fund_deposit"),
    path('add-deposit/', views.add_deposit, name="add_deposit"),
    path('otc-payment/', views.otc_payment, name="otc_payment"),

    # Login/Register
    path('accounts/', include('accounts.urls')),
    path('login/', views.login_redirect_view, name='login'),
    path('signup/', views.signup_redirect_view, name='signup'),
    path('logout/', views.logout_view, name="logout"),
   # path('resetpassword/', views.resetPasswordView, name="resetpassword"),
   # path('password_reset', views.password_reset_request, name="password_reset"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password/password_reset_complete.html'), name='password_reset_complete'),

    # Bank Officer URLs
    path('dashboard/pending', views.dashboard_pending_view, name="dashboard-pending"),
    path('dashboard/approved', views.dashboard_approved_view, name="dashboard-approved"),
    path('dashboard/rejected', views.dashboard_rejected_view, name="dashboard-rejected"),

    path('applicant_information/<int:pk>', views.applicant_information_view, name="applicant-information"),
    path('borrower_information/<int:pk>', views.borrower_information_view, name="borrower-information"),

    # Borrower URLs
    path('myloans', views.borrower_loanlist, name="borrower-loanlist"),
    path('loan/<int:pk>', views.loan_information_view, name="loan-information"),
    path('applyloan', views.applyforLoan, name="apply-for-loan"),
]
