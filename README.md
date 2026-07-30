# YOLOv8 无人机航拍树木与石头检测

这是一个面向无人机机器学习与图像识别初学者的 Python 项目，用三个现有 YOLO 数据集训练自己的 YOLOv8 模型，并检测航拍图片中的：

- `tree`：树木、树冠和树干
- `stone`：石头、岩块

项目目前专注于静态图片，后续可以复用模型接入无人机摄像头或 RTSP 视频流。

## 主要程序

- `check_environment.py`：检查 Conda、Python、PyTorch、Ultralytics 和 GPU。
- `prepare_dataset.py`：合并并统一数据集。
- `train.py`：使用 `yolov8n.pt` 迁移学习。
- `predict_image.py`：检测一张图片或一个图片目录，保存标注图片和 JSON/CSV 结果。

## 第一次使用

请从完整的[中文使用手册](使用手册.md)开始。最短流程如下：

```bat
conda activate yolov8
cd /d D:\zyzcodex\codex-yolov8
python check_environment.py
python prepare_dataset.py --config config\project.yaml
python train.py --config config\project.yaml
```

训练完成后，将下面命令中的模型和图片路径换成你自己的实际路径：

```bat
python predict_image.py --model "D:\zyzcodex\codex-yolov8\runs\detect\uav_tree_stone\weights\best.pt" --source "D:\待检测图片\example.jpg"
```

## 重要说明

- 不要把数据集、`best.pt` 或 `runs` 目录提交到 GitHub。
- 第一次训练前必须先运行数据准备程序。
- 本项目不会自动修改原始数据集。
- 训练与预测代码以 Python 3.8、PyTorch 1.13.1+cu116、Ultralytics 8.4.112 为基准。
- 原始数据集来自开源网站 Roboflow，均在各自的 `data.yaml` 中标明 CC BY 4.0 来源。
