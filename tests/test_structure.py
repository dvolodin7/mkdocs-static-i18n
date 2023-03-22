from pathlib import Path

from mkdocs.commands.build import build
from mkdocs.config.base import load_config

USE_DIRECTORY_URLS = [
    Path("404.html"),
    Path("image.en.png"),
    Path("image.fr.png"),
    Path("image.en.fake"),
    Path("image.fr.fake"),
    Path("index.fr/index.html"),
    Path("index.html"),
    Path("assets/image_non_localized.png"),
    Path("topic1/named_file.en/index.html"),
    Path("topic1/named_file.fr/index.html"),
    Path("topic2/README.en/index.html"),
    Path("topic2/index.html"),
    Path("topic2/1.1.filename.fr.html"),
    Path("topic2/1.1.filename.html"),
]
NO_USE_DIRECTORY_URLS = [
    Path("404.html"),
    Path("image.en.png"),
    Path("image.fr.png"),
    Path("image.en.fake"),
    Path("image.fr.fake"),
    Path("index.fr.html"),
    Path("index.html"),
    Path("assets/image_non_localized.png"),
    Path("topic1/named_file.en.html"),
    Path("topic1/named_file.fr.html"),
    Path("topic2/README.en.html"),
    Path("topic2/index.html"),
    Path("topic2/1.1.filename.fr.html"),
    Path("topic2/1.1.filename.html"),
]


def test_build_use_directory_urls():
    mkdocs_config = load_config(
        "tests/mkdocs.yml",
        theme={"name": "mkdocs"},
        use_directory_urls=True,
        docs_dir="docs_suffix_structure/",
    )
    build(mkdocs_config)
    site_dir = mkdocs_config["site_dir"]
    generate_site = [f.relative_to(site_dir) for f in Path(site_dir).glob("**/*.html")]
    generate_site.extend(
        [f.relative_to(site_dir) for f in Path(site_dir).glob("**/image*.*")]
    )
    assert sorted(generate_site) == sorted(USE_DIRECTORY_URLS)


def test_build_no_use_directory_urls():
    mkdocs_config = load_config(
        "tests/mkdocs.yml",
        theme={"name": "mkdocs"},
        use_directory_urls=False,
        docs_dir="docs_suffix_structure/",
    )
    build(mkdocs_config)
    site_dir = mkdocs_config["site_dir"]
    generate_site = [f.relative_to(site_dir) for f in Path(site_dir).glob("**/*.html")]
    generate_site.extend(
        [f.relative_to(site_dir) for f in Path(site_dir).glob("**/image*.*")]
    )
    assert sorted(generate_site) == sorted(NO_USE_DIRECTORY_URLS)


PLUGIN_USE_DIRECTORY_URLS = [
    Path("404.html"),
    Path("image.png"),
    Path("image.fake"),
    Path("index.html"),
    Path("assets/image_non_localized.png"),
    Path("topic1/named_file/index.html"),
    Path("topic2/index.html"),
    Path("topic2/1.1.filename.html"),
    Path("en/index.html"),
    Path("en/image.png"),
    Path("en/image.fake"),
    Path("en/assets/image_non_localized.png"),
    Path("en/topic1/named_file/index.html"),
    Path("en/topic2/index.html"),
    Path("en/topic2/1.1.filename.html"),
    Path("fr/index.html"),
    Path("fr/image.png"),
    Path("fr/image.fake"),
    Path("fr/assets/image_non_localized.png"),
    Path("fr/topic1/named_file/index.html"),
    Path("fr/topic2/index.html"),
    Path("fr/topic2/1.1.filename.html"),
]
PLUGIN_NO_USE_DIRECTORY_URLS = [
    Path("404.html"),
    Path("image.png"),
    Path("image.fake"),
    Path("index.html"),
    Path("assets/image_non_localized.png"),
    Path("topic1/named_file.html"),
    Path("topic2/index.html"),
    Path("topic2/1.1.filename.html"),
    Path("en/index.html"),
    Path("en/image.png"),
    Path("en/image.fake"),
    Path("en/assets/image_non_localized.png"),
    Path("en/topic1/named_file.html"),
    Path("en/topic2/index.html"),
    Path("en/topic2/1.1.filename.html"),
    Path("fr/index.html"),
    Path("fr/image.png"),
    Path("fr/image.fake"),
    Path("fr/assets/image_non_localized.png"),
    Path("fr/topic1/named_file.html"),
    Path("fr/topic2/index.html"),
    Path("fr/topic2/1.1.filename.html"),
]


