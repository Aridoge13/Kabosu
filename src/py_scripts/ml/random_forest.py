# Kabosu Machine Learning Pipeline

from sklearn.model_selection import train_test_split
from sklearn.metrics import RocCurveDisplay
from sklearn.preprocessing import StandardScaler
import pandas as pd
import matplotlib.pyplot as plt
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (classification_report,
                             roc_auc_score,
                             confusion_matrix,
                             ConfusionMatrixDisplay)
from sklearn.model_selection import GridSearchCV
import tensorflow as tf
from keras import layers, callbacks
import shap

# 1. Random Forest Baseline Model
print("Training Random Forest Baseline...")

# Load or define datasets
# Replace with your dataset path
data = pd.read_csv(input("Path to dataset"))
# Replace "target" with your target column name
X = data.drop(columns=["target"])
y = data["target"]

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

rf_model = RandomForestClassifier(
    n_estimators=100,
    max_depth=10,
    random_state=42,
    class_weight='balanced'  # Important for imbalanced datasets
)
rf_model.fit(X_train, y_train)

# Evaluate
y_pred = rf_model.predict(X_test)
y_proba = rf_model.predict_proba(X_test)[:, 1]

print("\nRandom Forest Performance:")
print(classification_report(y_test, y_pred))
print(f"AUC-ROC: {roc_auc_score(y_test, y_proba):.3f}")

# Confusion Matrix for Random Forest
cm_rf = confusion_matrix(y_test, y_pred)
ConfusionMatrixDisplay(cm_rf).plot()
plt.title("Random Forest Confusion Matrix")
plt.tight_layout()
plt.savefig(input("Provide path to save Random Forest confusion matrix:"))
plt.close()

# Save model
joblib.dump(rf_model, input("provide path to save the model"))

# 2. Hyperparameter Tuning
print("\nPerforming Hyperparameter Tuning...")

param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [5, 10, None],
    'min_samples_split': [2, 5, 10]
}

grid_search = GridSearchCV(
    RandomForestClassifier(random_state=42, class_weight='balanced'),
    param_grid,
    cv=5,
    scoring='roc_auc',
    n_jobs=-1  # Use all available cores
)
grid_search.fit(X_train, y_train)

print("Best parameters found:", grid_search.best_params_)
best_model = grid_search.best_estimator_

# 3. Model Interpretation
print("\nGenerating Model Interpretations...")

# Feature Importance
importances = pd.DataFrame({
    'Transcript': X.columns,
    'Importance': best_model.feature_importances_
}).sort_values('Importance', ascending=False)

# Plot top 20 transcripts
plt.figure(figsize=(10, 8))
plt.barh(importances['Transcript'][:20], importances['Importance'][:20])
plt.title("Top 20 Important Transcripts")
plt.xlabel("Feature Importance Score")
plt.tight_layout()
plt.savefig(input("provide path to save the figures:"))
plt.close()

# SHAP Analysis (sample 100 instances for speed)
explainer = shap.TreeExplainer(best_model)
shap_values = explainer.shap_values(X_test.iloc[:100])

plt.figure()
shap.summary_plot(shap_values, X_test.iloc[:100], plot_type="bar", show=False)
plt.tight_layout()
plt.savefig(input("Provide path to save the SHAP summary figure"))
plt.close()

# Neural Network Model
print("\nTraining Neural Network...")

# Normalize data for NN
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Define model architecture
nn_model = tf.keras.Sequential([
    layers.Dense(256, activation='relu', input_shape=(X_train.shape[1],)),
    layers.BatchNormalization(),
    layers.Dropout(0.5),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.3),
    layers.Dense(1, activation='sigmoid')
])

# Custom metrics
METRICS = [
    tf.keras.metrics.BinaryAccuracy(name='accuracy'),
    tf.keras.metrics.AUC(name='auc'),
    tf.keras.metrics.Precision(name='precision'),
    tf.keras.metrics.Recall(name='recall')
]

# Compile model
nn_model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
    loss='binary_crossentropy',
    metrics=METRICS
)

# Callbacks
early_stopping = callbacks.EarlyStopping(
    monitor='val_auc',
    patience=5,
    mode='max',
    restore_best_weights=True
)

# Train model
history = nn_model.fit(
    X_train_scaled, y_train,
    validation_split=0.2,
    epochs=50,
    batch_size=64,
    callbacks=[early_stopping],
    verbose=1
)

# Evaluate
nn_pred = (nn_model.predict(X_test_scaled) > 0.5).astype(int)
print("\nNeural Network Performance:")
print(classification_report(y_test, nn_pred))

# Confusion Matrix for Neural Network
cm_nn = confusion_matrix(y_test, nn_pred)
ConfusionMatrixDisplay(cm_nn).plot()
plt.title("Neural Network Confusion Matrix")
plt.tight_layout()
plt.savefig(input("Provide path to save Neural Network confusion matrix:"))
plt.close()

# Save model and scaler
nn_model.save(input("Provide the path to save the Neural Network Model"))
joblib.dump(scaler, input("Provide path to save the scaler"))

# 5. Model Comparison
print("\nComparing Model Performance:")

# Generate ROC curves for both models

plt.figure(figsize=(10, 8))
# Random Forest ROC
RocCurveDisplay.from_estimator(
    best_model, X_test, y_test, name='Random Forest')
# Neural Network ROC
RocCurveDisplay.from_estimator(
    nn_model, X_test_scaled, y_test, name='Neural Network')
plt.title('ROC Curve Comparison')
plt.plot([0, 1], [0, 1], 'k--')
plt.tight_layout()
plt.savefig(input("Provide the path to save the figure for ROC comparison"))
plt.close()

print("\nKabosu model training complete!")
