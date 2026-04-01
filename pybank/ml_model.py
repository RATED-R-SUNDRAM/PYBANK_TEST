#
""" 
OBJECTIVE IS TO CREATE MULTIPLE JUPYTER NOTEBOOK TYPE CELLS FOR VISUALIZATION OF DIFFERENT STEPS
OF ML MODEL BUILDING 
1. Loading libraries
2. loading iris data and creating pandas dataframe
3. BASIC EDA , checks and distributions
4. BASIC PREPROCESSING - train test split and scaling
5. MODEL BUILDING - XGBOOST CLASSIFIER
6. MODEL EVALUATION - confusion matrix and classification report
"""

#%%
# 1. Loading libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, classification_report
from xgboost import XGBClassifier

#%%

# 2. loading iris data and creating pandas dataframe
from sklearn.datasets import load_iris
iris = load_iris()
df = pd.DataFrame(data= iris.data, columns=iris.feature_names)
df['target'] = iris.target
df.head()
# %%
# 3. BASIC EDA , checks and distributions
print(df.info())
print(df.describe())
sns.pairplot(df, hue='target')
plt.show()
# %%
# 4. BASIC PREPROCESSING - train test split and scaling
X = df.drop('target', axis=1)
y = df['target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
# %%
model = XGBClassifier(
    n_estimators=2000,           # More trees
    learning_rate=0.05,         # Lower learning rate (slower, often better)
    max_depth=5,                # Shallower trees                   # More L2 regularization
    alpha=0.5,                  # L1 regularization
    gamma=1,                    # Minimum loss reduction
    subsample=0.8,              # Use 80% of training data per tree
    colsample_bytree=0.8,       # Use 80% of features per tree
    use_label_encoder=False, 
    eval_metric='mlogloss'
)
model.fit(X_train, y_train, obj=weighted_loss)
# %%
# 6. MODEL EVALUATION
y_pred = model.predict(X_test)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

# %%