def test_plugin_use_directory_urls():
    mkdocs_config = load_config(
        "tests/mkdocs.yml",
        theme={"name": "mkdocs"},
        use_directory_urls=True,
        docs_dir="docs_suffix_structure/",
        plugins={
            "search": {},
            "i18n": {
                "default_language": "en",
                "languages": {"fr": "français", "en": "english"},
            },
        },
    )
    build(mkdocs_config)
    site_dir = mkdocs_config["site_dir"]
    generate_site = [f.relative_to(site_dir) for f in Path(site_dir).glob("**/*.html")]
    generate_site.extend(
        [f.relative_to(site_dir) for f in Path(site_dir).glob("**/image*.*")]
    )
    assert sorted(generate_site) == sorted(PLUGIN_USE_DIRECTORY_URLS)


def test_plugin_use_directory_urls_static_nav():
    mkdocs_config = load_config(
        "tests/mkdocs.yml",
        theme={"name": "mkdocs"},
        use_directory_urls=True,
        docs_dir="docs_suffix_structure/",
        plugins={
            "search": {},
            "i18n": {
                "default_language": "en",
                "languages": {"fr": "français", "en": "english"},
            },
        },
        nav=[
            {
                "Home": "index.md",
            }
        ],
    )
    build(mkdocs_config)
    site_dir = mkdocs_config["site_dir"]
    generate_site = [f.relative_to(site_dir) for f in Path(site_dir).glob("**/*.html")]
    generate_site.extend(
        [f.relative_to(site_dir) for f in Path(site_dir).glob("**/image*.*")]
    )
    assert sorted(generate_site) == sorted(PLUGIN_USE_DIRECTORY_URLS)


def test_plugin_use_directory_urls_per_folder():
    mkdocs_config = load_config(
        "tests/mkdocs.yml",
        theme={"name": "mkdocs"},
        use_directory_urls=True,
        docs_dir="docs_folder_structure/",
        plugins={
            "search": {},
            "i18n": {
                "default_language": "en",
                "docs_structure": "folder",
                "languages": {"fr": "français", "en": "english"},
            },
        },
    )
    build(mkdocs_config)
    site_dir = mkdocs_config["site_dir"]
    generate_site = [f.relative_to(site_dir) for f in Path(site_dir).glob("**/*.html")]
    generate_site.extend(
        [f.relative_to(site_dir) for f in Path(site_dir).glob("**/image*.*")]
    )
    assert sorted(generate_site) == sorted(PLUGIN_USE_DIRECTORY_URLS)


def test_plugin_use_directory_urls_per_folder_static_nav():
    mkdocs_config = load_config(
        "tests/mkdocs.yml",
        theme={"name": "mkdocs"},
        use_directory_urls=True,
        docs_dir="docs_folder_structure/",
        plugins={
            "search": {},
            "i18n": {
                "default_language": "en",
                "docs_structure": "folder",
                "languages": {"fr": "français", "en": "english"},
            },
        },
        nav=[
            {
                "Home": "index.md",
            }
        ],
    )
    build(mkdocs_config)
    site_dir = mkdocs_config["site_dir"]
    generate_site = [f.relative_to(site_dir) for f in Path(site_dir).glob("**/*.html")]
    generate_site.extend(
        [f.relative_to(site_dir) for f in Path(site_dir).glob("**/image*.*")]
    )
    assert sorted(generate_site) == sorted(PLUGIN_USE_DIRECTORY_URLS)


def test_plugin_no_use_directory_urls():
    mkdocs_config = load_config(
        "tests/mkdocs.yml",
        theme={"name": "mkdocs"},
        use_directory_urls=False,
        docs_dir="docs_suffix_structure/",
        plugins={
            "search": {},
            "i18n": {
                "default_language": "en",
                "languages": {"fr": "français", "en": "english"},
            },
        },
    )
    build(mkdocs_config)
    site_dir = mkdocs_config["site_dir"]
    generate_site = [f.relative_to(site_dir) for f in Path(site_dir).glob("**/*.html")]
    generate_site.extend(
        [f.relative_to(site_dir) for f in Path(site_dir).glob("**/image*.*")]
    )
    assert sorted(generate_site) == sorted(PLUGIN_NO_USE_DIRECTORY_URLS)


def test_plugin_no_use_directory_urls_per_folder():
    mkdocs_config = load_config(
        "tests/mkdocs.yml",
        theme={"name": "mkdocs"},
        use_directory_urls=False,
        docs_dir="docs_folder_structure/",
        plugins={
            "search": {},
            "i18n": {
                "default_language": "en",
                "docs_structure": "folder",
                "languages": {"fr": "français", "en": "english"},
            },
        },
    )
    build(mkdocs_config)
    site_dir = mkdocs_config["site_dir"]
    generate_site = [f.relative_to(site_dir) for f in Path(site_dir).glob("**/*.html")]
    generate_site.extend(
        [f.relative_to(site_dir) for f in Path(site_dir).glob("**/image*.*")]
    )
    assert sorted(generate_site) == sorted(PLUGIN_NO_USE_DIRECTORY_URLS)


