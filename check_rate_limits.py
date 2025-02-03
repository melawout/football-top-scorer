import requests


def check_rate_limits(url, headers):
    """Check rate limits for the API"""

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    daily_limits = response.headers.get("x-ratelimit-requests-limit")
    daily_remaining = response.headers.get("x-ratelimit-requests-remaining")
    calls_per_min_allowed = response.headers.get("X-RateLimit-Limit")
    calls_per_min_remaining = response.headers.get("X-RateLimit-Remaining")

    rate_limits = {
        "daily_limits": daily_limits,
        "daily_remaining": daily_remaining,
        "minute_limit": calls_per_min_allowed,
        "minute_remaining": calls_per_min_remaining,
    }

    print(rate_limits)
