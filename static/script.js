document.addEventListener("DOMContentLoaded", function() {
    // Get all anchor tags on the page
    const links = document.querySelectorAll("a");
    // Add click event listener to each link
    links.forEach(link => {
        link.addEventListener("click", function(event) {
            // Prevent the default action
            event.preventDefault();
            // Open the link in a new tab
            window.open(event.target.href, '_blank');
            // Refresh the current page
            location.reload();
        });
    });
});
