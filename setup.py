from setuptools import setup
from setuptools import find_packages

with open("README.md","r") as fh:
    long_description = fh.read()

setup(
    name = 'Dendrite Neural Networks',
    version = '0.0.9',
    description = 'Dendrite-Neural-Networks is an implementation of processing units that performed classification using closed decision boundaries.',
    py_modules = ["DMN","DEN","DSN","PreTrain.HpC.HBpC","PreTrain.HpC.HEpC","PreTrain.HpC.HSpC", "PreTrain.kmeans.bkmeans","PreTrain.kmeans.ekmeans","PreTrain.kmeans.skmeans"],
    packages = find_packages(),
    package_dir = {'':'src'},
      
    long_description = long_description,
    long_description_content_type = "text/markdown",
    
    install_requires = ['Keras>=2.6',
                        "Tensorflow >= 2.9.1",
                        "Numpy >= 1.19.5",
                        "Scikit-learn >= 1.0.2"
                       ],
    url = "https://github.com/RRomanGodinez/Dendrite-Neural-Networks",
    author = "Rodrigo Román Godínez.",
    author_email = "rodrigo_0045@hotmail.com, rodrigo0045@gmail.com",
    
)
