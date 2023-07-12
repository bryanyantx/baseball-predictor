document.addEventListener('DOMContentLoaded', function() {
    const passwordContent = document.getElementById('password');
    const showPassword = document.getElementById('show-password');

    showPassword.addEventListener('click', function() {
        if(showPassword.checked) {
            passwordContent.type = 'text';
        }
        else {
            passwordContent.type = 'password';
        }
    });
});