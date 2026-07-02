from dotenv import load_dotenv
import os
from tavily import TavilyClient

load_dotenv()
tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

query = "latest marketing trends for small businesses July 2026"
results = tavily.search(query=query, search_depth="advanced", max_results=5)

print("✅ Sam — Your first marketing agent is running!")
print("\n🔍 Research results for campaign ideas:")
for r in results['results']:
    print(f"• {r['title']} → {r['url'][:60]}...")

print("\n💡 Campaign idea generated:")
print("Run a 'Trend-to-Campaign' thread on X + LinkedIn with user-generated content contest. Target small businesses in Utah. Expected engagement: high because it's timely and local.")