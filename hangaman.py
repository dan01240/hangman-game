from random import randint

# Words that can be used in a Hangman game, categorized by difficulty
words = {
    'easy': [
        "apple", "banana", "island", "robot", "cat", "sun", "tree", "dog", "book", "car", "fish", "star", "moon", "water", "pen", "cup", "hat", "bag", "shoe", "ball", "house", "boat", "milk", "hand", "leg"
    ],
    'medium': [
        "giraffe", "jacket", "kangaroo", "ocean", "mountain", "pencil", "elephant", "castle", "pirate", "forest", "garden", "planet", "train", "desert", "diamond", "guitar", "whale", "bridge", "candle", "statue", "village", "rocket", "beaver", "canyon", "harbor"
    ],
    'difficult': [
        "dragon", "volcano", "microscope", "astronaut", "laboratory", "university", "dictionary", "constellation", "philosopher", "galaxy", "hieroglyph", "algorithm", "symphony", "metropolis", "archaeology", "revolution", "periscope", "quarantine", "telescope", "bacterium", "conglomerate", "hemisphere", "photosynthesis", "subterranean", "monolith"
    ]
}

def select_difficulty():
    while True:
        difficulty = input("Please select a difficulty level (easy, medium, difficult): ").lower()
        if difficulty in words:
            return difficulty
        else:
            print("Invalid difficulty level selected. Please choose from 'easy', 'medium', or 'difficult'.")

def hangman_game(word_to_guess):
    guess_count = 0
    guess_limit = 6
    guess_letter = []
    display = ['_'] * len(word_to_guess)

    print(f"\nWelcome to Hangman Game Project 5\n")
    print(f"Word to guess: {' '.join(display)}\n")

    # Game loop
    while guess_count < guess_limit:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1:
            print("Please enter a single letter.")
        elif guess in guess_letter:
            print("You already guessed this letter.")
        elif guess not in word_to_guess:
            print(f"Incorrect guess! You have {guess_limit - guess_count - 1} guesses left.")
            guess_letter.append(guess)
            guess_count += 1
        else:
            print(f"Good job! '{guess}' is in the word.")
            guess_letter.append(guess)
            word_as_list = list(word_to_guess)
            indices = [i for i, letter in enumerate(word_as_list) if letter == guess]
            for index in indices:
                display[index] = guess

        print(f"Current word: {' '.join(display)}")
        
        if '_' not in display:
            print(f"Congratulations! You guessed the word: {word_to_guess}")
            return

    print(f"Game over! The word was: {word_to_guess}")

# Main execution
difficulty = select_difficulty()
filtered_words = words[difficulty]
word_to_guess = filtered_words[randint(0, len(filtered_words) - 1)]
hangman_game(word_to_guess)
