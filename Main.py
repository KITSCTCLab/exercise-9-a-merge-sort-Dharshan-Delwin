from typing import List

def merge_sort(data) -> None:
  if(lb<ub):
     mid = lb+ub/2
      merge_sort(data,lb,mid)
      mrge_sort(data,mid+1,ub)
      Merge(lb,mid,ub)


# Do not change the following code
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
merge_sort(data)
print(data)
