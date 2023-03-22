from mkdocs.commands.build import build
from mkdocs.config.base import load_config


def test_plugin_language_selector_use_directory_urls():
    mkdocs_config = load_config(
        "tests/mkdocs.yml",
        theme={"name": "mkdocs"},
        use_directory_urls=True,
        docs_dir="docs_suffix_structure/",
        plugins={
            "i18n": {
                "default_language": "en",
                "languages": {"fr": "français", "en": "english"},
            }
        },
    )
    i18n_plugin = mkdocs_config["plugins"]["i18n"]
    result = i18n_plugin.on_config(mkdocs_config, force=True)
    assert result["extra"]["alternate"] == [
        {"name": "english", "link": "./", "fixed_link": None, "lang": "en"},
        {"name": "français", "link": "./fr/", "fixed_link": None, "lang": "fr"},
    ]


def test_plugin_language_selector_no_use_directory_urls():
    mkdocs_config = load_config(
        "tests/mkdocs.yml",
        theme={"name": "mkdocs"},
        use_directory_urls=False,
        docs_dir="docs_suffix_structure/",
        plugins={
            "i18n": {
                "default_language": "en",
                "languages": {"fr": "français", "en": "english"},
            }
        },
    )
    i18n_plugin = mkdocs_config["plugins"]["i18n"]
    result = i18n_plugin.on_config(mkdocs_config, force=True)
    assert result["extra"]["alternate"] == [
        {"name": "english", "link": "./index.html", "fixed_link": None, "lang": "en"},
        {
            "name": "français",
            "link": "./fr/index.html",
            "fixed_link": None,
            "lang": "fr",
        },
    ]


def test_plugin_language_selector_fixed_alternate():
    mkdocs_config = load_config(
        "tests/mkdocs.yml",
        theme={"name": "mkdocs"},
        use_directory_urls=True,
        docs_dir="docs_suffix_structure/",
        extra={
            "alternate": [
                {"name": "english", "link": "./default", "lang": "en"},
                {"name": "français", "link": "./french", "lang": "fr"},
            ]
        },
        plugins={
            "i18n": {
                "default_language": "en",
                "languages": {"fr": "français", "en": "english"},
            }
        },
    )
    i18n_plugin = mkdocs_config["plugins"]["i18n"]
    result = i18n_plugin.on_config(mkdocs_config)
    assert result["extra"]["alternate"] == [
        {"name": "english", "link": "./default", "lang": "en"},
        {"name": "français", "link": "./french", "lang": "fr"},
    ]


def test_plugin_language_selector_single_default_language():
    mkdocs_config = load_config(
        "tests/mkdocs.yml",
        theme={"name": "mkdocs"},
        use_directory_urls=True,
        docs_dir="docs_suffix_structure/",
        plugins={"i18n": {"default_language": "fr", "languages": {"fr": "français"}}},
    )
    i18n_plugin = mkdocs_config["plugins"]["i18n"]
    result = i18n_plugin.on_config(mkdocs_config, force=True)
    assert result["extra"] == {}


def test_plugin_language_selector_use_directory_urls_default():
    mkdocs_config = load_config(
        "tests/mkdocs.yml",
        theme={"name": "mkdocs"},
        use_directory_urls=True,
        docs_dir="docs_suffix_structure/",
        plugins={
            "i18n": {
                "default_language": "en",
                "languages": {
                    "default": {"name": "default_english"},
                    "fr": "français",
                    "en": "english",
                },
            }
        },
    )
    i18n_plugin = mkdocs_config["plugins"]["i18n"]
    result = i18n_plugin.on_config(mkdocs_config, force=True)
    assert result["extra"]["alternate"] == [
        {"name": "default_english", "link": "./", "fixed_link": None, "lang": "en"},
        {"name": "français", "link": "./fr/", "fixed_link": None, "lang": "fr"},
        {"name": "english", "link": "./en/", "fixed_link": None, "lang": "en"},
    ]


def test_plugin_language_selector_fixed_link():
    mkdocs_config = load_config(
        "tests/mkdocs.yml",
        theme={"name": "mkdocs"},
        docs_dir="docs_suffix_structure/",
        plugins={
            "i18n": {
                "default_language": "en",
                "languages": {
                    "fr": {"name": "français", "fixed_link": "/fr"},
                    "en": {"name": "english", "fixed_link": "/en"},
                },
            }
        },
    )
    i18n_plugin = mkdocs_config["plugins"]["i18n"]
    result = i18n_plugin.on_config(mkdocs_config, force=True)
    assert result["extra"]["alternate"] == [
        {"name": "english", "link": "./", "fixed_link": "/en", "lang": "en"},
        {"name": "français", "link": "./fr/", "fixed_link": "/fr", "lang": "fr"},
    ]
    build(mkdocs_config)


def test_plugin_language_selector_fixed_link_with_static_alternate():
    mkdocs_config = load_config(
        "tests/mkdocs.yml",
        theme={"name": "mkdocs"},
        docs_dir="docs_suffix_structure/",
        extra={
            "alternate": [
                {"name": "english", "link": "./", "lang": "en"},
                {
                    "name": "français",
                    "link": "./fr/",
                    "lang": "fr",
                },
            ],
        },
        plugins={
            "i18n": {
                "default_language": "en",
                "languages": {
                    "fr": {"name": "français", "fixed_link": "/fr"},
                    "en": {"name": "english", "fixed_link": "/en"},
                },
            }
        },
    )
    i18n_plugin = mkdocs_config["plugins"]["i18n"]
    result = i18n_plugin.on_config(mkdocs_config)
    assert result["extra"]["alternate"] == [
        {"name": "english", "link": "./", "lang": "en"},
        {"name": "français", "link": "./fr/", "lang": "fr"},
    ]
    build(mkdocs_config)
