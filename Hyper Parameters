cats = ['rec.sport.hockey', 'sci.crypt', 'sci.electronics', 'sci.space', 'rec.motorcycles', 'misc.forsale']
newsgroups = fetch_20newsgroups(subset='train', categories=cats, remove=('headers', 'footers', 'quotes'))
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(newsgroups.data)
y = newsgroups.target
metric = 'euclidean'