// Wait until the DOM is fully loaded
document.addEventListener("DOMContentLoaded", function() {
    // Fetch all anchor tags on the page
    const links = document.querySelectorAll("a");
    
    // Loop through each anchor tag
    links.forEach(link => {
        // Attach a click event listener to the anchor tag
        link.addEventListener("click", function(event) {
            // Prevent the default action of navigating to the link
            event.preventDefault();
            // Open the clicked link in a new browser tab
            window.open(event.target.href, '_blank');
            // Reload the current page
            location.reload();
        });
    });

    // Add a 'Copy to Clipboard' feature to buttons with the 'copyButton' class
    document.querySelectorAll('.copyButton').forEach(function(button) {
        // Attach a click event listener to the button
        button.addEventListener('click', function(e) {
            // Fetch the URL from the button's 'data-url' attribute
            const url = e.target.getAttribute('data-url');
            // Use the Clipboard API to copy the URL
            navigator.clipboard.writeText("http://127.0.0.1:5000/"+url).then(function() {
                // Change the button text to indicate success
                e.target.textContent = 'Copied!';
                // Revert the button text back to 'Copy' after 2 seconds
                setTimeout(function() {
                    e.target.textContent = 'Copy';
                }, 2000);
            });
        });
    });
});

// Function to trigger native sharing using Web Share API
function nativeShare(url) {
    // Check if the Web Share API is supported by the browser
    if (navigator.share) {
        // Use the Web Share API
        navigator.share({
            title: 'Share this link',
            url: url
        }).then(() => {
            console.log('Thanks for sharing!');
        })
        .catch(console.error);
    } else {
        // Alert the user if Web Share API is not supported
        alert('Web Share API not supported.');
    }
}

// Function to delete a URL by sending a POST request to the server
function deleteUrl(event, shortUrl) {
    // Prevent the default action of form submission
    event.preventDefault();

    // Send a POST request to delete the URL
    fetch('/delete_url', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ url: shortUrl })
    })
    .then(response => response.json())  // Parse the JSON response
    .then(data => {
        // Reload the page if the URL is successfully deleted
        if (data.success) {
            location.reload();
        } else {
            // Show an alert if the deletion fails
            alert('Failed to delete URL');
        }
    })
    .catch(error => {
        // Log any errors to the console
        console.error('Error:', error);
    });
}
