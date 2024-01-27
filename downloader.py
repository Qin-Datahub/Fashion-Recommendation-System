import concurrent.futures
import requests
import json
import argparse
import uuid

# Create an argument parser
parser = argparse.ArgumentParser()
parser.add_argument('--input_dir', help='Json file containing image urls')
parser.add_argument('--output_dir', help='Output directory saving downloaded images')
args = parser.parse_args()

# Define a function to download images
def download_image(url):
    response = requests.get(url, verify=False)
    filename = args.output_dir + str(uuid.uuid4()) + ".jpeg" # set a unique name for the image

    with open(filename, 'wb') as file:
        file.write(response.content)
    print(f'Downloaded: {filename}')

if __name__ == "__main__":

    # Open the JSON file
    with open(args.input_dir, 'r') as file:
        data = json.load(file)

    # Get a list of image urls
    image_urls = []
    for i in range(len(data)):
        image_urls.append(data[i]["image_src"])
    
    # Set the maximum number of threads
    max_threads = 100

    # Download images in parallel using multithreading
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
        executor.map(download_image, image_urls)
