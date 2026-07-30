from src.collectors.demo import DemoCollector


def main():

    collector = DemoCollector()

    jobs = collector.collect()

    print()

    print("=" * 60)

    print(f"Collected {len(jobs)} jobs")

    print("=" * 60)

    for job in jobs:

        print()

        print(job.company)
        print(job.role)
        print(job.location)
        print(job.source)


if __name__ == "__main__":
    main()