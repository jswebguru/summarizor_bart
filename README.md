# SummerTime - A summarization library

A library to help users choose appropriate summarization tools based on their specific tasks or needs. Includes models, evaluation metrics, and datasets.

Check out our midway showcase notebook on Colab to give SummerTime a try.        [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Yale-LILY/SummerTime/blob/murori/midway-notebook/SummerTime_midway_showcase.ipynb)


NOTE: Although, most of the library functionality is up and running, there are some features that are still in progress and will soon be added. We are updating the library weekly, please bear with us as we finalize the library. Any helpful comments are highly encouraged, please feel free to reach out to any of our team members.


## Installation and setup

#### Create and activate a new `conda` environment:
```bash
!conda create -n summertime python=3.7
!conda activate summertime
```

#### `pip` dependencies for local demo:
```bash
!pip install -r requirements.txt
```
##### Setup `ROUGE`
```bash
!export ROUGE_HOME=/usr/local/lib/python3.7/dist-packages/summ_eval/ROUGE-1.5.5/
!pip install -U  git+https://github.com/bheinzerling/pyrouge.git
```



## Quick Start
Imports model, initializes default model, and summarizes sample documents.
```python
import model as st_model

model = st_model.summarizer()
documents = [
    """ PG&E stated it scheduled the blackouts in response to forecasts for high winds amid dry conditions. 
    The aim is to reduce the risk of wildfires. Nearly 800 thousand customers were scheduled to be affected 
    by the shutoffs which were expected to last through at least midday tomorrow."""
]
model.summarize(documents)

# ["California's largest electricity provider has turned off power to hundreds of thousands of customers."]
```

Also, please run our colab notebook for a more hands-on demo and more examples. 

 [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Yale-LILY/SummerTime/blob/murori/midway-notebook/SummerTime_midway_showcase.ipynb)



## Models

### Supported Models
SummerTime supports different models (e.g., TextRank, BART, Longformer) as well as model wrappers for more complex summariztion tasks (e.g., JointModel for multi-doc summarzation, BM25 retrieval for query-based summarization).

| Models                    | Single-doc           | Multi-doc            | Dialogue-based       | Query-based          |
| ---------                 | :------------------: | :------------------: | :------------------: | :------------------: | 
| BartModel                 | :heavy_check_mark:   |                      |                      |                      |   
| BM25SummModel             |                      |                      |                      | :heavy_check_mark:   | 
| HMNetModel                |                      |                      | :heavy_check_mark:   |                      |
| LexRankModel              | :heavy_check_mark:   |                      |                      |                      |
| LongformerModel           | :heavy_check_mark:   |                      |                      |                      |
| MultiDocJointModel        |                      | :heavy_check_mark:   |                      |                      |
| MultiDocSeparateModel     |                      | :heavy_check_mark:   |                      |                      |
| PegasusModel              | :heavy_check_mark:   |                      |                      |                      |
| TextRankModel             | :heavy_check_mark:   |                      |                      |                      |
| TFIDFSummModel            |                      |                      |                      | :heavy_check_mark:   |                   |

To see all supported models, run:

```python
from model import SUPPORTED_SUMM_MODELS
print(SUPPORTED_SUMM_MODELS)
```


### Import and initialization:
```python
import model as st_model

# To use a default model
default_model = st_model.summarizer()    

# Or a specific model
bart_model = st_model.BartModel()
pegasus_model = st_model.PegasusModel()
lexrank_model = st_model.LexRankModel()
textrank_model = st_model.TextRankModel()
```

Users can easily access documentation to assist with model selection
```python
sample_model.show_capability()
pegasus_model.show_capability()
textrank_model.show_capability()
```

To use a model for summarization, simply run:
```python
documents = [
    """ PG&E stated it scheduled the blackouts in response to forecasts for high winds amid dry conditions. 
    The aim is to reduce the risk of wildfires. Nearly 800 thousand customers were scheduled to be affected 
    by the shutoffs which were expected to last through at least midday tomorrow."""
]

sample_model.summarize(documents)
# or 
pegasus_model.summarize(documents)
```

All models can be initialized with the following optional options:
```python
def __init__(self,
         trained_domain: str=None,
         max_input_length: int=None,
         max_output_length: int=None,
         ):
```

All models will implement the following methods:
```python
def summarize(self,
  corpus: Union[List[str], List[List[str]]],
  queries: List[str]=None) -> List[str]:

def show_capability(cls) -> None:
```



## Datasets

