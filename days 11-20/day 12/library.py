def choose_difficulty():
    difficulty = input(
        'Choose dificulty: type \'easy\' or \'hard\':\n').lower()
    if difficulty == 'easy':
        return 10
    elif difficulty == 'hard':
        return 5
    else:
        return choose_difficulty()
