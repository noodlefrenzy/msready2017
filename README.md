# Microsoft Ready 2017
## Machine Learning for CSE

This is code and supporting materials for a brief talk given during Microsoft Ready 2017 for the newly-minted CSE division (previously DX). A 20 minute talk is not enough to cover the entirety of ML and Deep Learning, so it was pretty abbreviated. To motivate the differences between Cognitive Services, Deep Learning, and Machine Learning I used demos solving the "Hotdog / Not Hotdog" problem from Silicon Valley.

## Replicating Locally

Create a new Anaconda environment using the `environment.yml` file contained in the repository (see [the conda documentation](https://conda.io/docs/using/envs.html#use-environment-from-file)). Execute `img_downloader.py` and `download_model.py` to download images in some categories (via Bing Image Search) and the ResNet18 model we use for transfer learning. Note that you'll need to set the `BING_API_KEY` environment variable or the image download will fail (well, the search will). Please sign up for the Bing Image Search API at [https://portal.azure.com](https://portal.azure.com).

## Custom Vision Service

## CNTK Transfer Learning

Once you've downloaded the images and model, you need to validate the images and convert them into a training/testing set for CNTK. Run `img_to_cntk.py` to do that work. You should now be able to run the `CNTK Hot Doggin.ipynb` Jupyter Notebook and train a hotdog prediction model.

## Azure ML Classifier

