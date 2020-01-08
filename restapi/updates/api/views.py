from updates.models import Update as UpdateModel
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
# creating, updating, deleting, retrieving(1) -- update model
import json
from .mixins import CSRFExemptMixin
from restapi.mixins import HttpResponseMixin
from updates.forms import UpdateModelForm

from .utils import is_json


class UpdateModelDetailAPIView(CSRFExemptMixin, HttpResponseMixin, View):
    '''
    retrieve update delete ---> object
    '''
    is_json = True

    def get_object(self, id=None):
        # try:
        #     obj = UpdateModel.objects.get(id=id)
        # except UpdateModel.DoesNotExist:
        #     obj = None
        qs = UpdateModel.objects.filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None

    def get(self, request, id, *args, **kwargs):
        obj = self.get_object(id=id)
        if obj is None:
            error_data = json.dumps({'message': 'update not found'})
            return self.render_to_response(error_data, status=404)
        json_data = obj.serialize()
        return self.render_to_response(json_data)

    def post(self, request, *args, **kwargs):
        json_data = json.dumps({'message': 'Now allowed, please use the /api/updates/ endpoint'})
        return self.render_to_response(json_data, 403)

    def put(self, request, id, *args, **kwargs):
        valid_json = is_json(request.body)
        if not valid_json:
            return self.render_to_response(json.dumps({'message': 'invalid data set json'}), status=400)
        obj = self.get_object(id=id)
        if obj is None:
            error_data = json.dumps({'message': 'update not found'})
            return self.render_to_response(error_data, status=404)

        data = json.loads(obj.serialize())
        passed_data = json.loads(request.body)

        for key, value in passed_data.items():
            data[key] = value

        form = UpdateModelForm(data, instance=obj)
        if form.is_valid():
            obj = form.save(commit=True)
            obj_data = json.dumps(data)
            return self.render_to_response(obj_data, status=201)
        if form.errors:
            data = json.dumps(form.errors)
            return self.render_to_response(data, status=400)
        json_data = json.dumps({'message': 'something'})
        return self.render_to_response(json_data)

    def delete(self, request, id, *args, **kwargs):
        obj = self.get_object(id=id)
        if obj is None:
            error_data = json.dumps({'message': 'update not found'})
            return self.render_to_response(error_data, status=404)
        deleted_, item_deleted = obj.delete()
        if deleted_ == 1:
            json_data = json.dumps({'message': 'Successfully deleted'})
            return self.render_to_response(json_data)
        error_data = json.dumps({'message': 'could not delete item'})
        return self.render_to_response(error_data, status=404)


class UpdateModelListAPIView(CSRFExemptMixin, HttpResponseMixin, View):
    '''
    list view ---> retrieve detail view
    create view
    udpate
    delete
    '''
    is_json = True
    queryset = None

    def get_queryset(self):
        self.queryset = UpdateModel.objects.all()
        return self.queryset

    def get_object(self, id=None):
        if id is None:
            return None
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None

    def get(self, request, *args, **kwargs):
        data = json.loads(request.body)
        passed_id = data.get('id', None)
        if passed_id is not None:
            obj = self.get_object(id=passed_id)
            if obj is None:
                error_data = json.dumps({'message': 'Object not found'})
                return self.render_to_response(error_data, status=404)
            json_data = obj.serialize()
            return self.render_to_response(json_data)
        else:
            qs = self.get_queryset()
            json_data = qs.serialize()
            return self.render_to_response(json_data)

    def post(self, request, *args, **kwargs):
        form = UpdateModelForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=True)
            obj_data = obj.serialize()
            return self.render_to_response(obj_data, status=201)
        if form.errors:
            data = json.dumps(form.errors)
            return self.render_to_response(data, status=400)
        data = json.dumps({"message": "You cannot delete an entire listr", "status": 400})
        return self.render_to_response(data)

    def put(self, request, *args, **kwargs):
        valid_json = is_json(request.body)
        if not valid_json:
            return self.render_to_response(json.dumps({'message': 'invalid data set json'}), status=400)

        passed_data = json.loads(request.body)
        passed_id = passed_data.get('id', None)
        if not passed_id:
            error_data = json.dumps({'message': 'invalid ID'})
            return self.render_to_response(error_data, status=404)
        obj = self.get_object(id=passed_id)
        if obj is None:
            error_data = json.dumps({'message': 'Object  not found'})
            return self.render_to_response(error_data, status=404)

        data = json.loads(obj.serialize())
        for key, value in passed_data.items():
            data[key] = value

        form = UpdateModelForm(data, instance=obj)
        if form.is_valid():
            obj = form.save(commit=True)
            obj_data = json.dumps(data)
            return self.render_to_response(obj_data, status=201)
        if form.errors:
            data = json.dumps(form.errors)
            return self.render_to_response(data, status=400)
        json_data = json.dumps({'message': 'something'})
        return self.render_to_response(json_data)

    def delete(self, request, *args, **kwargs):
        valid_json = is_json(request.body)
        if not valid_json:
            return self.render_to_response(json.dumps({'message': 'invalid data set json'}), status=400)
        passed_data = json.loads(request.body)
        passed_id = passed_data.get('id', None)
        if not passed_id:
            error_data = json.dumps({'message': 'invalid ID'})
            return self.render_to_response(error_data, status=404)
        obj = self.get_object(id=passed_id)
        if obj is None:
            error_data = json.dumps({'message': 'update not found'})
            return self.render_to_response(error_data, status=404)
        deleted_, item_deleted = obj.delete()
        if deleted_ == 1:
            json_data = json.dumps({'message': 'Successfully deleted'})
            return self.render_to_response(json_data)
        error_data = json.dumps({'message': 'could not delete item'})
        return self.render_to_response(error_data, status=404)
