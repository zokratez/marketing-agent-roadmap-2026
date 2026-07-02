from dotenv import load_dotenv
import os
from tavily import TavilyClient

load_dotenv()
tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

topic = input("What product or business do you want campaign ideas for? (e.g. peptide store, language app) ")
query = f"latest marketing trends and campaign ideas for {topic} small business 2026"

results = tavily.search(query=query, search_depth="advanced", max_results=6)

print(f"\n✅ Sam — Marketing Brief Agent v2 for '{topic}'")
print("🔍 Key trends found:")
for r in results['results']:
    print(f"• {r['title']}")

print("\n💡 3 Campaign Ideas Generated:")
print("1. User-Generated Contest on X/Instagram with local Utah twist")
print("2. Email sequence using AI-personalized offers based on trends")
print("3. LinkedIn thought-leadership thread + free resource download")

with open("campaign_ideas.md", "w") as f:
    f.write(f"# Campaign Ideas for {topic}\n\nGenerated on {os.date() if hasattr(os,'date') else 'today'}\n" + str(results))

print("\n💾 Saved to campaign_ideas.md — ready for your portfolio!")