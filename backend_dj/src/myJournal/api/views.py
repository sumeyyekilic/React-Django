from backend_dj.src.myJournal.models import bulletJournal
from rest_framework.generics import ListAPIView
from .serialzers import bulletJSerialzer

class bulletJListView(ListAPIView):
    myqueryset=bulletJournal.objects.all()
    serializer_class=bulletJSerialzer


class bulletJDetailtView(ListAPIView):
    myqueryset=bulletJournal.objects.all()
    serializer_class=bulletJSerialzer