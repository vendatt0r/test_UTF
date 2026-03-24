from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Prefetch

from .models import FoodCategory, Food
from .models import FoodListSerializer


class FoodListView(APIView):
    def get(self, request):
        published_foods = Food.objects.filter(is_publish=True)

        categories = FoodCategory.objects.filter(
            food__is_publish=True
        ).distinct().prefetch_related(
            Prefetch('food', queryset=published_foods)
        ).order_by('order_id')

        serializer = FoodListSerializer(categories, many=True)
        return Response(serializer.data)
