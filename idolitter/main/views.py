from django.template.response import TemplateResponse
from django.views import View

class GroupView(View):
  def get(self, request, *args, **kwargs):
    context = {
      'message': "Hello World!",
    }
    return TemplateResponse(request, 'main/group.html', context)

group = GroupView.as_view()
