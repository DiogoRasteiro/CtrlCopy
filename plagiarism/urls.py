from django.urls import path
from . import views

app_name = 'plagiarism'

# This method connects the URLs the user types to a method in views.py. The methods are used to perform backend actions and then render the HTML templates
# Each URL itself has a path, an associated method and a name which is used internally to refer to it


urlpatterns = [
        # Completed Pages:

        # The homepage
        path('', views.index, name='index'),
        # A page to view the documents individually
        path('document/<int:document_id>/', views.document, name = 'document'),
        # A page to submit the documents
        path('submit/', views.submit, name = 'SubmitDocument'),
        # Login page
        path('login/', views.login, name = 'Login'),
        # About Us page
        path('about/', views.about_us, name = 'About'),
        # Logout
        path('logout/', views.logout, name = 'Logout'),

        path('submitted/', views.submitted, name = 'Submitted'),

        path('welcome/', views.welcome, name = 'Welcome'),

        # Pages we have yet to implement

        # # Middle page to verify the correctness of the document and configure settings for the detetor
        # # This page should only be accessed by submitting the form in 'Submit Document'
        # path('analyzedoc', views.analyzedoc, name = 'Analyse Document'),

        # # Page to compare 2 documents by a professor
        # # This page should only be accessed by a professor in the 'Plagiarism Evaluation' page
        # path('compare2docs', views.compare2docs, name = 'Document Comparison'),

        # # Page to show the results of a plagiarism test
        # # This can only be accessed after the 'Analyze Document'
        # path('plagevaluation', views.plagevaluation, name = 'Plagiarism Evaluation'),


        # # Page to reject a submitted document by a professor
        # path('rejected', views.rejected, name = 'Rejected'),

        # # Public profile
        path('profile', views.profile, name = 'Profile'),

        # # Edit/private profile
        # path('editprofile', views.editprofile, name = 'Edit Profile'),


]
