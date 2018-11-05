import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split

aidir = r'C:\Users\rhynes\Google Drive\UCD\3 - Research\EPO Project'

df=pd.read_pickle(aidir+'\\abstracts.pkl')


train=df.sample(frac=0.8,random_state=200)
test=df.drop(train.index)

X = train['abstract']
y = train['ai']

#X_train, X_valid, y_train, y_valid = train_test_split(X,y, test_size=0.2)

count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(X)

#abstract_counts = count_vect.fit_transform(df['abstract'])

#tf_transformer = sklearn.feature_extraction.text.TfidfTransformer(use_idf=True)

#abstract_tf = tf_transformer.fit_transform(abstract_counts)



text_clf = Pipeline([('vect', 	CountVectorizer()),
					('tfidf', TfidfTransformer()),
					('clf',	MultinomialNB()),
])

text_clf.fit(X, y)

predicted = text_clf.predict(test['abstract'])
np.mean(predicted == test['ai'])