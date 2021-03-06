from cx_Freeze import setup, Executable


readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

include_files = []
includes = [
    # os.environ["DJANGO_SETTINGS_MODULE"], #rootapp
    "PyQt4.QtCore",
    'atexit',
    'clip_trans.clip_trans_ui',
]
exclude_files = []
build_exe_dir = "build/"
zip_includes = []
final_script_list = [Executable(script='clip_trans/clip_trans_app.py',
                                base='Win32GUI'
)]

build_exe_params = {
    "includes": includes,
    'include_files': include_files,
    "bin_excludes": exclude_files,
    "build_exe": build_exe_dir,
    "zip_includes": zip_includes,
    # "packages": find_packages(),
    #"create_shared_zip": False,
}

setup(
    name='clip_trans',
    version='0.1.0',
    description='"Clipboard Transformer transform the content in clipboard to new content according to certain script"',
    long_description=readme + '\n\n' + history,
    author='Richard Wang',
    author_email='richardwangwang@gmail.com',
    url='https://github.com/weijia/clip_trans',
    packages=[
        'clip_trans',
    ],
    package_dir={'clip_trans':
                     'clip_trans'},
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='clip_trans',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    options={"build_exe": build_exe_params},
    executables=final_script_list,
)