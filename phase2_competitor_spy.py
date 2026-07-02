from dotenv import load_dotenv
from tavily import TavilyClient
import os

load_dotenv()
tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

print("🔍 Phase 2 Spy Tool — Competitor Research for Peptide Store")

query = "top competitors to Paco peptide store in Utah wellness peptides 2026"
results = tavily.search(query=query, max_results=5)

print("\nCompetitors found:")
for r in results['results']:
    print(f"• {r['title']} - {r['url']}")

print("\n💡 Campaign counter-idea: Offer 'Local Utah Recovery Pack' with free local pickup and gym partnership to beat competitors.")
