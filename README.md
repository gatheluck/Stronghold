# Stronghold

## Train

Example code:
```
cd apps
python train.py dataset=cifar10
```

if you want to check logs, please run the following code.

```
cd logs/train/[OUTPUT_DIR]
mlflow ui 
```

Hyperparam samples:
| dataset | batch size | ep  | optim | lr | mom | decay | schduler | step | gamma | ref
---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ----
| CIFAR-10 | 32 | 200 | SGD | 0.1 | 0.9 | 0.0001 | multistep | 100,150 | 0.1 | https://arxiv.org/abs/1908.08016
| ImageNet | 256 | 90 | SGD | 0.1 | 0.9 | 0.0001 | multistep | 30,60,80 | 0.1 | https://arxiv.org/abs/1908.08016

## Transfer

Example code:
```
cd apps
python transfer.py weight=[PATH_TO_WEIGHT_OR_CHEKPOINT] original_num_classes=22 
```

Hyperparam samples:
| source | target | batch size | ep  | optim | lr | mom | decay | schduler | step | gamma | ref
---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ----
| ImagNet | CIFAR | 128  | 50 | SGD | 0.01 | 0.9 | 0.0001 | step | 30 | 0.1 | https://openreview.net/pdf?id=ryebG04YvB

## Test

Example code:
```
cd apps
python test.py ckpt_path=[PATH_TO_CHEKPOINT]
```
By default, .ckpt file is saved under `logs/train/yyyy-mm-dd_tt-mm-ss/checkpoint/epoch=XX-val_loss_avg=X.XX.ckpt`.

## Fourier Heat Map

Example code:
```
cd apps
python fourier_heatmap.py weight=[PATH_TO_CHECKPOINT]
```

## Note
### Train
| dataset | model | batch size | ep  |  loss | train acc | val acc | optim | lr | mom | decay | schduler | step | gamma | id
---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| CIFAR-10 | resnet56 | 256 | 90 | 0.4557 | 92.88 | 86.23 | SGD | 0.01 | 0.9 | 0.0001 | multi step | 30,60,80 | 0.1 | 2020-06-26_12-55-57_cifar10
| fbdb_l2_basis-0031_cls-0022 | resnet50 | 256 | 90  | 0.1136  | 97.31 | 96.39 | SGD | 0.01 | 0.9 | 0.0001 | multi step | 30,60,80 | 0.1 | 2020-06-25_16-03-46_fbdb_l2_basis-0031_cls-0022
| fbdb_l2_basis-0031_cls-0022 | resnet56 | 256 | 90  | 0.04835  | 99.32 | 98.79  | SGD | 0.01 | 0.9 | 0.0001 | multi step | 30,60,80 | 0.1 | 2020-06-25_17-56-30_fbdb_l2_basis-0031_cls-0022

### Transfer
#### from fbdb_l2_basis-0031_cls-0022
| source | target  | model | batch size | ep  | loss | train acc | val acc | optim | lr | mom | decay | schduler | step | gamma | unfreeze | id
---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- 
| fbdb_l2_basis-0031_cls-0022 | CIFAR-10  | resnet50 | 256 | 50 | 2.180 | 18.74 | 19.35 | SGD | 0.01 | 0.9 | 0.0001 | step | 30 | 0.1 | level_0 | 2020-06-25_16-57-11_fbdb_l2_basis-0031_cls-0022_cifar10
| fbdb_l2_basis-0031_cls-0022 | CIFAR-10  | resnet50 | 256 | 90 | 2.138 | 20.60 | 21.18 | SGD | 0.01 | 0.9 | 0.0001 | multistep | 30,60,80 | 0.1 | level_0 | 2020-06-25_17-22-20_fbdb_l2_basis-0031_cls-0022_cifar10
| fbdb_l2_basis-0031_cls-0022 | CIFAR-10  | resnet56 | 256 | 90 | 2.155 | 19.50 | 20.70 | SGD | 0.01 | 0.9 | 0.0001 | multistep | 30,60,80 | 0.1 | level_0 | 2020-06-25_18-33-57_fbdb_l2_basis-0031_cls-0022_cifar10
| fbdb_l2_basis-0031_cls-0022 | CIFAR-10  | resnet56 | 256 | 90 | 1.294 | 53.78 | 57.70 | SGD | 0.01 | 0.9 | 0.0001 | multistep | 30,60,80 | 0.1 | level_1 | 2020-06-26_21-54-37_fbdb_l2_basis-0031_cls-0022_cifar10
| fbdb_l2_basis-0031_cls-0022 | CIFAR-10  | resnet56 | 256 | 90 | 0.9137 | 67.94  | 67.89 | SGD | 0.01 | 0.9 | 0.0001 | multistep | 30,60,80 | 0.1 | level_2 | 2020-06-27_01-05-44_fbdb_l2_basis-0031_cls-0022_cifar10
| fbdb_l2_basis-0031_cls-0022 | CIFAR-10  | resnet56 | 256 | 90 | 0.6508 | 80.26 | 77.75 | SGD | 0.01 | 0.9 | 0.0001 | multistep | 30,60,80 | 0.1 | level_3 | 2020-06-27_03-06-11_fbdb_l2_basis-0031_cls-0022_cifar10 


