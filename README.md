# Mask-Guided Attention Network for Occluded Pedestrian Detection

Pedestrian detection framework as detailed in [arXiv report](https://arxiv.org/abs/1910.06160), accepted to ICCV 2019.

## Installation
Our MGAN is based on [mmdetection](https://github.com/open-mmlab/mmdetection). Please check [INSTALL.md](https://github.com/open-mmlab/mmdetection/blob/master/docs/INSTALL.md) for installation instructions.

## Datasets
You can download [CityScapes Datasets](https://www.cityscapes-dataset.com/).Put it in data folder.

## Testing
The following commands will test the model on 1 GPU.
```
python tools/test.py city_cfgs/mgan_50_65.py models/50_65.pth --out result/50_65.pkl
```
## Eval
The following command will evaltate the results on CityPersons
```
python eval/eval_demo.py
```

## Results
| R       | HO     |                                                             Download                                                              |
|:----:  | :----: | :-------------------------------------------------------------------------------------------------------------------------------: |
| 11.0    |   50.3 | [Google Drive](https://drive.google.com/file/d/1gww2UZDLlE76JFA80LoR37OTHxokhaii/view?usp=sharing)/ [Baidu Yun](https://pan.baidu.com/s/1q68cjZZyH4lqNjy9nv588Q)(zq93) |