# sa salvam niste imagini cu niste caini intr-un pdf
import json
import os
import time
from json import JSONDecodeError
import requests
import image_functions as func_images
import pdf_functions as pdf




MENU = """
1. Save Random Image
2. Show All Images
3. Save Images To PDF
4. Delete all images
"""


def read_config(path: str = "config.json") -> dict:
    try:
        with open(path, "r") as f:
            data = f.read()
            conf_dict = json.loads(data)
    except FileNotFoundError as e:
        print(f"The config file is missing... {e}")
    except JSONDecodeError as e:
        print(f"Watch your json... {e}")
    except Exception as e:
        print(f"Unknown exception {e}")

    return conf_dict





if __name__ == '__main__':
    config = read_config()

    while True:
        user_pick = input(MENU)

        match user_pick:
            case "1":
                random_image_dict = func_images.get_dog_image(config['url_dog_images'])
                content = func_images.download_dog_image(random_image_dict['message'])
                func_images.save_dog_image(content)

            case "2":
                func_images.show_all_images()
            case "3":
                pdf.create_pdf("test.pdf")
            case "4":
                pass



