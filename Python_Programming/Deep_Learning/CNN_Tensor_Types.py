import tensorflow as tf

scaler_tensor = tf.constant(11)
print("Scalar tensor : ",scaler_tensor)

vector_tensor = tf.constant([11,21,51,101])
print("Vector tensor : ",vector_tensor)

matrix_tensor = tf.constant([[10,20,30],[40,50,60]])
print("Matrix tensor: ",matrix_tensor)

tensor_3D  = tf.constant([
    [[1,2],[3,4]],
    [[5,5],[6,6]],
    [[9,10],[11,12]]
])
print("3D Matrix : ",tensor_3D)