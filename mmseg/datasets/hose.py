from .builder import DATASETS
from .custom import CustomDataset


@DATASETS.register_module()
class HoseDataset(CustomDataset):
    """Hose dataset.

    In segmentation map annotation for Hose, 0 stands for background, which
    is not included in 150 categories. ``reduce_zero_label`` is fixed to True.
    The ``img_suffix`` is fixed to '.jpg' and ``seg_map_suffix`` is fixed to
    '.png'.
    """
    CLASSES = (
        'hose'
        )

    PALETTE = None

    def __init__(self, **kwargs):
        super(HoseDataset, self).__init__(
            img_suffix='.png',
            seg_map_suffix='.png',
            reduce_zero_label=True,
            **kwargs)
