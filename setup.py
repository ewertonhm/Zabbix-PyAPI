from distutils.core import setup
setup(
    name='Zabbix_PyAPI',
    packages=['Zabbix_PyAPI'],
    version='0.1',
    license='MIT',
    description='Simple zabbix api using python',
    author='Ewerton Henrique Marschalk',
    author_email='sis-ewertonmarschalk@uniguacu.edu.br',      # Type in your E-Mail
    # Provide either the link to your github or to your website
    url='https://github.com/ewertonhm/Zabbix-PyAPI',
    # I explain this later on
    download_url='https://github.com/ewertonhm/Zabbix-PyAPI/archive/refs/tags/0.1.tar.gz',
    # Keywords that define your package best
    keywords=['ZABBIX', 'API'],
    install_requires=[            # I get to this in a second
        'requests'
    ],
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Development Status :: 3 - Alpha',
        # Define that your audience are developers
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',   # Again, pick a license
        # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
