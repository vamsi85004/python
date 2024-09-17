def can_construct_ransom_note(message, magazine):
    """
    Check if it's possible to construct the ransom note from the magazine words.

    :param message: str, the ransom note message
    :param magazine: str, the magazine text
    :return: bool, True if the message can be constructed, False otherwise
    """
    from collections import Counter

    # Count the frequency of each word in the message and magazine
    message_words = message.split()
    magazine_words = magazine.split()

    message_count = Counter(message_words)
    magazine_count = Counter(magazine_words)

    # Check if for every word in the message, the magazine has enough occurrences
    for word, count in message_count.items():
        if magazine_count[word] < count:
            return False

    return True

# Example usage:
message = "give me the money"
magazine = "give me the money now or face consequences"

print(can_construct_ransom_note(message, magazine))  # Output: True

message = "give me the gold"
magazine = "give me the money now or face consequences"

print(can_construct_ransom_note(message, magazine))  # Output: False
