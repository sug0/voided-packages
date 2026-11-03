from pathlib import Path
from setuptools import find_packages, setup

readme_path = Path(__file__).parent / "README.md"
long_description = (
    readme_path.read_text(encoding="utf-8") if readme_path.exists() else ""
)

setup(
    name="python-libei",
    version="0.8.0",
    description=(
        "Inject, receive and capture input on Wayland from Python: ctypes bindings "
        "for libei, libeis and liboeffis, plus the RemoteDesktop and InputCapture portals"
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Dennis K. Paulsen",
    license="MIT",
    python_requires=">=3.10",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    package_data={
        "libei": ["py.typed"],
    },
    install_requires=[],
    extras_require={
        "portal": ["PyGObject>=3.42"],
        "dev": ["pytest>=7", "ruff>=0.6", "mypy>=1.11"],
    },
    keywords=[
        "wayland",
        "libei",
        "libeis",
        "liboeffis",
        "input",
        "input-emulation",
        "emulated-input",
        "input-capture",
        "eis",
        "portal",
        "xdg-desktop-portal",
        "remote-desktop",
        "automation",
        "gui-testing",
        "accessibility",
        "ctypes",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Operating System :: POSIX :: BSD :: FreeBSD",
        "Operating System :: POSIX :: Linux",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Topic :: Desktop Environment",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Testing",
        "Typing :: Typed",
    ],
    project_urls={
        "Homepage": "https://github.com/ctrondlp/python-libei",
        "Repository": "https://github.com/ctrondlp/python-libei",
        "Issues": "https://github.com/ctrondlp/python-libei/issues",
        "Documentation": "https://github.com/ctrondlp/python-libei/tree/main/docs",
        "pyguitest": "https://github.com/ctrondlp/pyguitest",
        "Changelog": "https://github.com/ctrondlp/python-libei/blob/main/CHANGELOG.md",
    },
)