### Datasets supported
SummerTime supports different summarization datasets across different domains (e.g., CNNDM dataset - news article corpus, Samsum - dialogue corpus, QM-Sum - query-based dialogue corpus, MultiNews - multi-document corpus, ML-sum - multi-lingual corpus, PubMedQa - Medical domain, Arxiv - Science papers domain, among others.

| Datasets         | Single doc         | Multi doc          |  Dialogue-based    |  Query-based       |  Multi-lingual     | News articles      | Scientific papers  | Medical papers  | TV transcripts     | Meetings domain    |
| ---------------- | :----------------: | :----------------: | :----------------: | :----------------: | :----------------: | :----------------: | :----------------: | :----------------: | :----------------: | :----------------: |
| ArxivDataset     | :heavy_check_mark: |                    |                    |                    |                    |                    | :heavy_check_mark: |                     |                    |                    |
| CnndmDataset     | :heavy_check_mark: |                    |                    |                    |                    | :heavy_check_mark: |                    |                     |                    |                    |
| MlsumDataset     | :heavy_check_mark: |                    |                    |                    | German, Spanish, French, Russian, Turkish                    | :heavy_check_mark: |                    |                    |                    |                    |
| MultinewsDataset |                    | :heavy_check_mark: |                    |                    |                    | :heavy_check_mark: |                    |                     |                    |                    |
| PubmedqaDataset  | :heavy_check_mark: |                    |                    | :heavy_check_mark: |                    |                    |                    | :heavy_check_mark: |                    |                    |
| QMsumDataset     | :heavy_check_mark: |                    | :heavy_check_mark: | :heavy_check_mark: |                    |                    |                    |                     |                    | :heavy_check_mark: |
| SamsumDataset    | :heavy_check_mark: |                    | :heavy_check_mark: |                    |                    |                    |                    |                     |                    |                    |
| ScisummnetDataset| :heavy_check_mark: |                    |                    |                    |                    |                    | :heavy_check_mark: |                     |                    |                    |
| SummscreenDataset| :heavy_check_mark: |                    | :heavy_check_mark: |                    |                    |                    |                    |                     | :heavy_check_mark: |                    |
| XsumDataset      | :heavy_check_mark: |                    |                    |                    |                    | :heavy_check_mark: |                    |                     |                    |                    |

To see all supported datasets, run:

```python
from dataset import SUPPORTED_SUMM_DATASETS
print(SUPPORTED_SUMM_DATASETS)
``` 


### Import and initialization:
```python
import dataset
```


### Dataset Initialization
```python
import dataset

cnn_dataset = dataset.CnndmDataset()
# or 
xsum_dataset = dataset.XsumDataset()
# ..etc
```

##### Dataset Object
All datasets are implementations of the `SummDataset` class. Their data splits can be accessed as follows:
```python
dataset = dataset.CnndmDataset()

train_data = dataset.train_set  
dev_data = dataset.dev_set  
test_data = dataset.test_set        
```
Users will be able to see the details of the datasets including size, domain, recommended models, LICENSE, etc. by:
```python
dataset = dataset.CnndmDataset()

dataset.show_description()
```

##### Data instance
The data in all datasets is contained in a `SummInstance` class object, which has the following properties:
```python
data_instance.source = source    # either `List[str]` or `str`, depending on the dataset itself, string joining may needed to fit into specific models.
data_instance.summary = summary  # a string summary that serves as ground truth
data_instance.query = query      # Optional, applies when a string query is present

print(data_instance)             # to print the data instance in its entirety
```

### Loading and using data instances
Data is loaded using a generator to save on space and time

#### To get a single instance
```python
data_instance = next(cnn_dataset.train_set)
print(data_instance)
```

#### To get a slice of the dataset
```python
import itertools

# Get a slice from the train set generator - first 5 instances
train_set = itertools.islice(cnn_dataset.train_set, 5)

corpus = [instance.source for instance in train_set]
print(corpus)
```


## Using the datasets with the models - Examples
```python
import itertools
import dataset
import model

cnn_dataset = dataset.CnndmDataset()


# Get a slice of the train set - first 5 instances
train_set = itertools.islice(cnn_dataset.train_set, 5)

corpus = [instance.source for instance in train_set]


# Example 1 - traditional non-neural model
# LexRank model
lexrank = model.LexRankModel(corpus)
print(lexrank.show_capability())

lexrank_summary = lexrank.summarize(corpus)
print(lexrank_summary)


# Example 2 - A spaCy pipeline for TextRank (another non-neueral extractive summarization model)
# TextRank model
textrank = model.TextRankModel()
print(textrank.show_capability())

textrank_summary = textrank.summarize(corpus)
print(textrank_summary)


# Example 3 - A neural model to handle large texts
# LongFormer Model
longformer = model.LongFormerModel()
longformer.show_capability()

longformer_summary = longformer.summarize(corpus)
print(longformer_summary)
```



## Evaluation
SummerTime supports different evaluation metrics including: BertScore, Bleu, Meteor, Rouge, RougeWe

To print all supported metrics:
```python
from evaluation import SUPPORTED_EVALUATION_METRICS

pprint(SUPPORTED_EVALUATION_METRICS)
```

### Import and initialization:
```python
import evaluation as st_eval

bert_eval = st_eval.bertscore()
bleu_eval = st_eval.bleu_eval()
meteor_eval = st_eval.bleu_eval()
rouge_eval = st_eval.rouge()
rougewe_eval = st_eval.rougewe()
```

### Evaluation Class
All evaluation metrics can be initialized with the following optional arguments:
```python
def __init__(self, metric_name):
```

All evaluation metric objects implement the following methods:
```python
def evaluate(self, model, data):

def get_dict(self, keys):
```

### Using evaluation metrics
Get sample summary data
```python
from evaluation.base_metric import SummMetric
from evaluation import Rouge, RougeWe, BertScore

import itertools

# Initializes a bertscore metric object
metric = BertScore()

# Evaluates model on subset of cnn_dailymail
# Get a slice of the train set - first 5 instances
train_set = itertools.islice(cnn_dataset.train_set, 5)

corpus = [instance for instance in train_set]
pprint(corpus)

articles = [instance.source for instance in corpus]

summaries = sample_model.summarize(articles)
targets = [instance.summary for instance in corpus]
```

Evaluate the data on different metrics
```python
from evaluation import  BertScore, Rouge, RougeWe,

# Calculate BertScore
metric = BertScore()
metric.evaluate(summaries, targets)

# Calculate Rouge
metric = Rouge()
metric.evaluate(summaries, targets)

# Calculate RougeWe
metric = RougeWe()
metric.evaluate(summaries, targets)
```




## Contributors
This repository is built by the [LILY Lab](https://yale-lily.github.io/) at Yale University, led by Prof. [Dragomir Radev](https://cpsc.yale.edu/people/dragomir-radev). The main contributors are [Ansong Ni](https://niansong1996.github.io), Zhangir Azerbayev, Troy Feng, Murori Mutuma and Yusen Zhang (Penn State). For comments and question, please open an issue.
