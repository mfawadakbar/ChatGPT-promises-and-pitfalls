grep --recursive -l {ROOT_DIR} | xargs -i sed '0,/```python/d;/```/,$d'
