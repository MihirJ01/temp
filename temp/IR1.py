#1.Write a program to demonstrate bitwise operation
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

corpus=[
    'this is the first document.',
    'this document is second document.',
    'and this is third one.',
    'is this first document?'
    ]

vec = CountVectorizer()
x = vec.fit_transform(corpus)
print(x.toarray())

df = pd.DataFrame(x.toarray(),columns=vec.get_feature_names_out())
print(df)

andData = df[(df['this']==1) & (df['first']==1)]
print("Indices in which this and first are present at",andData.index.tolist())


#2.Write a python program to perform N-Gram analysis specifically
#based on unigram, bigram and trigram. Using NLTK.

import nltk
from nltk.util import ngrams
from nltk import word_tokenize

text = "This is a sample text for unigram, bigram, and trigram extraction using NLTK,"

lt = text.lower()

tokens = word_tokenize(lt)
print("OG text")
print(tokens)

unigrams = list(ngrams(tokens,1))
print("unigram")
print(unigrams)

bigram = list(ngrams(tokens,2))
print("Bigram")
print(bigram)

trigram = list(ngrams(tokens,3))
print("Trigram")
print(trigram)


#3.Write a python program to evaluate the performance of an IR model using
#standard evaluation metrics.

from sklearn.metrics import precision_score,recall_score,f1_score

#Sample data (ground truth and predicated relevance)

ground_truth = [1,0,1,1,0,0,0,1,1,1,0,0,1,0,1]
predicated_relevance = [1,1,0,0,0,0,0,1,1,0,1,0,1,1,1]
print('Ground Truth = ',ground_truth,'\nPredicated Relevance = ',predicated_relevance)

#Calculate evalution metrics
precision = precision_score(ground_truth,predicated_relevance)
recall = recall_score(ground_truth,predicated_relevance)
f1 = f1_score(ground_truth,predicated_relevance)

#Print the results
print('Precision : ',precision,'\nRecall : ',recall,'\nF1 Score : ',f1)



#4. Write a program to compute similarity between two text documents.


import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def cosine_similarity(x,y):
    #Ensure length of x and y are the same
    if len(x) != len(y):
        return None
    #Compute the dot product between x and y
    dot_product = np.dot(x, y)
    #Compute the 1, 2 norms (magnitudes) of x and y
    magnitude_x = np.sqrt(np.sum(x ** 2))
    magnitude_y = np.sqrt(np.sum(y ** 2))
    #Compute the cosine similarity
    cosine_similarity = dot_product / (magnitude_x * magnitude_y)
    return cosine_similarity
corpus = ['Data Science is one of the most important fields of science','This is one of the best data science courses',
          'Data Scientists analyse data']
#Create a matrix to represent the corpus
X = CountVectorizer().fit_transform(corpus).toarray()
print(X)
cos_sim_1_2 = cosine_similarity(X[0,:],X[1,:])
cos_sim_1_3 = cosine_similarity(X[0,:],X[2,:])
cos_sim_2_3 = cosine_similarity(X[1,:],X[2,:])

print('Cosine Similarity between: ')
print('Document 1 and Document 2: ', cos_sim_1_2)
print('Document 1 and Document 3: ', cos_sim_1_3)
print('Document 2 and Document 3: ', cos_sim_2_3)


#5.Write a program in python to implement text clustering using TFIDF
#and K Means

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans

documents = [
    "I love the taste of Italian food, especially pizza and pasta.",
    "Artificial Intelligence and Machine Learning are revolutionizing technology.",
    "Football is a popular sport around the world, especially in Europe.",
    "I enjoy coding and building software solutions with Python.",
    "The economy is affected by inflation and the stock market.",
    "The Python programming language is widely used for data science and AI."
]

vectorizer = TfidfVectorizer(stop_words="english")

x = vectorizer.fit_transform(documents)

num_cluster = 3

kmeans = KMeans(n_clusters = num_cluster,random_state=42)
kmeans.fit(x)

labels = kmeans.labels_

print(f"Document 1: {documents[0]}")
print(f"Cluster: {labels[0]}\n")

print(f"Document 2: {documents[1]}")
print(f"Cluster: {labels[1]}\n")

print(f"Document 3: {documents[2]}")
print(f"Cluster: {labels[2]}\n")

print(f"Document 4: {documents[3]}")
print(f"Cluster: {labels[3]}\n")

print(f"Document 5: {documents[4]}")
print(f"Cluster: {labels[4]}\n")

print(f"Document 6: {documents[5]}")
print(f"Cluster: {labels[5]}\n")

silhouette_avg = silhouette_score(x,labels)
print(silhouette_avg)


#6.**Write program for pre-processing of Text document: stop word removal

import nltk
##nltk.download('stopwords')
##nltk.download('punkt')
##nltk.download('punkt_tab')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
example_sentence = 'Quantum mechanics describes the behavior of particles at the atomic level.'
stop_words = set(stopwords.words('english'))
# Tokenize the sentence
word_tokens = word_tokenize(example_sentence)
# Filter out stop words
filtered_sentence = [w for w in word_tokens if w.lower() not in stop_words]
stopwords_found = [w for w in word_tokens if w.lower() in stop_words]
# Print results
print(f'Sentence is: {word_tokens}')
print(f'Filtered Sentence is: {filtered_sentence}')
print('Stop words in example sentence were : ',stopwords_found)
print('Count of stop words in the example sentence: ', len(stopwords_found))



#9.Implement Dynamic programming algorithm for computing the edit distance between
#strings s1 and s2.

