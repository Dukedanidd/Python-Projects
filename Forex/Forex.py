import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dropout, GRU, Dense
from datetime import datetime, timedelta
import os

class ForexPredictor:
    def __init__(self, par_divisas='EURUSD=X', prediction_days=60):
        self.par_divisas = par_divisas
        self.prediction_days = prediction_days
        self.model = None
        self.scaler = MinMaxScaler(feature_range=(0,1))
        self.hist = None
        
    def cargar_datos(self, start_date='2016-1-1', end_date=None):
        if end_date is None:
            end_date = datetime.now().strftime('%Y-%m-%d')
            
        try:
            ticker = yf.Ticker(self.par_divisas)
            self.hist = ticker.history(start=start_date, end=end_date)
            if self.hist.empty:
                raise ValueError(f"No se encontraron datos para {self.par_divisas}")
                
            print(f"Datos cargados para {self.par_divisas}")
            print(f"Período: {start_date} hasta {end_date}")
            print(f"Total de registros: {len(self.hist)}")
            return self.hist
        except Exception as e:
            print(f"Error al cargar datos: {str(e)}")
            return None

    def preparar_datos(self):
        if self.hist is None:
            raise ValueError("Primero debe cargar los datos usando cargar_datos()")
            
        try:
            scaled_data = self.scaler.fit_transform(self.hist['Close'].values.reshape(-1,1))
            
            x_train = []
            y_train = []
            
            for x in range(self.prediction_days, len(scaled_data)):
                x_train.append(scaled_data[x-self.prediction_days:x, 0])
                y_train.append(scaled_data[x, 0])
                
            x_train, y_train = np.array(x_train), np.array(y_train)
            x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
            
            return x_train, y_train
        except Exception as e:
            print(f"Error al preparar datos: {str(e)}")
            return None, None

    def crear_modelo(self, units=100, dropout_rate=0.2):
        try:
            model = Sequential([
                GRU(units=units, return_sequences=True, 
                    input_shape=(self.prediction_days, 1)),
                Dropout(dropout_rate),
                GRU(units=units, return_sequences=True),
                Dropout(dropout_rate),
                GRU(units=units),
                Dropout(dropout_rate),
                Dense(units=1)
            ])
            
            model.compile(optimizer='adam', loss='mean_squared_error')
            self.model = model
            model.summary()
            return model
        except Exception as e:
            print(f"Error al crear modelo: {str(e)}")
            return None

    def entrenar_modelo(self, x_train, y_train, epochs=100, batch_size=32, validation_split=0.1):
        if self.model is None:
            raise ValueError("Primero debe crear el modelo usando crear_modelo()")
            
        try:
            history = self.model.fit(
                x_train, 
                y_train, 
                epochs=epochs, 
                batch_size=batch_size,
                validation_split=validation_split,
                verbose=1
            )
            
            plt.figure(figsize=(12,6))
            plt.plot(history.history['loss'], label='Loss de entrenamiento')
            plt.plot(history.history['val_loss'], label='Loss de validación')
            plt.title('Historial de Entrenamiento')
            plt.xlabel('Época')
            plt.ylabel('Loss')
            plt.legend()
            plt.grid(True)
            plt.show()
            
            return history
        except Exception as e:
            print(f"Error durante el entrenamiento: {str(e)}")
            return None

    def predecir_precios(self, test_start='2022-1-1', test_end='2023-2-1'):
        if self.model is None:
            raise ValueError("Primero debe crear y entrenar el modelo")
            
        try:
            hist_test = yf.Ticker(self.par_divisas).history(start=test_start, end=test_end)
            actual_prices = hist_test['Close'].values
            
            total_dataset = pd.concat((self.hist['Close'], hist_test['Close']), axis=0)
            model_inputs = total_dataset[len(total_dataset)-len(hist_test)-self.prediction_days:].values
            model_inputs = self.scaler.transform(model_inputs.reshape(-1,1))
            
            x_test = []
            for x in range(self.prediction_days, len(model_inputs)):
                x_test.append(model_inputs[x-self.prediction_days:x, 0])
                
            x_test = np.array(x_test)
            x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
            
            predicted_prices = self.model.predict(x_test)
            predicted_prices = self.scaler.inverse_transform(predicted_prices)
            
            return actual_prices, predicted_prices
        except Exception as e:
            print(f"Error al predecir precios: {str(e)}")
            return None, None

    def guardar_modelo(self, ruta='modelo_forex.h5'):
       
        if self.model is None:
            raise ValueError("No hay modelo para guardar")
        try:
            self.model.save(ruta)
            print(f"Modelo guardado en {ruta}")
        except Exception as e:
            print(f"Error al guardar el modelo: {str(e)}")
        
    def cargar_modelo(self, ruta='modelo_forex.h5'):
        
        if not os.path.exists(ruta):
            raise FileNotFoundError(f"No se encontró el modelo en {ruta}")
        try:
            self.model = load_model(ruta)
            print(f"Modelo cargado desde {ruta}")
        except Exception as e:
            print(f"Error al cargar el modelo: {str(e)}")

    def predecir_futuros_dias(self, dias=30):
        if self.model is None:
            raise ValueError("Primero debe crear y entrenar el modelo")
            
        try:
            last_data = self.hist['Close'].values[-self.prediction_days:]
            future_predictions = []
            current_batch = last_data
            
            for _ in range(dias):
                current_batch_scaled = self.scaler.transform(current_batch.reshape(-1,1))
                current_batch_reshaped = np.reshape(current_batch_scaled, 
                                                  (1, self.prediction_days, 1))
                
                prediction = self.model.predict(current_batch_reshaped, verbose=0)
                prediction_unscaled = self.scaler.inverse_transform(prediction)[0][0]
                future_predictions.append(prediction_unscaled)
                
                current_batch = np.append(current_batch[1:], prediction_unscaled)
            
            return future_predictions
        except Exception as e:
            print(f"Error al predecir días futuros: {str(e)}")
            return None

    def visualizar_predicciones(self, actual_prices, predicted_prices, save_path=None):
        try:
            plt.figure(figsize=(12,6))
            plt.plot(actual_prices, color='red', label=f'{self.par_divisas} precios reales')
            plt.plot(predicted_prices, color='green', label=f'{self.par_divisas} precios predichos')
            plt.title(f'Predicción de {self.par_divisas}')
            plt.xlabel('Tiempo')
            plt.ylabel('Precio')
            plt.legend()
            plt.grid(True)
            
            if save_path:
                plt.savefig(save_path)
                print(f"Gráfica guardada en {save_path}")
            
            plt.show()
        except Exception as e:
            print(f"Error al visualizar predicciones: {str(e)}")

    def calcular_rentabilidad(self, actual_prices, predicted_prices):
        try:
            rentabilidad = 1
            señales = []
            
            for i in range(1, len(actual_prices)):
                if predicted_prices[i-1] > actual_prices[i-1]:
                    # Señal de compra
                    rentabilidad_dia = actual_prices[i] / actual_prices[i-1]
                    rentabilidad *= rentabilidad_dia
                    señales.append(('COMPRA', (rentabilidad_dia-1)*100))
                else:
                    # Señal de venta
                    rentabilidad_dia = actual_prices[i-1] / actual_prices[i]
                    rentabilidad *= rentabilidad_dia
                    señales.append(('VENTA', (rentabilidad_dia-1)*100))
                    
            return rentabilidad, señales
        except Exception as e:
            print(f"Error al calcular rentabilidad: {str(e)}")
            return None, None
    def guardar_modelo(self, ruta='modelo_forex.h5'):
        if self.model is None:
            raise ValueError("No hay modelo para guardar")
        try:
            self.model.save(ruta)
            print(f"Modelo guardado en {ruta}")
        except Exception as e:
            print(f"Error al guardar el modelo: {str(e)}")
            
    def cargar_modelo(self, ruta='modelo_forex.h5'):
        if not os.path.exists(ruta):
            raise FileNotFoundError(f"No se encontró el modelo en {ruta}")
        try:
            self.model = load_model(ruta)
            print(f"Modelo cargado desde {ruta}")
        except Exception as e:
            print(f"Error al cargar el modelo: {str(e)}")
