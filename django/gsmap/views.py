import hashlib
import os

from django.contrib.auth.views import LoginView
from django.contrib.auth import login as auth_login
from django.http import HttpResponseRedirect

from django.views.generic import DetailView

from rest_framework import generics, parsers, renderers
from rest_framework.response import Response

from gsmap.models import Workspace, Snapshot, Annotation, Category, State, Attachement

from .permissions import IsUser
from .serializers import SnapshotDataUploadSerializer, AnnotationSerializer, AnnotationRateUpSerializer, AttachmentsDataUploadSerializer

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY') or os.getenv(
    'DJANGO_SECRET_KEY_DEV')


class StaffBrowsableMixin(object):
    def get_renderers(self):
        """
        Add Browsable API renderer if user is staff.
        """
        rends = self.renderer_classes
        if self.request.user and self.request.user.is_superuser:
            rends.append(renderers.BrowsableAPIRenderer)
        return [renderer() for renderer in rends]


class CustomLoginView(LoginView):
    """
    Customized to include Workspace data in the request cookie
    """
    def get_workspace_id(self, user):
        """
        Retrieves last user Workspace.
        """
        workspace = Workspace.objects.filter(snapshots__user=user).last()
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


class SnapshotFileUploadView(StaffBrowsableMixin, generics.UpdateAPIView):
    permission_classes = [
        IsUser,
    ]
    queryset = Snapshot.objects.all()
    serializer_class = SnapshotDataUploadSerializer
    lookup_url_kwarg = 'snapshot_id'
    http_method_names = [
        'patch',
    ]
    parser_classes = [parsers.MultiPartParser]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance,
                                         data=request.data,
                                         partial=True)  # Enable PATCH
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


class AnnotationCreateView(StaffBrowsableMixin, generics.CreateAPIView):
    queryset = Annotation.objects.all()
    serializer_class = AnnotationSerializer
    http_method_names = [
        'post',
    ]
    # parser_classes = [parsers.MultiPartParser]


class AnnotationRateUpView(StaffBrowsableMixin, generics.UpdateAPIView):
    queryset = Annotation.objects.all()
    serializer_class = AnnotationRateUpSerializer
    lookup_url_kwarg = 'annotation_id'
    http_method_names = [
        'patch',
    ]

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        data = {}
        serializer = self.get_serializer(instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)


class AnnotationPublishView(DetailView):
    model = Annotation
    template_name = "annotation_publish.html"

    def get_queryset(self):
        return Annotation.objects.filter(id=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nochange'] = False

        context['workspaceHash'] = self.object.workspace.pk
        context['snapshotHash'] = self.object.workspace.snapshots.first().pk
        context['contactName'] = self.object.workspace.annotations_contact_name
        context[
            'contactEmail'] = self.object.workspace.annotations_contact_email

        if self.object.public:
            context['nochange'] = True
            return context
        context['publishKeyHex'] = self.kwargs['publishKeyHex']
        recipient = self.object.author_email
        idstr = str(self.object.id)
        uniquestr = recipient + idstr + SECRET_KEY
        publishKeyHex = hashlib.md5(uniquestr.encode()).hexdigest()
        context['success'] = False

        if publishKeyHex == self.kwargs['publishKeyHex']:
            self.object.public = True
            self.object.save()
            self.object.refresh_from_db()
            context['success'] = True
        return context


class AnnotationAttachmentsUploadView(StaffBrowsableMixin,
                                      generics.UpdateAPIView):
    queryset = Attachement.objects.all()
    serializer_class = AttachmentsDataUploadSerializer
    lookup_url_kwarg = 'annotation_id'
    http_method_names = [
        'patch',
    ]
    parser_classes = [parsers.MultiPartParser]

    def update(self, request, *args, **kwargs):

        data = [{
            'document': document,
            'annotation': kwargs['annotation_id']
        } for _, document in request.data.items()]

        serializer = self.get_serializer(
            None,
            data=data,
            partial=True,  # Enable PATCH
            many=True)

        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)
