from django.conf import settings
from django.contrib import admin
# from django.contrib.auth.views import LoginView
from gsmap.views import CustomLoginView, logout, SnapshotFileUploadView, AnnotationCreateView, AnnotationRateUpView, AnnotationPublishView, AnnotationAttachmentsUploadView
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.urls import include
from graphene_django.views import GraphQLView
from gsuser.views import OIDCLogoutView
from mozilla_django_oidc.views import OIDCAuthenticationRequestView

urlpatterns = [
    path('api/v1/snapshots/<str:snapshot_id>/',
         csrf_exempt(SnapshotFileUploadView.as_view())),
    path('api/v1/annotations/', AnnotationCreateView.as_view()),
    path('api/v1/annotations/<str:annotation_id>/attachments/',
         csrf_exempt(AnnotationAttachmentsUploadView.as_view())),
    path('api/v1/rateupannotation/<str:annotation_id>/',
         AnnotationRateUpView.as_view()),
    path('annotation/publish/<int:pk>/<str:publishKeyHex>',
         AnnotationPublishView.as_view(),
         name='annotation-publish'),
    path('markdownx/', include('markdownx.urls')), 
    path('account/login/',
         CustomLoginView.as_view(template_name='registration/login.html'),
         name='login'),
    path('account/logout/', logout, name='logout'),
    path('gmanage/', admin.site.urls),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
]

if settings.OIDC_ACTIVE:
     urlpatterns = [
          path('gmanage/login/', OIDCAuthenticationRequestView.as_view(), name='oidc_login'),
          path('gmanage/logout/', OIDCLogoutView.as_view(), name='oidc_logout'),
     ] + urlpatterns
     urlpatterns += [
          path('oidc/', include('mozilla_django_oidc.urls')),
     ]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static('/downloads', document_root=settings.MEDIA_ROOT)
