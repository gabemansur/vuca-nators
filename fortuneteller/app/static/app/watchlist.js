document.addEventListener('DOMContentLoaded', function() {

    // Event listener for updatewatchlist button click
    document.querySelectorAll('.updatewatchlist').forEach(item => {
        item.addEventListener('click', event => updateWatchlist(event));
    });

    // Event listener for watchlist item button click
    document.querySelectorAll('.watchlistitem').forEach(item => {
        item.addEventListener('click', event => updateWatchlistAndRemoveFromTable(event));
    });
});

function updateWatchlist(event) {

    // Fetch updatewatchlist with target id
    fetch('/updatewatchlist', {
        method: 'POST',
        body: JSON.stringify({
            symbol: event.target.id,
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data["updated_watchlist"])

        // Check if watchlist has item added
        // True, add red button and edit text to remove
        // False, add green button and edit text to add
        if (data["added"]) {
            event.target.classList.add("btn-danger")
            event.target.classList.remove("btn-success")
            event.target.textContent = "Remove"
        } else {
            event.target.classList.add("btn-success")
            event.target.classList.remove("btn-danger")
            event.target.textContent = "Add"
        }
    })
}

function updateWatchlistAndRemoveFromTable(event) {
    fetch('/updatewatchlist', {
        method: 'POST',
        body: JSON.stringify({
            symbol: event.target.id,
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data["updated_watchlist"])

        // Check if watchlist has item added
        // True, add red button and edit text to remove
        // False, remove item from watchlist by target id
        if (data["added"]) {
            event.target.classList.add("btn-danger")
            event.target.classList.remove("btn-success")
            event.target.textContent = "Remove"
        } else {
            document.querySelector("#" + event.target.id).remove()
        }
    })
}