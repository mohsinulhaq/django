from django.shortcuts import render
from django.views.generic import View


class Github(View):
    def get(self, request):
        return render(request, 'github.html', {'title': 'Mohsin Ul Haq'})


class Autocomplete(View):
    def get(self, request):
        return render(request, 'autocomplete.html', {'title': 'Autocomplete'})


class Radio(View):
    def get(self, request):
        return render(request, 'radio.html', {'title': 'Custom Radio Button'})


class Regex(View):
    def get(self, request):
        return render(request, 'regex.html', {'title': 'Regex Validation'})


class Facebook(View):
    def get(self, request):
        return render(request, 'facebook.html', {'title': 'Facebook Integration'})


class Pagination(View):
    def get(self, request):
        return render(request, 'pagination.html', {'title': 'Pagination'})


class Test(View):
    def get(self, request):
        return render(request, 'test.html', {'title': 'Test'})
