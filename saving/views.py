from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Profile
from .forms import AddMoney, OpenNewPot, AddMoneySavingPot

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

@login_required
def create_saving_pot_view(request):
    profile = Profile.objects.get(user=request.user)

    if request.method =="POST":
        pot_form = OpenNewPot(data=request.POST)
        if pot_form.is_valid():
            saving_pot = pot_form.save(commit=False)
            saving_pot.profile = profile
            saving_pot.user = request.user
            saving_pot.save()
            messages.success(request, 'Saving por created successfully')
            return redirect('profile')
    else:
        pot_form = OpenNewPot()

    return render(
        request, 'account/open_pot.html',
        {
            'pot_form': pot_form
        }
    )

@login_required
def saving_pot_details_view(request, pot_id):
    profile = Profile.objects.get(user=request.user)
    saving_pot = profile.saving_pots.get(id=pot_id)

    if request.method == "POST":
        add_funds_form = AddMoneySavingPot(data=request.POST)
        if add_funds_form.is_valid():
            amount_to_add = add_funds_form.cleaned_data['balance']
            if profile.main_balance >= amount_to_add:
                profile.main_balance -= amount_to_add
                saving_pot.balance += amount_to_add
                profile.save()
                saving_pot.save()
                messages.add_message(request, messages.SUCCESS, 'Transfer completed')
            else:
                messages.add_message(request, messages.ERROR, 'Insufficient funds in main balance')
            return redirect('profile')
    else:
        add_funds_form = AddMoneySavingPot()

    return render(
        request, 'account/saving_pot_details.html',
        {
            'saving_pot': saving_pot,
            'add_funds_form': add_funds_form
        }
    )


@login_required
@login_required
def close_pot_confirmation_view(request, pot_id):
    profile = Profile.objects.get(user=request.user)
    saving_pot = profile.saving_pots.get(id=pot_id)

    if request.method == 'POST':
        saving_pot.delete()
        messages.add_message(request, messages.SUCCESS, 'Saving pot closed.')

        return redirect('profile')

    return render(
        request, 'account/close_pot.html',
        {
            'pot_id': pot_id,
            'balance': saving_pot.balance
        }
        )