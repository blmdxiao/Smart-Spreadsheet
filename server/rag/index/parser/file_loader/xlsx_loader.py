import os
from typing import Dict, List
from llama_parse import LlamaParse
import pandas as pd
from tabulate import tabulate
from server.logger.logger_config import my_logger as logger
from server.rag.index.parser.file_loader.table_processor import ExcelTableProcessor


LLAMA_CLOUD_API_KEY = os.getenv('LLAMA_CLOUD_API_KEY')


class AsyncXlsxLoader:
    def __init__(self, file_path: str) -> None:
        logger.info(f"[FILE LOADER] init xlsx, file_path: '{file_path}'")
        self.file_path = file_path

    async def get_markdown_tables(self) -> Dict[str, List[str]]:
        try:
            processor = ExcelTableProcessor(self.file_path)
            sheet_tables = processor.process_sheets()
            return sheet_tables
        except Exception as e:
            logger.error(f"get_markdown_tables is failed, exception: {e}")
            return []

    def remove_analysis_header(self, text: str) -> str:
        if text.startswith('# Analysis Output'):
            trip_size = len('# Analysis Output')
            text = text[trip_size:]
        return text

    async def get_content_by_llama_parse(self) -> str:
        try:
            parser = LlamaParse(
                api_key=LLAMA_CLOUD_API_KEY,
                result_type="markdown",
            )

            text_vec = []

            import nest_asyncio
            nest_asyncio.apply()

            documents = parser.load_data(self.file_path)
            for doc in documents:
                text_vec.append(self.remove_analysis_header(doc.text))
            content = "\n\n".join(text_vec)
            return content
        except Exception as e:
            logger.error(f"get_content_by_llama_parse is failed, exception: {e}")
            return ''

    async def get_content(self) -> str:
        try:
            content = ''

            # Load all sheets from the Excel file
            sheets_dict = pd.read_excel(self.file_path, sheet_name=None)
            # This will hold the markdown content for all sheets
            markdown_content = []

            # Load all sheets from the Excel file
            sheets_dict = pd.read_excel(self.file_path, sheet_name=None)
            # This will hold the markdown content for all sheets
            markdown_content = []

            # Process each sheet in the workbook
            for sheet_name, df in sheets_dict.items():
                # Add a header for each sheet in the Markdown output
                markdown_content.append(f"# {sheet_name}\n")

                # Convert the DataFrame to a Markdown string using DataFrame.to_markdown()
                markdown_str = df.to_markdown(index=False)
                markdown_content.append(markdown_str)
                markdown_content.append("\n")  # Add a newline for spacing between sheets
   
            if markdown_content:
                content = "\n".join(markdown_content)

            if not content:
                logger.warnning(f"file_path: '{self.file_path}' is empty!")
            return content
        except Exception as e:
            logger.error(f"get_content is failed, exception: {e}")
            return ''
