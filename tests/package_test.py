from importlib.metadata import PackageNotFoundError, version

import agend_ae


def test_package_expoe_a_versao() -> None:
    """Teste base para verificar se o pacote está instalável/importável (via checagem de versão)"""
    try:
        installed_version: str | None = version("agend_ae")
    except PackageNotFoundError:
        installed_version = getattr(agend_ae, "__version__", None)

    assert installed_version is not None
    assert isinstance(installed_version, str)
    assert len(installed_version) > 0
