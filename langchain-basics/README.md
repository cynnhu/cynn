# LangChain 基础入门

这组示例按学习顺序介绍 LangChain 的核心组成：提示词模板、聊天模型、输出解析器，以及 Runnable 链。

## 环境准备

```bash
cd langchain-basics
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

编辑 `.env`，填入模型服务的 API Key。也可以设置 `OPENAI_BASE_URL`，连接 OpenAI 兼容服务。

## 示例说明

| 文件 | 内容 | 是否需要 API Key |
| --- | --- | --- |
| `01_prompt_template.py` | 创建并填充聊天提示词模板 | 否 |
| `02_model_call.py` | 调用聊天模型 | 是 |
| `03_output_parser.py` | 认识字符串输出解析器 | 否 |
| `04_simple_chain.py` | 使用 `prompt \| model \| parser` 组合链 | 是 |

## 运行示例

```bash
python 01_prompt_template.py
python 02_model_call.py
python 03_output_parser.py
python 04_simple_chain.py
```

`02_model_call.py` 和 `04_simple_chain.py` 会产生真实模型调用费用，请确认 API 配置和服务商计费规则。
