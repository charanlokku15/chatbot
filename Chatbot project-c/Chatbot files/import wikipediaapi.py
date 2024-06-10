import wikipediaapi
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download NLTK resources
nltk.download('punkt')
nltk.download('wordnet')

# Fetch Leonardo DiCaprio Wikipedia page
wiki = wikipediaapi.Wikipedia('en')
page = wiki.page("Leonardo DiCaprio")
text = page.text

# Preprocess text
sentences = nltk.sent_tokenize(text)
lemmatizer = nltk.stem.WordNetLemmatizer()

def preprocess_text(text):
    tokens = nltk.word_tokenize(text.lower())
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return ' '.join(tokens)

sentences = [preprocess_text(sentence) for sentence in sentences]

# Build TF-IDF vectorizer
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(sentences)

# Define a function to get response
def get_response(input_text):
    input_text = preprocess_text(input_text)
    input_vector = vectorizer.transform([input_text])

    similarities = cosine_similarity(input_vector, X)
    max_similarity_index = similarities.argmax()
    response = sentences[max_similarity_index]
    
    return response

# Chatbot functionalities
def chatbot(input_text):
    if 'exit' in input_text.lower():
        return "Goodbye! Have a great day."
    else:
        return get_response(input_text)

# Running the chatbot
print("Chatbot: Hello, I'm a chatbot about Leonardo DiCaprio. You can exit the chatbot at any time by entering 'exit'. What is your name?")
user_input = input("User: ")

if 'name is' in user_input.lower():
    # Getting the name of the user if the input contains 'name is'
    user_name = user_input.split('name is')[-1].strip()
else:
    # Using the user input directly as the name
    user_name = user_input

print(f"Chatbot: Hello {user_name}, What can I help you with today?")

while True:
    user_input = input("User: ")
    response = chatbot(user_input)
    print("Chatbot:", response)
