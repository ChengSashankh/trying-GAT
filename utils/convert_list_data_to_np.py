import pickle as pkl
import numpy as np

# Convert labels
labels = pkl.load(
        open('/Users/cksash/Documents/FYP-holidays/fyp-main/data/joined_labels.pkl', 'rb')
    )

labels_one_hot = np.zeros((len(labels), 2))

for idx, l in enumerate(labels):
    labels_one_hot[idx][int(l)] = 1.0

# Check if same number of 1s and zeros after conversion
assert(sum(labels) == np.sum(labels_one_hot[:, 1]))

pkl.dump(labels_one_hot, open('/Users/cksash/Documents/FYP-holidays/fyp-main/data/labels_one_hot.pkl', 'wb'))

## Not required. They are already np arrays
# Convert node vectors
# node_vec = pkl.load(
#         open('/Users/cksash/Documents/FYP-holidays/fyp-main/data/joined_node_vec.pkl', 'rb')
#     )
#
# node_vec_np = np.zeros((len(node_vec), len(node_vec[0])))
#
# for idx in range(len(node_vec)):
#     node_vec_np[idx, :] = node_vec[idx, :]
#
#     assert(sum(node_vec[idx]) == np.sum(node_vec_np[idx]))
#
# pkl.dump(node_vec_np, open('/Users/cksash/Documents/FYP-holidays/fyp-main/data/node_vec_np.pkl', 'wb'))