def Levenshtein(s1, s2):
    if s1 == "":
        return len(s2)
    elif s2 == "":
        return len(s1)
    elif s1[-1] == s2[-1]:
        cost = 0
    else:
        cost = 1

    res = min(
        [
            Levenshtein(s1[:-1], s2) + 1,  # deletion
            Levenshtein(s1, s2[:-1]) + 1,  # insertion
            Levenshtein(s1[:-1], s2[:-1]) + cost,  # substitution
        ]
    )
    return res

s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")
print(f"The Levenshtein distance between '{s1}' and '{s2}' is: {Levenshtein(s1, s2)}")



#10.Write a program to implement simple crawler.

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

# Base URL (Change this to the website you want to crawl)
base_url = "https://example.com/"

# Set to store visited URLs
visited_urls = set()

# List to store URLs to visit next
urls_to_visit = [base_url]

# Set a crawl limit to avoid infinite loops
MAX_PAGES = 10  # Adjust as needed

# Function to crawl a page and extract links
def crawl_page(url):
    try:
        response = requests.get(url, timeout=5)  # Set a timeout to prevent hanging requests
        response.raise_for_status()  # Raise an exception for HTTP errors

        soup = BeautifulSoup(response.content, "html.parser")

        # Extract links and enqueue new URLs
        links = []
        for link in soup.find_all("a", href=True):
            next_url = urljoin(url, link["href"])  # Convert relative URLs to absolute

            # Ensure we only crawl pages within the same domain
            if urlparse(next_url).netloc == urlparse(base_url).netloc:
                links.append(next_url)

        return links

    except requests.exceptions.RequestException as e:
        print(f"Error crawling {url}: {e}")
        return []

# Start crawling
pages_crawled = 0

while urls_to_visit and pages_crawled < MAX_PAGES:
    current_url = urls_to_visit.pop(0)  # Dequeue the first URL

    if current_url in visited_urls:
        continue

    print(f"Crawling: {current_url}")

    new_links = crawl_page(current_url)
    visited_urls.add(current_url)
    urls_to_visit.extend(new_links)

    pages_crawled += 1

print("Crawling finished.")


#11.Demonstrate a simple web scraping process using Python within the environment.
import requests
from bs4 import BeautifulSoup

# Specify the URL you want to scrape
url = "https://google.com"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, "html.parser")

    # Find and print the text content (modify as needed based on the HTML structure)
    text_content = soup.get_text()
    print(text_content)
else:
    print(f"Error: Unable to fetch content. Status code: {response.status_code}")


#12.Write a program to parse XML text, generate Web graph and compute topic specific page rank

import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph (replace this with your own graph)
G = nx.DiGraph()
G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 1)])

# Calculate PageRank
pagerank_scores = nx.pagerank(G)

# Calculate HITS (Hub and Authority) scores
hits_scores = nx.hits(G)

# Print the results
print("PageRank Scores:", pagerank_scores)
print("Hub Scores:", hits_scores[0])
print("Authority Scores:", hits_scores[1])

# Visualize the graph
pos = nx.spring_layout(G)  # positions for all nodes
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=15, font_weight='bold')
plt.title("Directed Graph Visualization")
plt.show()


#13.Calculate Page rank along with hubs and authorities.

import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph (replace this with your own graph)
G = nx.DiGraph()
G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 1)])

# Calculate PageRank
pagerank_scores = nx.pagerank(G)

# Calculate HITS (Hub and Authority) scores
hits_scores = nx.hits(G)

# Print the results
print("PageRank Scores:", pagerank_scores)
print("Hub Scores:", hits_scores[0])
print("Authority Scores:", hits_scores[1])

# Visualize the graph
pos = nx.spring_layout(G)  # positions for all nodes
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=15, font_weight='bold')
plt.title("Directed Graph Visualization")
plt.show()


#14.**Write a program for mining Twitter to identify tweets for a specific period and identify trends and named entities
import tweepy

# Variables that contain the user credentials to access Twitter API
consumer_key = "TL7iYrpIU1pVgLjIlMNEk8Rzy"
consumer_secret = "1OyZ1LjlYG9iWYZmptKuK6o4tcC3T0Ldnc8QAyER0YygS0yTge"
access_token = "1387750007416098824-Mmz7t36RHIw4IzZaaoKZBlNq9h1G8k"
access_token_secret = "yatO8A6FNuxTuc10IvaBXSWrJMal6KjKSIQCTcW1XjniZ"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAN4jygEAAAAAGX5K7hvi0Ed%2FDLww9Fa%2BRbvwHy4%3DNF9XldSa2vhYWSpSn03tzRvPAiVPy6o47znyYbbrPFYwwdwZBq"  # Replace with your actual Bearer Token for OAuth 2.0

# This is a basic listener that just prints received tweets to stdout
class StdOutListener(tweepy.StreamingClient):
    def on_tweet(self, tweet):  # Tweepy v4.x uses `on_tweet` method
            print(f"Tweet ID: {tweet.id}")
            print(f"Tweet text: {tweet.text}")
            print(f"User: {tweet.author.username}")

    def on_error(self, status_code):  # Fix error handling
        print(f"Error encountered: {status_code}")
        if status_code == 420:  # Rate limit error
            return False  # Disconnect the stream
        return True  # Keep stream running for other errors

if __name__ == '__main__':
    try:
        # This handles Twitter authentication and the connection to Twitter Streaming API
        stream = StdOutListener(bearer_token)

        # Add rules to filter tweets containing 'python', 'javascript', or 'ruby'
        stream.add_rules(tweepy.StreamRule("python OR javascript OR ruby"))

        # Start the stream to capture tweets
        print("Streaming started. Listening for tweets...")
        stream.filter(tweet_fields=["text"])  # Specify tweet fields for better handling
    except Exception as e:
        print(f"An error occurred: {e}")




   
