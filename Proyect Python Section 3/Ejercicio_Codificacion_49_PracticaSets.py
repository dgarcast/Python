"""  

Une los siguientes sets en uno solo, llamado mi_set_3:

{1, 2, "tres", "cuatro"}

{"tres", 4, 5}

"""


mi_set = {1,2,"tres","cuatro"}
mi_set2 = {"tres",4,5}

mi_set_3 = mi_set.union(mi_set2)
print(mi_set_3)