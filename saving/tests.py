from django.test import TestCase
from .forms import (
    CustomSignupForm,
    AddMoney,
    OpenNewPot,
    AddMoneySavingPot,
    ChangeNameSavingPot
)


class TestCustomSignupForm(TestCase):
    """Tests for the CustomSignupForm"""

    def test_form_is_valid(self):
        """Test that the form is valid with all fields"""
        form_data = {
            'nominated_bank_account': '12345678',
            'main_balance': '100.00'
        }
        form = CustomSignupForm(form_data)
        self.assertTrue(form.is_valid(), msg="Form is not valid")

    def test_nominated_bank_account_is_required(self):
        """Test that the nominated_bank_account field is required"""
        form_data = {'main_balance': '100.00'}
        form = CustomSignupForm(form_data)
        self.assertFalse(
            form.is_valid(),
            msg="Form is valid without nominated_bank_account"
        )
        self.assertIn('nominated_bank_account', form.errors)

    def test_main_balance_is_required(self):
        """Test that the main_balance field is required"""
        form_data = {'nominated_bank_account': '12345678'}
        form = CustomSignupForm(form_data)
        self.assertFalse(
            form.is_valid(),
            msg="Form is valid without main_balance"
        )
        self.assertIn('main_balance', form.errors)


class TestAddMoneyForm(TestCase):
    """Tests for the AddMoney form"""

    def test_form_is_valid(self):
        """Test that the form is valid with the main_balance field"""
        form_data = {'main_balance': '50.00'}
        form = AddMoney(form_data)
        self.assertTrue(form.is_valid(), msg="Form is not valid")

    def test_main_balance_is_required(self):
        """Test that the main_balance field is required"""
        form = AddMoney({})
        self.assertFalse(
            form.is_valid(),
            msg="Form is valid without main_balance"
        )
        self.assertIn('main_balance', form.errors)


class TestOpenNewPotForm(TestCase):
    """Tests for the OpenNewPot form"""

    def test_form_is_valid(self):
        """Test that the form is valid with the name field"""
        form_data = {'name': 'New Pot'}
        form = OpenNewPot(form_data)
        self.assertTrue(form.is_valid(), msg="Form is not valid")

    def test_name_is_required(self):
        """Test that the name field is required"""
        form = OpenNewPot({})
        self.assertFalse(
            form.is_valid(),
            msg="Form is valid without name"
        )
        self.assertIn('name', form.errors)


class TestAddMoneySavingPotForm(TestCase):
    """Tests for the AddMoneySavingPot form"""

    def test_form_is_valid(self):
        """Test that the form is valid with the balance field"""
        form_data = {'balance': '20.00'}
        form = AddMoneySavingPot(form_data)
        self.assertTrue(form.is_valid(), msg="Form is not valid")

    def test_balance_is_required(self):
        """Test that the balance field is required"""
        form = AddMoneySavingPot({})
        self.assertFalse(
            form.is_valid(),
            msg="Form is valid without balance"
        )
        self.assertIn('balance', form.errors)


class TestChangeNameSavingPotForm(TestCase):
    """Tests for the ChangeNameSavingPot form"""

    def test_form_is_valid(self):
        """Test that the form is valid with the name field"""
        form_data = {'name': 'Updated Pot Name'}
        form = ChangeNameSavingPot(form_data)
        self.assertTrue(form.is_valid(), msg="Form is not valid")

    def test_name_is_required(self):
        """Test that the name field is required"""
        form = ChangeNameSavingPot({})
        self.assertFalse(
            form.is_valid(),
            msg="Form is valid without name"
        )
        self.assertIn('name', form.errors)
