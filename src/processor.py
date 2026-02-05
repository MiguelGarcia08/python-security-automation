def prioritize_vulnerabilities(vulns, min_cvss):
    """
    Filter vulnerabilities based on risk criteria.
    """
    return [
        v for v in vulns
        if v.get("cvss", 0) >= min_cvss and v.get("exploitable", False)
    ]
