document.addEventListener("DOMContentLoaded", function () {
    // Get DOM elements
    const showPasswordBtn = document.querySelector('.fa-eye');
    const passwordInp = document.querySelector('.password-input');

showPasswordBtn.addEventListener('click', () => {
    // Toggle password visibility
    if (passwordInp.type === 'password') {
        passwordInp.type = 'text'; // Show password
        showPasswordBtn.classList.remove('fa-eye');
        showPasswordBtn.classList.add('fa-eye-slash');
    } else {
        passwordInp.type = 'password'; // Hide password
        showPasswordBtn.classList.remove('fa-eye-slash');
        showPasswordBtn.classList.add('fa-eye');
    }

});
// Update password checklist on keyup
passwordInp.addEventListener('keyup', updatePasswordChecklist);
});


document.getElementById("loginButton").addEventListener("click", function (event) {
    event.preventDefault();
    // You can add validation or other logic here if needed.
    // Then, you can submit the form:
    document.querySelector("form").submit();
});