PLUGIN_USE_DIRECTORY_URLS_NO_DEFAULT = [
    Path("404.html"),
    Path("image.png"),
    Path("image.fake"),
    Path("index.html"),
    Path("assets/image_non_localized.png"),
    Path("topic1/named_file/index.html"),
    Path("topic2/index.html"),
    Path("topic2/1.1.filename.html"),
    Path("fr/index.html"),
    Path("fr/image.png"),
    Path("fr/image.fake"),
    Path("fr/assets/image_non_localized.png"),
    Path("fr/topic1/named_file/index.html"),
    Path("fr/topic2/index.html"),
    Path("fr/topic2/1.1.filename.html"),
]
PLUGIN_NO_USE_DIRECTORY_URLS_NO_DEFAULT = [
    Path("404.html"),
    Path("image.png"),
    Path("image.fake"),
    Path("index.html"),
    Path("assets/image_non_localized.png"),
    Path("topic1/named_file.html"),
    Path("topic2/index.html"),
    Path("topic2/1.1.filename.html"),
    Path("fr/index.html"),
    Path("fr/image.png"),
    Path("fr/image.fake"),
    Path("fr/assets/image_non_localized.png"),
    Path("fr/topic1/named_file.html"),
    Path("fr/topic2/index.html"),
    Path("fr/topic2/1.1.filename.html"),
]


def test_plugin_use_directory_urls_no_default_language():
    mkdocs_config = load_config(
        "tests/mkdocs.yml",
        theme={"name": "mkdocs"},
        use_directory_urls=True,
        docs_dir="docs_suffix_structure/",
        plugins={
            "search": {},
            "i18n": {
                "default_language": "en",
                "languages": {"fr": "français"},
            },
        },
    )
    build(mkdocs_config)
    site_dir = mkdocs_config["site_dir"]
    generate_site = [f.relative_to(site_dir) for f in Path(site_dir).glob("**/*.html")]
    generate_site.extend(
        [f.relative_to(site_dir) for f in Path(site_dir).glob("**/image*.*")]
    )
    assert sorted(generate_site) == sorted(PLUGIN_USE_DIRECTORY_URLS_NO_DEFAULT)


def test_plugin_use_directory_urls_no_default_language_folder_structure():
    mkdocs_config = load_config(
        "tests/mkdocs.yml",
        theme={"name": "mkdocs"},
        use_directory_urls=True,
        docs_dir="docs_folder_structure/",
        plugins={
            "search": {},
            "i18n": {
                "default_language": "en",
                "docs_structure": "folder",
                "languages": {"fr": "français"},
            },
        },
    )
    build(mkdocs_config)
    site_dir = mkdocs_config["site_dir"]
    generate_site = [f.relative_to(site_dir) for f in Path(site_dir).glob("**/*.html")]
    generate_site.extend(
        [f.relative_to(site_dir) for f in Path(site_dir).glob("**/image*.*")]
    )
    assert sorted(generate_site) == sorted(PLUGIN_USE_DIRECTORY_URLS_NO_DEFAULT)


def test_plugin_no_use_directory_urls_no_default_language():
    mkdocs_config = load_config(
        "tests/mkdocs.yml",
        theme={"name": "mkdocs"},
        use_directory_urls=False,
        docs_dir="docs_suffix_structure/",
        plugins={
            "search": {},
            "i18n": {
                "default_language": "en",
                "languages": {"fr": "français"},
            },
        },
    )
    build(mkdocs_config)
    site_dir = mkdocs_config["site_dir"]
    generate_site = [f.relative_to(site_dir) for f in Path(site_dir).glob("**/*.html")]
    generate_site.extend(
        [f.relative_to(site_dir) for f in Path(site_dir).glob("**/image*.*")]
    )
    assert sorted(generate_site) == sorted(PLUGIN_NO_USE_DIRECTORY_URLS_NO_DEFAULT)


def test_plugin_no_use_directory_urls_no_default_language_folder_structure():
    mkdocs_config = load_config(
        "tests/mkdocs.yml",
        theme={"name": "mkdocs"},
        use_directory_urls=False,
        docs_dir="docs_folder_structure/",
        plugins={
            "search": {},
            "i18n": {
                "default_language": "en",
                "docs_structure": "folder",
                "languages": {"fr": "français"},
            },
        },
    )
    build(mkdocs_config)
    site_dir = mkdocs_config["site_dir"]
    generate_site = [f.relative_to(site_dir) for f in Path(site_dir).glob("**/*.html")]
    generate_site.extend(
        [f.relative_to(site_dir) for f in Path(site_dir).glob("**/image*.*")]
    )
    assert sorted(generate_site) == sorted(PLUGIN_NO_USE_DIRECTORY_URLS_NO_DEFAULT)