def visualizar_predicciones_completas(predictor, actual_prices, predicted_prices, future_predictions):
    try:
        plt.figure(figsize=(12,6))
        
        # Crear array de días para el eje x
        dias_historicos = np.arange(len(actual_prices))
        dias_futuros = np.arange(len(actual_prices)-1, 
                                len(actual_prices) + len(future_predictions))
        
        # Plotear datos históricos
        plt.plot(dias_historicos, actual_prices, 
                color='red', label='Precios reales')
        plt.plot(dias_historicos, predicted_prices, 
                color='green', label='Predicciones históricas')
        
        # Plotear predicciones futuras
        plt.plot(dias_futuros, 
                np.concatenate(([actual_prices[-1]], future_predictions)),
                color='blue', linestyle='--', label='Predicciones futuras')
        
        plt.title(f'Predicción de {predictor.par_divisas} con proyección futura')
        plt.xlabel('Días')
        plt.ylabel('Precio')
        plt.legend()
        plt.grid(True)
        plt.show()
    except Exception as e:
        print(f"Error al visualizar predicciones completas: {str(e)}")
def entrenar_modelo():
    try:
        print("Iniciando entrenamiento del modelo...")
        
        # Inicializar el predictor
        predictor = ForexPredictor(par_divisas='EURUSD=X', prediction_days=60)
        
        # Cargar y preparar datos
        print("\nCargando datos históricos...")
        predictor.cargar_datos(start_date='2016-1-1')
        
        print("\nPreparando datos para entrenamiento...")
        x_train, y_train = predictor.preparar_datos()
        
        # Crear y entrenar modelo
        print("\nCreando modelo...")
        predictor.crear_modelo(units=100, dropout_rate=0.2)
        
        print("\nIniciando entrenamiento...")
        predictor.entrenar_modelo(
            x_train, 
            y_train, 
            epochs=100,
            batch_size=32,
            validation_split=0.1
        )
        
        # Guardar el modelo entrenado
        print("\nGuardando modelo...")
        predictor.guardar_modelo('/content/modelo_forex_entrenado.h5')
        
        print("\nEntrenamiento completado exitosamente!")
        return predictor
        
    except Exception as e:
        print(f"\nError durante el entrenamiento: {str(e)}")
        return None


