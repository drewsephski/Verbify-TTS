from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()


VERSION = "0.0.1"


setup(
    name='verbify-tts',
    version=VERSION,
    description='A text-to-speech service free and for everyone',
    author='Matteo Paltenghi',
    author_email="mattepalte@live.it",
    url='https://github.com/MattePalte/Verbify-TTS',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        # REST API
        'fastapi==0.95.1',
        'uvicorn==0.21.1',
        # MODELING
        'torch==2.0.0',
        'transformers==4.38.2',
        'omegaconf==2.0.6',
        'packaging==23.1',
        'PyYAML==6.0',
        'fairseq==0.12.2',
        'g2p-en==2.1.0',
        # TEXT PREPROCESSING
        'pandas==2.0.0',
        'numpy==1.23.0',
        'PyAutoGUI==0.9.53',
        # AUDIO
        'pygame==2.3.0',
        'sox==1.4.1',
        'soundfile==0.12.1',
        'scipy==1.10.1',
    ],
    packages=[
        'verbify_tts',
        'verbify_tts.services',
        'verbify_tts.actuators',
    ],
    package_data={
        'verbify_tts': [
            'configuration/*.ahk',
            'configuration/config.yaml',
            'configuration/idioms.csv'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    license="MIT",
    # extra requirements
    extras_require={
        'dev': [
            'pytest',
            'pytest-cov',
            'flake8',
            'twine',
            'wheel',
        ]
    },
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'verbify_server = verbify_tts.services.tts:main',
            'verbify_read_selected = verbify_tts.actuators.command_read:command_speak_selection',
            'verbify_stop_tts = verbify_tts.actuators.command_stop:command_stop',
        ],
    },
)
