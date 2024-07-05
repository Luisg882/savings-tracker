from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile
from .forms import AddMoney

def home_view(request):
    if request.user.is_authenticated:
        return redirect('profile')
    return render(request, 'account/index.html')

@login_required
def profile_view(request):
    profile = Profile.objects.get(user=request.user)
    saving_pots_list = profile.saving_pots.all()

    paginator = Paginator(saving_pots_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(
        request, 'account/profile.html', 
        {'profile': profile,
         'page_obj': page_obj}
    )

@login_required
def move_money_view(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == "POST":
        add_money_form = AddMoney(data=request.POST, instance=profile)
        if add_money_form.is_valid():
            add_money_form.save()
            messages.add_message(request, messages.SUCCESS, 'Transfer completed')
            return redirect('profile')  
    else:
        add_money_form = AddMoney(instance=profile)

    return render(
        request, 'account/move_money.html',
        {
            'profile': profile,
            'add_money_form': add_money_form,
        }
    )
