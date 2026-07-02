from dotenv import load_dotenv
import os
from tavily import TavilyClient

load_dotenv()
tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

print("🔍 Phase 2 Competitor Spy v2 for Peptide Store")

query = "competitors to Paco peptide store in Utah wellness and performance peptides 2026"
results = tavily.search(query=query, max_results=5)

print("\nCompetitors found:")
for r in results['results']:
    print(f"• {r['title']}")

print("\n💡 Campaign counter-idea: Offer better local Utah delivery and gym bundle to beat competitors.")

print("💾 Spy ran successfully!")