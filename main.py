from vulnerabilities import vulnerabilities

def process_vulnerabilities(vulns):
    prioritized = [
    v for v in vulns
    if v["cvss"] >= 5.0
]


    # for vuln in vulns:
    #     if vuln["exploitable"] and vuln["cvss"] >= 7.0:
    #         prioritized.append(vuln)

    return prioritized
def summarize_by_severity(vulns):
    summary = {}

    for vuln in vulns:
        severity = vuln["severity"]
        summary[severity] = summary.get(severity, 0) + 1

    return summary


def main():
    prioritized = process_vulnerabilities(vulnerabilities)
    summary = summarize_by_severity(prioritized)

    print("Summary:")
    for severity, count in summary.items():
        print(f"{severity}: {count}")

# def main():
#     critical_assets = process_vulnerabilities(vulnerabilities)
#     #print("Critical assets affected:")
#     # for asset in critical_assets:
#     #     print(f"- {asset}")
#     print("Summary:")
#     for asset in critical_assets:
#         print(f"{asset.get("severity")} - {list(asset.values()).count(asset.get("severity"))}")  
#     # print("Critical assets affected:")
#     # for asset in critical_assets:
#     #     print(f"- {asset}")

if __name__ == "__main__":
    main()
