function setTransferMessage() {
    var balance = parseFloat(document.getElementById('pot-balance').value);
    var transferMessage = document.getElementById('transfer-message');
    if (balance > 0) {
        transferMessage.textContent = 'The funds will be transferred to your bank account.';
    } else {
        transferMessage.textContent = 'The saving pot is empty and will be closed.';
    }
}

// Call the function to set the message when the page loads
setTransferMessage();

// Handle the confirmation logic
document.getElementById('close-pot-btn').addEventListener('click', function() {
    var balance = parseFloat(document.getElementById('pot-balance').value);
    var message = balance > 0 
        ? 'The funds will be transferred to your bank account.' 
        : 'The saving pot is empty and will be closed.';
    
    if (confirm('Are you sure you want to close this pot? ' + message)) {
        document.getElementById('close-pot-form').submit();
    }
});