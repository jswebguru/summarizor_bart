from .base_metric import SummMetric
from summ_eval.metric import Metric as SEMetric
from typing import List, Dict


class SummEvalMetric(SummMetric):
    """
    Generic class for a summarization metric whose backend is SummEval.
    """

    def __init__(self, se_metric: SEMetric):
        self.se_metric = se_metric

    def evaluate(
        self, inputs: List[str], targets: List[str], keys: List[str]
    ) -> Dict[str, float]:
        score_dict = self.se_metric.evaluate_batch(inputs, targets)
        return {key: score_dict[key] if key in score_dict else None for key in keys}
