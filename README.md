# 2021_AI_Seminar

## Prerequisites
- If you don't have Anaconda, enter them in the terminal.
```bash
$ wget https://repo.anaconda.com/archive/Anaconda3-2021.05-Linux-x86_64.sh
$ sh Anaconda3-2021.05-Linux-x86_64.sh
```
```bash
$ git clone https://github.com/JungmoKoo/2021_AI_Seminar
$ cd 2021_AI_Seminar
$ conda env create -f env.yml
$ conda activate aiseminar
$ pip install pycocotools opencv_python
```

## If you don't have PyCharm.
```bash
$ wget https://download.jetbrains.com/python/pycharm-community-2021.1.2.tar.gz
$ tar -xvf pycharm-community-2021.1.2.tar.gz
$ sh pycharm-community-2021.1.2/bin/pycharm.sh
```

## If you want to change your GPU, put the code below inside the python code.
- {GPU_NUMBER}: change this parameter
```python
os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"] = "{GPU_NUMBER}"
```