# ML_Blog_Topic_Tagger

This project creates a model that generates tags for blogs.

The data for the project can be found at this link: http://u.cs.biu.ac.il/~koppel/blogs/
I used blogs.zip

process_blogs.py: Cleans up the xml data and text, then turns it into json. The xml data is very malformed

split_data.py: Splits the json data into dev, train, and test.

pred_top_model.py: Vectorizes the text data and generates an LDA model. The vectorizer, model, and clustered topic tags
				are then saved.

lda_predict.py: Loads the vectorizer, model, and tag set. Test file to check how the tags come out.
