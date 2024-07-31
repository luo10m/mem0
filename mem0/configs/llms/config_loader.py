import yaml
from typing import Dict, Any


def load_config() -> Dict[str, Any]:
    """
    Load the LLM provider configuration from the YAML file.

    Returns:
        Dict[str, Any]: The loaded configuration as a dictionary.
    """
    with open("./llm_providers.yaml", "r") as f:
        config = yaml.safe_load(f)

    for provider in config.get("providers", []):
        for model in provider.get("models", []):
            if model.get("max_tokens") is None:
                model["max_tokens"] = 4096

    return config


# 如果需要在其他地方使用这个配置,可以添加以下行:
LlmProvidersConfig = load_config()


# 这意味着其他模块可以直接导入并使用这个预加载的配置，而不需要每次都调用 load_config() 函数。使用方法如下：
# 1. 在需要使用配置的模块中导入 llm_provider_config：
#       from mem0.configs.llms.config_loader import llm_provider_config
# 2. 直接使用 llm_provider_config 访问配置信息：
#    获取所有提供商
#       providers = llm_provider_config["providers"]
#   获取特定提供商的配置
#       g4f_config = next(p for p in providers if p["name"] == "g4f")
#   获取特定模型的最大 token 数
#       gpt4_max_tokens = next(m["max_tokens"] for m in g4f_config["models"] if m["name"] == "gpt-4")
#   获取提供商的速率限制
#       g4f_rate_limit = g4f_config["rate_limit"]
# 3. 在初始化 LLM 客户端或其他操作中使用这些配置：
#       from mem0.configs.llms.base import BaseLlmConfig
#
#       llm_config = BaseLlmConfig(provider="g4f", model="gpt-4", max_tokens=gpt4_max_tokens)
