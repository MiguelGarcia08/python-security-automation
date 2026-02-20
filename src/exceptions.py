class VulnerabilityProcessingError(Exception):
    """Base exception for vulnerability processing errors."""


class InvalidVulnerabilityData(VulnerabilityProcessingError):
    """Raised when vulnerability data is malformed."""
