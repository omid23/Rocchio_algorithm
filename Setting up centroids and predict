check_classification_targets(y)
n_samples, n_features = X.shape
le = LabelEncoder()
y_indices = le.fit_transform(y)
classes = le.classes_
n_classes = classes.size

# Mask mapping each class to its members.
centroids = np.empty((n_classes, n_features), dtype=np.float64)
# Number of clusters in each class.
n_cluster = np.zeros(n_classes)

for current_class in range(n_classes):
    center_mask = y_indices == current_class
    n_cluster[current_class] = np.sum(center_mask)
    centroids[current_class] = X[center_mask].mean(axis=0)
    
def get_vectorizer_array(query):
    return vectorizer.transform([query]).toarray()


def pred(X):
    return classes[pairwise_distances(X, centroids, metric=metric).argmin(axis=1)]

