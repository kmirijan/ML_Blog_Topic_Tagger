import json
from joblib import load
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer

def main():
	classifier = {}

	with open('classifier.json', 'r') as f:
		classifier = json.load(f)

	lda_model = load('lda_model.joblib')
	vectorizer = load('vectorizer.joblib')


	tags = set()
	blog_dict = {}

	with open('json_splits/dev/7596.male.26.Internet.Scorpio.json') as f:
		blog_dict = json.load(f)

	for key in blog_dict['posts']:
		text = blog_dict['posts'][key]['text']

		x = list(lda_model.transform(vectorizer.transform([text]))[0])
		topic_class = (x.index(max(x)))
		tags.add(classifier[str(topic_class)])

	print(tags)





if __name__ == '__main__':
    main()