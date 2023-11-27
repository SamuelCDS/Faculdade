import numpy as np

class LogisticRegression:
    def __init__(self, learning_rate=0.01, n_iterations=1000, regularization_strength=0.01, add_bias=True):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.regularization_strength = regularization_strength
        self.add_bias = add_bias
        self.weights = None

    def _sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def _add_bias_column(self, X):
        # Add a column of ones for the bias term if add_bias is True
        if self.add_bias:
            return np.c_[np.ones(X.shape[0]), X]
        return X

    def _calculate_regularization_term(self):
        # Exclude bias term from regularization
        return (self.regularization_strength / 2) * np.sum(self.weights[1:]**2)

    def fit(self, X, y):
        np.random.seed(42)
        X = self._add_bias_column(X)
        self.weights = np.random.rand(X.shape[1])

        for _ in range(self.n_iterations):
            predictions = self._sigmoid(np.dot(X, self.weights))
            errors = y - predictions

            # Compute gradient with regularization term
            gradient = np.dot(X.T, errors) - self.regularization_strength * self.weights
            self.weights += self.learning_rate * gradient

    def predict(self, X):
        X = self._add_bias_column(X)
        return np.round(self._sigmoid(np.dot(X, self.weights)))

    def accuracy(self, X, y):
        predictions = self.predict(X)
        accuracy = np.mean(predictions == y)
        return accuracy

    def precision_recall_f1(self, X, y):
        predictions = self.predict(X)
        tp = np.sum((predictions == 1) & (y == 1))
        fp = np.sum((predictions == 1) & (y == 0))
        fn = np.sum((predictions == 0) & (y == 1))

        precision = tp / (tp + fp) if (tp + fp) != 0 else 0
        recall = tp / (tp + fn) if (tp + fn) != 0 else 0
        f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) != 0 else 0

        return precision, recall, f1

class DecisionTree:
    def __init__(self, max_depth=None):
        self.max_depth = max_depth
        self.tree = None

    def _calculate_gini(self, y):
        classes, counts = np.unique(y, return_counts=True)
        probabilities = counts / len(y)
        gini = 1 - np.sum(probabilities**2)
        return gini

    def _split_dataset(self, X, y, feature_index, threshold):
        left_mask = X[:, feature_index] <= threshold
        right_mask = ~left_mask
        return X[left_mask], y[left_mask], X[right_mask], y[right_mask]

    def _find_best_split(self, X, y):
        m, n = X.shape
        best_gini = float('inf')
        best_feature_index = None
        best_threshold = None

        for feature_index in range(n):
            thresholds = np.unique(X[:, feature_index])
            for threshold in thresholds:
                X_left, y_left, X_right, y_right = self._split_dataset(X, y, feature_index, threshold)

                if len(y_left) == 0 or len(y_right) == 0:
                    continue

                gini_left = len(y_left) / m * self._calculate_gini(y_left)
                gini_right = len(y_right) / m * self._calculate_gini(y_right)
                gini = gini_left + gini_right

                if gini < best_gini:
                    best_gini = gini
                    best_feature_index = feature_index
                    best_threshold = threshold

        return best_feature_index, best_threshold

    def _build_tree(self, X, y, depth):
        if depth == 0 or len(np.unique(y)) == 1:
            # If max depth is reached or only one class is present, create a leaf node
            return {"class": np.bincount(y).argmax()}

        feature_index, threshold = self._find_best_split(X, y)

        if feature_index is None:
            # No split found, create a leaf node
            return {"class": np.bincount(y).argmax()}

        X_left, y_left, X_right, y_right = self._split_dataset(X, y, feature_index, threshold)
        if depth:
            left_subtree = self._build_tree(X_left, y_left, depth - 1)
            right_subtree = self._build_tree(X_right, y_right, depth - 1)

            return {"feature_index": feature_index, "threshold": threshold, "left": left_subtree, "right": right_subtree}

    def fit(self, X, y):
        self.tree = self._build_tree(X, y, self.max_depth)

    def _predict_sample(self, sample, tree):
        if "class" in tree:
            return tree["class"]
        if sample[tree["feature_index"]] <= tree["threshold"]:
            return self._predict_sample(sample, tree["left"])
        else:
            return self._predict_sample(sample, tree["right"])

    def predict(self, X):
        return np.array([self._predict_sample(sample, self.tree) for sample in X])

