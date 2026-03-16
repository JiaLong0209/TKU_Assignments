import os
from google import genai

def list_my_models():
    api_key = os.environ.get("GOOGLE_API_KEY", "AIzaSyBHEhcYQH0TOLLHp-B4t8i5OhhuD-TFZJk")
    client = genai.Client(api_key=api_key)
    
    print("🔍 正在搜尋 よしたかくん 可以使用的模型列表...")
    print("-" * 50)
    
    # 使用 models.list() 取得清單
    for model in client.models.list():
        # 篩選出我們感興趣的 gemma 或 gemini 模型
        if "gemma" in model.name or "gemini" in model.name:
            print(f"ID: {model.name}")
            print(f"   ﹂ 支援方法: {model.supported_generation_methods}")
            print(f"   ﹂ 描述: {model.description}\n")

if __name__ == "__main__":
    list_my_models()