PLUGIN_USE_DIRECTORY_URLS_DEFAULT_ONLY = [
    Path("404.html"),
    Path("image.png"),
    Path("image.fake"),
    Path("index.html"),
    Path("assets/image_non_localized.png"),
    Path("topic1/named_file/index.html"),
    Path("topic2/index.html"),
    Path("topic2/1.1.filename.html"),
]
PLUGIN_NO_USE_DIRECTORY_URLS_DEFAULT_ONLY = [
    Path("404.html"),
    Path("image.png"),
    Path("image.fake"),
    Path("index.html"),
    Path("assets/image_non_localized.png"),
    Path("topic1/named_file.html"),
    Path("topic2/index.html"),
    Path("topic2/1.1.filename.html"),
]


def test_plugin_use_directory_urls_default_language_only():
    mkdocs_config = load_config(
        "tests/mkdocs.yml",
        theme={"name": "mkdocs"},
        use_directory_urls=True,
        docs_dir="docs_suffix_structure/",
        plugins={
            "search": {},
            "i18n": {
                "default_language_only": True,
                "default_language": "en",
                "languages": {"fr": "français", "en": "english"},
            },
        },
    )
    build(mkdocs_config)
    site_dir = mkdocs_config["site_dir"]
    generate_site = [f.relative_to(site_dir) for f in Path(site_dir).glob("**/*.html")]
    generate_site.extend(
        [f.relative_to(site_dir) for f in Path(site_dir).glob("**/image*.*")]
    )
    assert sorted(generate_site) == sorted(PLUGIN_USE_DIRECTORY_URLS_DEFAULT_ONLY)


def test_plugin_use_directory_urls_default_language_only_folder_structure():
    mkdocs_config = load_config(
        "tests/mkdocs.yml",
        theme={"name": "mkdocs"},
        use_directory_urls=True,
        docs_dir="docs_folder_structure/",
        plugins={
            "search": {},
            "i18n": {
                "default_language_only": True,
                "default_language": "en",
                "docs_structure": "folder",
                "languages": {"fr": "français", "en": "english"},
            },
        },
    )
    build(mkdocs_config)
    site_dir = mkdocs_config["site_dir"]
    generate_site = [f.relative_to(site_dir) for f in Path(site_dir).glob("**/*.html")]
    generate_site.extend(
        [f.relative_to(site_dir) for f in Path(site_dir).glob("**/image*.*")]
    )
    assert sorted(generate_site) == sorted(PLUGIN_USE_DIRECTORY_URLS_DEFAULT_ONLY)


def test_plugin_no_use_directory_urls_default_language_only():
    mkdocs_config = load_config(
        "tests/mkdocs.yml",
        theme={"name": "mkdocs"},
        use_directory_urls=False,
        docs_dir="docs_suffix_structure/",
        plugins={
            "search": {},
            "i18n": {
                "default_language_only": True,
                "default_language": "en",
                "languages": {"fr": "français", "en": "english"},
            },
        },
    )
    build(mkdocs_config)
    site_dir = mkdocs_config["site_dir"]
    generate_site = [f.relative_to(site_dir) for f in Path(site_dir).glob("**/*.html")]
    generate_site.extend(
        [f.relative_to(site_dir) for f in Path(site_dir).glob("**/image*.*")]
    )
    assert sorted(generate_site) == sorted(PLUGIN_NO_USE_DIRECTORY_URLS_DEFAULT_ONLY)


def test_plugin_no_use_directory_urls_default_language_only_folder_structure():
    mkdocs_config = load_config(
        "tests/mkdocs.yml",
        theme={"name": "mkdocs"},
        use_directory_urls=False,
        docs_dir="docs_folder_structure/",
        plugins={
            "search": {},
            "i18n": {
                "default_language_only": True,
                "default_language": "en",
                "docs_structure": "folder",
                "languages": {"fr": "français", "en": "english"},
            },
        },
    )
    build(mkdocs_config)
    site_dir = mkdocs_config["site_dir"]
    generate_site = [f.relative_to(site_dir) for f in Path(site_dir).glob("**/*.html")]
    generate_site.extend(
        [f.relative_to(site_dir) for f in Path(site_dir).glob("**/image*.*")]
    )
    assert sorted(generate_site) == sorted(PLUGIN_NO_USE_DIRECTORY_URLS_DEFAULT_ONLY)
