from .base_multi_doc_model import MultiDocSummModel
from summertime.model.base_model import SummModel
from summertime.model.single_doc import TextRankModel
from typing import Union, List


class MultiDocJointModel(MultiDocSummModel):

    model_name = "Multi-document joint"
    is_multi_document = True

    def __init__(self, model_backend: SummModel = TextRankModel, **kwargs):
        model: SummModel = model_backend(**kwargs)
        self.model = model

        super(MultiDocJointModel, self).__init__(
            trained_domain=self.model.trained_domain,
            max_input_length=self.model.max_input_length,
            max_output_length=self.model.max_output_length,
        )

    def summarize(
        self,
        corpus: Union[List[str], List[List[str]]],
        query: Union[List[str], List[List[str]]] = None,
    ) -> List[str]:
        self.assert_summ_input_type(corpus, None)
        joint_corpus = []
        for instance in corpus:
            joint_corpus.append(" ".join(instance))

        summaries = self.model.summarize(joint_corpus)

        return summaries

    @classmethod
    def generate_basic_description(cls) -> str:
        basic_description = (
            "MultiDocJointModel performs multi-document summarization by"
            " first concatenating all documents,"
            " and then performing single-document summarization on the concatenation."
        )
        return basic_description

    @classmethod
    def show_capability(cls):
        basic_description = cls.generate_basic_description()
        more_details = (
            "A multi-document summarization model."
            " Allows for custom model backend selection at initialization."
            " Concatenates each document in corpus and returns single-document summarization of joint corpus.\n"
            "Strengths: \n - Allows for control of backend model.\n"
            "Weaknesses: \n - Assumes all documents are equally weighted.\n"
            " - May fail to extract information from certain documents.\n"
        )
        print(f"{basic_description}\n{'#' * 20}\n{more_details}")
