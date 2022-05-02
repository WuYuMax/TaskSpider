import setuptools


with open("README.md", "r",encoding='utf-8') as fh:
  long_description = fh.read()

setuptools.setup(
  name="TaskSpider",
  version="0.0.2",
  author="WuYuMax",
  author_email="332062922@qq.com",
  description="A framework which can help you make your webspider more OOP and easy",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/WuYuMax/TaskSpider",
  packages=setuptools.find_packages(),
  classifiers=[
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: Apache Software License",
  "Operating System :: OS Independent",
  ],
)
