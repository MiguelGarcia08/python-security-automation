def summarize_by_severity(vulns):
    summary = {}

    for vuln in vulns:
        severity = vuln.get("severity", "UNKNOWN")
        summary[severity] = summary.get(severity, 0) + 1

    return summary


def print_summary(summary):
    print("Summary:")
    for severity, count in summary.items():
        print(f"{severity}: {count}")
