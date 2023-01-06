from django.shortcuts import render, redirect
from django.utils import timezone
from . import models, forms
from django.core.paginator import Paginator, EmptyPage
from django.views.generic import ListView, DetailView, View
from django_countries import countries

# Create your views here.

class HomeView(ListView):
    model = models.House
    paginate_by = 10
    paginate_orphans = 5
    ordering = "name"
    # ordering = "created"
    page_kwarg = "page" 
    context_object_name = "houses"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = timezone.now
        context["now"] = now
        
        return context
    pass

class HouseDetail(DetailView):
    model = models.House

class SearchView(View):
    def get(self, request):
        country = request.GET.get("country")
        houses = models.House.objects.all()
        if country:
            form = forms.SearchForm(request.GET)
            if form.is_valid():
                country = form.cleaned_data.get("country")
                city = form.cleaned_data.get("city")
                room_type = form.cleaned_data.get("room_type")
                price = form.cleaned_data.get("price")
                guests = form.cleaned_data.get("guests")
                bedrooms = form.cleaned_data.get("bedrooms")
                beds = form.cleaned_data.get("beds")
                baths = form.cleaned_data.get("baths")
                amenities = form.cleaned_data.get("amenities")
                facilities = form.cleaned_data.get("facilities")

                # search argument
                filter_args = {}
                filter_args["country"] = country
                if city != "":
                    filter_args["city__startswith"] = city
                if room_type is not None:
                    filter_args["room_type"] = room_type
                if price is not None:
                    filter_args["price__lte"] = price
                if guests is not None:
                    filter_args["guests__gte"] = guests
                if bedrooms is not None:
                    filter_args["bedrooms__gte"] = bedrooms
                if beds is not None:
                    filter_args["beds__gte"] = beds
                if baths is not None:
                    filter_args["baths__gte"] = baths
                for amenity in amenities:
                    filter_args["amenities"] = amenity
                for facility in facilities:
                    filter_args["facilities"] = facility
                houses = models.House.objects.filter(**filter_args)
        else:
            form = forms.SearchForm()

        context = {"form": form, "houses":houses} 

        return render(request, "house/search.html", context)

# def search2(request):
#     city = request.GET.get("city", "")
#     city = str.capitalize(city)
#     country = request.GET.get("country", "")
#     house_type = int(request.GET.get("house_type", 0))
#     price = int(request.GET.get("price", 0))
#     guest = int(request.GET.get("guest", 0))
#     bedroom = int(request.GET.get("bedroom", 0))
#     bed = int(request.GET.get("bed", 0))
#     bath = int(request.GET.get("bath", 0))

#     s_amenities = request.GET.getlist("amenities") 
#     s_facilities = request.GET.getlist("facilities") 

#     form = {
#         "city": city,
#         "s_country": country,
#         "s_house_type": house_type,
#         "price": price,
#         "guest": guest,
#         "bedroom": bedroom,
#         "bed": bed,
#         "bath": bath,
#         "s_amenities": s_amenities,
#         "s_facilities": s_facilities,
#     }
#     house_types = models.HouseType.objects.all()
#     amenities = models.Amenity.objects.all()
#     facilities = models.Facility.objects.all()
#     choices = {
#         "countries": countries,
#         "house_types": house_types,
#         "amenities": amenities,
#         "facilities": facilities,
#     }

#     filter_args = {}
#     if city != "": filter_args["city__startswith"] = city
#     if country != "": filter_args["country"] = country

#     if house_type != 0: filter_args["house_type__pk"] = house_type
#     if price != 0: filter_args["price__lte"] = price
#     if guest != 0: filter_args["guest__gte"] = guest
#     if bedroom != 0: filter_args["bedroom__gte"] = bedroom
#     if bed != 0: filter_args["bed__gte"] = bed
#     if bath != 0: filter_args["bath__gte"] = bath

#     if len(s_amenities) > 0:
#         for s_amenity in s_amenities:
#             filter_args["amenities__pk"] = int(s_amenity)
#     if len(s_facilities) > 0:
#         for s_facility in s_facilities:
#             filter_args["amenities__pk"] = int(s_facility)

#     houses = models.House.objects.filter(**filter_args)

#     return render(request, "house/search.html", {**form, **choices, "houses":houses})

