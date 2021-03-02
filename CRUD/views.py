from django.shortcuts import render
from rest_framework.response import Response
from .models import Quote
from .serializers import QuoteSerializer
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def QuoteList(request):
    Quotes = Quote.objects.all()
    serializer = QuoteSerializer(Quotes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def QuoteDetail(request, pk):
    quote = Quote.object.all(id=pk)
    serializer = QuoteSerializer(quote, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def QuoteCreate(requests):
    serializer = QuoteSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['GET'])
def QuoteUpdate(request, pk):
    quote = Quote.objects.get(id=pk)

    serializer = QuoteSerializer(instance=quote, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
    
@api_view(['DELETE'])
def QuoteDelete(request, pk):
    quote = Quote.objects.get(id=pk)
    quote.delete()

