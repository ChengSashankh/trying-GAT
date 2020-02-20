import random

# Now we perform the train-test-val split
indices = list(range(10))
random.shuffle(indices)
print(indices)
train_ratio = 0.7
val_ratio = 0.1
test_ratio = 0.2

assert(train_ratio + val_ratio + test_ratio == 1.0)

total_elements = len(indices)

train_indices = indices[0: int(train_ratio * total_elements)]
print(train_indices)
indices = indices[int(train_ratio * total_elements):]
val_indices = indices[0: int(val_ratio * total_elements)]
print(val_indices)
indices = indices[int(val_ratio * total_elements):]
test_indices = indices
print(test_indices)

# Code for creating the mask
# Not required - mask is created above in using code from other fn

# train_mask = [0 for i in range(total_elements)]
# val_mask = [0 for i in range(total_elements)]
# test_mask = [0 for i in range(total_elements)]
#
# # Set the masks
# for i in train_indices:
#     train_mask[i] = 1
#
# for i in test_indices:
#     test_mask[i] = 1
#
# for i in val_indices:
#     val_mask[i] = 1