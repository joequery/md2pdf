from setuptools import setup
import os, shutil

setup(name='md2pdf',
      version='1.0',
      description='Markdown to PDF converter',
      author='Joseph McCullough',
      author_email='joseph@vertstudios.com',
	  install_requires=['markdown2', 'xhtml2pdf'],
      scripts=['md2pdf']
     )
