function toggleCard(card) {
    const isExpanded = card.classList.contains('expanded');
    const expandedCard = document.querySelector('.pokemon-card.expanded');

    if (expandedCard && expandedCard !== card) {
        expandedCard.classList.remove('expanded');
    }

    if (!isExpanded) {
        card.classList.add('expanded');
    } else {
        card.classList.remove('expanded');
    }
}

document.addEventListener('click', function(event) {
    const expandedCard = document.querySelector('.pokemon-card.expanded');
    if (expandedCard && !expandedCard.contains(event.target)) {
        expandedCard.classList.remove('expanded');
    }
});