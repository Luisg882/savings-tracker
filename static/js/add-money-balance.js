document.addEventListener('DOMContentLoaded', function () {
    var amountInput = document.getElementById('amount-to-add');
    var balanceInput = document.getElementById('id_main_balance'); // Adjusted to match your input field ID

    if (amountInput && balanceInput) {
        amountInput.addEventListener('input', function () {
            var currentBalance = parseFloat(balanceInput.value) || 0;
            var amountToAdd = parseFloat(amountInput.value) || 0;
            
            var newBalance = currentBalance + amountToAdd;
            
            balanceInput.value = newBalance.toFixed(2); 
        });
    }
});