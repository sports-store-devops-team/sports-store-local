from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
COMPOSE_FILE = ROOT / "docker-compose.yml"
EXPECTED_CONTEXTS = {
    "auth-service": "../sports-store-auth-service",
    "catalog-service": "../sports-store-catalog-service",
    "cart-service": "../sports-store-cart-service",
    "order-service": "../sports-store-order-service",
    "payment-service": "../sports-store-payment-service",
    "frontend": "../sports-store-frontend",
    "gateway": "../sports-store-gateway",
}
REQUIRED_VARIABLES = {"MONGO_ROOT_PASSWORD", "JWT_SECRET", "PAYMENT_FAILURE_SUFFIX"}


def main():
    document = yaml.safe_load(COMPOSE_FILE.read_text(encoding="utf-8"))
    services = document["services"]

    for service, expected in EXPECTED_CONTEXTS.items():
        actual = services[service]["build"]
        assert actual == expected, f"{service} build context changed: {actual}"
        assert (ROOT / actual).resolve().is_dir(), f"missing build context: {actual}"

    compose_text = COMPOSE_FILE.read_text(encoding="utf-8")
    for variable in REQUIRED_VARIABLES:
        assert f"${{{variable}" in compose_text, f"missing declaration: {variable}"

    assert services["gateway"]["ports"] == ["8080:8080"]
    assert "ports" not in services["frontend"]
    print("Compose structure and local Gateway routing validated.")


if __name__ == "__main__":
    main()