#### from fbdb_full_basis-0031_cls-0961

### Fourier Heat map
| dataset | model | eps | source train | target train | unfreeze  | heatmap | samples | id
---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ----
| cifar10 | resnet56 | 16(l2) | cifar10 | - | -  | <img src="samples/fourier_heatmap/2020-06-26_12-55-57_cifar10_fhmap.png" height="100px"> | <img src="samples/fourier_heatmap/2020-06-26_12-55-57_cifar10_example_images.png" height="100px"> | 2020-06-26_12-55-57_cifar10
| fbdb_l2_basis-0031_cls-0022 | resnet56 | 16(l2) | fbdb_l2_basis-0031_cls-0022 | - | -  | <img src="samples/fourier_heatmap/2020-06-25_17-56-30_fbdb_l2_basis-0031_cls-0022_fhmap.png" height="100px"> | <img src="samples/fourier_heatmap/2020-06-25_17-56-30_fbdb_l2_basis-0031_cls-0022_example_images.png" height="100px"> | 2020-06-25_17-56-30_fbdb_l2_basis-0031_cls-0022
| cifar10 | resnet56 | 16(l2) | fbdb_l2_basis-0031_cls-0022 | cifar10 | level1 | <img src="samples/fourier_heatmap/2020-06-27_00-36-24_fbdb_l2_basis-0031_cls-0022_cifar10_fhmap.png" height="100px"> | <img src="samples/fourier_heatmap/2020-06-27_00-36-24_fbdb_l2_basis-0031_cls-0022_cifar10_example_images.png" height="100px"> | 2020-06-27_00-36-24_fbdb_l2_basis-0031_cls-0022_cifar10
| cifar10 | resnet56 | 16(l2) | fbdb_l2_basis-0031_cls-0022 | cifar10 | level2 | <img src="samples/fourier_heatmap/2020-06-27_02-28-43_fbdb_l2_basis-0031_cls-0022_cifar10_fhmap.png" height="100px"> | <img src="samples/fourier_heatmap/2020-06-27_02-28-43_fbdb_l2_basis-0031_cls-0022_cifar10_example_images.png" height="100px"> | 2020-06-27_02-28-43_fbdb_l2_basis-0031_cls-0022_cifar10
| cifar10 | resnet56 | 16(l2) | fbdb_l2_basis-0031_cls-0022 | cifar10 | level3 | <img src="samples/fourier_heatmap/2020-06-27_04-01-57_fbdb_l2_basis-0031_cls-0022_cifar10_fhmap.png" height="100px"> | <img src="samples/fourier_heatmap/2020-06-27_04-01-57_fbdb_l2_basis-0031_cls-0022_cifar10_example_images.png" height="100px"> | 2020-06-27_04-01-57_fbdb_l2_basis-0031_cls-0022_cifar10

