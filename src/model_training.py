import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

def train_model():
    df = pd.read_csv('data/cleaned_data.csv', index_col=0, parse_dates=True)
    df['Target'] = (df['Return'] > 0).astype(int)

    X = df[['Open', 'High', 'Low', 'Close', 'Volume']]
    y = df['Target']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

    clf = RandomForestClassifier()
    clf.fit(X_train, y_train)
    preds = clf.predict(X_test)

    print("\n📊 Classification Report:")
    print(classification_report(y_test, preds))
