import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
import matplotlib.pyplot as plt

# 1. Датагаа унших
try:
    df = pd.read_csv('ub_bus_data.csv')
    print("Датаг амжилттай уншлаа!")
except FileNotFoundError:
    print("Алдаа: 'ub_bus_data.csv' файл олдсонгүй!")
    exit()

# 2. Оролт (X) болон Гаралт (y)-ыг тохируулах
X = df[['distance_km', 'hour', 'traffic_index']]
y = df['arrival_time_mins']

# 3. Датагаа сургалтын (80%) болон тестийн (20%) хэсэгт хуваах
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Модель үүсгэж сургах (Gradient Boosting)
print("AI Модель суралцаж байна...")
model = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)
model.fit(X_train, y_train)

# 5. Таамаглал хийх ба үр дүнг шалгах
predictions = model.predict(X_test)
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print(f"\n--- Моделийн үр дүн ---")
print(f"Дундаж алдаа (MAE): {mae:.2f} минут")
print(f"Нарийвчлалын оноо (R2): {r2:.2f}")

# 6. Үр дүнг графикаар харуулах
plt.figure(figsize=(10, 6))
plt.scatter(y_test, predictions, alpha=0.4, color='blue')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
plt.xlabel('Бодит хугацаа (Actual Mins)')
plt.ylabel('AI-ийн таамаглал (Predicted Mins)')
plt.title('UB Bus Arrival: Actual vs Predicted')
plt.grid(True)
plt.show()