import os
import re
from PIL import Image
import requests
from time import sleep
import binascii
import io

bing_api_key = os.getenv('BING_API_KEY')
if not bing_api_key:
    raise EnvironmentError('Must provide valid BING_API_KEY, see https://portal.azure.com and ' + \
                           '+New->AI + Cognitive Services->Bing Search APIs')

def get_image_content_uris(search_term, offset=0, count=50, mkt='en-us', safe_search='Moderate'):
    bing_image_uri = 'https://api.cognitive.microsoft.com/bing/v5.0/images/search'
    req = requests.get(bing_image_uri,
                       params={'offset': offset,
                               'count': count,
                               'mkt': mkt,
                               'safeSearch': safe_search,
                               'q': search_term},
                       headers={'Ocp-Apim-Subscription-Key': bing_api_key})
    content_uris = [v['contentUrl'] for v in req.json()['value']]
    return content_uris

def grab_image(image_uri, file_loc):
    req = requests.get(image_uri, stream=True)
    stream = io.BytesIO()
    for chunk in req.iter_content(chunk_size=128):
        stream.write(chunk)
    stream.seek(0)
    img = Image.open(stream)
    #print(img.size)
    img.convert(mode='RGB').save(file_loc)

def grab_images_to_dir(image_uris, dir_loc):
    if not os.path.exists(dir_loc):
        os.makedirs(dir_loc)
    results = []
    for ix, uri in enumerate(image_uris):
        outf = '{}/image_{}.jpg'.format(dir_loc, ix+1)
        try:
            grab_image(uri, outf)
            results.append((uri, outf))
        except Exception as e:
            print('Failed to download "{}": {}'.format(uri, e))
    return results

def search_for_examples(root_loc, search_term, count=100):
    if not os.path.exists(root_loc):
        os.makedirs(root_loc)
    content_uris = get_image_content_uris(search_term, count=count)
    dir_suffix = re.sub(r'\s+', '_', search_term) # TODO: Should escape search_term better here
    imgs_path = root_loc + '/' + dir_suffix
    return grab_images_to_dir(content_uris, imgs_path)

root_dir = 'c:/dev/git_ws/msready2017/images'
with open(root_dir + '/images.tsv', 'w') as img_tsv:
    img_tsv.write('Label\tPath\tURL\n')
    for term in ['hot dog', 'cat', 'dog', 'fish', 'pizza', 'omelet', 'eagle', 'boat']:
        curresults = search_for_examples(root_dir, term)
        for cururi, curpath in curresults:
            img_tsv.write('{}\t{}\t{}\n'.format(term, curpath, cururi))
        print('Downloaded all images for "{}", sleeping.'.format(term))
        sleep(0.1)