# Mask-Guided Attention Network for Occluded Pedestrian Detection

Pedestrian detection framework as detailed in [arXiv report](https://arxiv.org/abs/1910.06160), accepted to ICCV 2019.

## Installation
Our MGAN is based on [mmdetection](https://github.com/open-mmlab/mmdetection). Please check [INSTALL.md](https://github.com/open-mmlab/mmdetection/blob/master/docs/INSTALL.md) for installation instructions.

## Datasets
You can download [CityScapes Datasets](https://www.cityscapes-dataset.com/).Put it in data folder.

## Testing
The following commands will test the model on 1 GPU. The model can be downloaded [here](https://drive.google.com/file/d/1DjY3JCRX0OkKkQocjX2DX7BV4UG29hGS/view?usp=sharing)
```
./tools/dist_test.sh city_cfgs/mgan_50_65.py models/50_65.pth --eval bbox --out result/50_65.pkl
```
## Eval
The following command will evaltate the results on CityPersons
```
python eval/eval_demo.py
```
