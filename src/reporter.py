def summarize_by_severity(vulns):
    summary = {}

    for vuln in vulns:
        severity = vuln.get("severity", "UNKNOWN")
        summary[severity] = summary.get(severity, 0) + 1

    return summary


def print_summary(summary):
    print("Summary:")
    for severity, count in sorted(
        summary.items(), key=lambda x: x[1], reverse=True
    ):
        print(f"{severity}: {count}")
