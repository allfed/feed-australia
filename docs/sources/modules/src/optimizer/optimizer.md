#


## Optimizer
[source](https://github.com/allfed/allfed-integrated-model/blob/master/src/optimizer/optimizer.py/#L10)
```python 

```




**Methods:**


### .optimize
[source](https://github.com/allfed/allfed-integrated-model/blob/master/src/optimizer/optimizer.py/#L14)
```python
.optimize(
   single_valued_constants, multi_valued_constants
)
```


### .second_optimization_smoothing
[source](https://github.com/allfed/allfed-integrated-model/blob/master/src/optimizer/optimizer.py/#L105)
```python
.second_optimization_smoothing(
   model, variables, NMONTHS, ASSERT_SUCCESSFUL_OPTIMIZATION,
   single_valued_constants
)
```

---
in this case we are trying to get the differences between all the variables
to be the
smallest, without causing the optimization to fail.

### .add_seaweed_to_model
[source](https://github.com/allfed/allfed-integrated-model/blob/master/src/optimizer/optimizer.py/#L217)
```python
.add_seaweed_to_model(
   model, variables, month
)
```


### .add_stored_food_to_model_only_first_year
[source](https://github.com/allfed/allfed-integrated-model/blob/master/src/optimizer/optimizer.py/#L280)
```python
.add_stored_food_to_model_only_first_year(
   model, variables, month
)
```


### .add_stored_food_to_model
[source](https://github.com/allfed/allfed-integrated-model/blob/master/src/optimizer/optimizer.py/#L337)
```python
.add_stored_food_to_model(
   model, variables, month
)
```


### .add_culled_meat_to_model
[source](https://github.com/allfed/allfed-integrated-model/blob/master/src/optimizer/optimizer.py/#L395)
```python
.add_culled_meat_to_model(
   model, variables, month
)
```

---
incorporate linear constraints for culled meat consumption each month
it's like stored food, but there is a preset limit for how much can be produced

### .add_outdoor_crops_to_model_no_relocation
[source](https://github.com/allfed/allfed-integrated-model/blob/master/src/optimizer/optimizer.py/#L451)
```python
.add_outdoor_crops_to_model_no_relocation(
   model, variables, month
)
```


### .add_outdoor_crops_to_model_no_storage
[source](https://github.com/allfed/allfed-integrated-model/blob/master/src/optimizer/optimizer.py/#L501)
```python
.add_outdoor_crops_to_model_no_storage(
   model, variables, month
)
```


### .add_outdoor_crops_to_model
[source](https://github.com/allfed/allfed-integrated-model/blob/master/src/optimizer/optimizer.py/#L546)
```python
.add_outdoor_crops_to_model(
   model, variables, month
)
```


### .add_objectives_to_model
[source](https://github.com/allfed/allfed-integrated-model/blob/master/src/optimizer/optimizer.py/#L677)
```python
.add_objectives_to_model(
   model, variables, month, maximize_constraints
)
```

