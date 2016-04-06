## Data Source
https://data.kpu.go.id/dps.php

### Run
```python name.py test_file.input result.csv```


### Input File

Multiple name, seperate by new line

```
Devita Pearce
Muhammad Hatta
Ridwan Kamil
```


### Result file

Result will be write in csv

| Tested_Name | Predicted_Gender | Female_Score | Male_Score | Percentage |
| --- | --- | --- | --- | --- |
| 'Devita Pearce' | f | 35 | 0 | 1.0 |
| 'Muhammad Hatta' | m | 11 | 101 | 0.901785714286 |
| 'Ridwan Kamil' | m | 14 | 73 | 0.83908045977 |
