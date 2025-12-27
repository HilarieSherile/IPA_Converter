"""
ipa_transcriber.py 
Author: Hilarie Sielenou

"""
def get_ipa(word):
    """
    Convert a word to its IPA transcription. 
    For MVP, i will use a placeholder dictionary. 
    """

    ipa_dict = {
        "hello": "həˈloʊ",
        "world": "wɝːld",
        "language": "ˈlæŋɡwɪdʒ",
        "python": "ˈpaɪθɑn"
    }
    return ipa_dict.get(word.lower(), "IPA not found")

def main(): 
    print("Welcome to the IPA Converter!")
    
    while True: 
        user_input = input ("Enter a word (o type 'exit' to quit): ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break 

        ipa = get_ipa(user_input)
        print(f"IPA transcription: {ipa}\n")


if __name__ == "__main__": 
    main()