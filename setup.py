from setuptools import setup, find_packages

setup(
    name='llt',  # Замените на имя вашего пакета
    version='0.1.0',  # Замените на текущую версию вашего пакета
    author='mssnskyi',  # Ваше имя
    author_email='_',  # Ваш email
    description='low and high level tools API',  # Краткое описание вашего пакета
    long_description=open('README.md').read(),  # Длинное описание, прочитанное из файла README.md
    long_description_content_type='text/markdown',  # Тип содержимого длинного описания
    url='https://github.com/yourusername/yourreponame',  # URL репозитория вашего проекта
    packages=find_packages(),  # Автоматический поиск всех пакетов и под-пакетов
    classifiers=[
        'Programming Language :: Python :: 3',  # Классификатор языка программирования
        'License :: OSI Approved :: MIT License',  # Классификатор лицензии
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Минимальная требуемая версия Python
    install_requires=[
        # Список зависимостей, например:
        # 'requests>=2.23.0',
        # 'numpy>=1.18.1',
    ],
    entry_points={
        'console_scripts': [
            # Создание исполняемых скриптов, например:
            # 'your_command=your_package.module:function',
        ],
    },
)
