

from typing import Any, Callable, Dict, List, Optional, Union

import numpy as np

class CorrentropyAffineICP:
    def __init__(self, source: Optional[np.ndarray] = None, tf_init_params: Dict = {}, use_cuda: bool = False) -> None:
        self._tf_init_params = tf_init_params
