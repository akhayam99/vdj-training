from django.http import JsonResponse

def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''



def index(request):
    return JsonResponse([
    {
      "id": 1,
      "name": "Product 1",
      "price": 100,
      "stock": 10,
    },
    {
      "id": 2,
      "name": "Product 2",
      "price": 200,
      "stock": 20,
    },
    {
      "id": 3,
      "name": "Product 3",
      "price": 300,
      "stock": 30,
    },
    {
      "id": 4,
      "name": "Product 4",
      "price": 400,
      "stock": 40,
    },
    {
      "id": 5,
      "name": "Product 5",
      "price": 500,
      "stock": 50,
    }
    ], safe = False
  )