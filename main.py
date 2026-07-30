from src.utils.config_loader import load_all_configs


def main():
    config = load_all_configs()

    print("=" * 50)
    print("🚀 JobHunter AI")
    print("=" * 50)

    print(f"\nCompanies Loaded : {len(config['companies'])}")

    print("\nSearch Profiles")
    for profile in config["keywords"]:
        print(f"  • {profile}")

    print("\nLocations")
    for location in config["settings"]["locations"]:
        print(f"  • {location}")

    print("\nExcluded Roles")
    for role in config["settings"]["exclude"]:
        print(f"  • {role}")

    print("\n✅ Configuration Loaded Successfully")


if __name__ == "__main__":
    main()