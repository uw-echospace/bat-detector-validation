# bat-detector-validation

## Description of the Repo
This is a manual data cleaning repo for training the `batdetect2` model.  
`batdetect2` is a machine learning model that can detect bat calls. However, it is currently not very accurate in detecting the calls of the various species of bats living in the Union Bay Natural Area.
Thus, in order to train a model better suited to detecting the calls of bats in Union Bay Natural Area, this repo randomly selected the audiomoth recordings from all the deployed locations in all available months and had someone manually label all the calls of bats in these randomly selected recordings.

## Download the WAV files
Since WAV files are too large, users should download the files to their own computers. The code to download from the OSN to your computer is called download_wav.py and is located under scripts. To use the code, you need to change row 7 and 9 into your own bucket name and the local directory where you want to store the WAV files. 


Folders:
- [data](https://github.com/smohid26/bat-detector-validation/tree/main/data)
    - [batdetect2](https://github.com/smohid26/bat-detector-validation/tree/main/data/batdetect2)
        - bat calls detected by bat detect software
    - [human](https://github.com/smohid26/bat-detector-validation/tree/main/data/human)
         - bat calls detected by human
- analysis
    - notebooks
    - scripts


<img width="891" alt="image" src="https://github.com/uw-echospace/bat-detector-validation/assets/102640018/d036fb64-b626-42fa-9007-36b63f03f9b1">
