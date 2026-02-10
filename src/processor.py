# def prioritize_vulnerabilities(vulns, min_cvss):
#     """
#     Filter vulnerabilities based on risk criteria.
#     """
#     return [
#         v for v in vulns
#         if v.get("cvss", 0) >= min_cvss and v.get("exploitable", False)
#     ]

from src.exceptions import InvalidVulnerabilityData


def prioritize_vulnerabilities(vulns, min_cvss=7.0):
    prioritized = []

    for vuln in vulns:
        try:
            cvss = float(vuln.get("cvss"))
            exploitable = bool(vuln.get("exploitable", False))
        except (TypeError, ValueError):
            print(
                f"[WARN] Skipping malformed vulnerability "
                f"{vuln.get('id', 'UNKNOWN')}"
            )
            continue  # ← CLAVE

        if exploitable and cvss >= min_cvss:
            prioritized.append(vuln)

    return prioritized
