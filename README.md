Here’s a sample `README.md` for your Hugging Face API:

````markdown
# Hugging Face LLM API

This project provides a RESTful API for generating text using Hugging Face's pre-trained language models. The API is built using **FastAPI** and packaged in a Docker container for easy deployment. It supports both CPU and GPU environments and returns responses in JSON format.

---

## Features

- **Efficient Text Generation**: Leverage state-of-the-art Hugging Face models like GPT-2 or any other compatible model.
- **JSON API**: Accepts prompts and returns generated text in a structured JSON format.
- **Customizable Parameters**: Configure max token length and the number of response sequences.
- **Easy Deployment**: Dockerized for quick setup in any environment, including cloud platforms.
- **Interactive Documentation**: Automatically generated Swagger and ReDoc UI for API exploration.

---

## Getting Started

### Prerequisites

- **Docker**: Install Docker from [docker.com](https://www.docker.com/).
- **GPU Support** (Optional): NVIDIA drivers and CUDA-compatible GPU (if you plan to use GPU acceleration).

---

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/huggingface-api.git
   cd huggingface-api
   ```
````

2. **Build the Docker Image**:

   ```bash
   docker build -t huggingface-api .
   ```

3. **Run the Docker Container**:
   - **For CPU**:
     ```bash
     docker run -it --rm -p 5000:5000 huggingface-api
     ```
   - **For GPU** (if supported):
     ```bash
     docker run -it --rm --gpus all -p 5000:5000 huggingface-api
     ```

---

### Usage

1. **Access the API**:
   Once the container is running, the API is available at: `http://localhost:5000`.

2. **Send a Text Generation Request**:
   Use tools like `curl`, Postman, or a browser to interact with the API.

   **Example `curl` Request**:

   ```bash
   curl -X POST "http://localhost:5000/generate/" \
        -H "Content-Type: application/json" \
        -d '{"text": "What is the capital of France?", "max_length": 30, "num_return_sequences": 1}'
   ```

   **Sample JSON Response**:

   ```json
   {
     "responses": ["The capital of France is Paris."]
   }
   ```

3. **Interactive Documentation**:
   - Swagger UI: [http://localhost:5000/docs](http://localhost:5000/docs)
   - ReDoc: [http://localhost:5000/redoc](http://localhost:5000/redoc)

---

## API Reference

### POST `/generate/`

Generate text based on a given prompt.

#### Request Body (JSON)

| Parameter              | Type     | Default  | Description                               |
| ---------------------- | -------- | -------- | ----------------------------------------- |
| `text`                 | `string` | Required | Input prompt for text generation.         |
| `max_length`           | `int`    | `50`     | Maximum number of tokens in the response. |
| `num_return_sequences` | `int`    | `1`      | Number of responses to generate.          |

#### Response

| Field       | Type   | Description                       |
| ----------- | ------ | --------------------------------- |
| `responses` | `list` | List of generated text responses. |

#### Example

**Request**:

```json
{
  "text": "Tell me a story about AI.",
  "max_length": 50,
  "num_return_sequences": 1
}
```

**Response**:

```json
{
  "responses": ["Once upon a time, an AI learned to write its own stories..."]
}
```

---

## Customization

1. **Change the Model**:
   Modify the `MODEL_NAME` in `run_model.py` to use a different Hugging Face model:

   ```python
   MODEL_NAME = "microsoft/Phi-3-mini-128k-instruct"
   ```

2. **Add Additional Parameters**:
   Enhance the `generate` method in `run_model.py` to include more options like temperature or top-p sampling.

---

## Acknowledgements

- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [FastAPI Framework](https://fastapi.tiangolo.com/)
- [Docker](https://www.docker.com/)
