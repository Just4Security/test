
import sys
import csv
import os
from openai import AsyncOpenAI
import asyncio
import time

print("="*60)
print("脚本开始执行")
print("="*60)

# 配置
DOUBAO_API_KEY = "fd61d5ec-9e51-45a0-9912-9911189fa008"
DOUBAO_BASE_URL = "https://ark.cn-beijing.volces.com/api/v3"
MAX_CONCURRENT_REQUESTS = 50  # 增加并发数
TEST_LIMIT = None  # 处理全部数据

