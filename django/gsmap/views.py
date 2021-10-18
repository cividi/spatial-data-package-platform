from django.contrib.auth.views import LoginView
from django.contrib.auth import login as auth_login
from django.http import HttpResponseRedirect
from django.http import HttpResponse

from rest_framework import generics, parsers
from rest_framework.response import Response

from gsmap.models import Workspace, Snapshot, Annotation, Category, Attachement

from .permissions import IsUser
from .serializers import SnapshotDataUploadSerializer, AnnotationSerializer, AnnotationRateUpSerializer


class CustomLoginView(LoginView):
    """
    Customized to include Workspace data in the request cookie
    """
    def get_workspace_id(self, user):
        """
        Retrieves last user Workspace.
        """
        workspace = Workspace.objects.filter(
            snapshots__user=user
        ).last()
        if workspace:
            return workspace.get_relative_url()
        return None

    def form_valid(self, form):
        """Security check complete. Log the user in."""
        user = form.get_user()
        auth_login(self.request, user)
        response = HttpResponseRedirect(self.get_success_url())
        # insert workspace info
        workspace_id = self.get_workspace_id(user)
        if workspace_id:
            response.set_cookie('workspaceid', workspace_id)
        return response


def logout(request):
    response = HttpResponseRedirect('/')
    response.delete_cookie('sessionid')
    response.delete_cookie('workspaceid')
    return response


class SnapshotFileUploadView(generics.UpdateAPIView):
    permission_classes = [IsUser,]
    queryset = Snapshot.objects.all()
    serializer_class = SnapshotDataUploadSerializer
    lookup_url_kwarg = 'snapshot_id'
    http_method_names = ['patch',]
    parser_classes = [parsers.MultiPartParser]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)  # Enable PATCH
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

class AnnotationCreateView(generics.CreateAPIView):
    queryset = Annotation.objects.all()
    serializer_class = AnnotationSerializer
    http_method_names = ['post',]
    #parser_classes = [parsers.MultiPartParser]

class AnnotationRateUpView(generics.UpdateAPIView):
    queryset = Annotation.objects.all()
    serializer_class = AnnotationRateUpSerializer
    lookup_url_kwarg = 'annotation_id'
    http_method_names = ['patch',]

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        data = {"rating": instance.rating + 1}
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        
        return Response(serializer.data)

#class AnnotationPublishView(request, annotation_id, publishKeyHex):
    #annotation  = get_object_or_404(Annotation, id=annotation_id)
    # account.public = True
    # account.save() 
    # return HttpResponse("annotation_id: %s." % annotation_id)
