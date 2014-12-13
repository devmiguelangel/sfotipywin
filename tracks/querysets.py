from django.db.models import QuerySet


class TrackQuerySet(QuerySet):

    def top(self):
        return self.order_by('-listen')
