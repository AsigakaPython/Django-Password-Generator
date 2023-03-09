import random

from django.shortcuts import render


def home(request):
    return render(request, 'generator/home.html')


def about(request):
    return render(request, 'generator/about.html')


def password(request):
    characters = list("abcdefg")
    numbers = list("1234567890")
    uppercase = list("ABCDEFG")
    specials = list("!@#$%^&*")
    length = request.GET.get("length")

    with_uppercase = request.GET.get("uppercase")
    with_specials = request.GET.get("specials")
    with_numbers = request.GET.get("numbers")

    result_password = ""

    for i in range(int(length)):
        all_possible_list = characters

        if with_uppercase:
            all_possible_list.extend(uppercase)
        if with_specials:
            all_possible_list.extend(specials)
        if with_numbers:
            all_possible_list.extend(numbers)

        result_password += random.choice(all_possible_list)

    return render(request, 'generator/password.html', {'password': result_password})
