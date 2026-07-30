# YOLOv8 无人机航拍树木与石头检测

这是一个面向初学者的 Python 项目，用随仓库提供的三个 YOLO 数据集训练自定义 YOLOv8 模型，并检测航拍图片中的：

- `tree`：树木、树冠和树干
- `stone`：石头、岩块

项目目前专注于静态图片，后续可以复用模型接入无人机摄像头或 RTSP 视频流。

## 下载后即可使用的数据

仓库的 `database` 文件夹已经包含三套原始数据：

```text
database/
├── Nature objects.v1i.yolov8/
├── open-pit-rock-chunks-test.v3i.yolov8/
└── Tree-Top-View.v1i.yolov8/
```

配置全部使用相对路径。其他人从 GitHub 下载项目 ZIP 并解压后，不需要另外下载或修改数据集路径，只需按照[中文使用手册](使用手册.md)配置环境，然后运行数据准备、训练和预测命令。

## 主要程序

- `check_environment.py`：检查 Conda、Python、PyTorch、Ultralytics 和 CUDA。
- `prepare_dataset.py`：合并并统一 `database` 中的三套数据，不修改原始文件。
- `train.py`：使用 `yolov8n.pt` 迁移学习。
- `predict_image.py`：检测一张图片或一个图片目录，保存标注图片和 JSON/CSV 结果。

## 最短使用流程

以下命令都在 Windows CMD 中运行。先进入解压后的项目目录：

```bat
conda activate yolov8
cd /d "项目解压目录"
python check_environment.py
python prepare_dataset.py --config config\project.yaml
python train.py --config config\project.yaml
```

训练完成后，把图片路径换成自己的实际文件：

```bat
python predict_image.py --model "runs\detect\uav_tree_stone\weights\best.pt" --source "%USERPROFILE%\Pictures\example.jpg"
```

如果训练输出目录带有数字后缀，请使用命令行实际显示目录中的 `best.pt`。

## 重要说明

- 原始数据保存在 `database`，数据准备结果保存在被 Git 忽略的 `generated`。
- `generated`、`runs`、`outputs` 和模型权重不会提交到 GitHub。
- 第一版类别固定为 `tree` 和 `stone`。
- 基准环境为 Windows、Python 3.8、PyTorch 1.13.1+cu116；使用支持 CUDA 的 NVIDIA GTX 10 系或更新显卡。
- Ultralytics 从官方 GitHub 源码安装，项目不限定某个具体显卡型号。
- 三套数据来自 Roboflow，原始说明文件标明 CC BY 4.0 许可。

完整安装、训练、预测和故障处理步骤请阅读[使用手册](使用手册.md)。
