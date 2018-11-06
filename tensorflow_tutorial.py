import tensorflow as tf
#print(tf.__version__)

x1 = tf.constant(1, name = 'constant_x1')

x2 = tf.constant(4, name = 'constant_x2')

v1 = tf.constant([2, 4, 5], dtype = tf.float32, name = 'constant_vec1')
v2 = tf.constant([3, 6, 1], dtype = tf.float32, name = 'constant_vec1')

sess = tf.Session()
y = x1 + x2
print(sess.run(y))