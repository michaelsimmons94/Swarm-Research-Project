# Swarm-Research-Project

## Summary

A model that compares two types of swarms. The first swarms uses basic heuristics to distribute itself across an area. The other swarm mimics root growth. This is built ontop of the Project Mesa framework https://github.com/projectmesa/mesa.

## How to Run


To launch an interactive server where you can modify inidividual parameters
run:

```
    $ python run.py
```

If your browser doesn't open automatically, point it to [http://127.0.0.1:8521/](http://127.0.0.1:8521/). When the visualization loads, press Reset, then Run.

To do data analysis run:
```
    $ jupyter notebook
```


## Files

* ``Swarm Data Analysis.ipynb``: Jupyter Notebook with the model and commands to recreate the data.
* ``run.py``: initializes the interactive server.
* ``model.py``: Contains the model.

## Notes

Anaconda and mesa will need to be installed for this to run.
To install mesa run the command:
```
    $ pip install mesa
```
