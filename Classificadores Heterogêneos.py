import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, jaccard_score

# Criar dados fictícios para exemplo
X, y = make_classification(n_samples=1000, n_features=20, random_state=42)

# Dividir os dados em treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Modelos base
model1 = LogisticRegression(random_state=42)
model2 = DecisionTreeClassifier(random_state=42)
model3 = KNeighborsClassifier(n_neighbors=3)

# Modelo final (meta-classificador)
final_model = LogisticRegression(random_state=42)

# Treinar modelos base nos dados de treinamento
model1.fit(X_train, y_train)
model2.fit(X_train, y_train)
model3.fit(X_train, y_train)

# Fazer previsões dos modelos base nos dados de teste
pred1 = model1.predict(X_test)
pred2 = model2.predict(X_test)
pred3 = model3.predict(X_test)

# Criar conjunto de dados para o modelo final usando as previsões dos modelos base
stacked_X_train = np.column_stack((pred1, pred2, pred3))

# Treinar o modelo final nos dados criados pelo modelo base
final_model.fit(stacked_X_train, y_test)

# Fazer previsões no conjunto de teste usando o modelo de empilhamento
stacked_X_test = np.column_stack((model1.predict(X_test), model2.predict(X_test), model3.predict(X_test)))
stacked_pred = final_model.predict(stacked_X_test)

# Avaliar o desempenho do modelo final
print(f'Acuracia do modelo 1: {accuracy_score(y_test, pred1)}')
print(f'Acuracia do modelo 2: {accuracy_score(y_test, pred2)}')
print(f'Acuracia do modelo 3: {accuracy_score(y_test, pred3)}')
print(f'Acurácia do modelo de empilhamento: {accuracy_score(y_test, stacked_pred)}')
print(f'Matriz do modelo de empilhamento: \n{confusion_matrix(y_test, stacked_pred)}')
print(f'Quoficiente do modelo de empilhamento: {jaccard_score(y_test, stacked_pred)}')
