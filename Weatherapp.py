import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, 
                             QVBoxLayout, QLabel, QLineEdit)
from PyQt5.QtCore import Qt

class weatherapp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Weather API")
        self.city_label = QLabel("Enter the City : ",self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather",self) 
        self.temp_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.desc_label = QLabel(self)
        self.initUI()

    def initUI(self):
        #self.city_input.setPlaceholderText("eg-kolkata") 
        vbox = QVBoxLayout() #create a vertical layout box
        vbox.addWidget(self.city_label) #adds all the widgets in vbox
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temp_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.desc_label)
        self.setLayout(vbox) #vbox layout

        self.city_label.setAlignment(Qt.AlignCenter) #all alignment are aligned in center
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temp_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.desc_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city_label") #all object name are created
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temp_label.setObjectName("temp_label")
        self.emoji_label.setObjectName("emoji_label")
        self.desc_label.setObjectName("desc_label")

        self.setStyleSheet("""                   #for making it look stylish
                            QPushButton,QLabel{
                           font-family: Arial;
                           }
                           QLabel#city_label{
                           font-size : 40px;
                           font-style : italic;
                           }
                           QLineEdit#city_input{
                           font-size : 40px;
                           }
                           QPushButton#get_weather_button{
                           font-size : 30px;
                           font-weight : bold;
                           background-color : #3498db;
                           color : white;
                           border-radius : 10px;
                           padding : 10px;
                           }
                           QLabel#temp_label{
                           font-size : 75px;
                           font-weight : bold;
                           color : black; 
                           }
                           QLabel#emoji_label{
                           font-size : 120px;
                           font-family : Segoe UI emoji;
                           }
                           QLabel#desc_label{
                           font-size : 80px;
                           }
                            """)
        self.get_weather_button.clicked.connect(self.get_weather) #works when buttom clicked

    def get_weather(self):
        api_key = "YOUR_API_KEY"
        city = self.city_input.text()
        url = f"https://api.openweathermap.org//data//2.5//weather?q={city}&appid={api_key}"
        try:
            responce = requests.get(url) #request for a url
            responce.raise_for_status()
            data = responce.json() #save in data variable in json file
            if data["cod"] == 200:
                self.weather_show(data)
        except requests.exceptions.HTTPError as http_error:
            match responce.status_code:
                case 400:
                    self.error("Bad request:\nPlease check your input")
                case 401:
                    self.error("Unauthorised:\nInvalid API key")   
                case 403:
                    self.error("Forbidden:\nAccess is denied")
                case 404:
                    self.error("Not Found:\nCity not found")
                case 500:
                    self.error("Internal Server Error:\nPlease try again")
                case 502:
                    self.error("Bad Gateway:\nInvalid Response to the Server")
                case 503:
                    self.error("Service Unavailable:\nServer is down")
                case 504:
                    self.error("Gateway Timeout\nNo responce from the server") 
                case _:
                    self.error(f"HTTP Error Occoured {http_error}")  
        except requests.exceptions.ConnectionError:
            self.error("Connection Error:\nPlease check your internet connection")
        except requests.exceptions.TooManyRedirects:
            self.error("Too many redirects:\nPlease check your url")
        except requests.exceptions.Timeout:
            self.error("Timeout Error:\nThe request has timeout")                          
        except requests.exceptions.RequestException as req_error:
            self.error(f"Request Error\n{req_error}")        
    def error(self,massage):
        self.temp_label.setStyleSheet("color : black;"
                                      "font-size : 30px;")
        self.temp_label.setText(massage)
        self.emoji_label.clear() #clears shown data 
        self.desc_label.clear()
    def weather_show(self,data):
        temp_k = data["main"]["temp"]
        self.temp_label.setStyleSheet("font-size : 75px;"
                                      "font-weight : bold;")
        temp_c = temp_k - 273.15
        self.temp_label.setText(f"{temp_c:.0f} °C")
        #temp_f = ((temp_k - 273.15) * (9/5)) + 32
        #self.temp_label.setText(f"{temp_f:.0f} °F")
        #print(data)

        weather_id = data["weather"][0]["id"]
        self.emoji_label.setText(self.emoji_show(weather_id))
        

        desc = data["weather"][0]["description"]
        self.desc_label.setText(desc)
    @staticmethod    
    def emoji_show(weather_id):
        if  200 <= weather_id <= 232:
            return "⛈️"
        elif 300 <= weather_id <= 321:
            return "🌤️"
        elif 500 <= weather_id <= 531:
            return "☔"
        elif 600 <= weather_id <= 622:
            return "❄️"
        elif weather_id == 800:
            return "☀️"
        elif 801 <= weather_id <=804:
            return "☁️"
        elif weather_id == 701:
            return "🌫️"
        elif weather_id == 711:
            return "💨"
        elif weather_id == 721:
            return "🌁"
        elif weather_id == 731:
            return "💨"
        elif weather_id == 741:
            return "🌫️"
        elif weather_id == 751:
            return "💨"
        elif weather_id == 761:
            return "💨"
        elif weather_id == 762:
            return "🌋"
        elif weather_id == 771:
            return "💨"
        elif weather_id == 781:
            return "🌪️"
                  
def main():
    app = QApplication(sys.argv)
    Weatherapp = weatherapp()
    Weatherapp.show()
    sys.exit(app.exec())    

if __name__ == "__main__":
    main()        
