import requests
import sys

# Replace 'your_token_here' with your actual GitHub Personal Access Token
GITHUB_TOKEN = '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'
GITHUB_API_URL = "https://api.github.com"
HEADERS = {"Authorization": f"token {GITHUB_TOKEN}"}

def fetch_packages(org_or_user):
    """Fetch a list of packages for a given organization or user"""
    response = requests.get(f"{GITHUB_API_URL}/orgs/{org_or_user}/packages", headers=HEADERS)
    if response.status_code != 200:
        print("Error fetching packages")
        sys.exit(1)
    return response.json()

def list_packages(packages):
    """List all packages with an index for user selection"""
    for i, package in enumerate(packages):
        print(f"{i}. {package['name']}")
    print("\nSelect a package by number: ", end="")

def fetch_package_versions(org_or_user, package_name):
    """Fetch all versions for a selected package"""
    response = requests.get(f"{GITHUB_API_URL}/orgs/{org_or_user}/packages/container/{package_name}/versions", headers=HEADERS)
    if response.status_code != 200:
        print("Error fetching package versions")
        sys.exit(1)
    return response.json()

def main():
    org_or_user = input("Enter GitHub organization or user name: ")
    packages = fetch_packages(org_or_user)
    if not packages:
        print("No packages found")
        sys.exit(0)
    list_packages(packages)
    selection = int(input())
    selected_package = packages[selection]
    versions = fetch_package_versions(org_or_user, selected_package['name'])
    print(f"Versions of {selected_package['name']}:")
    for version in versions:
        print(f"- {version['name']}")