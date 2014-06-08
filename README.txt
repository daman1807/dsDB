The module focuses on storing data at multiple locations using permutation and combination so that it can be easily called on when search is initialized.
If store record in data system it will automatically generate its search patterns and will then save it according to the patterns so as to save time when a search query is initialized

For example if your record contains string – ‘India’, then its possible search patterns will be ( I , IN , IND , INDI , INDIA , N , ND, NDI , NDIA , D , DI , DIA , I , IA , A) . All of the above mentioned patterns will have the record – ‘India’ in it.

The module have four main methods – path() , db() , insert() , search() , searchColumn() , delete() , deleteColumn() , update() .The methods are discussed in detail in ‘methods.txt’ and two properties - File and columns.

The file 'ds.py' is the module file and 'ds.pyc' is complied fiel of the module
Just copy and paste them to 'Lib' folder of your pythoon directory.