def main():
    try:
        # Inicializar el predictor
        predictor = ForexPredictor(par_divisas='EURUSD=X', prediction_days=60)
        
        # Cargar y preparar datos
        print("\nCargando datos históricos...")
        predictor.cargar_datos()
        
        print("\nPreparando datos para entrenamiento...")
        x_train, y_train = predictor.preparar_datos()
        
        # Crear y entrenar modelo
        print("\nCreando modelo...")
        predictor.crear_modelo(units=100, dropout_rate=0.2)
        
        print("\nIniciando entrenamiento...")
        predictor.entrenar_modelo(
            x_train, 
            y_train, 
            epochs=20,
            batch_size=32,
            validation_split=0.1
        )
        
        # Guardar el modelo entrenado
        predictor.guardar_modelo('/content/modelo_forex_entrenado.h5')
        
        # Realizar predicciones
        actual_prices, predicted_prices = predictor.predecir_precios()
        
        # Visualizar resultados
        predictor.visualizar_predicciones(actual_prices, predicted_prices)
        
        # Calcular rentabilidad
        rentabilidad, señales = predictor.calcular_rentabilidad(actual_prices, predicted_prices)
        print(f"\nRentabilidad total: {(rentabilidad-1)*100:.2f}%")
        
        # Predecir próximos días
        future_predictions = predictor.predecir_futuros_dias(10)
        print("\nPredicciones para los próximos 10 días:")
        for i, pred in enumerate(future_predictions, 1):
            print(f"Día {i}: {pred:.4f}")
            
        # Visualizar predicciones completas
        visualizar_predicciones_completas(predictor, actual_prices, 
                                        predicted_prices, future_predictions)
        
    except Exception as e:
        print(f"Error en la ejecución: {str(e)}")
        import traceback
        print(traceback.format_exc())

if __name__ == "__main__":
    main()