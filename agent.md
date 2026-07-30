# 项目概述

本项目使用 Python 3.8、Ultralytics YOLOv8 和 PyTorch，在无人机航拍图片中检测树木与石头。第一版只处理静态图片；现有数据没有可靠的“森林”标签，因此不虚构森林类别。后续获得相应标注后，可增加森林识别，并扩展到摄像头或 RTSP 实时视频流。

# 项目目标

- 将三个 YOLO 数据集安全合并为 `tree`、`stone` 两类，且不修改原始数据。
- 使用 `yolov8n.pt` 迁移学习，生成可用于航拍图片检测的自定义权重。
- 提供环境检查、数据准备、训练和图片预测脚本。
- 保存标注图片及 JSON、CSV 检测明细。
- 不将数据集、模型权重和运行结果提交到 GitHub。

# 实施步骤

1. 激活 Conda 环境 `yolov8`，检查 Python、PyTorch、Ultralytics 和 CUDA。
2. 按配置合并数据：`tree/tree-top/trunk → tree`，`rock/stone → stone`，石头多边形转检测框。
3. 校验 train、valid、test 的图片与标签，生成统一 `data.yaml` 和统计清单。
4. 使用 YOLOv8 预训练权重训练并验证模型，保留 `best.pt`。
5. 使用训练后的权重检测指定图片或图片目录，输出可视化图片和结构化结果。
6. 后续补充森林标注；实时功能复用预测层接入摄像头编号或网络流地址。

# 环境与原则

- Conda 环境：`yolov8`
- Python：3.8
- PyTorch：1.13.1+cu116
- Ultralytics：从官方 GitHub 下载源码并使用 `pip install -e .` 安装
- GPU：支持 CUDA 的 NVIDIA GTX 10 系或更新型号
- 原始数据随项目保存在 `database`；派生数据默认写入 `generated/uav-tree-stone.v1.yolov8`
- Windows 训练入口必须放在 `if __name__ == "__main__":` 中
