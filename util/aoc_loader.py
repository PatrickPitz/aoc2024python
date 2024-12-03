import os
import json
import requests

class AocLoader:
    def __init__(self, day: int):
        current_dir = os.path.dirname(__file__)
        config_file_path = os.path.join(current_dir, '..', 'config', 'config.json')
        config_file_path = os.path.abspath(config_file_path)
        self.config = self.load_config(config_file_path)
        self.year = str(self.config['year'])
        self.day = str(day)
        self.cookie = self.config['cookie']
        self.link = f'https://adventofcode.com/{self.year}/day/{self.day}/input'


    def load_config(self, config_file: str):
        try:
            with open(config_file, 'r') as file:
                config = json.load(file)
            return config
        except Exception as e:
            print(f"Error loading config file: {e}")
            return {}

    def load_data(self):
        filename = 'day' + self.day + '.txt' if int(self.day) >= 10 else 'day0' + self.day + '.txt'
        current_dir = os.path.dirname(__file__)
        input_file_path = os.path.join(current_dir, '..', 'input', filename)
        input_file_path = os.path.abspath(input_file_path)
        if os.path.exists(input_file_path):
            with open(input_file_path, "r") as file:
                print("load static")
                return file.read()
        else:
            return self.download()

    def download(self):
        print("Downloading file...")
        headers = {
            'Cookie': 'session=' + self.cookie,
        }
        response = requests.get(self.link, headers=headers)
        if response.status_code == 200:
            filename = './input/day' + self.day + '.txt' if int(self.day) >= 10 else './input/day0' + self.day  + '.txt'
            with open(filename, "w") as file:
                file.write(response.text)
            print("File downloaded successfully.")
        else:
            print(f"Failed to download file. Status code: {response.status_code}")
        return response.text