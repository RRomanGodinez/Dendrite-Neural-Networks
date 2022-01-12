from setuptools import setup
from setuptools import find_packages

with open("README.md","r") as fh:
    long_description = fh.read()

setup(
    name = 'Dendrite Neural Networks',
    version = '0.0.1',
    description = 'Dendrite-Neural-Networks is an implementation of processing units that performed classification using closed decision boundaries with only one neuron.',
    py_modules = ["DMN","DEN","DSN","PreTrain.HpC.HBpC","PreTrain.HpC.HEpC","PreTrain.HpC.HSpC", "PreTrain.kmeans.bkmeans","PreTrain.kmeans.ekmeans","PreTrain.kmeans.skmeans"],
    packages = find_packages(),
    package_dir = {'':'src'},
      
    lons_description = long_description,
    long_description_content_type = "text/markdown",
    
    install_requires = ["Keras  ∼= 2.4.3",
                        "Tensorflow ∼= 2.3",
                        "Numpy ∼= 1.20.1",
                        "Scikit-learn ∼= 0.24.1"],
    url = "",
    author = "Rodrigo Román Godínez.",
    author_email = "rodrigo_0045@hotmail.com, rodrigo0045@gmail.com",
    
)