# Iterum Client Libraries

Iterum allows for the creation of client libraries for different languages. These client libraries, together with the sidecars function as a layer of abstraction between the framework and the transformation step as shown in the following image:

![abstraction](images/abstraction.png)


In this way, the transformation step does not have to concern itself with the communication with the framework, and can focus on the actual transformation step.


### Current client library implementations

* [Pyterum](https://github.com/iterum-provenance/pyterum), Python library


## Some elements of any complete library
* An implementation of the communication protocol described defined in the [transmit package](https://github.com/iterum-provenance/iterum-go/tree/master/transmit) This is the communication protocol used and so sending and receiving should happen in this manner. This includes reading and writing from `.socket` files. 
* Data send in this manner can be parsed as JSON but should follow certain structures. The main types are: KillMessage, DoneWith and LocalFragmentDesc. 
  Specifications of these types can be found in the [descriptors package](https://github.com/iterum-provenance/iterum-go/tree/master/descriptors) and an example implementation for python is available in [Pyterum](https://github.com/iterum-provenance/pyterum). 
* From Pyterum also the `env.py` and `config.py` should be considered in order to grasp what kind of variables are passed to transformation steps and how configuration options specified in the pipeline definitions can be accessed. The rest of the Pyterum package is mostly used to add some user friendliness and to ease the work of users. 