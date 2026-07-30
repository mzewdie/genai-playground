import logging
from pathlib import Path


def configure_logging() -> None:
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)

    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(name)s - %(message)s",
        datefmt="%H:%M:%S",
    )

    # Console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    # File
    #file_handler = logging.FileHandler(log_dir/"doc_analyser_logs.log")
    file_handler = logging.FileHandler(log_dir/"doc_analyser_logs.log",
                                       mode="w",          # Overwrite the log file on each application start
                                       encoding="utf-8",) 
    #mode="w" → overwrite the log file each time the application starts.
    #mode="a" (the default) → append to the existing log file.
    
    file_handler.setLevel(logging.DEBUG)
    #file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    logger.handlers.clear()      # Remove existing handlers
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    
    
    #llm debugger
    llm_debug_logger = logging.getLogger("llm_debug")
    llm_handler = logging.FileHandler("logs/llm_debug.log",
                                      mode="w",         
                                      encoding="utf-8",)
    
    llm_handler.setLevel(logging.DEBUG)
    llm_debug_logger = logging.getLogger("llm_debug")
    llm_debug_logger.setLevel(logging.DEBUG)
    llm_debug_logger.addHandler(llm_handler)