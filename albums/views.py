import json
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from rest_framework import viewsets
from albums.models import Album
from albums.serializers import AlbumSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class JSONResponseMixin(object):

    def response_handler(self):
        format = self.request.GET.get('format', None)

        if format == 'json':
            return self.render_to_json_response()

        context = self.get_context_data()
        return self.render_to_response(context)

    def render_to_json_response(self):
        data = self.get_data()
        return JsonResponse(data, safe=False)


class AlbumListView(JSONResponseMixin, ListView):
    model = Album
    template_name = 'album_list.html'
    paginate_by = 2

    def get_data(self):
        data = [{
            'name': album.name,
            'cover': album.cover.url,
            'slug': album.slug,
            'artist': json.loads(
                serializers.serialize('json',
                                      [album.artist, ],
                                      fields=('first_name', 'last_name'))),
        } for album in self.object_list]

        return data

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        return self.response_handler()

    def get_context_data(self, **kwargs):
        context = super(AlbumListView, self).get_context_data(**kwargs)
        page = self.request.GET.get('page', None)

        if page is None:
            page = 1

        context.update({'page': page})

        return context

    def get_queryset(self):
        if self.kwargs.get('artist'):
            queryset = self.model.objects.filter(
                artist__slug__contains=self.kwargs['artist'])
        else:
            queryset = super(AlbumListView, self).get_queryset()

        return queryset


class AlbumDetailView(JSONResponseMixin, DetailView):
    model = Album
    template_name = 'album_detail.html'

    def get_data(self):
        data = {
            'name': self.object.name,
            'cover': self.object.cover.url,
            'slug': self.object.slug,
            'artist': json.loads(
                serializers.serialize('json',
                                      [self.object.artist, ],
                                      use_natural_foreign_keys=True,
                                      use_natural_primary_keys=True)),
            'tracks': [t.name for t in self.object.track_set.all()]
        }

        return data

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return self.response_handler()
