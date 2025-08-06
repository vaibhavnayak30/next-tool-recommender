# Custom Next Tool Predictor with Confidence Score

This project implements a custom deep learning model in PyTorch designed to predict the next user action (tool) in a sequence. A unique feature of this model is its ability to not only predict the next tool but also to output a confidence score, indicating its certainty in the prediction.

The model is built with a transformer-based architecture and is trained on a synthetic dataset of realistic user workflows in a text-editing environment. This project serves as a practical example of custom model training, multi-objective loss functions, and data generation for sequence prediction tasks.

## 🚀 Key Features

* **Transformer-based Architecture:** A core `TransformerDecoder` handles sequential data, learning complex relationships between tools.
* **Context-Rich Embeddings:** The model's input embeddings are a learned fusion of three sources: tool IDs, positional information, and pre-trained semantic embeddings of tool descriptions.
* **Multi-Objective Loss:** The model is trained to optimize two objectives simultaneously:
    * **Tool Prediction:** Using `FocalLoss` to handle class imbalance and accurately predict the next tool.
    * **Confidence Scoring:** Using `Binary Cross-Entropy Loss` to train a separate head to predict how confident the model is in its primary prediction.
* **Robust Training Practices:** The training loop includes adaptive learning rate scheduling (`ReduceLROnPlateau`), gradient clipping, and checkpointing to save the best-performing model.
* **Synthetic Dataset Generation:** The project includes a robust method for generating a diverse and meaningful dataset of user tool sequences, mimicking realistic workflows.

## 🧠 Model Architecture

The model, `EnhancedToolPredictor`, is composed of the following key components:

1.  **Input Embedding Layer:** It takes tool IDs, positional indices, and pre-computed description embeddings. These three vectors are combined (by element-wise addition) to create a single rich representation for each tool in the sequence.
2.  **Transformer Decoder Stack:** A stack of `nn.TransformerDecoderLayer`s processes the combined embeddings, allowing the model to learn the dependencies between tools in the sequence.
3.  **Output Layers:** The final representation from the transformer is passed to two separate linear layers:
    * `output_layer`: Maps the internal representation to the size of the tool vocabulary, producing raw prediction scores (logits).
    * `confidence_head`: Maps the internal representation to a single value, representing the model's confidence.

## 📊 Dataset

The dataset is synthetically generated to simulate user behavior. It combines:

* **`tool_vocab` & `tool_descriptions`**: A comprehensive list of tools and their functions.
* **`tool_patterns`**: A dictionary that defines likely next actions for each tool.
* **`common_workflows`**: Longer, pre-defined sequences that represent common, multi-step tasks (e.g., "Drafting a New Document").

This approach ensures the model is trained on both common short-term patterns and more complex, meaningful workflows.

## 🚀 Getting Started

### Prerequisites

You will need Python and the following libraries:

```bash
pip install torch sentence-transformers scikit-learn numpy