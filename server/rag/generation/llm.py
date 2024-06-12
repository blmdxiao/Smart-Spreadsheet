import os
from openai import OpenAI
from server.logger.logger_config import my_logger as logger


class LLMGenerator:
    def __init__(self) -> None:
        self.llm_name = os.getenv('LLM_NAME')
        if self.llm_name == 'OpenAI':
            api_key = os.getenv('OPENAI_API_KEY')
            self.client = OpenAI(api_key=api_key)
            self.model_name = os.getenv('GPT_MODEL_NAME')
        else:
            raise ValueError(f"Unsupported LLM_NAME: '{self.llm_name}'. Must be in['OpenAI']")

    def generate(self, prompt: str, is_streaming: bool = False, is_json: bool = False):
        if is_streaming:
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=[{"role": "user", "content": prompt}],
                temperature=0,
                #top_p=0.7,
                stream=True
            )
            return response
        else:
            if is_json:
                response = self.client.chat.completions.create(
                    model=self.model_name,
                    response_format={"type": "json_object"},
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0,
                    #top_p=0.7,
                    stream=False
                )
            else:
                response = self.client.chat.completions.create(
                    model=self.model_name,
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0,
                    #top_p=0.7,
                    stream=False
                )
            return response


llm_generator = LLMGenerator()