### Named Params
| model | keys |
---- | ----
| resnet50 | 'conv1.weight', 'bn1.weight', 'bn1.bias', 'layer1.0.conv1.weight', 'layer1.0.bn1.weight', 'layer1.0.bn1.bias', 'layer1.0.conv2.weight', 'layer1.0.bn2.weight', 'layer1.0.bn2.bias', 'layer1.0.conv3.weight', 'layer1.0.bn3.weight', 'layer1.0.bn3.bias', 'layer1.0.downsample.0.weight', 'layer1.0.downsample.1.weight', 'layer1.0.downsample.1.bias', 'layer1.1.conv1.weight', 'layer1.1.bn1.weight', 'layer1.1.bn1.bias', 'layer1.1.conv2.weight', 'layer1.1.bn2.weight', 'layer1.1.bn2.bias', 'layer1.1.conv3.weight', 'layer1.1.bn3.weight', 'layer1.1.bn3.bias', 'layer1.2.conv1.weight', 'layer1.2.bn1.weight', 'layer1.2.bn1.bias', 'layer1.2.conv2.weight', 'layer1.2.bn2.weight', 'layer1.2.bn2.bias', 'layer1.2.conv3.weight', 'layer1.2.bn3.weight', 'layer1.2.bn3.bias', 'layer2.0.conv1.weight', 'layer2.0.bn1.weight', 'layer2.0.bn1.bias', 'layer2.0.conv2.weight', 'layer2.0.bn2.weight', 'layer2.0.bn2.bias', 'layer2.0.conv3.weight', 'layer2.0.bn3.weight', 'layer2.0.bn3.bias', 'layer2.0.downsample.0.weight', 'layer2.0.downsample.1.weight', 'layer2.0.downsample.1.bias', 'layer2.1.conv1.weight', 'layer2.1.bn1.weight', 'layer2.1.bn1.bias', 'layer2.1.conv2.weight', 'layer2.1.bn2.weight', 'layer2.1.bn2.bias', 'layer2.1.conv3.weight', 'layer2.1.bn3.weight', 'layer2.1.bn3.bias', 'layer2.2.conv1.weight', 'layer2.2.bn1.weight', 'layer2.2.bn1.bias', 'layer2.2.conv2.weight', 'layer2.2.bn2.weight', 'layer2.2.bn2.bias', 'layer2.2.conv3.weight', 'layer2.2.bn3.weight', 'layer2.2.bn3.bias', 'layer2.3.conv1.weight', 'layer2.3.bn1.weight', 'layer2.3.bn1.bias', 'layer2.3.conv2.weight', 'layer2.3.bn2.weight', 'layer2.3.bn2.bias', 'layer2.3.conv3.weight', 'layer2.3.bn3.weight', 'layer2.3.bn3.bias', 'layer3.0.conv1.weight', 'layer3.0.bn1.weight', 'layer3.0.bn1.bias', 'layer3.0.conv2.weight', 'layer3.0.bn2.weight', 'layer3.0.bn2.bias', 'layer3.0.conv3.weight', 'layer3.0.bn3.weight', 'layer3.0.bn3.bias', 'layer3.0.downsample.0.weight', 'layer3.0.downsample.1.weight', 'layer3.0.downsample.1.bias', 'layer3.1.conv1.weight', 'layer3.1.bn1.weight', 'layer3.1.bn1.bias', 'layer3.1.conv2.weight', 'layer3.1.bn2.weight', 'layer3.1.bn2.bias', 'layer3.1.conv3.weight', 'layer3.1.bn3.weight', 'layer3.1.bn3.bias', 'layer3.2.conv1.weight', 'layer3.2.bn1.weight', 'layer3.2.bn1.bias', 'layer3.2.conv2.weight', 'layer3.2.bn2.weight', 'layer3.2.bn2.bias', 'layer3.2.conv3.weight', 'layer3.2.bn3.weight', 'layer3.2.bn3.bias', 'layer3.3.conv1.weight', 'layer3.3.bn1.weight', 'layer3.3.bn1.bias', 'layer3.3.conv2.weight', 'layer3.3.bn2.weight', 'layer3.3.bn2.bias', 'layer3.3.conv3.weight', 'layer3.3.bn3.weight', 'layer3.3.bn3.bias', 'layer3.4.conv1.weight', 'layer3.4.bn1.weight', 'layer3.4.bn1.bias', 'layer3.4.conv2.weight', 'layer3.4.bn2.weight', 'layer3.4.bn2.bias', 'layer3.4.conv3.weight', 'layer3.4.bn3.weight', 'layer3.4.bn3.bias', 'layer3.5.conv1.weight', 'layer3.5.bn1.weight', 'layer3.5.bn1.bias', 'layer3.5.conv2.weight', 'layer3.5.bn2.weight', 'layer3.5.bn2.bias', 'layer3.5.conv3.weight', 'layer3.5.bn3.weight', 'layer3.5.bn3.bias', 'layer4.0.conv1.weight', 'layer4.0.bn1.weight', 'layer4.0.bn1.bias', 'layer4.0.conv2.weight', 'layer4.0.bn2.weight', 'layer4.0.bn2.bias', 'layer4.0.conv3.weight', 'layer4.0.bn3.weight', 'layer4.0.bn3.bias', 'layer4.0.downsample.0.weight', 'layer4.0.downsample.1.weight', 'layer4.0.downsample.1.bias', 'layer4.1.conv1.weight', 'layer4.1.bn1.weight', 'layer4.1.bn1.bias', 'layer4.1.conv2.weight', 'layer4.1.bn2.weight', 'layer4.1.bn2.bias', 'layer4.1.conv3.weight', 'layer4.1.bn3.weight', 'layer4.1.bn3.bias', 'layer4.2.conv1.weight', 'layer4.2.bn1.weight', 'layer4.2.bn1.bias', 'layer4.2.conv2.weight', 'layer4.2.bn2.weight', 'layer4.2.bn2.bias', 'layer4.2.conv3.weight', 'layer4.2.bn3.weight', 'layer4.2.bn3.bias', 'fc.weight', 'fc.bias'
| resnet56 | 'conv1.weight', 'bn1.weight', 'bn1.bias', 'layer1.0.conv1.weight', 'layer1.0.bn1.weight', 'layer1.0.bn1.bias', 'layer1.0.conv2.weight', 'layer1.0.bn2.weight', 'layer1.0.bn2.bias', 'layer1.1.conv1.weight', 'layer1.1.bn1.weight', 'layer1.1.bn1.bias', 'layer1.1.conv2.weight', 'layer1.1.bn2.weight', 'layer1.1.bn2.bias', 'layer1.2.conv1.weight', 'layer1.2.bn1.weight', 'layer1.2.bn1.bias', 'layer1.2.conv2.weight', 'layer1.2.bn2.weight', 'layer1.2.bn2.bias', 'layer1.3.conv1.weight', 'layer1.3.bn1.weight', 'layer1.3.bn1.bias', 'layer1.3.conv2.weight', 'layer1.3.bn2.weight', 'layer1.3.bn2.bias', 'layer1.4.conv1.weight', 'layer1.4.bn1.weight', 'layer1.4.bn1.bias', 'layer1.4.conv2.weight', 'layer1.4.bn2.weight', 'layer1.4.bn2.bias', 'layer1.5.conv1.weight', 'layer1.5.bn1.weight', 'layer1.5.bn1.bias', 'layer1.5.conv2.weight', 'layer1.5.bn2.weight', 'layer1.5.bn2.bias', 'layer1.6.conv1.weight', 'layer1.6.bn1.weight', 'layer1.6.bn1.bias', 'layer1.6.conv2.weight', 'layer1.6.bn2.weight', 'layer1.6.bn2.bias', 'layer1.7.conv1.weight', 'layer1.7.bn1.weight', 'layer1.7.bn1.bias', 'layer1.7.conv2.weight', 'layer1.7.bn2.weight', 'layer1.7.bn2.bias', 'layer1.8.conv1.weight', 'layer1.8.bn1.weight', 'layer1.8.bn1.bias', 'layer1.8.conv2.weight', 'layer1.8.bn2.weight', 'layer1.8.bn2.bias', 'layer2.0.conv1.weight', 'layer2.0.bn1.weight', 'layer2.0.bn1.bias', 'layer2.0.conv2.weight', 'layer2.0.bn2.weight', 'layer2.0.bn2.bias', 'layer2.1.conv1.weight', 'layer2.1.bn1.weight', 'layer2.1.bn1.bias', 'layer2.1.conv2.weight', 'layer2.1.bn2.weight', 'layer2.1.bn2.bias', 'layer2.2.conv1.weight', 'layer2.2.bn1.weight', 'layer2.2.bn1.bias', 'layer2.2.conv2.weight', 'layer2.2.bn2.weight', 'layer2.2.bn2.bias', 'layer2.3.conv1.weight', 'layer2.3.bn1.weight', 'layer2.3.bn1.bias', 'layer2.3.conv2.weight', 'layer2.3.bn2.weight', 'layer2.3.bn2.bias', 'layer2.4.conv1.weight', 'layer2.4.bn1.weight', 'layer2.4.bn1.bias', 'layer2.4.conv2.weight', 'layer2.4.bn2.weight', 'layer2.4.bn2.bias', 'layer2.5.conv1.weight', 'layer2.5.bn1.weight', 'layer2.5.bn1.bias', 'layer2.5.conv2.weight', 'layer2.5.bn2.weight', 'layer2.5.bn2.bias', 'layer2.6.conv1.weight', 'layer2.6.bn1.weight', 'layer2.6.bn1.bias', 'layer2.6.conv2.weight', 'layer2.6.bn2.weight', 'layer2.6.bn2.bias', 'layer2.7.conv1.weight', 'layer2.7.bn1.weight', 'layer2.7.bn1.bias', 'layer2.7.conv2.weight', 'layer2.7.bn2.weight', 'layer2.7.bn2.bias', 'layer2.8.conv1.weight', 'layer2.8.bn1.weight', 'layer2.8.bn1.bias', 'layer2.8.conv2.weight', 'layer2.8.bn2.weight', 'layer2.8.bn2.bias', 'layer3.0.conv1.weight', 'layer3.0.bn1.weight', 'layer3.0.bn1.bias', 'layer3.0.conv2.weight', 'layer3.0.bn2.weight', 'layer3.0.bn2.bias', 'layer3.1.conv1.weight', 'layer3.1.bn1.weight', 'layer3.1.bn1.bias', 'layer3.1.conv2.weight', 'layer3.1.bn2.weight', 'layer3.1.bn2.bias', 'layer3.2.conv1.weight', 'layer3.2.bn1.weight', 'layer3.2.bn1.bias', 'layer3.2.conv2.weight', 'layer3.2.bn2.weight', 'layer3.2.bn2.bias', 'layer3.3.conv1.weight', 'layer3.3.bn1.weight', 'layer3.3.bn1.bias', 'layer3.3.conv2.weight', 'layer3.3.bn2.weight', 'layer3.3.bn2.bias', 'layer3.4.conv1.weight', 'layer3.4.bn1.weight', 'layer3.4.bn1.bias', 'layer3.4.conv2.weight', 'layer3.4.bn2.weight', 'layer3.4.bn2.bias', 'layer3.5.conv1.weight', 'layer3.5.bn1.weight', 'layer3.5.bn1.bias', 'layer3.5.conv2.weight', 'layer3.5.bn2.weight', 'layer3.5.bn2.bias', 'layer3.6.conv1.weight', 'layer3.6.bn1.weight', 'layer3.6.bn1.bias', 'layer3.6.conv2.weight', 'layer3.6.bn2.weight', 'layer3.6.bn2.bias', 'layer3.7.conv1.weight', 'layer3.7.bn1.weight', 'layer3.7.bn1.bias', 'layer3.7.conv2.weight', 'layer3.7.bn2.weight', 'layer3.7.bn2.bias', 'layer3.8.conv1.weight', 'layer3.8.bn1.weight', 'layer3.8.bn1.bias', 'layer3.8.conv2.weight', 'layer3.8.bn2.weight', 'layer3.8.bn2.bias', 'linear.weight', 'linear.bias'