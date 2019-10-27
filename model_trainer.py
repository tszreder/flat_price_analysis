from read_csv import load_clean_data
import pandas as pd

file = 'flats.csv'

train = load_clean_data(file)[0]
target = load_clean_data(file)[1]

# print(train.shape)
# print(target.shape)
# print(train.dtypes)
# print(target.value_counts())

from sklearn.model_selection import train_test_split


data_train, data_test, target_train, target_test = train_test_split(
    train, target, test_size=0.30, random_state=10)

# print(data_train.shape)
# print(data_test.shape)
# print(target_train.shape)
# print(target_test.shape)

from sklearn.naive_bayes import BernoulliNB, GaussianNB
from sklearn.svm import LinearSVC, SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, recall_score, confusion_matrix, classification_report

# svc_model = LinearSVC(random_state=0, max_iter=1000, C=1000)
# svc_model = SVC(kernel='rbf', max_iter=1000, C=1000)

knn_model = KNeighborsClassifier(n_neighbors=11, weights='distance')


# svc_model = SVC(kernel='poly', max_iter=1000, C=1000)
# pred_test = svc_model.fit(data_train, target_train).predict(data_test)
pred_test = knn_model.fit(data_train, target_train).predict(data_test)
pred_test = pd.Series(pred_test).astype('str')
target_test = pd.Series(target_test).astype('str')

# print(pred_test.dtypes)
# print(target_test.dtypes)

print('Confusion Matrix - Testing Dataset')
print(pd.crosstab(target_test.ravel(), pred_test.ravel(), rownames = ['True'], colnames = ['Predicted'], margins = True))

print("SVC accuracy, C=1000 : ", accuracy_score(target_test, pred_test))
# print(confusion_matrix(y_true=target_test, y_pred=pred_test))
# print("SVC recall, C=1000 : ", recall_score(target_test, pred_test))
print(classification_report(y_true=target_test, y_pred=pred_test))
# #
# svc_model = LinearSVC(random_state=0, max_iter=1000, C=1)
# pred_test = svc_model.fit(data_train, target_train).predict(data_test)
# print("SVC accuracy, C=1 : ", accuracy_score(target_test, pred_test, normalize=True))
# # print("SVC recall, C=1 : ", recall_score(target_test, pred_test))
# # print(classification_report(y_true=target_test, y_pred=pred_test))
# #
# svc_model = LinearSVC(random_state=0, max_iter=1000, C=0.1)
# pred_test = svc_model.fit(data_train, target_train).predict(data_test)
# print("SVC accuracy, C=0.1 : ", accuracy_score(target_test, pred_test, normalize=True))
# # print("SVC recall, C=1 : ", recall_score(target_test, pred_test))
# # print(classification_report(y_true=target_test, y_pred=pred_test))