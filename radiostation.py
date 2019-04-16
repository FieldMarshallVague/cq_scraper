from bs4 import BeautifulSoup

# soup = BeautifulSoup(source, 'html.parser')

class RadioStationColumns:
    def __init__(self, station):
        self.call_sign = station['call_sign']
        self.frequency = station['frequency']
        self.city_of_license = station['city_of_license']
        self.licensee = station['licensee']
        self.format = station['format']
        
    def __str__(self):
        return f"""
            call_sign={self.call_sign},
            frequency={self.frequency},
            city_of_license={self.city_of_license},
            licensee={self.licensee},
            format={self.format}"""

class RadioStation:
    def __init__(self, columns):
        self.call_sign_raw = columns['call_sign']
        self.frequency = columns['frequency']
        self.city_of_license = columns['city_of_license']
        self.licensee = columns['licensee']
        self.format = columns['format']
        
    def __str__(self):
        return f"""
            call_sign={self.call_sign},
            frequency={self.frequency},
            city_of_license={self.city_of_license},
            licensee={self.licensee},
            format={self.format}"""
