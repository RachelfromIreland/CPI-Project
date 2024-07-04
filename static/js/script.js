document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('contactForm');
    const thankYouMessage = document.getElementById('thankYouMessage');
    const returnHomeButton = document.getElementById('returnHomeButton');
    const contactHeader = document.getElementById('contact-header');

    if (form && thankYouMessage && returnHomeButton) {
        // Add event listener for form submission
        form.addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent default form submission

            // Send the form data via Fetch API
            fetch('https://formspree.io/f/xjkbveaz', {
                method: 'POST',
                body: new FormData(form), // Serialize form data
                headers: {
                    'Accept': 'application/json'
                }
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                // Hide the form and display the thank you message
                form.style.display = 'none';
                contactHeader.style.display = 'none';
                thankYouMessage.style.display = 'block';
            })
            .catch(error => {
                console.error('Error:', error);
                alert('An error occurred while sending your message. Please try again later.');
            });
        });

        // Add event listener for "Return to Home" button
        returnHomeButton.addEventListener('click', function() {
            window.location.href = '/'; // Redirect to home page
        });
    } else {
        console.error('Form, thank you message, or return home button is null.');
    }
});