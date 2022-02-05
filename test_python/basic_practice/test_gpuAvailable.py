# tensorflow import
import tensorflow as tf
# GPU 감지여부 및  사용가능한 GPU개수
print('Num GPUs Available : ', len(tf.config.experimental.list_physical_devices('GPU')))



