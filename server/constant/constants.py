# Directory for storing cache files used by the DiskCache library
DISKCACHE_DIR = "diskcache_dir"

# Directory for storing SQLite database files
SQLITE_DB_DIR = "sqlite_dir"

# Name of the SQLite database file
SQLITE_DB_NAME = "mydatabase.sqlite3"

# Directory for storing Chroma vector database files
CHROMA_DB_DIR = "chroma_dir"

# Name of the collection in the Chroma vector database
CHROMA_COLLECTION_NAME = "mychroma_collection"

# Name of the OpenAI model used for embedding text
OPENAI_EMBEDDING_MODEL_NAME = "text-embedding-3-small"

# Maximum length of text chunks when splitting up large documents
MAX_CHUNK_LENGTH = 2560

# Amount of overlap between consecutive text chunks
CHUNK_OVERLAP = 0

# Maximum allowable length for a single query string
MAX_QUERY_LENGTH = 200

# Number of top documents to recall for initial retrieval in search operations
RECALL_TOP_K = 5

# Number of top documents to recall when using re-ranking
RERANK_RECALL_TOP_K = 10

# Defines the model used for re-ranking.
# 'ms-marco-TinyBERT-L-2-v2': Nano (~4MB), blazing fast model & competitive performance (ranking precision).
# 'ms-marco-MiniLM-L-12-v2': Small (~34MB), slightly slower & best performance (ranking precision).
RERANK_MODEL_NAME = "ms-marco-MiniLM-L-12-v2"

# Maximum number of historical user sessions to retain
MAX_HISTORY_SESSION_LENGTH = 2

# Duration in seconds before a session expires
SESSION_EXPIRE_TIME = 1800

# Base directory for serving static files
STATIC_DIR = "web"

# Sub-directory under STATIC_DIR where media files are stored
MEDIA_DIR = "media_dir"

# Unique identifier for the distributed lock in the DiskCache
DISTRIBUTED_LOCK_ID = "open_kf:distributed_lock"

# Expiration time for the distributed lock (in seconds)
DISTRIBUTED_LOCK_EXPIRE_TIME = 20

# Directory where downloaded local files are stored
LOCAL_FILE_DOWNLOAD_DIR = "download_dir"

# Maximum number of concurrent requests allowed for file writing
MAX_CONCURRENT_WRITES = 5

# Maximum file size (30MB in bytes)
MAX_FILE_SIZE = 30 * 1024 * 1024

# Maximum number of files per upload
MAX_LOCAL_FILE_BATCH_LENGTH = 10

# Supported file extensions
FILE_LOADER_EXTENSIONS = {
".xlsx"
}


# in t_local_file_tab
#`doc_status` meanings:
#  0 - 'Process failed'
#  1 - 'Local files recorded'
#  2 - 'Local files parsing'
#  3 - 'Local files parsing completed'
#  4 - 'Local files text Embedding stored in VectorDB'
LOCAL_FILE_PROCESS_FAILED = 0
LOCAL_FILE_RECORDED = 1
LOCAL_FILE_PARSING = 2
LOCAL_FILE_PARSING_COMPLETED = 3
LOCAL_FILE_EMBEDDED = 4


# in t_doc_embedding_map_tab
#`doc_source` meanings:
#  1 - 'from sitemap URLs'
#  2 - 'from isolated URLs'
#  3 - 'from local files'
FROM_LOCAL_FILE = 3
