import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
from sklearn.metrics import adjusted_rand_score

def sample_model():
    documents = ["This little kitty came to play when I was eating at a restaurant.",
                 "Merley has the best squooshy kitten belly.",
                 "Google Translate app is incredible.",
                 "If you open 100 tab in google you get a smiley face.",
                 "Best cat photo I've ever taken.",
                 "Climbing ninja cat.",
                 "Impressed with google map feedback.",
                 "Key promoter extension for Google Chrome."]

    vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1,1))
    X = vectorizer.fit_transform(documents)

    true_k = 2
    #model = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1)
    model = DBSCAN(eps=3, min_samples=5)
    model.fit(X)

    print("Top terms per cluster:")
    print(model.labels_)
    # order_centroids = model.cluster_centers_.argsort()[:, ::-1]
    # terms = vectorizer.get_feature_names()
    # for i in range(true_k):
    #     print("Cluster %d:" % i),
    #     for ind in order_centroids[i, :10]:
    #         print(' %s' % terms[ind]),
    #     print

    # print("\n")
    # print("Prediction")

    # Y = vectorizer.transform(["chrome browser to open."])
    # prediction = model.predict(Y)
    # print(prediction)

    # Y = vectorizer.transform(["My cat is hungry."])
    # prediction = model.predict(Y)
    # print(prediction)

def main():
    print('Hello World')
    sample_model()
    

if __name__ == '__main__':
    main()