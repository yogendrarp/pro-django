if IN_DOCKER:  # type: ignore # noqa: F821
    print("In Docker")
    assert MIDDLEWARE[:1] == [  # type: ignore # noqa: F821
        'django.middleware.security.SecurityMiddleware'
    ]
