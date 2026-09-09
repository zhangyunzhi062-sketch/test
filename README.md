# Winter.Z 的图像识别 ver1.1

当前代码为 **1.1.0B 威力加强版**：使用 YOLOv8 完成无人机航拍树木与石头检测。

## 版本选择

| Release | 定位 | 默认训练方案 |
| --- | --- | --- |
| **1.1.0A 显卡友好版（Latest）** | 推荐个人电脑 | 保持 1.0.0A：`yolov8n.pt`、100 epochs、640、batch 8、workers 0、patience 30 |
| **1.1.0B 威力加强版** | 推荐超算工作台 | `yolov8x.pt`、1000 epochs、832、自动 batch、workers 48、patience 200 |


这是一个面向初学者的无人机机器学习和图像识别 Python 项目，用随仓库提供的三个 YOLO 数据集训练自定义 YOLOv8 模型，并检测航拍图片中的：

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

使用者从 GitHub 下载项目 ZIP 并解压后，不需要另外下载或修改数据集路径，只需按照[中文使用手册](使用手册.md)配置环境，然后运行数据准备、训练和预测命令。

项目根目录还包含“待检测图片”文件夹。把图片放进去后，预测命令可以同时省略 `--source` 和 `--model`：两版默认模型都是 `runs\detect\uav_tree_stone\weights\best.pt`；识别完成后，程序会自动打开本次结果文件夹。

## 主要程序

- `check_environment.py`：检查 Conda、Python、PyTorch、Ultralytics 和 CUDA。
- `prepare_dataset.py`：合并并统一 `database` 中的三套数据，不修改原始文件。
- `train.py`：当前 1.1.0B 默认使用 `yolov8x.pt`、1000 轮与严格提前收敛设置。
- `predict_image.py`：默认使用原始训练目录的 `best.pt` 检测“待检测图片”，保存结果并自动打开结果目录。

## 最短使用流程

以下命令都在 Windows CMD 中运行：

```bat
conda activate yolov8
cd  "项目解压目录"
python check_environment.py
python prepare_dataset.py --config config\project.yaml
python train.py --config config\project.yaml
```

训练完成后，把图片放进项目根目录的“待检测图片”，然后运行：

```bat
python predict_image.py
```

默认读取 `runs\detect\uav_tree_stone\weights\best.pt`。如果模型在其他目录，用 `--model` 指定；仍可通过 `--source` 临时指定其他图片或文件夹。

## 重要说明

- 原始数据保存在 `database`，数据准备结果保存在被 Git 忽略的 `generated`。
- `generated`、`runs`、`outputs` 和用户训练生成的模型权重不会提交到 GitHub。
- 1.1.0A Release 完整包附带官方 `yolov8n.pt`；1.1.0B 完整包附带官方 `yolov8x.pt`。它们都是初始训练权重，不是用户训练结果。
- 第一版类别固定为 `tree` 和 `stone`。
- 基准环境为 Windows、Python 3.8、PyTorch 1.13.1+cu116；使用支持 CUDA 的 NVIDIA GTX 10 系或更新显卡。
- Ultralytics 从官方 GitHub 源码安装，项目不限定某个具体显卡型号。
- 三套数据来自机器学习开源网站Roboflow，原始说明文件均标明 CC BY 4.0 许可。

完整安装、训练、预测和故障处理步骤请阅读[使用手册](使用手册.md)。
