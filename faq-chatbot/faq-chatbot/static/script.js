document.addEventListener('DOMContentLoaded', function() {
    // Focus the question input field when page loads
    const questionInput = document.querySelector('input[name="question"]');
    if (questionInput) questionInput.focus();

    // Add animation when submitting forms
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function() {
            const submitButton = this.querySelector('button[type="submit"]');
            if (submitButton) {
                submitButton.disabled = true;
                submitButton.textContent = 'Processing...';
            }
        });
    });
});
