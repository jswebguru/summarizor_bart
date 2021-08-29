from dataset.dataset_loaders import (
    CnndmDataset,
    MultinewsDataset,
    SamsumDataset,
    XsumDataset,
    PubmedqaDataset,
    MlsumDataset,
    ScisummnetDataset,
    SummscreenDataset,
    QMsumDataset,
    ArxivDataset,
)


SUPPORTED_SUMM_DATASETS = [
    CnndmDataset,
    MultinewsDataset,
    SamsumDataset,
    XsumDataset,
    PubmedqaDataset,
    MlsumDataset,
    ScisummnetDataset,
    SummscreenDataset,
    QMsumDataset,
    ArxivDataset,
]


def list_all_datasets():
    all_datasets = []
    for ds in SUPPORTED_SUMM_DATASETS:
        all_datasets.append(ds.__name__)

    return all_datasets
