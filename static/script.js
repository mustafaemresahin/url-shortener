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

    const visitButton = document.querySelectorAll('.visitButton');
    
    // Add a click event listener to each button
    visitButton.forEach(function(button) {
      button.addEventListener('click', function(event) {
        // Prevent the default action
        event.preventDefault();
        // Open the link in a new tab
        window.open(event.target.href, '_blank');
        // Refresh the page
        location.reload();
      });
    });
    // Copy to Clipboard
    document.querySelectorAll('.copyButton').forEach(function(button) {
        button.addEventListener('click', function(e) {
            const url = e.target.getAttribute('data-url');
            navigator.clipboard.writeText("http://127.0.0.1:5000/"+url).then(function() {
                e.target.textContent = 'Copied!';
                setTimeout(function() {
                    e.target.textContent = 'Copy';
                }, 2000);
            });
        });
    });
});