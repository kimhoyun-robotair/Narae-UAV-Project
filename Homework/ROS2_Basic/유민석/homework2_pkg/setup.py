from setuptools import setup

package_name = 'homework2_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    py_modules=[
        package_name + '.hello_publisher',
        package_name + '.hello_subscriber',
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='mindol',
    maintainer_email='mindol@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'publisher = homework2_pkg.hello_publisher:main',
            'subscriber = homework2_pkg.hello_subscriber:main',
        ],
    },
)
