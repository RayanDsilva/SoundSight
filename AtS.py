import os
from nltk.metrics import edit_distance

def find_closest_match(user_input, sign_languages):
    # Calculate the edit distance (Levenshtein distance) between user input and each sign language
    distances = [(language, edit_distance(user_input, language)) for language in sign_languages]
    # Sort the distances by the edit distance in ascending order
    sorted_distances = sorted(distances, key=lambda x: x[1])
    # Return the sign language with the smallest edit distance
    return sorted_distances[0][0]

def display_avatar(sign_language):
    # Path to the folder containing avatar videos
    folder_path = "C:\\Users\\91735\\OneDrive\\Desktop\\audio to sign\\firsttry\\assets"

    # Dictionary mapping sign languages to file names
    sign_language_files = {
        "After": "After.mp4",
        # Add more sign languages and their corresponding file names as needed
    }

    # Check if the sign language provided by the user exists in the dictionary
    if sign_language in sign_language_files:
        file_name = sign_language_files[sign_language]
        file_path = os.path.join(folder_path, file_name)
        
        # Check if the file exists
        if os.path.exists(file_path):
            print(f"Displaying avatar for {sign_language}...")
            print(f"Path to file: {file_path}")
        else:
            print(f"Avatar video for {sign_language} not found.")
    else:
        # Find the closest match to the user input using similarity matching
        closest_match = find_closest_match(sign_language, sign_language_files.keys())
        file_name = sign_language_files[closest_match]
        file_path = os.path.join(folder_path, file_name)
        print(f"Displaying avatar for closest match: {closest_match}...")
        print(f"Path to file: {file_path}")

# Example usage:
user_input = input("Enter a sentence in sign language: ")
display_avatar(user_input.lower())  # Convert user input to lowercase for case-insensitive matchingimpo