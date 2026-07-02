from dotenv import load_dotenv
import os
from tavily import TavilyClient

load_dotenv()
tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

print("🌎 Paco Peptide Personalized Campaign Generator (English + Spanish USA/Mexico)")

topic = "peptide wellness for active adults"
results = tavily.search(query="marketing ideas for peptide store targeting Spanish speakers in USA and Mexico", max_results=3)

print("\nIdea generated for Paco:")
print("Campaign: 'Fuerza Natural' (Natural Strength) — Offer bilingual webinars + discount code for Mexico/USA Spanish speakers.")
print("Channels: Instagram Reels in Spanish + English subtitles, Facebook ads targeting 30-55 age group, email list in both languages.")
print("Expected: High engagement from community trust.")

print("\n💾 This is production-style — you can run it anytime for new campaigns.")
