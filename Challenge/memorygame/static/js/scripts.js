document.addEventListener('DOMContentLoaded', () => {
    const cards = document.querySelectorAll('.card');
    let flippedCards = [];

    cards.forEach(card => {
        card.addEventListener('click', () => {
            if (flippedCards.length < 2 && !card.classList.contains('face-up')) {
                card.classList.add('face-up');
                flippedCards.push(card);

                if (flippedCards.length === 2) {
                    // Check if the two flipped cards match
                    if (flippedCards[0].dataset.name === flippedCards[1].dataset.name) {
                        flippedCards.forEach(flippedCard => {
                            flippedCard.classList.add('match');
                        });
                        setTimeout(() => {
                            flippedCards.forEach(flippedCard => {
                                flippedCard.style.visibility = 'hidden';
                            });
                            flippedCards = [];
                        }, 1000); // Delay to show the matched cards before hiding
                    } else {
                        flippedCards.forEach(flippedCard => {
                            flippedCard.classList.add('no-match');
                        });
                        setTimeout(() => {
                            flippedCards.forEach(flippedCard => {
                                flippedCard.classList.remove('face-up');
                                flippedCard.classList.remove('no-match');
                            });
                            flippedCards = [];
                        }, 1000); // Delay to flip back the unmatched cards
                    }
                }
            }
        });
    });
});