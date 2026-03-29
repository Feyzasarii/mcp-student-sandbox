import os
import logging

AWS_SECRET_KEY_ENV = "AWS_SECRET_KEY"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


def get_aws_secret_key() -> str:
    """Load the AWS secret key from a secure environment variable."""
    secret_key = os.getenv(AWS_SECRET_KEY_ENV)
    if not secret_key:
        raise RuntimeError(
            f"Environment variable {AWS_SECRET_KEY_ENV} is required and must not be hard-coded"
        )
    return secret_key


def connect() -> None:
    """Connect using the configured AWS secret key without exposing it in logs."""
    secret_key = get_aws_secret_key()
    logger.info("Connecting securely to AWS")
    # Use the secret key here for authentication, but never log it.
    _ = secret_key


if __name__ == "__main__":
    try:
        connect()
    except RuntimeError as error:
        logger.error("Configuration error: %s", error)
        raise
