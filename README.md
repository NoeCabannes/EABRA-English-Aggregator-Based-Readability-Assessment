# EABRA: English Aggregator-Based Readability Assessment

EABRA is a Python toolkit designed to evaluate the readability of English texts. It is the English counterpart to the French FABRA toolkit. It automatically extracts a wide array of language features (Length, Lexical, Syntactic, and Discourse) from your text and calculates 18 statistical aggregators for each feature, providing an extremely detailed linguistic profile of the input. It resues the language variables and aggregators from FABRA.

## Features extracted

EABRA groups its extractions into the following families:
1. **Length-based Variables**: Sentence length (words per sentence), Word length (letters per word, syllables per word).
2. **Lexical Variables**: Lexical diversity measures including TTR (Type-Token Ratio), MTLD, and LogTTR.
3. **Syntactic Variables**: Parse tree depths, and counts of Universal Dependency relations (e.g., nominal subjects, adjectival modifiers).
4. **Discourse Variables**: Referential expressions (proportion of pronouns and definite articles to nouns).

All sentence-level and word-level features are passed through **18 statistical aggregators** (Sum, Min, Max, Length, Median, Q1, Q3, 80th Percentile, 90th Percentile, Average, Mode, Variance, Standard Deviation, Relative Standard Deviation, Interquartile Range, Dolch Metric, Skewness, and Kurtosis).

---

## 🛠️ Prerequisites & installation

### 1. Python version
**Important:** EABRA utilizes `spaCy` under the hood for advanced NLP tasks. `spaCy` relies on compiled C-extensions. Therefore, it is highly recommended to use **Python 3.11, 3.12, or 3.13**. 
*(Using brand new versions like Python 3.14 may cause installation errors as pre-built wheels might not be available yet).*

### 2. Install dependencies
Open your terminal or command prompt and run the following command to install the required Python libraries:

```bash
pip install spacy pydantic pyphen lexical-diversity textstat pandas scipy numpy "setuptools<70.0.0"
```

### 3. Download the spaCy language model
EABRA requires the English language model for `spaCy`. Download it by running:

```bash
python -m spacy download en_core_web_sm
```

---

## 🚀 How to use EABRA

You can use EABRA to process a single text string or process an entire dataset (Pandas DataFrame) at once.

### Processing a Pandas DataFrame (Recommended)

This is the most efficient way to process multiple texts.

```python
import pandas as pd
import sys
print(sys.executable)
from eabra.pipeline import EABRAPipeline

# 1. Initialize the pipeline
print("Initializing EABRA...")
pipeline = EABRAPipeline()

# 2. Prepare your data in a Pandas DataFrame
data = {
    'text_id': [1, 2],
    'text': [
        "When you think of dinosaurs and where they lived, what do you picture? Do you see hot, steamy swamps, thick jungles, or sunny plains? Dinosaurs lived in those places, yes. But did you know that some dinosaurs lived in the cold and the darkness near the North and South Poles? This surprised scientists, too. Paleontologists used to believe that dinosaurs lived only in the warmest parts of the world. They thought that dinosaurs could only have lived in places where turtles, crocodiles, and snakes live today. Later, these dinosaur scientists began finding bones in surprising places. One of those surprising fossil beds is a place called Dinosaur Cove, Australia. One hundred million years ago, Australia was connected to Antarctica. Both continents were located near the South Pole. Today, paleontologists dig dinosaur fossils out of the ground. They think about what those ancient bones must mean.",
        "The Dunwich horror itself came between Lammas and the equinox in 1928, and Dr. Armitage was among those who witnessed its monstrous prologue. He had heard, meanwhile, of Whateley's grotesque trip to Cambridge, and of his frantic efforts to borrow or copy from the Necronomicon at the Widener Library. Those efforts had been in vain, since Armitage had issued warnings of the keenest intensity to all librarians having charge of the dreaded volume. Wilbur had been shockingly nervous at Cambridge; anxious for the book, yet almost equally anxious to get home again, as if he feared the results of being away long. Early in August the half-expected outcome developed, and in the small hours of the third Dr. Armitage was awakened suddenly by the wild, fierce cries of the savage watchdog on the college campus. Deep and terrible, the snarling, half-mad growls and barks continued; always in mounting volume, but with hideously significant pauses. Then there rang out a scream from a wholly different throat—such a scream as roused half the sleepers of Arkham and haunted their dreams ever afterward—such a scream as could come from not being born of earth, or wholly of earth."
    ]
}
df = pd.DataFrame(data)

# 3. Process the dataframe
# Specify the dataframe and the name of the column containing the text
print("Extracting features...")
results_df = pipeline.process_dataframe(df, text_column='text')

# 4. View results
print(f"Extraction complete! Found {len(results_df.columns)} columns.")

# Print all metrics, iterating over the columns
print("\nFull output for Text 1 and Text 2:")
for col in results_df.columns:
    if col not in ['text_id', 'text']:
        val1 = results_df.iloc[0][col]
        val2 = results_df.iloc[1][col]
        if isinstance(val1, float):
            print(f"{col:25s}: Text 1 = {val1:7.2f} | Text 2 = {val2:7.2f}")
        else:
            print(f"{col:25s}: Text 1 = {str(val1):>7s} | Text 2 = {str(val2):>7s}")
```

### Processing a single text string

```python
from eabra.pipeline import EABRAPipeline

# 1. Initialize the pipeline
pipeline = EABRAPipeline()

# 2. Process your text
text = "The quick brown fox jumps over the lazy dog."
features = pipeline.process_text(text)

# The result is a dictionary containing hundreds of aggregated features
print("Average Syllables per word:", features['LENwrdSYL_avg'])
print("Lexical Diversity (TTR):", features['LEXdvrWLT'])
```

## Troubleshooting

- **ModuleNotFoundError: No module named 'pkg_resources'**: This occurs in newer Python versions with certain libraries like `lexical-diversity`. Ensure you have installed `setuptools<70.0.0` as specified in the installation steps.
- **spaCy Build Errors**: If `pip install spacy` fails during the "Building wheels" step, ensure you are not using an unsupported or overly-new version of Python (like 3.14). Downgrading to Python 3.13 or 3.12 will fix this.

## Language variables / aggregators description

We kept the same names from FABRA. FABRA documentation is available here. https://cental.uclouvain.be/fabra/docs.html (webpage archive in PDF format can be found in the repository)
