import io

from google.cloud import vision_api
from google.cloud.vision_api import types

def detect_text(image_file):
    """Detects text in an image file."""
    client = vision_api.ImageAnnotatorClient()

    with io.open(image_file, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations

    for text in texts:
        print('\n"{}"'.format(text.description))
        for vertex in text.bounding_poly.vertices:
            print('bounds: {}'.format(vertex))

