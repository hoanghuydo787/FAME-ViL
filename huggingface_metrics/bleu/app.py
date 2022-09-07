# Copyright (c) Facebook, Inc. and its affiliates.

import evaluate
from evaluate.utils import launch_gradio_widget


module = evaluate.load("bleu")
launch_gradio_widget(module)
