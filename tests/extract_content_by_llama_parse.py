import os
from typing import List
from llama_parse import LlamaParse


LLAMA_CLOUD_API_KEY = "xxxx"  # get from cloud.llamaindex.ai


def remove_analysis_header(text: str) -> str:
    if text.startswith('# Analysis Output'):
        trip_size = len('# Analysis Output')
        text = text[trip_size:]
    elif text.startswith('Analysis Output'):
        trip_size = len('Analysis Output')
        text = text[trip_size:]
    return text


def output_content(file_list: List[str], output_type: str) -> None:
    parser = LlamaParse(
        api_key=LLAMA_CLOUD_API_KEY,
        result_type=output_type,
    )

    os.makedirs(f"output_of_llama_parse/{output_type}", exist_ok=True)
    for index, file_path in enumerate(file_list):
        out_vec = []
        documents = parser.load_data(file_path)
        for doc in documents:
            out_vec.append(remove_analysis_header(doc.text))
        content = "\n\n".join(out_vec)

        if output_type == "markdown":
            filename = f"output_of_llama_parse/{output_type}/ex_{index}.md"
        else:
            filename = f"output_of_llama_parse/{output_type}/ex_{index}.txt"

        with open(filename, 'w') as file:
            file.write(content)

if __name__ == '__main__':
    file_list = [
        './example_0.xlsx',
        './example_1.xlsx',
        './example_2.xlsx'
    ]

    output_content(file_list, "markdown")
    output_content(file_list, "text")
