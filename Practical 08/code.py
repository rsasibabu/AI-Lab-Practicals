import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

df = pd.read_csv("student_course_reviews_500.csv")
df.head(10)
df.shape
(500, 2)
df.info()
df.isna().any()
df.isna().sum()
df_clean = df.dropna()
df_clean.shape
df_clean.isna().sum()
df_clean['sentiment'].unique()
df_clean['sentiment'].value_counts()

x = df_clean['review_text']
y = df_clean['sentiment']
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.3, random_state=42, stratify=y
)

vectorizer = CountVectorizer()
x_train_vec = vectorizer.fit_transform(x_train)
x_test_vec = vectorizer.transform(x_test)

model = MultinomialNB()
model.fit(x_train_vec, y_train)
y_pred = model.predict(x_test_vec)
print(classification_report(y_test, y_pred))

new_reviews = [
    "The professor explained every single concept very clearly.",
    "Exams were unreasonably long and grading was completely unfair.",
    "Decent lectures, matched standard course content."
]
new_reviews_vec = vectorizer.transform(new_reviews)
predictions = model.predict(new_reviews_vec)
for review, pred in zip(new_reviews, predictions):
    print(f"Review: '{review}' --> Predicted Sentiment: {pred}")
