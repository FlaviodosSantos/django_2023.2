from urllib import response
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import HotelForm
from .models import Hotel


def hotel_image_view(request):

    if request.method == 'POST':
        form = HotelForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = HotelForm()

    return render(request, 'hotel_image_form.html', {'form': form})


def success(request):
    return HttpResponse('successfully uploaded')


def index(request):
    if request.method == 'GET':
        hotels = Hotel.objects.all()
        return render(request, 'display_imagens.html', {'hotel_images': hotels})


def display_hotel_images(request):

    if request.method == 'GET':
        hotels = Hotel.objects.all()
        return render(request, 'display_hotel_images.html',
                      {'hotel_images': hotels})


def hotel_delete(request, id):
    if request.method == 'GET':
        # post = get_object_or_404(Post, pk=id)
        hotel = get_object_or_404(Hotel, pk=id)

        if hotel.hotel_Main_Img:
            hotel.hotel_Main_Img.delete()

        hotel.delete()
        return render(request, 'display_hotel_images.html',
                      {'hotel_images': hotel})
    else:
        return HttpResponse('Error ao deletar')
