```python3 program.py <case> <image_path>```
-  case
    -  ```0``` means provide ```image_path``` as the path where our incomplete image is there
    - ```1``` means provide ```image_path``` of colored image which we will split into three channels, apply py to get thier npy, reconstruct, then combine
    - output image will be in ```Reconstructed``` folder 
- line 9 of ```program.py``` contains the ```zoom``` and ```corruption``` level. Modify Accordingly
- ```our_data/R/s_vec.npy``` contains ```s``` vector found by <b>convex minimisation</b> for RED Channel and 
- ```our_data/G/s_vec.npy``` contains ```s``` vector found by <b>convex minimisation</b> for GREEN Channel and 
- ```our_data/B/s_vec.npy``` contains ```s``` vector found by <b>convex minimisation</b> for BLUE Channel and 