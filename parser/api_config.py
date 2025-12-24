import os
from openai import OpenAI


def load_api_config():
    """
    从根目录的openapi_key.txt文件中加载API配置
    文件格式：
    https://dashscope.aliyuncs.com/compatible-mode/v1 
    sk-4cca9e59e44f49ca8d6a5184c118d354
    """
    config_file = "/workspace/openapi_key.txt"
    
    if not os.path.exists(config_file):
        raise FileNotFoundError(f"API配置文件不存在: {config_file}")
    
    with open(config_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    if len(lines) < 2:
        raise ValueError("API配置文件格式不正确，应包含base_url和api_key两行")
    
    base_url = lines[0].strip()
    api_key = lines[1].strip()
    
    # 创建OpenAI客户端
    client = OpenAI(
        api_key=api_key,
        base_url=base_url
    )
    
    return client


# 全局客户端实例
llm_client = load_api_config()


def get_llm_client():
    """
    获取LLM客户端
    """
    return llm_client