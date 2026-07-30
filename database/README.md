# 随项目提供的原始数据集

本目录包含项目训练所需的三套原始 YOLO 数据：

- `Nature objects.v1i.yolov8`
- `open-pit-rock-chunks-test.v3i.yolov8`
- `Tree-Top-View.v1i.yolov8`

`config/project.yaml` 使用相对于项目根目录的路径引用这些数据。下载完整项目 ZIP 并解压后，不需要修改数据路径。

请不要直接修改原始数据。运行：

```bat
python prepare_dataset.py --config config\project.yaml
```

程序会在项目根目录的 `generated/uav-tree-stone.v1.yolov8` 中生成统一的 `tree`、`stone` 两类检测数据。

各数据集来源和 CC BY 4.0 许可信息保留在对应目录的 `data.yaml`、`README.dataset.txt` 和 `README.roboflow.txt` 中。
