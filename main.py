from src.search.serpapi import SerpApiSearch


def main():

    search = SerpApiSearch()

    results = search.search(
        'Strategy Consultant Delhi NCR'
    )

    print("=" * 60)

    print(f"Found {len(results)} results")

    print("=" * 60)

    for r in results:

        print(r.title)
        print(r.url)
        print()


if __name__ == "__main__":
    main()