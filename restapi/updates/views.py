import json
from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from restapi.mixins import JsonResponseMixin
from .models import Update


def json_example_view(request):
    data = {
        "count": 1000,
        "content": "Some new Content"
    }
    json_data = json.dumps(data)
    return HttpResponse(json_data, content_type='application/json')


class JsonCVB(View):
    def get(self, request, *args, **kwargs):
        data = {
            "count": 1000,
            "content": "Some new Content"
        }
        return JsonResponse(data)


class JsonCVB2(JsonResponseMixin, View):
    def get(self, request, *args, **kwargs):
        data = {
            "count": 1000,
            "content": "Some new Content"
        }
        return self.render_to_json_response(data)


class SerializedDetaileView(View):
    def get(self, request, *args, **kwargs):
        obj = Update.objects.get(id=1)
        json_data = obj.serialize()
        return HttpResponse(json_data, content_type='application/json')


class SerializedListView(View):
    def get(self, request, *args, **kwargs):
        # qs = Update.objects.all()
        # data = serialize("json", qs, fields=('user', 'content'))
        json_data = Update.objects.all().serialize()
        return HttpResponse(json_data, content_type='application/json')
