from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.core.exceptions import SuspiciousOperation


class ItemManipulationView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        data = [
            {
                'name': "Biriyani",
                'price': 100,
                'subitems': [
                    {
                        'name': 'Raitha',
                        'price': 30,
                        'quantity': '100ml'
                    },
                    {
                        'name': "Kuruma",
                        'price': 40,
                        'quantity': '30ml'
                    }
                ]
            },
            {
                'name': "Parotta",
                'price': 20,
                'subitems': [
                    {
                        'name': 'Raitha',
                        'price': 10,
                        'quantity': '100ml'
                    },
                    {
                        'name': "Kuruma",
                        'price': 40,
                        'quantity': '30ml'
                    }
                ]
            },
            {
                'name': "Idli",
                'price': 50,
                'subitems': [
                    {
                        'name': 'Sambar',
                        'price': 30,
                        'quantity': '100ml'
                    },
                    {
                        'name': "Cocount Chutney",
                        'price': 40,
                        'quantity': '30ml'
                    },
                    {
                        'name': "Kaara Chutney",
                        "price": 60,
                        'quantity': "40ml"
                    }
                ]
            },

        ]
        return Response(data)

        def post(self, request):
            pass
