import os
from openai import OpenAI


def load_api_config():
    """
    从根目录的openapi_key.txt文件中加载API配置
    """
    parser_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(parser_dir)
    config_file = os.path.join(project_root, "openai_key.txt")  # 绝对路径
    
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