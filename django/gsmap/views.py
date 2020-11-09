from django.contrib.auth.views import LoginView
from django.contrib.auth import login as auth_login
from django.http import HttpResponseRedirect

from gsmap.models import Workspace


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