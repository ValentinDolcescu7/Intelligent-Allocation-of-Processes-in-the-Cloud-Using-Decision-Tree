import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, ConfusionMatrixDisplay
from sklearn.utils import shuffle
from joblib import dump, load
import matplotlib.pyplot as plt
import os

csv_path = r'D:\Licenta\Test7\Cloud\dataset_final.csv'
dataset = pd.read_csv(csv_path)

dataset = shuffle(dataset, random_state=42)

features = ['Area','Instructions', 'Size','Priority', 'Bandwidth', 'Delay', 'Score']

X = dataset[features]
y = dataset['Allocated_Worker']

X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.4, random_state=42, stratify=y)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42, stratify=y_temp)

clf = DecisionTreeClassifier(random_state=42, max_depth=5, min_samples_split=10, min_samples_leaf=5)
clf.fit(X_train, y_train)

y_train_pred = clf.predict(X_train)
train_accuracy = accuracy_score(y_train, y_train_pred)
train_conf_matrix = confusion_matrix(y_train, y_train_pred)
train_class_report = classification_report(y_train, y_train_pred, zero_division=0)

print(f'Training Accuracy: {train_accuracy}')
print('Training Classification Report:')
print(train_class_report)
print('Training Confusion Matrix:')
print(train_conf_matrix)

ConfusionMatrixDisplay(train_conf_matrix, display_labels=clf.classes_).plot(cmap=plt.cm.Blues)
plt.title('Matricea de confuzie - Setul de antrenament')
plt.show()

y_val_pred = clf.predict(X_val)
val_accuracy = accuracy_score(y_val, y_val_pred)
val_conf_matrix = confusion_matrix(y_val, y_val_pred)
val_class_report = classification_report(y_val, y_val_pred, zero_division=0)

print(f'Validation Accuracy: {val_accuracy}')
print('Validation Classification Report:')
print(val_class_report)
print('Validation Confusion Matrix:')
print(val_conf_matrix)

y_test_pred = clf.predict(X_test)
test_accuracy = accuracy_score(y_test, y_test_pred)
test_conf_matrix = confusion_matrix(y_test, y_test_pred)
test_class_report = classification_report(y_test, y_test_pred, zero_division=0)

print(f'Test Accuracy: {test_accuracy}')
print('Test Classification Report:')
print(test_class_report)
print('Test Confusion Matrix:')
print(test_conf_matrix)

ConfusionMatrixDisplay(test_conf_matrix, display_labels=clf.classes_).plot(cmap=plt.cm.Blues)
plt.title('Matricea de confuzie - Setul de testare')
plt.show()

model_path = r'D:\Licenta\Licenta\allocated_worker_model.joblib'
dump(clf, model_path)





