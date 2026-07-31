"""Word cloud of S&P 500 company names, sized by approximate market cap."""

from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Top S&P 500 companies with approximate relative weights (market cap tiers)
companies = {
    "Apple": 100, "Microsoft": 95, "NVIDIA": 90, "Amazon": 85,
    "Alphabet": 70, "Meta": 65, "Berkshire Hathaway": 50,
    "Broadcom": 45, "Tesla": 42, "JPMorgan": 40,
    "Eli Lilly": 38, "Visa": 35, "Walmart": 34, "UnitedHealth": 33,
    "Mastercard": 30, "Johnson & Johnson": 28, "Costco": 27,
    "Procter & Gamble": 26, "Home Depot": 25, "Netflix": 24,
    "Coca-Cola": 23, "Salesforce": 22, "Cisco": 21, "Abbott": 20,
    "Chevron": 19, "Disney": 18, "PepsiCo": 18, "Intel": 17,
    "Nike": 16, "Goldman Sachs": 16, "Morgan Stanley": 15,
    "Starbucks": 15, "Boeing": 14, "McDonald's": 14, "AMD": 13,
    "Caterpillar": 13, "Target": 12, "FedEx": 12, "PayPal": 11,
    "Uber": 11, "Airbnb": 10, "Moderna": 10, "Spotify": 9,
    "General Electric": 9, "Ford": 8, "Delta": 8,
    "Lockheed Martin": 8, "3M": 7, "Hilton": 7, "Kraft Heinz": 6,
    "Hershey": 6, "Chipotle": 6, "Lululemon": 5, "Etsy": 5,
    "Domino's": 5, "Snap": 4, "Ralph Lauren": 4, "Hasbro": 4,
    "Under Armour": 3, "Gap": 3, "Nordstrom": 3,
}

wc = WordCloud(
    width=1200,
    height=900,
    background_color="white",
    colormap="Dark2",
    max_words=60,
    prefer_horizontal=0.75,
    relative_scaling=0.55,
    min_font_size=10,
    max_font_size=120,
    margin=8,
)
wc.generate_from_frequencies(companies)

fig, ax = plt.subplots(figsize=(5, 3.75))
ax.imshow(wc, interpolation="bilinear")
ax.axis("off")
fig.tight_layout(pad=0)
fig.savefig("sp500_wordcloud.pdf", bbox_inches="tight", dpi=200)
print("Saved to sp500_wordcloud.pdf")
