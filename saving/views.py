from django.urls import reverse
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Profile
from .forms import AddMoney, OpenNewPot, AddMoneySavingPot, ChangeNameSavingPot


def home_view(request):
    """
    Display the index.html.

    Checks if the user is logged in. Depending on the login status,
    the user is redirected to the profile view or the index.html.
    """
    if request.user.is_authenticated:
        return redirect('profile')
    return render(request, 'account/index.html')


@login_required
def profile_view(request):
    """
    Profile view.

    Displays the current main balance and
    all saving pots the user has.
    """
    profile = Profile.objects.get(user=request.user)
    saving_pots_list = profile.saving_pots.all()

    paginator = Paginator(saving_pots_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(
        request, 'account/profile.html',
        {'profile': profile, 'page_obj': page_obj}
    )


@login_required
def move_money_view(request):
    """
    Move money view.

    Allows the user to add funds
    to the main balance.
    """
    profile = Profile.objects.get(user=request.user)

    if request.method == "POST":
        add_money_form = AddMoney(data=request.POST, instance=profile)
        if add_money_form.is_valid():
            add_money_form.save()
            profile_url = reverse('profile')
            messages.success(
                request,
                f'Transfer completed. <a href="{profile_url}" class="alert-link">Go to Profile</a>',
                extra_tags='safe'
            )
    else:
        add_money_form = AddMoney(instance=profile)

    return render(
        request, 'account/move_money.html',
        {'profile': profile, 'add_money_form': add_money_form}
    )


@login_required
def create_saving_pot_view(request):
    """
    Create a saving pot view.

    Allows the user to create new pots
    and add them to the user profile.
    """
    profile = Profile.objects.get(user=request.user)

    if request.method == "POST":
        pot_form = OpenNewPot(data=request.POST)
        if pot_form.is_valid():
            saving_pot = pot_form.save(commit=False)
            saving_pot.profile = profile
            saving_pot.user = request.user
            saving_pot.save()
            profile_url = reverse('profile')
            messages.success(
                request,
                f'New Pot created. <a href="{profile_url}" class="alert-link">Go to Profile</a>',
                extra_tags='safe'
            )
    else:
        pot_form = OpenNewPot()

    return render(request, 'account/open_pot.html', {'pot_form': pot_form})


@login_required
def saving_pot_details_view(request, pot_id):
    """
    Saving pot details view.

    Displays the current balance of the pot
    allowing funds to be added from the main balance.
    Provides links to close the saving pot and change its name.
    """
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
                messages.success(
                    request, 'Transfer completed', extra_tags='safe'
                )
    else:
        add_funds_form = AddMoneySavingPot()

    return render(
        request, 'account/saving_pot_details.html',
        {'saving_pot': saving_pot, 'add_funds_form': add_funds_form}
    )


@login_required
def close_pot_confirmation_view(request, pot_id):
    """
    Close pot view.

    Allows the user to close the saving pot.
    """
    profile = Profile.objects.get(user=request.user)
    saving_pot = profile.saving_pots.get(id=pot_id)

    if request.method == 'POST':
        saving_pot.delete()
        return redirect('profile')

    return render(
        request, 'account/close_pot.html',
        {'pot_id': pot_id, 'balance': saving_pot.balance}
    )


@login_required
def change_name_pot_details_view(request, pot_id):
    """
    Change pot name view.

    Allows the user to change the name of the pot.
    """
    profile = Profile.objects.get(user=request.user)
    saving_pot = profile.saving_pots.get(id=pot_id)

    if request.method == "POST":
        change_name_form = ChangeNameSavingPot(data=request.POST, instance=saving_pot)
        if change_name_form.is_valid():
            change_name_form.save()
            profile_url = reverse('profile')
            messages.success(
                request,
                f'Name Changed. <a href="{profile_url}" class="alert-link">Go to Profile</a>',
                extra_tags='safe'
            )
    else:
        change_name_form = ChangeNameSavingPot(instance=saving_pot)

    return render(
        request, 'account/change_pot_name.html',
        {'saving_pot': saving_pot, 'change_name_form': change_name_form}
    )
