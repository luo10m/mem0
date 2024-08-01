from openai import OpenAI

from mem0.embeddings.base import EmbeddingBase
from mem0.configs.llms.config_loader import LlmProvidersConfig


class DoubaoEmbedding(EmbeddingBase):

    def __init__(self, model="ep-20240613070020-zmfrj"):
        # 获取 doubao 配置
        doubao_config = next(p for p in LlmProvidersConfig["providers"] if p["name"] == "doubao")
        # 使用配置中的 base_url
        self.client = OpenAI(base_url=doubao_config["base_url"])
        self.model = model
        self.dims = 1536

    def embed(self, text):
        """
        Get the embedding for the given text using OpenAI.

        Args:
            text (str): The text to embed.

        Returns:
            list: The embedding vector.
        """
        text = text.replace("\n", " ")
        return self.client.embeddings.create(input=[text], model=self.model).data[0].embedding
