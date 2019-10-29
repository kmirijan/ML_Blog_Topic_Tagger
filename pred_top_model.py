import os,json, nltk
from joblib import dump
from nltk.corpus import brown
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer


DATAPATH = 'json_splits/'

def get_tags(model, vectorizer, top_n=10):
	classifier = {}
	for idx, topic in enumerate(model.components_):
		x = [(vectorizer.get_feature_names()[i], topic[i])
                        for i in topic.argsort()[:-top_n - 1:-1]]
		classifier[idx] = x[0][0]

	return classifier

def main():
	file_names = os.listdir(DATAPATH + 'dev/')

	data = []
	 
	for filename in file_names:
		path = DATAPATH + 'dev/' + filename
		blog_dict = {}
		with open(path, 'r') as f:
			blog_dict = json.load(f)

		for key in blog_dict['posts']:
			document = blog_dict['posts'][key]['text']
			data.append(document)
	 
	NO_DOCUMENTS = len(data)
	print(NO_DOCUMENTS)

	NUM_TOPICS = 50
 
	vectorizer = CountVectorizer(min_df=5, max_df=0.9, 
	                             stop_words='english', lowercase=True, 
	                             token_pattern='[a-zA-Z\-][a-zA-Z\-]{2,}')
	data_vectorized = vectorizer.fit_transform(data)
	 
	# Build a Latent Dirichlet Allocation Model
	lda_model = LatentDirichletAllocation(n_components=NUM_TOPICS, max_iter=10, learning_method='online')
	lda_Z = lda_model.fit_transform(data_vectorized)
	# print(lda_Z.shape)  # (NO_DOCUMENTS, NO_TOPICS)
	print("LDA Model:")
	classifier = get_tags(lda_model, vectorizer)
	with open('classifier.json', 'w') as fp:
			json.dump(classifier, fp)


	dump(lda_model, 'lda_model.joblib') 
	dump(vectorizer, 'vectorizer.joblib')

	print('---------------------------DONE---------------------------')

if __name__ == '__main__':
    main()