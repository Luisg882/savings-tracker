// Getting the main balance and make the logic to change the message dependong of the result
function getTransferMessage() {
    var balance = parseFloat(document.getElementById('pot-balance').value);
    var message = balance > 0 
        ? 'The funds will be transferred to your bank account.' 
        : 'The saving pot is empty and will be closed.';
    return { balance: balance, message: message };
}

// TThis functions sets the transfer message
function setTransferMessage() {
    var { message } = getTransferMessage();
    var transferMessage = document.getElementById('transfer-message');
    transferMessage.textContent = message;
}

// Call the function to set the message when the page loads
setTransferMessage();

// Displays a warning message to confirm if the user really want to close the account 
document.getElementById('close-pot-btn').addEventListener('click', function() {
    var { message } = getTransferMessage();
    
    // Html content that is going to be added
    var closingPotWarning = document.getElementById('closing-pot-warning');
    closingPotWarning.innerHTML = `
        <p>Are you sure you want to close this pot? ${message}</p>
        <button id="confirm-close" class="btn btn-danger">Yes, Close Pot</button>
        <button id="cancel-close" class="btn btn-secondary">Cancel</button>
    `;

    // Add event listener to the confirm button
    document.getElementById('confirm-close').addEventListener('click', function() {
        document.getElementById('close-pot-form').submit();
    });

    // Add event listener to the cancel button
    document.getElementById('cancel-close').addEventListener('click', function() {
        closingPotWarning.innerHTML = ''; // Clear the warning message
    });
});