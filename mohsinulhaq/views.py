from django.shortcuts import render
from django.views.generic import View


class index(View):

    def get(self, request):
        return render(request, 'index.html', {'title': 'Mohsin Ul Haq',
                                              'styles': ['index.css'],
                                              'scripts': ['index.js']})


class autocomplete(View):

    def get(self, request):
        return render(request, 'autocomplete.html',
                      {'title': 'Autocomplete',
                       'styles': ['autocomplete.css'],
                       'scripts': ['autocomplete.js']})


class radio(View):

    def get(self, request):
        return render(request, 'radio.html', {'title': 'Custom Radio Button',
                                              'styles': ['radio.css'],
                                              'scripts': []})


class regex(View):

    def get(self, request):
        return render(request, 'regex.html', {'title': 'Regex Validation',
                                              'styles': ['regex.css'],
                                              'scripts': ['regex.js']})


class facebook(View):

    def get(self, request):
        return render(request, 'facebook.html',
                      {'title': 'Facebook Integration',
                       'styles': ['facebook.css'],
                       'scripts': ['facebook.js', 'fbsdksetup.js']})


class pagination(View):

    def get(self, request):
        return render(request, 'pagination.html',
                      {'title': 'Pagination',
                       'styles': ['pagination.css'],
                       'scripts': ['pagination.js']})


class about(View):

    def get(self, request):
        return render(request, 'about.html', {'title': 'About Me',
                                              'styles': [],
                                              'scripts': []})


class test(View):

    def get(self, request):
        return render(request, 'test.html', {'title': 'Test',
                                             'styles': ['test.css'],
                                             'scripts': ['test.js']})
