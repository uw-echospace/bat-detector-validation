# bat-detector-validation

## Description of the Repo
This is a manual data cleaning repo for training the `batdetect2` model.  
`batdetect2` is a machine learning model that can detect bat calls. However, it is currently not very accurate in detecting the calls of the various species of bats living in the Union Bay Natural Area.
Thus, in order to train a model better suited to detecting the calls of bats in Union Bay Natural Area, this repo randomly selected the audiomoth recordings from all the deployed locations in all available months and had someone manually label all the calls of bats in these randomly selected recordings.




Folders:
- [data](https://github.com/smohid26/bat-detector-validation/tree/main/data)
    - [batdetect2](https://github.com/smohid26/bat-detector-validation/tree/main/data/batdetect2)
        - bat calls detected by bat detect software
    - [human](https://github.com/smohid26/bat-detector-validation/tree/main/data/human)
         - bat calls detected by human
- analysis
    - notebooks
    - scripts