class KNeighborsClassifier:
    def __init__(self, k=3):
        self.k = k
        self.X_train = None
        self.y_train = None

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def _calculate_distances(self, X):
        # Calcula as distâncias euclidianas entre os pontos em X_train e X
        return np.linalg.norm(self.X_train - X[:, np.newaxis], axis=2)

    def predict(self, X):
        distances = self._calculate_distances(X)
        
        # Encontra os índices dos k vizinhos mais próximos para cada ponto em X
        k_neighbors_indices = np.argsort(distances, axis=1)[:, :self.k]
        
        # Obtém os rótulos dos k vizinhos mais próximos
        k_neighbors_labels = self.y_train[k_neighbors_indices]
        
        # Para cada ponto em X, retorna o rótulo mais comum entre os k vizinhos mais próximos
        return np.apply_along_axis(lambda x: np.bincount(x).argmax(), axis=1, arr=k_neighbors_labels)

class StackingClassifier:
    def __init__(self, base_models, final_model):
        """
        StackingClassifier.

        Parameters:
        - base_models (list): Lista de modelos de base.
        - final_model: Modelo final que utiliza as previsões dos modelos de base.
        """
        self.base_models = base_models
        self.final_model = final_model

    def fit(self, X, y, validation_data=None):
        """
        Treina os modelos de base e o modelo final.

        Parameters:
        - X (array-like): Dados de treinamento.
        - y (array-like): Rótulos de treinamento.
        - validation_data (tuple, optional): Dados de validação na forma (X_val, y_val).

        Returns:
        - self
        """
        # Verificação de tipos
        if not all(hasattr(model, 'fit') and hasattr(model, 'predict') for model in self.base_models):
            raise ValueError("Todos os modelos de base devem ter métodos 'fit' e 'predict'.")

        if not hasattr(self.final_model, 'fit') or not hasattr(self.final_model, 'predict'):
            raise ValueError("O modelo final deve ter métodos 'fit' e 'predict'.")

        # Treina modelos de base
        base_predictions = []
        for model in self.base_models:
            model.fit(X, y)
            base_predictions.append(model.predict(X))

        base_predictions = np.column_stack(base_predictions)

        # Treina modelo final
        if validation_data is not None:
            X_val, y_val = validation_data
            val_predictions = [model.predict(X_val) for model in self.base_models]
            val_predictions = np.column_stack(val_predictions)
            self.final_model.fit(base_predictions, y, validation_data=(val_predictions, y_val))
        else:
            self.final_model.fit(base_predictions, y)

        return self

    def predict(self, X):
        """
        Faz previsões usando os modelos treinados.

        Parameters:
        - X (array-like): Dados de entrada.

        Returns:
        - array: Previsões do modelo final.
        """
        base_predictions = np.column_stack([model.predict(X) for model in self.base_models])
        return self.final_model.predict(base_predictions)

    def predict_proba(self, X):
        """
        Faz previsões de probabilidade usando os modelos treinados (se disponíveis).

        Parameters:
        - X (array-like): Dados de entrada.

        Returns:
        - array: Probabilidades previstas pelo modelo final.
        """
        if hasattr(self.final_model, 'predict_proba'):
            base_probabilities = [model.predict_proba(X) for model in self.base_models]
            base_probabilities = np.column_stack(base_probabilities)
            return self.final_model.predict_proba(base_probabilities)
        else:
            raise AttributeError("O modelo final não suporta o método 'predict_proba'.")


# Dados fictícios para exemplo
np.random.seed(42)
X = np.random.rand(100, 5)
y = np.random.randint(0, 2, size=100)

# Modelos base
logistic_model = LogisticRegression()
tree_model = DecisionTree()
knn_model = KNeighborsClassifier()

# Modelo final (meta-classificador)
final_model = LogisticRegression()

# Modelo de empilhamento
stacking_model = StackingClassifier(base_models=[logistic_model, tree_model, knn_model], final_model=final_model)

# Treinar o modelo de empilhamento
stacking_model.fit(X, y)

# Fazer previsões usando o modelo de empilhamento
stacking_predictions = stacking_model.predict(X)

# Avaliar o desempenho do modelo de empilhamento
accuracy = np.mean(stacking_predictions == y)
print(f'Acurácia do modelo de empilhamento: {accuracy}')
