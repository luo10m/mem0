import importlib

from mem0.configs.llms.base import BaseLlmConfig


def load_class(class_type):
    module_path, class_name = class_type.rsplit(".", 1)
    module = importlib.import_module(module_path)
    return getattr(module, class_name)


class LlmFactory:
    provider_to_class = {
        "g4f": "mem0.llms.g4f.py.G4fLLM",
        "openrouter": "mem0.llms.openrouter.py.OpenRouterLLM",
        "doubao": "mem0.llms.doubao.py.DoubaoLLM",
        "ollama": "mem0.llms.ollama.py.OllamaLLM",
        "openai": "mem0.llms.openai.OpenAILLM",
        "groq": "mem0.llms.groq.GroqLLM",
        "together": "mem0.llms.together.TogetherLLM",
        "aws_bedrock": "mem0.llms.aws_bedrock.AWSBedrockLLM",
        "litellm": "mem0.llms.litellm.LiteLLM",
    }

    @classmethod
    def create(cls, provider_name, config):
        class_type = cls.provider_to_class.get(provider_name)
        if class_type:
            llm_instance = load_class(class_type)
            base_config = BaseLlmConfig(**config)  # mem0/configs/llms/base.py
            return llm_instance(base_config)
        else:
            raise ValueError(f"Unsupported Llm provider: {provider_name}")


class EmbedderFactory:
    provider_to_class = {
        "g4f": "mem0.embeddings.g4f.G4fEmbedding",
        "openrouter": "mem0.embeddings.openrouter.OpenRouterEmbedding",
        "doubao": "mem0.embeddings.doubao.DoubaoEmbedding",
        "openai": "mem0.embeddings.openai.OpenAIEmbedding",
        "ollama": "mem0.embeddings.ollama.OllamaEmbedding",
        "huggingface": "mem0.embeddings.huggingface.HuggingFaceEmbedding",
    }

    @classmethod
    def create(cls, provider_name):
        class_type = cls.provider_to_class.get(provider_name)
        if class_type:
            embedder_instance = load_class(class_type)()
            return embedder_instance
        else:
            raise ValueError(f"Unsupported Embedder provider: {provider_name}")
