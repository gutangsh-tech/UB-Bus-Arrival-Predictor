import pandas as pd
import numpy as np

def generate_bus_data(samples=2000):
    np.random.seed(42)
    distance = np.random.uniform(0.5, 10, samples) # Буудлаас холдох зай
    hour = np.random.randint(7, 22, samples)       # Цаг
    
    # Түгжрэлийн индекс (8:00 болон 18:00 цагт их байна)
    traffic_factor = 0.2 + 0.8 * (np.exp(-(hour-8)**2/4) + np.exp(-(hour-18)**2/4))
    
    # Ирэх хугацааг тооцоолох логик
    arrival_time = (distance / 40) * 60 * (1 + traffic_factor * 3) + np.random.normal(2, 1, samples)
    
    # Датаг хүснэгт болгох
    df = pd.DataFrame({
        'distance_km': distance,
        'hour': hour,
        'traffic_index': traffic_factor,
        'arrival_time_mins': np.maximum(1, arrival_time)
    })
    return df

# Энэ хэсэг заавал хамгийн зүүн талдаа, ямар ч зайгүй байх ёстой
if __name__ == "__main__":
    print("Дата үүсгэж байна...")
    bus_df = generate_bus_data()
    bus_df.to_csv('ub_bus_data.csv', index=False)
    print("Амжилттай! 'ub_bus_data.csv' файл үүслээ.")