import os
import sys
from server.logger.logger_config import my_logger as logger


os.environ["TOKENIZERS_PARALLELISM"] = "false"


def check_env_variables():
    LLM_NAME = os.getenv('LLM_NAME')
    llm_name_list = ['OpenAI']
    if LLM_NAME not in llm_name_list:
        logger.error(f"LLM_NAME: '{LLM_NAME}' is illegal! Must be in {llm_name_list}.")
        sys.exit(-1)

    if LLM_NAME == 'OpenAI':
        # OPENAI_API_KEY: API key for accessing OpenAI's services.
        OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
        if OPENAI_API_KEY == 'xxxx':
            logger.error(f"OPENAI_API_KEY: '{OPENAI_API_KEY}' is illegal!")
            sys.exit(-1)

        # GPT_MODEL_NAME: Specific GPT model being used, e.g., 'gpt-3.5-turbo' or 'gpt-4-turbo', or 'gpt-4o'.
        GPT_MODEL_NAME = os.getenv('GPT_MODEL_NAME')
        gpt_model_name_list = ['gpt-3.5-turbo', 'gpt-4-turbo', 'gpt-4o']
        if GPT_MODEL_NAME not in gpt_model_name_list:
            logger.error(f"GPT_MODEL_NAME: '{GPT_MODEL_NAME}' is illegal! Must be in {gpt_model_name_list}")
            sys.exit(-1)

    # MIN_RELEVANCE_SCORE: Minimum score for a document to be considered relevant, and will be used in prompt, between 0.3 and 0.7.
    MIN_RELEVANCE_SCORE = os.getenv('MIN_RELEVANCE_SCORE')
    try:
        min_relevance_score = float(MIN_RELEVANCE_SCORE)
        if min_relevance_score < 0.3 or min_relevance_score > 0.7:
            logger.error(f"MIN_RELEVANCE_SCORE: {MIN_RELEVANCE_SCORE} is illegal! It should be a float number between [0.3~0.7]")
            sys.exit(-1)
    except Exception as e:
        logger.error(f"MIN_RELEVANCE_SCORE: {MIN_RELEVANCE_SCORE} is illegal! It should be a float number between [0.3~0.7]")
        sys.exit(-1)

    # BOT_TOPIC: Main topic or domain the bot is designed to handle, like 'OpenIM' or 'LangChain'.
    BOT_TOPIC = os.getenv('BOT_TOPIC')
    if BOT_TOPIC == 'xxxx':
        logger.error(f"BOT_TOPIC: '{BOT_TOPIC}' is illegal! You must set your own bot topic, such as 'OpenIM' or 'LangChain', etc.")
        sys.exit(-1)

    # URL_PREFIX: The prefix URL for accessing media and other resources, must start with 'http://' or 'https://'.
    URL_PREFIX = os.getenv('URL_PREFIX')
    if not URL_PREFIX.startswith('http://') and not URL_PREFIX.startswith('https://'):
        logger.error(f"URL_PREFIX: '{URL_PREFIX}' is illegal! It must start with 'http://' or 'https://'")
        sys.exit(-1)

    # USE_PREPROCESS_QUERY: Flag (0 or 1) indicating whether preprocessing should be applied to queries.
    USE_PREPROCESS_QUERY = os.getenv('USE_PREPROCESS_QUERY')
    try:
        use_preprocess_query = int(USE_PREPROCESS_QUERY)
        if use_preprocess_query not in [0, 1]:
            logger.error(f"USE_PREPROCESS_QUERY: {USE_PREPROCESS_QUERY} is illegal! It should be 0 or 1!")
            sys.exit(-1)
    except Exception as e:
        logger.error(f"USE_PREPROCESS_QUERY: {USE_PREPROCESS_QUERY} is illegal! It should be 0 or 1!")
        sys.exit(-1)

    # USE_RERANKING: Flag (0 or 1) indicating whether reranking should be applied to search results.
    USE_RERANKING = os.getenv('USE_RERANKING')
    try:
        use_reranking = int(USE_RERANKING)
        if use_reranking not in [0, 1]:
            logger.error(f"USE_RERANKING: {USE_RERANKING} is illegal! It should be 0 or 1!")
            sys.exit(-1)
    except Exception as e:
        logger.error(f"USE_RERANKING: {USE_RERANKING} is illegal! It should be 0 or 1!")
        sys.exit(-1)

    # USE_DEBUG: Flag (0 or 1) indicating whether to output additional debug information, such as `search`, `reranking`, `prompt`.
    USE_DEBUG = os.getenv('USE_DEBUG')
    try:
        use_debug = int(USE_DEBUG)
        if use_debug not in [0, 1]:
            logger.error(f"USE_DEBUG: {USE_DEBUG} is illegal! It should be 0 or 1!")
            sys.exit(-1)
    except Exception as e:
        logger.error(f"USE_DEBUG: {USE_DEBUG} is illegal! It should be 0 or 1!")
        sys.exit(-1)

    # USE_LLAMA_PARSE: Flag (0 or 1) indicating whether to use `LlamaParse` to parse Excel files.
    USE_LLAMA_PARSE = os.getenv('USE_LLAMA_PARSE')
    try:
        use_llama_parse = int(USE_LLAMA_PARSE)
        if use_llama_parse not in [0, 1]:
            logger.error(f"USE_LLAMA_PARSE: {USE_LLAMA_PARSE} is illegal! It should be 0 or 1!")
            sys.exit(-1)
    except Exception as e:
        logger.error(f"USE_LLAMA_PARSE: {USE_LLAMA_PARSE} is illegal! It should be 0 or 1!")
        sys.exit(-1)

    if use_llama_parse == 1:
        # LLAMA_CLOUD_API_KEY: API key for accessing services of LlamaCloud.
        LLAMA_CLOUD_API_KEY = os.getenv('LLAMA_CLOUD_API_KEY')
        if LLAMA_CLOUD_API_KEY == 'xxxx':
            logger.error(f"LLAMA_CLOUD_API_KEY: '{LLAMA_CLOUD_API_KEY}' is illegal!")
            sys.exit(-1)
