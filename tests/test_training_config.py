"""训练参数构造的无模型测试。"""

import argparse
import tempfile
import unittest
from pathlib import Path

from train import build_training_arguments


class TrainingArgumentsTests(unittest.TestCase):
    def test_cli_overrides_defaults(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            config = {
                "_project_root": root,
                "project": {"prepared_dataset": str(root / "prepared")},
                "training": {
                    "model": "yolov8n.pt",
                    "epochs": 100,
                    "imgsz": 640,
                    "batch": 8,
                    "device": "0",
                    "workers": 0,
                    "seed": 42,
                    "patience": 30,
                    "project": "runs/detect",
                    "name": "uav_tree_stone",
                },
            }
            args = argparse.Namespace(
                model=None,
                epochs=5,
                imgsz=None,
                batch=2,
                device="cpu",
                workers=None,
            )
            result = build_training_arguments(config, args)
            self.assertEqual(result["epochs"], 5)
            self.assertEqual(result["batch"], 2)
            self.assertEqual(result["device"], "cpu")
            self.assertEqual(result["data"], str(root / "prepared" / "data.yaml"))
            self.assertTrue(result["val"])


if __name__ == "__main__":
    unittest.main()
