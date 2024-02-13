import requests
import os


def get_package_versions(owner, repo, package_name, token):
    api_url = f"https://api.github.com/orgs/{owner}/packages/container/{package_name}/versions"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github.v3+json",
    }

    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        versions = response.json()
        if versions:
            print(f"Versions for package {package_name}:")
            for version in versions:
                print(version["name"])
        else:
            print(f"No versions found for package {package_name}.")
    else:
        print(
            "Failed to fetch package versions. Check the package name and your API token."
        )


def list_github_packages(owner, repo, token):
    api_url = f"https://api.github.com/repos/{owner}/{repo}/packages"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github.v3+json",
    }

    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        packages = response.json()
        if packages:
            print(f"Packages found for {owner}/{repo}:")
            for package in packages:
                print(f"Name: {package['name']}, ID: {package['id']}")

            selected_package = input(
                "Enter the name of the package to list its versions: "
            )
            get_package_versions(owner, repo, selected_package, token)
        else:
            print("No packages found.")
    else:
        print(
            "Failed to fetch packages. Make sure the repository exists and your API token is correct."
        )


if __name__ == "__main__":
    OWNER = input("GH_USER")
    REPO = input("GH_REPO")
    TOKEN = input("GH_PAT")
    list_github_packages(OWNER, REPO, TOKEN)
