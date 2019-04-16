newsgroups_test = fetch_20newsgroups(subset='test', categories=cats, remove=('headers', 'footers', 'quotes'))
x_testdata = newsgroups_test.data
y_test = newsgroups_test.target
testdata = [[a_, b_] for a_, b_ in zip(x_testdata, y_test)]

correct = sum(str(pred(get_vectorizer_array(testcase[0]))[0]) == str(testcase[1]) for testcase in testdata)

# Print the accurency in percentage
result = str(correct / len(testdata) * 100) + "%"

result