function showButtons(card) {
    var buttons = card.querySelector('.buttons');
    buttons.style.bottom = '0';
}

function hideButtons(card) {
    var buttons = card.querySelector('.buttons');
    buttons.style.bottom = '-60px';
}

document.addEventListener('DOMContentLoaded', function() {
    var productCards = document.querySelectorAll('.product-card');

    productCards.forEach(function(card) {
        card.addEventListener('mouseover', function() {
            showButtons(this);
        });

        card.addEventListener('mouseleave', function() {
            hideButtons(this);
        });
    });
});

