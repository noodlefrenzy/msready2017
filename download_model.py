import os
try:
    from urllib.request import urlretrieve 
except ImportError: 
    from urllib import urlretrieve
   
def download_model(model_file_name, model_url):
    model_dir = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(model_dir, model_file_name)
    if not os.path.exists(filename):
        print('Downloading model from ' + model_url + ', may take a while...')
        urlretrieve(model_url, filename)
        print('Saved model as ' + filename)
    else:
        print('CNTK model already available at ' + filename)

def download_model_by_name(model_name):
    if not model_name.endswith('.model'):
        model_name = model_name + '.model'

    modelNameToUrl = {
        'AlexNet.model':   'https://www.cntk.ai/Models/AlexNet/AlexNet.model',
        'AlexNetBS.model': 'https://www.cntk.ai/Models/AlexNet/AlexNetBS.model',
        'ResNet_18.model': 'https://www.cntk.ai/Models/ResNet/ResNet_18.model',
        'Fast-RCNN_grocery100.model' : 'https://www.cntk.ai/Models/FRCN_Grocery/Fast-RCNN_grocery100.model'
    }

    if not model_name in modelNameToUrl:
        print("ERROR: Unknown model name '%s'." % model_name)
    else:
        download_model(model_name, modelNameToUrl[model_name])

download_model_by_name('ResNet_18.model')