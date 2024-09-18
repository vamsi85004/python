class CapitalDetector:
    def detect_capital_use(self, word):
        """
        :type word: str
        :rtype: bool
        """
        # Check if all characters are uppercase
        if word.isupper():
            return True
        # Check if all characters are lowercase
        elif word.islower():
            return True
        # Check if only the first character is uppercase and the rest are lowercase
        elif word[0].isupper() and word[1:].islower():
            return True
        return False

# Example usage
detector = CapitalDetector()
word = input("Enter a word to check its capitalization: ")
if detector.detect_capital_use(word):
    print(f"The capitalization of '{word}' is correct.")
else:
    print(f"The capitalization of '{word}' is incorrect.")
