import httpx
from duckduckgo_search import DDGS
import argparse
import warnings
import sys

warnings.filterwarnings("ignore")

ddg_search = DDGS()

def get_answer(query: str) -> str:
    models = ["gpt-4o-mini", "llama-3.1-70b", "mixtral-8x7b", "claude-3-haiku"]
    
    for model in models:
        try:
            response = ddg_search.chat(keywords=query, model=model, timeout=30)
            if response:  
                return response
        except Exception:
            continue
    
    return "Unable to fetch an answer. Please try again later."

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get answer to a query.")
    parser.add_argument("query", type=str, help="The query to get an answer for.")
    args = parser.parse_args()
    answer = get_answer(args.query)
    sys.stdout.write(answer)
    sys.stdout.flush()
