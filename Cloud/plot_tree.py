import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, learning_curve
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn.utils import shuffle
import matplotlib.pyplot as plt

csv_path = r'D:\Licenta\Licenta\Cloud\dataset_final.csv'
dataset = pd.read_csv(csv_path)
dataset = shuffle(dataset, random_state=42)

features = ['Area','Instructions', 'Size','Priority', 'Bandwidth', 'Delay', 'Score']
X = dataset[features]
y = dataset['Allocated_Worker']

X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.4, random_state=42, stratify=y)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42, stratify=y_temp)

clf = DecisionTreeClassifier(random_state=42, max_depth=5, min_samples_split=10, min_samples_leaf=5)
clf.fit(X_train, y_train)

def plot_tree_customized(*args, **kwargs):
    tree_fig = plot_tree(*args, **kwargs)
    for node in tree_fig:
        color = node.get_bbox_patch().get_facecolor()
        new_color = (
            min(color[0] * 1.2, 1.0), 
            min(color[1] * 0.8, 1.0), 
            min(color[2] * 0.6, 1.0),
            color[3] 
        ) 
        node.get_bbox_patch().set_facecolor(new_color)
        if "node #3" in node.get_text():
            node.get_bbox_patch().set_facecolor('lightblue')
        node.get_bbox_patch().set_edgecolor('black')
    return tree_fig

plt.figure(figsize=(15, 15), dpi=100)

plot_tree_customized(clf, 
          feature_names=X.columns, 
          class_names=[str(i) for i in clf.classes_], 
          filled=True, 
          rounded=True, 
          fontsize=16,  
          precision=2,  
          impurity=True, 
          node_ids=True,  
          proportion=True, 
          label='all',
          max_depth=5  
         )

plt.show()
