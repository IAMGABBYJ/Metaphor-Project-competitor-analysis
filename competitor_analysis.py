# Import the required classes and functions from metaphor_tool.py


from metaphor_tool import Metaphor


def analyze_competitors(competitor_url):
    api_key = 'fb2fbe11-925c-403d-94c3-0858931f48e4'
    client = Metaphor(api_key=api_key)
    results = client.find_similar(url=competitor_url)

    # Extract important details from results.
    analysis_data = []
    for result in results.results:
        analysis_data.append({
            'Title': result.title,
            'URL': result.url,
            'Published Date': result.published_date,
            'Author': result.author,
        })

    return analysis_data


if __name__ == "__main__":
    competitor_url = input("Enter the URL of the competitor's article: ")
    data = analyze_competitors(competitor_url)
    for entry in data:
        print(entry)

