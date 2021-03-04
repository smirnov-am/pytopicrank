from setuptools import setup, find_packages

setup(name='pytopicrank',
      version='0.3.2',
      description='Implementation of TopicRank algorithm for keyphrase extraction from text',
      url='https://github.com/smirnov-am/pytopicrank',
      author='Alexey Smirnov',
      author_email='msc.smirnov.am@gmail.com',
      license='MIT',
      install_requires=['decorator==4.2.1',
                        'langdetect==1.0.7', 'networkx==2.1', 'nltk==3.2.5',
                        'numpy', 'scikit-learn==0.19.1', 'scipy==1.0.0', 'six==1.11.0'],
      packages=['pytopicrank'])
